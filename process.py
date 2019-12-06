import csv

N7110_KEYPAD_ZERO = 0
N7110_KEYPAD_ONE = 1
N7110_KEYPAD_TWO = 2
N7110_KEYPAD_THREE = 3
N7110_KEYPAD_FOUR = 4
N7110_KEYPAD_FIVE = 5
N7110_KEYPAD_SIX = 6
N7110_KEYPAD_SEVEN = 7
N7110_KEYPAD_EIGHT = 8
N7110_KEYPAD_NINE = 9
N7110_KEYPAD_STAR = 10
N7110_KEYPAD_HASH = 11
N7110_KEYPAD_MENU_LEFT = 100
N7110_KEYPAD_MENU_RIGHT = 101
N7110_KEYPAD_MENU_UP = 102
N7110_KEYPAD_MENU_DOWN = 103
N7110_KEYPAD_CALL_ACCEPT = 104
N7110_KEYPAD_CALL_REJECT = 105

#activated after hash 11
N7110_IME_T9 = 0
N7110_IME_T9_CAPS = 1
N7110_IME_ABC = 2
N7110_IME_ABC_CAPS = 3

KEYPAD = {'0':" 0", '1':  r".,'?!\"1-()@/:", '2': "abc2", '3':"def3", '4': "ghi4", '5':"jkl5", '6':"mno6", '7':"pqrs7", '8':"tuv8", '9':"wxyz9", '10':r"@/:_;+&%*[]{}" }

def get_keypresses(filename):
    with open(filename) as sms4file:
        csvreader = csv.reader(sms4file)
        sms4list = list(csvreader)
        keypresses = [entry[1] for entry in sms4list]
        return keypresses

sms1_keys = get_keypresses('sms1.csv')
sms2_keys = get_keypresses('sms2.csv')
sms3_keys = get_keypresses('sms3.csv')
sms4_keys = get_keypresses('sms4.csv')
print(sms4_keys)

def parse(inputs):
  output = ""
  toUpper = False
  for current in range(len(inputs)):
    character = inputs[current] 
    if current < len(inputs) - 1:
      print(current)
      next_char = inputs[current + 1]
    else:
      next_char = 'EOF'
    count = 0
    while character == next_char:
      character = inputs[current]
      count += 1
      current += 1
    if character == '11':
      if count % 2 == 0:
        toUpper = True
      else:
        toUpper = False
    elif character == '100':
      pass
      current =  current - 1 if current > 0 else 0
    elif character == '101':
      pass
      current =  current + 1 if current <= len(inputs) - 1 else len(inputs) - 1
    elif character == '102':
      pass
    elif character == '103':
      pass
    elif character == '104':
      pass
    elif character == '105':
      pass
    else:
      if count > 0:
        print(f'{character} : {count}')
      
      selected = KEYPAD[character]
      new_input = selected[count % len(selected)]
      output = output + new_input if not toUpper else output + new_input.upper()
      print(new_input)
  return output

sms1 = parse(sms1_keys)
sms2 = parse(sms2_keys)
sms3 = parse(sms3_keys)
sms4 = parse(sms4_keys)

print(sms1)
print(sms2)