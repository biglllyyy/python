data ='''##\x01\xfeLDPGAAAB0GG105585\x01\x00\x1e\x11\x07\x14\x17;\x04\x00\x0189860316402002255480\x01\x00\xeb'''



from VRealTimeUpload import VehicleRealTime

realtime = VehicleRealTime()


# realtime.unpack_head(data[0:24])

realtime.unpack_head(data[0:24])
# realtime.handle_back(data[24:])

# realtime.handle_back(data[24:])
# print(realtime.instance_to_dict())

# print realtime.instance_to_dict()