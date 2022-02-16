t = ['t', 'r', 'u', 'e']
l = ['l', 'o', 'v', 'e']

true_count = 0
love_count = 0

person1 = input("Person 1: ").lower()
person2 = input("Person 2: ").lower()

combined = person1 + " " + person2

for x in t:
  true_count = true_count + combined.count(x)

for x in l:
  love_count = love_count + combined.count(x)

score = int(str(true_count) + str(love_count))

if (score < 10 or score > 90):
  print("Your score is %d, you go together like Coke and mentos." % score)
elif score > 40 and score < 50:
  print("Your score is %d, you are alright together." % score)
else:
  print("Your score is %d." % score)
  