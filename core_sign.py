 # -*- coding: utf-8 -*
import sys
import os

sign_tool_path=os.path.split(os.path.realpath(__file__))[0]

if len(sys.argv) <2:
	print('Usage: python core_sign.py [Apk/Dex filepath]')
else:
	file_path = sys.argv[1]
	apk_signed_path = file_path[0:file_path.index(".")]+"_signed.apk"
	
	print("apk sign will process:"+file_path)
	#反编译apk
	if "apk" in file_path:
		print("sign apk:" + file_path)
		#jarsigner -verbose -keystore test.keystore -signedjar signed.apk unsigned.apk 'test'
		#os.system("{}/apktool.sh d {} -o {} -f".format(decompile_lib, file_path, apk_decompile_path))
		os.system("jarsigner -verbose -keystore {}/test.keystore -signedjar  {} {} 'test'".format(sign_tool_path, apk_signed_path, file_path))
		print ("sign end")

