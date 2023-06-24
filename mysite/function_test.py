# typehinting


# 정수형 숫자 두개를 합해서 출력한다.
def sum(x: int, y:int)-> int:
    """정수형 숫자 두개를 합해서 출력한다.

    Args:
        x (int): 정수형 숫자
        y (int): 정수형 숫자

    Returns:
        int: 정수형 숫자 두개를 합 한 결과
    """
    print(x + y)

if __name__=='__main__':
    sum(100, 200)