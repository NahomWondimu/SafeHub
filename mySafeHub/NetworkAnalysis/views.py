from django.http import HttpResponse
from django.template import loader
# Note that repeated site links should not be accepted. Check DB.


from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from scripts.tempScript import analyze_data
from datetime import datetime
from .models import WebPage  # Import the model
from django.views.decorators.http import require_POST


# Create your views here.
def Net_Analysis(request):
    template = loader.get_template('net.html')
    return HttpResponse(template.render())

@require_POST
def process_data(request):
    if request.method == "POST":
        data = request.POST.get("data")
        if data:    # if data passed successfully.
            result = analyze_data(data)
            resultTemplate = loader.get_template('results.html')

            # get time
            currentTime = datetime.now()  # Current datetime
            formattedTime = currentTime.time()

            new_entry = WebPage(
                placeHolder=result,
                time_entered=formattedTime,
            )

            resultContext = {
                'myResults' : new_entry,
            }

            new_entry.save()
            print("Entry saved to database:", new_entry)
            return HttpResponse(resultTemplate.render(resultContext))
        else:
            errorType = 'No data passed.'
    else:
        errorType = 'Invalid Request Made.'

    errorContext = {
        'errorType': errorType,
    }
    errorTemp = loader.get_template('error.html')
    return HttpResponse(errorTemp.render(errorContext))