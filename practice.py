# # # # # # # # # # for i in range(1, 11):
# # # # # # # # # #     print(i*2)
# # # # # # # # # x = 10
# # # # # # # # # x = "Python"
# # # # # # # # # print(x, type(x))
# # # # # # # # lst = [2, 4, 6, 2, 4, 5, 3, 3]
# # # # # # # # n = len(lst)
# # # # # # # # for i in range (n):
# # # # # # # #     min_index = i
# # # # # # # #     for j in range (i+1, n):
# # # # # # # #         if lst[j] < lst[min_index]:
# # # # # # # #             min_index = j
# # # # # # # #         lst[i], lst[min_index] =lst[min_index], lst[i]
# # # # # # # # print(lst)
# # # # # # # sentence = input("Enter a sentence: ")
# # # # # # # words = sentence.split()
# # # # # # # freq = {}
# # # # # # # for word in words:
# # # # # # #     freq[word] = freq.get(word, 0) + 1
# # # # # # # print(freq)
# # # # # # t = ( 1, 6, 3, 5, 3, 5, 4)
# # # # # # print(t[0])
# # # # # # print(t[5])
# # # # # # print(t[0:5])
# # # # # # print(t[:3])
# # # # # dict = {"name" : "alice", "age": 25, "city": "New York"}
# # # # # print(dict.keys())
# # # # # print(dict.values())
# # # # # print(dict.items())
# # # # # dict.update({"course" : "python"})
# # # # # print(dict)
# # # # numbers = [2, 3, 42, 4, 5, 6, 67, 3, 2, 4, 2, 3,]
# # # # unique = list(set(numbers))
# # # # print(unique)
# # # f = open("data.txt", "w")
# # # f.write(" lorem ipsum dolor sit amet, consectetur adipiscing elit. lorem ipsum dolor sit amet, consectetur adipiscing elit. \n")
# # # f.close()
# # # f = open("data.txt", "r")
# # # print(f.read())
# # # f.close()
# # # from data import calc
# # # result = calc(10, 3)
# # # print(result)
# # # cration of dict
# # dict = {"name" : "alice", "age": 25, "city": "New York"}
# # # accesing dict 
# # print(dict["name"])
# # print(dict.get("age"))
# # # modification
# # dict["age"] = 26
# # dict["city"] = "Los Angeles"
# # # using built-in methods
# # print(len(dict))
# # print(type(dict))
# # # using methods
# # print(dict.keys())
# # print(dict.values())
# # print(dict.items())
# # dict.update({"course" :"python"})
# # print(dict)
# import math
# print(math.sqrt(99999))
import numpy as np