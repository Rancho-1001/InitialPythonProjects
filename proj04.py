# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 01:11:23 2023

@author: user
"""

''' Insert heading comments here.'''


MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             E. Encode an image with a text.
             D. Decode an image.
             M. Display the menu of options.
             X. Exit from the program.'''
    

def numtobase( N, B ):
    '''This function accepts as input a non-negative integer N and a base B (no error checking);
    it should return a string representing the number N in base B. The string should always be 
    of length multiple of 8 unless the number is 0.Your function must output the
    empty string when the input value of N is 0. (This avoids leading zeros!)'''
    pass  # insert your code here
    
    N = int(N)
    B = int(B)
    base_num = ''
    
    if N == 0:
        return base_num
    
    while N > 0:
        base_num = str(N%B) + base_num 
        N //= B
        
    return base_num.zfill(8) 
         

def basetonum( S, B ):
    '''This function accepts as input a string S and a base B where S represents a number 
    in base B where B is between 2 and 10 inclusive.
    It should then return an integer in base 10 representing the same number as S.
    It should output 0 when S is the empty string'''
    pass  # insert your code here
    
    B = int(B)
    S = S[::-1]
    decimal_num = 0
    if S == '':
        return 0
    
    for i in range(len(S)):
        new_number = S[i]
        
        if new_number.isdigit():
            new_number = int(new_number)
        decimal_num += new_number*(B**i)
        
    return decimal_num 


def basetobase(B1,B2,s_in_B1):
    '''Now, we can assemble what we've written to write a function that takes three inputs:
        a base B1, a base B2 and s_B1, which is a string representing a number in base B1. 
        Then, your function should return a string representing the same number in base B2.
        S_B1 is always of length multiple of 8.'''
    pass  # insert your code here
    
    B1 = int(B1)
    B2 = int(B2)
    if s_in_B1 == '':
        return ''
    
    if B2 == 10:
        output = basetonum(s_in_B1, B1)
        output1 = str(output).zfill(8)
        return output1
    else:
        output = basetonum(s_in_B1, B1)
        output1 = numtobase(output, B2)
        
        if len(output1) <= 8:
            output1 = output1.zfill(8)
            return output1
        else:
            output1 = output1.zfill(16)
            return output1 

      
def encode_image(image,text,N):
    '''This function takes a binary string image representing the image, 
    text representing the message to be hidden in the image and N representing
    how many bits represent each pixel, and returns another binary string as output.
    The output binary string should be the original image with the text embedded using the LSB algorithm defined earlier.
    If image is empty, the function should return an empty string. If text is empty, the image should not change.
    If the image is not big enough to hold all the text, the function should return None'''
    pass  # insert your code here
    
    if image == '':
        return ''
    if text == '':
        return image 
    message = ''
    for i,ch in enumerate(text):
        
            ch_decimal = ord(ch)
            text_message = numtobase(ch_decimal, 2)
            message += text_message
            
    message_index = 0
    new_image = image
    
    for i in range(N-1,len(image), N):
        new_image = new_image[:i]+ message[message_index] + new_image[i+1:]
        message_index += 1 
        if message_index == len(message):
            break
    
    
    if message_index < len(message):
        return ''
    return new_image 
    


def decode_image(stego,N):
    '''This function takes a binary string and N representing how many bits represent each pixel 
    as input and returns a string as output, which is the hidden text. The function "inverts" or "undoes" 
    the encoding in your encode_text() function. That is, decode_image(encode_image(image,text,N),N) 
    should give back text and some more characters as gibberish.'''
    pass  # insert your code here 
    
    encoded_message = ''
    for i in range(N-1,len(stego), N):  #To get the encoded message
        encoded_message += stego[i]
    n = 0 
    while n <= len(encoded_message): #To slash down the length of the encoded message to the least multiple of 8
        n += 8
    n -= 8
    new_encoded_message = encoded_message[:n]
    
    decoded_message = ''
    for i in range(0, len(new_encoded_message),8):
        stego_ch = new_encoded_message[i:i+8]
        #convert stegoch to its number
        stego_number = basetonum(stego_ch, 2)
        
        #convert the number to its character
        stego_letter = chr(stego_number)
        #add the character to decoded message
        decoded_message += stego_letter 
        
    return decoded_message
        

        

def main():
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''

    print(BANNER)
    pass  # insert your code here
    print(MENU)
    options = ('a','b','c','e','d','m','x')
    
    user_option = input("\n\tEnter option: ").lower()
    while user_option != 'x':
        if user_option == 'm' or user_option not in options:
            if user_option == 'm':
                print(MENU)
                user_option = input("\n\tEnter option: ").lower()
            if user_option not in options:
                print("\nError:  unrecognized option [{}]".format(user_option.upper()))
                print(MENU)
                user_option = input("\n\tEnter option: ").lower()
                
        if user_option == 'a':
            N = input("\n\tEnter N: ")
            
            while N.isdigit() is False:
                print("\n\tError: {} was not a valid non-negative integer.".format(N))
                N = input("\n\tEnter N: ")
   
            B = int(input("\n\tEnter Base: "))
            
            while (2 <= B <= 10) is False:
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B))
                B = int(input("\n\tEnter Base: "))
                
            output = numtobase(N, B)
            print("\n\t {} in base {}: {}".format(int(N),int(B),output))
            
            user_option = input("\n\tEnter option: ").lower()
            
        if user_option == 'b':
            S = input("\n\tEnter string number S: ")
            
            B = int(input("\n\tEnter Base: "))
            
            while (2 <= B <= 10) is False:
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B))
                B = int(input("\n\tEnter Base: "))
                
            output = basetonum(S, B)
            print("\n\t {} in base {}: {}".format(S,B,output))
            
            user_option = input("\n\tEnter option: ").lower()
            
        if user_option == 'c':
            B1 = int(input("\n\tEnter base B1: "))
            
            while (2 <= B1 <= 10) is False:
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B1))
                B1 = int(input("\n\tEnter base B1: "))
                
            B2 = int(input("\n\tEnter base B2: "))
            
            while (2 <= B2 <= 10) is False:
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B2))
                B2 = int(input("\n\tEnter base B2: "))
                
            S_in_B1 = input("\n\tEnter string number: ")
            
            if S_in_B1 == '0':
                output = ''
            else:
                output = basetobase(B1, B2, S_in_B1)
                
            print("\n\t {} in base {} is {} in base {}...".format(S_in_B1, B1 , output , B2))
            
            user_option = input("\n\tEnter option: ").lower() 
            
        if user_option == 'e':
            Image_String = input("\n\tEnter a binary string of an image: ")
            
            Number_of_bits = int(input("\n\tEnter number of bits used for pixels: "))
            
            Text_to_hide = input("\n\tEnter a text to hide in the image: ")
            
            output = encode_image(Image_String, Text_to_hide, Number_of_bits)
            
            if Image_String == '' or (len(Image_String) <= 16):
                print("\n\tImage not big enough to hold all the text to steganography")
                
            else:
                print("\n\t Original image: {}".format(Image_String))
                
                print("\n\t Encoded image: {}".format(output))
                
            
            user_option = input("\n\tEnter option: ").lower() 
            
        
        if user_option == 'd':
            encoded_image = input("\n\tEnter an encoded string of an image: ")
            
            Number_of_bits = input("\n\tEnter number of bits used for pixels: ")
            
            output = decode_image(encoded_image, int(Number_of_bits))
            
            print("\n\t Original text: {}".format(output))
            
            user_option = input("\n\tEnter option: ").lower() 
            
        
    else:
        print('\nMay the force be with you.')
    
    
    
    
    
    
# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == '__main__': 
    main() 
    

"\n\tEnter option: "
"\n\tEnter N: "
"\n\tError: {} was not a valid non-negative integer."
"\n\tEnter Base: "
"\n\tError: {} was not a valid integer between 2 and 10 inclusive."
"\n\tEnter Base: "
"\n\t {} in base {}: {}"
"\nEnter string number S: "
"\n\tEnter base B1: "
"\n\tEnter base B2: "
"\n\t {} in base {} is {} in base {}..."
"\n\tEnter a binary string of an image: "
"\n\tEnter number of bits used for pixels: "
"\n\tEnter a text to hide in the image: "
"\n\t Original image: {}"
"\n\t Encoded image: {}"
"\n\tImage not big enough to hold all the text to steganography"
"\n\tEnter an encoded string of an image: "
"\n\tEnter number of bits used for pixels: "
"\n\t Original text: {}"
"\nError:  unrecognized option [{}]"
'\nMay the force be with you.'
    
    
















