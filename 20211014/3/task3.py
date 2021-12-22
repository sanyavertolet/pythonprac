top = input()

height = len(top)

gas = 0
liquid = 0

width = 1

bot = ''

while bot != top:
    width += 1
    bot = input()
    if bot[1] == '.':
        gas += 1
    elif bot[1] == '~':
        liquid += 1


gas_vol = gas * (height - 2)
liquid_vol = liquid * (height - 2)

liquid = liquid_vol // (width - 2)
if liquid_vol % (width - 2) != 0:
    liquid += 1
gas = height - liquid - 2

print('#' * width)
for i in range(height - 2):
    if gas != 0:
        print('#' + '.' * (width - 2) + '#')
        gas -= 1
    elif liquid != 0:
        print('#' + '~' * (width - 2) + '#')
        liquid -= 1
print('#' * width)

digits = max(len(str(gas_vol)), len(str(liquid_vol)))


liquid_str = '~' * 20
gas_str = '.' * 20

if liquid_vol > gas_vol:
    gas_str = '.' * round(20 * gas_vol / liquid_vol) + ' ' * (20 - round(20 * gas_vol / liquid_vol))
elif gas_vol > liquid_vol:
    liquid_str = '~' * round(20 * liquid_vol / gas_vol) + ' ' * (20 - round(20 * liquid_vol / gas_vol))


print(gas_str, '{0:>{digits}}/{1}'.format(gas_vol, gas_vol + liquid_vol, digits=digits))
print(liquid_str, '{0:>{digits}}/{1}'.format(liquid_vol, gas_vol + liquid_vol, digits=digits))


