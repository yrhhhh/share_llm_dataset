Article

# Structural Design and Optimization of a Resonant Micro-Accelerometer Based on Electrostatic Stiffness by an Improved Differential Evolution Algorithm

Libin Huang $^{1,2,\ast}$ , Qike Li $^{1,2}$ , Yan Qin $^{1,2}$ , Xukai Ding $^{1,2}$ , Meimei Zhang $^{1,2}$ and Liye Zhao $^{1,2}$

$^{1}$ School of Instrument Science and Engineering, Southeast University, Nanjing 210096, China; 220203477@seu.edu.cn (Q.L.); qhh12zhh@163.com (Y.Q.); ding.xk@seu.edu.cn (X.D.); 220193328@seu.edu.cn (M.Z.); liyezhao@seu.edu.cn (L.Z.)   
2 Key Laboratory of Micro-Inertial Instruments and Advanced Navigation Technology, Ministry of Education, Nanjing 210096, China   
* Correspondence: huanglibin@seu.edu.cn

![](images/e680421b5848a7560e07fc2311d3aed71f8727541caa7fe241e3fa4578f31704.jpg)

# check for updates

Citation: Huang, L.; Li, Q.; Qin, Y.; Ding, X.; Zhang, M.; Zhao, L. Structural Design and Optimization of a Resonant Micro-Accelerometer Based on Electrostatic Stiffness by an Improved Differential Evolution Algorithm. Micromachines 2022, 13, 38 https://doi.org/10.3390/mi13010038

Academic Editors: Yang Liu, Regina Luttge, Marisa Manzano, Beatrix Jurado Sánchez, Anna Vikulina and Ioanna Zergioti

Received: 2 December 2021  
Accepted: 24 December 2021  
Published: 28 December 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/116cfa461e91ba30c0e1cb25d3c2ed5a2ce7e0bf083eb7a6b4d3f88e5acb1df6.jpg)

Copyright: © 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

Abstract: This study designed an in-plane resonant micro-accelerometer based on electrostatic stiffness. The accelerometer adopts a one-piece proof mass structure; two double-folded beam resonators are symmetrically distributed inside the proof mass, and only one displacement is introduced under the action of acceleration, which reduces the influence of processing errors on the performance of the accelerometer. The two resonators form a differential structure that can diminish the impact of common-mode errors. This accelerometer realizes the separation of the introduction of electrostatic stiffness and the detection of resonant frequency, which is conducive to the decoupling of accelerometer signals. An improved differential evolution algorithm was developed to optimize the scale factor of the accelerometer. Through the final elimination principle, excellent individuals are preserved, and the most suitable parameters are allocated to the surviving individuals to stimulate the offspring to find the globally optimal ability. The algorithm not only maintains the global optimality but also reduces the computational complexity of the algorithm and deterministically realizes the optimization of the accelerometer scale factor. The electrostatic stiffness resonant micro-accelerometer was fabricated by deep dry silicon-on-glass (DDSOG) technology. The unloaded resonant frequency of the accelerometer resonant beam was between 24 and $26\mathrm{kHz}$ , and the scale factor of the packaged accelerometer was between 54 and $59\mathrm{Hz/g}$ . The average error between the optimization result and the actual scale factor was $7.03\%$ . The experimental results verified the rationality of the structural design.

Keywords: resonant accelerometer; electrostatic stiffness; structural design; differential evolution algorithm

# 1. Introduction

As a kind of micro-electro-mechanical system (MEMS) accelerometer, a silicon resonant micro-accelerometer has the advantages of a direct digital signal output, high sensitivity, high resolution, wide dynamic range, strong anti-interference ability, and good stability [1-5]. It has the advantage of being useable to develop a higher-precision microelectromechanical accelerometer. The electrostatic stiffness resonant micro-accelerometer combines electrostatic stiffness with the resonance principle. The resonant frequency is affected by the change in electrostatic stiffness, which greatly reduces the dependence of the device performance on processing errors [6].

At present, there are two main types of resonant accelerometers based on electrostatic stiffness: in-plane and out-of-plane [7-10] detection. The in-plane electrostatic stiffness resonant micro-accelerometer mainly has two structural forms: one is a structure in which the proof mass and the resonator are independent [6,11-17], and the other is a structure in

which the proof mass is a component of the resonator [18-20]. The first type of accelerometer is composed only of a double-ended tuning fork (DETF) and two proof masses. In terms of structure, the two proof masses and the resonator are independent of each other. The two beams of the DETF are electrically connected to the two masses by means of small parallel plate capacitors. This structure is simple and implementable. In the second type of accelerometer, the proof mass is an integral part of the resonator. The reverse arrangement of the two resonators is realized by the reverse arrangement of the electrostatic negative stiffness plate capacitor. The acceleration is calculated by the difference in the frequency of the two resonators. Each resonator is composed of two proof masses, and the in-phase and anti-phase vibration modes of the two proof masses are used for sensitive mode and modulation mode, respectively. Although the difficulty of designing sensitive structures is increased, the multiplexing of proof masses and resonators can better save the layout of sensitive structures.

The structure's performance is determined by the structure itself, so the design and improvement of the micro-accelerometer structure have become one of the hot directions in the field of micro-accelerometer research. There are two main ideas for the structural design of the micro-accelerometer. One is to verify the rationality of the structural design by simulating the structure with finite element analysis software based on rich design experience and experiments. The relationship between performance indexes and key structural parameters is investigated through simulation. The optimization of the structural parameter values is realized by comprehensive consideration. This method can design structures that meet certain performance requirements, but it is difficult to find structures that meet the optimal performance. The other is to establish the mathematical model of the optimization problem according to the structural optimization theory and seek the optimal structural parameters that meet some design requirements under certain constraints. For example, Pei et al. [21] combined the zero-order method and the gradient search method to complete the coarse and exact optimization. The scalar factor of the optimized quartz beam accelerometer improved $16\%$ , which improved the performance of the accelerometer. Wang and Zhao et al. [22] aimed at the piezoelectric accelerometer with high sensitivity. The beam configuration of the accelerometer with high sensitivity and low stress characteristics is obtained by means of a genetic algorithm. Wang et al. [23] used genetic algorithms to optimize the design of the flexible structure of the mechanically amplified MEMS accelerometer, which greatly improved the bandwidth and sensitivity of the accelerometer. In Pak's research [24], a sensor noise model was developed for two MEMS accelerometers with the same topology, and the noise performance of the accelerometer was improved using the MOEA/D evolution algorithm optimization. Zhang and Shi [25] obtained the final optimized model by the NSGA-II algorithm using a combination of OSF-based and Kriging agent models. The optimized accelerometer size was reduced by $29.33\%$ , and its resonant frequency and sensitivity were improved.

Based on the first type of accelerometer, we designed an in-plane electrostatic stiffness resonant micro-accelerometer. The accelerometer adopts a one-piece proof mass structure; two double-folded beam resonators are symmetrically distributed inside the proof mass. Only one displacement of the proof mass is introduced under acceleration, which reduces the influence of the processing error on the accelerometer performance. The two resonators form a differential structure, which can reduce the impact of common-mode errors. The structure realizes the separation of electrostatic stiffness introduction and resonant frequency detection, which is conducive to the decoupling of accelerometer signals and simplifies the design of accelerometer circuits.

The differential evolution algorithm is introduced to optimize the scale factor of the accelerometer. An improved differential evolution algorithm was developed to save the better individuals through the principle of last elimination and assign the most suitable algorithm parameters to the surviving individuals in order to stimulate the ability of the offspring individuals to find the global optimum. While maintaining the global optimality, the

complexity of the algorithm is reduced. The parameters achieved the optimal configuration, and the structural optimization of the accelerometer was deterministically realized.

# 2. Structural Design of a Resonant Micro-Accelerometer Based on Electrostatic Stiffness

# 2.1. Overall Structure Design

The overall structure of the new resonant micro-accelerometer based on electrostatic stiffness is shown in Figure 1. Two perfectly symmetrical double-folded beam resonators are contained in the accelerometer. The driving and detection of a single resonant beam are performed by two sets of comb capacitors, respectively, and the parallel plate capacitor is used only to adjust the resonant beam stiffness. The above capacitor design realizes the separation of electrostatic stiffness introduction and resonant frequency detection. During operation, the resonant beam is connected to the carrier signal, and the fixed driving comb capacitor is connected to the reverse AC voltage with DC bias to drive the resonant beam to the resonant state. Another DC voltage is applied to the proof mass to generate the voltage difference of the parallel plate capacitor, which introduces electrostatic negative stiffness for the tuning fork beam. Each resonator provides two sets of driving combs and detecting combs. One set of resonator driving combs is connected to voltage $V_{a1} = V_{c}\sin\omega t + V_{d}$ , and the other set is connected to $V_{a2} = -V_{c}\sin\omega t + V_{d}$ . Thus, $V_{a1}^2 - V_{a2}^2 \propto \sin\omega t$ , and the driving force is a sinusoidal harmonic force. The accelerometer adopts a one-piece proof mass structure. Two resonators are symmetrically distributed inside the proof mass to form a differential structure, reducing the influence of common-mode errors. The proof mass only introduces one displacement under the action of acceleration, which reduces the influence of manufacturing errors on the performance of the accelerometer.

![](images/9990fb461c15db54f766e01eb694ee75ddaaad1a578007355f03590da260140f.jpg)  
Figure 1. Schematic diagram of the overall structure of the accelerometer.

Since the accelerometer proof mass adopts a one-piece structure, when there is no acceleration, the proof mass is subjected to two electrostatic forces of equal magnitude and opposite direction, the proof mass is in a static initial position, the electrostatic stiffnesses introduced by two resonators are equal. The resonant frequencies of two resonators are equal and the output of the accelerometer is zero. When the accelerometer is sensitive to acceleration, the proof mass is displaced under the action of inertial force. The gap of the parallel plate capacitors between the mass and a resonator increase, and the electrostatic stiffness decreases, which increases the resonant frequency. At the same time, the gap of

the parallel plate capacitors between the proof mass and the other resonator reduces, and the electrostatic stiffness increases, which reduces the resonant frequency. The resonant frequency difference of two resonators is used as the output of the accelerometer, which is approximately linear with the input acceleration.

# 2.2. Theoretical Analysis

For dynamic analysis of a resonator, the vibration equation of a single resonant beam can be expressed as [13,14]

$$
m \ddot {y} + c \dot {y} + k y = F _ {d} + F _ {e} \tag {1}
$$

where $m$ is the effective mass of the resonant beam vibrating transversely, $c$ is the vibration damping coefficient, $k$ is the effective mechanical stiffness of the resonant beam, $y$ is the resonant beam vibration mode coordinate, $F_{d}$ is the driving force generated by the driving comb capacitor in the resonant beam vibration direction, and $F_{e}$ is the electrostatic force generated by the parallel plate capacitor in the resonant beam vibration direction.

Substituting specific expressions of $F_{d}$ and $F_{e}$ into Equation (1), ignoring higher terms and combining like terms, we have [13,26]

$$
m \ddot {y} + c \dot {y} + \left(k - k _ {e}\right) y = \frac {N \varepsilon h}{2 d _ {0}} V _ {a} ^ {2} - \frac {\varepsilon A V _ {s} ^ {2}}{2 g _ {0} ^ {2}} \tag {2}
$$

where $N$ is the number of driving comb capacitor pairs, $\varepsilon$ is the dielectric constant, $h$ is the effective thickness of the driving comb capacitor, $d_{0}$ is the gap of the driving comb capacitor pole plates, $V_{a}$ is the driving voltage of the comb structure, $A = N_{S}hl$ is the orthogonal area of the parallel plate structure, $N_{S}$ is the number of parallel plate capacitor pairs, $l$ is the effective length of each pair of parallel plates, $g_{0}$ is the static initial gap of a single parallel plate capacitor, $V_{s}$ is the potential difference between the resonant beam and the parallel plate, and $k_{e} = \frac{\varepsilon AV_{s}^{2}}{g_{0}^{3}}$ is the electrostatic stiffness. When a potential difference exists between the resonant beam and the proof mass, the electrostatic negative stiffness is generated to make the resonant beam stiffness weaker and reduce its resonant frequency.

Let $y_{1}$ be the displacement corresponding to the change in the $y$ -direction of the resonant beam under the action of electrostatic force when the acceleration is zero. $\Delta y_{1}$ is the displacement of the resonant beam in the $y$ -direction relative to $y_{1}$ under the action of electrostatic force when the acceleration is not zero. Unlike other accelerometers, this accelerometer adopts a single proof mass structure. When there is no acceleration, the proof mass is subjected to two electrostatic forces of equal magnitude and opposite directions. In this case, the displacement of the proof mass-support beam system in the $y$ -direction is 0. Let $\Delta y_{2}$ be the displacement of the proof mass-support beam system in the $y$ -direction when the acceleration is not 0. When the accelerometer is operating, a DC voltage $V_{s}$ is applied at the proof mass anchor, the driving comb is connected to $V_{a1} = V_{c}\sin\omega t + V_{d}$ , and the resonant beam is connected to a square wave signal $V_{f}$ . The output frequency $f_{e1}$ can be expressed as [14]

$$
f _ {e 1} = \frac {1}{2 \pi} \sqrt {\frac {k - \frac {\varepsilon A V _ {s} ^ {2}}{\left(g _ {0} + \Delta y _ {2} - y _ {1} + \Delta y _ {1}\right) ^ {3}}}{m}} \tag {3}
$$

Similarly, the output frequency $f_{e2}$ of the other resonator can be expressed as

$$
f _ {e 2} = \frac {1}{2 \pi} \sqrt {\frac {k - \frac {\varepsilon A V _ {s} ^ {2}}{\left(g _ {0} - \Delta y _ {2} - y _ {1} - \Delta y _ {1}\right) ^ {3}}}{m}} \tag {4}
$$

Through calculation and simplification [13,26], we can obtain

$$
\left\{ \begin{array}{r l} f _ {e 1} & = \frac {1}{2 \pi} \sqrt {\frac {k - \frac {\varepsilon A V _ {S} ^ {2}}{g _ {0} ^ {3} \left(1 + \frac {\Delta y _ {2}}{g _ {0}}\right) ^ {3}}}{m}} = f _ {0} \sqrt {1 - \frac {\beta}{\left(1 + \alpha\right) ^ {3}}} \\ & \approx f _ {0} (\sqrt {1 - \beta} + \frac {3}{2} \frac {\beta}{\sqrt {1 - \beta}} \alpha - \frac {3}{4} (\frac {3 \beta^ {2}}{\sqrt {(1 - \beta) ^ {3}}} + \frac {8 \beta}{\sqrt {(1 - \beta)}}) \alpha^ {2} + o (\alpha^ {2})) \\ f _ {e 2} & = \frac {1}{2 \pi} \sqrt {\frac {k - \frac {\varepsilon A V _ {S} ^ {2}}{g _ {0} ^ {3} \left(1 - \frac {\Delta y _ {2}}{g _ {0}}\right) ^ {3}}}{m}} = f _ {0} \sqrt {1 - \frac {\beta}{\left(1 - \alpha\right) ^ {3}}} \\ & \approx f _ {0} (\sqrt {1 - \beta} - \frac {3}{2} \frac {\beta}{\sqrt {1 - \beta}} \alpha - \frac {3}{4} (\frac {3 \beta^ {2}}{\sqrt {(1 - \beta) ^ {3}}} + \frac {8 \beta}{\sqrt {(1 - \beta)}}) \alpha^ {2} + o (\alpha^ {2})) \end{array} \right. \tag {5}
$$

The frequency difference of the two resonators is

$$
\Delta f = f _ {e 1} - f _ {e 2} \approx f _ {0} \frac {3 \beta}{\sqrt {1 - \beta}} \alpha \tag {6}
$$

where $f_0$ is the unloaded resonant frequency of the beam, $\beta$ is the stiffness ratio, and their expressions are as follows [27]:

$$
f _ {0} = \frac {1}{2 \pi} \sqrt {\frac {k}{m}} = \frac {1}{2 \pi} \sqrt {\frac {1 6 . 5 3 9 E w ^ {3}}{L ^ {3} \left(0 . 3 9 7 \rho A _ {l} + \rho A _ {f}\right)}}, \beta = \frac {k _ {e}}{k}, \Delta y _ {2} = \frac {m _ {s} \cdot a}{k _ {s} - 2 k _ {e}}, \alpha = \frac {\Delta y _ {2}}{g _ {0}} = \frac {m _ {s} a}{g _ {0} \left(k _ {s} - 2 k _ {e}\right)} \tag {7}
$$

where $E$ is the modulus of elasticity of silicon; $\rho$ is the density of silicon; $L, w,$ and $h$ are the length, width, and thickness of the resonant beam, respectively; $A_{l} = wL$ is the surface area of the beam; $A_{f}$ is the surface area of the additional proof mass; and $m_{s}$ is the mass of the proof mass.

The scale factor $(SF)$ is an important indicator for assessing the performance of an accelerometer, and is expressed as

$$
\begin{array}{l} S F \approx \frac {\delta \Delta f}{\delta \bar {a}} \mathbf {g} _ {n} \approx 3 f _ {0} \frac {\beta}{\sqrt {1 - \beta}} \cdot \frac {m _ {s}}{g _ {0} \left(k _ {s} - 2 k _ {e}\right)} \mathbf {g} _ {n} \quad = \frac {3 k _ {e} f _ {0}}{\sqrt {k \left(k - k _ {e}\right)}} \cdot \frac {m _ {s}}{g _ {0} \left(k _ {s} - 2 k _ {e}\right)} \mathbf {g} _ {n} \tag {8} \\ = \frac {1}{2 \pi} \frac {3 k _ {e}}{\sqrt {m (k - k _ {e})}} \cdot \frac {m _ {s}}{g _ {0} \left(k _ {s} - 2 k _ {e}\right)} g _ {n} \\ \end{array}
$$

where $\mathbf{g}_n$ is the value of gravitational acceleration.

# 3. Structural Optimization Design by the Improved Differential Evolution Algorithm

3.1. Optimization Objectives

The structure size parameter is brought into Equation (8) to obtain

$$
S F = \frac {1}{2 \pi} \frac {3 \varepsilon A V _ {s} ^ {2}}{g _ {0} ^ {3} \sqrt {\left(0 . 3 9 7 \cdot \rho w L h + \rho A _ {f} h\right) \times \left(1 6 . 5 3 9 \cdot \frac {E w ^ {3} h}{L ^ {3}} - \frac {\varepsilon A V _ {s} ^ {2}}{g _ {0} ^ {3}}\right)}} \cdot \frac {\left(\rho w _ {2} L _ {2} h - \rho A _ {t} h + \rho A _ {p} h\right)}{g _ {0} \left(\frac {E w _ {1} ^ {3} h}{2 L _ {1} ^ {3}} - 2 \frac {\varepsilon A V _ {s} ^ {2}}{g _ {0} ^ {3}}\right)} \cdot g _ {n} \tag {9}
$$

where $w_{2}$ and $L_{2}$ are the maximum values in the length and width directions of the proof mass, $A_{t}$ is the area of the hollowed-out part of the proof mass, and $A_{p}$ is the area of the parallel plate structure inside the proof mass, $L_{1}$ is the length of the support beam, and $w_{1}$ is the width of the support beam. There are many parameters that affect the accelerometer scale factor in Equation (9), but the key parameters are DC voltage $V_{S}$ ; resonant beam length $L$ and width $w$ ; support beam length $L_{1}$ and width $w_{1}$ ; and the initial gap between parallel plates $g_{0}$ .

It can be seen from Equation (9) that $V_{s}$ is positively correlated with $SF$ ; however, due to the pull-in effect of the parallel plate capacitor structure in the accelerometer, the

DC voltage $V_{s}$ connected to the proof mass should be less than the pull-in voltage $V_{s}^{\prime}$ . It is also known from the literature [13,17,26,28] that the pull-in voltage $V_{s}^{\prime}$ is related to the size parameter, and that $V_{s}^{\prime}$ is negatively related to the range. Considering the range and structural stability, the pull-in voltage $V_{s}^{\prime}$ is controlled between 20 and 30 V [17].

Therefore, the range of $V_{s}$ is determined as $5 \leq V_{s} \leq 15\mathrm{V}$ ( $V_{s} < 0.8 \cdot V_{s}^{\prime}$ ). Considering the size of the package housing, $w_{2}$ is taken as $2800~\mu \mathrm{m}$ and $L_{2}$ as $3800~\mu \mathrm{m}$ .

Considering the existing manufacturing technology, pull-in voltage, scale factor, nonlinearity, and other factors, the optimization problem is shown in Equation (10):

$$
\min  f (x) = - S F
$$

$$
s. t. 3 <   g _ {0} <   4. 5,
$$

$$
1 1 0 0 <   L <   1 3 0 0, 7. 5 <   w <   1 0,
$$

$$
5 0 0 <   L _ {1} <   6 0 0, 9 <   w _ {1} <   1 2, \tag {10}
$$

$$
2 4, 0 0 0 <   f _ {0} <   3 0, 0 0 0,
$$

$$
2 0 <   k _ {s} <   3 6, 0 <   k _ {e} <   4,
$$

$$
5 \leq V _ {s} \leq 1 5 \text {a n d} V _ {s} <   0. 8 \cdot V _ {s} ^ {\prime}
$$

where the units of $k_{e}$ and $k_{s}$ in the above equation are measured in $\mathrm{N / m}$ , and the other length units are measured in $\mu \mathrm{m}$ . The goal of structural optimization design is to obtain the optimal value of the scale factor under the above constraints. In the actual process of optimizing the accelerometer problem, the parameter dimension is 6 (length and width of the resonant beam; length and width of the support beam; parallel plate capacitor gap; and DC voltage $V_{S}$ (taking into account the pull-in effect)), corresponding to the above-given limitation factors. The other structural parameters of the accelerometer are shown in Table 1.

Table 1. Structural parameters of the accelerometer.   

<table><tr><td>Parameter</td><td>Values</td><td>Units</td></tr><tr><td>Structural layer thickness</td><td>60</td><td>μm</td></tr><tr><td>Driving comb length</td><td>20</td><td>μm</td></tr><tr><td>Driving comb width</td><td>4</td><td>μm</td></tr><tr><td>Detecting comb length</td><td>20</td><td>μm</td></tr><tr><td>Detecting comb width</td><td>4</td><td>μm</td></tr><tr><td>Parallel plate capacitor length</td><td>25</td><td>μm</td></tr><tr><td>Parallel plate capacitor width</td><td>4</td><td>μm</td></tr><tr><td>Comb frame length</td><td>700</td><td>μm</td></tr><tr><td>Comb frame width</td><td>20</td><td>μm</td></tr><tr><td>Distance between two resonant beams</td><td>100</td><td>μm</td></tr></table>

# 3.2.Standard DE

The DE (differential evolution) algorithm [29,30] was originally designed to solve the Chebyshev polynomial. The main idea is to use the differences between individuals in the population to make the next generation of individuals search the solution space to find the optimal solution. The main process includes initial population, mutation operation, crossover operation, and selection operation.

The steps for standard DE are as follows [30].

# 3.2.1. Initialization

After determining the constraints on the number of populations $NP$ , the maximum number of generations $G_{max}$ and the dimensionality of the problem $D$ , the initial generation of individuals (vectors) within the population is initialized:

$$
x ^ {G} = \left(x _ {(1)} ^ {G}, x _ {(2)} ^ {G}, \dots \dots , x _ {(N P)} ^ {G}\right) G = 1, 2, 3, \dots , G _ {\max } \tag {11}
$$

where $x_{(i)}^{G} = \left[x_{(i,1)}^{G},x_{(i,2)}^{G},\dots \dots ,x_{(i,d)}^{G}\right] i = 1,2,\dots ,NP$

The initial vector is randomly selected and can be represented by the following equation:

$$
x _ {(i, j)} ^ {0} = x _ {(i, j \min )} + r a n d (0, 1) \left[ x _ {(i, j \max )} - x _ {(i, j \min )} \right] j = 1, 2, \dots , D \tag {12}
$$

where $x_{(i,jmin)}$ and $x_{(i,jmax)}$ are the limit range of the $j$ -th parameter.

# 3.2.2. Mutation Operation

In this step, the standard DE algorithm is described as the mutation of all target individuals in the population:

$$
\mathrm {D E} / \operatorname {r a n d} / 1: v _ {i} ^ {G} = x _ {r 1} ^ {G} + F \cdot \left(x _ {r 2} ^ {G} - x _ {r 3} ^ {G}\right) \text {w h e r e ,} F \in (0, 1) \tag {13}
$$

The algorithm adopts the DE/rand/1 mutation strategy. In this step, each mutated individual is composed of a parent part and a mutated part. The mutated part is obtained by the difference of two randomly selected individuals from the parent population, except for the aforementioned parent individual. The individual obtained by the mutation operation is the mutation vector [31]. In addition, Price, Storn, and other studies have proposed various strategies, including DE/best/1 and DE/rand-to-best/1 [29,32].

# 3.2.3. Crossover Operation

The mutant individuals generated in the previous generation are cross operated with their parents to generate test vectors. At least one element of the test vector comes from a mutated individual, which provides power for the next generation of population evolution.

$$
u _ {(i, j)} = \left\{ \begin{array}{l l} v _ {(i, j)}, & i f (\operatorname {r a n d} (0, 1) \leq C R) \text {o r} j = j _ {\text {r a n d}} \\ x _ {(i, j)}, & \text {o t h e r w i s e} \end{array} \right. \tag {14}
$$

where $j_{rand} = \text{rand}(0,1)$ , and $CR$ is the crossover rate, which is a key parameter in the differential evolution algorithm that reflects the differences between parent and offspring individuals.

# 3.2.4. Selection Operation

After the crossover operation is completed, the objective function values of the test individuals $u$ and $x$ are used for one-to-one selection. For the minimization problem, the selection operation can be expressed as

$$
x _ {i} ^ {G + 1} = \left\{ \begin{array}{l l} u _ {i} ^ {G + 1}, & f \left(u _ {i} ^ {G + 1}\right) \leq f \left(x _ {i} ^ {G}\right) \\ x _ {i} ^ {G}, & \text {o t h e r w i s e} \end{array} \right. \tag {15}
$$

It is important to select the better vector to survive to the next generation by comparing the parent vector with the test vector. The above steps are then repeated until the number of evolutionary generations reaches $G_{max}$ .

# 3.3. Improved Differential Evolution Algorithm

The DE optimization algorithm has the problems [31] of search stagnation and premature convergence in the application. The main reasons for this are that [33] (1) strict constraints may create an extremely narrow region in which the optimal objective function value exists, and that (2) it is of great significance to have a high searchability to leave out the local optimum when searching for the best results. Therefore, it is a necessary condition to have a strong global search ability to maintain population diversity. The performance of the DE algorithm mainly depends on several control parameters, including scale factor $F$ [34], the crossover rate $CR$ , population size $NP$ [35,36], and the mutation strategy.

Various self-adaptive DE algorithms have been proposed by many researchers. For example, Liu and Lampinen proposed a fuzzy adaptive DE algorithm [37], which uses a fuzzy logic controller to adjust the parameters $F$ and $CR$ . Qin et al. proposed the SaDE

algorithm [38], where $F$ and $CR$ are adaptively adjusted based on a previous high-quality solution experience. Fan and Zhang proposed a differential evolution algorithm, CSA-SADE [39], with crossover strategy adaptation; this method can obtain suitable control parameters, mutation strategies, and crossover strategies at different stages of evolution. By optimizing the mutation strategy, Deng developed a new, improved DE algorithm based on the wavelet basis function [40], which realized the acceleration of convergence and the search for the global optimum.

The idea of RDE [41] is that when the parent is a better individual, a new individual is generated near it, then a mutation vector is generated near the parent vector through a smaller $F$ , and a test vector is generated near the mutation vector through a larger $CR$ . If the parent vector is poor, the mutation vector is generated by a larger $F$ far away from the parent vector, and the smaller $CR$ generates the test vector far away from the mutation vector. This balances the convergence and divergence of the search well, improves the search efficiency of the algorithm, and reduces unnecessary searches and the computational complexity of the algorithm.

Based on RDE and considering the globality and optimality of DE algorithm optimization, an improved algorithm, SAPRDE (self-adaptive population rank-based differential evolution), was developed. SAPRDE sorts the previous generation population during the evolution process, then preserves the good individuals through the final elimination principle. In addition, after population sorting and global parameter sorting, it maps the most suitable parameters, mutation rate $F$ and crossover rate $CR$ to each surviving individual, which stimulates the ability of offspring individuals to find the global optimum. The above is SAPRDE's core idea. In this way, global optimality is maintained while algorithm complexity is reduced. Moreover, the parameters are optimally configured, and the optimization of the accelerometer scale factor is achieved.

The initial population size $(NP_{max})$ of the SAPRDE algorithm is $15D - 20D$ , and the termination size $(NP_{min})$ is $2D$ . For the DE algorithm, different mutation strategies will have different effects on the performance of the algorithm. The SAPRDE algorithm adopts the DE/best/1 strategy. At the beginning of evolution, the rich population makes the algorithm's global search ability strong. On this basis, the adaptively adjusted mutation and crossover rates make the optimal evolution direction unrestricted.

If the mutated vector exceeds the specified range in the optimization process, it will be initialized again. Then, the program will continue to run. The main steps of SAPRDE are as follows. Record the information provided by the ranking in each round. One is to provide the basis for the parameter allocation for the population; the other is to provide information on the linear decrease in the population number $NP$ . Then, the parameters are taken linearly in the interval and wait for allocation according to Equations (16) and (17).

$$
F _ {j} = F _ {\min } + \left(F _ {\max } - F _ {\min }\right) \frac {S _ {j}}{N P - 1} \tag {16}
$$

$$
C R _ {j} = C R _ {\max } - \left(C R _ {\max } - C R _ {\min }\right) \frac {S _ {j}}{N P - 1} \tag {17}
$$

$$
N P _ {i} = N P _ {\max } - \text {r o u n d} \left[ \frac {2 i}{G _ {\max }} \left(N P _ {\max } - N P _ {\min }\right) \right], \text {w h e n} i \leq \frac {G _ {\max }}{2} \tag {18}
$$

In Equations (16)-(18), $i$ is the current evolutionary generation, $S_{j}$ is the ranking of the fitness of each individual in the population in each round, and $F_{j}$ and $CR_{j}$ are the parameters that are linearly allocated to the population during the execution process. Taking the interval of $CR$ and $F$ suggested in the article of Storn and Price as the standard, $F_{\min}, F_{\max}, CR_{\min},$ and $CR_{\max}$ are taken as the two ends of the interval (0.5,1), (0.8,1); the specific values optimize changes with the actual accelerometer parameters. On this basis, the algorithm uses the parameters to be assigned as calculated in Equations (16) and (17) to linearly assign the population. Figure 2 is the flow chart of the algorithm program. After the judgment operation between $sf\left(u_i^{G+1}\right)$ and $sf\left(x_i^G\right)$ , the algorithm sorts the

fitness of all surviving individuals in all populations at the time described above. After sorting, the ranking information is recorded. Obviously, the ranking information is used for the corresponding selection of the next round of parameter allocation. The algorithm eliminates bad individuals every few rounds, leaving the top-ranked individuals, so the ranking information also eliminates poor individuals. This is a method of RDE assignment. The number of populations in each round is shown in Equation (18). Then, the next round begins, and so on, until the termination conditions are met. It should be noted that the eliminated vector needs to be approximated before the elimination process is performed. All the improvement steps are marked in red in Figure 2. After the above steps, every control parameter in each round is assigned to the most suitable surviving individuals. This algorithm thusly realizes self-adaptive parameter assignment, eliminates bad individuals, and reduces unnecessary calculations.

![](images/f74c9c795701ee6b4cbe16ea9985f332e2758bf8f9f1f4d4cb01eecedb916ad0.jpg)  
Figure 2. SAPRDE flow chart.

# 3.4. Optimization Results

The optimization algorithm program was run in the software Matlab2020b. To reflect the effect of SAPRDE, we used the ordinary DE algorithm with the same strategy as SAPEDE for comparison. The algorithm parameters and condition settings of both were the same, except for the improved content proposed in this article, in the sense that both used the parameter interval suggested in Storn and Price [30]. Four results of the two algorithms

can be randomly taken for comparison. In Figure 3, the general DE algorithm eventually reaches a stable state after 200-500 generations (generally 300 generations) of evolution. In the process of evolution, the algorithm reaches stability with too many evolutionary generations due to its slow speed of searching for good individuals. The value of the stable state did not ultimately converge to a fixed value: it converged to the local optimum and lacked the motivation to jump out of the local area. In contrast, the four runs in Figure 3b demonstrate the good repeatability of the SAPRDE algorithm, as the results of several runs were relatively consistent. The algorithm basically reached a stable state near the 100th generation and evolved to stabilize at 200-300 generations. After improvement, the number of iterations to find the optimal parameters was greatly reduced, and the success rate of finding the optimal solution was also higher. The results prove that the above-mentioned self-adaptive strategy increases the diversity of the population. Figure 4 shows the change curve of each specific parameter in the study of the evolution process.

![](images/87ab12fde207cf09ab6356a3603a7edc1b577b53465d0a3a4168890cfa9c262b.jpg)  
(a)

![](images/b303c0e7585dc71ec9c4e7cbbb69f28cd08e6a131dd5e8ef6ba1d4855e64f087.jpg)  
(b)   
Figure 3. Comparison of optimization of two algorithms. (a) ordinary DE algorithm. (b) SAPRDE algorithm.

As shown in Figure 4, it is obvious that the performance of SAPRDE is better than that of the ordinary DE algorithm in the optimization of the accelerometer parameters. The ordinary DE algorithm undergoes a long evolutionary process in parameter optimization. For example, the support beam length $L_{1}$ and width $w_{1}$ were still unstable at nearly 800 generations. On the contrary, the SAPRDE algorithm quickly searches for the optimal values of each parameter and quickly enters a stable state. The convergence values of $L$ , $w$ , $L_{1}$ , $w_{1}$ , $g_{0}$ , and $V_{S}$ were $1100\mu \mathrm{m}$ , $8.64\mu \mathrm{m}$ , $502.26\mu \mathrm{m}$ , $9.61\mu \mathrm{m}$ , $3.15\mu \mathrm{m}$ , and $15\mathrm{V}$ , respectively.

Figure 5 shows the evolution value of four hundred generations in six random runs. Unlike the ordinary DE algorithm, the result of SAPRDE was almost identical, which shows the good repeatability of the improved algorithm. In addition, we can see that the final value of the ordinary DE algorithm did not achieve the optimal effect every time. This is because the algorithm cannot be adjusted in time when it falls into local optimization, resulting in the evolution result not reaching the ideal optimization. In terms of time complexity, SAPRDE also had a running time reduction of $25\%$ compared to the ordinary DE algorithm, which also verifies that the method of selecting excellent individual survival of the fittest reduces the overall computational complexity of the algorithm. The optimized result of the scale factor was $60.27\mathrm{Hz / g}$ ; the unloaded resonant frequency of the resonator beam was $24.148\mathrm{kHz}$ .

![](images/08ccd4670f81109306bef35e96d4d7bfcca9eeccdd38aa5161c301c4eb067c34.jpg)  
(a)

![](images/edfd58d6e0ea8752caad74bdcb668b43e406e01bf78958eccdce00018f036c45.jpg)  
(b)

![](images/e19c357bd4787b7d542c67cd2aef3e743de0fcd5e5544ded04077e8435826b5e.jpg)  
(c)

![](images/dd4f3c575e9954f7536320b9627b78937ce6ca013bf0090454856aa04da6ae54.jpg)  
(d)

![](images/2ad1067faa7b8763d960665b073499fcb7315eb0787013a49d22606d6e9d0143.jpg)  
(e)

![](images/0927d1605fb02f934d6f63e3a3bc646a9ba28ac3dc1219dc8da36668f5ea0e47.jpg)  
(f)

![](images/d63c609d7af1169943189f2bd56bbfa088e0c96b3db16f763550910230cfe7f3.jpg)  
Figure 4. The optimization process of each parameter before and after algorithm improvement. (a) Length of the resonant beam $L$ ; (b) width of the resonant beam $w$ ; (c) length of support beam $L_1$ ; (d) width of support beam $w_1$ ; (e) gap of parallel plate capacitor $g_0$ ; (f) DC voltage $V_s$ .   
Figure 5. Convergence value at 400 generations of 6 random evolutions.

# 4. Experiment

The resonant micro-accelerometer based on electrostatic stiffness was fabricated by the deep dry silicon-on-glass (DDSOG) process. Photographs of the fabricated resonant accelerometer taken under the microscope are shown in Figure 6.

![](images/f6206c5781ae6c87ba125e3f1e92658139dd19e3fdea07286b2ee87364dd5422.jpg)  
Figure 6. Photographs of the fabricated accelerometer.

With the help of the probe station (Figure 7a), an open-loop test of the accelerometer was conducted. The outer fixed combs of the upper resonant beam and the inner fixed combs of the lower resonant beam are the driving end, and the opposite is the detection end. The two sides of the resonator are connected with a DC biased AC driving voltage to drive the resonator to the reverse working mode. The common terminal current is drawn at the anchor. The test leads are shown in Figure 7b.

![](images/b57385f14b36f4a559cdf5edd6f89b0aca3ef519cba2d9ac17176c18970ee18d.jpg)  
(a)

![](images/2d9f184d897216b5429554567858323ea14f010b61be58bb6b4ae9704a7c19ea.jpg)  
(b)   
Figure 7. Open-loop test. (a) Probe station. (b) Accelerometer open-loop test pinout.

All the accelerometers on the wafer were tested in the open-loop mode. The unloaded resonant frequencies of all the accelerometers were between 24 and $26\mathrm{kHz}$ . The test data of 10 accelerometers are shown in Table 2. Due to manufacturing errors, the resonant frequency of the resonator fluctuates, and there is a difference between the resonant frequencies of the two resonators of the same accelerometer. In general, the measured resonant frequencies of the fabricated accelerometer were basically consistent with the theoretical values.

Table 2. Unloaded resonant frequency of accelerometer resonator (kHz).   

<table><tr><td>Accelerometer Number</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Upper resonator</td><td>24.64</td><td>25.67</td><td>24.77</td><td>25.93</td><td>25.57</td><td>25.63</td><td>25.89</td><td>25.36</td><td>25.41</td><td>25.23</td></tr><tr><td>Lower resonator</td><td>24.69</td><td>25.78</td><td>24.86</td><td>25.98</td><td>25.53</td><td>25.64</td><td>25.87</td><td>25.43</td><td>25.48</td><td>25.29</td></tr></table>

The scale factor test of five packaged accelerometers was performed through closed-loop circuits (Figure 8). With the $15\mathrm{V}$ detection voltage provided, the scale factor of accelerometers is shown in Table 3. It can be seen from the test data that the average error between actual scale factor and the result of the optimized design of five packaged accelerometers was $7.03\%$ . The actual scale factor of the packaged accelerometers was basically consistent with the result of the optimized design, taking into account factors such as manufacturing and packaging errors.

![](images/1e594c577cce53705054ba2493c5025192a481ccc2000ad5f1e4b890b442e15a.jpg)  
Figure 8. Packaged accelerometer and closed-loop circuits.

Table 3. Scale factor and error of packaged accelerometers.   

<table><tr><td>Accelerometer Number</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Scale factor (Hz/g)</td><td>54.23</td><td>55.46</td><td>55.94</td><td>56.36</td><td>58.17</td></tr><tr><td>Error (%)</td><td>10.02</td><td>7.98</td><td>7.18</td><td>6.49</td><td>3.48</td></tr></table>

# 5. Conclusions

This paper designed a resonant micro-accelerometer based on electrostatic stiffness. The working principle of the accelerometer was analyzed, and the expression of the scale factor was deduced. The mathematical model for the optimal design of a specific accelerometer structure was determined. An improved differential evolution algorithm, SAPRDE, was developed to optimize the accelerometer scale factor. The improved algorithm not only maintained the global optimality of the scale factor, but also reduced the complexity of the algorithm. The optimization results show that the SAPRDE algorithm has obvious advantages over the ordinary DE algorithm in terms of global search and computing time. The optimized accelerometer was fabricated by the DDSOG process. The unloaded resonant frequency of the fabricated accelerometer resonant beam was between 24 and $26\mathrm{kHz}$ , and the scale factor of the packaged accelerometers was between 54 and $59\mathrm{Hz / g}$ , which met the design and optimization expectations. The results showed that the SAPRDE algorithm optimization was in accordance with the structural characteristics of the resonant micro-accelerometer based on electrostatic stiffness.

Author Contributions: Conceptualization, L.H. and X.D.; methodology, L.H.; formal analysis, Y.Q.; investigation, M.Z.; data curation, Q.L.; writing—original draft preparation, Q.L.; supervision, L.Z. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Conflicts of Interest: The authors declare no conflict of interest.

# References

1. Furubayashi, Y.; Oshima, T.; Yamawaki, T.; Watanabe, K.; Mori, K.; Mori, N.; Matsumoto, A.; Kamada, Y.; Isobe, A.; Sekiguchi, T. A 22-ng/√Hz 17-mW Capacitive MEMS Accelerometer with Electrically Separated Mass Structure and Digital Noise-Reduction Techniques. IEEE J. Solid-State Circuits 2020, 55, 2539–2552. [CrossRef]   
2. Zhang, H.; Zhang, Y.; Zhang, W. Design and Analysis of MEMS Biaxial Coupled Resonance Accelerometer. In Proceedings of the 2021 IEEE 16th International Conference on Nano/Micro Engineered and Molecular Systems (NEMS), Xiamen, China, 25-29 April 2021; pp. 1867-1870.   
3. Edalatfar, F.; Hajhashemi, S.; Yaghootkar, B.; Bahreyni, B. Dual mode resonant capacitive MEMS accelerometer. In Proceedings of the 2016 IEEE International Symposium on Inertial Sensors and Systems, Laguna Beach, CA, USA, 22-25 February 2016; pp. 97-100.   
4. Todi, A.; Mansoorzare, H.; Moradian, S.; Abdelvand, R. High Frequency Thin-Film Piezoelectric Resonant Micro-Accelerometers with A Capacitive Mass-Spring Transducer. In Proceedings of the 2020 IEEE Sensors, Rotterdam, The Netherlands, 25-28 October 2020; pp. 1-4.   
5. Park, B.; Lee, S.; Han, K.; Yu, M.-J.; Chang, B. Response characteristics of a MEMS resonant accelerometer to external acoustic excitation. In Proceedings of the 2016 IEEE Sensors, Orlando, FL, USA, 30 October-3 November 2016; pp. 1-3.   
6. Seok, S.; Chun, K. Inertial-grade in-plane resonant silicon accelerometer. *Electron. Lett.* **2006**, 42, 1092–1093. [CrossRef]   
7. Lee, B.-L.; Oh, C.-h.; Lee, S.; Oh, Y.-S.; Chun, K.-J. A vacuum packaged differential resonant accelerometer using gap sensitive electrostatic stiffness changing effect. In Proceedings of the IEEE Thirteenth Annual International Conference on Micro Electro Mechanical Systems (Cat. No. 00CH36308), Miyazaki, Japan, 23-27 January 2000; pp. 352-357.   
8. Kim, H.C.; Seok, S.; Kim, I.; Choi, S.-D.; Chun, K. Inertial-grade out-of-plane and in-plane differential resonant silicon accelerometers (DRXLs). In Proceedings of the 13th International Conference on Solid-State Sensors, Actuators and Microsystems, 2005, Digest of Technical Papers, TRANSDUCERS'05, Seoul, Korea, 5-9 June 2005; pp. 172-175.   
9. Comi, C.; Corigliano, A.; Langfelder, G.; Zega, V.; Zerbini, S. Sensitivity and temperature behavior of a novel z-axis differential resonant micro accelerometer. J. Micromech. Microeng. 2016, 26, 035006. [CrossRef]   
10. Yang, B.; Dai, B.; Zhao, H. The Design and Simulation of a New Z-Axis Resonant Micro-Accelerometer Based on Electrostatic Stiffness. In Advanced Materials Research; Trans Tech Publications: Freienbach, Switzerland, 2013; pp. 478-483.   
11. Seok, S.; Kim, H.; Chun, K. An inertial-grade laterally-driven MEMS differential resonant accelerometer. In Proceedings of the SENSORS, 2004 IEEE, Vienna, Austria, 24-27 October 2004; pp. 654-657.   
12. Liu, H.; Zhang, F.T.; He, X.; Su, W.; Zhang, F. Structure design and fabrication for resonant accelerometer based on electrostatic stiffness. J. Chongqing Univ. 2011, 34, 36-42.   
13. Liu, H. Research on Micro Resonant Accelerometers Based on Electrostatic Stiffness; Chongqing University: Chongqing, China, 2011.   
14. Zhang, F.; He, X.; Shi, Z.; Zhou, W. Structure design and fabrication of silicon resonant micro-accelerometer based on electrostatic rigidity. In Proceedings of the World Congress on Engineering, London, UK, 1-3 July 2009.   
15. Zhang, F.; Shi, Z.; He, X.; Liu, H. Structure Stability of Micro Silicon Resonant Acceleration Sensors Based on Electrostatic Rigidity. MEMS Device Technol. 2010, 47, 770-775.   
16. Zhou, W.; He, X.; Su, W.; Li, B.; Chen, L. Design of resonant micro accelerometer based on electrostatic stiffness. Transducer Microsyst. Technol. 2009, 97, 92-94.   
17. Zhou, W. Research of Electromechanical Coupling Characteristics and Key Technologies in Microaccelerometer; Southeast Jiaotong University: Chengdu, China, 2010.   
18. Wang, Y.; Zhang, J.; Yao, Z.; Lin, C.; Zhou, T.; Su, Y.; Zhao, J. A MEMS resonant accelerometer with high performance of temperature based on electrostatic spring softening and continuous ring-down technique. IEEE Sens. J. 2018, 18, 7023-7031. [CrossRef]   
19. Zhai, D.; Liu, D.; He, C.; Guan, R.; Lin, L.; Dong, L.; Zhao, Q.; Yang, Z.; Yan, G. A resonat accelerometer based on ring-down measurement. In Proceedings of the 2015 Transducers-2015 18th International Conference on Solid-State Sensors, Actuators and Microsystems (TRANSDUCERS), Anchorage, AK, USA, 21–25 June 2015; pp. 1125–1128.   
20. Trusov, A.A.; Zotov, S.A.; Simon, B.R.; Shkel, A.M. Silicon accelerometer with differential frequency modulation and continuous self-calibration. In Proceedings of the 2013 IEEE 26th International Conference on Micro Electro Mechanical Systems (MEMS), Taipei, Taiwan, 20-24 January 2013; pp. 29-32.   
21. Pei, R.; Wang, X.; Gao, X.; Yu, J. Optimization design technique for key structure of quartz vibrating-beam accelerometer. J. Harbin Inst. Technol. 2012, 44, 129-132.   
22. Wang, Y.; Zhang, J.; Xia, Y.; Li, P. Optimization of supporting beams of piezoelectric omnidirectional accelerometer under stress constraint. Opt. Precis. Eng. 2020, 28, 1751-1760.   
23. Wang, C. Design and Optimization of the Subwavelength Gratings and Compliant Beams for Hign Precision MEMS Accelerometers; Zhejiang University: Hangzhou, China, 2018.   
24. Pak, M.; Fernandez, F.V.; Dundar, G. Optimization of a MEMS accelerometer using a multiobjective evolutionary algorithm. In Proceedings of the 2017 14th International Conference on Synthesis, Modeling, Analysis and Simulation Methods and Applications to Circuit Design (SMACD), Giardini Naxos, Italy, 12-15 June 2017; pp. 1-4.   
25. Zhang, J.; Shi, Y.; Zhao, R.; Wang, Y.; Guo, C.; Zhang, T. Miniaturization Design of High-Range Accelerometer Based on Multi-Objective Optimization. Chin. J. Sens. Actuators 2021, 34, 1152-1157.

26. Qin, Y. Structural Design and Analysis of Electrostatic Stiffness Resonant Micro-Accelerometer; Southeast University: Nanjing, China, 2021.   
27. Chen, W. Structure Design and Analysis of Micromechanical Silicon Resonant Accelerometer; Southeast University: Nanjing, China, 2012.   
28. Nielson, G.N.; Barbastathis, G. Dynamic pull-in of parallel-plate and torsional electrostatic MEMS actuators. J. Microelectromech. Syst. 2006, 15, 811-821. [CrossRef]   
29. Storn, R.; Price, K. Differential evolution—A simple and efficient heuristic for global optimization over continuous spaces. J. Glob. Optim. 1997, 11, 341-359. [CrossRef]   
30. Price, K.V. Differential evolution vs. the functions of the 2/sup nd/ICEO. In Proceedings of the 1997 IEEE International Conference on Evolutionary Computation (ICEC'97), Indianapolis, IN, USA, 13-16 April 1997; pp. 153-157.   
31. Akinsolu, M.O.; Liu, B.; Lazaridis, P.I.; Mistry, K.K.; Mognaschi, M.E.; Di Barba, P.; Zaharis, Z.D. Efficient design optimization of high-performance mems based on a surrogate-assisted self-adaptive differential evolution. IEEE Access 2020, 8, 80256-80268. [CrossRef]   
32. Das, S.; Konar, A.; Chakraborty, U.K. Two improved differential evolution schemes for faster global search. In Proceedings of the 7th Annual Conference on Genetic and Evolutionary Computation, Washington, DC, USA, 25-29 June 2005; pp. 991-998.   
33. Mousavirad, S.J.; Rahnamayan, S. Enhancing SHADE and L-SHADE Algorithms Using Ordered Mutation. In Proceedings of the 2020 IEEE Symposium Series on Computational Intelligence (SSCI), Canberra, ACT, Australia, 1-4 December 2020; pp. 337-344.   
34. Guo, S.-M.; Yang, C.-C.; Hsu, P.-H.; Tsai, J.S.-H. Improving differential evolution with a successful-parent-selecting framework. IEEE Trans. Evol. Comput. 2014, 19, 717-730. [CrossRef]   
35. Awad, N.H.; Ali, M.Z.; Suganthan, P.N.; Reynolds, R.G. An ensemble sinusoidal parameter adaptation incorporated with L-SHADE for solving CEC2014 benchmark problems. In Proceedings of the 2016 IEEE Congress on Evolutionary Computation (CEC), Vancouver, BC, Canada, 24-29 July 2016; pp. 2958-2965.   
36. Tanabe, R.; Fukunaga, A.S. Improving the search performance of SHADE using linear population size reduction. In Proceedings of the 2014 IEEE Congress on Evolutionary Computation (CEC), Beijing, China, 6-11 July 2014; pp. 1658-1665.   
37. Liu, J.; Lampinen, J. A fuzzy adaptive differential evolution algorithm. Soft Comput. 2005, 9, 448-462. [CrossRef]   
38. Qin, A.K.; Huang, V.L.; Suganthan, P.N. Differential evolution algorithm with strategy adaptation for global numerical optimization. IEEE Trans. Evol. Comput. 2008, 13, 398-417. [CrossRef]   
39. Fan, Q.; Zhang, Y. Self-adaptive differential evolution algorithm with crossover strategies adaptation and its application in parameter estimation. Chemom. Intell. Lab. Syst. 2016, 151, 164-171. [CrossRef]   
40. Deng, W.; Xu, J.; Song, Y.; Zhao, H. Differential evolution algorithm with wavelet basis function and optimal mutation strategy for complex optimization problem. Appl. Soft Comput. 2021, 100, 106724. [CrossRef]   
41. Takahama, T.; Sakai, S. Efficient constrained optimization by the ε constrained adaptive differential evolution. In Proceedings of the 2012 IEEE Congress on Evolutionary Computation (CEC), Brisbane, Australia, 10-15 June 2012; pp. 1-8.