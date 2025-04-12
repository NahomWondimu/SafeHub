from django.http import HttpResponse
import pandas as pd
from django.shortcuts import render
from django.template import loader
from .virusTotalChecker import *
from datetime import datetime
from .models import WebPage  # Import the model
from django.views.decorators.http import require_POST


# Create your views here.
# Note that repeated site links should not be accepted. Check DB.
def Web_Analysis(request):
    template = loader.get_template('testProcess.html')
    return HttpResponse(template.render())

@require_POST
def process_data(request):
    if request.method == "POST":
        urlToCheck = request.POST.get("addressToTest")
        if urlToCheck:
            urlToCheck = urlToCheck.strip()
            print(f"URL to check: {urlToCheck}")
            try:
                result = urlReport(urlToCheck)
                print("Got back from report")
                resultTemplate = loader.get_template('results.html')
                new_entry = WebPage(
                    url=result["url"],
                    community_score=result["community_score"],
                    last_analysis_date=result["last_analysis_date"],
                    last_analysis_stats=result["last_analysis_stats"],
                    redirection_chain=result["redirection_chain"],
                    reputation=result["reputation"],
                    times_submitted=result["times_submitted"],
                    tld=result["tld"],
                    virustotal_report=result["virustotal_report"],
                    time_entered=datetime.now().time()
                )
                new_entry.save()
                print("Entry saved to database:", new_entry)
                resultContext = {'myResults': new_entry}
                return HttpResponse(resultTemplate.render(resultContext))
            except Exception as e:
                print(f"Error occurred: {e}")
                errorContext = {'errorType': 'Error processing URL.'}
                errorTemp = loader.get_template('error.html')
                return HttpResponse(errorTemp.render(errorContext))
        else:
            errorType = 'No data passed.'
    else:
        errorType = 'Invalid Request Made.'

    errorContext = {'errorType': errorType}
    errorTemp = loader.get_template('error.html')
    return HttpResponse(errorTemp.render(errorContext))
