using System;

namespace Aula03
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.SetCursorPosition(20, 5);
            Console.WriteLine("Hello World!");
            Console.ReadKey();
            Console.Clear();
            
            Console.BackgroundColor = ConsoleColor.White;
            Console.ForegroundColor = ConsoleColor.Black;
            Console.WriteLine("\\Oi, Tudo bem?\\");
            Console.WriteLine(@"\Oi, Tudo bem?\");
            Console.Write("\"Olá, mundo\"");
            Console.ResetColor();            
            Console.ReadKey();
            Console.Clear();

            Console.ForegroundColor = ConsoleColor.Green;           
            Console.WriteLine("C# é \n\"SUPER\"\nFácil!\a");            
            Console.ReadKey();
            Console.Clear();

        }
    }
}
