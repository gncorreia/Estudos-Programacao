using System;

namespace Ex03
{
    class Program
    {
        static void Main(string[] args)
        {
            
            string frase = Console.ReadLine();
            string x = Console.ReadLine();
            string y = Console.ReadLine();
            string z = Console.ReadLine();

            //string s = Console.ReadLine();

            // string[] vet = s.Split(' '); // separou a string em vetores

            // pode fazer desse jeito tbm que da o mesmo resultado:
            string[] vet = Console.ReadLine().Split(' ');

            string a = vet[0]; // distribuiu esse vetores em outras variáveis
            string b = vet[1];
            string c = vet[2];

            Console.WriteLine("Você Digitou: ");
            Console.WriteLine(frase);
            Console.WriteLine(x);
            Console.WriteLine(y);
            Console.WriteLine(z);
            Console.WriteLine(a);
            Console.WriteLine(b);
            Console.WriteLine(c);
        }
    }
}
