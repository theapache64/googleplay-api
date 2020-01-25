from gpapi.googleplay import GooglePlayAPI, RequestError

import sys
import os

gsfId = int(os.environ["GPAPI_GSFID"])
authSubToken = os.environ["GPAPI_TOKEN"]

server = GooglePlayAPI("en_US", "UTC")
print("Logging in...")
server.login(None, None, gsfId, authSubToken)

packageName = sys.argv[1]
print('Downloading APK for ' + packageName)

fl = server.download(packageName)
with open(packageName + ".apk", "wb") as apk_file:
    for chunk in fl.get("file").get("data"):
        apk_file.write(chunk)
    print("\nDownload successful\n")

