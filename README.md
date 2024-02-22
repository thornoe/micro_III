# Microeconomics III
Slides for teaching exercise classes in [Microeconomics III](https://kurser.ku.dk/course/aØka08005u/2019-2020) at UCPH in Autumn 2019.

* [Session 1](https://github.com/thornoe/micro_III/blob/master/s1/main.pdf) ([manus](https://github.com/thornoe/micro_III/blob/master/s1/Manus_S1.docx?raw=true))
* [Session 2](https://github.com/thornoe/micro_III/blob/master/s2/main.pdf) ([manus](https://github.com/thornoe/micro_III/blob/master/s2/Manus_S2.docx?raw=true))
* [Session 3](https://github.com/thornoe/micro_III/blob/master/s3/main.pdf) ([manus](https://github.com/thornoe/micro_III/blob/master/s3/Manus_S3.docx?raw=true))
* [Session 4](https://github.com/thornoe/micro_III/blob/master/s4/main.pdf) ([manus](https://github.com/thornoe/micro_III/blob/master/s4/Manus_S4.docx?raw=true))
* [Session 5](https://github.com/thornoe/micro_III/blob/master/s5/main.pdf) ([manus](https://github.com/thornoe/micro_III/blob/master/s5/Manus_S5.docx?raw=true))
* [Session 6](https://github.com/thornoe/micro_III/blob/master/s6/main.pdf)
* [Session 7](https://github.com/thornoe/micro_III/blob/master/s7/main.pdf) ([manus](https://github.com/thornoe/micro_III/blob/master/s7/Manus_S7.docx?raw=true))
* [Session 8](https://github.com/thornoe/micro_III/blob/master/s8/main.pdf) and [*Recipe for a static Bayesian game*](https://github.com/thornoe/micro_III/blob/master/s8/static_bayesian_game.pdf)
* [Session 9](https://github.com/thornoe/micro_III/blob/master/s9/main.pdf) ([manus](https://github.com/thornoe/micro_III/blob/master/s9/Manus_S9.docx?raw=true)) and [*Auctions: Seller's expected revenue*](https://github.com/thornoe/micro_III/blob/master/s9/seller's_revenue.pdf)
* [Session 10](https://github.com/thornoe/micro_III/blob/master/s10/main.pdf)
* [Session 11](https://github.com/thornoe/micro_III/blob/master/s11/main.pdf) and [*Signaling games: Cookbook and notation*](https://github.com/thornoe/micro_III/blob/master/s11/cookbook_notation.pdf)
* [Session 12](https://github.com/thornoe/micro_III/blob/master/s12/main.pdf)

The "figures" folders contain Python code for Cournot and mixed strategy diagrams (sessions 2-4) as well as Inkscape (svg) files for the game trees (sessions 5-12).


## Drawing game trees
I draw the game trees in [Inkscape](https://inkscape.org/), which is a great piece of free software – when you have gotten used to it.
* Editing one of the existing game trees can be a quite straightforward start. If
* One can use LaTeX math mode such as `$x_1$`.
* Exporting an illustration to a LaTeX document can be a bit cumbersome. Choose a name without spacing and save it as type: “Portable Document Format (\*.pdf)” and choose “Omit text in PDF and create LaTeX file” and “Use exported object’s size”, which creates two new files (\*.pdf and \*.pdf_tex). Both must be included in the folder that is referred to in the LaTeX document using the code below (e.g. uploaded to [Overleaf](https://www.overleaf.com/)) to even see what the final figure looks like, as the files make little sense on their own.
```latex
\begin{figure}[!h]
  \center
  \def\svgwidth{.9\columnwidth} % "1.0" equals the width of the column
  \import{folder_name/}{figure_name.pdf_tex}
\end{figure}
```
* When editing figures or tables for LaTeX in an external program it becomes cumbersome to use Overleaf, as you need to upload each edition. Instead, consider setting up an offline text editor such as [Atom](https://github.com/thornoe/AtomSetup) or [Visual Studio Code](https://code.visualstudio.com) (with [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)).
* Troubleshoot errors when building in LaTeX:
    - If LaTeX can't build, it's usually due to free-floating rather than attached elements, typically dots or dashed lines. In Inkscape, two different selecting tools can be accessed by pressing `F1` and `F2` respectively. For dots one needs to use `F2` in order for them to 'attach' when hovering near the end of a line.
    - If white space is left at the right of the figure, reduce the font size in Inkscape as this only affects the area taken into account for the figure.

For students, I instead recommend drawing game trees in hand (or using PowerPoint) as it is the quickest and resembles the exam situation.
* Writing an assignments on the computer, one can take a picture or leave blank space to draw the figures after printing.
* Alternatively, an existing game tree can simply be coloured in Paint or PowerPoint.


## License
This project is released under the [MIT License]([https://github.com/thornoe/GreenGDP/blob/master/LICENSE](https://github.com/thornoe/micro_III/blob/master/LICENSE)), that is, you can basically do anything with my code as long as you give appropriate credit and don’t hold me liable.
