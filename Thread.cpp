#include <iostream>
#include <chrono>
#include <math.h>
#include <thread>

#include <cstdint>
//		Windows
#ifdef _WIN32
#include <x86intrin.h>
uint64_t rdtscp()
{
unsigned int	aux;
	return __rdtscp(&aux);
}
#else
//	Linux/macOS
uint64_t	rdtscp(){
    unsigned	int	lo,hi;
    asm	volatile	("rdtscp"	:	"=a"	(lo),	"=d"	(hi));
	return	((uint64_t)hi	<<	32)	|	lo;
}
#endif

using namespace std;
using namespace chrono;

const long long MAX = 1e9;

long double calculo(int i, int qthreads){

    long double pi = 0.0;
    long long int r;
    long double aux = 0.0;
    long double sinal = 1.0;
    int j;
    int limite = MAX/qthreads;
    long int valor = i * limite;
    for(j = ((valor - limite) + 1); j <= limite; j++){
            for(r = 0; r < 1000000000; r++){
                aux = aux + ((sinal)/((2*r+2)*(2*r+3)*(2*r+4)));
                sinal = -sinal;
                }
                pi = 3 + 4*(aux);
                }
    return pi;
}

int main(){

    auto t0	= steady_clock::now();
    int qthreads = 0;

    cout << "Digite o numero de threads: ";
    cin >> qthreads;

    long double vetor[qthreads];
        thread * vt[qthreads];
        for(int i = 1; i <= qthreads; ++i)
        {
            vt[i] = new thread(calculo, i, qthreads);
        }

    /*for(int i = 1; i <= qthreads; i++){
        qthreads.join(thread[i]);
    }*/

    long double soma = 0;

    for(int i = 0; i <= qthreads; i++){
       soma += vetor[i];
    }

    cout << "Pi: " << soma << endl;

    auto d = steady_clock::now() - t0;
    cout <<	duration_cast<milliseconds>(d).count() << " ms" << endl;

    return 0;
}

