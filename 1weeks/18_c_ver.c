#include <stdio.h>

int	count_words(char *s, char c)
{
	int 	count;
	int		in_word;

	count = 0;
	in_word = 0;
	while (*s)
	{
		if (*s != c && !in_word)
		{
			in_word = 1;
			count++;
		}
		else if (*s == c)
			in_word = 0;
		s++;
	}
	return (count);
}

// str이 첫번째 인자로 들어왔다는 전제
int main(int ac, char ** av)
{
    int count = 0;
	//스페이스로 구분한다고 한다면!!
	count = count_words(av[1], ' ');

    printf("%d\n", count);
    return 0;
}