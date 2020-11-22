def nearest_value(values: set, one: int) -> int:

    print(answer)


nearest_value({4, 7, 10, 11, 12, 17}, 9) #== 10
nearest_value({4, 7, 10, 11, 12, 17}, 8) #== 7
nearest_value({4, 8, 10, 11, 12, 17}, 9) #== 8
nearest_value({4, 9, 10, 11, 12, 17}, 9) #== 9
nearest_value({4, 7, 10, 11, 12, 17}, 0) #== 4
nearest_value({4, 7, 10, 11, 12, 17}, 100) #== 17
nearest_value({5, 10, 8, 12, 89, 100}, 7) #== 8
nearest_value({-1, 2, 3}, 0) #== -1


