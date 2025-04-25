vehicles = {
    'dreams': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-AM 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'Jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple',
}

# my_car = vehicles['fiesta']
# print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get("er5")
# print(learner)

vehicles["starfighter"] = "Lockheed F-104"    # adding the key/values to the vehicles
vehicles["learjet"] = "Bombardier Learjet 75"  # adding the key/values to the vehicles
vehicles["toy"] = "glider" # adding the key/values to the vehicles
# upgrade the virago
vehicles["virago"] = "Yamaha XV535"  # adding the value with same key

del vehicles["starfighter"]
# del vehicles["f1"]

# pop value will return the result
result = vehicles.pop("f1", "You wish! Sell the learjet and you might afford a racing car")
print(result) # return the result as default value because key is not present

plane = vehicles.pop("learjet")
print(plane) # result as value of key

bike = vehicles.pop("tenere", "not present")
print(bike) # result as value of key because key is already present

vehicles.pop("f1", None)  # key not present but code will not crash because we passed defalut value as None
# vehicles.pop("f1")  #key not present, code will crash
# vehicles.pop("toy")  # key is present it will remove the key/value

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")

for key, value in vehicles.items():
    print(key, value, sep=", ")
