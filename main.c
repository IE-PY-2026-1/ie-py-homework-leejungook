//1, 주석
/*
	파일 이름: week 7/ main.c
	작성자: 김영웅, 26-04-20
	하는 일: switch-case문 연습
*/

//2. 전처리기
#include <stdio.h>
#include <stdlib.h>

// 3. main 함수
int main()
{
	system("chcp 65001");
	
	//1. 변수 선언 - 정수 month, days
	
}

void exam()
{
	int month;
	int days;
	//2. 사용자 입력 
	printf("달을 입력하시오:");
	scanf("%d", &month);
	
	//3. switch-case 문		-2월 // 4, 6, 9 11월 // 그 외 
	switch (month)
	{
		case 2:
			days = 28;
			break;
		case 4:
		case 6:
		case 9:
		case 11:
			days = 30;
			break;
		default:
			days = 31;		
			break;
	}
	//4. 출력 - 12월의 일수는 31일 입니다.
	printf("%d월의 일수는 %d일 입니다.\n", month, days);
		
	return 0;
}