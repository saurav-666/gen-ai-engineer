using System;

namespace ShapeAreaCalculator
{
    public class ShapeCalculator
    {
        public double CalculateCircleArea(double radius)
        {
            return Math.PI * radius * radius;
        }

        public double CalculateRectangleArea(double length, double width)
        {
            return length * width;
        }

        public double CalculateTriangleArea(double baseLength, double height)
        {
            return 0.5 * baseLength * height;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            ShapeCalculator calculator = new ShapeCalculator();

            double circleArea = calculator.CalculateCircleArea(5);
            Console.WriteLine($"Circle Area: {circleArea}");

            double rectangleArea = calculator.CalculateRectangleArea(4, 6);
            Console.WriteLine($"Rectangle Area: {rectangleArea}");

            double triangleArea = calculator.CalculateTriangleArea(3, 7);
            Console.WriteLine($"Triangle Area: {triangleArea}");
        }
    }
}