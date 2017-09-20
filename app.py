import httplib
import urllib
import base64

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'ccec1dd9d05d491694d7c535167f9f1b'
}

params = urllib.urlencode({

})

try:
    with open("emotionsample.jpeg", "rb") as f:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request('POST', '/emotion/v1.0/recognize?%s' % params, f, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

# https://westus.api.cognitive.microsoft.com/emotion/v1.0
