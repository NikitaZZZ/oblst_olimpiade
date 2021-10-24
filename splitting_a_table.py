t = int(input())
answers = []

for i in range(t):
    n, m = map(int, input().split()) 

    matrix = []
    num_n = 1
    num_m = 1

    matrix_a_2 = []
    matrix_b_2 = []

    matrix_h_top_2 = []
    matrix_h_bottom_2 = []

    sums_v = []
    sums_h = []

    # Создаем матрицу
    for a in range(n):
        matrix_m = []
        
        for b in range(m):
            matrix_m.append(num_m)
            num_m += 1

        num_n += 1
        matrix.append(matrix_m)

    # ----- Горизонталь -----
    for i in range(0, n):
        matrix_h_top = []
        matrix_h_bottom = []

        if i == 0:
            for a in range(m):
                matrix_h_top.append(matrix[i][a])
        else:
            for s in range(0, i+1):
                for g in range(m):
                    matrix_h_top.append(matrix[s][g])

        for k in range(i+1, n):
            for b in range(m):
                matrix_h_bottom.append(matrix[k][b])

        # Складываем все числа верхней/нижней части матрицы
        sum_h_top = []
        sum_h_bottom = []

        sum_h_top_test = 0
        sum_h_bottom_test = 0

        if len(matrix_h_bottom) != 0:
            for sum_h_top_cycle in range(len(matrix_h_top)):
                sum_h_top_test = sum_h_top_test + matrix_h_top[sum_h_top_cycle]

            for sum_h_bottom_cycle in range(len(matrix_h_bottom)):
                sum_h_bottom_test = sum_h_bottom_test + matrix_h_bottom[sum_h_bottom_cycle]

            sums_h.append([sum_h_top_test, sum_h_bottom_test])

    # ----- Вертикаль -----
    for vert in range(0, m):
        matrix_v_left = []
        matrix_v_right = []

        if vert == 0:
            for a in range(n):
                matrix_v_left.append(matrix[a][vert])
        else:
            for b in range(0, vert+1):
                for c in range(n):
                    matrix_v_left.append(matrix[c][b])

        for d in range(vert+1, m):
            for e in range(n):
                matrix_v_right.append(matrix[e][d])

        # Складываем все числа верхней/нижней части матрицы
        sum_v_left = []
        sum_v_right = []

        sum_v_left_test = 0
        sum_v_right_test = 0

        if len(matrix_v_right) != 0:
            for sum_v_left_cycle in range(len(matrix_v_left)):
                sum_v_left_test = sum_v_left_test + matrix_v_left[sum_v_left_cycle]

            for sum_v_right_cycle in range(len(matrix_v_right)):
                sum_v_right_test = sum_v_right_test + matrix_v_right[sum_v_right_cycle]

            sums_v.append([sum_v_left_test, sum_v_right_test])

    # ----- Суммы вертикали и горизонтали -----
    sums_v_final = []
    sums_h_final = []

    for elem_sum_v in range(len(sums_v)):
        sum = 0

        for number in range(len(sums_v[elem_sum_v])-1):
            sum = sums_v[elem_sum_v][number+1] - sums_v[elem_sum_v][number]
            sum = -sum if sum < 0 else sum

        sums_v_final.append(sum)

    for elem_sum_h in range(len(sums_h)):
        sum = 0

        for number in range(len(sums_h[elem_sum_h])-1):
            sum = sums_h[elem_sum_h][number+1] - sums_h[elem_sum_h][number]
            sum = -sum if sum < 0 else sum

        sums_h_final.append(sum)

    # ----- Сравниваем суммы вертикали и горизонтали и выводим ответ -----
    if len(sums_h) != 0 and len(sums_v) != 0:
        if min(sums_h_final) < min(sums_v_final):
            answers.append('H {}'.format(sums_h_final.index(min(sums_h_final)) + 2))
        else:
            answers.append('V {}'.format(sums_v_final.index(min(sums_v_final)) + 2))    
    elif len(sums_h) == 0:
        sums_v_final = []
        
        for i in range(len(sums_v)):
            for j in range(len(sums_v[i])-1):
                sum = sums_v[i][j+1] - sums_v[i][j]
                sum = -sum if sum < 0 else sum

                sums_v_final.append(sum)

        answers.append('V {}'.format(sums_v_final.index(min(sums_v_final)) + 2))
    elif len(sums_v) == 0:
        sums_h_final = []
        
        for i in range(len(sums_h)):
            for j in range(len(sums_h[i])-1):
                sum = sums_h[i][j+1] - sums_h[i][j]
                sum = -sum if sum < 0 else sum

                sums_h_final.append(sum)

        answers.append('H {}'.format(sums_h_final.index(min(sums_h_final)) + 2))

print('----- Answers -----')
for answer in range(len(answers)):
    print(answers[answer])