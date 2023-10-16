import time

def typing_speed_test():
    print("Type the following sentence:")
    sentence = "The Children unravel a series of extrodinary."
    print(sentence)
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_typed = len(user_input.split())
    typing_speed = words_typed / elapsed_time
    
    print("Your typing speed is {:.2f} words per second.".format(typing_speed))

typing_speed_test()

