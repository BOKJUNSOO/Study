#include <stdio.h>
/*
int main(void)
{
    int age = 14;
    int year;
    printf("year:%d\n",year); // 변수에 저장된 값을 출력할때는 지시자가 필요하다. %d == decimal integer (python baek 3~4 #1)
    printf("age:%d\n",age);
    printf("age:%d",14);
}


int main(void)
{
    int x = 10;
    int y = 20;
    int tmp;    // temp 임시 변수를 하나 지정한다
    tmp = x;    // 저장될 변수 상자는 왼쪽에 쓴다
    x = y;
    y = tmp;
    printf("x:%d y:%d", x , y);
}

#define WIDE 20
int main(void)
{
    const int HEIGHT = 10;
    int TRIANGEL = (WIDE*HEIGHT)/2;
    printf("AREA=%d",TRIANGEL);
    return 0;
}


// 타입의 일치
int main(void)
{
    short s = 0x1234567890; //2byte 저장
    int i = 0x1234567890;   //4byte 저장 가능
    printf("%#llx=%lld\n\n",0x1234567890,0x1234567890); 
    printf("sizeofS=%d\n",sizeof(s));
    printf("sizeofi=%d\n",sizeof(i));
    printf("sizeOfSt=%d\n",sizeof(0x123456790));

    //16진수로 출력
    printf("[16진수]\n");
    printf("s=%#x\n", s);   // %x는 정수를 16진수의 형태로 출력한다. // 16진수 한자리 = 4bit
    printf("i=%#x\n", i);   // #는 16진수 아에 접두사까지 표시해준다. // 8자리출력 = 32bit = 4byte => int타입의 변수 크기
    
    //10진수로 출력
    printf("[10진수]\n");
    printf("s=%d\n",s);
    printf("i=%d\n",i);
}

#define EMAIL "ask@codechobo.com"
int main(void)
{
    char ch = 65; // = 'A';
    char email[] = "ask@codechobo.com";
    
    int i = 0xFF;
    long long ll = 12345678901234LL;

    unsigned ui = 0xFFFFffff;
    unsigned long long ull = 0xFFFFffffFFFFffffLL;
    printf("long long size = %d\n",sizeof(long long));
    
    printf("ch='%c', %d\n", ch, ch);    // 문자로 출력, 10진정수로 출력
    printf("i=%d, %x, %X, %o, %#o\n", i, i , i , i ,i); // 10진정수로 출력 , 16진정수로 출력, 8진 정수로출력
    printf("ll=%lld\n",ll); //longlong 타입을 출력할때는 %lld 를 사용

    printf("ui=%u, %#x, %d\n)",ui,ui,ui);   // 부호없는 정수를 출력할 때는 반드시 %u를 사용한다.
    printf("ull=%llu,%#llx,%lld\n",ull,ull,ull);

    printf("\"Hello, world\"\n");
    printf("ask me, EMAIL please.\n");
    printf("ask me, " EMAIL " please.\n");
    printf("ask me, %s please.\n", EMAIL);
    
    printf("[12345678901234567890]\n");
    printf("[%s]\n", email);
    printf("[%20s]\n", email);  //20칸 확보 좌로정렬
    printf("[%-20s]\n", email);
    printf("%.8s\n", email);
    return 0;
}
*/
int main(void)
{
    float f = 12.12345f;
    printf("%%f = %f\n", f);    //f에 상관없이 소숫점 아래 6자리 까지 출력(빈자리는0)
    printf("%%8f = %8f\n", f);  // 전체 8자리 출력(빈자리는 0)
    printf("%%.3f = %.3f\n",f); // 소숫점아래 3자리 즉, %전체자리.소수점자리f 형태이다.
    printf("전체가7 = %7f\n",f);
    printf("sizeF= %d\n",sizeof(float));
    float a = 3;
    int b = 3.14f;
    printf("size of b = %d",b);
}