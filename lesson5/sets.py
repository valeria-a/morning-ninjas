# unordered collection
s1 = {4, 5, 7, 8}
s2 = set()

# print(s1, s2)

# print(s1[2])
# s1 = {4, 5, 7, 8, 7}
# print(s1)

s3 = set([1,2,2,3, 3])
# print(s3)

names = ['Daniel', 'Ziv', 'Eyal', 'Daniel']
# print(set(names))
# print(list(set(names)))
# set actions


lecture_days = {'Sun', 'Tue', 'Wed'}
sport_days = {'Tue', 'Thu'}
lecture_and_sport = lecture_days.intersection(sport_days)
print(lecture_and_sport)
busy_days = lecture_days.union(sport_days)
print(busy_days)



