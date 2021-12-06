def solution(file_object):
    result = []
    for l in file_object.readlines():
        l = l.strip()
        try:
            val = int(l)
            if -1000000000 <= val <= 1000000000:
                result.append(val)
        except ValueError:
            pass
    return result


f = open("file_object.txt", "r")
print(solution(f))
f.close()

