
s=[{'model': 'customer.employee', 'pk': 1, 'fields': {'ename': 'suresh', 'eage': 27}},
   {'model': 'customer.employee', 'pk': 2, 'fields': {'ename': 'sachin', 'eage': 26}}]
s2= [{'model': 'customer.employee', 'pk': 3, 'fields': {'ename': 'sachin', 'eage': 26}},
 {'model': 'customer.employee', 'pk': 4, 'fields': {'ename': 'mahesh', 'eage': 23}},
 {'model': 'customer.employee', 'pk': 5, 'fields': {'ename': 'rahul', 'eage': 44}}]
s3=[{'model': 'customer.employee', 'pk': 3, 'fields': {'ename': 'sachin', 'eage': 26}},
 {'model': 'customer.employee', 'pk': 4, 'fields': {'ename': 'mahesh', 'eage': 23}}]
# s=[{'model': 'customer.employee', 'pk': 1, 'fields': {'ename': 'suresh', 'eage': 27}}, {'model': 'customer.employee', 'pk': 2, 'fields': {'ename': 'sachin', 'eage': 26}}][{'model': 'customer.employee', 'pk': 3, 'fields': {'ename': 'sachin', 'eage': 26}}, {'model': 'customer.employee', 'pk': 4, 'fields': {'ename': 'mahesh', 'eage': 23}}, {'model': 'customer.employee', 'pk': 5, 'fields': {'ename': 'rahul', 'eage': 44}}]
# print(s[0])
for i in s2:
    print(i)


