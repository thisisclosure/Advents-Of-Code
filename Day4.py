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
        print (newstr)
    else:
        return numstr

    return newstr

def check_range(i1, i2):
    count = 0
    num1, num2 = int(i1), int(i2)
    for num in range(num1, num2, 1):
        numstr = str(num) 
        numstr = ignore_trip(numstr)
        count = count + 1 if (has_dup(numstr) and increasing(numstr)) else count + 0
            #if has_trip(numstr):
            #    repeated = repeats(numstr, 3)
            #    count = count + 1 if has_dup(numstr.replace(first_trip(numstr),'')) else count + 0
            #    continue
            
    return count   
            
        
    #else:
    #    continue
    # 
print(check_range(input1, input2))