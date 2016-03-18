#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include <math.h>

int main()
{
	int i = 0;
	printf("Please enter a number >5 and <= 20:   ");
	char* num = (char*) malloc(5*sizeof(char));
	fgets(num, 5, stdin);
	i = atoi(num);

	while (i<=5 || i>20)
	{
		printf("Please enter a number >5 and <=20:   ");
		fgets(num,5,stdin);
		i = atoi(num);
	}

	free(num);
	printf("The size of the array is: %d\n",i);

	double array[i];
	int a;
	for(a = 0; a < i; a++)
	{
		double d;
		printf("Please enter a real numer: ");
		char* real = (char*) malloc(sizeof(double));
		fgets(real,sizeof(double),stdin);
		d = atof(real);
		array[a]=d;
		free(real);
	}

	int b;
	for(b = 0; b < i; b++){
		printf("Real number: %f\n",array[b]);
	}

	int size = sizeof(array)/sizeof(array[0]);
	
	double mean(double a[], int size);
	double avg  = mean(array,size);
	printf("Mean of array is %f\n", avg);

	double median(double a[], int size);
	double midpoint = median(array,size);
	printf("Median of array is %f\n",midpoint);

	double sd(double mean, double a[], int size);
	double std = sd(avg,array,size);
	printf("Standard deviation of the array is %f\n", std);

	double mode(double a[],int size);
	double modeEle = mode(array,size);
	
	return 0;

}

double  mean(double  a[], int size)
{
        int i;
        double sum;
        for(i = 0; i < size; i++)
        {
                sum = sum + a[i];
        }

	double ans = sum/size;
        return ans;
}

double median(double a[], int size)
{
	if(size % 2 == 0)
	{
		int index = size / 2;
		double median = (a[index-1] + a[index]) / 2;
		return median;
	}
	else
	{
		int index = size / 2;
		return a[index];
	}
}

double mode(double a[],int size)
{
    int i, j, sum = 0,  t, b[20] = {0}, k = 0, c = 1, max = 0, mode;
    
    for (i = 0; i < size - 1; i++)
    {
        mode = 0;
        for (j = i + 1; j < size; j++)
        {
            if (a[i] == a[j]) {
                mode++;
            }
        }
        if ((mode > max) && (mode != 0)) {
            k = 0;
            max = mode;
            b[k] = a[i];
            k++;
        }
        else if (mode == max) {
            b[k] = a[i];
            k++;
        }
    }
    
    for (i = 0; i < size; i++)
    {
        if (a[i] == b[i])	
            c++;
    } 
        if (c == size){
            printf("\nThere is no mode");
       	}
	else
        {
            printf("\nMode\t= ");
            for (i = 0; i < k; i++)
	    {
                printf("%d ",b[i]);
	    }
        }
        printf("\n");
        return 0;
}

double sd(double mean, double a[],int size)
{
	int i;
	double  sum = 0;
	double pow(double base, double exponent);

	for(i = 0; i < size; i++)
	{
		double base = mean - a[i];
		sum = sum + pow(base,2);
	}

	double meanSquare = sum / size;
	double sqrt(double x);
	double res = sqrt(meanSquare);

	return res;

}

