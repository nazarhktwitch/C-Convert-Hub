using System;
using System.Collections.Generic;

namespace BankingApp
{
    public class BankAccount
    {
        public string Owner { get; }
        public decimal Balance { get; private set; }
        
        public BankAccount(string owner, decimal balance)
        {
            Owner = owner;
            Balance = balance;
        }
        
        public void Deposit(decimal amount)
        {
            if (amount > 0)
            {
                Balance += amount;
                Console.WriteLine($"Deposited {amount:C} to {Owner}'s account");
            }
        }
        
        public void Withdraw(decimal amount)
        {
            if (amount > 0 && Balance >= amount)
            {
                Balance -= amount;
                Console.WriteLine($"Withdrew {amount:C} from {Owner}'s account");
            }
        }
        
        public void TransferTo(BankAccount other, decimal amount)
        {
            if (Balance >= amount)
            {
                Balance -= amount;
                other.Balance += amount;
                Console.WriteLine($"Transferred {amount:C} from {Owner} to {other.Owner}");
            }
        }
        
        public override string ToString() => 
            $"Account owner: {Owner}, Balance: {Balance:C}";
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            var accounts = new List<BankAccount>
            {
                new BankAccount("Alice", 1000.50m),
                new BankAccount("Bob", 500.25m)
            };
            
            accounts[0].Deposit(200.75m);
            accounts[1].Withdraw(100.50m);
            accounts[0].TransferTo(accounts[1], 300.00m);
            
            Console.WriteLine("\nFinal account states:");
            foreach (var acc in accounts)
            {
                Console.WriteLine(acc);
            }
        }
    }
}