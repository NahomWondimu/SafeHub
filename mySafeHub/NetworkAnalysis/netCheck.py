#!usr/bin/env python3
import nmap
import subprocess
import os
import pandas as pd
import netifaces
import netdiscover
from scapy.all import sniff
from datetime import datetime
import subprocess
import json
import time
import signal

import subprocess
import time

def getNetworkDevices(runtime=10):
    try:
        process = subprocess.Popen(
            ["bettercap", "-no-colors", "-iface", "en0", "-eval",
             "net.probe on; sleep 5; net.show; net.probe off; quit"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        stdout, stderr = process.communicate(timeout=15)

        devices = []
        in_table = False
        
        for line in stdout.splitlines():
            # Skip all lines starting with [ until we find the table
            if not in_table:
                if line.startswith('┌─'):
                    in_table = True
                    continue  # Skip the top border line
                elif line.startswith('['):
                    continue  # Skip other log lines
                else:
                    continue  # Skip everything before table

            # Process table lines
            if in_table:
                # Stop when we hit empty line after table
                if not line.strip():
                    break
                
                # Skip middle border lines (├─...┤) and header line
                if any(c in line for c in ['├─', '┤', 'IP Address']):
                    continue
                
                # Split and clean table row
                parts = [p.strip() for p in line.split('│') if p.strip()]
                
                if len(parts) >= 4:
                    devices.append({
                        "IP Address": parts[0],
                        "MAC Address": parts[1],
                        "Manufacturer": parts[2],
                        "Host Name": parts[3]
                    })

        return devices

    except subprocess.TimeoutExpired:
        process.kill()
        print("Process timed out")
        return []
    except Exception as e:
        print(f"Error: {str(e)}")
        return []
    
def capture_packets():
    """
    Capture network packets and return a DataFrame containing their details.
    """
    packets_data = []

    def packet_callback(packet):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if packet.haslayer('IP'):
            ip_src = packet['IP'].src
            ip_dst = packet['IP'].dst
            protocol = packet.proto
            src_port = dst_port = None

            if packet.haslayer('TCP'):
                src_port = packet['TCP'].sport
                dst_port = packet['TCP'].dport

            elif packet.haslayer('UDP'):
                src_port = packet['UDP'].sport
                dst_port = packet['UDP'].dport

            packet_summary = packet.summary()

            packets_data.append({
                'Timestamp': timestamp,
                'Source IP': ip_src,
                'Destination IP': ip_dst,
                'Protocol': protocol,
                'Source Port': src_port,
                'Destination Port': dst_port,
                'Packet Summary': packet_summary
            })

    sniff(prn=packet_callback, store=0, timeout=5)  # Sniff packets for 10 seconds (adjust as needed)

    return pd.DataFrame(packets_data)

def portscanner():
    
    nm = nmap.PortScanner()
    nm.scan('127.0.0.1', '0-1023')

    hostState = nm['127.0.0.1'].state()
       
    protos = nm['127.0.0.1'].all_protocols() 
    portList = nm['127.0.0.1']['tcp'].keys()

    for port in portList:
        if nm['127.0.0.1'].has_tcp(port):
            proto = 'tcp'
        else:
            continue
        df = pd.DataFrame({
            'port': port,
            'tcpProtocol': proto,
            'portInfo': nm['127.0.0.1'][proto][port],
            'portState': nm['127.0.0.1'][proto][port]['state'],
            })

    print(df)
    return df

# Helper method
def get_default_gateway_ip():
    gws = netifaces.gateways()
    if 'default' in gws and netifaces.AF_INET in gws['default']:
        return gws['default'][netifaces.AF_INET][0]
    return None

def gatewayScanner():
    scanner = nmap.PortScanner()

    # Define target IP address or hostname
    target = get_default_gateway_ip()
    if target is None:
        return "Error"

    scanner.scan(target, arguments='-sn')   # No port scanning. We just want gateway.
    

    dataGathered = {
        'host': target,
        'state': scanner[target].state(),
    }

    return dataGathered