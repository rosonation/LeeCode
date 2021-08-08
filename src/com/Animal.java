package com;

public class Animal {
    public Animal() {
        move();
    }
    public void move() {
        String name = "Animal";
        System.out.println("Animal move : " + name);
    }
}

class Cat extends Animal {
    public void move() {
        String name = "Cat";
        System.out.println("Cat move : " + name);
    }

    public static void main(String[] args) {
        new Cat();
    }
}
