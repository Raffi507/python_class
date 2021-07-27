import os
import requests
import threading
import time
import datetime

# def func():
#     req1 = requests.get("https://unsplash.com/photos/F_-0BxGuVvo") # requests.get("https://unsplash.com/photos/75_s8iWHKLs")
#     req2 = requests.get("https://unsplash.com/photos/F_-0BxGuVvo")# requests.get("https://unsplash.com/photos/75_s8iWHKLs")
#     req3 = requests.get("https://unsplash.com/photos/F_-0BxGuVvo")# requests.get("https://unsplash.com/photos/75_s8iWHKLs")
#     req4 = requests.get("https://unsplash.com/photos/F_-0BxGuVvo") #requests.get("https://unsplash.com/photos/75_s8iWHKLs")
#     req5 = requests.get("https://unsplash.com/photos/F_-0BxGuVvo") #requests.get("https://unsplash.com/photos/75_s8iWHKLs")
#
#     res = req1.json()
#     res2 = req2.json()
#     res3 = req3.json()
#     res4 = req4.json()
#     res5 = req5.json()
#     print(f"'{res[0]['q']}' --{res[0]['a']}")
#     print(f"'{res2[0]['q']}' --{res2[0]['a']}")
#     print(f"'{res3[0]['q']}' --{res3[0]['a']}")
#     print(f"'{res4[0]['q']}' --{res4[0]['a']}")
#     print(f"'{res5[0]['q']}' --{res5[0]['a']}")
#
# # for i in range(10):
# #     x = threading.Thread(target=func)
# #     # thread_list.append(x)
# #     time.sleep(1)
# #     x.start()
#
#
# #2
# sum = 0
#
# list1 = [100, 79, 758, 2, 65, 547]
#
# for i in range(len(list1)):
#     sum = sum + list1[i]
#
# print("The sum is - ", sum)


#3
def list_sum(list):
	sum = 0
	for e in list:
		if type(e) == type([]):
			sum = sum + list_sum(e)
		else:
			sum = sum + e

	return sum

recr_list =  [1, 2, [3,4], [5,6]]
print(list_sum(recr_list))