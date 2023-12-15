import datetime

# evenify(input_numbers): return a sortedlist of even numbers in input_numbers

def evenify(input_numbers):

    even_number = []
    for num in input_numbers:
        if num % 2 == 0:
            even_number.append(num)
    return sorted(even_number)

# foo_max(items): find and return the maximum element in the list (items)

def foo_max(items):
    list = [i for i in items]
    maximum_num = list[0] 
    for nums in list[1:]:
        if nums > maximum_num:
            maximum_num = nums
    return maximum_num


# sautee(sentence): take a sentence and return the sentence with the words in reverse order

def sautee(sentence):
    sentence = sentence.split()

    return ' '.join(sentence[::-1])

# flambe(sentence): returns a new list with the words sorted by their length

def flambe(sentence):
    words = sentence.split()
    final_list = sorted(words, key=len)
    return final_list

# poach(dt: datetime.datetime): return True if datetime is in a leap year and False if not

def poach(dt):
    if dt.year % 4 == 0 and (dt.year % 100 != 0 or dt.year % 400 == 0):
        return True
    else:
        return False

current_datetime = datetime.datetime.now()
result = poach(current_datetime)

# heron(a, b, c): return the area of a triangle given the lengths of its three sides (Heron's formula)
# s = (a + b + c) / 2
# area = √(s * (s - a) * (s - b) * (s - c))

def heron(a, b, c):
    s = (a+b+c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) **0.5
    return area

if __name__ == "__main__":
    print(evenify([2,34,12,42,21,11]))
    print (foo_max([12,432,12,234,2]))
    print(sautee('My name is Neelakshi'))
    print(flambe('My name is Neelakshi'))
    print(heron(5,8,6))
    print("Is the current datetime in a leap year?", result)







