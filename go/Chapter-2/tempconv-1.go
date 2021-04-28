/*
Example of Type Conversion
package tempconv performs Celsius and Fahrenheit temperature computations.
*/

package main

import "fmt"

type Celsius float64
type Faherenheit float64

const (
	AbsoluteZeroC Celsius = -273.15
	FreezingC     Celsius = 0
	BoilingC      Celsius = 100
)

func main() {
	fmt.Printf("%g\n", BoilingC-FreezingC)
	BoilingF := CToF(BoilingC)
	fmt.Printf("%g\n", BoilingF-CToF(FreezingC))
	fmt.Printf("%g\n", BoilingC-FreezingC)
}

func CToF(c Celsius) Faherenheit { return Faherenheit(c*9/5 + 32) }
func FToC(f Faherenheit) Celsius { return Celsius((f - 32) * 5 / 9) }
