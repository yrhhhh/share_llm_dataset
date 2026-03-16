Article

# Closed-Loop Control and Output Stability Analysis of a Micromechanical Resonant Accelerometer

Heng Liu *, Yu Zhang and Jiale Wu

School of Electronic & Information Engineering, Nanjing University of Information Science & Technology, Nanjing 210044, China

* Correspondence: 002357@nuist.edu.cn

Abstract: In this study, a dynamic equation for a micromechanical resonant accelerometer based on electrostatic stiffness is analyzed, and the parameters influencing sensitivity are obtained. The sensitivity can be increased by increasing the detection proof mass and the area facing the detection capacitor plate and by decreasing the stiffness of the fold beams and the initial distance between the plate capacitors. Sensitivity is also related to the detection voltage: the larger the detection voltage, the greater the sensitivity. The dynamic equation of the closed-loop self-excited drive of the accelerometer is established, and the steady-state equilibrium point of the vibration amplitude and the stability condition are obtained using the average period method. Under the constraint conditions of the PI controller, when the loading acceleration changes, the vibration amplitude is related to the reference voltage and the pre-conversion coefficient of the interface circuit and has nothing to do with the quality factor. When the loading voltage is $2\mathrm{V}$ , the sensitivity is $321\mathrm{Hz / g}$ . Three Allan variance analysis methods are used to obtain the frequency deviation of $0.04\mathrm{Hz}$ and the amplitude deviation of $0.06\mathrm{mV}$ within $30\mathrm{min}$ at room temperature. When the temperature error in the incubator is $\pm 0.01^{\circ}\mathrm{C}$ , the frequency deviation decreases to $0.02\mathrm{Hz}$ , and the resolution is $56\mathrm{ug}$ . The fully overlapping Allan variance analysis method (FOAV) requires a large amount of data and takes a long time to implement but has the most accurate stability of the three methods.

Keywords: resonant accelerometer; sensitivity; self-excited oscillation; frequency stability; Allan variance

![](images/eb0b8ff23e776dd0dacba694f0608df8e133442315b0879f68b0cd77e7a407da.jpg)

Citation: Liu, H.; Zhang, Y.; Wu, J.

Closed-Loop Control and Output

Stability Analysis of a

Micromechanical Resonant

Accelerometer. Micromachines 2022,

13, 1281. https://doi.org/

10.3390/mi13081281

Academic Editor: Ha Duong Ngo

Received: 28 June 2022

Accepted: 5 August 2022

Published: 8 August 2022

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/6371a5203106b36adcf57b89d197d15daad0f63c792902347e46fe60b1f689dc.jpg)

Copyright: © 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

# 1. Introduction

The advantages of micromechanical resonant accelerometers are their small size, low power consumption, mass production, and their use of strong anti-interference output as a frequency signal. They are widely used to measure acceleration, displacement, force, etc. The working principle of this technology is to change the stiffness of the resonant beam through acceleration to change the resonant frequency [1]. There are two main types of stiffness changes: inherent stiffness change types and external electrostatic negative stiffness types. With the intrinsic stiffness change type, acceleration acts on the movable mass to generate an inertial force; the inertial force directly loads onto the axial end of the vibrating beam through a lever [2,3]. In order to improve the sensitivity and common mode rejection ratio (CMRR) of axial force-sensitive resonant accelerometers, two identical micromechanical levers are generally used. However, manufacturing process errors will lead to different force coefficients and nonlinearity of sensitivity. When the micromechanical lever amplifies the axial force, it also increases the coupling sensitivity of the cross axis [4,5]. At the same time, the levers need long-term repetitive work, and there is a risk of fatigue fracture. Once the resonant frequency is determined, there is deviation between the resonant frequency and the expected design value due to manufacturing errors. As such, subsequent adjustments to the sensitivity and other parameters for inherent stiffness change-type resonant accelerometers cannot be realized [6].

When a voltage is loaded to the movable capacitor plate, the movable plate produces an equivalent electrostatic negativitystiffness, and its magnitude is related to the loading

voltage, the area facing the plates, the distance between the plates, and the dielectric constant of the medium between the plates. The equivalent stiffness of the movable plate decreases due to electrostatic negative stiffness, so the resonance frequency of the movable plate also decreases [7-9]. Micromechanical resonant accelerometers that are based on external electrostatic negative stiffness are able to tune the sensitivity according to the loading voltage, and the sensitivity has little dependence on manufacturing errors [6]. There are two typical forms of electrostatic stiffness resonant accelerometers: in the first type, the plate distance changes through acceleration [10-14], and for the other, the area facing the plate is changed through acceleration [15-17]. The former is in-plane vibration, and the latter is out-of-plane vibration. The two-mode shapes are different, and the last is much more nonlinear.

Both axial forces sensitive and electrostatic stiffness types have two movable parts, one is the resonant beam, which is responsible for the output frequency to characterize the acceleration, and the other is the sensitive mass block subsystem, which converts the acceleration into the force loaded on the axial direction of the resonant beam. The motion directions of the two movable parts are orthogonal, and the motion of the sensitive mass subsystem does not affect the motion displacement of the resonant beam so that the sensitivity can be easily calculated by the resonant beam [2,3]. However, for the electrostatic stiffness accelerometer, the two moving parts are coupled in the same direction. Especially for the in-plane moving electrostatic stiffness resonant accelerometer, the displacement of the resonant beam is affected by the displacement of the mass subsystem, so it is difficult to give the sensitivity relationship directly [10-14]. The sensitivity is obtained through experimental tests, and it is difficult to guide optimal microstructure design. The sensitivity analysis of the electrostatic stiffness resonant accelerometer with in-plane vibration has not been investigated. The analytical expression of sensitivity is helpful for better design and optimization of the layout of microstructure, so this part of the work has a clear significance.

When micromechanical resonant accelerometers are in the resonance state, the amplitude of the detection signal and the signal-to-noise ratio at the detection end corresponding to the same amplitude of the driving force are the largest. At the same time, to reduce cross-coupling between the vibration amplitude and the resonant frequency, it is necessary to maintain the constant amplitude vibration of the vibrating beam [18]. Automatic gain control is widely used in continuous amplitude control; phase-locked loops and self-excited oscillation are often used to achieve frequency tracking control [19-21]. The authors of reference [20] analyzed the closed-loop control theory under automatic gain and used a phase-locked loop using the average period method; however, they did not investigate or experimentally verify frequency stability and amplitude stability using the control method, affecting how the resolution was tested and analyzed. Allan variance is often used to analyze the phase noise of resonant sensors. During analysis, the sampling sequence is first grouped using the cluster analysis method, and the mean value of each group is used as the subsequent analysis target [22]. According to different grouping methods, Allan variance is divided into fully overlapping Allan variance (FOAV), incomplete overlapping Allan variance (NFOAV), and non-overlapping Allan variance (NAV) [23]. Different variance analysis methods have different application scenarios for different sample sizes, analysis times, and precision requirements.

This study focuses on three issues: the first issue aims to solve the relationship between the sensitivity of the electrostatic stiffness of the resonant micro accelerometer and the structural parameters as well as the loading voltage to guide the layout optimization design of the accelerometer; the second is to determine whether the steady-state behavior of the closed-loop self-excited system meets the amplitude and frequency requirements based on the dynamic behavior analysis; and the third is to analyze the stability of the resonance frequency and vibration amplitude under closed-loop self-excitation to determine the resolution and stability of the accelerometer.

# 2. Working Principles of Micromechanical Resonant Accelerometer

The structural layer of the resonant micro-accelerometer includes a sensitive proof mass with some damping holes, the folded beams supporting the suspended proof mass, the detection plate capacitor pair attached to the proof mass, the fixed driving comb capacitor pair, a double-ended tuning fork (DETF) resonant beam, and fixed anchors, as shown in Figure 1. The Y-axis is the drive and detection direction. By adopting single-side drive and single-end detection, the structure of the accelerometer can be divided into two identical single-beam resonant accelerometers at the middle symmetry point. The folded beam and the proof mass structure are connected to the detection voltage $V_{s}$ , the movable tuning fork beam is connected to the high-frequency square wave $V_{a}$ , and the fixed comb is connected to the AC voltage $V_{ac} \sin \omega t$ and the DC bias voltage $V_{d}$ . The resonant beam structure is equivalent to a second-order system, and the input-output relationship is analogous as a band-pass filter. For the low-amplitude high-frequency square wave voltage $V_{a}$ , the frequency is far from the resonant frequency and is equivalent to grounding. When the DC amplitude of the driving voltage $V_{d}$ is much larger than the AC amplitude $V_{ac}$ , and acceleration $a$ is applied, and the output frequency of the single resonant beam $f_{e}$ can be expressed as

$$
f _ {e} = \frac {1}{2 \pi} \sqrt {\frac {k _ {m} - k _ {e} (a)}{m}} \tag {1}
$$

![](images/d8f9de79c8f4d1f476053ef70d9d616dc1076d8d4f4606f0e844f9bec7f39e4c.jpg)  
Figure 1. Resonant micro-accelerometer.

In Formula (1), $k_{m}$ is the stiffness of the tuning fork beam, $m$ is the mass of the tuning fork beam and its attached microstructure, and $k_{e}(a)$ is the electrostatic stiffness when there is acceleration, which is related to $a$ . The proof mass and the plate at the detection end will be displaced by $\Delta d$ :

$$
\Delta d = \frac {m _ {s} \cdot a}{k _ {s}} \tag {2}
$$

In Formula (2), $m_{s}$ represents the mass of the proof mass with damping holes and its attached microstructure, $k_{s}$ is the equivalent stiffness of the four folded beams, and the corresponding electrostatic stiffness $k_{e}(a)$ is

$$
k _ {e} (a) = \frac {\varepsilon \cdot S \cdot V _ {s} ^ {2}}{\left(d _ {0} - \Delta d\right) ^ {3}} = \frac {\varepsilon \cdot S \cdot V _ {s} ^ {2} \cdot k _ {s} ^ {3}}{\left(d _ {0} \cdot k _ {s} - m _ {s} \cdot a\right) ^ {3}} \tag {3}
$$

where $\varepsilon$ is the dielectric constant of air and $S$ is the area facing the detection capacitor plate. The structural design requirements are $k_{s} \ll k_{m}$ and $\Delta d \ll d_{0}$ , resulting in

$$
f _ {e} \approx f _ {0} \left(1 - \frac {3 \beta}{2} \frac {\Delta d}{d _ {0}} - (3 \alpha + \frac {9}{8} \alpha^ {2}) \left(\frac {\Delta d}{d _ {0}}\right) ^ {2} + o \left(\left(\frac {\Delta d}{d _ {0}}\right)\right) ^ {2} \dots\right) \tag {4}
$$

where

$$
\beta = \frac {\varepsilon \cdot S \cdot V _ {s} ^ {2}}{d _ {0} ^ {3} \cdot k _ {m}}, \alpha = \frac {\varepsilon \cdot S \cdot V _ {s} ^ {2}}{d _ {0} ^ {3} \cdot k _ {m}} \cdot (1 - \frac {\varepsilon \cdot S \cdot V _ {s} ^ {2}}{d _ {0} ^ {3} \cdot k _ {m}}), f _ {0} = \frac {1}{2 \pi} \sqrt {k _ {m} / m}
$$

Ignoring higher-order terms, $f_{e}$ can be expressed as

$$
f _ {e} \approx \frac {1}{2 \pi} \sqrt {k _ {m} / m} \cdot (1 - \frac {3 \varepsilon \cdot S \cdot V _ {s} ^ {2}}{2 d _ {0} ^ {3} \cdot k _ {m}} \frac {m _ {s} \cdot a}{d _ {0} \cdot k _ {s}}) \tag {5}
$$

According to Formula (5), the resonant frequency $f_{e}$ has an approximately linear relationship with the acceleration $a$ . The sensitivity can be increased by increasing the proof mass $m_{s}$ and the area facing the detection capacitor plate $S$ and by decreasing the equivalent stiffness $k_{s}$ and the initial distance between the plate capacitors $d_{o}$ . The sensitivity is also related to the square of the detection voltage $V_{s}$ ; the larger $V_{s}$ is, the greater the sensitivity will be.

The structural layer of the accelerometer was made of a monocrystalline silicon material doped with concentrated boron to improve the conductivity of the microstructure. Pyrex 7740 glass was used as the substrate material, and this material anode bonded the microstructure and the substrate. Inductively coupled plasma (ICP) etching technology was used to obtain larger depth and width ratios. In step 1, the monocrystalline silicon wafer was cleaned, and the bonding platform was etched; in step 2, the monocrystalline silicon was doped with concentrated boron via a diffusion process to increase the conductivity of the structure; in step 3, Au was sputtered on the borosilicate glass, followed by the photolithography electrode and lead; in step 4, the glass and silicon were bonded through the anode; in step 5, the back of the bonded silicon wafer was dry-etched with excess silicon, and the structural layer was thinned; in step 6, the back of the silicon wafer was etched with the deep silicon etching process. The process flow is relatively simple and has high yield; the gap between the structure and the substrate is easy to control; there are fewer pollution impurities, only three masks, and three photolithography periods; and the process is inexpensive. The process flow is shown in Figure 2. The fabricated accelerometer is shown in Figure 3, and a computer vision method was used to directly mark the length and width dimensions. Table 1 shows the structural parameters that were designed and measured.

![](images/058fa8d2f5833e918649b946930bdff4396342b94ed29e0c1083e1ea836f0605.jpg)  
(1)

![](images/b5d99a7388c7752ccd0b38507f021bd28870b84f1fcdce81779d4c96f22f2af2.jpg)  
(2)

![](images/66729f37f3335339687ed85744dee058493f93bc8ad4db453f6cf0d89b588aae.jpg)

![](images/caf5bb9196020a7be46da81636a744c81037aa3a57fc83e309b07f38e5fc39df.jpg)  
(3）

![](images/e42cd016fe58b722a1cd0d3385776114611cfdd8c9b1218103bdde7a3f18b97f.jpg)  
(4)

![](images/b55da50d2568120aff6c60d7b70834d6d85b51d19dd77692e396b962eeb18b7a.jpg)

![](images/0a03ccc70ea16f12ebfa2ca63eba2bccd096e030c6923cb65e7f214ee0191ebf.jpg)  
(5）

![](images/676ce1a936d22359cf5a18d280561b8befb20a98ea95be871fbc8f9035db6020.jpg)  
(6)

![](images/c2591b5da8cd534dfb5b65b8b85490cfc9d8c8220f2a3675cb70b1ee0fda2f63.jpg)  
Figure 2. Bulk silicon technological process. (1) clean the monocrystalline silicon wafer and etch the bonding platform; (2) dope with concentrated boron via a diffusion process; (3) sputter Au on the borosilicate glass; (4) bond the glass and silicon through the anode; (5) dry-etched with excess silicon; (6) etch the back of the silicon wafer.

![](images/fda65172d7360e6027ced40653b010c3b1c74780fcad670691f130a0acd67898.jpg)  
Figure 3. Fabricated accelerometer. 1. the upper electrode connected to sensing voltage; 2. the upper electrode connected to driving voltage; 3. the electrode connected to the tuning fork beam; 4. the lower electrode connected to driving voltage; 5. the lower electrode connected to sensing voltage.

Table 1. Structural parameters of the accelerometer.   

<table><tr><td>Parameters</td><td>Units</td><td>Design</td><td>Measurement</td></tr><tr><td>Length of fold beam</td><td>μm</td><td>500</td><td>472.5</td></tr><tr><td>Width of fold beam</td><td>μm</td><td>8</td><td>7.04</td></tr><tr><td>Spacing of fold beam</td><td>μm</td><td>14</td><td>16.2</td></tr><tr><td>Length of connecting beam</td><td>μm</td><td>160</td><td>148.4</td></tr><tr><td>Width of connecting beam</td><td>μm</td><td>9</td><td>7.5</td></tr><tr><td>Spacing of connecting beam</td><td>μm</td><td>4</td><td>4.95</td></tr><tr><td>Length of drive comb</td><td>μm</td><td>40</td><td>38.5</td></tr><tr><td>Width of drive comb</td><td>μm</td><td>5</td><td>4.79</td></tr><tr><td>Spacing of drive comb</td><td>μm</td><td>2</td><td>2.5</td></tr><tr><td>Pairs of drive comb</td><td>pair</td><td>19</td><td>19</td></tr><tr><td>Length of DETF</td><td>μm</td><td>700</td><td>661.6</td></tr><tr><td>Width of DETF</td><td>μm</td><td>8</td><td>7.4</td></tr><tr><td>Length of detection capacitor</td><td>μm</td><td>50</td><td>45.2</td></tr><tr><td>Width of detection capacitor</td><td>μm</td><td>6</td><td>4.87</td></tr><tr><td>Spacing of detection capacitor 1</td><td>μm</td><td>2</td><td>2.46</td></tr><tr><td>Spacing of detection capacitor 2</td><td>μm</td><td>10</td><td>10.56</td></tr><tr><td>Total pairs of detection capacitors</td><td></td><td>40</td><td>40</td></tr><tr><td>Length of proof mass</td><td>μm</td><td>620</td><td>609</td></tr><tr><td>Width of proof mass</td><td>μm</td><td>700</td><td>683</td></tr><tr><td>Length of damping hole</td><td>μm</td><td>10</td><td>12.41</td></tr><tr><td>Width of damping hole</td><td>μm</td><td>10</td><td>12.93</td></tr><tr><td>Number of damping hole</td><td></td><td>110</td><td>110</td></tr><tr><td>Structure layer thickness</td><td>μm</td><td>40</td><td>40.4</td></tr></table>

A WykoNt1100 optical profiler (VeecoInstruments Inc., Plainview, NY, USA) was used to test the accelerometer under an atmospheric pressure package. The test showed that the vibration amplitude was less than $10\mathrm{nm}$ and that the interface circuit was difficult to detect. Therefore, the microstructure was vacuum-packaged in a metal tube and shell to reduce resonance energy consumption. First, a single accelerometer chip was cut out of the silicon chip using laser-scribing technology; second, we applied an epoxy resin sealant on the bottom of the metal tube shell and stuck the independent chip on the surface of the substrate; third, using ultrasonic wire-bonding technology, the Au wire on the glass substrate was connected to the metal wire on the metal shell, and the shell was then capped using an ultrasonic welding process in a nitrogen environment; finally, the micro

accelerometer was placed in a temperature box and maintained at a high temperature of $60^{\circ}\mathrm{C}$ for two hours and then reduced to room temperature to complete the packaging of the whole device. The packaged accelerometer is shown in Figure 4 and uses a dual in-line package with eight pins $(20.8\mathrm{mm} \times 12.7\mathrm{mm} \times 5.5\mathrm{mm})$ . The degree of vacuum was estimated at nearly $30\mathrm{mTorr}$ and was maintained under high-vacuum conditions using a getter within the package.

![](images/64ad69d7cc7c12a135f990f6cd3b0fdb1a2e3ac8cf10d7d6fc07569561a9e091.jpg)  
Figure 4. Vacuum-packaged accelerometer.

# 3. Design of Measurement and Control Circuit for the Accelerometer

The fabricated micromechanical resonant accelerometer is symmetrical up and down and can be divided into two identical single resonant beam accelerometers. Taking a single resonant beam as an example, the measurement and control circuit includes a charge amplifier, an AC amplifier, a high-pass filter, a square wave generation circuit, a switch demodulation circuit, low-pass filter 1, a full-wave rectifier, low-pass filter 2, a phase shifter, a voltage divider, a subtraction circuit, a proportional-integral adjustment circuit, and a power supply circuit, as shown in Figure 5. Detection capacitance exists between detection electrode 5 and tuning fork electrode 3, and a fixed capacitance also exists between detection electrode 5 and driving electrode 4. Detection electrode 5 is connected to the charge amplifier, and the output signal has co-frequency interference, which is mainly generated by the coupling capacitance between detection electrode 5 and driving electrode 4. To eliminate co-frequency interference, the interface circuit adopts high-frequency square-wave modulation and switches the demodulation circuit [24].

![](images/62254626b07ce9a2446cd213f32e1af03b18dca2bf7809021859cb59adb4be70.jpg)  
Figure 5. The control circuit of the micro-accelerometer.1. the upper electrode connected to sensing voltage; 2. the upper electrode connected to driving voltage; 3. the electrode connected to the tuning fork beam; 4. the lower electrode connected to driving voltage; 5. the lower electrode connected to sensing voltage.

During the open-loop test, the acceleration in the sensitive direction was $0\mathrm{g}$ , and the three red-dotted circuits were disconnected, as shown in Figure 5. The AC test point was obtained by the AC drive voltage and was determined using the Agilent35670A dynamic signal analyzer (Agilent Technologies Inc., Santa Clara, CA, USA). The DC test point was determined using the DC drive voltage via the DC-stabilized power supply, and the signal output from the low-pass filter was connected to the feedback input of the Agilent35670A. The amplitude-frequency curve was obtained when the sweep frequency range

was $10 - 60\mathrm{kHz}$ , as shown in Figure 6. As the detection voltage was $1\mathrm{V}$ , the corresponding resonance frequency was $35.2986\mathrm{kHz}$ , and the quality factor Q was 1076. The corresponding resonant frequency changed nonlinearly with the change in the detection voltage.

![](images/6b0b2cadd3b9456e2967c1136279c9c3ae20f819f2990dca12bab182f20e0a89.jpg)  
Figure 6. Amplitude-frequency curve of micro-accelerometer sweep frequency test.

In the closed-loop measurements and control circuit design, the output sine wave signal was obtained through low-pass filter 1. One channel of the sine wave signal was connected to the driving comb electrode through the all-pass phase shifter. The other channel obtained the amplitude of the sine wave through full-wave rectification and low-pass filter 2. The DC amplitude voltage was subtracted from the reference voltage and was connected to the driving comb electrode through a resistor after proportional-integral adjustment, which resulted in automatic AC-DC control [25].

The sinusoidal signal, which was obtained from the open-loop test was proportional to the vibration displacement of the microstructure. Combined with Figure 5, the corresponding dynamic diagram is shown in Figure 7 and included two loops. One loop maintains the phase balance [26], and the other keeps the vibration amplitude constant. In Figure 7, $k_{1}$ is the gain coefficient of the charge amplifier; $\tau$ is the time constant of low-pass filter 2; $A$ is the DC voltage after filtering; $V_{R}$ is the DC reference voltage; $V_{d}$ is the DC driving voltage; $V_{ac}$ is the AC driving voltage; $\mu$ is the time constant of the phase shifter; $k_{p}$ and $k_{I}$ are the proportional and integral coefficients, respectively; $k_{2}$ is the voltage-force conversion coefficient related to the driving comb; and $r(t)$ is the equivalent driving force generated by thermal noise. Supposing that the vibration displacement of the resonant beam is $x(t), x(t) = a(t)\cos (\omega_{d}t + \phi (t))$ , the amplitude is $a(t)$ , the phase is $\phi (t)$ , and the angular frequency is $\omega_{d}$ .

![](images/ada5991403bcbe892b4254a5bfb02f193a6219e3e150af6f583c34536bf1bcf8.jpg)  
Figure 7. The closed-loop measurement and control circuit.

According to the dynamic principle of each module, the following analysis model was established:

$$
\left\{ \begin{array}{l} m \left(\ddot {x} + \frac {\omega}{Q} \dot {x} + \omega^ {2} x\right) = - K \cdot V _ {d} a (t) \sin \left(\omega_ {d} t + \phi (t) + \varphi\right) \\ \dot {A} (t) = \frac {1}{\tau} \left(| k _ {1} x | - A (t)\right) \\ \dot {V} _ {d} = k _ {p} \left(\dot {V} _ {R} - \dot {A}\right) + k _ {I} \left(V _ {R} - A\right) \end{array} \right. \tag {6}
$$

where $K = k_{1} \cdot k_{2}$ and $\ddot{x}(t), \dot{x}(t)$ , and $x(t)$ are substituted into formula system (6), and the slow time-varying system is solved with the principle of the averaging method as follows:

$$
\dot {a} (t) = - \frac {1}{2} a (t) \cdot \left(\frac {\omega_ {d}}{Q} - \frac {K V _ {d}}{m \omega_ {d}} \cos \varphi\right) \tag {7}
$$

$$
\dot {\phi} (t) = \frac {1}{2} \frac {K V _ {d}}{m \omega_ {d}} \sin \varphi \tag {8}
$$

$$
\dot {A} (t) = \frac {1}{\tau} \left(\frac {2}{\pi} k _ {1} a (t) - A (t)\right) \tag {9}
$$

$$
\dot {V} _ {d} (t) = k _ {I} \left(V _ {R} - A (t)\right) - k _ {p} \frac {1}{\tau} \left(\frac {2}{\pi} k _ {1} a (t) - A (t)\right) \tag {10}
$$

When the quality factor is large, the change in state variables of the slow time-varying system is close to 0. By making each state variable be 0 after derivation with time, two equilibrium points are obtained as follows:

$$
\left\{ \begin{array}{l} \overline {{a _ {0}}} = 0 \\ \overline {{A _ {0}}} = 0 \end{array} \right. \tag {11}
$$

$$
\left\{ \begin{array}{l} \bar {a _ {1}} = \frac {\pi V _ {R}}{2 k _ {1}} \\ \bar {A _ {1}} = V _ {R} \\ \bar {V _ {1 d}} = \frac {m \omega_ {d} ^ {2}}{K Q \cos \varphi} \end{array} \right. \tag {12}
$$

The variables $a(t), A(t)$ , and $V_{d}(t)$ represent linearization at the equilibrium points $(\overline{a_1},\overline{A_1},\overline{V_{1d}})$ , and the corresponding state equations are:

$$
\dot {a} (t) = - \frac {\omega_ {d}}{2 Q} \left(a (t) - \frac {\pi V _ {R}}{2 k _ {1}}\right) + \frac {\pi V _ {R}}{4 k _ {1}} \left(V _ {d} - \frac {\omega_ {d}}{Q}\right) \tag {13}
$$

$$
\dot {A} (t) = \frac {1}{\tau} \frac {2}{\pi} k _ {1} \left(a (t) - \frac {\pi V _ {R}}{2 k _ {1}}\right) - \frac {1}{\tau} \left(A (t) - V _ {R}\right) \tag {14}
$$

$$
\dot {V} _ {d} (t) = \left(k _ {p} \frac {1}{\tau} - k _ {I}\right) \left(A (t) - V _ {R}\right) - k _ {p} \frac {1}{\tau} \frac {2}{\pi} k _ {1} \left(a (t) - \frac {\pi V _ {R}}{2 k _ {1}}\right) \tag {15}
$$

The state equation characteristic matrix is:

$$
\left| \begin{array}{c c c} \frac {\omega_ {d}}{2 Q} & 0 & \frac {\pi V _ {R}}{4 k _ {1}} \\ \frac {2 k _ {1}}{\tau \pi} & - \frac {1}{\tau} & 0 \\ \frac {2 k _ {1} k _ {p}}{\tau \pi} & \frac {k _ {p}}{\tau} - k _ {I} & 0 \end{array} \right|
$$

The eigenvalue of the matrix $\lambda$ is solved as follows:

$$
\lambda^ {3} + \left(\frac {\omega_ {d}}{2 Q} + \frac {1}{\tau}\right) \lambda^ {2} + \left(\frac {\omega_ {d}}{2 Q \tau} + \frac {V _ {R} k _ {p}}{2 \tau}\right) \lambda + \frac {V _ {R}}{2 \tau} \left(\frac {2 k _ {p}}{\tau} - k _ {I}\right) = 0 \tag {16}
$$

According to the Routh criterion, the vibration stability of the driving mode needs to satisfy the below conditions:

$$
k _ {I} <   \frac {2 k _ {p}}{\tau} \tag {17}
$$

Thesystem has different poles and demonstrates different dynamic performances when changing $k_{p}, k_{I}$ , and $\tau$ in the system. According to Formula (12), the steady-state amplitude $a(t)$ is related to $V_{R}$ and $k_{1}$ and has nothing to do with the microstructure's stiffness, mass, resonant frequency, or quality factor. Under temperature disturbance, the amplitude of the closed-loop drive mode that corresponds to the frequency drift remains unchanged, and the measurement and control circuit can realize constant amplitude vibration and frequency tracking.

The system has two equilibrium points. When the amplitude of the equilibrium point $(\overline{a_0},\overline{A_0})$ is 0, the microstructure does not start to vibrate, and it is an unstable equilibrium point. If the microstructure can start to vibrate, the coefficient of the first-order term of the linear equation is greater than 0 $((a(t) > 0))$ , which satisfies the following equation:

$$
- \frac {1}{2} \left(\frac {\omega_ {0}}{Q} - \frac {K V _ {R}}{m \omega_ {0}} \cos \varphi\right) > 0 \tag {18}
$$

After solving inequality (18), we achieve

$$
V _ {R} > \frac {m \omega_ {0} {} ^ {2}}{K Q \cos \varphi} \tag {19}
$$

According to Formula (19), $V_{R}$ must be greater than the DC driving voltage corresponding to the static equilibrium point so that the microstructure of the driving mode can start to vibrate stably. The phase shift error $\varphi$ should be 0 under ideal conditions. When there is a phase offset, the larger the deviation angle, a larger $V_{R}$ is required [26].

According to the theoretical analysis, a self-excited oscillation measurement and control circuit is established, as shown in Figure 8. The measurement and control circuit are on the left, and the phase shifter adjusts the phase through a rheostat. When the acceleration in the sensitive direction is $0\mathrm{g}$ and the detection voltage is $1\mathrm{V}$ , the oscillation amplitude gradually increases and becomes stable after the micro-accelerometer is powered on. After adjusting the automatic gain circuit, the oscillation amplitude is constant. The vibration waveform is shown in Figure 9. After $2.83\mathrm{ms}$ , the amplitude was stable, and the peak-to-peak value was $2.89\mathrm{V}$ .

![](images/1b4d0fd299f6724f345343fc2a763be9c1112f64cb78845c41374b63e0b50740.jpg)  
Figure 8. Experimental device of the circuit.

After partially enlarging the waveform shown in Figure 9, the wave was a symmetrical sine wave, which is consistent with the theoretical design. The spectrum analyzer was used to analyze the stabilized sine wave, and the corresponding resonance frequency was $35.300\mathrm{kHz}$ , and the power was about $2.4\mathrm{dBV}$ .

![](images/808abb475c11cd717fa86d3f0e993df26bc961685922ad923ea5e3cdb5c80cc4.jpg)  
Figure 9. Oscillation observation waveform.

The accelerometer was manually placed into a tilted position, the acceleration changed from $0\mathrm{g}$ to $1\mathrm{g}$ , and the electrical signal corresponding to the vibration of the resonant beam is shown in Figure 10. When the acceleration jumped, the vibration amplitude was stable. As the acceleration changed, the amplitude was the same, and the middle represents the manual flip time of the accelerometer.

![](images/4ae40ee0a11639a8c122067596bb7136af03e7431db5b38c35629ec2b556a832.jpg)  
Figure 10. The acceleration jump oscillation process.

The self-made rotary slide and dial were able to achieve precise adjustments of $0.5^{\circ}$ and to provide acceleration input from $-1\mathrm{g}$ to $1\mathrm{g}$ through gravity decomposition. The test instrument is shown in Figure 8, and the corresponding voltage supply mode remained unchanged. The dial was adjusted to achieve a difference in the rotation angle of $15^{\circ}$ and to decompose the acceleration into the corresponding sine components. When the detection voltage changed to $2\mathrm{V}$ and the corresponding acceleration rotation angle ranged from $-90^{\circ}$ to $90^{\circ}$ , the relationship between the acceleration and output frequency is shown as in Figure 11, and the sensitivity was $321\mathrm{Hz / g}$ . When the detection voltage was $3\mathrm{V}$ , the large detection voltage corresponded to high sensitivity, but the output frequency and acceleration had a seriously nonlinear relationship.

![](images/2f98a5343c284dc26e46a34486d7476b4271c7f9e3a3b7af888ddf169ad61082.jpg)  
Figure 11. Sensitivity of the micro-accelerometer.

# 4. Analysis and Experiment of Output Stability

The micromechanical resonant accelerometer is sensitive to acceleration caused by the frequency, and the frequency's stability determines the resolution [27,28]. At the same time, it has been reported that a large vibration amplitude will lead to the coupling of amplitude and resonant frequency [29], so it is necessary to quickly and accurately analyze the stability of the steady-state vibration amplitude and the resonant frequency [30].

In Allan variance analysis, the sampling sequence is first grouped using the cluster analysis method, and the mean of each group is used as the next analysis target [31,32]. Then, the adjacent cluster means in the mean sequence are differed, and half of the mean square values of all of the differences is the Allan variance value, which represents the error situation of the sample sequence analyzed under a clustering time scale.

The steps for Allan variance analysis are provided below:

1. The sensor output signal is sampled using $\tau 0$ as the time interval, and a total of $N$ discrete sample data are collected to obtain the sampling sequence $\chi (i), i = 1,2,3,\ldots ,N$ .

2. Average grouping is performed on the sampling sequence $\chi(i)$ . First, the length parameter $\alpha$ and step-size parameter $\beta$ of the sample data group are set. $\alpha$ and $\beta$ are both positive integers; that is, each group contains $\alpha$ sample data for grouping, and the first data for adjacent groups are separated by the $\beta - 1$ interval. The time scale of each group is $\tau = \alpha \tau 0$ . Then, parameters $\alpha$ and $\beta$ are used to group the sampling sequence $\chi(i)$ , which must satisfy the condition $\alpha < N / 2$ , and $\alpha$ is an integer multiple of the step-size parameter $\beta$ . Finally, the average value of each group of data is calculated according to Formula (20), and the mean value sequence $\gamma(j), j = 1, 2, 3, \ldots, K$ is obtained. The mean value sample sequence contains $K$ data in total, and the exact value of the sequence length $K$ can be calculated according to Formula (21):

$$
\gamma (j) = \frac {1}{\alpha} \sum_ {i = 1} ^ {\alpha} \chi ((j - 1) \beta + i) \tag {20}
$$

$$
K = \left\lfloor \frac {N}{\alpha} \right\rfloor \frac {\alpha}{\beta} - \frac {\alpha}{\beta} + 1 \tag {21}
$$

3. The Allan variance is calculated according to the mean series. First, the difference between two "adjacent" mean samples in the mean sample sequence $\gamma (j)$ is calculated, and the difference sequence $Z(i)$ is obtained, as shown in Formula (22). Then the mean square value of the difference sequence $Z(i)$ is calculated, and multiplied by 0.5 to determine the Allan variance value, as shown in Formula (23).

$$
z (i) = \gamma \left(i + \frac {\alpha}{\beta}\right) - \gamma (i) \tag {22}
$$

$$
\sigma^ {2} = \frac {1}{2 \left(K - \frac {\alpha}{\beta}\right)} \sum_ {i = 1} ^ {K - \frac {\alpha}{\beta}} z (i) ^ {2} \tag {23}
$$

Formula (23) is the general calculation formula for Allan variance, and the value range of step parameter $\beta$ is $1, 2, 3, \ldots, \alpha$ . Step parameter $\beta = 1$ is the fully overlapping Allan variance, $\beta = \alpha$ is the non-overlapping Allan variance, and $1 < \beta < \alpha$ is the incomplete overlapping Allan variance, as shown in Figure 12.

![](images/f13bfdd38e1d5719d16873c074b4bead9d3a297d62414c173de05d4aac5083e6.jpg)  
Figure 12. Three Allan variance grouping methods.

4. The Allan variance is calculated by changing the group length $\alpha$ , and a logarithmic plot is created. Different group length parameters $\alpha$ correspond to different grouping methods and mean sample sequences for the same sampling sequence $\chi(i)$ , and the Allan variance values calculated by different $\alpha$ parameters are different. The value of parameter $\alpha$ needs to satisfy Formula (21). According to Formula (24), all of the $\alpha$ parameters that meet the requirements are calculated, and the corresponding Allan variance value is obtained. Finally, the time parameter $\tau = m\tau0$ is used as the independent variable, and the Allan-squared variance is used as the dependent variable to draw a double logarithmic graph. The error and stability of the sampling sequence can be seen in the graph.

$$
\alpha <   \frac {N}{2}, \frac {\alpha}{\beta} = p (p = 1, 2, 3 \dots \dots) \tag {24}
$$

The frequency meter (Agilent53132A, Agilent Technologies Inc., Santa Clara, CA, USA) and digital multi-meter (DM3068, Beijing RIGOL Inc. Beijing, China) were used to collect the frequency and amplitude data of the steady-state vibration, respectively. The sampling interval was set to $1\mathrm{~s}$ , and the sampling length was 1800. The entire sampling process lasted $30\mathrm{~min}$ . Figures 13 and 14 are the frequency and amplitude data curves, respectively $(\mathrm{Vs} = 2\mathrm{~V},$ acceleration is $0\mathrm{~g},$ room temperature is $28.10^{\circ}\mathrm{C})$ .

![](images/15704ec0ce621010113cb8c41a65a3542b00a38463881cb998b8907df8c57242.jpg)  
Figure 13. Frequency data samples.

![](images/47a6b9060ae090b69b84c177643189688077490cb068e9cc96dc5466586c7953.jpg)  
Figure 14. Amplitude data samples.

First, the high-precision variance analysis method in MATLAB software (MathWorks Inc. Natick, MA, USA) was used. When the fixed step parameter $\beta = 1$ and the group length parameter $\alpha$ traverses from 1 to 900, the Allan variance value is calculated under different group length parameters $\alpha$ . As shown in Figure 15, the curve of stability the analysis results is smooth and stable overall.

![](images/0fe39bee4bcd66d6905f7830343833b3b804a8b25c42b945b9746a14bd2449ca.jpg)  
Figure 15. Frequency data curve of Allan variance.

Then, the balanced variance analysis method was used. The step parameter is set to $\beta = 2$ , and the group length parameter $\alpha$ satisfies Formula (24). As shown in Figure 15, the fluctuation of the stability analysis curve was larger than that of the high-precision variance analysis curve.

Finally, the fast analysis of variance method was used. The step parameter is set to $\beta = \alpha$ , and the group length parameter $\alpha$ traverses all of the factors along the total length of the data $N$ . As shown in Figure 15, the curve demonstrating the stability results had many inflection points.

According to Figure 15, consistent curve trends were found in the double logarithmic plots obtained using the three methods. Among them, the high-precision variance analysis curve was the smoothest, and the calculated frequency deviation was the most accurate. The fast analysis variance curve contained the most inflection points and the lowest number of data points. The precision of the balanced variance analysis curve was between the two. The frequency deviation in the steady-state vibration of the accelerometer was less than $0.04\mathrm{Hz}$ , the resonant frequency was $35.29961\mathrm{kHz}$ , and the frequency deviation was within $\pm 10$ ppm.

Comparing the running times of the three analysis methods, Figure 16 shows that the execution time of high-precision variance analysis was much longer than that of the other two. The execution time increased exponentially as the length of the frequency sample sequence increased, while the execution time required for fast variance analysis was extremely short, while that required for balanced variance analysis was moderate.

![](images/c872a41612d95c39898a09c2b4c319d5c2f46cd5354af258149733776f93b7c1.jpg)  
Figure 16. Comparison chart of execution time.

In the same way, the amplitude data of the steady-state vibration in Figure 14 were used to perform stability analysis. The amplitude of the steady-state vibration signal of the sensor was $2.2\mathrm{V}$ , and the Allan variance analysis results can be seen in Figure 17. The deviation of the amplitude was less than $0.06\mathrm{mV}$ and was within $\pm 30$ ppm.

![](images/3df99d915ff6dc5649d6e2106e644d974263bc4f8d358e9d6ec376f3845da39b.jpg)  
Figure 17. Amplitude data curve for Allan variance.

The constant temperature experiment was carried out using a micromechanical accelerometer. The temperature error of the temperature experimental box was $\pm 0.01^{\circ}\mathrm{C}$ , and it was adjusted to $28.10^{\circ}\mathrm{C}$ . The experimental device is shown in Figure 18. A frequency meter was used to obtain the frequency data of the steady-state vibration, as shown in Figure 19, and to perform frequency stability analysis, as shown in Figure 20. The frequency deviation was less than $0.02\mathrm{Hz}$ after temperature control was implemented, which is significantly reduced when compared to that without temperature control. The resolution referring to the sensitivity analysis was determined to be $56\mathrm{ug}$ . Therefore, ambient temperature significantly affects the frequency stability of the accelerometer, and the resolution is higher under constant temperature conditions.

![](images/bc16300b5b8355017f28d3b29b4aaeb7a3629b63627e3e10010525fb9414c096.jpg)  
Figure 18. Constant temperature experimental box.

![](images/67f5d23e557e6693f8d2008449a2682369a3bd6796349629c62a15d7d74dbb50.jpg)  
Figure 19. Frequency samples after temperature control.

![](images/352cde2659aab59294722df593e22742a912e7e8f846baf6812be38abe6d9ef4.jpg)  
Figure 20. Variance analysis of FOAV.

# 5. Conclusions

This paper designed an in-plane vibration-type resonant micromechanical accelerometer based on electrostatic stiffness. The working principle of the accelerometer was analyzed, and the expression of the sensitivity was deduced. The open-loop experiment confirmed the adjustment effect of the loading voltage on the sensitivity. A large loading voltage corresponded to significant sensitivity, but excessive loading voltage increased nonlinearity. The self-excited oscillation measurement and control circuit experiment based on the average period method showed the vibration amplitude was related to the reference voltage and the preconversion coefficient of the interface circuit and had nothing to do with the quality factor. The stability analysis results of the frequency and vibration amplitude within $30\mathrm{min}$ at room temperature by the three Allan variance analysis methods were compared. The frequency deviation was determined to be $0.04\mathrm{Hz}$ , and the amplitude deviation was determined to be $0.06\mathrm{mV}$ . In the constant temperature experimental box, the temperature was stable within the deviation range of $0.01^{\circ}\mathrm{C}$ ; the frequency deviation decreased to $0.02\mathrm{Hz}$ . In Table 2, a comparison is shown between the proposed device and a few resonant accelerometers based on electrostatic stiffness reported in literature. Our work achieved the maximum sensitivity of $321\mathrm{Hz/g}$ in the range of $-1\mathrm{g}$ to $1\mathrm{g}$ and the resolution was $56\mathrm{ug}$ .

Among the three Allan variance analysis methods, high-precision Allan variance analysis has high calculation accuracy but requires a large amount of time for implementation; fast Allan variance analysis requires a very short amount of time, but the calculation accuracy is average, and balanced Allan variance analysis can change the balance between its calculation accuracy and execution time.

Table 2. Comparison between this device and reported resonant accelerometers.   

<table><tr><td>Items</td><td>Ref. [10]</td><td>Ref. [15]</td><td>Ref. [16]</td><td>Ref. [17]</td><td>Ref. [11]</td><td>Ref. [12]</td><td>Ref. [13]</td><td>Ref. [14]</td><td>This Work</td></tr><tr><td>Year of manufacture</td><td>2004</td><td>2014</td><td>2015</td><td>2016</td><td>2018</td><td>2019</td><td>2021</td><td>2022</td><td>2022</td></tr><tr><td>Resonant frequency(kHz)</td><td>24.88</td><td>24.85</td><td>13.69</td><td>2.44</td><td>3.625</td><td>20</td><td>186</td><td>25.5</td><td>35.3</td></tr><tr><td>Sensitivity (Hz/g@V)</td><td>128@N/A</td><td>14@2.5</td><td>32@25</td><td>10@1.5</td><td>5.09@5</td><td>20@35</td><td>45.8@35</td><td>56@15</td><td>321@2</td></tr><tr><td>Full scale range(g)</td><td>±1</td><td>±1</td><td>±1</td><td>0~10</td><td>±1</td><td>±1</td><td>&gt;25</td><td>N/A</td><td>±1</td></tr><tr><td>Resolution (ug)</td><td>5.2</td><td>N/A</td><td>727</td><td>N/A</td><td>4.3</td><td>27</td><td>8300</td><td>N/A</td><td>56</td></tr><tr><td>Bandwidth (Hz)</td><td>110</td><td>N/A</td><td>50</td><td>100</td><td>N/A</td><td>N/A</td><td>&gt;2000</td><td>N/A</td><td>&gt;1000</td></tr><tr><td>Thickness(um)</td><td>40</td><td>22</td><td>20</td><td>22</td><td>80</td><td>N/A</td><td>N/A</td><td>60</td><td>40</td></tr></table>

The axial force-sensitive resonant accelerometer and the electrostatic stiffness resonant accelerometer in this study belong to in-plane vibration. There are both movable resonant beams and acceleration-sensitive mass blocks. However, the motion directions of the resonant beams and acceleration-sensitive mass blocks in the axial force-sensitive accelerometer are perpendicular to each other, so the axial coupling effect is small. The resonant beam and the acceleration-sensitive mass in the electrostatic stiffness resonant accelerometer have the same motion direction and are coupled, and the sensitivity is nonlinear. The plate pull-in effect in the electrostatic stiffness resonant accelerometer limits the increase in the range, and the sensitivity will show significant nonlinearity with the increase in the range. A large electrostatic negative stiffness will also reduce the stability of the accelerometer. Still, the electrostatic stiffness resonant accelerometer has the advantage of using the loading voltage to tune the sensitivity and has little dependence on manufacturing error.

To improve the sensitivity and resolution of the silicon micro resonant accelerometer, the resonant frequency of the silicon micro resonant accelerometer would generally increase significantly, and the layer thickness of the microstructure would be reduced to less than $10\mathrm{um}$ , and the interface capacitance would be weak. The use of special integrated circuits could improve the sensor's resolution, but it would also increase the technical difficulty and development cost. The measurement and control circuit composed of discrete devices used in the low-frequency resonant accelerometer has a relatively large phase noise and small resolution. In this study, we need to pay attention to the phase noise and the resolution improvement.

Author Contributions: Design and experiment, H.L. and J.W.; simulation, Y.Z.; writing—original draft preparation, H.L.; writing—review and editing, Y.Z. All authors have read and agreed to the published version of the manuscript.

Funding: This work was funded by the National Key Research and Development Program (2019YFC1804704) and the Postgraduate Research & Practice Innovation Program of Jiangsu Province (SJCX22_0339).

Institutional Review Board Statement: It does not involve any moral or academic issues.

Informed Consent Statement: All authors were informed.

Data Availability Statement: All data are true and reliable.

Conflicts of Interest: The authors declare no conflict of interest.

# References

1. Yin, Y.; Fang, Z.; Han, F.; Yan, B.; Dong, J.; Wu, Q. Design and test of a micromachined resonant accelerometer with high scale factor and low noise. Sens. Actuators A 2017, 268, 52-60.   
2. Chun, Z.; Milind, P.; Guillermo, S.; Philipp, S.; Arif, M.; Xudong, Z.; Ashwin, S. A resonant MEMS accelerometer with 56ng bias stability and 98ng/Hz1/2 noise floor. J. Microelectromechan. Syst. 2019, 28, 324-326.   
3. Mustafazade, A.; Pandit, M.; Zhao, C. A vibrating beam MEMS accelerometer for gravity and seismic measurements. Sci. Rep. 2020, 10, 10415. [CrossRef] [PubMed]   
4. Jing, L.; Fan, S.; Cheng, L.; Guo, Z.; Liu, H. Design and analysis of micromechanical resonant accelerometer. In Proceedings of the 8th IEEE International Symposium on Instrumentation and Control Technology, London, UK, 11-13 July 2012.   
5. Huimin, Z.; Yating, Z.; Wei, Z. Design and analysis of MEMS biaxial coupled resonance accelerometer. In Proceedings of the 16th Annual IEEE International Conference on Nano/Micro Engineered and Molecular Systems, Xiamen, China, 25-29 April 2021.   
6. Yang, G.; Qiang, L.; Junwu, Z.; Junguang, L. Research status and development trend of micro-mechanical resonance accelerometer. High Power Laser Part. Beams 2017, 29, 080201.

7. Andrew, E.; Stone, K.J.; David, S.; Inseob, H.; Talso, C. Electrostatic frequency reduction: A negative stiffness mechanism for measuring dissipation in a mechanical oscillator at low frequency. Rev. Sci. Instrum. 2020, 92, 015101-015110.   
8. Al-Shudeifat, M.A. Effect of negative stiffness content on the periodic motion of nonlinearly coupled oscillators. J. Comput. Nonlinear Dyn. 2021, 16, 501-506. [CrossRef]   
9. Liu, L.; Nie, Y.; Lei, Y. A Novel Sensor Prototype with Enhanced and Adaptive Sensitivity Based on Negative Stiffness Mechanism. Sensors 2020, 20, 4644. [CrossRef]   
10. Seok, S.; Kim, H.; Chun, K. An inertial-grade laterally-driven MEMS differential resonant accelerometer. Sensors 2004, 11, 654-657.   
11. Yagang, W.; Jing, Z.; Zhichao, Y. A MEMS resonant accelerometer with high performance of temperature based on electrostatic spring softening and continuous ring-down technique. IEEE Sens. J. 2018, 18, 7023-7031.   
12. Shin, S.; Wen, H.; Hyun, K.K.; Vukasin, G. A dual-axis resonant accelerometer based on electrostatic stiffness modulation in epi-seal process. IEEE Sens. 2019, 10, 1-4.   
13. Shin, S.; Kwon, H.K.; Vukasin, G.; Kenny, T. A temperature compensated biaxial eFM accelerometer in epi-seal process. Sens. Actuators A Phys. 2021, 330, 112860-112870. [CrossRef]   
14. Huang, L.; Li, Q.; Qin, Y. Structural design and optimization of a resonant micro-accelerometer based on electrostatic stiffness by an improved differential evolution algorithm. Micromachines 2022, 13, 38. [CrossRef] [PubMed]   
15. Caspani, A.; Comi, C.; Corigliano, A. A differential resonant micro accelerometer for out-of-plane measurements. Procedia Eng. 2014, 87, 640-643. [CrossRef]   
16. Yang, B.; Wang, X.; Dai, B. A new z-axis resonant micro-accelerometer based on electrostatic stiffness. Sensors 2015, 15, 687-702. [CrossRef]   
17. Comi, C.; Corigliano, A.; Langfelder, G. Sensitivity and temperature behavior of a novel z-axis differential resonant micro accelerometer. J. Micromechan. Microeng. 2016, 26, 035006. [CrossRef]   
18. Eisuke, H.; Hiroshi, Y.; Yasuyuki, Y. Experimental amplitude and frequency control of a self-excited microcantilever by linear and nonlinear feedback. J. Micromechan. Microeng. 2022, 32, 34001-34014.   
19. Nan-Chyuan, T.; Chung-Yang, S. Experimental analysis and characterization of electrostatic-drive tri-axis micro-gyroscope. Sens. Actuators A 2010, 158, 231-239.   
20. Indeitsev, D.A.; Belyaev, Y.V.; Lukin, A.V.; Popov, I.A. Nonlinear dynamics of MEMS resonator in PLL-AGC self-oscillation loop. Nonlinear Dyn. 2021, 104, 3187-3204. [CrossRef]   
21. Hutomo, W.; Qing, Z.; Stephan, M.; Andreas, W. A phase locked loop frequency tracking system for portable micro electromechanical piezoresistive cantilever mass sensors. Microsyst. Technol. 2014, 20, 559-569.   
22. Jinlong, S.; Zhiyong, S.; Lvhua, W.; Hailiang, W. Random error analysis of MEMS gyroscope based on an improved DAVAR algorithm. Micromachines 2018, 9, 373.   
23. Qian, Z.; Xueyun, W.; Shiqian, W.; Chaoying, P. Application of improved fast dynamic Allan Variance for the characterization of MEMS gyroscope on UAV. J. Sens. 2018, 2018, 1-6.   
24. Liu, H.; Meng, R. Self-oscillation loop design and measurement for an MEMS resonant accelerometer. Int. J. Adapt. Control. Signal Process. 2013, 27, 859–872.   
25. Su, Y.; Xu, P.; Han, G.; Si, C.; Ning, J.; Yang, F. The characteristics and locking process of nonlinear MEMS gyroscopes. Micromachines 2020, 11, 233. [CrossRef]   
26. Linjun, A.; Hiroshi, Y. Self-excited oscillation produced by a phase shift: Linear and nonlinear instabilities. Nonlinear Dyn. 2022, 107, 587-597.   
27. Antonio, D.; Zanette, D.H.; López, D. Frequency stabilization in nonlinear micromechanical oscillators. Nat. Commun. 2012, 3, 806. [CrossRef] [PubMed]   
28. Olivier, M.; Xin, Z.; Rasul, R.G. Measuring frequency fluctuations in nonlinear Nano mechanical resonators. ACS Nano 2018, 12, 5753-5760.   
29. Defoort, M.; Hentz, S.; Shaw, S.W.; Shoshani, O. Amplitude stabilization in a synchronized nonlinear nanomechanical oscillator. Commun. Phys. 2022, 5, 93. [CrossRef]   
30. Jun, X.; Hui, L.; Xiao, W.; Danni, L.; Lishuang, F. Stability design of resonance frequency tracking system for sensing resonator. IEEE Sens. J. 2020, 20, 2570-2577.   
31. Jinyang, H.; Yang, Z.; GuoMing, X.; Qin, S.; Anping, Q. Systematic modeling of a MEMS resonant accelerometer based on displacement coordination. IEEE Sens. J. 2022, 22, 6454-6465.   
32. Li, L.; Liu, H.; Shao, M.; Ma, C. A novel frequency stabilization approach for mass detection in nonlinear mechanically coupled resonant sensors. Micromachines 2021, 12, 178. [CrossRef]