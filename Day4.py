inputstr = "246515-739105"
inputs = [numstr for numstr in inputstr.split("-")]
input1, input2 = inputs[0], inputs[1]

def has_dup(inputstr):
    dupes = [(str(i)+str(i)) for i in range(10)]
    for dup in dupes:
        #print(f"dup {dup} dupes {dupes} inputstr {inputstr}")
        if dup in inputstr:
            return True
        else:
            continue
    return False

def has_trip(inputstr):
    trips = [(str(i)+str(i)+str(i)) for i in range(10)]
    for trip in trips:
        #print(f"dup {dup} dupes {dupes} inputstr {inputstr}")
        if trip in inputstr:
            return True
        else:
            continue
    return False

def first_rep(inputstr, num):
    reps = [(str(i)*num) for i in range(10)]
    for rep in reps:
        if rep in inputstr:
            return rep
        else:
            continue
    return []

def first_trip(inputstr):
    trips = [(str(i)+str(i)+str(i)) for i in range(10)]
    for trip in trips:
        #print(f"dup {dup} dupes {dupes} inputstr {inputstr}")
        if trip in inputstr:
            return trip
        else:
            continue
    return []

def repeats(inputstr, num):
    reps = [(str(i)*num) for i in range(10)]
    output = []
    for rep in reps:
        #print(f"dup {dup} dupes {dupes} inputstr {inputstr}")
        if rep in inputstr:
            output += rep
        else:
            continue
    return output

def has_min_repeats(inputstr, num):
    reps = [(str(i)*num) for i in range(10)]
    result = False
    for rep in reps:
        if rep in inputstr:
            print(f'{rep} in {inputstr}')
            return True
        else:
            continue
    
    return result


def increasing(inputstr):
    for index in range(len(inputstr)):
        if index == 0:
            continue
        else:
            prior = int(inputstr[index - 1])
            current = int(inputstr[index])
            if current < prior:
                return False
            else:
                continue
    return True

def ignore_trip(numstr):
    if has_trip(numstr):
        newstr = numstr.replace(first_trip(numstr),'')
        if has_trip(newstr):
            newstr = ignore_trip(newstr)
    else:
        return numstr
    return newstr

def ignore_rep(numstr, num):
    if has_min_repeats(numstr, num):
        newstr = numstr.replace(first_rep(numstr, num),'')
        if has_min_repeats(newstr, num):
            newstr = ignore_rep(newstr, num)
    else:
        return numstr
    return newstr

def check_num(num):
    numstr = str(num)
    result = False 
    if (increasing(numstr)):
        for i in range(6,2,-1):
            print(i)
            if has_min_repeats(numstr, i):
                print(numstr)
                numstr = ignore_rep(numstr, i)
                print(numstr)
                if increasing(numstr) and has_dup(numstr):
                    return True
                else:
                    return False
            else:
                continue
        if has_dup(numstr):
            return True
        else:
            return False
    else:
        return False


def check_range(i1, i2):
    count = 0
    output = []
    num1, num2 = int(i1), int(i2)
    #count = sum([1 for num in range(num1, num2, 1) if check_num(num)])
    output = [num for num in range(num1, num2, 1) if check_num(num)]
            #if has_trip(numstr):
            #    repeated = repeats(numstr, 3)
            #    count = count + 1 if has_dup(numstr.replace(first_trip(numstr),'')) else count + 0
            #    continue
            
    return len(output)

for i in range(6,2,-1):
    print(has_min_repeats("112233", i))
    print(has_min_repeats("123444", i))
    print(has_min_repeats("111122", i))
print("done")
print(check_num("112233"))
print(check_num("123444"))
print(check_num("111122"))
print(check_range(input1, input2))