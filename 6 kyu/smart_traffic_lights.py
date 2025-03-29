"""Smart Traffic Lights
6 kyu
https://www.codewars.com/kata/58587905ed1b4dad6e0000c6

Description:
Story

Your friend Bob is working as a taxi driver. After working for a month he is frustrated in the city's traffic lights. He asks you to write a program for a new type of traffic light. It is made so it turns green for the road with the most congestion.
Task

Given 2 pairs of values each representing a road (the number of cars on it and its name), construct an object whose turngreen method returns the name of the road with the most traffic at the moment of the method call, and clears that road from cars.

After both roads are clear of traffic, or if the number of cars on both roads is the same from the beginning, return an empty value instead.
Example

t = SmartTrafficLight([42, "27th ave"], [72, "3rd st"])
t.turngreen()  ==  "3rd st"
t.turngreen()  ==  "27th ave"
t.turngreen()  ==  null

t = SmartTrafficLight([10, "27th ave"], [10, "3rd st"])
t.turngreen()  ==  null


"""


class SmartTrafficLight:
    def __init__(self, st1, st2):
        self.x = sorted((st1, st2))

    def turngreen(self):
        if self.x[0][0] == self.x[1][0]:
            return None
        self.x[0][0] = 0
        return self.x[0][1]


# class SmartTrafficLight:
#     def __init__(self, st1, st2):
#         self.st1, self.st2 = st1, st2
#
#     def turngreen(self):
#         if self.st1[0] == self.st2[0]:
#             return None
#         if self.st1[0] > self.st2[0]:
#             self.st1[0] = 0
#             return self.st1[1]
#         else:
#             self.st2[0] = 0
#             return self.st2[1]

t = SmartTrafficLight([42, "27th ave"], [72, "3rd st"])
print(t.turngreen())
print(t.turngreen())
print(t.turngreen())