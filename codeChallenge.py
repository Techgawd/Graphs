# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
# {
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }
# Your algorithm should return 41, the sum of the values 23 and 18.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
# UNDERSTAND
# I know that we need to be able to tell the difference between strings and integers and single out just the integers, then we will need to add those values together and return the answer

# PLAN
# I need to add the dictionary of info, I need to loop through each object, if the value is an integer, will save to new array(starts with zero), then I will need to return sum of all integers

dict_t = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

sum_val = 0
for key, val in dict_t.items():
    if type(val) == int:
        sum_val += val

print(sum_val)