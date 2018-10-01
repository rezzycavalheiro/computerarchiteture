#include <iostream>
#include <fstream>

const unsigned long TAM_MEM = 16*1024*1024;
typedef int Word;

using namespace std;

int main(){
unsigned int x [16000000];
ifstream arquivo;
unsigned long address;

arquivo.open("C:/Users/renata.cavalheiro/Resultado.run");
if (!arquivo){
    cerr << "Nao foi possivel abrir o arquivo";
}

 arquivo.close();

 Word mem[TAM_MEM];

}
