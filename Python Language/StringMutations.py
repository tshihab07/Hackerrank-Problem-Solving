# Problem Mutation: Modify a string

# Method - I: Converting into list
# Creating Function: Argument(string, position, character_to_be_modified)
def mutate_string(string, pos, ch):
    str_list = list(string)
    str_list[pos] = ch
    
    return "".join(str_list)
    

# Method - III: Slicing
def mutate_str(string, pos, ch):
    return string[:pos] + ch + string[pos+1:]



if __name__ == '__main__':
    string = input("Enter String: ")
    position = int(input("Enter Position: "))
    character = input("Enter Character: ")
    
    modified_str1 = mutate_string(string, position, character)
    
    modified_str2 = lambda string, pos, ch: string[:pos] + ch + string[pos+1:]
    modified_str2 = modified_str2(string, position, character)
    
    modified_str3 = mutate_str(string, position, character)
    
    print("\nOutputs:")
    print("Result of Method - I:", modified_str1)
    print("Result of Method - II:", modified_str2)
    print("Result of Method - III:", modified_str3)
    
    
    
    
    
    
    
    
    
    
    
    
