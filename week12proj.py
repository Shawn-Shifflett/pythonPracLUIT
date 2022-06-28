#The list should be empty initially.
#Populate the list using append or insert.
#Print the list and the length of the list.
#Remove two specific services from the list by name or by index.
#Print the new list and the new length of the list.

#Create a list of services using Python. IE: S3, Lambda, EC2, etc

#The list should be empty initially.
groupList = []

#Populate the list using append or insert.
groupList.append("S3")
groupList.append("Lambda")
groupList.append("EC2")
groupList.append("CloudFront")
groupList.append("CloudFormation")

#Print the list
print("List:", groupList)
#Print the length of the list
print("List Length:", len(groupList))

#Remove 2 specific services from the list by index
del groupList[4]
#Remove 2 specific services from the list by name
groupList.remove("CloudFront")

print("----------------------------------")

#print new list
print("New List:", groupList)

#print new length of the list
print("New List Length:", len(groupList))