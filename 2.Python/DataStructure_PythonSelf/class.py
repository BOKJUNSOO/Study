# class
# class 는 물건을 만들어내는 설계도이다.
# 객체는 틀로 만들어낸 물건이다.
# 객체는 클래스내의 메서드로 생성할 수 있다.
# 인스턴스는 메모리에 살아있는 객체이다.

# class의 기본구조
class FourCal:                         # self에는 객체 FourlCal의 정보가 저장된다.
    def __init__(self, first, second): # FourCal 객체를 생성할때 자동으로 변수가 초기화된다.
        self.first = first             # FourCal 객체 생성시 두가지 변수를 지정한다.
        self.second = second           # 생성자 __init__ 은 객체가 직접 변수를 받을 수 있게 해준다
        self.__third = 0               # third 라는 변수는 객체 생성시 parameter로 받지 않아도 된다. grobal
    def add(self):
        result = self.first + self.second
        return result

a = FourCal(1,2) # 객체 생성시 객체 a에 first, seond라는 변수가 생성된다.
                 # 객체변수, 속성 이라고 칭한다. 객체의 객체변수는 다른 객체와 상관없는 독립적인 값을 가진다.



# 캡슐화
# 객체를 사용하는 사람으로부터 변수와 함수를 숨기는 작업
# 인스턴스 변수와 인스턴스 함수 앞에 __를 붙힌다.

class Circle:
    def __init__(self, 반지름):
        if 반지름 < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__반지름 = 반지름
        self.__파이 = 3.14
    
    @property
    def 반지름(self):
        return self.__반지름
    
    @반지름.setter
    def 반지름(self, value):
        if value < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__반지름 = value
    
    @property
    def 둘레(self):
        return 2 * self.__파이 * self.__반지름
    @property
    def 넓이(self):
        return self.__파이 * (self.__반지름 ** 2)
    
circle = Circle(10) # circle 이라는 인스턴스 객체
                     # 음수로 매개변수를 받지 못하게

circle.__반지름 = -10   # 변수를 직접 설정하면 if 문을 작성해도 소용없음
                        # __ 캡슐화를 통해 객체사용자가 변수에 접근 못하게할 수 있음
                        # circle 객체는 반지름이라는 속성이 없다고 출력

print(circle.둘레)    # 음수로 변수를 지정해도 인스턴스 객체에서 지정된 반지름을 이용, 양수로 표기됨

circle.__반지름 = 10 # 변수로 값을 지정하는건 불가능하다 하지만 함수로 하는 것은 가능함
                     # 겟터와 셋터
print(circle.반지름)
circle.반지름 = 20
print(circle.둘레)