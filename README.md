# Research-G

Research-G is a library used for **researches**(which means that I do not focus too much on performance and easy-to-use and easy-to-improve are the two points I care most) on computer graphics and it can be used to make demos for computer graphics easily.  Research-G comprises **three parts, Research-M, Research-P and Research-V** which are used for mathematical computation, physical simulation and visualization respectively.  The dependencies between the three parts are research-M -> research-P, research-M -> research-V.

This repository is a complete library of research-G and you can also used three parts respectively.  Here are the link of the three repositories.
-	research-M:  https://github.com/ZhiqiLi-CG/Research-M.git
-	research-P: https://github.com/ZhiqiLi-CG/Research-P.git
-	research-V: https://github.com/ZhiqiLi-CG/Research-V.git

## 1. Research-M

You may ask, "Why Research-M?", since there are so many computation library like Eigen.  However, Eigen have the following disadvantages:

- Lazy Evaluation of Eigen is unstable and it is easy to be misused, especially in kernel function
- Only basic functions of Eigen could be used in device directly and many complexed functions could not be used, like computing eigen vectors of several small matrix. (Note: This senario exists.  Though cublas can compute a large matrix parallel, cublas could not compute several small matrix easily. )  

Research-M solves these problems and it also have other advantages:

- Research-M provides other advanced function, like homology computation of topology, moving linear square fitting and other geometry calculation.  
- It also provides other easy-to-use functions.  
- The functions in Research-M are designed to be used in both host and device, which means that you could write complexed kernel functions in CUDA based on the tools provided by Research-M.

## 2. Research-V

Research-V provide visualization tools for data, like point-cloud  drawer for physical simulation, Mapper and persistent homology  for data analysis.  The core of Research-V is the openGL adapter, which provides easy-to-use drawer and window manager for openGL.  There is some results of Research-V

-  Persistent Homology: 
-  bubble drawer: 
- Mapper:  

## 3. Research-P

**This is my original purpose of these libraries!** During the experiment of physical simulation , we must do calculation for physical process and visualize the result to see if the result is correct (Research-M and Research-V are born therefore).  During 

## 4. This Lib is Easy to Use!

The only thing you need to do in your cmakelist:(Take Research-V as example)

1. `include ` the `.cmake` file of the lib you want to use.
2. call the ``Set_ResearchV_Env`` before you ``add_execute``
3. call ``ResearchV_Deps`` to add all dependencies.

You could select some options during this process and the result of the options you select will be provided in a `config.h` file which is add to you project automatically.

If you have some questions, don't worry and each library provide several examples and you can build it by running the `make_project.py` directly without other config.