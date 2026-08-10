scores = [1,2,3,4]

scores.extend("Hello-World");
print(scores)

scores.remove("H")
print(scores)

xx = scores.pop()
print(xx, scores)

loc = scores.index("-")
print(loc)

num = scores.count(2)
print(num)

nums = [1,3,5,6,2,5]

nums.sort(reverse=True)
print(nums)

