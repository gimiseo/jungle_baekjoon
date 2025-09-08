#include <stdio.h>
#include <stdlib.h>

/* [left..mid], [mid+1..right] 두 구간은 "이미 정렬되어 있다"고 가정하고
   두 구간을 "하나의 정렬된 구간"으로 합치는 함수 */
void merge(int a[], int left, int mid, int right) {
    int n = right - left + 1;
    int *tmp = (int*)malloc(sizeof(int) * n);  // 병합 결과를 잠시 담을 배열

    int i = left;      // 왼쪽 구간 현재 위치
    int j = mid + 1;   // 오른쪽 구간 현재 위치
    int t = 0;         // tmp 배열에 채울 위치

    // 두 구간에서 더 작은 값을 차례로 꺼내 tmp에 담는다
    while (i <= mid && j <= right) {
        if (a[i] <= a[j]) tmp[t++] = a[i++];
        else              tmp[t++] = a[j++];
    }

    // 남은 것들 마저 복사 (둘 중 하나만 실행됨)
    while (i <= mid)   tmp[t++] = a[i++];
    while (j <= right) tmp[t++] = a[j++];

    // tmp의 내용을 원본 a[left..right]에 되돌려쓰기
    for (int k = 0; k < n; ++k) {
        a[left + k] = tmp[k];
    }

    free(tmp);
}

/* 배열 a의 [left..right]를 정렬 */
void merge_sort(int a[], int left, int right) {
    if (left >= right) return;       // 원소 1개(또는 공집합)이면 이미 정렬됨

    int mid = (left + right) / 2;    // 반으로 나누기
    merge_sort(a, left, mid);        // 왼쪽 정렬
    merge_sort(a, mid + 1, right);   // 오른쪽 정렬
    merge(a, left, mid, right);      // 둘을 합쳐 정렬
}

int main(void) {
    int a[] = {21, 10, 12, 20, 25, 13, 15, 22};
    int n = sizeof(a) / sizeof(a[0]);

    printf("정렬 전: ");
    for (int i = 0; i < n; ++i) printf("%d ", a[i]);
    printf("\n");

    merge_sort(a, 0, n - 1);

    printf("정렬 후: ");
    for (int i = 0; i < n; ++i) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
