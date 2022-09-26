from collections import defaultdict

# 50*50 빈 행렬
# 1 <= r, c <= 50
# UPDATE r c data: [r]x[c]에 data를 입력(병합된 칸도 전부 update)
# UPDATE data1 data2: 모든 data1을 data2로 바꾸기(병합된 칸도 전부 update)
# PRINT r c: [r]x[c]에 있는 data를 출력 => 출력된 순서대로 answer에 담아서 출력(빈칸인 경우 'EMPTY'를 입력해서 출력)
# MERGE r1 c1 r2 c2: [r1]x[c1]칸과 [r2]x[c2]칸을 병합 (두칸 모두 데이터가 존재하면 [r1]x[c1]의 값으로 변경)
# UNMERGE r c: [r]x[c]칸만 남기고 병합된 모든 데이터 삭제


def solution(commands):
    answer = []
    arr = [[""]*51 for i in range(51)]
    value_dict = defaultdict(list)

    for c in commands:
        tmp = c.split()

        if tmp[0] == "UPDATE":

            if len(tmp) == 4:
                r, c = int(tmp[1]), int(tmp[2])
                data = arr[r][c]
                # 새로 입력할 데이터가 value_dict에 없으면 생성
                if tmp[3] not in value_dict:
                    value_dict[tmp[3]] = []

                # EMPTY인 경우
                if not data:
                    value_dict[tmp[3]].append([r, c])
                    arr[r][c] = tmp[3]

                else:
                    for v in value_dict[arr[r][c]]:
                        x, y = v[0], v[1]
                        arr[x][y] = tmp[3]
                        value_dict[tmp[3]].append([x, y])

                    value_dict[data].clear

            else:
                # data2가 value_dict에 없으면 생성
                if tmp[2] not in value_dict:
                    value_dict[tmp[2]] = []

                for v in value_dict[tmp[1]]:
                    x, y = v[0], v[1]
                    arr[x][y] = tmp[2]
                    value_dict[tmp[2]].append([x, y])

                # 기존값의 value_dict는 삭제
                value_dict[tmp[1]].clear

        elif tmp[0] == "PRINT":
            r, c = int(tmp[1]), int(tmp[2])
            if arr[r][c]:
                answer.append(arr[r][c])
            else:
                answer.append('EMPTY')

        elif tmp[0] == "MERGE":
            r1, c1 = int(tmp[1]), int(tmp[2])
            r2, c2 = int(tmp[3]), int(tmp[4])
            v1 = arr[r1][c1]
            v2 = arr[r2][c2]

            # 두 칸에 모두 데이터가 있었다면 [r1]x[c1]칸의 데이터로 전부 변경
            if v1 and v2:
                value_dict[v2].remove([r2, c2])
                value_dict[v1].append([r2, c2])
                arr[r2][c2] = v1

            # 한 칸에만 있는 경우 그 데이터로 전부 변경
            elif v1:
                value_dict[v1].append([r2, c2])
                arr[r2][c2] = v1

            elif v2:
                value_dict[v2].append([r1, c1])
                arr[r1][c1] = v2

        else:
            r, c = int(tmp[1]), int(tmp[2])
            data = arr[r][c]
            for v in value_dict[data]:
                arr[v[0]][v[1]] = ""

            value_dict[data].clear
            arr[r][c] = data
            value_dict[data] = [[r, c]]

    return answer


print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon",
                "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle",
                "MERGE 1 2 1 3", "MERGE 1 3 1 4",
                "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))

# [EMPTY, group]
