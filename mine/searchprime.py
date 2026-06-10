'''a code to search prime numbers'''


#search prime numbers
def search_prime(num):
    nums=[2]
    candidate=3

    while nums[-1]<num:
        is_prime=True
        for p in nums:
            if candidate%p==0:
                is_prime=False
                break
        if is_prime:
            nums.append(candidate)
        candidate+=2

    return [p for p in nums if p<=num]

#user enter
while True:
    num = int(input('Please enter an integer: '))
    if num=='q':
        break
    else:
        print(search_prime(num))