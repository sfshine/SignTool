jarsigner -verbose -keystore test.keystore -signedjar signed.apk unsigned.apk 'test'
adb install -r signed.apk