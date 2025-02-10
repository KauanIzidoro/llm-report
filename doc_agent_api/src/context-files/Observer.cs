using System;
using System.Collections.Generic;

public interface IObserver
{
    void Update(string message);
}

public interface ISubject
{
    void RegisterObserver(IObserver observer);
    void RemoveObserver(IObserver observer);
    void NotifyObservers(string message);
}

public class Subject : ISubject
{
    private List<IObserver> _observers = new List<IObserver>();

    public void RegisterObserver(IObserver observer)
    {
        if (!_observers.Contains(observer))
        {
            _observers.Add(observer);
        }
    }

    public void RemoveObserver(IObserver observer)
    {
        if (_observers.Contains(observer))
        {
            _observers.Remove(observer);
        }
    }

    public void NotifyObservers(string message)
    {
        foreach (var observer in _observers)
        {
            observer.Update(message);
        }
    }

    public void DoSomethingImportant()
    {
        Console.WriteLine("Subject: Estou fazendo algo importante!");
        NotifyObservers("Algo importante aconteceu!");
    }
}

public class ConcreteObserver : IObserver
{
    private string _name;

    public ConcreteObserver(string name)
    {
        _name = name;
    }

    public void Update(string message)
    {
        Console.WriteLine($"{_name} recebeu a mensagem: {message}");
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Subject subject = new Subject();

        ConcreteObserver observer1 = new ConcreteObserver("Observer 1");
        ConcreteObserver observer2 = new ConcreteObserver("Observer 2");

        subject.RegisterObserver(observer1);
        subject.RegisterObserver(observer2);

        subject.DoSomethingImportant();

        subject.RemoveObserver(observer1);
        subject.DoSomethingImportant();
    }
}