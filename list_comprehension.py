temps = [221, 234, 340, 230, -99]
new_temps = [temp / 10 for temp in temps]
print(new_temps)

conditional_temp = [temp / 10 for temp in temps if temp != -99]
print(conditional_temp)

conditional_temp_else=[temp / 10 if temp != -99 else 0 for temp in temps]
print(conditional_temp_else)