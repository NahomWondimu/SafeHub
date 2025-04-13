from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from datetime import datetime
from .tempScript import analyze_data
from .models import Network
from django.views.decorators.http import require_POST
# Note that repeated site links should not be accepted. Check DB.

# Create your views here.
def Net_Analysis(request):
    template = loader.get_template('net.html')
    return HttpResponse(template.render())

# if returned data 'has' "Error", send up error message.
@require_POST
def process_data(request):
    if request.method == "POST":
        data = request.POST.get("networkInfo")
        if data:    # if data passed successfully.
            result = analyze_data(data)
            resultTemplate = loader.get_template('results.html')

            # get time
            currentTime = datetime.now()  # Current datetime
            formattedTime = currentTime.time()

            new_entry = Network(
                placeHolder=result,
                time_entered=formattedTime,
            )

            resultContext = {
                'myResults' : new_entry
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