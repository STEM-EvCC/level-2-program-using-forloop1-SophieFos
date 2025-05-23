mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

num_missions = 0
num_success = 0
missions_before_2000 = []

#iterate though the name list
for index, mission in enumerate(mission_names):
  
  #increment mission count
  num_missions += 1
  
  #update success
  if (mission_success[index]):
    num_success += 1
  
  #update pre-2000 misions
  if (mission_years[index] < 2000):
    missions_before_2000.append(mission)

#print mission num
print(f"Total number of missions: {num_missions}")

#print success
print(f"Number of successful missions: {num_success}")

print(f"Success rate: {(num_success/num_missions):.2%}")
Missions launched before the year 2000:
print("Missions launched before the year 2000:")

for mission in missions_before_2000:
  print(f"- {mission}")