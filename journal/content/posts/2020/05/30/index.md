---
title: "Octave"
date: 2020-05-30T09:45:38+01:00
description: ""
categories: ["coursera", "octave"]
tags: []
toc: true
dropCap: true
displayInMenu: false
displayInList: true
---

Today we are going to cover Octave, and this is a quick intro on Octave for submitting the programming assignment.
The syntax is Matlab-like, and I will probably port to python later on.

## Documentation

```octave
>> help eye
'eye' is a built-in function from the file libinterp/corefcn/data.cc

 -- eye (N)
 -- eye (M, N)
 -- eye ([M N])
 -- eye (..., CLASS)
     Return an identity matrix.

     If invoked with a single scalar argument N, return a square NxN
     identity matrix.

     If supplied two scalar arguments (M, N), 'eye' takes them to be the
     number of rows and columns.  If given a vector with two elements,
     'eye' uses the values of the elements as the number of rows and
     columns, respectively.  For example:

          eye (3)
           =>  1  0  0
               0  1  0
               0  0  1

     The following expressions all produce the same result:

          eye (2)
          ==
          eye (2, 2)
          ==
          eye (size ([1, 2; 3, 4]))

     The optional argument CLASS, allows 'eye' to return an array of the
     specified type, like

          val = zeros (n,m, "uint8")

     Calling 'eye' with no arguments is equivalent to calling it with an
     argument of 1.  Any negative dimensions are treated as zero.  These
     odd definitions are for compatibility with MATLAB.

     See also: speye, ones, zeros.

Additional help for built-in functions and operators is
available in the online version of the manual.  Use the command
'doc <topic>' to search the manual index.

Help and information about Octave is also available on the WWW
at https://www.octave.org and via the help@octave.org
mailing list.
>>
```

## Interface

```octave
% This is a comment
```

```octave
% change prompt from octave:1> to >>
octave:1> PS1('>> ');
>> 
```

```octave
% assign variable and semicolon supressing output
>> a = 3
a =  3
>> a = 3;
>>
>> b = 'hi';
>> b
b = hi
>>
>> c = (3>=1);
>> c
c = 1
>>
>> d = pi;
>> d
d =  3.1416
>>
```

```octave
# stdout
>> a = pi;
>> disp(a);
 3.1416
>> disp(sprintf('2 decimals: %0.2f', a))
2 decimals: 3.14
>> disp(sprintf('6 decimals: %0.6f', a))
6 decimals: 3.14159
>>
```

```octave
# default format
>> a = pi;
>> a
a =  3.1416
>> format long
>> a
a =  3.141592653589793
>> format short
>> a
a =  3.1416
>>
```

## Arithmetic operations

```octave
>> 5+6
ans =  11
>> 3-2
ans =  1
>> 5*8
ans =  40
>> 1/2
ans =  0.50000
>> 2^6
ans =  64
```

## (Ine|E)quality

```octave
>> 1 == 2
ans = 0
>> 1 ~= 2
ans = 1
```

## Logic

```octave
>> 1 && 0
ans = 0
>> 1 || 0
ans = 1
>> xor(1,0)
ans = 1
```

## Matrix & Vector

```octave
>> A = [1 2; 3 4; 5 6]
A =

   1   2
   3   4
   5   6

>>
>> B = [1 2; % enter for newline here
> 3 4;
> 5 6]
B =

   1   2
   3   4
   5   6

>>
```

```octave
>> v = [1 2 3]
v =

   1   2   3

>> v = [1; 2; 3]
v =

   1
   2
   3

>>
```

```octave
% create vector from 1 to 2, increment 0.1 for each step
>> v = 1:0.1:2
v =

 Columns 1 through 7:

    1.0000    1.1000    1.2000    1.3000    1.4000    1.5000    1.6000

 Columns 8 through 11:

    1.7000    1.8000    1.9000    2.0000

>>
% create vector from 1 to 6, default increment 1 for each step
>> v = 1:6
v =

   1   2   3   4   5   6

>>
```

```octave
% generate 2*3 matrix, filled by 1s
>> ones(2,3)
ans =

   1   1   1
   1   1   1

>>
% generate 2*3 matrix, filled by 1s,
% then mutiply 2 and assign to the valiable C
>> C = 2*ones(2,3)
C =

   2   2   2
   2   2   2

>>
% zero 1*3 matrix
>> w = zeros(1,3)
w =

   0   0   0

>>
% generate 3*3 matrix filled with random numbers between 0 and 1
>> w = rand(3,3)
w =

   0.3449646   0.5964889   0.3440872
   0.2568673   0.9458705   0.3747054
   0.4332061   0.2943530   0.0073413

>>
% generate 1*3 matrix filled with random numbers drawn
% from a Gaussian distribution with mean 0 and variance
% or standard deviation equal to 1
>> w = randn(1,3)
w =

  -0.234578   0.037919  -1.420126

>>
% generate a 4*4 identity matrix
>> I = eye(4)
I =

Diagonal Matrix

   1   0   0   0
   0   1   0   0
   0   0   1   0
   0   0   0   1

>>
% get size of a matrix
>> A = [1 2; 3 4; 5 6];
>> A
A =

   1   2
   3   4
   5   6

>> size(A)
ans =

   3   2

>> size(A,1)
ans =  3
>> size(A,2)
ans =  2
>>
```

## Histogram

```octave
% generate 10000 random elements
>> w = -6 + sqrt(10)*(randn(1,10000));
>> hist(w)
>>
```

{{< smallimg src="histogram1.png" alt="histogram" >}}

```octave
% add more bins
>> hist(w,50)
>>
```

{{< smallimg src="histogram2.png" alt="histogram" >}}

## Load Data

```octave
% similar to *nix commands
>> pwd
ans = /Users/simon/some/path
>> ls
featuresX.dat	priceY.dat
```

```octave
% load data file into memory, as variable featuresX and priceY
>> load featuresX.dat
>> load priceY.dat
>> who
Variables in the current scope:

ans        featuresX  priceY

>>
>> whos
Variables in the current scope:

   Attr Name           Size                     Bytes  Class
   ==== ====           ====                     =====  =====
        ans            1x2                         16  double
        featuresX     27x2                        432  double
        priceY        27x1                        216  double

Total is 83 elements using 664 bytes

>>
```

```octave
% remove a variable from memory
>> clear featuresX
>> whos
Variables in the current scope:

   Attr Name        Size                     Bytes  Class
   ==== ====        ====                     =====  =====
        ans         1x2                         16  double
        priceY     27x1                        216  double

Total is 29 elements using 232 bytes

>>
```

```octave
% Get the first 10 items from priceY
>> v = priceY(1:10)
v =

   3999
   3299
   3690
   2320
   5399
   2999
   3149
   1989
   2120
   2425

>>
% Save and export the variable v to a file in binary format
>> save hello.mat v;
>>
% Save and export the variable v to a file in ASCII format
>> save hello.txt v -ascii;
>>
```

## Manipulate Data

```octave
% note that index start from 1
>> A = [1 2; 3 4; 5 6]
A =

   1   2
   3   4
   5   6

>> A(3,2)
ans =  6
>>
% ":" means every element along that row/column
>> A(3,:)
ans =

   5   6

>>
>> A(:,2)
ans =

   2
   4
   6

>>
% get all elements in row 1 and 3
>> A([1 3],:)
ans =

   1   2
   5   6

>>
```

```octave
% range assignment
>> A(:,2) = [10; 11; 12]
A =

    1   10
    3   11
    5   12

>>
% append new column to the right
>> A = [A, [100; 101; 102]]
A =

     1    10   100
     3    11   101
     5    12   102

>>
% put all elements into a single vector
>> A(:)
ans =

     1
     3
     5
    10
    11
    12
   100
   101
   102

>>
% merge matrice
>> A = [1 2; 3 4; 5 6]
A =

   1   2
   3   4
   5   6

>> B = [11 12; 13 14; 15 16]
B =

   11   12
   13   14
   15   16

>> C = [A B]
C =

    1    2   11   12
    3    4   13   14
    5    6   15   16

>> D = [A; B]
D =

    1    2
    3    4
    5    6
   11   12
   13   14
   15   16

>>
```

## Computing on Data

```octave
% matrix multiplication
>> A = [1 2; 3 4; 5 6]
A =

   1   2
   3   4
   5   6

>> B = [11 12; 13 14; 15 16]
B =

   11   12
   13   14
   15   16

>> C = [1 1; 2 2]
C =

   1   1
   2   2

>> A*C
ans =

    5    5
   11   11
   17   17

>>
```

In general, `.` means **element-wise** operation.

```octave
>> A
A =

   1   2
   3   4
   5   6

>> B
B =

   11   12
   13   14
   15   16

>>
% element-wise multiplication
>> A .* B
ans =

   11   24
   39   56
   75   96

>>
% other element-wise operations
>> A .^ 2
ans =

    1    4
    9   16
   25   36

>>
>> 1 ./ A
ans =

   1.00000   0.50000
   0.33333   0.25000
   0.20000   0.16667

>>
% build-in functions
>> log(A)
ans =

   0.00000   0.69315
   1.09861   1.38629
   1.60944   1.79176

>>
>> exp(A)
ans =

     2.7183     7.3891
    20.0855    54.5982
   148.4132   403.4288

>>
>> V = [1 15 2 0.5]
V =

    1.00000   15.00000    2.00000    0.50000

>>
>> max(V)
ans =  15
>>
>> [value, index] = max(V)
value =  15
index =  2
>>
% element-wise comparison, get boolean result
>> V < 3
ans =

  1  0  1  1

>>
% element-wise comparison, get index
>> find(V < 3)
ans =

   1   3   4

>>
% element-wise comparison, get index
>> [row,column] = find(A >= 4)
row =

   3
   2
   3

column =

   1
   2
   2

>>
% meaning A(3,1), A(2,2) and A(3,3) >= 4
>> -A
ans =

  -1  -2
  -3  -4
  -5  -6

>>
>> abs(-A)
ans =

   1   2
   3   4
   5   6

>>
>> A+1
ans =

   2   3
   4   5
   6   7

>>
>> sum(V)
ans =  18.500
>>
>> prod(V)
ans =  15
>>
>> floor(V)
ans =

    1   15    2    0

>>
>> ceil(V)
ans =

    1   15    2    1

>>
% matrix transpose
>> A'
ans =

   1   3   5
   2   4   6

>>
```

```octave
% create an N-by-N magic square
>> M = magic(3)
M =

   8   1   6
   3   5   7
   4   9   2

>>
% inverse of a Matrix
>> pinv(M)
ans =

   0.147222  -0.144444   0.063889
  -0.061111   0.022222   0.105556
  -0.019444   0.188889  -0.102778

>>
```

## Plotting Data

```octave
>> t = [0:0.01:0.98];
>> y1 = sin(2*pi*4*t);
>> plot(t,y1);
>>
```

{{< smallimg src="graph1.png" alt="sin" >}}

```octave
>> y2 = cos(2*pi*4*t);
>> plot(t,y2);
>>
```

{{< smallimg src="graph2.png" alt="cos" >}}

```octave
>> plot(t,y1);
>> hold on; % presist the current grpah
>> plot(t,y2,'r'); % change colour to red
>> xlabel('time')
>> ylabel('value')
>> legend('sin','cos')
>> title('my plot')
>> print -dpng 'myPlot.png' % save as png
>>
>> close % close the plot window from octave
>>
```

{{< smallimg src="myPlot.png" alt="sin and cos with labels" >}}

```octave
% multiple plot windows
>> figure(1); plot(t,y1);
>> figure(2); plot(t,y2);
>>
```

{{< smallimg src="graph3.png" alt="multiple plot" >}}

```octave
% divides plot into a 1x1 grid, access first element
>> subplot(1,2,1);
>> plot(t,y1);
% access second element
>> subplot(1,2,2);
>> plot(t,y2);
>>
```

{{< smallimg src="graph4.png" alt="subplot" >}}

```octave
% set axis in the format ([X_LO X_HI Y_LO Y_HI])
>> axis([0.5 1 -1 1])
>>
```

{{< smallimg src="graph5.png" alt="subplot with updated axis scale" >}}

```octave
% clear graph
>> clf;
>>
```

We can also use colour to represent the values in a matrix.

```octave
>> M = magic(5)
M =

   17   24    1    8   15
   23    5    7   14   16
    4    6   13   20   22
   10   12   19   21    3
   11   18   25    2    9

>> imagesc(M)
```

{{< smallimg src="colour1.png" alt="colour" >}}

```octave
% run three commands in one go (comma chaining)
% with colour bar and greyscale
>> imagesc(M), colorbar, colormap gray;
```

{{< smallimg src="colour2.png" alt="colour" >}}

```octave
% let's try a larger matrix
>> imagesc(magic(15)), colorbar, colormap gray;
```

{{< smallimg src="colour3.png" alt="colour" >}}

## Control Statements

### for-loop

```octave
>> v = zeros(10,1)
v =

   0
   0
   0
   0
   0
   0
   0
   0
   0
   0

% space is optional here, but better for readability
>> for i = 1:10,
>    v(i) = 2^i;
>  end;
>>
>> v
v =

      2
      4
      8
     16
     32
     64
    128
    256
    512
   1024

>>
```

### while-loop

```octave
% continue from the for-loop
>> i = 1;
>> while i <= 5,
>    v(i) = 100;
>    i = i + 1;
>  end;
>>
>> v
v =

    100
    100
    100
    100
    100
     64
    128
    256
    512
   1024

>>
```

### if

```octave
% continue from the while-loop
>> i = 1;
>> while true,
>    v(i) = 999;
>    i = i + 1;
>    if i == 6,
>      break;
>    end;
>  end;
>>
>> v
v =

    999
    999
    999
    999
    999
     64
    128
    256
    512
   1024

>>
```

We can also use `elseif` and `else` keywords for the `if`.

## Function

Function file should put into the working directory, i.e. run the `pwd` command.

For example, this function indicates that it will return a value `y`.

`squareThisNumber.m`
```octave
function y = squareThisNumber(x)

y = x^2;
```

Octave will automatically locate the function in the directory. Hence:

```octave
>> pwd
ans = /Users/simon/some/path
>> squareThisNumber(5)
ans =  25
```

Octave can also return multiple values in a function.

`squareAndCubeThisNumber.m`
```octave
function [y1,y2] = squareAndCubeThisNumber(x)

y1 = x^2;
y2 = x^3;
```

```octave
>> [a,b] = squareAndCubeThisNumber(5);
>> a
a =  25
>> b
b =  125
```

Another example of plotting the cost function `J` by an Octave function:

### Practical Example - Cost Function

`costFunctionJ.m`
```octave
function J = costFunctionJ(X, y, theta)

% X is the "design matrix" containing our training examples.
% y is the class labels

% number of training examples
m = size(X, 1);
% predictions of hypothesis on all m examples
predictions = X * theta;
% squared errors
sqrErrors = (predictions - y) .^ 2;

J = 1 / ( 2 * m ) * sum(sqrErrors);
```

```octave
>> X = [1 1; 1 2; 1 3];
>> y = [1; 2; 3];
>> theta = [0; 1];
>> j = costFunctionJ(X, y, theta)
j = 0
>>
>> theta = [0; 0];
>> j = costFunctionJ(X, y, theta)
j =  2.3333
>>
```

## Vectorisation

In general, use the built-in library or library for linear algebra to avoid for-loop.

Not quite understand the math here, need to revisit.

{{< smallimg src="vectorisation.png" alt="Coursera Machine Learning by Andrew Ng" >}}

## Quiz

{{< smallimg src="quiz.png" alt="quiz result" >}}

Hmm, made two mistakes and both of them related to Computing on Data. Revisit tomorrow...
