# Hearthstone Fatigue Calculator
Just a handy fatigue calculator, pretty useful when you're playing Mill Rogue or similar stuff and you're too lazy to calculate the lethal damage. 

![](https://i.imgur.com/mIbLYWb.png)

## Modes
1. **Lethal mode**: turns needed for X damage
2. **Calculator mode**: damage dealt in X turns

*Note: You get to choose the initial fatigue damage in both modes*

## How it works
The basics of this program are actually a very popular mathematical problem: the [triangular numbers](https://en.wikipedia.org/wiki/Triangular_number). They count objects arranged in an equilateral triangle, as in the diagram on the bottom:

![](https://upload.wikimedia.org/wikipedia/commons/1/1c/First_six_triangular_numbers.svg)

This is basically the sum of the dots of each row in our triangle:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8411fe69f79f2971b7c7a453b0b547bb37e9f6df)

But for fatigue damage, you don't always start at 1 dot. Maybe you're already 3 turns in and you want to calculate the damage left. That's when trapezoidal numbers come into play. You can learn more about them [on this paper by Carlton Gamer, David W. Roeder and John J. Watkins](https://www.jstor.org/stable/2689901?origin=crossref&seq=1#metadata_info_tab_contents).

![](https://i.imgur.com/GsaR1wo.png)

 A trapezoidal triangle can be expressed as the entire triangular number (until `k+l`) minus the small triangular number (until `k`). The formula then can be simplified to:
 
 ![](https://i.imgur.com/vajUmq4.png)
 
 to obtain the trapezoidal number beginning with `k+1`. Now, to find the turns given the total fatigue damage, we could use the solved formula for `l`:

 ![](https://i.imgur.com/wTHGwW9.png)

 But as it's a quadratic equation and not as exact and simple as I'd want it to be, the program is just designed to loop until it finds the requested trapezoidal result. If you think of a better method, don't doubt in opening an issue in this repository and letting me know!
 
Other sources:

* [C. Gamer, D. W. Roeder, and J. J. Watkins, “Trapezoidal Numbers,” Mathematics Magazine, vol. 58, no. 2, pp. 108–110, 1985](https://www.hindawi.com/journals/ijmms/2017/4515249/)
* [R. Guy, “Sums of consecutive integers,” The Fibonacci Quarterly. Official Organ of the Fibonacci Association, vol. 20, no. 1, pp. 36–38, 1982](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.388.5889&rep=rep1&type=pdf)