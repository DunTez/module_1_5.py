immutable_var_tuple_ = 1, 2, 'coconut', 'oil'
print(immutable_var_tuple_)
#immutable_var_tuple_[1] = 5 #Не можем изменить, так как кортеж-это неизменяемый тип данных
mutable_list = ([7, 5],4)
mutable_list[0][0] = 6
print(mutable_list)