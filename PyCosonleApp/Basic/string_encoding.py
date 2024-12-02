import socket

def test(input_str):
    translated_str = input_str.translate(str.maketrans('PTSHA', '90168'))
    return translated_str

#Test case
str1 = "PHP"
print("Original string: ", str1)
print("Coded string: ", test(str1))

str2 = "JAVASCRIPT"
print("Original string: ", str2)
print("Coded string: ", test(str2))

#or
def test_encoding(input_str):
    translated_str = input_str.replace('P', '9').replace('T', '0').replace('S', '1').replace('H', '6').replace('A', '8')
    return translated_str

#Test case
str1 = "PHP"
print("Original string: ", str1)
print("Coded string: ", test(str1))

str2 = "JAVASCRIPT"
print("Original string: ", str2)
print("Coded string: ", test(str2))

#check lowercase or uppercase
def test_lower_or_upper(input_str):
    return input_str.islower() or input_str.isupper()

# Test case
str1 = "PHP"
print("Original string: ", str1)
print("Coded string: ", test_lower_or_upper(str1))

str2 = "javascript"
print("Original string: ", str2)
print("Coded string: ", test_lower_or_upper(str2))

str3 = "JavaScript"
print("Original string: ", str3)
print("Coded string: ", test_lower_or_upper(str3))

def remove_first_and_last_element(input_str):
    return input_str if len(input_str) < 3 else input_str[1:-1]
str1 = "PHP"
print("Original string: ", str1)
print("After Removing the string: ", remove_first_and_last_element(str1))

str2 = "Python"
print("Original string: ", str2)
print("After Removing the string: ", remove_first_and_last_element(str2))

def reverse_string_lowercase(input_str):
    return input_str[::-1].lower()
print("Reverse string in lower case:", reverse_string_lowercase("ElepHanT"))

def sort_string_alphabetical(input_str):
    return ''.join(sorted(input_str))
print("Convert the letters into alphabetical order:", sort_string_alphabetical("javascript"))


def get_domain_name(ip_address):
    result = socket.gethostbyaddr(ip_address)
    return list(result)[0]
print(get_domain_name("8.8.8.8"))
print(get_domain_name("13.251.106.90"))
print(get_domain_name("8.8.4.4"))
print(get_domain_name("23.23.212.126"))