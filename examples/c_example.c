#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_USERS 10

typedef struct {
    int id;
    char name[50];
    float balance;
} User;

void deposit(User* user, float amount) {
    if (amount > 0) {
        user->balance += amount;
        printf("Deposited $%.2f to %s\n", amount, user->name);
    }
}

void withdraw(User* user, float amount) {
    if (amount > 0 && user->balance >= amount) {
        user->balance -= amount;
        printf("Withdrew $%.2f from %s\n", amount, user->name);
    }
}

void transfer(User* from, User* to, float amount) {
    if (from->balance >= amount) {
        from->balance -= amount;
        to->balance += amount;
        printf("Transferred $%.2f from %s to %s\n", 
               amount, from->name, to->name);
    }
}

int main() {
    User users[MAX_USERS] = {
        {1, "Alice", 1000.50f},
        {2, "Bob", 500.25f}
    };
    
    deposit(&users[0], 200.75f);
    withdraw(&users[1], 100.50f);
    transfer(&users[0], &users[1], 300.00f);
    
    printf("\nFinal balances:\n");
    for (int i = 0; i < 2; i++) {
        printf("%s: $%.2f\n", users[i].name, users[i].balance);
    }
    
    return 0;
}