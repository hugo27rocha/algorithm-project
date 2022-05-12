Execution flow:

Project$ python inputgenerator.py

Project$ python read.py

Datacenter List
['datacenter_1_tier_1', 'datacenter_2_tier_1', 'datacenter_3_tier_2', 'datacenter_4_tier_2'] 

serverList
['datacenter_1_tier_1_server_1', 'datacenter_1_tier_1_server_2', 'datacenter_2_tier_1_server_3', 'datacenter_2_tier_1_server_4', 'datacenter_3_tier_2_server_5', 'datacenter_3_tier_2_server_6', 'datacenter_4_tier_2_server_7', 'datacenter_4_tier_2_server_8'] 

serverCost
{'datacenter_1_tier_1_server_1': '5', 'datacenter_1_tier_1_server_2': '18', 'datacenter_2_tier_1_server_3': '1', 'datacenter_2_tier_1_server_4': '26', 'datacenter_3_tier_2_server_5': '38', 'datacenter_3_tier_2_server_6': '42', 'datacenter_4_tier_2_server_7': '6', 'datacenter_4_tier_2_server_8': '45'} 

FatherCost
{'datacenter_1_tier_1': '25', 'datacenter_2_tier_1': '26'} 

deployCost
{'datacenter_1_tier_1': '46', 'datacenter_2_tier_1': '41', 'datacenter_3_tier_2': '2', 'datacenter_4_tier_2': '12'} 