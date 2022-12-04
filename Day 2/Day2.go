package main

import (
	"fmt"
	"log"
	"os"
)

func main() {

	input, err := os.ReadFile("Day2_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	for i := 0; i <= 2; i++ {
		fmt.Println(input[i])
	}
}
