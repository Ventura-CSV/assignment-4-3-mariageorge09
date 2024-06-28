def main():
    number = int(input('Enter your input: '))
    result = []
    x = number
    rem = 0 
    while x > 0:
        rem = (x % 2)
        result.append(rem)
        print (rem)
        x= x // 2
    print(result)
        
    
   

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
