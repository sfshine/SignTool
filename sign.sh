#jarsigner -verbose -keystore test.keystore -signedjar signed.apk unsigned.apk 'test'
TOOL_HOME=~/Soft/Android/SignTool
python ${TOOL_HOME}/core_sign.py $1

