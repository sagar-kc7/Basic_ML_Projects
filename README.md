These are the basic ML project resources. If you can do better, you are allowed to push changes.


Code: 
/* To find substring, prefix, suffix of a string */
#include<stdio.h>
#include<string.h>
void find_prefix(char string[]);
void find_suffix(char string[]);
void find_substring(char string[],int,int);

int main()
{
	char string[20];
	int i,j;
	printf("\n Enter a string\t");
	gets(string);
	
	printf("\n Prefixes:");
	find_prefix(string);
	printf("\n Suffixes");
	find_suffix(string);
	
printf("\nEnter i and j for substring");
	scanf("%d%d",&i,&j);
	find_substring(string,i,j);
	
	return 0;
}

void find_prefix(char string[])
{
	int i,j;
	char prefix[20];
	for(i=strlen(string);i>=0;i--)
	{
		for( j = 0; j<i;j++)
		  {
		  	prefix[j]= string[j];
		  }
		  prefix[j]='\0';
		  printf("\n %s",prefix);
	}
}
void find_suffix(char string[])
{
	int i,j,k;
	char suffix[20];
	for(i=0;i<=strlen(string);i++)
	{
		k = i;
		for( j = 0; j<strlen(string);j++)
		  {
		  	suffix[j]= string[k];
		  	k++;
		  }
		  suffix[j]='\0';
		  printf("\n %s",suffix);
	}
}

void find_substring(char string[],int x, int y)
{
	char substr[20];
	
	int k=0;
	for(int i=x-1;i<y;i++)
	{ 
	     substr[k]=string[i];
	     k++;
	}
	substr[k]='\0';
	printf("\n Substring:\n%s",substr);
	
}









OUTPUT:



TOC Lab : Implement a PDA for L = { set of all strings over {0,1} such that  equal number of 0s and 1s , acceptance by final state */
#include<stdio.h>
#include<string.h>
#define MAX 100
enum states { q0, q1,qf};
void push(char ch);
void pop();
char get_stack_top();
enum states delta(enum states, char, char);

struct stack
{
	char symbols[MAX];
	int top;
};
struct stack s;

int main()
{
	char input[20];
	enum states curr_state = q0;
	s.top = -1;
	int i =0;
	char ch = 'e';    // e indicating epsilon
	char st_top = 'e';
	curr_state = delta(curr_state,ch,st_top);
	
	printf("\n Enter a binary string\t");
	gets(input);
	
	ch = input[i];
	st_top = get_stack_top();
	int c=0;
	
	while( c <=strlen(input))
	{
		curr_state = delta(curr_state,ch,st_top);
		ch = input[++i];
		st_top=get_stack_top();
		c++;
      }
	if(curr_state == qf)
	   printf("\n The string %s is accepted.",input);
	else 
	    printf("\n The string %s is not accepted.",input);	    
		
   return 0;			
}

enum states delta(enum states s, char ch, char st_top)
{
	   enum states curr_state;
		switch(s)
		{
			case q0:
				if(ch=='e' && st_top=='e')
				{
					curr_state = q1;
					push('$');   		// $ is stack bottom marker
				}
				break;
			case q1:
				if(ch=='0' && (st_top=='$' ||st_top=='0'))
				{
					curr_state = q1;
					push(ch);
				}
				else if(ch=='1' && (st_top=='$'||st_top=='1'))
				{
					curr_state = q1;
					push(ch);
				}
				else if(ch=='1' && st_top=='0'||ch=='0'&&st_top=='1')
				{
					curr_state = q1;
					pop();
				}
				else if(ch=='\0' && st_top=='$')
				{
					curr_state = qf;
					pop();
				}
				break;
			}
	return curr_state;
}

//function to get stack top symbol
char get_stack_top()
{
	return (s.symbols[s.top]);
}

//push function
void push(char ch)
{
	if(s.top<MAX-1 )
	  {
	  	s.symbols[++s.top] = ch;
	  }
	else
	{
		printf("\n Stack Full.");
	}
}

//pop function
void pop()
{
	if(s.top>-1)
	{
		s.symbols[s.top]=' ';
		s.top--;
	}
	else
	printf("\n Stack Empty.");
}

OUTPUT:
