package com.rosonation.java;

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
    public static void main(String[] args) {
        new Cat();
    }

    public void move() {
        String name = "Cat";
        System.out.println("Cat move : " + name);
    }
}
