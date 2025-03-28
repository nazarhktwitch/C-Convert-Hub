#include <iostream>
#include <vector>
#include <string>
#include <memory>

using namespace std;

class BankAccount {
private:
    string owner;
    double balance;
    
public:
    BankAccount(string owner, double balance) 
        : owner(owner), balance(balance) {}
    
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited $" << amount << " to " << owner << "'s account\n";
        }
    }
    
    void withdraw(double amount) {
        if (amount > 0 && balance >= amount) {
            balance -= amount;
            cout << "Withdrew $" << amount << " from " << owner << "'s account\n";
        }
    }
    
    void transferTo(BankAccount& other, double amount) {
        if (balance >= amount) {
            balance -= amount;
            other.balance += amount;
            cout << "Transferred $" << amount << " from " << owner 
                 << " to " << other.owner << endl;
        }
    }
    
    friend ostream& operator<<(ostream& os, const BankAccount& acc) {
        os << "Account owner: " << acc.owner 
           << ", Balance: $" << acc.balance;
        return os;
    }
};

int main() {
    vector<unique_ptr<BankAccount>> accounts;
    accounts.emplace_back(make_unique<BankAccount>("Alice", 1000.50));
    accounts.emplace_back(make_unique<BankAccount>("Bob", 500.25));
    
    accounts[0]->deposit(200.75);
    accounts[1]->withdraw(100.50);
    accounts[0]->transferTo(*accounts[1], 300.00);
    
    cout << "\nFinal account states:\n";
    for (const auto& acc : accounts) {
        cout << *acc << endl;
    }
    
    return 0;
}