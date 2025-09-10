def char_ascii_compare(str1, str2):
    i = 0
    if str1 == str2:
       return 0
    while str1[i] == str2[i]:
        i += 1
    if ord(str1[i]) < ord(str2[i]):
        return 1
    return 0

def insert(array, start, end):
  for i in range(start + 1, end + 1):
    for j in range(i, 0, -1):
        if len(array[j]) < len(array[j - 1]):
            array[j], array[j - 1] = array[j - 1], array[j]
        elif len(array[j]) == len(array[j - 1]):
           if char_ascii_compare(array[j], array[j - 1]):
              array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

n = int(input())

word_list = []
for _ in range(n):
    word_list.append(input().strip())
insert(word_list, 0, len(word_list) - 1)

unique = []
for word in word_list:
   if word not in unique:
      unique.append(word)
for word in unique:
   print(word)