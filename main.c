#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    char EGN[11];
    char names[256];
    unsigned int age;
    unsigned char education;
    unsigned char job_status;
    unsigned char marital_status;
} Person;

void print_menu() {
    printf("1. Add a person\n");
    printf("2. Delete a person\n");
    printf("3. Print all persons\n");
    printf("4. Exit\n");
}

void add_person(FILE *file) {
    Person p;
    printf("Enter EGN: ");
    scanf("%s", p.EGN);
    printf("Enter names: ");
    scanf("%s", p.names);
    printf("Enter age: ");
    scanf("%u", &p.age);
    printf("Enter education level (0-3): ");
    scanf("%hhu", &p.education);
    printf("Enter job status (0-1): ");
    scanf("%hhu", &p.job_status);
    printf("Enter marital status (0-1): ");
    scanf("%hhu", &p.marital_status);
    fwrite(&p, sizeof(Person), 1, file);
}

void delete_person(FILE *file, const char *EGN) {
    FILE *temp_file = tmpfile();
    Person p;
    while (fread(&p, sizeof(Person), 1, file)) {
        if (strcmp(p.EGN, EGN) != 0) {
            fwrite(&p, sizeof(Person), 1, temp_file);
        }
    }
    fseek(file, 0, SEEK_SET);
    fseek(temp_file, 0, SEEK_SET);
    while (fread(&p, sizeof(Person), 1, temp_file)) {
        fwrite(&p, sizeof(Person), 1, file);
    }
    fclose(temp_file);
}

void print_persons(FILE *file) {
    Person p;
    fseek(file, 0, SEEK_SET);
    while (fread(&p, sizeof(Person), 1, file)) {
        printf("EGN: %s\n", p.EGN);
        printf("Names: %s\n", p.names);
        printf("Age: %u\n", p.age);
        printf("Education level: %hhu\n", p.education);
        printf("Job status: %hhu\n", p.job_status);
        printf("Marital status: %hhu\n\n", p.marital_status);
    }
}

int main() {
    char filename[256];
    printf("Enter filename: ");
    scanf("%s", filename);

    FILE *file = fopen(filename, "a+");
    if (file == NULL) {
        printf("Cannot open file\n");
        return 1;
    }

    int choice;
    char EGN[11];
    while (1) {
        print_menu();
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                add_person(file);
                break;
            case 2:
                printf("Enter EGN: ");
                scanf("%s", EGN);
                delete_person(file, EGN);
                break;
            case 3:
                print_persons(file);
                break;
            case 4:
                fclose(file);
                return 0;
            default:
                printf("Invalid choice\n");
        }
    }
}
