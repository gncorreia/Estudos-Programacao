using System;
using System.Globalization;


namespace Ex01
{
    class Program
    {
        static void Main(string[] args)
        {            
            Console.WriteLine("Olá, Mundo!");
            Console.WriteLine("Bem vindo!");

            double x = 10.578920463675;
            int y = 32;
            string z = "Maria";
            char w = 'F';
            
            Console.WriteLine(x);

            Console.WriteLine(x.ToString("F2"));
            Console.WriteLine(x.ToString("F4"));

            Console.WriteLine(x.ToString("F2", CultureInfo.InvariantCulture));

            Console.WriteLine();
            Console.WriteLine("RESULTADO = " + x);
            Console.WriteLine("O valor do troco é " + x + " reais");
            Console.WriteLine("O valor do troco é " + x.ToString("F2") + " reais");

            Console.WriteLine();
            Console.WriteLine("A paciente " + z + " tem" + y + " anos e seu sexo é " + w);

            Console.ReadLine();
        }
    }
}
