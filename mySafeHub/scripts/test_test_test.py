from virusTotalChecker import urlReport  

# Example usage
def test_urlReport():
    test_url = "http://maliciouswebsitetest.com/"  # Replace with a sample URL you want to test.
    try:
        urlReport(test_url)
        print("Function executed successfully. Check the output for results.")
    except Exception as e:
        print(f"Function encountered an error: {e}")

if __name__ == "__main__":
    test_urlReport()
