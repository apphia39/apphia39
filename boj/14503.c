#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main() {
	int n, m;
	int r, c, d;
	int board[50][50];

	scanf("%d %d", &n, &m);
	scanf("%d %d %d", &r, &c, &d);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &board[i][j]);
		}
	}

	int i = r, j = c;
	int clean = 0;
	int flag = 0;
	int spin = 0;

	while (1) {
		if (flag == 1)
			break;

		if (board[i][j] == 0) {
			board[i][j] = 2; //1번 (청소하기)
			clean++;
		}

		while (1) {
			//2번(왼쪽 탐색)
			if (d == 0) { //북쪽 보고 있는 경우
				if (board[i][j - 1] == 0) { //a
					d = 3;
					j--;
					break;
				}
				else {
					if (board[i + 1][j] != 0 && board[i - 1][j] != 0 && board[i][j + 1] != 0 && board[i][j - 1] != 0) {
						if (board[i + 1][j] == 1) {
							flag = 1;
							break;
						}
						else {
							i++;
							continue;
						}
					}
					d = 3;
					continue;
				}
			}

			if (d == 1) { //동쪽 보고 있는 경우
				if (board[i - 1][j] == 0) { //a
					d = 0;
					i--;
					break;
				}
				else {
					if (board[i + 1][j] != 0 && board[i - 1][j] != 0 && board[i][j + 1] != 0 && board[i][j - 1] != 0) {
						if (board[i][j - 1] == 1) {
							flag = 1;
							break;
						}
						else {
							j--;
							continue;
						}
					}
					d = 0;
					continue;
				}
			}

			if (d == 2) { //남쪽 보고 있는 경우
				if (board[i][j + 1] == 0) { //a
					d = 1;
					j++;
					break;
				}
				else {
					if (board[i + 1][j] != 0 && board[i - 1][j] != 0 && board[i][j + 1] != 0 && board[i][j - 1] != 0) {
						if (board[i - 1][j] == 1) {
							flag = 1;
							break;
						}
						else {
							i--;
							continue;
						}
					}
					d = 1;
					continue;
				}
			}

			if (d == 3) { //서쪽 보고 있는 경우
				if (board[i + 1][j] == 0) { //a
					d = 2;
					i++;
					break;
				}
				else {
					if (board[i + 1][j] != 0 && board[i - 1][j] != 0 && board[i][j + 1] != 0 && board[i][j - 1] != 0) {
						if (board[i][j + 1] == 1) {
							flag = 1;
							break;
						}
						else {
							j++;
							continue;
						}
					}
					d = 2;
					continue;
				}
			}
		}
	}

	printf("%d", clean);

	return 0;
}