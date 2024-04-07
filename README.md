# Exploring Integral Velocity Equation of Chemistry Reaction

### This is a repository to share the process of exploring the Chemistry Integral Velocity Equation, and if there are any improvements or errors, please feel free to open the issue 😊

## Chemistry II Exploration Performance Tasks for the 1st Semester of 2024

## Reason For Selection
When a chemical reaction occurs, given concentration data over time, it was explored to obtain the order of reaction.

## Proof the integral velocity equation
- Zero Order Reaction
```math
\displaylines{v = -{d[A] \over dt}, v = k \\ \therefore -{d[A] \over dt} = k \\ \therefore d[A] = -k \ dt \\ \int_{[A]_0}^{[A]_t} d[A] = -k \ \int_{0}^{t} dt \\ \therefore\underline{[A]_t = -kt + [A]_0}}
```

- First Order Reaction
```math
\displaylines{v = -{d[A] \over dt}, v = k[A] \\ \therefore -{d[A] \over dt} = k[A] \\ \therefore {1 \over [A]} d[A] = -k \ dt \\ \int_{[A]_0}^{[A]_t} {1 \over [A]} d[A] = -k \ \int_{0}^{t} dt \\ \therefore\underline{\ln{[A]_t} = -kt + \ln{[A]_0}}}
```

- Second or more nth Order Reaction
```math
\displaylines{v = -{d[A] \over dt}, v = k[A]^{n} \\ \therefore -{d[A] \over dt} = k[A]^{n} \\ \therefore {1 \over [A]^{n}} d[A] = -k \ dt \\ \int_{[A]_0}^{[A]_t} {1 \over [A]^{n}} d[A] = -k \ \int_{0}^{t} dt \\ \therefore\underline{{1 \over {[A]_t}^{n-1}} = (n-1)kt + {1 \over {[A]_0}^{n-1}}}}
```

## Development Environment
- Macbook Pro, Sonoma OS 14.3.1 (23D60)
- Python 3.11.6

## Installation & Usage
- MacOS, Linux, (etc..)
```bash
pip3 install --upgrade -r requirements.txt
```
if this doesn't work, try
```bash
python3 -m pip install --upgrade -r requirements.txt
```
```bash
python3 main.py 
```

- Windows
```bash
pip install --upgrade -r requirements.txt
```
```bash
python main.py 
```
