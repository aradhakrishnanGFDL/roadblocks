import caselist
print(caselist.dict)
#{'CASENAME': {'NAME': 'casename'}, 'CASENAME1': {'NAME': 'casename1'}}
print("MULTI-RUN")

print(caselist.dict["CASENAME"]["NAME"])
print(caselist.dict["CASENAME1"]["NAME"])

