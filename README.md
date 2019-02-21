# GATE Cloud API Python Example

This is a brief example of using the GATE Cloud on-line API
using the `requests` library in Python.

If you just want to see the code, it's [`annie.py`](blob/master/annie.py).

To run the code you'll need
Python 3 and the [`requests` library](https://pypi.org/project/requests/).

## Install using `conda`

If you have `conda`,
you can create a new environment with Python 3 and `requests` like this:

    conda create --name gate-cloud-example python=3 requests

activate it:

    conda activate gate-cloud-example

## Install using `pip`

If you already use Python and `pip` then, as an alternative to using `conda`,
you can install the dependencies using:

    pip install -r requirements.txt

## Running it

Run the script:

    python annie.py Hieronymus Bosch was a Dutch painter from Brabant, born in 1450

When successful, the script will
print a formatted version of the JSON result it obtains from the GATE Cloud web service; and,
the parts of the text that correspond to annotations that ANNIE found.

The above example will output some JSON that only a web programmer can love, followed by:

    Date : 1450
    Location : Brabant
    Person : Hieronymus Bosch

## Quota

GATE Cloud has a quota for API calls; if you use an API key quota is increased.
You can generate new API keys by logging into your GATE Cloud account,
and visiting the [API Key page](https://cloud.gate.ac.uk/yourAccount/apiKeys).

The `requests` library will use credentials in your [`.netrc`](https://ec.haxx.se/usingcurl-netrc.html) file.
So put them in like this:

    machine cloud-api.gate.ac.uk
    login 71rs93h36m0c
    password 9u8ki81lstfc2z8qjlae


###

Refer to documentation here: https://cloud.gate.ac.uk/info/help/online-api.html

and api browser here:
https://cloud.gate.ac.uk/shopfront/displayItem/annie-named-entity-recognizer?fromApi=1

requests make this really easy
Need to set content-type


or twitie

Accept
Expect: 100?

