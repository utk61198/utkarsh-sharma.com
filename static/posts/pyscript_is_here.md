---
title: PyScript is here. But what does it mean for the future of web development?
date: 4/5/22
tags:
  - web development
  - python
slug: pyscript_is_here
postno: 1
---

# PyScript is here. But what does it mean for the future of web development?

Recently Anaconda announced PyScript, which allows us to embed Python code into HTML and run it in the browser. It is built on top of Pyodide (allows installation and execution of python packages in the browser with the help of micropip) and uses web assembly to translate python code into a website. The project is still in its formative phase, and many modules are not supported; therefore cannot be imported into the HTML file. Nevertheless, the future looks bright for PyScript as it is right now, the number one trending project on GitHub. Many developers are contributing to the project and fixing some of the common issues arising. PyScript will enable data scientists and machine learning enthusiasts to create web apps without learning JavaScript and other web development technologies. Many of the libraries such as pandas, numpy and matplotlib are supported directly out of the box.

<script src="https://gist.github.com/utk61198/14412e56a6eac7f03644bcb4596a8f1c.js"></script>


![Output](https://miro.medium.com/max/470/1*MR9NCFYpkY1PLVP1sHzvmA.png "output")

So does this mean everyone will leave the realm of JavaScript? Well, not in the near future. As good as PyScript sounds, it is still lacking some essential components. For example, while exploring the framework, I could not load the requests module since it is not supported yet. Only packages that Pyodide supports can be used. There is still a lot of work to be done. But one thing is for sure, the future of data-centric web development holds unlimited possibilities.
