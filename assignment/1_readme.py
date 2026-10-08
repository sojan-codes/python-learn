#how to merge two dict and what are there challenges

dict1 = {
    'name' : 'Sojan'
}
dict2 = {
    'lname' : 'Shakya'
}

dict3 = dict1 | dict2
print(dict3)
# Challenges of Merging Two Dictionaries
# Duplicate keys – If both dictionaries contain the same key, the value from the second dictionary replaces the first.
# Data loss – Duplicate keys can cause the original value to be overwritten.
# Different data types – Incompatible or unexpected data types may cause problems when processing the merged data.
# Nested dictionaries – Simple merging does not properly combine nested dictionaries; one nested dictionary may overwrite another.

# The symbol | is called a vertical bar or pipe.