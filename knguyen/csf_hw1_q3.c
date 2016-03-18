#include <stdio.h>

typedef enum{A,B,C,D,E,F,G,H,I,J,K} State;

typedef enum{False, True} Bool;

Bool str_match(char str[], State s);

int main(int argc, char *argv[])
{
	Bool str_match(char str[], State s);
	if(str_match(argv[1], A))
		printf("STRING ACCEPTED\n");
	else
		printf("STRING NOT ACCEPTED\n");

}

Bool str_match(char str[], State s)
{
	if( (s == I) && (str[0] =='\0') )
		return True; 
	else if( (s == K) && (str[0] == '\0') )
		return True; 
	else  if( (s != I) && (str[0] =='\0') )
                return False;
	else
	{
		if(str[0] == 'a'){
			switch(s)
			{
				case A: return (str_match(str+1, B));
				case B: return (str_match(str+1, B));
				case J: return (str_match(str+1, B));
				case C: return (str_match(str+1, D));
				case D: return (str_match(str+1, E));
				case E: return (str_match(str+1, A));
				case F: return (str_match(str+1, G));
				case G: return (str_match(str+1, E));
				case H: return (str_match(str+1, I));
				case I: return (str_match(str+1, K));
				case K: return (str_match(str+1, K));
			}
		}
		else if(str[0] == 'b'){
			switch(s)
                        {
                                case A: return (str_match(str+1, J));
                                case B: return (str_match(str+1, C));
                                case J: return (str_match(str+1, J));
                                case C: return (str_match(str+1, A));
                                case D: return (str_match(str+1, A));
                                case E: return (str_match(str+1, F));
                                case F: return (str_match(str+1, A));
                                case G: return (str_match(str+1, H));
                                case H: return (str_match(str+1, A));
                                case I: return (str_match(str+1, K));
                                case K: return (str_match(str+1, K));
                        }

		}
		else
		{
			switch(s)
                        {
                                case A: return (str_match(str+1, J));
                                case B: return (str_match(str+1, J));
                                case J: return (str_match(str+1, J));
                                case C: return (str_match(str+1, A));
                                case D: return (str_match(str+1, A));
                                case E: return (str_match(str+1, A));
                                case F: return (str_match(str+1, A));
                                case G: return (str_match(str+1, A));
                                case H: return (str_match(str+1, A));
                                case I: return (str_match(str+1, K));
                                case K: return (str_match(str+1, K));
                        }

		}
	}
}

