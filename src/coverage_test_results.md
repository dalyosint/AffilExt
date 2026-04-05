# Window of Interest Coverage Test

Review these outputs to ensure the `\author` and affiliation blocks are caught inside the window.

## Paper ID: 0704.0295
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: dcg_submission8.tex|>
%% version from Mar 20, 2008.
% AMS-LaTeX 1.2 sample file for journals, based on amsart.cls.
%
% Replace amsart by the documentclass for the target journal, e.g. tran-l.
%
\documentclass{amsart}

\usepackage{color}
\usepackage{graphicx,epsf}
\usepackage [cmtip,arrow]{xy}
\usepackage {pb-diagram,pb-xy} 

%%\usepackage [UglyObsolete,tight,heads=LaTeX] {diagrams}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\newtheorem{xca}[theorem]{Exercise}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{observation}[theorem]{Observation}
\newtheorem{notation}[theorem]{Notation}
\numberwithin{equation}{section}


%    Absolute value notation
\newcommand{\abs}[1]{\lvert#1\rvert}
%    Blank box placeholder for figures (to avoid requiring any
%    particular graphics capabilities for printing this document).
\newcommand{\blankbox}[2]{%
 \parbox{\columnwidth}{\centering
%    Set fboxsep to 0 so that the actual size of the box will match the
%    given measurements more closely.    \setlength{\fboxsep}{0pt}%
    \fbox{\raisebox{0pt}[#2]{\hspace{#1}}}%
  }%
}
% ----------------------------------------------------------------

\vfuzz2pt % Don't report over-full v-boxes if over-edge is small

\hfuzz2pt % Don't report over-full h-boxes if over-edge is small

% THEOREMS -------------------------------------------------------
\include{diagrams}
\newcommand{\norm}[1]{\left\Vert#1\right\Vert}

\renewcommand{\abs}[1]{\left\vert#1\right\vert}

\newcommand{\set}[1]{\left\{#1\right\}}

\newcommand{\Real}{{\mathbb R}}

\newcommand{\Z}{\mathbb Z}
\newcommand{\Q}{\mathbb Q}
%%\newcommand{\R}{{\rm  R}}
\newcommand{\Rc}{{\rm  R}}
\newcommand{\R}{{\mathbb  R}}

\newcommand{\N}{{\mathbb N}}
\newcommand{\hocolimit}{{\mathrm{hocolim}}}

\newcommand{\eps}{\varepsilon}

\newcommand{\f}{\mathbf{f}}

\newcommand{\w}{\mathbf{w}}

\newcommand{\x}{\mathbf{x}}

\newcommand{\y}{\mathbf{y}}

\newcommand{\z}{\mathbf{z}}

\newcommand{\To}{\longrightarrow}

\newcommand{\BX}{\mathbf{B}(X)}

\newcommand{\A} {\mathcal{A}}
\newcommand{\B} {\mathcal{B}}
\newcommand{\HH} {{\rm H}}

\newcommand{\D}{\mathcal{D}}

\newcommand {\E} {{\rm Ext}}
\newcommand {\RR} {{\mathcal R}}

\newcommand {\eqv} {\Leftrightarrow}

%%\newcommand {\s}    {{\mbox{\rm sign}}}


\newcommand {\ZZ} {{\rm Z}}
\newcommand {\level} {{\rm level}}
\newcommand {\hide}[1]{}

\renewcommand{\a}{\mathbf{a}}

\renewcommand{\x}{\mathbf{x}}

\renewcommand{\y}{\mathbf{y}}

\newcommand{\s}{\mathbf{s}}

\renewcommand{\z}{\mathbf{z}}
\newcommand{\Sphere}{{\mathbf  S}}
\newcommand{\Suspension}{{\mathbf  S}}

\newcommand{\dist}{{\rm  dist}}

\newcommand{\bigcupdot}
{\mathop{\makebox[0pt]{\hskip 1.4em $\boldsymbol\cdot$}\bigcup}}


\begin{document}

\title[Topological types of parametrized arrangements]{
On the number of topological  types occurring in a parametrized family 
of arrangements
\footnote{2000 Mathematics Subject Classification 14P10, 14P25}}
%    Information for first author
\author{Saugata Basu}
%%    Address of record for the research reported here
\address{School of Mathematics,
Georgia Institute of Technology, Atlanta, GA 30332, U.S.A.}
%%   Current address
\email{saugata.basu@math.gatech.edu}
%    \thanks will become a 1st page footnote.
\thanks{The author was supported in part by NSF grant CCF-0634907.}
\keywords{Combinatorial Complexity, O-minimal Structures, 
Homotopy Types, Arrangements}
% ----------------------------------------------------------------



--- START OF DOCUMENT TAIL ---
{proof}[Proof of Theorem \ref{the:homotopy_closed_ordinary}]
The proof is similar to that of Theorem
\ref{the:homotopy_closed_stable} given above, except we use
Theorem \ref{the:union_ordinary} instead of Theorem \ref{the:union_stable},
and this accounts for the slight worsening of the exponent in the bound.
\end{proof}

\begin{proof}[Proof of Theorem \ref{the:homotopy_general_ordinary}]
Using a construction due to Gabrielov and Vorobjov
\cite{GV07} (see also \cite{Basu9})
it is possible to replace any given ${\mathcal A}$-set 
by  a closed bounded ${\mathcal A}'$-set
(where ${\mathcal A}'$ is a new family of definable closely
related to ${\mathcal A}$ with 
$\#\A' = 2k(\#\A)$),
such that the new set has the same homotopy type as the original one.
Using this construction
one can directly deduce Theorem \ref{the:homotopy_general_ordinary}
from Theorem \ref{the:homotopy_closed_ordinary}. We omit the details.
\end{proof}

\bibliographystyle{amsplain}
\bibliography{master}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1822
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: cpma.tex|>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Energy Functionals for The Parabolic Monge-Ampere Equation
%
% Last Modified: Fri 13 Apr 2007 04:19:24 PM Eastern Daylight Time
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\documentclass[11pt]{amsart}
\usepackage{amsmath,amsthm}
\usepackage{cpma}
\usepackage{enumerate}

%\usepackage{enumerate}
%\usepackage{fullpage}
%\addtolength{\hoffset}{1.5cm}
%\addtolength{\oddsidemargin}{1.5cm}
%\addtolength{\textwidth}{.8 cm}
%\addtolength{\hoffset}{-0.4 cm}
%\addtolength{\voffset}{-0.2 cm}
%\addtolength{\textheight}{0.8 cm}
%\addtolength{\footskip}{0.5 cm}

\newtheorem{thm}{Theorem}
\newtheorem{prop}[thm]{Proposition}
\newtheorem{defn}[thm]{Definition}
\newtheorem{lem}[thm]{Lemma}
\newtheorem{cor}[thm]{Corollary}
\newtheorem{conj}[thm]{Conjecture}
\newtheorem{remark}[thm]{Remark}
%\newtheorem{question}[theorem]{Question}
%\newtheorem{condn}[theorem]{Condition}
%\newtheorem{observation}[thm]{Observation}

\newcommand{\ld}{\log\det}
\newcommand{\M}{\grad^2}
\newcommand{\ub}{\underline{u}{}}
\newcommand{\ccnorm}[1]{\norm{#1}_{\cC^2(\bar{\fO})}}
\newcommand{\llnorm}[1]{\norm{#1}_{L^2(\fO)}}
\newcommand{\lnorm}[1]{\norm{#1}_{L^1(\fO)}}

\DeclareMathOperator{\diam}{diam}
\DeclareMathOperator{\dist}{dist}
\DeclareMathOperator{\re}{Re}

%\baselineskip=12pt
\baselineskip=15pt

\begin{document}
\title{Energy Functionals for the Parabolic Monge-Amp\`{e}re Equation}

%\author{Zuoliang Hou \and Qi Li}
% AMSart 
\author{Zuoliang Hou}
\address{Mathematics Department, Columbia University, New York, NY 10027}
\email{hou@math.columbia.edu}
\author{Qi Li}
\address{Mathematics Department, Columbia University, New York, NY 10027}
\email{liqi@math.columbia.edu}
\date{\today}
\maketitle

\section{Introduction}

Because of its close connection with the \KH-Ricci flow, the parabolic
complex \MA{} equation on complex manifolds has been studied by many
authors.  See, for instance, \cite{Cao1985, ChenTian2002,
PhongSturm2006}.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\footnote{Maybe some more reference here?}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
On the other hand, theories for complex \MA{} equation on both
bounded domains and complex manifolds were developed in \cite{BedfordTaylor1976,
Yau1978, CKNS1985, Kolodziej1998}. 
In this paper, we are going to study the parabolic complex
\MA{} equation over a bounded domain. 

\

Let $\fO \subset \CC^n$ be a bounded domain with smooth boundary $\di\fO$.
Denote $\cQ_T=\fO \times
(0,T)$ with $T>0$, $B=\fO \times \left\{ 0 \right\} $, $\fG=\di\fO \times
\left\{ 0 \right\}$ and $\fS_T=\di\fO \times (0, T)$. Let $\di_p
\cQ_T$ be the parabolic boundary of $\cQ_T$, i.e. $\di_p \cQ_T = B
\cup \fG \cup \fS_T$. Consider the following boundary value problem:
\begin{equation}
  \left\{
  \begin{aligned}
    & \dod{u}{t} - \ld\big(u_{\fa\bar{\fb}}\big) = f(t, z, u) 
    && \text{ in } \cQ_T, \\ 
    & u= \vff           & & \text{ on } \di_p \cQ_T. 
  \end{aligned}
  \right.
  \label{eq:1}
\end{equation}
where $f \in \cC^{\infty}(\RR \times \bar{\fO} \times \RR)$ and $\vff
\in \cC^{\infty}(\di_p\cQ_T)$.
We will always assume that
\begin{equation}
  \dod{f}{u} \leq 0.
  \label{eq:2}
\end{equation}
Then we will prove that 

\begin{thm}
  Suppose there exists a spatial plurisubharmonic (psh) function  $\ub \in \cC^2(\bar{\cQ}_T)$
  such that
  \begin{equation}
  \left.
  \begin{aligned}
    & {\ub\,}_t - \ld \big({\ub\,}_{\fa\bar{\fb}}\big) \leq f(t, z, \ub)
    \qquad \qquad \text{ in } \cQ_T, \\
    & \ub \leq \vff \quad \text{on }\; B  \qquad \text{and} \qquad 
    \ub = \vff \quad \text{on }\; \fS_T \cap \fG.  
  \end{aligned}
  \right.
  \label{eq:3}
  \end{equation}
  Then there exists a spatial psh solution $u \in
  \cC^{\infty}(\bar{\cQ}_T)$ of (\ref{eq:1}) with $u \geq \ub$ if
  following compatibility condition is satisfied:
  $\forall\,z \in\di\fO$,
  \begin{equation}
    \begin{split}
     \vff_t - \ld\big( \vff_{\fa\bar{\fb}} \bi

--- START OF DOCUMENT TAIL ---
}), 
(\ref{eq:51}) and the uniform boundedness of $\det(u_{\fa\bar{\fb}})$,
we get
$$ \lim_{t\to \infty} \llnorm{u(\cdot, t)} = 0. $$
Since $\fO$ is bounded, the $L^2$ norm controls the $L^1$ norm, hence 
$$ \lim_{t\to \infty} \lnorm{u(\cdot, t)}=0. $$
Notice that by the Mean Value Theorem,
$$ | e^x - 1 | < e^{|x|} |x| $$
so
$$ \int_{\fO} |e^{\dot{u}} - 1 |\,dV \leq e^{\sup|\dot{u}|} \int_{\fO}
|\dot{u}|\,dV $$
Hence $e^{\dot{u}}$ converges to $1$ in $L^1(\fO)$ as $t$ approaches
$+\infty$. Now $u(\cdot,t)$ is bounded in $\cC^2(\lbar{\fO})$, so
$u(\cdot, t)$ converges to a unique function $\tilde{u}$, at least
sequentially in $\cC^1(\lbar{\fO})$, hence $f(z,u) \to f(z,\tilde{u})$
and 
$$ \det(\tilde{u}_{\fa\bar{\fb}}) = \lim_{t\to \infty} 
\det(u(\cdot,t)_{\fa\bar{\fb}}) = \lim_{t\to \infty} e^{\dot{u} -
f(z,u)} = e^{-f(z,\tilde{u})}, $$
i.e. $\tilde{u}$ solves (\ref{eq:8}). 

\qed 


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\bibliographystyle{alpha}
\bibliography{cpma}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1164
```latex
--- START OF DOCUMENT HEAD ---
mand{\bbP}{{\mathbb{P}}}
\newcommand{\bbE}{{\mathbb{E}}}
\newcommand{\bbZ}{{\mathbb{Z}}}
\newcommand{\bbC}{{\mathbb{C}}}
\newcommand{\bbQ}{{\mathbb{Q}}}
\newcommand{\bbT}{{\mathbb{T}}}
\newcommand{\bbS}{{\mathbb{S}}}

\newcommand{\calE}{{\mathcal E}}
\newcommand{\calS}{{\mathcal S}}
\newcommand{\calT}{{\mathcal T}}
\newcommand{\calM}{{\mathcal M}}
\newcommand{\calN}{{\mathcal N}}

%%%%%%%%%%%%%%%%%%  abbreviations %%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\dott}{\,\cdot\,}
\newcommand{\no}{\nonumber}
\newcommand{\lb}{\label}
\newcommand{\f}{\frac}
\newcommand{\ul}{\underline}
\newcommand{\ol}{\overline}
\newcommand{\ti}{\tilde  }
\newcommand{\wti}{\widetilde  }
\newcommand{\Oh}{O}
\newcommand{\oh}{o}
%\newcommand{%\marginlabel}[1]{\mbox{}%\marginpar{\raggedleft\hspace{0pt}#1}}
\newcommand{\tr}{\text{\rm{Tr}}}
\newcommand{\loc}{\text{\rm{loc}}}
\newcommand{\spec}{\text{\rm{spec}}}
\newcommand{\rank}{\text{\rm{rank}}}
%\newcommand{\ran}{\text{\rm{ran}}}
\newcommand{\dom}{\text{\rm{dom}}}
\newcommand{\ess}{\text{\rm{ess}}}
\newcommand{\ac}{\text{\rm{ac}}}
\newcommand{\singc}{\text{\rm{sc}}}
\newcommand{\sing}{\text{\rm{sing}}}
\newcommand{\pp}{\text{\rm{pp}}}
\newcommand{\supp}{\text{\rm{supp}}}
\newcommand{\AC}{\text{\rm{AC}}}
\newcommand{\bi}{\bibitem}
\newcommand{\hatt}{\widehat}
\newcommand{\beq}{\begin{equation}}
\newcommand{\eeq}{\end{equation}}
\newcommand{\ba}{\begin{align}}
\newcommand{\ea}{\end{align}}
\newcommand{\eps}{\varepsilon}
\newcommand{\del}{\delta}
\newcommand{\tht}{\theta}
\newcommand{\ka}{\kappa}
\newcommand{\al}{\alpha}
\newcommand{\be}{\beta}
\newcommand{\ga}{\gamma}
\newcommand{\partt}{\tfrac{\partial}{\partial t}}
\newcommand{\lan}{\langle}
\newcommand{\ran}{\rangle}
\newcommand{\til}{\tilde}
\newcommand{\tilth}{\til\tht}
\newcommand{\tilT}{\til T}
%\newcommand{\Ima}{\operatorname{Im}}
%\newcommand{\Real}{\operatorname{Re}}
%\newcommand{\diam}{\operatorname{diam}}

% use \hat in subscripts
% and upperlimits of int.


%
%  Rowan's unspaced list
%
\newcounter{smalllist}
\newenvironment{SL}{\begin{list}{{\rm\roman{smalllist})}}{%
\setlength{\topsep}{0mm}\setlength{\parsep}{0mm}\setlength{\itemsep}{0mm}%
\setlength{\labelwidth}{2em}\setlength{\leftmargin}{2em}\usecounter{smalllist}%
}}{\end{list}}


%%%%%%%%%%%%%%%%%%%%%% renewed commands %%%%%%%%%%%%%%%

%\renewcommand{\Re}{\text{\rm Re}}
%\renewcommand{\Im}{\text{\rm Im}}

%%%%%%%%%%%%%%%%%%%%%% operators %%%%%%%%%%%%%%%%%%%%%%
\DeclareMathOperator{\Real}{Re} \DeclareMathOperator{\Ima}{Im}
\DeclareMathOperator{\diam}{diam}
\DeclareMathOperator*{\slim}{s-lim}
\DeclareMathOperator*{\wlim}{w-lim}
\DeclareMathOperator*{\simlim}{\sim}
\DeclareMathOperator*{\eqlim}{=}
\DeclareMathOperator*{\arrow}{\rightarrow}
\DeclareMathOperator*{\dist}{dist} \DeclareMathOperator*{\divg}{div}
\DeclareMathOperator*{\Lip}{Lip} \allowdisplaybreaks
\numberwithin{equation}{section}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%% end of  definitions
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\newtheorem{theorem}{Theorem}[section]
\newtheorem*{t1}{Theorem 1}
\newtheorem*{t2}{Theorem 2}
\newtheorem*{t3}{Theorem 3}
\newtheorem*{t4}{Theorem 4}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
%\newtheorem{hypothesis}[theorem]{Hypothesis}
%\theoremstyle{hypothesis}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{xca}[theorem]{Exercise}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

% Absolute value notation
\newcommand{\abs}[1]{\lvert#1\rvert}


\begin{document}
\title[Front Speed-up and Quenching]
{Pulsating Front Speed-up and Quenching of Reaction \\ by Fast
Advection}

\author{Andrej Zlato\v s}

\address{\noindent Department of Mathematics \\ University of
Chicago \\ Chicago, IL 60637, USA \newline Email: \tt
zlatos@math.uchicago.edu}

%\date{April 3, 2007}



--- START OF DOCUMENT TAIL ---
ws, \rm Combustion
%Theory and Modelling {\bf 7} (2003), 487--508.

\bibitem{Weinberger}
H. Weinberger, \it On spreading speeds and traveling waves for
growth and migration models in a periodic habitat, \rm Jour. Math.
Biol. {\bf 45} (2002), 511--548.

\bibitem{Xin} J.~Xin, \it Existence and nonexistence of travelling waves and reaction-diffusion
front propagation in periodic media, \rm J. Stat. Phys. {\bf 73}
(1993), 893--926.

%\bibitem{Xin2} J.~Xin, \it Front propagation in heterogeneous media, \rm SIAM Rev. {\bf 42} (2000),
%161--230.

\bibitem{ZlaArrh} A.~Zlato\v s, \it Quenching and propagation of combustion without ignition
temperature cutoff, \rm Nonlinearity {\bf 18} (2005), 1463--1475.

\bibitem{ZlaMix} A. Zlato\v s, \it Diffusion in fluid flow: Dissipation enhancement by
flows in 2D, \rm preprint.

\bibitem{ZlaPercol} A.~Zlato\v s, \it Sharp Asymptotics for KPP Pulsating Front Speed-up and Diffusion
Enhancement by Flows, \rm preprint.

\end{thebibliography}


\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1330
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: paperfloer.tex|>
\documentclass[11pt]{amsart}
\usepackage{amssymb}
\textwidth15.8 cm
\voffset- .3cm
\textheight21 cm
\oddsidemargin.4cm
\evensidemargin.4cm
%\renewcommand\theenumi{\alph{enumi}}
%\renewcommand\theenumii{\roman{enumii}}

\numberwithin{equation}{section}
\renewcommand{\theequation}{\thesection .\arabic{equation}}

% Calligraphic letters 
%
\newcommand\A{\mathcal{A}}
\newcommand\M{\mathcal{M}}
\newcommand\G{\mathcal{G}}
\newcommand{\W}{\mathcal{W}}
\newcommand{\V}{\mathcal{V}}
\renewcommand{\L}{\mathcal{L}}
\renewcommand{\O}{\mathcal{O}}
\newcommand{\T}{\mathcal{T}}
\newcommand{\U}{\mathcal{U}}
\newcommand{\X}{\mathcal{X}}
\newcommand{\F}{\mathcal{F}}
%
% boldface letters
%
\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\bbT}{\mathbb{T}}
%
% Lie algebras
%
\newcommand\lie[1]{\mathfrak{#1}}

\newcommand{\fh}{\lie{h}}
\newcommand{\fg}{\lie{g}}
\newcommand{\fm}{\lie{m}}
\newcommand{\fz}{\lie{z}}
\newcommand{\Alc}{\lie{A}}
\newcommand{\fk}{\lie{k}}
\newcommand{\ft}{\lie{t}}
\newcommand{\fn}{\lie{n}}

\def	\inv	{^{-1}}

\newcommand{\Mg}[1]{M_{[ #1, \infty)}} 
\newcommand{\Ml}[1]{M_{(-\infty, #1]}} 

\newcommand{\Mgo}{\overline{M}_{ \geq 0}} 
\newcommand{\Mlo}{\overline{M}_{ \leq 0}} 

\usepackage{amsmath,amssymb}
\usepackage{picins,slashbox,dbnsymb,
  graphicx,verbatim,longtable,
  epic,eepic,stmaryrd,rotating}
\usepackage[all]{xy}

\theoremstyle{plain}
\newtheorem{principle}{Principle}
\newtheorem{axiom}{Axiom}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}{Proposition}[section]
\newtheorem{fact}[proposition]{Fact}
\newtheorem{lemma}[proposition]{Lemma}
\newtheorem{corollary}[proposition]{Corollary}
\newtheorem{claim}[proposition]{Claim}
\newtheorem{Truth}[proposition]{Truth}
\newtheorem{AlmostTruth}[proposition]{Almost Truth}
\newtheorem{conjecture}{Conjecture}
\newtheorem{slogan}{Slogan}

\theoremstyle{definition}
\newtheorem{definition}[proposition]{Definition}
\newtheorem{lemmadefinition}[proposition]{Lemma-Definition}
\newtheorem{problem}[proposition]{Problem}
\newtheorem{question}[proposition]{Question}
\newtheorem{solution}{Solution}
\newtheorem{prize}{Prize}

\theoremstyle{remark}
\newtheorem{example}[proposition]{Example}
\newtheorem{exercise}[proposition]{Exercise}
\newtheorem{hint}[proposition]{Hint}
\newtheorem{remark}[proposition]{Remark}
\newtheorem{warning}[proposition]{Warning}

\newcommand{\prtag}[1]{\tag*{\llap{$#1$\hskip-\displaywidth}}}

\newcommand{\mathmode}[1]{$#1$}
\newlength{\standardunitlength}
\setlength{\standardunitlength}{0.00083333in}

\newcommand{\eepic}[2]{
  \setlength{\unitlength}{#2\standardunitlength}
  \begin{array}{c}
    {\input #1.tex } 
  \end{array}
}
\newcommand{\silenteepic}[2]{
  \setlength{\unitlength}{#2\standardunitlength}
  \begin{array}{c}  \hspace{-1.7mm}
    \raisebox{-2pt}{\input #1.tex }
    \hspace{-1.9mm}
  \end{array}
}

\newcommand{\fig}[1]{figure~\ref{#1}}
\def\smily{{
  \setlength{\unitlength}{0.4\standardunitlength}
  \begin{array}{c}  \hspace{-1.7mm} \raisebox{-2pt}{
    \begin{picture}(616,629)(0,-10)
    \thicklines
    \put(308.000,344.500){\arc{375.000}{0.6435}{2.4981}}
    \put(308,307){\ellipse{600}{600}}
    \put(195,382){\blacken\ellipse{76}{76}}
    \put(195,382){\ellipse{76}{76}}
    \put(420,382){\blacken\ellipse{76}{76}}
    \put(420,382){\ellipse{76}{76}}
    \end{picture}
  }
  \hspace{-1.9mm}
  \end{array}
}}

\catcode`\@=11
\long\def\@makecaption#1#2{%
    \vskip 10pt
    \setbox\@tempboxa\hbox{%\ifvoid\tinybox\else\box\tinybox\fi
      \small{#1: }\ignorespaces #2}%
    \ifdim \wd\@tempboxa >\captionwidth {%
        \rightskip=\@captionmargin\leftskip=\@captionmargin
        \unhbox\@tempboxa\par}%
      \else
        \hbox to\hsize{\hfil\box\@tempboxa\hfil}%
    \fi}
\font\bfcaptionfont=cmssbx10 scaled \magstephalf
\newdimen\@captionmargin\@captionmargin=2\parindent
\newdimen\captionwidth\captionwidth=\hsize
\catcode`

--- START OF DOCUMENT TAIL ---
1342,1962)(1354,1940)
	(1364,1919)(1374,1899)(1381,1879)
	(1388,1860)(1393,1841)(1397,1822)
	(1400,1801)(1401,1780)(1400,1759)
	(1398,1738)(1394,1715)(1389,1693)
	(1383,1670)(1375,1646)(1366,1622)
	(1356,1599)(1346,1575)(1334,1552)
	(1322,1529)(1309,1506)(1297,1485)
	(1284,1463)(1271,1443)(1259,1423)
	(1247,1404)(1235,1384)(1221,1364)
	(1208,1343)(1194,1322)(1181,1301)
	(1166,1280)(1152,1259)(1137,1239)
	(1122,1219)(1106,1200)(1090,1182)
	(1074,1166)(1058,1151)(1042,1138)
	(1026,1126)(1009,1116)(993,1108)
	(976,1102)(960,1097)(944,1094)
	(927,1093)(910,1093)(892,1094)
	(873,1096)(853,1099)(832,1104)
	(810,1110)(788,1117)(765,1125)
	(742,1134)(718,1144)(695,1154)
	(671,1165)(648,1176)(624,1187)
	(602,1199)(579,1211)(557,1223)
	(535,1234)(516,1245)(497,1255)
	(477,1266)(457,1277)(436,1288)
	(414,1300)(391,1314)(365,1328)
	(339,1343)(310,1359)(280,1376)
	(249,1393)(216,1412)(184,1430)
	(152,1448)(122,1465)(95,1481)
	(72,1494)(53,1505)(39,1512)
	(29,1518)(24,1521)(22,1522)
\end{picture}
}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0831
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: ShraderEphremidesIWCMC07ArxivVersion.tex|>
\documentclass[10pt,conference]{IEEEtran}

\usepackage{cite}
\usepackage{subfigure}
\usepackage{graphicx}
\usepackage{url}
\usepackage{amsmath}
\usepackage{amssymb}
\interdisplaylinepenalty=2500

\hyphenation{op-tical net-works semi-conduc-tor}

\begin{document}

% paper title
\title{On packet lengths and overhead for random linear coding over the erasure channel}


% author names and affiliations
% use a multiple column layout for up to three different
% affiliations
\author{
\authorblockN{Brooke Shrader and Anthony Ephremides}
\authorblockA{Electrical and Computer Engineering Dept\\
and Institute for Systems Research \\
University of Maryland \\
College Park, MD 20742 \\
bshrader, etony@umd.edu} }

% make the title area
\maketitle



--- START OF DOCUMENT TAIL ---
. Palanki, B.
Hassibi and M. Effros, ``Capacity of wireless erasure networks,''
{\it IEEE Trans. Inform. Theory}, vol. 52, no. 3, pp. 789-804, 2006.
%note that the authors here state (footnote, p. 7) that their results hold for arbitrary alphabet size

\bibitem{SmithVishwanath06} B. Smith and S. Vishwanath, ``Asymptotic
transport capacity of wireless erasure networks,'' {\it Allerton}
conference, 2006.


%\bibitem{LiCaiYeung05} S.-Y. R. Li, N. Cai, and R. W. Yeung, ``On
%theory of linear network coding,'' ISIT 2005. %%discusses existence of a network code for suff large field size

\bibitem{HongNosratinia02} B. Hong and A. Nosratinia,
``Rate-constrained scalable video transmission over the Internet,''
{\it IEEE Packet Video Workshop}, 2002.

\bibitem{MacKay98} D. J. C. MacKay, ``Fountain codes,'' IEE Workshop
on Discrete Event Systems, 1998.

\bibitem{Proakis} J. G. Proakis, {\it Digital Communications,} Third
edition, McGraw-Hill, Boston, 1995.

\end{thebibliography}


\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1941
```latex
--- START OF DOCUMENT HEAD ---
nmargin
      \unhbox\@tempboxa\par}%
   \else
      \hbox to\captionwidth{\hfil\box\@tempboxa\hfil}%
   \fi}%
%
\def\fignr{\small\sffamily\bfseries}%
\def\capt{\small\sffamily}%


\newdimen\@captionmargin\@captionmargin2\parindent\relax
\newdimen\captionwidth\captionwidth\hsize\relax

\def\nin{\not\in}
\def\bQ{{\Bbb Q}}
\def\bC{{\Bbb C}}
\def\bR{{\Bbb R}}
\def\bN{{\Bbb N}}
\def\bZ{{\Bbb Z}}
\def\cE{{\cal E}}
\def\cK{{\cal K}}
\def\cI{{\cal I}}
\def\cR{{\cal R}}
\def\cV{{\cal V}}
\def\cO{{\cal O}}
\def\hD{{\hat D}}
\def\cD{{\cal D}}
\def\cX{{\cal X}}
\def\hK{{\hat K}}
%\def\bt{\bar t_2}
\def\bm{\bar t'_2}
\let\bt\bm 

\def\pr{\text{\rm pr}\,}
\def\ncap{\not\mathrel{\cap}}
\def\|{\mathrel{\kern1.5pt\Vert\kern1.5pt}}
\def\lra{\longrightarrow}
\def\llra{\longleftrightarrow}
\let\ds\displaystyle
\let\reference\ref
\def\so{\Rightarrow}
\let\x\exists
\let\fa\forall
\let\es\enspace

\let\x\exists
\let\sg\sigma
\let\tl\tilde
\let\ap\alpha
\let\dl\delta
\let\Dl\Delta
\let\be\beta
\let\gm\gamma
\let\Gm\Gamma
\let\nb\nabla
\let\Lm\Lambda
\let\sm\setminus
\let\vn\varnothing
\let\dt\det
\def\tG{\tl G}
\def\tD{\tl D}
\def\tS{\tl S}

\let\eps\varepsilon
\let\ul\underline
\let\ol\overline
\def\md{\min\deg}
\def\Md{\max\deg}
\def\Mcf{\max{\operator@font cf}}
\let\Mc\Mcf
\def\sgn{{\operator@font sgn}}

\def\ssim{\stackrel{\ds \sim}{\vbox{\vskip-0.2em\hbox{$\scriptstyle *$}}}}

\def\bysame{\same[\kern2cm]\,}
\def\qed{\hfill\@mt{\Box}}
\def\@mt#1{\ifmmode#1\else$#1$\fi}

\def\proof{\@ifnextchar[{\@proof}{\@proof[\unskip]}}
\def\@proof[#1]{\noindent{\bf Proof #1.}\enspace}

\def\myfrac#1#2{\raisebox{0.2em}{\small$#1$}\!/\!\raisebox{-0.2em}{\small$#2$}}
\newcommand{\mybr}[2]{\text{$\Bigl\lfloor\mbox{%
\small$\displaystyle\frac{#1}{#2}$}\Bigr\rfloor$}}
\def\mybrtwo#1{\mbox{\mybr{#1}{2}}}


\def\epsfs#1#2{{\ifautoepsf\unitxsize#1\relax\else
\epsfxsize#1\relax\fi\epsffile{#2.eps}}}
\def\epsfsv#1#2{{\vcbox{\epsfs{#1}{#2}}}}
\def\vcbox#1{\setbox\@tempboxa=\hbox{#1}\parbox{\wd\@tempboxa}{\box
  \@tempboxa}}

\def\@test#1#2#3#4{%
  \let\@tempa\go@
  \@tempdima#1\relax\@tempdimb#3\@tempdima\relax\@tempdima#4\unitxsize\relax
  \ifdim \@tempdimb>\z@\relax
    \ifdim \@tempdimb<#2%
      \def\@tempa{\@test{#1}{#2}}%
    \fi
  \fi
  \@tempa
}

\def\go@#1\@end{}
\newdimen\unitxsize
\newif\ifautoepsf\autoepsftrue

\unitxsize4cm\relax
\def\epsfsize#1#2{\epsfxsize\relax\ifautoepsf
  {\@test{#1}{#2}{0.1 }{4   }
		{0.2 }{3   }
		{0.3 }{2   }
		{0.4 }{1.7 }
		{0.5 }{1.5 }
		{0.6 }{1.4 }
		{0.7 }{1.3 }
		{0.8 }{1.2 }
		{0.9 }{1.1 }
		{1.1 }{1.  }
		{1.2 }{0.9 }
		{1.4 }{0.8 }
		{1.6 }{0.75}
		{2.  }{0.7 }
		{2.25}{0.6 }
		{3   }{0.55}
		{5   }{0.5 }
		{10  }{0.33}
		{-1  }{0.25}\@end
		\ea}\ea\epsfxsize\the\@tempdima\relax
		\fi
		}

% \input{myeqn.tex}

\let\diagram\diag

\def\boxed#1{\diagram{1em}{1}{1}{\picbox{0.5 0.5}{1.0 1.0}{#1}}}

 
\def\rato#1{\hbox to #1{\rightarrowfill}}
\def\arrowname#1{{\enspace
\setbox7=\hbox{F}\setbox6=\hbox{%
\setbox0=\hbox{\footnotesize $#1$}\setbox1=\hbox{$\to$}%
\dimen@\wd0\advance\dimen@ by 0.66\wd1\relax
$\stackrel{\rato{\dimen@}}{\copy0}$}%
\ifdim\ht6>\ht7\dimen@\ht7\advance\dimen@ by -\ht6\else
\dimen@\z@\fi\raise\dimen@\box6\enspace}}


\def\contr{\diagram{1em}{0.6}{1}{\piclinewidth{35}%
\picstroke{\picline{0.5 1}{0.2 0.4}%
\piclineto{0.6 0.6}\picveclineto{0.3 0}}}}

% \def\caselist{\bgroup
% %\leftmargin -2mm\relax
% % \itemsep\z@\relax
% % \labelwidth\z@\relax
% \begin{enumerate}%\listitemsep\z@
% \let\case\item
% \def\labelenumi{{\bf Case \theenumi.}}
% \def\labelenumii{{\bf Case \theenumi.\theenumii.}}
% }

\newcounter{pp}%
\newenvironment{mylist}[1]{%
\begin{list}{#1{pp})}%
{\usecounter{pp}\setlength{\labelwidth}{4mm}%
\setlength{\leftmargin}{0.6cm}\setlength{\itemsep}{1mm}%
\setlength{\topsep}{1mm}}%
\gdef\myitem{\item\xdef\@currentlabel{#1{pp})}}%
}{\end{list}}
% \def\endcaselist{\end{enumerate}\egroup}


\def\abstractname{}
 

\parskip5pt plus 1pt minus 2pt
\parindent\z@
  
   
{\let\@noitemerr\relax
\vskip-2.7em\kern0pt

--- START OF DOCUMENT TAIL ---
987), 187--194.
\bibitem[Mu2]{Murasugi2} \bysame\,, \em{Jones polynomials and classical
	conjectures in knot theory II}, Math. Proc. Cambridge
	Philos. Soc. {\bf 102(2)} (1987), 317--318. 
\bibitem[Pe]{Perko} K.~A.~Perko Jr., \em{On the classification of
	knots}, Proc. Amer. Math. Soc. {\bf 45} (1974), 262--266.
\bibitem[Ro]{Rolfsen} D.~Rolfsen, {\em Knots and links}, Publish
	or Perish, 1976.
\bibitem[S]{Silver} D.~S. Silver, {\em Knot Theory's Odd Origins},
	American Scientist {\bf 94(2)} (2006), 158--165.
\bibitem[Th]{Thistle} M.~B.~Thistlethwaite, {\em On the Kauffman
	polynomial of an adequate link}, Invent.\ Math. {\bf 93(2)}
	(1988), 285--296.
\bibitem[Th2]{Thistle2} \bysame\,, {\em A spanning tree expansion of
	the Jones polynomial}, Topology {\bf 26(3)} (1987), 297--309.
\bibitem[Th3]{Thistle3} \bysame\,, {\em On the structure and scarcity
	of alternating links and tangles},
	J. Knot Theory Ramifications {\bf 7(7)} (1998), 981--1004.
\end{thebibliography}
}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1001
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: taut.tex|>
\documentclass[a4paper,12pt]{amsart}

\usepackage{array}

\usepackage{epsf}
\newcommand{\inspic}[1]{\begin{tabular}{c}\epsfbox{#1}\end{tabular}}

\newtheorem{theorem}{Theorem}
\newtheorem{corollary}{Corollary}
\newtheorem{lemma}{Lemma}
\newtheorem{proposition}{Proposition}

\def\oM{{\overline{\mathcal{M}}}}
\def\C{\mathbb{C}}
\def\Z{\mathbb{Z}}
\def\CP{\mathbb{C}\mathrm{P}}
\def\d{\partial}
\def\F{\mathcal{F}}

\title{Tautological relations in Hodge field theory}

\author{A.~Losev}

\address{Institute for Theoretical and Experimental Physics, Bolshaya 
Che\-remushkinskaya 25, Moscow, 117218, Russia.}
\email{losev@itep.ru}

\author{S.~Shadrin}

\address{Department of Mathematics, University of Zurich,
Win\-ter\-thu\-rer\-stras\-se 190, CH-8057 Zurich, Switzerland.}

\email{sergey.shadrin@math.unizh.ch}

\author{I.~Shneiberg}

\address{Department of Algebra, Faculty of Mechanics and Mathematics,
Moscow State University, Leninskie Gory, GSP, Moscow, 119899, Russia.}

\email{shneiberg@mtu-net.ru}

\begin{document}



--- START OF DOCUMENT TAIL ---
point in graph calculus, 
arXiv: math.QA/0507106.

\bibitem{ss} S.~Shadrin, I.~Shneiberg, Belorousski-Pandharipande relation in dGBV algebras,
J. Geom. Phys. \textbf{57} (2007), no. 2, 597--615.

\bibitem{shn} I.~Shneiberg, Topological recursion relations in $\oM_{2,2}$, to appear in Funct. Anal. Appl. (2007).

\bibitem{t} U.~Tillmann, Vanishing of the Batalin-Vilkovisky algebra structure for TCFTs, 
Comm. Math. Phys. \textbf{205} (1999), no. 2, 283-286.

\bibitem{Witten} E. Witten, Two dimensional gravity and intersection theory on moduli space. 
Surveys in Differential Geometry, vol.~1 (1991), 243--310.

\bibitem{wit-na} E. Witten, Chern-Simons gauge theory as a string theory, The Floer memorial volume,
 637--678, Progr. Math.~\textbf{133}, Birkhaeuser, Basel, 1995.

\bibitem{zwi} B. Zwiebach, Closed string field theory: quantum action and the Batalin-Vilkovisky 
master equation, Nuclear Phys.~B \textbf{390} (1993), no. 1, 33--152.

\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2146
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: z-031216.tex|>
\documentclass[12pt]{article}
\usepackage{e-jc}
\usepackage{amsthm,amsmath,amssymb}
\usepackage{graphicx}
\usepackage[colorlinks=true,citecolor=black,linkcolor=black,urlcolor=blue]{hyperref}
\newcommand{\doi}[1]{\href{http://dx.doi.org/#1}{\texttt{doi:#1}}}
\newcommand{\arxiv}[1]{\href{http://arxiv.org/abs/#1}{\texttt{arXiv:#1}}}
\newcommand\QQ{\hbox{I\kern-.53em\hbox{Q}}}
\newcommand{\Z}{\hbox{\bf Z}}
\newcommand{\PP}{\hbox{\bf P}}
\newcommand{\R}{\hbox{\bf R}}
\newcommand{\F}{\hbox{\bf F}}
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{fact}[theorem]{Fact}
\newtheorem{observation}[theorem]{Observation}
\newtheorem{claim}[theorem]{Claim}

\theoremstyle{plain}%{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\newtheorem{examples}[theorem]{Examples}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{open}[theorem]{Open Problem}
\newtheorem{problem}[theorem]{Problem}
\newtheorem{question}[theorem]{Question}

\theoremstyle{plain}%{remark}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{note}[theorem]{Note}

\title{\bf Connected Edge-Disjoint Unions of Tur\'an Graphs}

\author{Italo J. Dejter\\
\small Department of Mathematics\\[-0.8ex]
\small University of Puerto Rico\\[-0.8ex]
\small Rio Piedras, PR 00936-8377\\
\small\tt italo.dejter@gmail.com\\
}

\date{\dateline{April 1, 2016}{XX}\\
\small Mathematics Subject Classifications: 05B25, 05C62, 05C75, 05E20}

\begin{document}

\maketitle



--- START OF DOCUMENT TAIL ---
55.
\bibitem{Dej2}
I. J. Dejter, On a {\it $\{K_4,K_{2,2,2}\}$-ultraho\-mo\-ge\-neous graph}, Austral. J. Combin., {\bf 44} (2009), 63--75.
\bibitem{Gard} A. Gardiner, {\it Homogeneous graphs}, J. Combinatorial Theory (B), {\bf 20}
    (1976), 94--102.
\bibitem{GK}
Ja. Ju. Gol'fand, M. H. Klin, {\it On $k$-ho\-mo\-ge\-neous graphs},
Algorithmic Stud. Combin., {\bf 186} (1978), 76--85 (in Russian).
\bibitem{Is}
D. C. Isaksen, C. Jankowski, S. Proctor, {\it On
$K_*$-ultraho\-mo\-ge\-neous graphs}, Ars Combin., {\bf 82} (2007),
83--96.
\bibitem{Por}  M. Klin, R. P\"oschel, K. Rosenbaum, Angewandte Algebra f\"ur Mathematiker und Informatiker, (in German)
    Friedr. Vieweg and Sohn, Braunschweig, 1988.

\bibitem{Sven} S. Reichard, {\it A criterion for the $t$-vertex condition of graphs}, J. Combin. Theory Ser. A {\bf 90} (2000), 304--314.
\bibitem{Ronse}
C. Ronse, {\it On ho\-mo\-ge\-neous graphs}, J. London Math. Soc.,
{\bf s2-17}, (1978), 375--379.
\end{thebibliography}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2384
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: fawnsc.tex|>
\documentclass[11pt]{amsart}
\usepackage{amssymb,amsmath,amsthm,enumerate}

\newtheorem{thm}{Theorem}[section]
\newtheorem{lem}[thm]{Lemma}
\newtheorem{cor}[thm]{Corollary}
\newtheorem{prop}[thm]{Proposition}
\newtheorem{conj}[thm]{Conjecture}
\newtheorem{quest}[thm]{Question}

\theoremstyle{remark}
\newtheorem{exm}{Example}
\newtheorem{rem}[thm]{Remark}
\theoremstyle{definition}
\newtheorem{defi}[thm]{Definition}

\newcommand {\Zz} {\mathbb{Z}}
\newcommand {\Nz} {\mathbb{N}}
\newcommand {\Cz} {\mathbb{C}}
\newcommand {\Qz} {\mathbb{Q}}
\newcommand {\Rz} {\mathbb{R}}
\newcommand {\Fz} {\mathbb{F}}
\newcommand {\Sz} {\mathbb{S}}
\newcommand {\CF} {{\mathcal F}}
\newcommand {\Oc} {{\mathcal O}}
\newcommand {\id} {\mbox{id}}
\newcommand{\BAR}{\overline}
\DeclareMathOperator{\modu}{mod \:}
\DeclareMathOperator{\SL}{SL}
\DeclareMathOperator{\GL}{GL}
\DeclareMathOperator{\Irr}{Irr}
\DeclareMathOperator{\diag}{diag}
\DeclareMathOperator{\w}{w}
\DeclareMathOperator{\Rep}{{\mathcal R}\it ep}

\DeclareMathOperator{\PSp}{PSp}
\DeclareMathOperator{\Sp}{Sp}
\DeclareMathOperator{\PSL}{PSL}
\DeclareMathOperator{\PSU}{PSU}
\DeclareMathOperator{\SO}{SO}

\newcommand{\defst}[1]{{\it #1}}

\begin{document}

\title{Fusion algebras with negative structure constants}
\author{Michael Cuntz}
\thanks{}
\address{Michael Cuntz, Universit\"at Kaiserslautern,
Postfach 3049, 67653 Kaiserslautern}
\email{cuntz@mathematik.uni-kl.de}
\keywords{fusion algebra, table algebra, Hadamard matrix}



--- START OF DOCUMENT TAIL ---
[ I=\langle
 \sum_m (T_{i,m}-\sum_{j=1}^n \lambda_{ij}T_{\tau(j),m}) c_m
 \mid i=1,\ldots,2^n \rangle .\]
Now it suffices to check that the coefficient
$T_{i,m}-\sum_{j=1}^n \lambda_{ij}T_{\tau(j),m}$ is zero exactly
for $m$ such that there exists $\mu$ with
$\sigma(b_m)_\nu=\delta_{\mu,\nu}$ for all $\nu$.
But for such an $m$,
\[ T_{i,m}=(-1)^{\sigma(b_i)_\mu}=b_{i,\mu} \]
and also $T_{\tau(j),m}=b_{\tau(j),\mu}$.
The assertion now follows from the orthogonality of $s$.
\end{proof}

\subsection*{Acknowledgment}

Section \ref{zbrwo} of this article generalizes and extends some
results of \cite{mC} which has been achieved under the supervision
of G. Malle. The author is also thankful to G. Malle for many
other valuable comments.

\iffalse
\nocite{CGR}
\nocite{Lus1}
\nocite{mC}
\nocite{mC1}
\nocite{bBaK}
\nocite{mGgM}
\nocite{gMSp}
\nocite{MUG}
\nocite{jN}
\nocite{wdW}
\nocite{hiBphZ}
\nocite{hB}
\nocite{zAeFmM}
\fi

\bibliographystyle{amsplain}
\bibliography{references}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1066
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: cmame07.tex|>
%A.V. Knyazev, Observations on degenerate saddle point problems, Comput. Methods Appl. Mech.Engrg. (2007), doi:10.1016/j.cma.2006.10.019
\documentclass[final]{elsart5p}
\journal{Comp. Meth. Applied Mech. Engineering, accepted and published as doi:10.1016/j.cma.2006.10.019}
%\usepackage[notref,notcite]{showkeys} %to show labels. Comment this out before submission.

\usepackage{ifpdf}
\usepackage{amssymb,latexsym,lineno}
\ifpdf
\usepackage[%
  pdftitle={Observations on degenerate saddle point problems},%
  pdfauthor={Andrew Knyazev},%
  pdfsubject={Degenerate saddle point problems},%
  pdfkeywords={Wellposedness,  
mixed, 
symmetric, 
saddle point, 
Lagrange multiplier, 
Ladygenskaya--Babuska--Brezzi (LBB) condition, 
inf--sup condition, 
coercivity, 
minimum gap between subspaces},%
  pdfstartview=FitH,%
  bookmarks=true,%
  bookmarksopen=true,%
  breaklinks=true,%
  colorlinks=true,%
  linkcolor=blue,anchorcolor=blue,%
  citecolor=blue,filecolor=blue,%
  menucolor=blue,pagecolor=blue,%
  urlcolor=blue]{hyperref}
\else
\usepackage[%
  breaklinks=true,%
  colorlinks=true,%
  linkcolor=blue,anchorcolor=blue,%
  citecolor=blue,filecolor=blue,%
  menucolor=blue,pagecolor=blue,%
  urlcolor=blue]{hyperref}
\fi

\usepackage[square,comma,numbers,sort&compress]{natbib} %advanced bib package

\newtheorem{mylemma}{Lemma}[section]
\newtheorem{mytheorem}{Theorem}[section]
\newtheorem{mycorollary}{Corollary}[section]
\newtheorem{remark}{Remark}[section]
%\newenvironment{Proof}{\proof}{\endproof}

\def\proof{{{\sl Proof}. }}
\def\endproof{$\Box$}

\def\l{\lambda}
\def\R{\rm R}
\def\T{\rm T}
\def\e{\epsilon}
\def\s{\sigma}
\def\k{\kappa}
\def\d{\delta}
\def\div{\rm div \,}
\def\tr{\rm tr \,}
\def\p{\partial}
\def\g{\grad \,}
\def\ia{{\bf R} (A)}
\def\ip{{\bf R} (P)}
\def\kp{{\bf N} (P)}
\def\ib{{\bf R} (B)}
%\def\kb{{\bf N} (B)}
\def\P{{\bf P}}
\def\Pp{\P^\perp}
\def\D{{\bf D}}
\def\Dp{{\bf D}^\perp}
\def\Im{{\bf R}}
\def\Ker{{\bf N}}
\def\N{{\bf N}}
\def\ka{{\bf N} (A)}
\def\H{{\bf H}}
\def\V{{\bf V}}
\def\F{{\bf F}}
\def\o{\omega}
\def\ol{\overline}

\def\R{\rm R}

\def\cal{{}}
\def\cD{{\cal D}}
\def\cDp{{\cal D}^{\perp }}

\let\NoHyper\relax %this enables hyperref for formulas

\pagestyle{plain}
\begin{document}
\begin{frontmatter}
% Title, authors and addresses
% use the thanksref command within \title, \author or \address for footnotes;
% use the corauthref command within \author for corresponding author footnotes;
% use the ead command for the email address,
% and the form \ead[url] for the home page:
% \title{Title\thanksref{label1}}
% \thanks[label1]{}

\title{Observations on degenerate saddle point problems}
\author{Andrew V. Knyazev%\corauthref{cor1}
%\thanksref{label2}
}
%\corauth[cor1]{}
\address{Department of Mathematical Sciences\\ 
University of Colorado at Denver
and Health Sciences Center\\
P.O. Box 173364, Campus Box 170, Denver, CO 80217-3364}

\ead{andrew.knyazev[AT]cudenver.edu}
\ead[url]{http://math.cudenver.edu/ $\tilde{}$ aknyazev/}
\thanks%[label2]
{Partially supported by the
National Science Foundation award DMS-0612751.}



--- START OF DOCUMENT TAIL ---
sterdam, 1992. Elsevier.

\bibitem[Knyazev and Widlund(2003)]{kw03}
A.~V. Knyazev and O.~Widlund.
\newblock {L}avrentiev regularization + {R}itz approximation = uniform finite
  element error estimates for differential equations with rough coefficients.
\newblock \emph{Mathematics of Computation}, 72:\penalty0 17--40, 2003.
%\newblock Posted on July 13, 2001, S0025-5718-01-01378-3.

\bibitem[Ladyzhenskaya(1985)]{MR793735}
O.~A. Ladyzhenskaya.
\newblock \emph{The boundary value problems of mathematical physics}, volume~49
  of \emph{Applied Mathematical Sciences}.
\newblock Springer-Verlag, New York, 1985.
%\newblock ISBN 0-387-90989-3.
%\newblock Translated from the Russian by Jack Lohwater [Arthur J. Lohwater].

\bibitem[Xu and Zikatanov(2003)]{MR1971217}
J. Xu and L. Zikatanov.
\newblock Some observations on {B}abu\v ska and {B}rezzi theories.
\newblock \emph{Numer. Math.}, 94\penalty0 (1):\penalty0 195--202, 2003.
%\newblock ISSN 0029-599X.

\end{thebibliography}



\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0787
```latex
--- START OF DOCUMENT HEAD ---
t as the basis
% for your article. Delete % as needed.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% First comes an example EPS file -- just ignore it and
% proceed on the \documentclass line
% your LaTeX will extract the file if required
\begin{filecontents*}{example.eps}
%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: 19 19 221 221
%%CreationDate: Mon Sep 29 1997
%%Creator: programmed by hand (JK)
%%EndComments
gsave
newpath
  20 20 moveto
  20 220 lineto
  220 220 lineto
  220 20 lineto
closepath
2 setlinewidth
gsave
  .4 setgray fill
grestore
stroke
grestore
\end{filecontents*}
%
\documentclass[runningheads]{svjour2}
%
\smartqed  % flush right qed marks, e.g. at end of proof
%
\usepackage{graphicx}
%
% \usepackage{mathptmx}      % use Times fonts if available on your TeX system
%
% insert here the call for the packages your document requires
\usepackage{latexsym,amssymb,amscd,amsmath}

%%%%%%%%%%%%%%%%%DECLARATIONS%%%%%%%%%%%%%%%%%%%%%
\def \qed {\hfill \rule{1ex}{1ex}}
\def \U {{\bf u}}
\def \x {{\bf x}}
\def \y {{\bf y}}
\def \H {{\bf H}}
\def \G {{\bf g}}
\def \Ub {{\overline{ \bf u}}}
\def \V {{\bf v}}
\def \bt {{\widetilde{\hbox{\rm \bf b}}}}
\def \W {{\bf w}}
\def \N {{\mathbf{n}}}
\def \T {{\mathbf{t}}}
\def \Ut {{\tilde {\mathbf{u}}}}
\def \Deltat {{\mathbf{\widetilde{\Delta}}}}
\def \F {{\bf f }}
\def \P {{\bf P}}
\def \R {{\mathbf{R}}}
\def \div {{\hbox{div }}}
\def \cf {{\emph{cf} }}
\def \D {{\mathbf{d}}}
\def \E {{\mathbf{e}}}
\def \L {{\bf L}}
\def \Q {{\mathbf{Q}}}
\def \T {{\mathcal{T}}}
\def \I {{\mathcal{I}}}
\def \n {{\bf {n}}}
\def \A {{\mathcal{A}}}
\def \b {{\hbox{\rm  b}}}
\def \Tt {{\mathbf{t}}}
%\def \Deltat{{{\mathbf{\Delta}}}}
\def \Nabla {{\hbox{\boldmath $\nabla$ \unboldmath \!\!}}}
\def \Del {{\hbox{\boldmath $\delta$ \unboldmath \!\!}}}
\def \psig {{\hbox{\boldmath $\psi$ \unboldmath \!\!}}}
\def \alphag {{\hbox{\boldmath $\alpha$ \unboldmath \!\!}}}
\let \eps=\varepsilon


\newcommand{\Epst}[2]{\hspace{-2mm}\hbox{ $\tilde{\hspace{1mm}\hbox{\boldmath $\eps$ \unboldmath}}^
{\hspace{-1.3mm}#1}_{\hspace{-1.3mm}#2}$\hspace{-1.4mm}  }}
\newcommand{\Etat}[2]{\hspace{-2mm}\hbox{ $\tilde {\hspace{1mm}\hbox{\boldmath $\eta$ \unboldmath
}}^{\hspace{-1.3mm}#1}_{{\hspace{-1.3mm}}#2}$\hspace{-1.4mm}  }}
\newcommand{\Eta}[2]{\hbox{\boldmath $ \eta^{\hbox{\unboldmath $\scriptstyle#1$}}
_{\hbox{\unboldmath $\scriptstyle #2$}}$ \unboldmath \hspace{-3mm}
}}
\newcommand{\Delt}[2]{\hbox{\boldmath $ \delta^{\hbox{\unboldmath $\scriptstyle#1$}}
_{\hbox{\unboldmath $\scriptstyle #2$}}$ \unboldmath \hspace{-3mm}
}}
\newcommand{\Eps}[2]{\hbox{\boldmath $ \epsilon^{\hbox{\unboldmath $\scriptstyle#1$}}
_{\hbox{\unboldmath $\scriptstyle #2$}}$ \unboldmath
\hspace{-1.6mm}}}

\newtheorem{lem}{Lemma}[section]
\newtheorem{theo}{Theorem}[section]
\newtheorem{prop}{Proposition}[section]
\newtheorem{rem}{Remark}

% etc.
%
% please place your own definitions here and don't use \def but
% \newcommand{}{}
%
\journalname{Numerische Mathematik}
%
\begin{document}

\title{Convergence of a finite volume scheme for the incompressible fluids%\thanks{Grants or other notes
%about the article that should go on the front page should be
%placed here. General acknowledgments should be placed at the end of the article.}
}
%\subtitle{Do you have a subtitle?\\ If so, write it here}

%\titlerunning{Short form of title}        % if too long for running head

\author{S\'ebastien Zimmermann
}

%\authorrunning{Short form of author list} % if too long for running head

\institute{S. Zimmermann \at
              17 rue Barr\`eme, 69006 Lyon - FRANCE\\
              Tel.: (+33)0472820337\\
%              Fax: +123-45-678910\\
              \email{Sebastien.Zimmermann@ec-lyon.fr}           %  \\
%             \emph{Present address:} of F. Author  %  if needed
%           \and
%           S. Author \at
%              second address
}

\date{Received: date / Revised: date}
% The correct dates will be entered by the editor


\maketitle



--- START OF DOCUMENT TAIL ---
ompressible flow on hybrid unstructured grids. J. Comp. Phys. {\bf 162},
  411--428 (2000).



\bibitem{temam}
Temam, R.: Sur l'approximation de la solution des \'equations de
Navier-Stokes par la m\'ethode de pas fractionnaires II. Arch. Rat.
Mech. Anal. {\bf 33}  377--385 (1969).



\bibitem{zimm1}
Zimmermann, S.: Stability of a colocated finite volume for the
incompressible Navier-Stokes equations. preprint (2006).

\bibitem{zimm2}
Zimmermann, S.: Stability of a  finite volume scheme for the
incompressible fluids. preprint (2006).

%\bibitem{herb4} R. Eymard, J. C. Latch\'e and R. Herbin,
%Convergence analysis of a colocated finite volume scheme for the
%incompressible Navier-Stokes equations on general 2D or 3D meshes,
%preprint LATP (2004).


%\bibitem{zimm}
%S. Zimmermann, \'Etude et impl\'ementation de m\'ethodes de volumes
%finis pour les fluides incompressibles, PhD, Blaise Pascal
%University, 2006(in french).


\end{thebibliography}

\end{document}
% end of file template.tex
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2169
```latex
--- START OF DOCUMENT HEAD ---
 
\newcommand{\SPAN}{\mathrm{ span }}    % span 
\newcommand{\Det}{{\mathrm{Det}}}      % Det 
\newcommand{\dom}{\mathrm{ dom }}      % domain 
\newcommand{\DIV}{\mathrm{ div }}      % divergence 
\newcommand{\trace}{\mathrm{ trace }}  % trace 
\newcommand{\tr}{\mathrm{ tr }}        % trace 
\newcommand{\sign}{\mathrm{ sign }}    % sign 
\newcommand{\id}{\mathrm{ id}}         % identity 
\newcommand{\Id}{\mathrm{ Id}} 
\newcommand{\rank}{\mathrm{ rank }}    % rank 
\newcommand{\codim}{\mathrm{ codim}}   % codimension 
\newcommand{\diag}{\mathrm{ diag}}     % diagonal matrix 
\newcommand{\cl}{\mathrm{ cl}}         % closure 
\newcommand{\dist}{\mathrm{ dist}}     % distance 
\newcommand{\INT}{\mathrm{ int}}       % interior 
\newcommand{\supp}{\mathrm{ supp}}     % support 
\newcommand{\INDEX}{\mathrm{ index}}   % (Fredholm)index 
\newcommand{\ind}{\mathrm{ind}} 
\newcommand{\grad}{\mathrm{ grad }}    % gradient 
\renewcommand{\Re}{\mathrm{ Re\,}}       % real part 
\renewcommand{\Im}{\mathrm{ Im\,}}       % imaginary part 
\newcommand{\Met}{{\mathfrak{Met}}}       % space of metrics 
\newcommand{\Jreg}{\cJ_{\mathrm{reg}}}   %regular J's 
\newcommand{\Jphireg}{\cJ_{\phi,\mathrm{reg}}} 
\newcommand{\Freg}{\cF_{\mathrm{reg}}} 
\newcommand{\pr}{{\mathrm{pr}}} 
\newcommand{\ev}{\mathrm{ev}} 
\newcommand{\Aut}{\mathrm{ Aut}}          % Automorphisms 
\newcommand{\Diff}{\mathrm{ Diff}}        % Diffeomorphisms 
\newcommand{\Vect}{\mathrm{ Vect}}        % Vector fields 
\newcommand{\Hol}{\mathrm{ Hol}}          % Holomorphic 
\newcommand{\End}{\mathrm{ End}}          % Endomorphisms 
\newcommand{\G}{\mathrm{G}} 
\newcommand{\Lie}{\mathrm{Lie}} 
\newcommand{\PSL}{\mathrm{PSL}} 
% 
%\renewcommand{\phi}{{\varphi}} 
\newcommand{\eps}{{\varepsilon}} 
\newcommand{\om}{{\omega}} 
\newcommand{\Om}{{\Omega}} 
\newcommand{\TOm}{{\widetilde{\Omega}}} 
\newcommand{\ta}{{\widetilde{a}}}  
\newcommand{\tc}{{\widetilde{c}}} 
\newcommand{\tC}{{\widetilde{C}}} 
\newcommand{\tcO}{{\widetilde{\cO}}} 
\newcommand{\tgamma}{{\widetilde{\gamma}}} 
\newcommand{\tp}{{\widetilde{p}}} 
\newcommand{\tq}{{\widetilde{q}}} 
\newcommand{\tS}{{\widetilde{S}}} 
\newcommand{\tcS}{{\widetilde{\cS}}} 
\newcommand{\tcSg}{{\widetilde{\cS}_{\textrm{good}}}} 
\newcommand{\tf}{{\widetilde{f}}} 
\newcommand{\tu}{{\widetilde{u}}} 
\newcommand{\tw}{{\widetilde{w}}} 
\newcommand{\tx}{{\widetilde{x}}}  
\newcommand{\ty}{{\widetilde{y}}} 
% 
\newcommand{\Cinf}{C^{\infty}} 
\newcommand{\reg}{\mathrm{ reg}} 
\newcommand{\CZ}{\mathrm{CZ}} 
% 
\newcommand{\inner}[2]{\left\langle #1, #2\right\rangle} 
\newcommand{\winner}[2]{\left\langle #1{\wedge}#2\right\rangle} 
% 
\def\NABLA#1{{\mathop{\nabla\kern-.5ex\lower1ex\hbox{$#1$}}}} 
\def\Nabla#1{\nabla\kern-.5ex{}_{#1}} 
\def\Tabla#1{\Tilde\nabla\kern-.5ex{}_{#1}} 
% 
\def\abs#1{\mathopen|#1\mathclose|} 
\def\Abs#1{\left|#1\right|} 
\def\norm#1{\mathopen\|#1\mathclose\|} 
\def\Norm#1{\left\|#1\right\|} 
\def\dslash{/\mskip-6mu/} 
% 
\renewcommand{\Tilde}{\widetilde} 
\renewcommand{\Hat}{\widehat} 
\newcommand{\half}{\mbox{$\frac12$}} 
\newcommand{\p}{{\partial}} 
\newcommand{\dbar}{{\bar\partial}} 
 
 
\newenvironment{enum}{\begin{enumerate}\renewcommand{\labelenumi}{(\roman{enumi})}}
{\renewcommand{\labelenumi}{(\arabic{enumi}.}\end{enumerate}}  
 
 
\begin{document} 
 
\title{An exact sequence for contact- 
  and symplectic homology} 
 
\author[Bourgeois and Oancea]{Fr\'ed\'eric {\sc Bourgeois}, \
Alexandru \sc{Oancea} 
           \\ \quad \\
         {\it Universit\'e Libre de Bruxelles, B-1050 Bruxelles,
Belgium} \\
         {\it Universit\'e Louis Pasteur, F-67084 Strasbourg, France}
\\ %\quad \\
{\tt fbourgeo@ulb.ac.be,\qquad oancea@math.u-strasbg.fr}
}

\date{15 October 2008} 
 
\maketitle 
 
 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%% Abstract %%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
 


--- START OF DOCUMENT TAIL ---
5} (1992), 1303--1360. 
 
\bibitem{S} M.~Schwarz, Cohomology operations from $S^1$-cobordisms 
in Floer homology, Ph.D. dissertation, ETH Zurich, 1995. 
 
\bibitem{Se} P.~Seidel, Symplectic homology as Hochschild homology. 
  math.SG/0609037. 
 
\bibitem{V} C.~Viterbo, Functors and computations in Floer homology 
   with applications. I. 
{\it Geom. Funct. Anal.} {\bf 9} (1999), 985--1033. 
 
\bibitem{Vcotangent} ------, Functors and computations in Floer 
homology with applications. II. Preprint Universit\'e Paris-Sud 
(1998), no. 98-15.  
 
\bibitem{Y} M.-L.~Yau,  Cylindrical contact homology of subcritical 
   Stein-fillable contact manifolds, {\it Geom. Topol.} {\bf 8} (2004), 
   1243--1280. 
} 
 
 
\end{thebibliography} 
 
\end{document} 
 
 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%% Junk  %%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0095
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: PolGrowth24.tex|>

\documentclass[11pt]{amsart}
\usepackage{amssymb}

\usepackage{amsmath,amssymb}
\usepackage{epsfig, psfrag, graphics}
%\usepackage{showkeys}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{amscd}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{exercise}[theorem]{Notations}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{example}[theorem]{Example}
\addtolength{\hoffset}{-0.5cm}
\addtolength{\textwidth}{1cm}
\newtheorem{prop}[theorem]{Proposition}
\newtheorem{thm}[theorem]{Theorem}
\newtheorem{lem}[theorem]{Lemma}
\newtheorem{cor}[theorem]{Corollary}
\newtheorem{conj}[theorem]{Conjecture}
\theoremstyle{definition}
\newtheorem{Ack}[theorem]{Acknowledgement}
\newtheorem{nota}[theorem]{Notations}
\newtheorem{defn}[theorem]{Definition}
\newtheorem{rem}[theorem]{Remark}
\newtheorem{exam}[theorem]{Example}
\newtheorem{prob}[theorem]{Problem}
\newtheorem{ques}[theorem]{Question}
\newtheorem{ob}[theorem]{Observation}
\newtheorem{clm}[theorem]{claim}
\newcommand{\pf}{ {\it Proof: } }
\newcommand{\edpf} { {$\square$ \par } }
\newcommand\E{\mathbb{E}}
\newcommand\Z{\mathbb{Z}}
\newcommand\R{\mathbb{R}}
\newcommand\T{\mathbb{T}}
\newcommand\C{\mathbb{C}}
\newcommand\N{\mathbb{N}}
\newcommand\G{\mathbf{G}}
\newcommand\A{\mathbb{A}}
\newcommand\K{\mathbb{K}}
\newcommand\g{\frak{g}}
\newcommand\vu{\frak{v}}
\newcommand\n{\frak{n}}
\newcommand{\eps} {\varepsilon}


\begin{document} \title[Asymptotic shape of balls in groups with polynomial growth]{Geometry of locally compact groups of polynomial
growth and shape of large balls.}
\author{Emmanuel Breuillard}
\email{emmanuel.breuillard@math.u-psud.fr}
\address{Universit\'e Paris-Sud 11, Laboratoire de Math\'ematiques, 91405 Orsay, France}
\date{April 2012}




--- START OF DOCUMENT TAIL ---
-624
(1989).

\bibitem{Sto}  M. Stoll, \textit{On the asymptotic of the growth of }$2$%
\textit{-step nilpotent groups}, J. London Math. Soc (2) \textbf{58} (1998),
no 1, 38--48.

\bibitem{Sto2}  M. Stoll, \textit{Rational and transcendental growth series
for higher Heisenberg groups}, Invent. math. \textbf{126}, 85-109 (1996).

\bibitem{Tem}  A. Tempelman, \textit{Ergodic theorems for group actions},
Mathematics and its applications, 78, Kluwer Academic publishers (1992).

\bibitem{Tes}  R. Tessera, \textit{Volumes of spheres in doubling measures
metric spaces and groups of polynomial growth},
\newblock { Bull. Soc. Math. France}, 135(1):47--64, 2007.

\bibitem{Wan}  H.C. Wang, \textit{Discrete subgroups of solvable Lie groups}%
, Annals of Math, (1956), \textbf{64}, 1-19.

\bibitem{wolf} J. Wolf,\textit{\ Growth of finitely generated solvable groups
and curvature of Riemanniann manifolds}, J. Differential Geometry, \textbf{2}
(1968) p. 421--446.
\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0665
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: MXZ-Hartree2.tex|>
\documentclass[11pt]{article}
\usepackage{amscd}
\usepackage{amsmath}
\usepackage{latexsym}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{graphicx}

 \oddsidemargin .5cm \evensidemargin .5cm \marginparwidth 40pt
 \marginparsep 10pt \topmargin 0.5cm
 \headsep1pt
 \headheight 0pt
 \textheight 8.5in
 \textwidth 5.8in
 \sloppy

 \setlength{\parskip}{8pt}

 \renewcommand{\theequation}{\arabic{section}.\arabic{equation}}

 \newtheorem{proposition}{Proposition}[section]
 \newtheorem{definition}{Definition}[section]
 \newtheorem{lemma}{Lemma}[section]
 \newtheorem{theorem}{Theorem}[section]
 \newtheorem{corollary}{Corollary}[section]
 \newtheorem{remark}{Remark}[section]

\makeatletter
\newcommand{\Extend}[5]{\ext@arrow0099{\arrowfill@#1#2#3}{#4}{#5}}
\makeatother



\begin{document}

 \title{ Global well-posedness and scattering for the energy-critical, defocusing Hartree equation for radial data}
 \author{{Changxing Miao,\ \ Guixiang Xu,\ \ and \ Lifeng Zhao }\\
         {\small Institute of Applied Physics and Computational Mathematics}\\
         {\small P. O. Box 8009,\ Beijing,\ China,\ 100088}\\
         {\small (miao\_changxing@iapcm.ac.cn, \ xu\_guixiang@iapcm.ac.cn, zhao\_lifeng@iapcm.ac.cn ) }\\
         \date{}
        }
\maketitle




--- START OF DOCUMENT TAIL ---
 Ozawa, Nonlinear scattering with
nonlocal interactions, Comm. Math. Phys. 146(1992), 259-275.

\bibitem{RyV05}E. Ryckman and M. Visan, Global well-posedness and
scattering for the defocusing energy-critical nonlinear
Schr\"{o}dinger equation in $\mathbb{R}^{1+4}$. Amer. J. Math.,
129(2007), 1-60.

\bibitem{Stri77}R. S. Strichartz, Restriction of Fourier tranform to
quadratic surfaces and decay of solutions of wave equations. Duke
Math. J., 44(1977), 705-714.

\bibitem{Tao05}T. Tao, Global well-posedness and scattering for the
higher-dimensional energy-critical nonlinear Schr\"{o}dinger
equation for radial data. New York Journal of Mathematics, 11(2005),
57-80.

\bibitem{Vi05}M. Visan, The defocusing energy-critical nonlinear
Schr\"{o}dinger equation in higher dimensions. to appear Duke Math.
J..

\bibitem{Wei}M. I. Weinstein, Nonlinear Schr\"{o}dinger equations and
sharp interpolation estimates. Comm. Math. Phys., 87(1983), 567-576.


\end{thebibliography}
\end{center}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1778
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: aop399.tex|>
%BeginFileInfo
%%Publisher=ARXIV
%%Project=AOP
%%Manuscript=AOP399
%%Stage=
%%TID=Romualda
%%Format=latex
%%Distribution=arXiv
%%Destination=PDF
%%DVI.Maker=arXiv_tex_dvi
%%PDF.Maker=arXiv_tex_pdf
%EndFileInfo
%
% Institute of Mathematical Statistics (IMI)
% Journal "The Annals of Probabability"

%secthm,seceqn,secfloat,nameyear,number,noautosecdot
\documentclass[aop,MSNbibl,secthm,nochecklpage,dvips]{arximspdf}

% settings
%PROOF

% article settings
\doi{10.1214/08-AOP399}
\volume{37}
\issue{1}
\pubyear{2009}
\firstpage{143}
\lastpage{188}

\makeatletter
\newproclaim{asm}{Assumption}
\newproclaim{note}{Note}
\newtheorem{lem}[thm]{Lemma}
\newtheorem{cor}[thm]{Corollary}

\def\eqref#1{(\ref{#1})}
\makeatother

\begin{document}
%
\begin{frontmatter}

\title{Quenched limits for transient, zero speed
one-dimensional random walk in random~environment}
\runtitle{Nonexistence of quenched stable limits for RWRE}

\begin{aug}
\author[A]{\fnms{Jonathon} \snm{Peterson}\thanksref{t1,t2}\corref{}\ead[label=e1]{peterson@math.wisc.edu}} \and
\author[B]{\fnms{Ofer} \snm{Zeitouni}\thanksref{t2}\ead[label=e2]{zeitouni@math.umn.edu}}
\runauthor{J. Peterson and O. Zeitouni}
\thankstext{t1}{Supported in part by a Doctoral Dissertation
Fellowship from the University of Minnesota.}
\thankstext{t2}{Supported in part by NSF Grant DMS-05-03775.}
\affiliation{University of Wisconsin and University of Minnesota}
\address[A]{Department of Mathematics\\
University of Wisconsin\\
480 Lincoln Drive\\
Madison, Wisconsin 53705\\
USA\\
\printead{e1}} %adresu isvedimo komanda gale!
\address[B]{School of Mathematics\\
University of Minnesota\\
206 Church St. SE\\
Minneapolis, Minnesota 55455\\
and\\
Faculty of Mathematics\\
Weizmann Institute of Science\\
Rehovot 76100\\
Israel\\
\printead{e2}}
\end{aug}

% HISTORY:
\received{\smonth{6} \syear{2006}}
\revised{\smonth{2} \syear{2008}}

% ABSTRACT
%


--- START OF DOCUMENT TAIL ---
le{Ballistic random walk in a random environment with a forbidden
  direction}.
\bjournal{ALEA Lat. Am. J. Probab. Math. Stat.}
\bvolume{1}
\bpages{111--147 (electronic)}.
\bmrnumber{MR2235176}
\end{barticle}
\endbibitem

%b13 ###
\bibitem{sRWRE}
\begin{barticle}[vtex]
\bauthor{\bsnm{Solomon},~\bfnm{Fred}\binits{F.}}
(\byear{1975}).
\btitle{Random walks in a random environment}.
\bjournal{Ann. Probab.}
\bvolume{3}
\bpages{1--31}.
\bmrnumber{MR0362503}
\end{barticle}
\endbibitem\vadjust{\goodbreak}

%b14 ###
\bibitem{zRWRE}
\begin{bincollection}[msn]
\bauthor{\bsnm{Zeitouni},~\bfnm{Ofer}\binits{O.}}
(\byear{2004}).
\btitle{Random walks in random environment}.
In \bbooktitle{Lectures on Probability Theory and Statistics}.
\bseries{Lecture Notes in Math.}
\bvolume{1837}
\bpages{189--312}.
\bpublisher{Springer}, \baddress{Berlin}.
\bmrnumber{MR2071631}
\end{bincollection}
\endbibitem

\end{thebibliography}

\printaddresses
\end{document}

TEKSTAS
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0805
```latex
--- START OF DOCUMENT HEAD ---
perref can be obtained at:
%
% http://www.ctan.org/tex-archive/macros/latex/contrib/supported/hyperref/
%
% Also, be aware that cite.sty (as of version 3.9, 11/2001) and hyperref.sty
% (as of version 6.72t, 2002/07/25) do not work optimally together.
% To mediate the differences between these two packages, IEEEtran.cls, as
% of v1.6b, predefines a command that fools hyperref into thinking that
% the natbib package is being used - causing it not to modify the existing
% citation commands, and allowing cite.sty to operate as normal. However,
% as a result, citation numbers will not be hyperlinked. Another side effect
% of this approach is that the natbib.sty package will not properly load
% under IEEEtran.cls. However, current versions of natbib are not capable
% of compressing and sorting citation numbers in IEEE's style - so this
% should not be an issue. If, for some strange reason, the user wants to
% load natbib.sty under IEEEtran.cls, the following code must be placed
% before natbib.sty can be loaded:
%
% \makeatletter
% \let\NAT@parse\undefined
% \makeatother
%
% Hyperref should be loaded differently depending on whether pdflatex
% or traditional latex is being used:
%
%\ifx\pdfoutput\undefined
%\usepackage[hypertex]{hyperref}
%\else
%\usepackage[pdftex,hypertexnames=false]{hyperref}
%\fi
%
% Pdflatex produces superior hyperref results and is the recommended
% compiler for such use.

% *** Do not adjust lengths that control margins, column widths, etc. ***
% *** Do not use packages that alter fonts (such as pslatex).         ***
% There should be no need to do such things with IEEEtran.cls V1.6 and later.

% correct bad hyphenation here
\hyphenation{op-tical net-works semi-conduc-tor IEEEtran}
\def\thefootnote{}

\begin{document}

% paper title
\title{Opportunistic Relay Selection with Limited Feedback}

% author names and affiliations
% use a multiple column layout for up to three different
% affiliations
\author{Caleb K. Lo, Robert W. Heath, Jr. and Sriram Vishwanath \\Wireless Networking and Communications Group \\ Department of Electrical and Computer Engineering \\ The University of Texas at Austin, Austin, Texas 78712-0240 \\ Email: [clo, rheath, sriram]@ece.utexas.edu
\thanks{Caleb K. Lo was supported by a Microelectronics and Computer Development (MCD) Fellowship and a Thrust 2000 Endowed Graduate Fellowship through The University of Texas at Austin.  Robert Heath was supported in part by the National Science Foundation under grant CNS-626797, the Office of Naval Research under grant number N00014-05-1-0169, and the DARPA IT-MANET program, Grant W911NF-07-1-0028.   Sriram Vishwanath was supported by the National Science Foundation under grants CCF-055274, CCF-0448181, CNS-0615061 and CNS-0626903.}}
\date{}

% avoiding spaces at the end of the author lines is not a problem with
% conference papers because we don't use \thanks or \IEEEmembership

% for over three affiliations, or if they all won't fit within the width
% of the page, use this alternative format:
%
%\author{\authorblockN{Michael Shell\authorrefmark{1},
%Homer Simpson\authorrefmark{2},
%James Kirk\authorrefmark{3},
%Montgomery Scott\authorrefmark{3} and
%Eldon Tyrell\authorrefmark{4}}
%\authorblockA{\authorrefmark{1}School of Electrical and Computer Engineering\\
%Georgia Institute of Technology,
%Atlanta, Georgia 30332--0250\\ Email: mshell@ece.gatech.edu}
%\authorblockA{\authorrefmark{2}Twentieth Century Fox, Springfield, USA\\
%Email: homer@thesimpsons.com}
%\authorblockA{\authorrefmark{3}Starfleet Academy, San Francisco, California 96678-2391\\
%Telephone: (800) 555--1212, Fax: (888) 555--1212}
%\authorblockA{\authorrefmark{4}Tyrell Inc., 123 Replicant Street, Los Angeles, California 90210--4321}}

% use only for invited papers
%\specialpapernotice{(Invited Paper)}

\renewcommand{\baselinestretch}{2}

\twocolumn
\renewcommand{\baselinestretch}{1}
%\renewcommand{\baselinestretch}{2}

\setcounter{page}{1}
\newpage

% make the title area
\maketitle



--- START OF DOCUMENT TAIL ---
~Qin and R.A.~Berry.
\newblock Distributed approaches for exploiting multiuser diversity in wireless networks.
\newblock {\em IEEE Trans. Inform. Theory}, 52(2):392--413, February 2006.

\bibitem{VisETAL:OppoBeamDumbAnte:Jun:02}
P.~Viswanath, D.N.C.~Tse and R.~Laroia.
\newblock Opportunistic beamforming using dumb antennas.
\newblock {\em IEEE Trans. Inform. Theory}, 48(6):1277--1294, June 2002.

\bibitem{LinCos:ErroContCodi:04}
S.~Lin and D.J.~Costello, Jr.
\newblock {\em Error Control Coding}.
\newblock Pearson Prentice Hall, Upper Saddle River, NJ, 2004.

\bibitem{LoETAL:HybrARQMultNetw:Apr:07}
C.K.~Lo, R.W.~Heath, Jr. and S.~Vishwanath.
\newblock Hybrid-ARQ in multihop networks with opportunistic relay selection.
\newblock To appear in {\em Proc. of the IEEE Intl. Conf. on Acoustics, Speech and Sig. Proc.}, Honolulu, HI, April 2007.

\bibitem{WireMANWorkGrp}
Wireless~MAN~Working~Group.
\newblock http://www.wirelessman.org/.

\end{thebibliography}

% that's all folks
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1308
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: revised_ant_combining_twireless.tex|>
% Modified from bare_conf.tex on 06-12-04
%% V1.2
%% 2002/11/18
%% by Michael Shell
%% mshell@ece.gatech.edu

%\documentclass[11pt, draft, peerreview]{IEEEtran}
\documentclass[11pt, onecolumn]{IEEEtran}
%\documentclass[10pt, conference]{IEEEtran}

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{verbatim}
\usepackage{epsfig}

\newtheorem{proposition}{Proposition}
\newtheorem{lemma}{Lemma}
\newtheorem{conjecture}{Conjecture}
\newtheorem{theorem}{Theorem}
\newcommand{\am}{\textsf{\footnotesize \small am}}
\newcommand{\cN}{{\cal N}}
\newcommand{\bh}{{\bf h}}
\newcommand{\bI}{{\bf I}}
\newcommand{\bw}{{\bf w}}
\newcommand{\be}{{\bf e}}
\newcommand{\bH}{{\bf H}}
\newcommand{\bG}{{\bf G}}
\newcommand{\bX}{{\bf X}}
\newcommand{\bQ}{{\bf Q}}
\newcommand{\bx}{{\bf x}}
\newcommand{\bn}{{\bf n}}
\newcommand{\bq}{{\bf q}}
\newcommand{\bv}{{\bf v}}
\newcommand{\by}{{\bf y}}
\newcommand{\bheff}{{\bf h}^{\textrm{eff}}}
\newcommand{\yeff}{y^{\textrm{eff}}}
\newcommand{\br}{{\bf r}}
\renewcommand{\th}{{\tilde \bh}}
\newcommand{\tH}{{\tilde \bH}}
\newcommand{\HH}{\mbox{\scriptsize{H}}}
\newcommand{\Prob}{\mbox{\rm Prob}\, }
\newcommand{\rank}{\mbox{\rm rank}\, }
\def\Box {\vrule height5pt width5pt depth0pt}
%\def\beginproof{\par\noindent {\bf Proof.}\ \ }
%\def\endproof{\hskip .5cm \Box \vskip .5cm}
\def\tx {\tilde x}
\def\bj {{\bar j}}
\def\blambda {\bar \lambda}
\def\C{\rm I\!\!\!C}
\def\R{\rm I\!R}
\def\Z{\rm Z\!\!Z}
\newcommand{\diag}{{\rm Diag}}
\def\argmax{\mathop{\rm arg\,max}}
\newcommand{\tr}{ {\rm Tr}}
\newcommand{\Tr}{ {\rm Tr}}
%\def\defeq{\buildrel \rm def \over =}
%\def\define{\buildrel \rm def \over =}
\def\defeq{:=}
\def\define{:=}

\psfull

\begin{document}

\title{Antenna Combining for the MIMO Downlink Channel}
\author{\authorblockN{Nihar Jindal} \\
\authorblockA{University of Minnesota, Department of ECE\\
Minneapolis, MN 55455, USA \\
Email: nihar@umn.edu}}
% make the title area
\maketitle


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


--- START OF DOCUMENT TAIL ---
smith, ``Finite-rate feedback {MIMO}
broadcast
  channels with a large number of users,'' 2007, to appear in \textit{IEEE J.
  Sel. Areas on Commun.}

\bibitem{Paulraj_Gore_Nabar}
A.~Paulraj, D.~Gore, and R.~Nabar, \emph{Introduction to Space-Time
Wireless
  Communications}.\hskip 1em plus 0.5em minus 0.4em\relax Cambridge University
  Press, 2003.

\bibitem{TrivHuangBoc07_Asilomar}
M.~Trivellato, H.~Huang, and F.~Boccardi, ``Antenna combining and
codebook
  design for {MIMO} broadcast channel with limited feedback,'' in \emph{Proc.
  Asilomar Conf. on Sig. and Systems}, Nov. 2007.

\bibitem{RavindranJindal07_ICASSP}
N.~Ravindran and N.~Jindal, ``{MIMO} broadcast channels with block
  diagonalization and finite rate feedback,'' in \emph{Proc. ICASSP}, April
  2007.

\bibitem{BoccardiHuang07_ICASSP}
F.~Boccardi and H.~Huang, ``A near-optimum technique using linear
precoding for
  the {MIMO} broadcast channel,'' in \emph{Proc. ICASSP}, April 2007.

\end{thebibliography}


\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0537
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: linearisation.tex|>
\documentclass[english]{article}

\usepackage[english]{babel}
\usepackage{latexsym}

\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{verbatim}
\usepackage{psfrag}
\usepackage{graphicx}

\textwidth=125 mm
 \textheight=195 mm
\theoremstyle{theorem}
\newtheorem{lemm}{Lemma}[section]
\newtheorem{prop}[lemm]{Proposition}
\newtheorem{coro}[lemm]{Corollary}
\newtheorem{theo}{Theorem}
\theoremstyle{remark}
\newtheorem{defi}[lemm]{Definition}
\newtheorem{nota}[lemm]{Notation}
\newtheorem{conv}[lemm]{Convention}
\newtheorem{exem}[lemm]{Example}
\newtheorem{rema}[lemm]{Remark}

\usepackage{color}

\definecolor{grey}{rgb}{0.6,0.6,0.6}
\newcommand{\proofend}{\hfill $\square$}
\newcommand{\Z}[1]{\mathbb{Z}/#1\mathbb{Z}}


\newcommand{\Crc}[2]{\mathrm{Bir}(#1,#2)}\newcommand{\defn}[1]{{\em #1}}
\newcommand{\CrP}{\mathrm{Bir}(\Pn)}
\newcommand{\Cr}[1]{\mathrm{Bir}(#1)}
\newcommand{\PGLn}[1]{\PGL(#1,\K)}
\newcommand{\GLZ}[1]{\GL(#1,\mathbb{Z})}
\newcommand{\Ker}{\mathrm{Ker}}
\newcommand{\pr}{pr}
\newcommand{\Diag}[3]{[#1:#2:#3]}
\newcommand{\DiaG}[4]{[#1:#2:#3:#4]}
\newcommand{\PGL}{\mathrm{PGL}}
\newcommand{\GL}{\mathrm{GL}}
\newcommand{\im}{{\bf i}}
\newcommand{\ipi}{{\bf i}\pi}
\newcommand{\K}{\mathbb{C}}
\newcommand{\Bir}{\mathrm{Bir}}
\newcommand{\Fix}{\mathrm{Fix}}
\newcommand{\vrif}[1]{\ensuremath{\mathbf{#1}}}
\newcommand{\Aut}{\mathrm{Aut}}
\newcommand{\Sym}{\mathrm{Sym}}
\newcommand{\Alt}{\mathrm{Alt}}
\newcommand{\rkPic}[1]{\mathrm{rk\ Pic}(#1)}
\newcommand{\Pn}{\mathbb{P}^2}
\newcommand{\Pic}[1]{\mathrm{Pic}(#1)}
\newcommand{\drawat}[3]{\makebox[0pt][l]{\raisebox{#2}{\hspace*{#1}#3}}}

\newcommand{\h}[1]{\hspace{-#1mm}}
\newcommand{\num}[1]{\ensuremath{\begin{array}{|c|}\hline {\mathbf{#1}} \\ \hline\end{array}}}
\newcommand{\nump}[1]{\ensuremath{\begin{array}{|c|}\hline {\mathrm{#1}} \\ \hline\end{array}}}
\newcommand{\Cs}[1]{\mathit{Cs}_{#1}}

\begin{document}
\title{Linearisation of finite Abelian subgroups of the Cremona group of the plane}
\author{J\'er\'emy Blanc}
\maketitle



--- START OF DOCUMENT TAIL ---
bib:KoS}
J. Koll\'ar, E. Szab\'o, {\it Fixed points of group actions and rational maps}. Canadian J. Math. {\bf 52} (2000), 1054-1056.
\bibitem[Kra]{bib:Kra}
H. Kraft, {\it Challenging problems on affine $n$-space.}
S\'eminaire Bourbaki, Vol. 1994/95.
Ast\'erisque No. {\bf 237} (1996), Exp. No. 802, 5, 295--317. 
\bibitem[Man]{bib:Man}
Yu. Manin, {\it Rational surfaces over perfect fields, II.} Math. USSR - Sbornik {\bf 1} (1967), 141-168.
\bibitem[Mu-Um]{bib:MuUm}
S. Mukai, H. Umemura, {\it Minimal rational threefolds.} Algebraic geometry, Tokyo/Kyoto, (1982), 490--518, 
Lecture Notes in Math., 1016, Springer, Berlin, 1983. 
\bibitem[Um]{bib:Um}
H. Umemura, {\it On the maximal connected algebraic subgroups of the Cremona group. I.} Nagoya Math. J. {\bf 88} (1982), 213--246. 
\bibitem[Wim]{bib:Wim}
A. Wiman, {\it Zur Theorie der endlichen Gruppen von birationalen Transformationen in der Ebene.} Math. Ann., vol. {\bf 48}, (1896), 497-498, 195-241.
\end{thebibliography}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0469
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: linearrangx.tex|>
\documentclass[12pt]{amsart}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{bm}
\usepackage{latexsym}
\usepackage{amsmath}
\usepackage{eufrak}
\usepackage{mathrsfs}
\usepackage{amscd}
\usepackage[all]{xy}
\usepackage[usenames]{color}
\usepackage[dvips]{graphicx}

\theoremstyle{plain}
\newtheorem{teo}{Theorem}[section]
\newtheorem{cor}[teo]{Corollary}
\newtheorem{lem}[teo]{Lemma}
\newtheorem{question}[teo]{Question}
\newtheorem{prop}[teo]{Proposition}
\theoremstyle{definition}
\newtheorem{defi}{Definition}[section]
\newtheorem{obs}{Remark}[section]
\newtheorem{example}{Example}[section]
\newtheorem{nota}{Notation}[section]

\DeclareMathOperator{\fix}{{Fix}} \DeclareMathOperator{\Ind}{{Ind}} \DeclareMathOperator{\Ima}{{Im}} \DeclareMathOperator{\aut}{{Aut}}
\DeclareMathOperator{\Core}{{Core}} \DeclareMathOperator{\Gal}{{Gal}} \DeclareMathOperator{\order}{{order}} \DeclareMathOperator{\Wier}{{Wier}}
\DeclareMathOperator{\Irr}{{Irr}} \DeclareMathOperator{\Stab}{Stab} \DeclareMathOperator{\spec}{Spec} \DeclareMathOperator{\sing}{sing}
\DeclareMathOperator{\effective}{effective}

\newcommand{\RR}{\mathbb R}

\def\G{{\mathcal{G}}}
\def\O{{\mathcal{O}}}
\def\I{{\mathcal{I}}}
\def\J{{\mathcal{J}}}
\def\L{{\mathcal{L}}}
\def\F{{\mathbb{F}}}
\def\K{{\mathbb{K}}}
\def\R{{\mathbb{R}}}
\def\M{{\mathscr{M}}}
\def\A{{\mathcal{A}}}
\def\X{{\mathcal{X}}}
\def\AA{{\mathscr{A}}}
\def\B{{\mathscr{B}}}
\def\CC{{\mathscr{C}}}
\def\LL{{\mathscr{L}}}
\def\e{{\mathfrak e}}
\def\E{{\mathcal E}}
\def\N{{\mathbb N}}
\def\Z{{\mathbb Z}}
\def\Q{{\mathbb Q}}
\def\H{{\mathscr H}}
\def\PP{{\mathscr P}}
\def\P{{\mathbb P}}
\def\C{{\mathbb C}}
\def\Af{{\mathbb A}}

\def\Hom{\textrm{Hom}}
\def\spec{\textrm{Spec}}
\def\Pic{\textrm{Pic}}
\def\div{\textrm{div}}
\def\k{\textrm{k}}
\def\ker{\textrm{ker}}
\def\coker{\textrm{coker}}


\pagestyle{plain}

%\setlength{\textwidth}{16.4cm} \setlength{\textheight}{23.4cm} \topmargin -1.0cm \oddsidemargin -0.0cm \evensidemargin -0.0cm
%\setlength{\textwidth}{16.4cm} \setlength{\textheight}{23.3cm} \topmargin 0.2cm \oddsidemargin -0.2cm \evensidemargin -0.2cm

\setlength{\textwidth}{16.4cm} \setlength{\textheight}{23.4cm} \topmargin -0.2cm \oddsidemargin -0.2cm \evensidemargin -0.2cm

\renewcommand{\baselinestretch}{1.15}


\begin{document}
\bibliographystyle{amsplain}

\title[Construcci\'on]{On line arrangements with applications to $3$-nets}
\author{Giancarlo Urz\'ua}


\email{urzua@math.umass.edu} \maketitle



--- START OF DOCUMENT TAIL ---
etely reducible hypersurfaces in a pencil},
    arXiv:math/0701312v2.

\bibitem{Stipins1}
    J. Stipins.
    \emph{Old and new examples of $k$-nets in $\P^2$},
    arXiv:math.AG/0701046.

\bibitem{Stipins2}
    J. Stipins.
    \emph{On finite $k$-nets in the complex projective plane},
    Ph.D. Thesis, University of Michigan (2007).

\bibitem{Urzua4}
    G. Urz\'ua.
    \emph{Arrangements of curves and algebraic surfaces},
    Ph.D. Thesis, University of Michigan (2008).

\bibitem{YuzNets04}
    S. Yuzvinsky.
    \emph{Realization of finite abelian groups by nets in $\P^2$},
    Compos. Math. 140, no. 6, (2004) 1614--1624.

\bibitem{Yuz08}
    S. Yuzvinsky.
    \emph{A new bound on the number of special fibers in a pencil of curves},
    arXiv:0801.1521v2.

\end{thebibliography}

\vspace{0.1 cm} {\small Department of Mathematics and Statistics, University of Massachusetts at Amherst, USA.}
%{\tiny MSC classes: primary 52C30 - 14J10 - 05B15, secondary 05B30-14H50-52C35}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1926
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: dbn2nd_Laguerre.tex|>
%
\documentclass[10pt]{amsart}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{amsthm}
\usepackage{amsxtra}
\usepackage{portland}
\usepackage{rotating}
%\usepackage{showkeys}
\usepackage{nicefrac}
\usepackage{float}
%\usepackage[all,web,arc,poly,dvips]{xy}
%\usepackage{epic,eepic}
\usepackage{epsfig}
\usepackage[dvips]{color}
\usepackage{array}
\usepackage{pifont}
\usepackage{multirow}
\usepackage{curves}

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{corollary}{Corollary}[section]
\newtheorem{lemma}{Lemma}[section]
\newtheorem{proposition}{Proposition}[section]
%{\theorembodyfont{\rmfamily} \newtheorem{remark}{Remark}[section]}

\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
\newtheorem{example}{Example}[section]
\newtheorem{conjecture}{Conjecture}[section]

\theoremstyle{remark}
\newtheorem{remark}{Remark}[section]
\newtheorem{note}{Note}[section]
\newtheorem{case}{Case}[section]
%\newtheorem{preremark}{Remark}[section]
%  \newenvironment{remark}%
%    {\begin{preremark}\upshape}{\end{preremark}}

\setlength{\parindent}{1.5em}
\renewcommand{\baselinestretch}{1.2}
\renewcommand{\theequation}{\thesection.\arabic{equation}}
\renewcommand{\thefigure}{\arabic{figure}}

\newcommand{\CC}{\mathbb C}
\newcommand{\RR}{\mathbb R}
\newcommand{\ZZ}{\mathbb Z}
\newcommand{\NN}{\mathbb N}
\newcommand{\+}{\!+\!}
\newcommand{\m}{\!-\!}
\newcommand{\ScSt}{\scriptstyle}
\newcommand{\PV}{${\rm P}_{\rm V}\:$}
\newcommand{\PVI}{${\rm P}_{\rm VI}\:$}
\newcommand{\pII}{${\rm P}_{\rm II}\:$}
\newcommand{\PIV}{${\rm P}_{\rm IV}\:$}
\newcommand{\PIII}{${\rm P}_{\rm III}\:$}
\newcommand{\PIIIprime}{${\rm P}_{\rm III^{\prime}}\:$}
\newcommand{\IIId}{${\rm III^{\prime}}\;$}
\newcommand{\half}{
        {\lower0.00ex\hbox{\raise.6ex\hbox{\the\scriptfont0 1}
                           \kern-.5em\slash\kern-.1em\lower.45ex
                                     \hbox{\the\scriptfont0 2}}}}
\newcommand{\quarter}{
        {\lower0.00ex\hbox{\raise.6ex\hbox{\the\scriptfont0 1}
                           \kern-.5em\slash\kern-.1em\lower.45ex
                                     \hbox{\the\scriptfont0 4}}}}
\newcommand{\tquarter}{
        {\lower0.00ex\hbox{\raise.6ex\hbox{\the\scriptfont0 3}
                           \kern-.5em\slash\kern-.1em\lower.45ex
                                     \hbox{\the\scriptfont0 4}}}}
\newcommand{\eighth}{
        {\lower0.00ex\hbox{\raise.6ex\hbox{\the\scriptfont0 1}
                           \kern-.5em\slash\kern-.1em\lower.45ex
                                     \hbox{\the\scriptfont0 8}}}}
\newcommand{\othird}{
        {\lower0.00ex\hbox{\raise.6ex\hbox{\the\scriptfont0 1}
                           \kern-.5em\slash\kern-.1em\lower.45ex
                                     \hbox{\the\scriptfont0 3}}}}


\begin{document}

\title[Distribution of the first Eigenvalue Spacing ...]
{The Distribution of the first Eigenvalue Spacing at the Hard Edge of the Laguerre Unitary Ensemble}

\author{Peter J. Forrester and Nicholas S. Witte}
\address{Department of Mathematics and Statistics,
University of Melbourne,Victoria 3010, Australia}
\email{\tt p.forrester@ms.unimelb.edu.au}\email{\tt n.witte@ms.unimelb.edu.au}



--- START OF DOCUMENT TAIL ---
a(z) $ for various values of the parameter $ a $.}
\end{table}

\vskip1.0cm

\begin{table}[h]
\renewcommand{\arraystretch}{1.2}
\begin{sideways}
\begin{tabular}{|c|c|c|c|c|}
\hline
 \multicolumn{5}{|c|}{Statistical Data} \\
\hline
        & mean & standard deviation & skewness & kurtosis excess \\
 $ a= $ & $ m_1 $ & $ \sigma $ & $ \gamma_1 $ & $ \gamma_2 $ \\
\hline
 $ -\frac{1}{2} $ & $ 0.948882728945527548 $ & $ 0.38067989233932349 $ & $ 0.3755455785328836 $ & $ -0.060161637308986 $ \\
 $  \frac{1}{2} $ & $ 0.9818310311076319 $   & $ 0.405745365891523 $   & $ 0.42308992831476 $   & $ -0.0168189358644 $ \\
\hline
\end{tabular}
\end{sideways}
\vskip0.5cm
\caption{Low order statistics of the distribution $ A^{\pm}(z) $ for the special cases of the parameter 
$ a=\pm\frac{1}{2} $.}
\end{table}


\section*{Acknowledgements}
This work was supported by the Australian Research Council.

\vfill\eject

\bibliographystyle{plain}
\bibliography{moment,random_matrices,nonlinear}


\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1361
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: liu_xin_qi.tex|>
\documentclass[11pt]{article}
%\usepackage{latexsym}
\usepackage{epsfig}
\usepackage{multirow}
%\usepackage{amsmath}
%\usepackage{showkeys}
%\input amssym.def
%\input amssym.tex
%\input epsf
\newcommand{\be}{\begin{equation}}
\newcommand{\ee}{\end{equation}}
%\newcommand{\br}{\begin{eqnarray}}
%\newcommand{\er}{\end{eqnarray}}
\newcommand{\TM}{T_{\mathrm{M}}}
\newcommand{\fm}{f_{\mathrm{m}}}
\newcommand{\zetam}{\zeta_{\mathrm{m}}}
\newcommand{\aM}{a_{\mathrm{M}}}
\newcommand{\Zm}{Z_{\mathrm{m}}}
\newcommand{\pe}{p_{\mathrm{e}}}
\newcommand{\ps}{p_{\mathrm{s}}}
\newcommand{\mm}{m_{\mathrm{m}}}
\newcommand{\cm}{c_{\mathrm{m}}}
\newcommand{\km}{k_{\mathrm{m}}}
\newcommand{\Mp}{M_{\mathrm{p}}}
\newcommand{\Cp}{C_{\mathrm{p}}}
\newcommand{\Kp}{K_{\mathrm{p}}}
\newcommand{\Ca}{C_{\mathrm{a}}}
\newcommand{\Ka}{K_{\mathrm{a}}}
\newcommand{\Lp}{L_{\mathrm{p}}}
\newcommand{\La}{L_{\mathrm{a}}^{n}}
\newcommand{\Mf}{M_{\mathrm{f}}}
\newcommand{\Mfs}{M_{\mathrm{f}}^{\mathrm{s}}}
\newcommand{\Ds}{D_{\mathrm{s}}}
\def\R{{\Bbb R}}
\def\lap{\triangle}
\renewcommand{\theequation}{\arabic{section}.\arabic{equation}}

\begin{document}

%\begin{frontmatter}
%\documentstyle[11pt,phonetic,apalike,psfig]{eearticle}
%\input{eedefs}
%\spacingset{1.4}
%\begin{document}
\newcommand{\ra}{\rightarrow}
\newcommand{\wh}{\widehat}
\newcommand{\nit}{\noindent}
\newcommand{\no}{\nonumber}
%\newcommand{\be}{\begin{equation}}
%\newcommand{\ee}{\end{equation}}
\newcommand{\ba}{\begin{eqnarray}}
\newcommand{\ea}{\end{eqnarray}}
\newcommand{\pa}{\mbox{$\partial$}}
\newcommand{\Gam}{\mbox{$\Gamma$}}
\newcommand{\dta}{\mbox{$\delta$}}
\newcommand{\fee}{\mbox{$\varphi$}}
\newcommand{\al}{\mbox{$\alpha$}}
\newcommand{\lam}{\mbox{$\lambda$}}
\newcommand{\eps}{\mbox{$\epsilon$}}
\newcommand{\gam}{\mbox{$\gamma$}}
\newcommand{\omg}{\mbox{$\omega$}}
\newtheorem{theo}{Theorem}[section]
\newtheorem{defin}{Definition}[section]
\newtheorem{prop}{Proposition}[section]
\newtheorem{lem}{Lemma}[section]
\newtheorem{cor}{Corollary}[section]
\newtheorem{rmk}{Remark}[section]
\renewcommand{\theequation}{\arabic{section}.\arabic{equation}}

%\begin{document}
\title{A Dynamic Algorithm for Blind Separation of Convolutive Sound Mixtures}

\author{Jie ${\rm Liu}^{*}$, \hspace{.1 in} Jack Xin\thanks{Department of Mathematics,
UC Irvine, Irvine, CA 92697, USA.}\hspace{.05 in},
%Jack Xin \thanks{Department of Mathematics, UC Irvine, Irvine, CA 92697, USA.}
 \hspace{.02 in} and
\hspace{.02 in} Yingyong Qi \thanks{
Qualcomm Inc,
5775 Morehouse Drive,
San Diego, CA 92121, USA.}
}
\date{}
%\setcounter{page}{0}
\thispagestyle{empty}

\maketitle

%\vspace{0.25 in}
\thispagestyle{empty}



--- START OF DOCUMENT TAIL ---
2}
\end{figure}

\newpage

\begin{figure}
\centerline{\includegraphics[width=400pt]{real_batch.eps}}
%\vspace{.25 in}
\caption{}
%\label{Fig3}
\end{figure}

\newpage

\begin{figure}
\centerline{\includegraphics[width=400pt]{real_dynamic_weights.eps}}
%\vspace{.25 in}
\caption{}
%\label{Fig4}
\end{figure}

\newpage

\begin{figure}
\centerline{\includegraphics[width=400pt]{synthetic_weights.eps}}
\caption{} \label{aij}
\end{figure}

\newpage

\begin{figure}
\centerline{\includegraphics[width=400pt]{female36_music_mix.eps}}
\caption{} \label{f-m.1}
\end{figure}

\newpage

\begin{figure}
\centerline{\includegraphics[width=400pt]{female36_music_DynamicBatch.eps}}
\caption{} \label{f-m.2}
\end{figure}

\newpage

\begin{figure}
\centerline{\includegraphics[width=400pt]{female36_noise_mix.eps}}
\caption{} \label{f-n.1}
\end{figure}

\newpage

\begin{figure}
\centerline{\includegraphics[width=400pt]{female36_noise_DynamicBatch.eps}}
\caption{} \label{f-n.2}
\end{figure}









\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1231
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: Entwining.tex|>
\documentclass{tac}
\usepackage[all]{xy}
\usepackage{amsmath,amssymb}
\title{Entwining structures in monoidal categories}
\author{B. Mesablishvili}

\amsclass{16W30, 18D10, 18 D35}

\keywords{Entwining module, (braided) monoidal category, Hopf algebra}
%\address{E.M. Vitale:\\
%Universit\'e catholique de Louvain, Ch. du Cyclotron 2, B 1348
%Louvain-la-Neuve, Belgium}

%\transmittedby{xxx}

%\received{xxxx-xx-xx}

%\revised{xxxx-xx-xx}

%\published{xxxx-xx-xx}

%\num{0}

%\startpage{0}

%\tacyear{2002}

%\copyrightyear{2003}

\thanks{Supported by the research project "Algebraic and Topological Structures
in Homotopical and Categorical  Algebra, K-theory and Cyclic
Homology``, with financial support of the grant  GNSF/ST06/3-004.}
\eaddress{bachi@rmi.acnet.ge}

\newtheorem{Theorem}{Theorem}
\newtheorem{Lemma}[Theorem]{Lemma}
\newtheorem{Proposition}[Theorem]{Proposition}
\newtheorem{Definition}[Theorem]{Definition}
\newtheorem{Corollary}[Theorem]{Corollary}
\newtheorem{Observation}[Theorem]{Observation}
\newtheorem{Remark}[Theorem]{Remark}
\newtheorem{Example}[Theorem]{Example}


\newcommand{\A}{{\mathcal {A}}}
\newcommand{\B}{{\mathcal {B}}}
\newcommand{\T}{{\textbf{T}=(T, \eta, \mu)}}
\newcommand{\G}{{\textbf{G}=(G, \varepsilon, \delta)}}
\newcommand{\GG}{{\bar{{\textbf{G}}}=(\bar{G}, \bar{\varepsilon}, \bar{\delta})}}
\newcommand{\TT}{{\bar{\textbf{T}}=(\bar{T}, \bar{\eta}, \bar{\mu})}}
\newcommand{\V}{{\mathcal {V}}}
\newcommand{\la}{{\mathcal {(\mathbb{C},\mathbb{A},\lambda)}}}
\newcommand{\Al}{{ {\mathbb{A}=(A,e_A,m_A)}}}
\newcommand{\C}{{\mathcal {\mathbb{C}=(C,\varepsilon_C, \delta_C)}}}

\begin{document}
\maketitle


--- START OF DOCUMENT TAIL ---
ge, 2003.

\bibitem{C} S. Caenepeel, G. Militaru and S. Zhu,{\em Frobenius and separable functors for generalized Hopf modules and nonlinear equations}, Lect. Notes Math. \textbf{1787}, (2003).

\bibitem{D}E. Dubuc, {\em Kan extensions in enriched category
theory}.
{ Lecture Notes Math.} \textbf{145} (1970).


\bibitem{Go} J. G\'{o}mez-Torrecillas, {\em Comonads and Galois
corings}. Appl. Categ. Struct. \textbf{14}, No. 5-6, 579-598 (2006).


\bibitem{M} S. MacLane, {\em Categories for the Working
Mathematician}.
Graduate Texts in Mathematics Vol. 5, Springer, Berlin-New York,
1971.

\bibitem{Me} B. Mesablishvili, {\em Monads of effective
descent type and comonadicity}. Theory and Applications of
Categories \textbf{16} (2006), 1--45.

\bibitem{W1} R. Wisbauer, {\em Algebras versus coalgebras}. Appl. Categ. Struct. (2007) (in press).

\bibitem{W} H. Wolff, {\em V-Localizations and V-mondas}.
 J. of Algebra \textbf{24} (1973), 405--438.



\end{thebibliography}











\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1022
```latex
--- START OF DOCUMENT HEAD ---
\def\cS{\mathcal{S}}
\def\cEtil{\widetilde{\mathcal{E}}}

\def\uhat{{\hat u}}
\def\vhat{{\hat v}}
\def\xhat{{\hat x}}
\def\yhat{{\hat y}}
\def\zhat{{\hat z}}
\def\pihat{{\hat\pi}}
\def\pitil{{\tilde\pi}}
\def\mutil{{\tilde\mu}}
\def\mutila{{\widetilde\mu}}
\def\nutil{{\tilde\nu}}

\def\eps{\varepsilon}
\def\kS{{\mathfrak S}}
\def\Xhat{{\widehat{X}}}
\def\cH{{\mathcal H}}
\def\cX{{\mathcal X}}
\def\bbB{{\mathcal B}}
\def\bbR{\mathbb R}
\def\bbN{\mathbb N}
\def\bbZ{\mathbb Z}
\def\bbQ{\mathbb Q}
\def\bbP{\mathbb P}
\def\bbE{\mathbb E}
\def\bbV{\mathbb V}
\def\fR{{{\rm I}\!{\rm R}}}
\def\fN{{{\rm I}\!{\rm N}}}
\def\fZ{{{\rm Z}\mkern-5.5mu{\rm Z}}}
\def\fT{{\rm T\mkern-7.4mu T}}
\def \fC{{\;{}^{ {}_\vert }\!\!\!{\rm C}}}
%\def\ph{\varphi}
\def\fQ{{{\rm Q}\kern-.65em {}^{{}_/ }\,}}
\def\fQQ{ {{\rm Q}\kern-.57em \scriptscriptstyle{}^{]\kern.055em[}\,}}
\def\fP{{I\!\!P}}
\def\fE{{I\!\!E}}
\def\one{{{\rm 1\mkern-1.5mu}\!{\rm I}}}
\def\w{\omega}
\DeclareMathOperator{\diam}{diam}
\DeclareMathOperator{\card}{card}
\DeclareMathOperator{\supp}{supp}
\DeclareMathOperator{\dist}{dist}
\DeclareMathOperator{\var}{Var}
\DeclareMathOperator{\Var}{Var}
\def\VVar{\text{$\mathbb{V}$\!ar}}
\DeclareMathOperator{\proj}{Proj}
\def\vard{d_{\scriptscriptstyle\rm Var}}
%\def\linf{\mathop{\underline{\lim}}}
%\def\lsup{\mathop{\overline{\lim}}}
\def\linf{\varliminf}
\def\lsup{\varlimsup}
\def\esssup{\mathop{{\rm ess~sup}}}
\def\ord{\kern0.1em o\kern-0.02em{}_{\ds\breve{}}\kern0.1em}
\def\Ord{\kern0.1em O\kern-0.02em{\ds\breve{}}\kern0.1em}
%\def\ord
%\def\Ord
\def\ds{\displaystyle}
\def\ss{\scriptstyle}
\def\sss{\scriptscriptstyle}
\def\vv{{\rm{w}}}
\def\VV{{\rm{W}}}
\def\fmonth{\ifcase\month\or Jan\or Feb\or Mar\or Apr
\or May\or Jun\or Jul\or Aug\or Sep
\or Oct\or Nov\or Dec\fi\ }
\def\mmddyyyy{\the\month.\the\day.\the\year}
\def\ddmmyyyy{\the\day.\the\month.\the\year}
\def\Mddyyyy{\fmonth~\the\day,~\the\year}

%% Uncomment this if you want enumeration in roman
%\renewcommand{\labelenumi}{(\roman{enumi})}  

%% Comment this if you do not want enumeration in italic 
%% The default is with numbers
\renewcommand{\labelenumi}{\it(\alph{enumi})}  

%%% Uniform defitions

\def\R{\bbR}
\def\N{\bbN}
\def\Z{\bbZ}
\def\Q{\bbQ}
\def\P{\bbP}
\def\E{\bbE}
\def\T{\bbT}
\def\C{\bbC}
\def\tilP{{\widetilde{\P}}}
\def\tilE{{\widetilde{\E}}}


\providecommand{\abs}[1]{\left\vert#1\right\vert}
\providecommand{\norm}[1]{\left\Vert#1\right\Vert}
\providecommand{\pp}[1]{\langle#1\rangle}
\providecommand{\Norm}[1]{\muskip0=-2mu{\left|\mkern\muskip0\left|
\mkern\muskip0\left|#1\right|\mkern\muskip0
\right|\mkern\muskip0\right|}}

%% Comment this if you want equations numbered throughout the note
\numberwithin{equation}{section}

\allowdisplaybreaks[1]

%% Uncomment this if you want more space between lines
%\renewcommand{\baselinestretch}{1.1}

%%%%%%
%% Acknoledgments environment
%%%%%%

\def\acknowledgment{{\it Acknowledgment.}}
\def\acknowledgments{{\it Acknowledgments.}}

\begin{document}

%%%%%%%
%%% Author(s), abstract, and other info
%%%%%%%

\author[F.~Rassoul-Agha]{Firas~Rassoul-Agha$^1$}   % First
\thanks{$^1$Department of Mathematics, University of Utah}
\thanks{$^1$Supported in part by NSF Grant DMS-0505030}
\address{F.~Rassoul-Agha, 155 S 1400 E, Salt Lake City, UT 84112}
\email{firas@math.utah.edu}
\urladdr{www.math.utah.edu/$\sim$firas}
\author[T.~Sepp\"al\"ainen]{Timo~Sepp\"al\"ainen$^{2}$} % Second
\thanks{$^2$Mathematics Department, University of Wisconsin-Madison}
\thanks{$^2$Supported in part by NSF Grant DMS-0402231}
\address{T.~Sepp\"al\"ainen, 419 Van Vleck Hall, Madison, WI 53706}
\email{seppalai@math.wisc.edu}
\urladdr{www.math.wisc.edu/$\sim$seppalai}

\date{\today}
% this will put the date as a footnote on the first page

\keywords{Random walk, non-nestling, random environment, 
central limit theorem,
invariance principle, point of view of the
particle, environment process, Green function.}
\subjclass[2000]{60K37, 60F05, 60F17, 82D30}

%\frenchspacing



--- START OF DOCUMENT TAIL ---
e 
                  % BibTex file, even if it's not cited.

\bibliographystyle{abbrv} % A regular style that is supported 
%\bibliographystyle{aop} % An AOP-like style found and edited by Firas
                        % (the tabbing is not right though)
\bibliography{nnrefs}
%\bibliography{refsfiras,refstimo,refsmarton}

%% If you want to use thebibliography look below:

%% Uncomment this if you want to use Bibliography instead of References
%\renewcommand{\refname}{Bibliography}

%% Uncomment this, if you wanted the references in small font.
%% Don't forget to uncomment the end part!
%\begin{footnotesize} %or \begin{small}

%\begin{thebibliography}{99}
%Separate the author, title, journal, issue, pages, and year.
%It will make it easier later to put them in different formats.
%Example:
%
%\bibitem{ferrarifontes}
%P.A.~Ferrari and L.R.G.~Fontes:
%Title.....
%Electron. J. Probab.
%\textbf{3},
%1--34
%(1998)
%

%\end{thebibliography}

%\end{footnotesize} %or \end{small}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0324
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: quadratic.tex|>
\documentclass[10pt,a4paper]{amsart}
\usepackage{amssymb,amsmath}
\usepackage[american,french]{babel}
%\usepackage[T1]{fontenc}
\usepackage{amsopn}
\usepackage{graphicx}
\usepackage[ec]{aeguill}
\usepackage{fancyhdr}
\usepackage[T1]{fontenc}
\textwidth 13cm
\textheight 21.5cm
\fancyhead{}
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\fancyhead[CO]{\textsl{On the pseudospectrum of elliptic quadratic differential operators}}
\fancyhead[CE]{\textsl{Karel Pravda-Starov}}
\fancyhead[RO]{\thepage}
\fancyhead[LE]{\thepage}
\title{On the pseudospectrum of elliptic quadratic differential operators}
\newcommand{\rr}{\mathbb{R}}
\newcommand{\eps}{\varepsilon}
\newcommand{\nn}{\mathbb{N}}
\newcommand{\cc}{\mathbb{C}}
\newcommand{\Reelle}{\operatorname{Re}}
\newcommand{\lde}{L^2(\rr^n)}
\newcommand{\Ima}{\operatorname{Im}}
\def\un{{\mathrm{1~\hspace{-1.4ex}l}}}
\def\init{\setcounter{equa}{0}}
\def\inc{\stepcounter{equa}}
\def\num{\tag{\thesubsection.\theequa}}
\begin{document}
\newcounter{equa}
\selectlanguage{american}
%\pagestyle{fancy}
\begin{center}
{\large\textbf{ON THE PSEUDOSPECTRUM OF ELLIPTIC QUADRATIC DIFFERENTIAL OPERATORS}\\
\bigskip
\medskip
Karel \textsc{Pravda-Starov}\\
\bigskip
University of California, Berkeley}
\end{center}
\bigskip
\bigskip

\newtheorem{lemma}{Lemma}[subsection]
\newtheorem{definition}{Definition}[subsection]
\newtheorem{proposition}{Proposition}[subsection]
\newtheorem{theorem}{Theorem}[subsection]


\textbf{Abstract}. We study the pseudospectrum of a class of non-selfadjoint differential operators. Our work consists in a detailed study of the microlocal properties, which rule the spectral 
stability or instability phenomena appearing under small perturbations for elliptic quadratic differential operators. The class of elliptic quadratic differential operators stands for the class of 
operators defined in the Weyl quantization by
complex-valued elliptic quadratic symbols. We establish in this paper a simple necessary and sufficient condition on the Weyl symbol of these operators, which ensures the stability of their spectra. 
When this condition is violated, we prove that it occurs some strong spectral instabilities for the high energies of these operators, in some regions which can be far away from their spectra. 
We give a precise geometrical description of them, which explains the results obtained for these operators in some numerical simulations giving the computation of \og false eigenvalues \fg \ 
far from their spectra by algorithms for eigenvalues computing.

\medskip


\noindent
\textbf{Key words.} Spectral instability, pseudospectrum, semiclassical quasimodes, non-selfadjoint operators, non-normal operators, condition $(\overline{\Psi})$, subellipticity.

\medskip


\noindent
\textbf{2000 AMS Subject Classification.} 35P05, 35S05.


\section{Introduction}
 
\subsection{Miscellaneous facts about pseudospectrum}
\init

In recent years, there has been a lot of interest in studying the pseudospectrum of non-selfadjoint operators. The study of this notion has
been initiated by noticing that for certain problems of science and engineering involving non-selfadjoint operators, the predictions suggested
by spectral analysis do not match with the numerical simulations. This fact lets thinking that in some cases the only knowledge of the spectrum of an operator is not enough to understand 
sufficiently its action. To supplement this lack of information contained in the spectrum, some new subsets of the complex plane called pseudospectra have been defined. The main idea 
about the definition of these new subsets is that it is interesting to study not only the points where the resolvent of an operator is not defined, i.e. its spectrum, but also where this resolvent 
is large in norm. This explains the following definition of the $\varepsilon$-pseudospectrum $\sigma_{\varepsilon}(A)$ of a matrix or an operator $A$, 
$$\sigma_{\varepsilon}(A)=\Big\{z \in \cc,  \ \|(zI-A)^{-1}\| \

--- START OF DOCUMENT TAIL ---
5}, 241-280 (1996).
\bibitem{sjostrand}
J.Sj\"{o}strand, \textit{Parametrices for pseudodifferential operators with multiple characteristics}, Ark. f\"{o}r Mat., \textbf{12},
85-130 (1974).
\bibitem{trefethen}
L.N.Trefethen, \textit{Pseudospectra of linear operators}, Siam Review \textbf{39}, 383-400 (1997).
\bibitem{trefethen2}
L.N.Trefethen, M.Embree, \textit{Spectra and Pseudospectra:
The Behavior of Nonnormal Matrices and Operators}, Princeton University Press (2005).
\bibitem{zworski1}
M.Zworski, \textit{A remark on a paper of E.B.Davies}, Proc. Am. Math. Soc., \textbf{129}, 2955-2957 (2001).
\bibitem{zworski2}
M.Zworski, \textit{Numerical linear algebra and solvability of partial differential equations}, Comm. Math. Phys., \textbf{229}, 293-307 (2002).
\end{thebibliography}



\bigskip
\bigskip


\noindent
\textsc{Department of Mathematics, University of California, Evans Hall,
Berkeley, CA 94720, USA}\\
\textit{E-mail address:} \textbf{karel@math.berkeley.edu}




\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1340
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: push-forward.tex|>
\documentclass[10pt]{amsart}
\usepackage[nohug,small]{diagrams}

\input{macros}

\newcommand{\SchS}{(\mathrm{Sch}/S)}
\newcommand{\Sets}{(\mathrm{Sets})}
\newcommand{\syrd}{\mathcal{Y}^r_d}
\newcommand{\shred}{\mathcal{H}^{r,e}_d}

\title[A push-forward formula when $\rho=0$]
{Tautological classes on moduli spaces of curves with linear
  series and a push-forward formula when $\rho=0$}

\begin{document}



--- START OF DOCUMENT TAIL ---
\qbezier(10,24)(8.58,19.8)(8.86,16.76)
\qbezier(8.86,16.76)(9.15,13.71)(10.33,10.55)
\qbezier(10.33,10.55)(11.41,7.41)(11.21,5.43)
\qbezier(11.21,5.43)(11.02,3.45)(9.87,1.16)
\linethickness{0.3mm}
\qbezier(18,24)(16.58,19.8)(16.86,16.76)
\qbezier(16.86,16.76)(17.15,13.71)(18.33,10.55)
\qbezier(18.33,10.55)(19.41,7.41)(19.21,5.43)
\qbezier(19.21,5.43)(19.02,3.45)(17.87,1.16)
\linethickness{0.3mm}
\qbezier(32,24)(30.58,19.8)(30.86,16.76)
\qbezier(30.86,16.76)(31.15,13.71)(32.33,10.55)
\qbezier(32.33,10.55)(33.41,7.41)(33.21,5.43)
\qbezier(33.21,5.43)(33.02,3.45)(31.87,1.16)
\put(10,28){\makebox(0,0)[cc]{$E_1$}}

\put(18,28){\makebox(0,0)[cc]{$E_2$}}

\put(34,28){\makebox(0,0)[cc]{$E_{g-2}$}}

\put(24,16){\makebox(0,0)[cc]{$\dotsb$}}

\put(6,4){\makebox(0,0)[cc]{$\bullet$}}

\put(6,8){\makebox(0,0)[cc]{$p'$}}

\put(9.39,20){\makebox(0,0)[cc]{$\bullet$}}

\put(6,20){\makebox(0,0)[cc]{$p_0$}}

\put(42,4){\makebox(0,0)[cc]{$\Proj^1$}}

\put(26,28){\makebox(0,0)[cc]{$\dotsb$}}

\end{picture}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0014
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: koichi_fujii.tex|>
\documentclass[A4j]{article}

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amscd}
\usepackage{amsthm}
\usepackage{graphicx}

\title{Iterated integrals and the loop product}
\date{}
\author{Koichi Fujii}

\begin{document} 

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}

\maketitle

\section{Introduction} 

The purpose of this paper is to describe string topology from the viewpoint of Chen's iterated integrals. Let $M$ be a compact closed oriented $d$-manifold and $LM$ be the free loop space of $M$, the set of unbased smooth maps from $S^1$ to $M$. 
Let $\mathbb{H}_*(LM)$  be the homology of the free loop space shifted by the dimension of the manifold i.e. $\mathbb{H}_*(LM)$ = $H_{*+d}(LM)$. Chas and Sullivan found the product on $\mathbb{H}_*(LM)$  which they called {\it loop product} \cite{chassullivan}:
$$
\mathbb{H}_p(LM) \otimes \mathbb{H}_q(LM) \rightarrow \mathbb{H}_{p+q}(LM).
$$
They showed that this product makes $\mathbb{H}_*(LM)$ an associative, commutative algebra.

Merkulov constructed a model for this product based on the theory of iterated integrals, especially of the formal power series connection \cite{merkulov}. He showed that there is an isomorphism of algebras
$$
\mathbb{H}_*(LM) \cong H_*(\Lambda M \otimes \mathbb{R} \bigl\langle \langle X \rangle \bigr\rangle )
$$
where $\Lambda M$ is the de Rham differential graded algebra of $M$ and $\mathbb{R} \bigl\langle \langle X \rangle \bigr\rangle$ is the formal completion of the free graded associative algebra generated by some noncommutative indeterminates.

On the other hand, Chen showed that the cohomology of the free loop space of the simply-connected manifold is isomorphic to the cohomology of the cyclic bar complex of differential forms via Chen's iterated integrals (see \cite{chen77.2} or \cite{gjp}):
$$
H^*(LM) \cong H^*(C(\Lambda M)).
$$

In this paper, we construct a model for the loop product based on the theory of the cyclic bar complex. We define a complex ${\rm{Hom}}(B(\Lambda M), \Lambda M)$ and its subcomplex ${\rm{\overline{Hom}}}(B(\Lambda M), \Lambda M)$ so that the $\rm{Poincar\acute{e}}$ duality induces the isomorphism of vector spaces
$$
H_*({\rm{Hom}}(C(\Lambda M), \mathbb{R})) \cong H_{*-d}(\overline{{\rm{Hom}}}(B(\Lambda M), \Lambda M)).
$$
We can define a product on ${\rm{\overline{Hom}}}(B(\Lambda M), \Lambda M)$ which realizes the loop product.
\begin{theorem}
 Let $M$ be a compact closed oriented simply-connected manifold. Assume that $H_*(M)$ is of finite type. Let $A$ be a differential graded subalgebra of $\Lambda M$ such that $H^*(A)$ $\cong$ $H^*(\Lambda M)$ by the inclusion. Then there is an isomorphism of associative, commutative algebras 
$$
\mathbb{H}_*(LM) \cong H_*(\overline{{\rm{Hom}}}(B(A), A)). 
$$ 
The product defined on $H_*(\overline{{\rm{Hom}}}(B(A), A))$ corresponds to the loop product under the isomorphism.
\end{theorem}

The paper is organized in the following way. In section 2, we briefly review Chen's iterated integrals.  In section 3, we give a construction of  a complex ${{\rm{Hom}}}(B(A), A)$, and discuss its properties. In section 4, we give a proof of theorem 1.1. In section 5, we study the iterated integrals on the free loop space of the non-simply-connected manifolds. In section 6, we describe a relation between the product on ${{\rm{Hom}}}(B(A), A)$ and the Goldman bracket. In this paper, all the homologies have their coefficients in the field of real numbers.

{\it Acknowledgement}: The author would like to thank Professor Toshitake Kohno much for helpful comments and gentle support.

\section{Chen's iterated integrals}
We briefly review Chen's iterated integrals (see \cite{chen77.2}, or \cite{gjp}). Let $M$ be a finite dimensional smooth manifold and let $LM$ be the free loop space of $M$, that is the space of all smooth maps from $S^1$ to $M$. Let $\Delta_k$ be the $k$-simplex 
$$
\{(t_1, \c

--- START OF DOCUMENT TAIL ---
 Amer. Math. Soc. {\bf83} (1977), no.5, 831-879.
\bibitem{cjy} R.L. Cohen, J.D.S. Jones and J. Yan, {\it The loop homology algebra of spheres and projective spaces}, Categorical Decomposition Techniques in Algebraic Topology (Isle of Skye, 2001), Progr. Math., vol. 215. $Birkh\ddot{a}user$, Basel, 2004, pp.77-92.  
\bibitem{dgms} P. Deligne, P. Griffiths, J. Morgan and D. Sullivan, {\it Real homotopy theory of $K\ddot{a}hler$ manifolds}, Invent. Math. {\bf 29} (1975), 245-274.
\bibitem{gjp} E. Getzler, J.D.S. Jones and S. Petrack {\it Differential forms on loop spaces and the cyclic bar complex}, Topology {\bf30} (1991), no.3, 339-371.  
\bibitem{goldman} W.M. Goldman, {\it Invariant functions on Lie groups and Hamlitonian flows of surface group representation}, Invent. Math. {\bf85} (1986), no.2, 263-302.
\bibitem{merkulov} S.A. Merkulov, {\it De Rham Model for String Topology}, International Mathematics Research Notices {\bf55} (2004), 2955-2981. 
\end{thebibliography}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1121
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: quadfinal.tex|>
\documentclass[12pt]{amsart}
\headheight=8pt     \topmargin=0pt
\textheight=624pt   \textwidth=432pt
\oddsidemargin=18pt \evensidemargin=18pt

\usepackage{t1enc}
\usepackage[latin1]{inputenc}
\usepackage{graphicx}
%\usepackage{epsfig,multicol}  
%\usepackage{color}
%\usepackage{amstheorem}

\usepackage{amsthm, amssymb}
\usepackage{amsfonts}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\newtheorem{xca}[theorem]{Exercise}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\numberwithin{equation}{section}



\newcommand\B{\mathbb{B}}
\newcommand\C{\mathbb{C}}
\newcommand\D{\mathbb{D}}
\newcommand\F{\mathbb{F}}
\newcommand\Z{\mathbb{Z}}
\newcommand\Q{\mathbb{Q}}
\newcommand\R{\mathbb{R}}
\newcommand\N{\mathbb{N}}
\newcommand\T{\mathbb{T}}
\newcommand\cA{\mathcal{A}}
\newcommand\cB{\mathcal{B}}
\newcommand\cC{\mathcal{C}}
\newcommand\cD{\mathcal{D}}
\newcommand\cE{\mathcal{E}}
\newcommand\cF{\mathcal{F}}
\newcommand\cG{\mathcal{G}}
\newcommand\cH{\mathcal{H}}
\newcommand\cI{\mathcal{I}}
\newcommand\cL{\mathcal{L}}
\newcommand\cM{\mathcal{M}}
\newcommand\cN{\mathcal{N}}
\newcommand\cO{\mathcal{O}}
\newcommand\cP{\mathcal{P}}
\newcommand\cQ{\mathcal{Q}}
\newcommand\cR{\mathcal{R}}
\newcommand\cS{\mathcal{S}}
\newcommand\cW{\mathcal{W}}
\newcommand\fA{\mathfrak{A}}
\newcommand\fQ{\mathfrak{Q}}
\newcommand\fS{\mathfrak{S}}

\newcommand\inpr[2]{\langle{#1,#2}\rangle}
\newcommand\biota{\bar{\iota}}
\newcommand\bkappa{\bar{\kappa}}
\newcommand\hgamma{\hat{\gamma}}
\newcommand\hrho{\hat{\rho}}
\newcommand\hxi{\hat{\xi}}
\newcommand\heta{\hat{\eta}}
\newcommand\hzeta{\hat{\zeta}}
\newcommand\bpi{\bar{\pi}}
\newcommand\bnu{\bar{\nu}}
\newcommand\br{\bar{r}}
\newcommand\brho{\bar{\rho}}
\newcommand{\id}{\mathrm{id}}
\newcommand{\tr}{\mathrm{tr}}
\newcommand{\Ad}{\mathrm{Ad}}
\newcommand{\Mor}{\mathrm{Mor}}
\newcommand{\Sect}{\mathrm{Sect}}
\newcommand{\End}{\mathrm{End}}
\newcommand{\Aut}{\mathrm{Aut}}
\newcommand{\Ang}{\mathrm{Ang}}
\newcommand{\Gal}{\mathrm{Gal}}
\newcommand{\opp}{\mathrm{opp}}
\newcommand{\tA}{\tilde{A}}
\newcommand{\tB}{\tilde{B}}
\newcommand{\tC}{\tilde{C}}
\newcommand{\tD}{\tilde{D}}
\newcommand{\tN}{\tilde{N}}
\newcommand{\tM}{\tilde{M}}
\newcommand{\tP}{\tilde{P}}
\newcommand{\tQ}{\tilde{Q}}
\newcommand{\tR}{\tilde{R}}
\newcommand{\tfQ}{\tilde{\fQ}}
\newcommand{\tlambda}{\tilde{\lambda}}
\newcommand{\quadri}{\begin{array}{ccc}
P & \subset& M \\
\cup & & \cup \\
N &\subset &Q 
\end{array}}
\newcommand{\tquadri}{\begin{array}{ccc}
\tP & \subset& \tM \\
\cup & & \cup \\
\tN &\subset &\tQ 
\end{array}}
%\newfont{\gothic} { ygoth scaled \magstep{1.5}}
%\newcommand{\notetoself}[1]{\marginpar{\tiny #1}}
%\newcommand{\5}{\vskip 5pt}
%\newcommand\bh{{\cal B}({\cal H})}
%\def\<{\langle}
%\def\>{\rangle}  
%\renewcommand\P{{$\cal P \hspace {4pt}$}}
%\newcommand\A{\mbox{\gothic A}\hspace {6pt}}
%\newcommand\T{\mbox{\gothic T}\hspace {6pt}}
%\newcommand\Am{\mbox{\gothic A}}
%\newcommand\Tm{\mbox{\gothic T}}



\newcommand{\hpic}[2]{\mbox{$\begin{array}[c]{l} 
\includegraphics*[height=#2]{figs/#1}
\end{array}$}}
 
\newcommand{\vpic}[2]{\mbox{$\begin{array}[c]{l} 
\includegraphics*[width=#2]{figs/#1}
\end{array}$}}

\newcommand{\hvpic}[3]{\mbox{$\begin{array}[c]{l} 
\includegraphics*[height=#2,width=#3]{figs/#1}
\end{array}$}}





\begin{document}


\title{Classification of noncommuting quadrilaterals of factors}
\author{Pinhas Grossman}
\author{Masaki Izumi}
\thanks{Work supported by JSPS}
\maketitle




--- START OF DOCUMENT TAIL ---
.


\bibitem{Was} Wassermann, A., 
Operator algebras and conformal field theory. III. Fusion of positive energy representations 
of ${\rm LSU}(N)$ using bounded operators. 
{\em Invent. Math.} {\bf 133} (1998), 467--538.

\bibitem{Wat} 
Watatani, Y., 
Lattices of intermediate subfactors.
{\em J. Funct. Anal.}, {\bf 140} (1996), 312--334.

\bibitem{Wen} 
Wenzl, H., 
$C^*$ tensor categories from quantum groups. 
{\em J. Amer. Math. Soc.} {\bf 11} (1998), 261--282. 

\bibitem{X} Xu, Feng, 
New braided endomorphisms from conformal inclusions. 
{\em Comm. Math. Phys.} {\bf 192} (1998), 349--403. 


\endthebibliography





\bigskip

\flushleft{Pinhas Grossman, Department of Mathematics, 1326 Stevenson Center, Vanderbilt University, Nashville, TN, 37203 \\
{\it e-mail}: pinhas.grossman@vanderbilt.edu}


\flushleft{Masaki Izumi, Department of Mathematics, Graduate
School of Science, Kyoto University, Sakyo-ku, Kyoto 606-8502,
Japan\\
{\it e-mail}: izumi@math.kyoto-u.ac.jp}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0231
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: Riemann.tex|>
\documentclass[a4paper,12pt]{amsart}
\usepackage{amssymb,a4wide,ifpdf}

\ifpdf
  \usepackage[pdftex]{graphicx,color}
  \usepackage[pdftex,colorlinks]{hyperref}%,colorlinks
  \hypersetup{%
      pdftitle={Sampling and Interpolation on Finite Riemann Surfaces},
      pdfauthor={Joaquim Ortega-Cerda},
      colorlinks=true,
      linkcolor=blue %red,cyan,green,yellow
  }
\else
  \usepackage[dvips]{graphicx,color}
  \usepackage[hypertex,colorlinks]{hyperref}
  \hypersetup{%
      colorlinks=true,
      linkcolor=blue %red,cyan,green,yellow
  }
\fi

\newcommand{\R}{\mathbb R}
\newcommand{\D}{\mathbb D}
\newcommand{\C}{\mathbb C}
\newcommand{\Z}{\mathbb Z}
\renewcommand{\H}{\mathcal H}
\newcommand{\ddbar}{\partial\bar\partial}
\newcommand{\dbar}{\bar\partial}
\newcommand{\dist}{\operatorname{dist}}


\renewcommand{\Re}{\operatorname{Re}}

\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}

%opening
\title{Interpolating and sampling sequences in finite Riemann surfaces}
\author{Joaquim Ortega-Cerd\`a}
\address{Dept.\ Matem\`atica Aplicada i An\`alisi, Universitat  de Barcelona,
Gran Via 585, 08071 Bar\-ce\-lo\-na, Spain}
\email{jortega@ub.edu}
\date{Working draft: \today}
\thanks{Supported by DGICYT grant MTM2005-08984-C02-02 and the CIRIT grant
2005SGR00611}

\keywords{} 
\subjclass{}



\begin{document}
\maketitle


--- START OF DOCUMENT TAIL ---
7--322.
  \MR{97c:30044}

\bibitem[Sei98]{Seip98}
\bysame, \emph{Developments from nonharmonic {F}ourier series}, Proceedings of
  the International Congress of Mathematicians, Vol. II (Berlin, 1998), no.
  Extra Vol. II, 1998, pp.~713--722 (electronic). \MR{99h:42023}

\bibitem[SS54]{SchSpe54}
Menahem Schiffer and Donald~C. Spencer, \emph{Functionals of finite {R}iemann
  surfaces}, Princeton University Press, Princeton, N. J., 1954. \MR{16,461g}

\bibitem[Sto65]{Stout65}
E.~L. Stout, \emph{Bounded holomorphic functions on finite {R}iemann surfaces},
  Trans. Amer. Math. Soc. \textbf{120} (1965), 255--285. \MR{32\#1358}

\bibitem[SV04]{SchVar04}
A.~Schuster and D.~Varolin, \emph{{I}nterpolation and {S}ampling for
  generalized {B}ergman spaces on finite {R}iemann {S}urfaces.}, Preprint,
  2004.

\bibitem[Wer64]{Wermer64}
John Wermer, \emph{Analytic disks in maximal ideal spaces}, Amer. J. Math.
  \textbf{86} (1964), 161--170. \MR{28 \#5355}

\end{thebibliography}







\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0942
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: skew_DH.tex|>
\documentclass[twoside,11pt]{amsart}
\usepackage{graphicx, lscape}
\usepackage{amsmath, amsfonts, amssymb, ifthen}

%%%%%%%%%%%% shorthands %%%%%%%%%%%%%%%%%


\renewcommand{\Re}{\operatorname{Re}}
\renewcommand{\Im}{\operatorname{Im}}
\renewcommand{\(}{\left(}
\renewcommand{\)}{\right)}  
\newcommand{\abs}[1]{\left\arrowvert #1\right\arrowvert}
\newcommand{\norm}[1]{\left\| #1\right\|}
\newcommand{\field}[1]{\mathbb{#1}}
\newcommand{\CC}{\ensuremath{\field{C}}} 
\newcommand{\RR}{\ensuremath{\field{R}}} 
\newcommand{\NN}{\ensuremath{\field{N}}} 
\newcommand{\DD}{\ensuremath{\field{D}}} 
\newcommand{\ZZ}{\ensuremath{\field{Z}}} 
\newcommand{\Ct}{\ensuremath{\field{C}^2}}
\newcommand{\Ch}{\ensuremath{\hat{\field{C}}}}
\newcommand{\Po}{\ensuremath{\field{P}^1}} 
\newcommand{\Pt}{\ensuremath{\field{P}^2}}

\newcommand{\Nvs}{\mathcal{N}_{v}^{\#}}
 
\newcommand{\eps}{\epsilon}
\newcommand{\lam}{\lambda}
\newcommand{\hol}{holomorphic }
\newcommand{\jjp}{J_{J_p}}

\newcommand{\A}{A(C_{J_p})}
\newcommand{\Apt}{A_{pt}(C_{J_p})}
\newcommand{\Acc}{A_{cc} (C_{J_p})} 

%\newcommand{WuLJp}{W^u(\Lambda) \cap (J_p \times \CC)}


%%%%%%%%%%%%%%% theorem-types %%%%%%%%%%%%%%%%%%%

\theoremstyle{plain}
%% In plain theorem style, text is italicized.
\newtheorem{thm}{Theorem}[section]
\newtheorem{cor}[thm]{Corollary}
\newtheorem{lem}[thm]{Lemma}
\newtheorem{prop}[thm]{Proposition}
\newtheorem{prob}[thm]{Problem}
\newtheorem{con}[thm]{Conjecture}
\newtheorem{example}[thm]{Example}

\theoremstyle{definition}
%% In defn style, the text is not italicized.
\newtheorem{defn}[thm]{Definition}
%\theoremstyle{remark}
%% "least emphatic style"
\newtheorem{rem}[thm]{Remark}
%\newtheorem*{prob}{Problem}
\newtheorem{question}[thm]{Question}


%%%%%%%%%%%%%%%% figures %%%%%%%%%%%%%%%%%%%%%%%

%\newcommand{\drawfigtwcantcl}{\scalebox{.75}{\includegraphics{twcantimag-combo-cl}}}

\newcommand{\drawfigtwbascl}{\scalebox{.5}{\includegraphics{twbas-combo-cl}}}

\newcommand{\drawfigaerocant}{\scalebox{.52}{\includegraphics{aerocantcombo-new-l}}}

\newcommand{\drawfigcantcircbas}{\scalebox{.8}{\includegraphics{cantcircbas-combo-bl}}}

%%%%%%%%%%%%%%%% comments %%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\showcomments}{yes}
%\newcommand{\showcomments}{no}

\newsavebox{\commentbox}
\newenvironment{comment}%
% begin comment
{\ifthenelse{\equal{\showcomments}{yes}}%
% then begin comment in margin
{\footnotemark
    \begin{lrbox}{\commentbox}
    \begin{minipage}[t]{1.25in}\raggedright\sffamily\small
    \footnotemark[\arabic{footnote}]}
% else eat contents of the environment
{\begin{lrbox}{\commentbox}}}%
% end comment
{\ifthenelse{\equal{\showcomments}{yes}}%
% then end comment
{\end{minipage}\end{lrbox}\marginpar{\usebox{\commentbox}}}
% else finish eating
{\end{lrbox}}}

\newcommand{\cb}[1]{\begin{comment} #1 \end{comment}}

%%%%%%%%%%%%%%%% document %%%%%%%%%%%%%%%%%%%%%%%%
\begin{document}

\title{Axiom A Polynomial skew products of $\Ct$ \\ and their postcritical sets}

\author[L. ~DeMarco]{Laura DeMarco$^1$}
\address{Department of Mathematics\\
University of Chicago\\
5734 S. University Ave.\\
Chicago, IL 60637\\
USA}
\email{demarco@math.uchicago.edu}
\author[S.L. ~Hruska]{Suzanne Lynch Hruska$^2$}
\address{Department of Mathematical Sciences\\
University of Wisconsin Milwaukee\\
PO Box 413\\
Milwaukee, WI 53201\\
USA}
\email{shruska@msm.umr.edu}

\date{\today}



--- START OF DOCUMENT TAIL ---
so if $x$ is any point in $\Lambda$, then there are unstable manifolds through $x$ for each prehistory $\hat{x} \in \hat{\Lambda}$.  If $f$ is 1-1 on $\Lambda$, then there is only one prehistory in $\Lambda$ for each point in $\Lambda$, so through a point in $\Lambda$ only one unstable manifold.
%If $f$ is not 1-1 on $\Lambda$, how do the various local unstable manifolds fit together to give a structure to $\Lambda$ (for example, we already know each connected component of $\Lambda_z$ is a point,  and $\Lambda$ has local product structure for any $f$ Axiom A)?
%\begin{comment} What about $(z^2, w^2+\eps(1-z))$?  Probably should shorten this discussion, or remove it \end{comment}
%\end{question}

%\begin{question} 
%Add a question like: To what extent does conjugacy preserve fiber dynamics. 
%\end{question}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Bibliography
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\bibliographystyle{alpha}
\bibliography{Skew}


 \end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1236
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: SNC3.tex|>
 %\documentclass[a4paper,12pt]{article}
 \documentclass{article}
\usepackage{amsmath}
 \usepackage{amsfonts}
 \usepackage{amsthm}
 \usepackage{amssymb}
\usepackage{dsfont}\let\mathbb\mathds
\usepackage[english,frenchb]{babel}
 \usepackage[latin1]{inputenc}
\usepackage[T1]{fontenc}

%\usepackage[all,dvips]{xy}

\usepackage[all]{xy}


%\usepackage[pdftex]{graphicx,color} 

\usepackage[active]{srcltx}
\usepackage[breaklinks=true]{hyperref}
\usepackage{eprint}

\DeclareMathOperator{\MOD}{MOD}
\DeclareMathOperator{\Vect}{Vect}
\DeclareMathOperator{\PAR}{PAR}
\DeclareMathOperator{\Par}{Par}
\DeclareMathOperator{\FPar}{FPar}
\DeclareMathOperator{\EFPar}{EFPar}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\Homb}{\bold{Hom}}
\DeclareMathOperator{\Ext}{Ext}
\DeclareMathOperator{\obj}{obj}
\DeclareMathOperator{\Tot}{Tot} 
\DeclareMathOperator{\SPEC}{\bold{Spec}}   
\DeclareMathOperator{\Sym}{Sym}
\DeclareMathOperator{\gr}{gr}
\DeclareMathOperator{\pr}{pr}
\DeclareMathOperator{\spec}{spec}
\DeclareMathOperator{\coker}{coker}
\DeclareMathOperator{\LC}{LC}
\DeclareMathOperator{\SLC}{SLC}
\DeclareMathOperator{\SLCF}{SLCF}
\DeclareMathOperator{\LCF}{LCF}
\DeclareMathOperator{\Champs}{Champs}
\DeclareMathOperator{\Rev}{Rev}
\DeclareMathOperator{\Cat}{Cat}
\DeclareMathOperator{\Ens}{Ens}
\DeclareMathOperator{\F}{F}
\DeclareMathOperator{\EF}{EF}
\DeclareMathOperator{\RH}{RH}
\DeclareMathOperator{\NS}{NS}
\DeclareMathOperator{\SS_0}{SS_0}
\DeclareMathOperator{\Rep}{Rep}
\DeclareMathOperator{\prof}{prof}
\DeclareMathOperator{\cone}{cone}
\DeclareMathOperator{\Aut}{Aut}
\DeclareMathOperator{\Ind}{Ind}
\DeclareMathOperator{\Pic}{Pic}
\DeclareMathOperator{\Pico}{Pic^0}
\DeclareMathOperator{\Pict}{Pic^{\tau}}
\DeclareMathOperator{\PIC}{\mathcal{P}\it{ic}}
\DeclareMathOperator{\SCPIC}{\bold{Pic}}
\DeclareMathOperator{\rg}{rg}
\DeclareMathOperator{\Gal}{Gal}




\newtheorem{thm}{Th\'eor\`eme}
\newtheorem{defi}{D\'efinition}
\newtheorem{cor}{Corollaire}
\newtheorem{prob}{Probl\`eme}
\newtheorem{lem}{Lemme}
\newtheorem{prop}{Proposition}
\newtheorem{rem}{Remarque}



  \newcommand{\UN}[4][r]{%
    \ar@/^1pc/[#1]^{#2}_*=<0.3pt>{}="HAUT"
    \ar@/_1pc/[#1]_{#3}^*=<0.3pt>{}="BAS"
    \ar @{=>} "HAUT";"BAS" ^{#4}
  }

\newcommand{\DEUX}[4][r]{%
    \ar@/^1pc/[#1]^{#2}_*=<0.3pt>{}="HAUT"
    \ar@/_1pc/[#1]_{#3}^*=<0.3pt>{}="BAS"
    \ar @{=>} "BAS";"HAUT" _{#4}
  }

%\input xy
%\xyoption{all}

\begin{document}
 
\bibliographystyle{tocplain} 
\author{Niels Borne}
\title{Sur les repr�sentations du groupe fondamental d'une vari�t� priv�e d'un diviseur � croisements normaux simples
%\\ (version pr�liminaire)
}
 
 \maketitle
 %\tableofcontents

\section{Introduction}
\label{sec:introduction}

\subsection{Une description alternative}
\label{sec:descr:alter}

En l'absence de lacets, la recherche d'une description alternative du groupe fondamental �tale (d�fini dans \cite{SGA1} en termes de rev�tements) est une question classique, motiv�e essentiellement par la volont� de d�terminer alg�briquement des groupes fondamentaux qui ne sont connus que par voie transcendante. 

L'�tude syst�matique du lien entre rev�tements de, disons, une vari�t� alg�brique projective $X$, et certain fibr�s sur $X$, commence avec Weil (\cite{Weil}). Celui-ci montre qu'un rev�tement galoisien non ramifi� de surfaces de Riemann $Y\rightarrow X$ permet d'associer � toute repr�sentation $V$ complexe du groupe de Galois $G$ un fibr� sur $X$ : on descend le fibr� trivial $Y\times V$ sur $Y$ en $E=Y\times V/G$. Weil remarque que cette op�ration est compatible avec le produit tensoriel, ce qui conf�re des propri�t�s remarquables aux fibr�s associ�s : ils sont en particulier \emph{finis}, au sens qu'il existe deux polyn�mes distincts $f,g$ � coefficients entiers positifs tels que $f(E)\simeq g(E)$. Il voit dans ces fibr�s la g�n�ralisation des fibr�s en droite de torsion, et commence � les caract�riser. 

Ce travail trouve son aboutissement dans la formulation de Nori (\c

--- START OF DOCUMENT TAIL ---
ier qu'il s'agit d'un ensemble, pour �tre  correct, il faut probablement supposer la cat�gorie $I$ petite} de triplets $(f,g,\alpha)$ :

\xymatrix@R=2pt{ 
&&& i \ar[dr]^f &&&\\
&&&    &   k,  &    f_*C \ar[r]^{\alpha} & g_* D\\
&&& j \ar[ur]_g &&&
}


pour la relation

\xymatrix@R=2pt{ 
i \ar[dr]^f &&&&& i \ar[dr]^{f'} &&&\\
&   k,  &    f_*C \ar[r]^{\alpha} & g_* D&\sim &&   k',  &    f'_*C \ar[r]^{\alpha'} & g'_* D\\
j \ar[ur]_g &&&&& j \ar[ur]_{g'} &&&
}

s'il existe 

\xymatrix@R=2pt{ 
&&& k \ar[dr]^h &\\
&&&    &   l \\
&&& k' \ar[ur]_{h'} &
}

tel que $h\circ f=h'\circ f'$, $h\circ g=h'\circ g'$ et $h_*\alpha=h'_*\alpha'$.
\end{enumerate}
	
\begin{prop}
	La cat�gorie $\mathcal C$, munie de la transformation naturelle canonique $\mathcal F \rightarrow c_{\mathcal C}$, est une $2$-limite pour $\mathcal F$.
\end{prop}

\begin{proof}
	C'est une v�rification longue mais directe de la d�finition \ref{deflimindcat} dans ce cas pr�cis.

\end{proof}


\bibliography{SNC3}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0813
```latex
--- START OF DOCUMENT HEAD ---
nd{\tq}{{\tilde q}}
\newcommand{\tu}{{\tilde u}}
\newcommand{\tv}{{\tilde v}}
\newcommand{\ts}{{\tilde s}}
\newcommand{\tn}{{\tilde n}}
\newcommand{\tell}{{\tilde\ell}}
\newcommand{\tI}{{\tilde I}}
\newcommand{\tN}{{\tilde N}}
\newcommand{\tm}{{\widetilde m}}
\renewcommand{\tt}{t}
\newcommand{\ttt}{{\tilde t}}
\newcommand{\ta}{{\tilde\alpha}}
\newcommand{\tbeta}{{\tilde\beta}}
\newcommand{\tsi}{{\tilde\sigma}}
\newcommand{\ttau}{{\tilde\tau}}
\newcommand{\tka}{{\tilde\kappa}}
\newcommand{\teta}{{\tilde\eta}}
\newcommand{\tchi}{{\tilde\chi}}
\newcommand{\ph}{\varphi}

\newcommand{\la}{\langle}
\newcommand{\ra}{\rangle}
\newcommand{\tbk}{{\tilde{\bf k}}}
\newcommand{\tbp}{{\tilde{\bf p}}}
\newcommand{\tbq}{{\tilde{\bf  q}}}
\newcommand{\tbr}{{\tilde{\bf  r}}}
\newcommand{\tbv}{{\tilde{\bf v}}}
\newcommand{\tbu}{{\tilde{\bf  u}}}
\newcommand{\tbK}{{\widetilde{\bf K}}}
\newcommand{\tmu}{{\tilde\mu}}
\newcommand{\tbm}{{\widetilde{\bf m}}}
\newcommand{\tbh}{{\tilde{\bf  h}}}
\newcommand{\balpha}{{\boldsymbol \alpha}}
\renewcommand{\a}{\alpha}
\renewcommand{\b}{\beta}
\newcommand{\g}{\gamma}
\newcommand{\e}{\varepsilon}
\newcommand{\s}{\sigma}
\newcommand{\om}{{\omega}}
\newcommand{\ka}{\kappa}
\newcommand{\bU}{{\bf U}}
\newcommand{\bE}{{\bf E}}
\newcommand{\cU}{{\cal U}}
\newcommand{\cM}{{\cal M}}
\newcommand{\cX}{{\cal X}}
\newcommand{\bR}{{\mathbb R}}
\newcommand{\bC}{{\mathbb C}}
\newcommand{\bN}{{\mathbb N}}
\newcommand{\bZ}{{\mathbb Z}}

\newcommand{\bi}{\bigskip}
\newcommand{\noi}{\noindent}
\newcommand{\tr}{\mbox{Tr}}
\newcommand{\sgn}{\mbox{sgn}}


\newcommand{\wt}{\widetilde}
\newcommand{\wh}{\widehat}
\newcommand{\ov}{\overline}

\newcommand{\bxi}{{\boldsymbol \xi}}
\newcommand{\bzeta}{\mbox{\boldmath $\zeta$}}
\newcommand{\bpsi}{\mbox{\boldmath $\psi$}}
\newcommand{\bnabla}{\mbox{\boldmath $\nabla$}}
\newcommand{\btau}{\mbox{\boldmath $\tau$}}
\newcommand{\tbtau}{\widetilde{\btau}}
\newcommand{\const}{\mathrm{const}}
\newcommand{\cG}{{\cal G}}
\newcommand{\cS}{{\cal S}}
\newcommand{\cC}{{\cal C}}
\newcommand{\cF}{{\cal F}}
\newcommand{\cA}{{\cal A}}
\newcommand{\cB}{{\cal B}}
\newcommand{\cE}{{\cal E}}
\newcommand{\cP}{{\cal P}}
\newcommand{\cD}{{\cal D}}
\newcommand{\cV}{{\cal V}}
\newcommand{\cW}{{\cal W}}
\newcommand{\cK}{{\cal K}}
\newcommand{\cH}{{\cal H}}
\newcommand{\cL}{{\cal L}}
\newcommand{\cN}{{\cal N}}
\newcommand{\cO}{{\cal O}}
\newcommand{\cJ}{{\cal J}}

\newcommand{\A}{\left( \int  \, W^2 | \nabla_m \nabla_k \phi|^2  \, + N
\int  \, W^2 |\nabla_m \phi|^2 + N^2 \int  \, W^2 |\phi|^2 \right)}
\newcommand{\B}{\left(\int \, W^2 |\nabla_m \phi|^2 + N \int  \, W^2
|\phi|^2 \right)}
\newcommand{\C}{\left( \int  \, W^2 | \nabla_m \nabla_k \phi|^2  \, + N
\int  \, W^2 |\nabla_m \phi|^2  \right)}
\newcommand{\Ci}{\left( \int  \, W^2 | \nabla_i \nabla_j \phi|^2  \, + N
\int  \, W^2 |\nabla_i \phi|^2  \right)}

\newcommand{\usi}{\underline{\sigma}}
\newcommand{\ubp}{\underline{\bp}}
\newcommand{\ubk}{\underline{\bk}}
\newcommand{\utbp}{\underline{\tbp}}
\newcommand{\utbk}{\underline{\tbk}}
\newcommand{\um}{\underline{m}}
\newcommand{\utm}{\underline{\tm}}
\newcommand{\utau}{\underline{\tau}}
\newcommand{\uttau}{\underline{\ttau}}
\newcommand{\uxi}{\underline{\xi}}
\newcommand{\ueta}{\underline{\eta}}
\newcommand{\ux}{\underline{x}}
\newcommand{\uv}{\underline{v}}
\newcommand{\ualpha}{\underline{\alpha}}
\newcommand{\Om}{\Omega}
\newcommand{\Hn}{\cH^{\otimes n}}
\newcommand{\Hsn}{\cH^{\otimes_s n}}
\newcommand{\thi}{ \; | \!\! | \!\! | \;}
\newcommand{\supp}{\operatorname{supp}}
\newcommand{\bfeta}{{\boldsymbol \eta}}

\newcommand{\no}{\nonumber}

\renewcommand{\thefootnote}{\arabic{footnote}}

\input epsf

\def\req#1{\eqno(\hbox{Requirement #1})}


\newcommand{\fh}{{\frak h}}
\newcommand{\tfh}{\wt{\frak h}}


\newcommand{\donothing}[1]{}

\begin{document}
\title{Dynamics of Bose-Einstein Condensates}
\author{Benjamin Schlein\\
\\
Department of Mathematics, University of California at Davis, CA
95616, USA}

\maketitle



--- START OF DOCUMENT TAIL ---
oss-Pitaevskii equation. {\it Phys.
Rev. Lett.} {\bf 98} (2007), no. 4, 040404.

\bibitem{EY} Erd{\H{o}}s, L.; Yau, H.-T.: Derivation
of the nonlinear {S}chr\"odinger equation from a many body {C}oulomb
system. \textit{Adv. Theor. Math. Phys.} \textbf{5} (2001), no. 6,
1169--1205.

\bibitem{LS} Lieb, E.H.; Seiringer, R.:
Proof of {B}ose-{E}instein condensation for dilute trapped gases.
\textit{Phys. Rev. Lett.} \textbf{88} (2002), no. 17, 170409.


%\bibitem{LSSY} Lieb, E.H.; Seiringer, R.; Solovej, J.P.; Yngvason, J.:
%{\sl The mathematics of the Bose gas and its condensation. }
%Oberwolfach Seminars, {\bf 34.} Birkhauser Verlag, Basel, 2005.

\bibitem{LSY} Lieb, E.H.; Seiringer, R.; Yngvason, J.: Bosons in a trap:
a rigorous derivation of the {G}ross-{P}itaevskii energy functional.
\textit{Phys. Rev A} \textbf{61} (2000), no. 4, 043602.

\bibitem{Sp} Spohn, H.: Kinetic Equations from Hamiltonian Dynamics.
\textit{Rev. Mod. Phys.} \textbf{52} (1980), no. 3, 569--615.


\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0993
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: ym_tail_cor.tex|>
%\documentclass[prl,superscriptaddress,nofootinbib]{revtex4}
\documentclass[prd,superscriptaddress, nofootinbib]{revtex4}
\usepackage{graphicx}% Include figure files
\usepackage{dcolumn}% Align table columns on decimal point
\usepackage{bm}
\usepackage{amsmath,amsthm,amssymb}
%\usepackage{setspace}

\setlength{\baselineskip}{16.0pt}    % 16 pt usual spacing between lines



\begin{document}
%

%\preprint{APS/123-QED}

\title{Late-time tails of a Yang-Mills field\\ on Minkowski and Schwarzschild backgrounds}

\author{Piotr Bizo\'n}
\affiliation{M. Smoluchowski Institute of Physics, Jagiellonian
University, Krak\'ow, Poland} \affiliation{Max-Planck-Institut f\"ur
Gravitationsphysik, Albert-Einstein-Institut, Potsdam, Germany}
\author{Tadeusz Chmaj}
\affiliation{H. Niewodniczanski Institute of Nuclear
   Physics, Polish Academy of Sciences,  Krak\'ow, Poland}
   \affiliation{Cracow University of Technology, Krak\'ow,
    Poland}
\author{Andrzej Rostworowski}
\affiliation{M. Smoluchowski Institute of Physics, Jagiellonian
University, Krak\'ow, Poland}
%
\date{\today}
%


--- START OF DOCUMENT TAIL ---
1993).

\bibitem{cs} P. T. Chru\'sciel and J. Shatah, Asian J. Math. \textbf{1}, 530
(1997).

\bibitem{cw}  R-G. Cai and A. Wang, Gen. Rel. Grav. \textbf{31}, 1367
(1999).

\bibitem{bcr} P. Bizo\'n, T. Chmaj, and A. Rostworowski,
math-th/0701037

%\bibitem{du} O. Dumitrascu, Stud. Cerc. Mat. \textbf{34}(4), 329 (1982).

\bibitem{fm} P. Forgacs and N.S. Manton, Commun. Math. Phys. \textbf{72}, 15
(1980).

\bibitem{l} E. W. Leaver, Phys. Rev. \textbf{D34}, 384 (1986).

\bibitem{p} R. Price, Phys. Rev. \textbf{D5}, 2419 (1972).

%\bibitem{clsy} E.S.C. Ching et al., Phys. Rev. {\bf D52}, 2118 (1995).

%\bibitem{knuth} We use here Knuth's notation in which the square
%bracket around an expression returns a value $1$ iff the expression
%is true.

\bibitem{b} L. Barack, Phys. Rev. \textbf{D59}, 044017 (1999).

\bibitem{dr} M. Dafermos and I. Rodnianski, math.AP/0503024

\bibitem{bcrs} P. Bizo\'n, N. Szpak, T. Chmaj, and A. Rostworowski,
in preparation


\end{thebibliography}


\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1043
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: LongAbstractDelahaye2.tex|>
\documentclass{ws-rv9x6}
\usepackage{ws-rv-van}             % numbered citation/references (default)
%\usepackage{ws-index}             % to produce multiple indices
\makeindex
%\newindex{aindx}{adx}{and}{Author Index}       % author index
%\renewindex{default}{idx}{ind}{Subject Index}  % subject index
\begin{document}



--- START OF DOCUMENT TAIL ---
Li, and P. Vit\'anyi. The miraculous universal distribution. \emph{Math. Intelligencer} 19(4), 7-15, 1997.
\bibitem{li2} M. Li and P. Vit\'anyi, \emph{An Introduction to Kolmogorov Complexity and Its Applications}, Springer, 1997.
\bibitem{levin} A.K.Zvonkin, L. A. Levin. "The Complexity of finite objects and the Algorithmic Concepts of Information and Randomness.", \emph{UMN = Russian Math. Surveys}, 25(6):83-124, 1970. 
\bibitem{lloyd} S. Lloyd, \emph{Programming the Universe}, Knopf, 2006.
\bibitem{solomonoff} R. Solomonoff, The Discovery of Algorithmic Probability, \emph{Journal of Computer and System Sciences}, Vol. 55, No. 1, pp. 73-88, August 1997.
\bibitem{solomonoff2} R. Solomonoff, \emph{A Preliminary Report on a General Theory of Inductive Inference}, (Revision of Report V-131), Contract AF 49(639)-376, Report ZTB-138, Zator Co., Cambridge, Mass., Nov, 1960
\bibitem{wolfram} S. Wolfram, \emph{A New Kind of Science}, Wolfram Media, 2002.

\end{thebibliography}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0069
```latex
--- START OF DOCUMENT HEAD ---
{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\disk}{\mathbb{D}}
\newcommand{\rSphere}{\overline{\C}}
\newcommand{\punct}[1]{{\C^{#1}\setminus\{0\}}}
\newcommand{\Proj}{\mathbb{P}}

% Outdated composition operator
\newcommand{\cp}[1]{^{\circ{#1}}}
\newcommand{\cpp}[1]{^{\circ({#1})}}

% Categories / Functors other than Gamma
%\newcommand{\cat}{\mf}
\newcommand{\topcat}{\operatorname{Top}}
\newcommand{\mapcat}{\operatorname{Map}}
\newcommand{\self}[1]{\operatorname{Self{\cat{#1}}}}
\newcommand{\functor}[1]{\operatorname{\msans{#1}}}
\newcommand{\fixed}{\functor{Fixed}}

% Cohology / Homology / Sheaves
\newcommand{\clDec}{\mf{c}}
\newcommand{\cochain}[1]{{#1}^{\bullet}}
\newcommand{\deRham}{H_{\text{deRham}}}
\newcommand{\forms}[1]{\ms{F}^{#1}}
%\newcommand{\forms}[1]{\ms{E}_{\text{deg\ }#1}}
\newcommand{\clForms}[1]{\forms{#1}_\clDec}
\newcommand{\hol}{\mc{O}} % Sheaf of holomorphic functions
\newcommand{\curDeg}[1]{\ms{C}^{#1}}
%\newcommand{\curDeg}[1]{{\ms{D}'}_{\text{deg\ }#1}}
\newcommand{\curDim}[1]{\ms{C}_{#1}}
%\newcommand{\curDim}[1]{{\ms{D}'}_{\text{dim\ }#1}}
\newcommand{\clCurDeg}[1]{\curDeg{#1}_\clDec}
\newcommand{\clCurDim}[1]{\curDim{#1}^\clDec}
\newcommand{\shHone}[2]{\ensuremath{H^1(#1,\sheaf{#2})}}
\newcommand{\hbundles}[1]{H^1(#1,\pluriharmonic)} 
\newcommand{\shsub}[1]{_{\sheaf{#1}}} % A sheaf subscript
\newcommand{\shGamma}[1]{\Gamma(\sheaf{#1})} % Gamma applied to a sheaf
\newcommand{\mGamma}[1]{\Gamma {#1}}
\newcommand{\mshGamma}[2]{\mGamma{{#1}\shsub{#2} }}
\newcommand{\mshHone}[2]{\ensuremath{H^1{#1}\shsub{#2}}}
\newcommand{\sequenceCohom}{\tilde}



% Injection/Surjection
\newcommand{\into}{\hookrightarrow}
\newcommand{\onto}{\twoheadrightarrow}


% Greens
\newcommand{\G}{\mc{G}}
\newcommand{\greens}{\mf{g}}


% Matrices / Column Vectors
\newcommand{\transpose}[1]{{}^\tau{#1}}
\newcommand{\vt}[1]{\begin{pmatrix} #1 \end{pmatrix}}


% Headings
\newcommand{\heading}{\section}
\newcommand{\subheading}{\subsection}



% Altered Text
\newcommand{\confirm}[1]{\orange{#1}}





% Temporary Placement Area
\newcommand{\smap}[1]{{#1}\to{#1}}
\newcommand{\scohom}[1]{{#1}\mto{#1}}
\newcommand{\lto}[1]{\overset{#1}{\to}} % labeled arrow
\newcommand{\lift}{\check}
\newcommand{\hollift}{\breve}
\newcommand{\except}{\mc{K}}
\newcommand{\weakstar}{weak$^\star$ }
\DeclareMathOperator{\exsupp}{ExSupp}
\DeclareMathOperator{\brsupp}{BrSupp}
\newcommand{\nonnegative}{\R_{\geq 0}}
\newcommand{\positive}{\R_{>0}}
\newcommand{\positiveK}{\K_0}
\newcommand{\andinfty}{\cup\{\infty\}}
\newcommand{\diff}{\gamma} 
\newcommand{\erg}{{\text{ergodic}}}
\newcommand{\nempty}{{\not=\emptyset}}
\newcommand{\K}{\mathbb{K}}
\newcommand{\khom}{H^\dagger}
\newcommand{\ot}{\leftarrow} % arrow pointing left
\newcommand{\lot}[1]{\overset{#1}{\ot}} % labelled arrow pointing left
\newcommand{\can}{\ms{C}}
\newcommand{\sca}{\mb{K}} % Field of scalars with complete metric
\newcommand{\interior}{\operatorname{int}}
\newcommand{\diam}{\operatorname{diam}}
\newcommand{\divisor}{\msans}
\newcommand{\current}{\msans}
\newcommand{\form}{\msans}
\newcommand{\maxMult}{\Upsilon}
\newcommand{\minMult}{\upsilon}
\newcommand{\smear}{\mc{S}}
\newcommand{\dvect}[1]{\frac{\partial}{\partial #1}}
\newcommand{\extend}[1]{\big\arrowvert^{#1}}
\newcommand{\nimble}{\ms{N}} 
\newcommand{\lenient}{\ms{L}} 
\newcommand{\comassNorm}[1]{\|{#1}\|_{\text{comass}}}
\newcommand{\supNorm}[1]{\|{#1}\|_{\text{sup}}}
\newcommand{\pder}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\cat}{\mc{S}}
\newcommand{\holder}{H}


\begin{document}

\title{Dynamical Objects for Cohomologically Expanding Maps.}
\author{John W. Robertson}
\maketitle

\bigskip
\noindent{John W. Robertson\footnote{Research partially supported by a Wichita State University ARCS Grant.}} \\
\noindent{Wichita State University} \\
\noindent{Wichita, Kansas 67260-0033} \\
\noindent{Phone: 316-978-3979} \\
\noindent{Fax: 316-978-3748} \\ 
\noindent{robertson@math.wichita.edu} \\







--- START OF DOCUMENT TAIL ---
F(z))=d\cdot G(z)$ and $G(\beta z)=G(z)+\logabs{\beta}$
%for $z\in \punct{n+1}$ and $\beta\in\C^*$.

Our Greens trivialization $\greens\colon p\to \R$ can be pulled
back to give a Green's function $\G\colon \ell^*\to\R$ 
on the punctured bundle $\ell^*$. It satisfies 
$\G(\tilde{f}(w))=\lambda\cdot \G(w)$ and $\G(\beta w)=\G(w)+\logabs{\beta}$
for $w\in \ell$ and $\beta\in\C^*$. Since 
$\greens$ is a trivialization of an $\R$ bundle
over a compact space, $\greens$ is proper. Since
$\logabs{\cdot}\colon \ell^*\to p$ is proper then $\G$ is proper.
Thus, in this setting one can construct a Greens function that is exactly
analogous to the Green's function constructed on
$\C^{n+1}$ for a holomorphic endomorphism
of $\Proj^n$.  Potentially one could take advantage of 
the special geometry of very ample bundles to get
information about the dynamics in this situation.


\section{Bibliography}


\bibliographystyle{alpha}
\bibliography{refer}

%\begin{thebibliography}{McM02}





\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0802
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: icassp_2007.tex|>
% Template for SLT-2006 paper; to be used with:
%          spconf.sty  - ICASSP/ICIP LaTeX style file, and
%          IEEEbib.bst - IEEE bibliography style file.
% --------------------------------------------------------------------------
\documentclass{article}
\usepackage{spconf,amsmath,epsfig}

% Example definitions.
% --------------------
\def\x{{\mathbf x}}
\def\L{{\cal L}}

% Title.
% ------
\title{Hybrid-ARQ in Multihop Networks with Opportunistic Relay Selection}
%
% Single address.
% ---------------
\name{Caleb K. Lo, Robert W. Heath, Jr. and Sriram Vishwanath \thanks{Caleb K. Lo was supported by a Microelectronics and Computer Development (MCD) Fellowship and a Thrust 2000 Endowed Graduate Fellowship through The University of Texas at Austin.  Robert Heath was supported in part by the National Science Foundation under grant CNS-626797 and the DARPA IT-MANET program, Grant W911NF-07-1-0028.  Sriram Vishwanath was supported by the National Science Foundation under grants CCF-055274, CCF-0448181, CNS-0615061 and CNS-0626903.}}
% \address{Wireless Networking and Communications Group \\ Department of Electrical and Computer Engineering \\ The University of Texas at Austin, Austin, Texas 78712 \\ Email: \{clo, rheath, sriram\}@ece.utexas.edu}
\address{The University of Texas at Austin, Austin, Texas 78712 \\ Email: \{clo, rheath, sriram\}@ece.utexas.edu}
%
% For example:
% ------------
%\address{School\\
%   Department\\
%   Address}
%
% Two addresses (uncomment and modify for two-address case).
% ----------------------------------------------------------
%\twoauthors
%  {A. Author-one, B. Author-two\sthanks{Thanks to XYZ agency for funding.}}
%   {School A-B\\
%   Department A-B\\
%   Address A-B}
%  {C. Author-three, D. Author-four\sthanks{The fourth author performed the work
%   while at ...}}
%   {School C-D\\
%   Department C-D\\
%   Address C-D}
%
\begin{document}
\topmargin=0mm
% \setlength{\evensidemargin}{-6.2mm}
% \setlength{\oddsidemargin}{-6.2mm}\setlength{\textwidth}{178mm}
% \setlength{\topmargin}{0in} \setlength{\columnsep}{6mm}
% \setlength{\textheight}{229mm } \pagestyle{empty}
% \marginsize{0.75in}{0.75in}{1in}{1in}
% \ninept
%
\maketitle
%


--- START OF DOCUMENT TAIL ---
.J.~Greenstein, L.J.~Cimini and A.M.~Haimovich.
\newblock New approaches for cooperative use of multiple antennas in ad hoc wireless networks.
\newblock In {\em Proc. of the IEEE Vehic. Techno. Conf.}, 4:2769-2773, Los Angeles, CA, September 2004.

\bibitem{ZhaVal:PracRelaNetwGene:Jan:05}
B.~Zhao and M.C.~Valenti.
\newblock Practical relay networks: a generalization of hybrid-ARQ.
\newblock {\em IEEE J. Select. Areas Commun.}, 23(1):7--18, January 2005.

\bibitem{TanHea:OppoFeedDownMult:Oct:05}
T.~Tang and R.W.~Heath, Jr.
\newblock Opportunistic feedback for downlink multiuser diversity.
\newblock {\em IEEE Comm. Lett.}, 9(10):948--950, October 2005.

\bibitem{Hag:RateCompPuncConv:Apr:88}
J.~Hagenauer.
\newblock Rate-compatible punctured convolutional codes (RCPC codes) and their applications.
\newblock {\em IEEE Trans. Comm.}, 36(4):389--400, April 1988.

\bibitem{WireMANWorkGrp}
Wireless~MAN~Working~Group.
\newblock http://www.wirelessman.org/.

\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0914
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: wormhole_math.tex|>
%revised by Allan April 6/07, arxiv submission


%\documentclass[a4,12pt]{article}
\documentclass[12pt]{article}
\usepackage{amssymb}
\usepackage{latexsym}
\usepackage{epsfig}
\usepackage{graphicx}
\usepackage{psfrag}

\parindent0pt
\parskip6pt




%Matti's macros

\newcommand{\newtextt}{\bf}
\newcommand{\newtekst}{\bf}
\newcommand{\newtext}{}

%\newcommand{\newnewtext}{}%{\bf}
%\newcommand{\newtext}{}
%\newcommand{\newtekst}{}

\newcommand{\HOX}[1]{\marginpar{\footnotesize #1}}

%\newcommand{\HOX}[1]{}


\newtheorem{definition}{Definition}[section]
\newtheorem{theorem}[definition]{Theorem}
\newtheorem{lemma}[definition]{Lemma}
\newtheorem{problem}[definition]{Problem}
\newtheorem{proposition}[definition]{Proposition}
\newtheorem{corollary}[definition]{Corollary}
\newtheorem{remark}[definition]{Remark}
\newtheorem{example}[definition]{Example}

\newcommand{\R}{{\mathbb R}}
\newcommand{\D}{{\mathbb D}}
\newcommand{\C}{{\mathbb C}}
\renewcommand{\S}{{\mathbb S}}
\newcommand{\N}{{\mathbb N}}
\newcommand{\proofbox}{{$\Box$}}
\def\hat{\widehat}
\def\tilde{\widetilde}
\def \bfo {\begin {eqnarray*} }
\def \efo {\end {eqnarray*} }
\def \ba {\begin {eqnarray*} }
\def \ea {\end {eqnarray*} }
\def \beq {\begin {eqnarray}}
\def \eeq {\end {eqnarray}}
\def \supp {\hbox{supp}\,}
\def \diam {\hbox{diam }}
\def \rad {\hbox{rad}}
\def \ind {\hbox{Ind}\,}
\def \dist {\hbox{dist}}
\def\diag{\hbox{diag }}
\def \det {\hbox{det}}
\def\bra{\langle}
\def\cet{\rangle}
\def \e {\varepsilon}
\def \p {\partial}
\def \a {\alpha}
\def\M{{\mathcal M}}
\def\F{{\mathcal F}}
\def\Z{{\Bbb Z}}
\def\p{\partial}
\def\sph{\mathbb S^2}
\def\R{\mathbb R}




\title{Electromagnetic wormholes via \\
       handlebody constructions}




\author{Allan Greenleaf, Yaroslav Kurylev,
\\ Matti Lassas and Gunther Uhlmann
\thanks{AG and GU are supported by
US NSF, ML by CoE-programm 213476 of Academy of Finland.}}





\date{}

\begin{document}

\maketitle







--- START OF DOCUMENT TAIL ---
rigorous time-domain analysis of full--wave
electromagnetic cloaking (Invisibility), preprint, ArXiv.org:07040248v1 (2007).


\bibitem{T2}
M.\ Visser,  {\it Lorentzian Wormholes},  AIP Press, 1997.


\end {thebibliography}




\vskip.2in
%\vfil\eject



\noindent{\sc Department of Mathematics}

\noindent{\sc University of Rochester}


\noindent{\sc Rochester, NY 14627, USA, \quad \tt{allan@math.rochester.edu}}


\vskip.2in



\noindent{\sc Department of Mathematical Sciences}


\noindent{\sc University of Loughborough}


\noindent{\sc Loughborough, LE11 3TU, UK,\quad \tt{Y.V.Kurylev@lboro.ac.uk}}





\vskip.2in



\noindent{\sc Institute of Mathematics}


\noindent{\sc Helsinki University of Technology}


\noindent{\sc Espoo, FIN-02015, Finland,\quad \tt{Matti.Lassas@tkk.fi}}





\vskip.2in



\noindent{\sc Department of Mathematics}

\noindent{\sc University of Washington}

\noindent{\sc Seattle, WA 98195, USA,\quad \tt{gunther@math.washington.edu}}









\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2359
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: ApplMathsLetStokesAccept.tex|>
% Template article for preprint document class `elsart'
% SP 2001/01/05
% Modifi� CG (ESME) pour Modele 3, une colonne, 2 titres, abstract/resume,
%
%  Version francaise pour Mathematiques (CRAS s�rie 1)
% Modifi� (CG, le 17 aout 2004) - rubrique(s), dates et presentateur
%    Le resume avant l'abstract comme dans le journal

\documentclass[doublespacing]{elsart}

% Utiliser l'option doublespacing ou reviewcopy pour avoir une
% inter-ligne double
% \documentclass[doublespacing]{elsart}

% Si vous avez des figures PostScript, utilisez l'extension 'graphics'
% pour des commandes simples
% \usepackage{graphics}

% ou l'extension 'graphicx' pour des commandes plus compliquees
% \usepackage{graphicx}

% ou utilisez l'extension 'epsfig' si vous preferez les 'vielles' commandes
% \usepackage{epsfig}

% Pour des symboles mathematiques :
%\usepackage{amsmath,amsthm,amsfonts,amssymb}
\usepackage{amsmath,amsfonts,amssymb}
\usepackage[dvips]{graphicx}
\usepackage[english,french]{babel}


%ENVIRONNEMENTS, THEOREMES, etc...
% Ils sont predefines, et ils suivent le format de la revue !
%English
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{e-proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{e-definition}[theorem]{Definition\rm}
\newtheorem{remark}{\it Remark\/}
\newtheorem{example}{\it Example\/}

%Fran�ais
\newtheorem{theoreme}{Th\'eor\`eme}[section]
\newtheorem{lemme}[theoreme]{Lemme}
\newtheorem{proposition}[theoreme]{Proposition}
\newtheorem{corollaire}[theoreme]{Corollaire}
\newtheorem{definition}[theoreme]{D\'efinition\rm}
\newtheorem{remarque}{\it Remarque}
\newtheorem{exemple}{\it Exemple\/}
\renewcommand{\theequation}{\arabic{equation}}
\setcounter{equation}{0}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% GUILLEMETS (FRENCH QUOTES) %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\og{\leavevmode\raise.3ex\hbox{$\scriptscriptstyle\langle\!\langle$~}}
\def\fg{\leavevmode\raise.3ex\hbox{~$\!\scriptscriptstyle\,\rangle\!\rangle$}}
\def\u{{\textbf {\textit u}}}
\def\f{{\textbf {\textit f}}}
\def\n{{\textbf {\textit n}}}
\def\v{{\textbf {\textit v}}}


\begin{document}
% Vous pouvez mettre dans la prochain ligne la rubrique choisie
% (si vous la connaissez) - meme deux, format : Rubrique1/Rubrique2
%\centerline{}
%\begin{frontmatter}
\begin{center}
\selectlanguage{english}
\title{ Navier-Stokes equations with periodic boundary conditions and pressure loss}
%\end{frontmatter}
\end{center}
\begin{center}
\author[1]{Ch\'erif Amrouche},
%\ead{cherif.amrouche@univ-pau.fr}
\author[1,2]{Macaire Batchi},
%\ead{ma.batchi@etud.univ-pau.fr}
\author[2]{Jean Batina}.
%\ead{jean.batina@univ-pau.fr}
\address[1]{Laboratoire de Math\'ematiques Appliqu\'ees,
CNRS UMR 5142}
\address[2]{Laboratoire de Thermique Energ\'etique et
Proc\'ed\'es}
\address{Universit\'e de Pau et des Pays de l'Adour}
\address{Avenue de l'Universit\'e 64000 Pau, France}
% etc, etc
\end{center}
%\end{frontmatter}
\begin{center}
%

--- START OF DOCUMENT TAIL ---
 problem in arbitrary dimension},\ \textrm{Czecholovak
Mathematical Journal}, \textbf{44\ (119)}, Praha, pp.109-139,\
(1994).

\bibitem{2}\textrm{R. Dautray et J. L. Lions}, \textit{Analyse math\'{e}%
matique et calcul num\'{e}rique pour les sciences et les
techniques,}\ tome 1-6, Masson, 1984.

\bibitem{3}\textrm{V. Girault and P. A. Raviart}, \ \textit{Finite
Element Methods for Navier-Stokes Equations, }Springer Series SCM,
1986.

\bibitem{4}\textrm{J. L. Lions}, \ \textit{Quelques m\'{e}thodes de r\'{e}%
solution des probl\`{e}mes aux limites non-lin\'{e}aires,
}Gauthier-Villars, 1969.

\bibitem{5}\textrm{S. V. Patankar, C. H. Liu  and E. M. Sparrow}, \textit{%
Fully developed flow and heat transfer in ducts having
streamwise-periodic variations of cross sectional area}, \emph{J.
Heat Transfer}, \textbf{99}, pp.180-186, (1977).

\bibitem{6}\textrm{R. Temam},\ \textit{Navier-Stokes
Equations.Theory and Analysis, }North-Holland, Amsterdam, 1985.

\end{thebibliography}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1986
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: closedVFs.tex|>
\documentclass[12pt,oneside]{article}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage{color}

%%
%\pagestyle{myheadings}    %You can use this line to define your left-hand and right-hand
                                                  % headings with the command \markboth
%\markboth{Nabil L. Youssef}{Title}
\textheight = 9.5in            %45\baselineskip
\textwidth = 6in \leftmargin=1.25in \rightmargin=1.25in
\topmargin=0.75in
\parindent=0.3in
\hoffset -1.3truecm \voffset -3truecm
%%%%%% This is to define \goth %%%%%%%%
\def\goth{\mathfrak}
\def\Sc{\mathcal}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MATH -------------------------------------------------------------------
\newcommand{\A}{{\cal A}}
\newcommand{\F}{{\cal F}}
\newcommand{\T}{{\cal T}}
\newcommand{\C}{{\cal C}}
\newcommand{\V}{{\cal V}}
\newcommand{\h}{{\cal H}}
\newcommand{\s}{{\cal S}}
\newcommand{\W}{{\cal W}}
\newcommand{\BH}{\mathbf B(\cal H)}
\newcommand{\KH}{\cal  K(\cal H)}
\newcommand{\Real}{\mathbb R}
%\newcommand{\Complex}{\mathbb C}
%\newcommand{\Field}{\mathbb F}
%\newcommand{\RPlus}{[0,\infty)}
\newcommand{\norm}[1]{\left\Vert#1\right\Vert}
\newcommand{\essnorm}[1]{\norm{#1}_{\text{\rm\normalshape ess}}}
\newcommand{\abs}[1]{\left\vert#1\right\vert}
\newcommand{\set}[1]{\left\{#1\right\}}
\newcommand{\seq}[1]{\left<#1\right>}
\newcommand{\eps}{\varepsilon}
\newcommand{\To}{\longrightarrow}
\newcommand{\RE}{\operatorname{Re}}
\newcommand{\IM}{\operatorname{Im}}
\newcommand{\Poly}{{\cal{P}}(E)}
\newcommand{\EssD}{{\cal{D}}}
\newcommand{\prof}{\noindent \textit{\textbf{Proof.\:\:}}}
\newcommand{\tm}{\T M}
\newcommand{\p}{\pi^{-1}(TM)}
\newcommand {\cp}{\mathfrak{X}(\pi (M))}
\newcommand {\ccp}{\mathfrak{X}^{*}(\pi (M))}
\newcommand {\cpp}{\mathfrak{X}(\T M)}
\def\o#1{\overline{#1}}

\def\pa{\partial}
\def\paa{\dot{\partial}}

\def\ti#1{\tilde{#1}}
\def\G{\Gamma}
\def\O{\Omega}

\def\f{ \mathfrak{F}(M)}

%def\:{{\em\,:}} def\({{\em (}} def\){{\em )}} def\[{{\em [}}
%\def\]{{\em ]}}
%\def\1#1{\big#1}
%\def\2#1{\Big#1}
%\def\3#1{\bigg#1}
%\def\4#1{\Bigg#1}


\setlength\arraycolsep{2pt}    %For suitable spacing in "Arrays"
\renewcommand{\arraystretch}{1.1}

\def\refname{\center References}
\def\Section#1{\vspace{30truept}\addtocounter{section}{1}\setcounter{thm}{0}\setcounter{equation}{0}
{\noindent\Large\bf\arabic{section}.~~#1}\par \vspace{12pt}}

\newtheorem{thm}{Theorem}[section]
\newtheorem{cor}[thm]{Corollary}
\newtheorem{lem}[thm]{Lemma}
\newtheorem{prop}[thm]{Proposition}
\newtheorem{defn}[thm]{Definition}
\newtheorem{example}{Example}
\newtheorem{rem}[thm]{Remark}


\def\thedefinition{\arabic{definition}}  %This is to put a period after Def.
\def\thetheorem{\arabic{theorem}}
\def\thelemma{\arabic{lemma}}
\def\theproposition{\arabic{proposition}}
\def\thecorollary{\arabic{corollary}}
\def\theexample{\arabic{example}}
\def\theremark{\arabic{remark}}

\numberwithin{equation}{section}
\newtheorem{theorema}{Theorem}            %To remove the enumeration
\def\thetheorema{\hspace{-0.3cm} .}

\begin{document}
%\title{{\bf CHARACTERIZATION OF CLOSED VECTOR FIELDS IN FINSLER GEOMETRY}}

\title{{\bf Characterization of Closed Vector Fields in Finsler Geometry}}
\author{\bf{Nabil L. Youssef }}
\date{}
\maketitle

% End of preamble and beginning of text.
% Produces the title.
\vspace{-1.15cm}

\begin{center}
{Department of Mathematics, Faculty of Science,\\
Cairo University, Giza, Egypt.\\
nyoussef@frcu.eun.eg,\, nlyoussef2003@yahoo.fr}
\end{center}
%\smallskip
\begin{center}
{\bf Dedicated to the memory of Prof. Dr. A. Tamim}
\end{center}

\bigskip

\noindent{\bf Abstract.}  The $\pi$-exterior derivative $\o d$,
which is the Finslerian generalization of the (usual) exterior
derivative $d$ of Riemannian geometry, is defined. The notion of a
$\o d$-closed vector field is introduced and investigated. Various
characterizations of \linebreak $\o d$-closed vector fields are
established. Some results concerning $\o d$-closed vector fields in


--- START OF DOCUMENT TAIL ---
s
  to \textsc{R}anders spaces}, Ph. D. Thesis, Cairo University, 1991.

\bibitem{r77}
\bysame, \emph{Fundamental differential operators in
\textsc{F}insler geomtry}, Proc. Math. Phys. Soc. Egypt, \textbf{73}
(1998), 67-93.

\bibitem{r48}
\bysame, \emph{Special \textsc{F}insler manifolds}, J. Egypt. Math.
Soc.,
  \textbf{10(2)} (2002), 149--177.

\bibitem{r79}
A. A. Tamim and N. L. Youssef, \emph{On generalised \textsc{R}anders
manifolds}, Algebras Groups and Geometries, \textbf{16} (1999),
115-126.

\bibitem{r83}
K. Yano, \emph{Integral formulas in \textsc{R}iemannian geometry},
Marcel Dekker Inc., New York, 1970.

\bibitem{r85}
N. L. Youssef, \emph{Sur les tenseurs de coubure de la connexion de
Berwald et ses distributions de nullit\'{e} }, Tensor, N. S.,
\textbf{36} (1982), 275-280.

\bibitem{r62}
N. L. Youssef, S. H. Abed, and A.~Soleiman, \emph{A global theory of
  conformal \textsc{F}insler geometry}, Submitted. ArXiv No.: math. DG/0610052.

\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2403
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: rings.tex|>
 \documentclass[11pt]{amsart}
    \textwidth=5in
    \textheight=7.5in

\usepackage{amsmath}
\usepackage[dvips]{graphicx}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{mathrsfs}
\usepackage[hyperindex]{hyperref}
\usepackage{amsrefs}


%\usepackage[notref,notcite]{showkeys}

%\usepackage[active]{srcltx}

\allowdisplaybreaks[1]
\newtheorem{thm}{Theorem}[section]
\newtheorem{prop}[thm]{Proposition}
\newtheorem{lemma}[thm]{Lemma}
\newtheorem{cor}[thm]{Corollary}

\theoremstyle{remark}
\newtheorem{problem}[thm]{Problem}
\theoremstyle{remark}
\newtheorem{remark}[thm]{Remark}

\newtheorem{convention}[thm]{Convention}

\theoremstyle{definition}
\newtheorem{defn}[thm]{Definition}

\theoremstyle{remark}
\newtheorem{ex}[thm]{Example}

\newcommand{\R}{{\mathbb{R}}}
\newcommand{\tg}{{\tilde{g}}}
\newcommand{\F}{{\mathcal{F}}}
\newcommand{\Su}{{\mathcal{S}}}
\newcommand{\he}{{H_\epsilon}}
\newcommand{\se}{{\Sigma_\epsilon}}
\newcommand{\set}{{\tilde{\Sigma}_\epsilon}}
\newcommand{\Ge}{{g}}
\newcommand{\gbar}{{\bar{g}}}
\newcommand{\pt}{\frac{\partial}{\partial t}}
\newcommand{\pl}{\frac{\partial}{\partial l}}
\newcommand{\pu}{\frac{\partial}{\partial u}}
\newcommand{\ps}{\frac{\partial}{\partial s}}
\newcommand{\dt}{\nabla_t}
\newcommand{\du}{\nabla_u}
\newcommand{\ds}{\nabla_s}
\newcommand{\sw }{\sqrt{w}}

\begin{document}


\title[Apparent horizons with product of spheres topology]{Existence 
of outermost
apparent horizons with product of spheres topology}

\author{Fernando Schwartz}
\address{Mathematics Department, Duke  University}
\email{fernando@math.duke.edu}



\maketitle




--- START OF DOCUMENT TAIL ---
anifolds also belong to
 an important special class of initial data, given by    
 asymptotically flat Riemannian manifolds  with nonnegative scalar curvature. 
These  manifolds correspond to
 totally geodesic slices of reasonable spacetimes (c.f. \cite{bray01})
 and have been studied extensively in this context.
 
 Constructing an  initial data  set that evolves into a black hole
 may seem impossible to achieve, since on the one hand
 the black hole region is determined from the entire 
 development of spacetime, and on the other hand
 we do not know how to compute the full evolution of the Cauchy problem. 
 Fortunately,  there is a simple criterion that guarantees the 
existence of black holes evolving from initial data.  Indeed, it is known
  that the future evolution of an initial data set that contains an
 {\it apparent horizon} has a black hole in it.  
Furthermore, any such black hole encloses 
 the apparent horizon. (See \cite{wald84}).  
  Our main result is the following.
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0501
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: nls.tex|>
\documentclass[12pt]{article}
\usepackage{amssymb,epsfig,times,graphicx}
\usepackage{amsmath}
%\usepackage{showkeys}
%\usepackage{pdfsync}
\newcommand{\rk}{\mbox {rk}\hskip 0.5truemm}
%\newcommand{\mod}{\mbox {mod}\hskip 0.5truemm}
\newcommand{\res}{{\rm res}\hskip 0.5truemm}
\newcommand{\diag}{{\rm diag}\hskip 0.5truemm}
\newcommand{\im} {\mbox {Im}\hskip 0.5truemm}
\newcommand{\sign}{\mbox{sign}\hskip 0.5truemm}
%\renewcommand{\theequation}{\arabic{section}.\arabic{subsection}.\arabic{equation}}
\def\theequation{\thesection.\arabic{equation}}
\def\theguess{\thesubsection.\arabic{guess}}
\newtheorem{theorem}{Theorem}
\newtheorem{guess}[theorem]{Conjecture}
%\def\thetheorem{\thesubsection.\arabic{theorem}}
\def\thetheorem{\thesection.\arabic{theorem}}
\newtheorem{prop}[theorem]{Proposition}
\def\theprop{\thesubsection.\arabic{prop}}
\newtheorem{lemma}[theorem]{Lemma}
%\def\thelemma{\thesubsection.\arabic{lemma}}
\def\thelemma{\thesection.\arabic{lemma}}
\newtheorem{cor}[theorem]{Corollary}
%\def\thecor{\thesubsection.\arabic{cor}}
\def\thecor{\thesection.\arabic{cor}}
\newtheorem{exam}[theorem]{Example}
%\def\theexam{\thesubsection.\arabic{exam}}
\def\theexam{\thesection.\arabic{exam}}
\newtheorem{remark}[theorem]{Remark}
%\def\theremark{\thesubsection.\arabic{remark}}
\def\theremark{\thesection.\arabic{remark}}
\newcommand{\eqa}{\begin{eqnarray}}
\newcommand{\eeqa}{\end{eqnarray}}
\newcommand{\beq}{\begin{equation}}
\newcommand{\eeq}{\end{equation}}
\newcommand{\nn}{\nonumber}
\newcommand{\dbl}{\langle\hskip -0.09truecm \langle}
\newcommand{\dbr}{\rangle\hskip -0.09truecm \rangle}
\newcommand{\pal}{\partial}
\newcommand{\tb}{\tilde b}
\newcommand{\tf}{\tilde F}
\newcommand{\F}{{\cal F}}
\newcommand{\R}{{\mathbb R}}
\newcommand{\al}{\alpha}
\newcommand{\ga}{\gamma}
\newcommand{\lgl}{\log{L}}
\newcommand{\ld}{\Lambda}
\newcommand{\de}{\delta}
\newcommand{\tn}{\widetilde \nabla}
\newcommand{\lm}{\lambda}
\newcommand{\del}{\delta}
\newcommand{\ve}{\varepsilon}
\newcommand{\w}{\omega}
\newcommand{\f}{F^{(1)}}
\newcommand{\tx}{t_{X}}
\newcommand{\txx}{t_{XX}}
\newcommand{\txxx}{t_{XXX}}
\newcommand{\txxxx}{t_{XXXX}}
\newcommand{\pf}{\noindent{\it Proof \ }}
\newcommand{\tr}{{\rm tr}}
\newcommand{\epf}{$\quad$\hfill
\raisebox{0.11truecm}{\fbox{}}\par\vskip0.4truecm}
\newcommand{\epl}{The lemma is proved.$\quad \Box$}
\newcommand{\ept}{The theorem is proved.$\quad \Box$}
\newcommand{\epp}{The proposition is proved.$\quad \Box$}
\setlength{\topmargin}{0.27in}
\setlength{\headheight}{0.0in}
\setlength{\headsep}{0.0in}
\textheight 22.5truecm
\textwidth 15.5truecm
\baselineskip16.2pt
\hoffset -0.8cm
\parskip 5pt plus 1pt
%\begin{document}

\title{On universality of critical behaviour in the focusing nonlinear Schr\"odinger equation, elliptic umbilic catastrophe and the {\it tritronqu\'ee} solution to the Painlev\'e-I equation.}
\author{{B.Dubrovin$^*$, T.Grava$^*$, C.Klein$^{**}$}\\
{\small $^*$ SISSA, Trieste; $^{**}$ Max-Planck Institute, Leipzig }}
\begin{document}
\maketitle


--- START OF DOCUMENT TAIL ---
er equation. {\it Comm. Pure Appl. Math.} {\bf  57}  (2004) 877--985.

\bibitem{to2} A.Tovbis, S.Venakides, X.Zhou,  On the long-time limit of semiclassical (zero dispersion limit) solutions of the focusing nonlinear Sch\"odinger equation: pure radiation case.  {\it Comm. Pure Appl. Math.}  {\bf 59}  (2006) 1379--1432.

\bibitem{trefethen1}  L.~N.~Trefethen,
   \emph{ Spectral Methods in MATLAB}, SIAM, Philadelphia, PA, 2000.
   
\bibitem{gwp2} Y.Tsutsumi, $L^2$-solutions for nonlinear Schr\"odinger equations and nonlinear groups. {\it Funkcial. Ekvac.} {\bf 30} (1987) 115--125.

\bibitem{whi} G.B.Whitham, {\it Linear and Nonlinear Waves}. Wiley-Intersci. 1974.

\bibitem{za} V.E.Zakharov, A.B.Shabat, A. B. Exact theory of two-dimensional self-focusing and one-dimensional self-modulation of waves in nonlinear media. {\it Soviet Physics JETP} {\bf 34} (1972), 
no. 1, 62-69.; translated from {\it \v{Z}. Eksper. Teoret. Fiz.}  (1971), no. 1, 118-134.

\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1980
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: mcosine-vcycle_submitted.tex|>
% ------------------------------------------------------------------------
% bmultdoc.tex for birkmult.cls*******************************************
% 8.03.2007
% ------------------------------------------------------------------------
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\documentclass{birkmult}
\usepackage{amssymb}
%
% THEOREM Environments (Examples)-----------------------------------------
%
 \newtheorem{thm}{Theorem}[section]
 \newtheorem{cor}[thm]{Corollary}
 \newtheorem{lem}[thm]{Lemma}
 \newtheorem{prop}[thm]{Proposition}
 \theoremstyle{definition}
 \newtheorem{defn}[thm]{Definition}
 \theoremstyle{remark}
 \newtheorem{rem}[thm]{Remark}
 \newtheorem*{ex}{Example}
 \numberwithin{equation}{section}
%--------------------------------------------------------------------------------------
\newcommand{\tronc}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\stronc}[1]{\left\lceil #1 \right\rceil}
\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\Chi}{\alza[.55mm]{\chi}}
\newcommand{\alza}[2][5mm]{{\raisebox{#1}{$#2$}}}
\newcommand{\mi}[1]{{\ensuremath{\underline{#1}}}}
\def\sdots{\mathinner{
    \mskip.01mu\raise5pt\vbox{\kern1pt\hbox{.}}
    \mskip.01mu\raise3pt\hbox{.}
    \mskip.01mu\raise1pt\hbox{.}
\mskip1mu}}
%--------------------------------------------------------------------------------------
%--------------------------------------------------------------------------------------
\begin{document}
%--------------------------------------------------------------------------------------
% editorial commands: to be inserted by the editorial office
%
%\firstpage{1}
%\volume{228}
%\Copyrightyear{2004}
%\DOI{003-0001}
%
%
%\seriesextra{Just an add-on}
%\seriesextraline{This is the Concrete Title of this Book\br H.E. R and S.T.C. W, Eds.}
%
% for journals:
%
%\firstpage{1}
%\issuenumber{1}
%\Volumeandyear{1 (2004)}
%\Copyrightyear{2004}
%\DOI{003-xxxx-y}
%\Signet
%\commby{inhouse}
%\submitted{March 14, 2003}
%\received{March 16, 2000}
%\revised{June 1, 2000}
%\accepted{July 22, 2000}
%
%
%
%--------------------------------------------------------------------------------------
%Insert here the title, affiliations and abstract:
%
\title[V-cycle optimal convergence for %%(unilevel**)
DCT-III matrices]
 {V-cycle optimal convergence for %%(unilevel**)
 DCT-III matrices}
%----------Author 1
\author[C. Tablino Possio]{C. Tablino Possio}

\address{%
Dipartimento di Matematica e Applicazioni,\\
Universit\`a di Milano Bicocca,\\
via Cozzi 53\\
20125 Milano\\
Italy}

\email{cristina.tablinopossio@unimib.it}

\thanks{The work of the author was partially supported by MIUR, grant
number 2006017542.}
%----------Author 2
%\author{A Second Author}
%\address{The address of\br
%the second author\br
%sitting somewhere\br
%in the world}
%\email{dont@know.who.knows}
%----------classification, keywords, date
\subjclass{Primary 65F10, 65F15, 15A12%; Secondary ***
}

\keywords{DCT-III algebra, two-grid and multigrid iterations,
multi-iterative methods}

%\date{January 1, 2004}
%----------additions
\dedicatory{Dedicated to Georg Heinig}
%%%--------------------------------------------------------------------------------------


--- START OF DOCUMENT TAIL ---
nging from $-q+1$ to $q-1$ (this matrix is the one
displayed in the inner box of \eqref{matrice Phi}). The
corresponding analysis is now straightforward: the vector of all
ones is an eigenvector of $M^T$ related to the eigenvalue 1
(because of the left side in \eqref{matrice Phi});
$\|M\|_\infty=1$, $M_{ij}\geqslant 0$ and $M$ is irreducible.
Finally, the result follows from the Perron--Frobenius theorem
applied to the matrix $M$. \qquad\end{proof}

We remark that the previous result on the limit polynomial
$\psi^*$ can be refined a little bit. Indeed, it belongs to
$\mathbb{R}_{q-1}$ (instead of $\mathbb{R}_q$) since the
eigenvector ${a}^*$ of $\overline{\Phi}_q$ related to the
dominating eigenvalue $\lambda=1$ is of the form
\[
\left(
\begin{array}{c}
   0         \\
   \hat{{a}}    \\
   0
\end{array}
\right),
\]
where $\hat{{a}}$ is the positive eigenvector of $M$ associated
with the dominating eigenvalue $\lambda=1$.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0098
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: CDMA_resub_2008.tex|>
% ------------------------------------------------ %
% Sparse CDMA                                      %
% J.Raymond  and David Saad                       %
% July 27 2007                                    %
% Changes in response to JphysA ref. rep          %
% ------------------------------------------------ %

\documentclass[12pt]{iopart}
\include{epsf}
\usepackage{amssymb}

\textwidth=16.1 cm
\newcommand{\cut}[1]{{}}

\def\vy{\mbox{\boldmath{$y$}}}
\def\vb{\mbox{\boldmath{$b$}}}
\def\vtau{\mbox{\boldmath{$\tau$}}}
\def\vsigma{\mbox{\boldmath{$\sigma$}}}
\def\vs{\mbox{\boldmath{$s$}}}
\def\vomega{\mbox{\boldmath{$\omega$}}}
\def\vxi{\mbox{\boldmath{$\xi$}}}
\def\tL{{\tilde L}}
\def\tC{{\tilde C}}

\newcommand{\sign}{\mathrm{sign}}
\newcommand{\erfc}{\mathrm{erfc}}

\renewcommand{\setminus}{\smallsetminus}
\newcommand{\ham}{\mathcal{H}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% --------------------------------------------------- %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{document}

\title{Sparsely-spread CDMA - a statistical mechanics based analysis}

\author{Jack Raymond and David Saad}

\address{
Neural Computation Research Group, Aston University, Aston Triangle, Birmingham, B4  7EJ
}
\ead{jack.raymond@physics.org}


--- START OF DOCUMENT TAIL ---
 be practical points for future implementation. There are
practical advantages of the sparse case over dense and orthogonal
codes in some regimes. The sparse CDMA method is likely to be
particularly useful in frequency-hopping and time-hopping code
division multiple access (FH and TH -CDMA) applications where the
effect of these practical limitations is less emphasised.

Extensions based on our method to cases without power control or
synchronisation have been attempted and are quite difficult. A
consideration of priors on the inputs, in particular the effects
when sparse CDMA is combined with some encoding method may also be
interesting.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ack Support from EVERGROW, IP No.~1935 in FP6 of the EU is
gratefully acknowledged. DS would like to thank Ido Kanter for
helpful discussions.


\section*{Bibliography}
\bibliographystyle{unsrt}
\bibliography{Bibliography}

\end{document}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1694
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: nice_PIR_limits.tex|>

\documentclass[times, 11pt]{article}
\usepackage{latex8}
\usepackage{times}
\usepackage{amsmath}
\usepackage{amssymb}
\input{macros}
\pagestyle{empty}


\begin{document}

\title{Locally Decodable Codes From Nice Subsets of Finite Fields  \\
       and Prime Factors of Mersenne Numbers}
\author{Kiran S. Kedlaya \\ MIT \\ kedlaya@mit.edu \and Sergey Yekhanin \\ MIT \\
yekhanin@mit.edu} \maketitle \thispagestyle{empty}



--- START OF DOCUMENT TAIL ---
mand{\Col}{\mathrm{Col}}
\newcommand{\Supp}{\mathrm{Supp}}

\newcommand{\accept}{\mathtt{accept}}
\newcommand{\reject}{\mathtt{reject}}
\newcommand{\fail}{\mathtt{fail}}
\newcommand{\halt}{\mathtt{halt}}


\newcommand{\HFam}{\mathcal{H}}
\newcommand{\FFam}{\mathcal{F}}
\newcommand{\Dom}{\mathcal{D}}
\newcommand{\Rng}{\mathcal{R}}

\newcommand{\Hall}{\mathrm{H}}
\newcommand{\Hmin}{\mathrm{H}_{\infty}}
\newcommand{\HRen}{\mathrm{H}_2}
\newcommand{\HSha}{\mathrm{H}_{\mathit{Sh}}}
\newcommand{\Ext}{\mathrm{Ext}}
\newcommand{\Con}{\mathrm{Con}}
\newcommand{\Samp}{\mathrm{Smp}}
\newcommand{\Enc}{\mathrm{Enc}}
\newcommand{\Code}{\mathcal{C}}

\newcommand{\zigzag}{\mathbin{\raisebox{.2ex}{
      \hspace{-.4em}$\bigcirc$\hspace{-.75em}{\rm z}\hspace{.15em}}}}

\newcommand{\eps}{\varepsilon}
\newcommand{\ci} {\stackrel{\rm{c}}{\equiv}}
\newcommand{\Time}{\mathrm{time}}
\newcommand{\inner}[2]{\left[#1,#2\right]}

\newcommand{\GL}{\operatorname{GL}}
\newcommand{\maj}{\operatornamewithlimits{maj}}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2048
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: gray_avoid_TCS42.tex|>
\documentclass[10pt]{amsart}
\usepackage{amssymb,latexsym,graphics}
%\usepackage{psfig}
\def\1a{{\mathbf 1}}
\def\2a{{\mathbf 2}}
\def\3a{{\mathbf 3}}
\def\4a{{\mathbf 4}}
\def\5a{{\mathbf 5}}
\def\6a{{\mathbf 6}}

\AtBeginDocument{
  \renewcommand{\labelitemii}{\(\blacklozenge\)}
  \renewcommand{\labelitemiii}{\ding{227}}
  \renewcommand{\labelitemiv}{\ding{70}}
}



\numberwithin{equation}{section}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{fact}[theorem]{Fact}
\newtheorem{example}[theorem]{Example}
\newtheorem{axiom}[theorem]{Axiom}
\newtheorem{property}[theorem]{Property}
\newtheorem{problem}[theorem]{Problem}
\newtheorem{notation}[theorem]{Notation}

\newcommand{\Sch}{\mathcal{S}}
\newcommand{\D}{\mathcal{D}}
\newcommand{\ee}{\mathsf{e}}
\newcommand{\dd}{\mathsf{d}}
\newcommand{\uu}{\mathsf{u}}
\newcommand{\rr}{\mathsf{r}}

\newcommand\GETOUT[1]{}
\pagenumbering{arabic}
\pagestyle{headings}

\newcommand{\s}{\mathfrak{S}}
\newcommand{\C}{\mathcal{C}}

\title[Combinatorial Gray codes for classes of permutations]{Combinatorial Gray codes for classes of pattern avoiding permutations}
\author{W.M.B. Dukes, M.F. Flanagan, T. Mansour and V. Vajnovszki}
\address{Science Institute, University of Iceland, Reykjav\'{i}k, Iceland.}
\email{dukes@raunvis.hi.is}
\address{Institute for Digital Communications, The University of Edinburgh, The King's Buildings, Mayfield Road, Edinburgh EH9 3JL, Scotland.}
\email{mark.flanagan@ieee.org}
\address{Department of Mathematics, University of Haifa, 31905 Haifa, Israel.}
\email{toufik@math.haifa.ac.il}
\address{LE2I UMR CNRS 5158, Universit\'e de Bourgogne B.P. 47 870, 21078 DIJON-Cedex France}
\email{vvajnov@u-bourgogne.fr}
\keywords{Gray codes, pattern avoiding permutations, generating algorithms}
\subjclass[2000]{Primary: 05A05, 94B25, Secondary: 05A15}
\begin{document}
\maketitle



--- START OF DOCUMENT TAIL ---
_93} Frank Ruskey, Simple combinatorial {G}ray codes constructed by reversing sublists,
in {\em ISAAC Conference, LNCS} {\bf 762} (1993) 201--208.

\bibitem{savage} Carla Savage, A Survey of Combinatorial Gray Codes, {\em SIAM Rev.} {\bf 39}:4 (1997) 605--629.

\bibitem{Vaj_02_1} Vincent  Vajnovszki, {G}ray visiting {M}otzkins,
{\em Acta Informatica} {\bf 38} (2002) 793-811.

\bibitem{Vaj_02_2}
Vincent Vajnovszki, A loopless algorithm for generating the
permutations of a multiset, {\em Theor. Comp. Sci.} {\bf 307} (2003)
415-431.

\bibitem{Wal_01} Timothy Walsh, {G}ray codes for involutions,
{\em J. Combin. Math. Combin. Comput.} {\bf 36} (2001) 95--118.

\bibitem{Wes_94} Julian West,
Generating trees and the {C}atalan and {S}chr\"oder numbers, {\em
Disc. Math.} {\bf 146} (1994) 247--262.

\bibitem{Weston_Vaj}
Mark Weston and Vincent Vajnovszki, Gray codes for necklaces and
Lyndon words of arbitrary base, {\em PuMA} {\bf17}(1-2) (2006)
175--182.
\end{thebibliography}



\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0994
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: Mediatic_Graphs.tex|>
\long\global\def\C#1\F{{}}
\documentclass[11pt]{article}
\usepackage{amsmath, amsthm, amssymb, graphicx, verbatim}
\setlength{\topmargin}{0cm}
\setlength{\headheight}{0cm}
\setlength{\headsep}{0cm}
\setlength{\textwidth}{15cm}
\setlength{\textheight}{9in}
\setlength{\footskip}{1.1cm}
\setlength{\oddsidemargin}{.3cm}
\setlength{\evensidemargin}{.3cm}
\usepackage[round]{natbib}
\swapnumbers
\input gen_macros_papers.dat
\begin{document}
\pagestyle{plain}

\title{\vspace*{-.5cm}\Huge Mediatic Graphs\thanks{We are grateful to David Eppstein for many useful exchanges pertaining to the results presented here.}}
\author{Jean-Claude Falmagne\thanks{Corresponding author: Dept. of Cognitive Sciences, University of California, Irvine, CA92697.} \hspace{4cm} Sergei Ovchinnikov\\
University of California, Irvine\hspace{2.3cm} San Francisco State University\\
\normalsize jcf@uci.edu\hspace{6cm}\normalsize sergei@sfsu.edu
}

\date{}
\maketitle

\thispagestyle{empty}

\vspace*{-.5cm}


--- START OF DOCUMENT TAIL ---
(1916)]{konig16}
\hspace*{-.7cm}D.~K{\"o}nig.
\newblock {{\"U}ber Graphen und ihren Anwendung auf Determinanten-theorie und
  Mengenlehre}.
\newblock \emph{Mathematische Annalen}, 77:\penalty0 453--465, 1916.

\bibitem[Ovchinnikov(2006{\natexlab{a}})]{ovchi06a}
\hspace*{-.7cm}S.~Ovchinnikov.
\newblock {Media theory: representations and examples}.
\newblock \emph{Discrete Applied Mathematics}, 2006.
\newblock Accepted for publication.

\bibitem[Ovchinnikov and Dukhovny(2000)]{ovchi00}
\hspace*{-.7cm}S.~Ovchinnikov and A.~Dukhovny.
\newblock {Advances in media theory}.
\newblock \emph{International Journal of Uncertainty, Fuzziness and
  Knowledge-Based Systems}, 8\penalty0 (1):\penalty0 45--71, 2000.
  
  \bibitem[Winkler(1984)]{winkl84}
\hspace*{-.7cm}P.M. Winkler.
\newblock {Isometric embedding in products of complete graphs}.
\newblock \emph{Discrete Applied Mathematics}, 7:\penalty0 221--225, 1984.
\end{itemize}
%\bibliography{grand}
%\bibliographystyle{plainnat}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1221
```latex
--- START OF DOCUMENT HEAD ---
mark}{\vskip 12pt \noindent {\bf Remark}\rm}{}
\newenvironment{opmerking}{\vskip 12pt \noindent {\bf Opmerking.}\rm}{}

\def\refe#1{(\ref{#1})}
\newcommand{\df}{\sl}  % or {\it}, for `new' notions
\newcommand{\X}[1]{X_{\textstyle \! \mbox{\small $#1$}}}
% \newcommand{\eqref}[1]{$(\mbox{\rm \ref{#1}})$}

\newcommand{\T}{{\mathbb T}}
\newcommand{\mP}{{\mathbb{P}}}
\newcommand{\Q}{{\mathbb Q}}
\newcommand{\R}{{\mathbb R}}
\newcommand{\C}{{\mathbb C}}
\newcommand{\N}{{\mathbb N}}
\newcommand{\Z}{{\mathbb Z}}
\newcommand{\D}{{\mathbb{D}}}

%\newcommand{\im}{{\rm{Im}}}
%\newcommand{\re}{{\rm{Re}}}
\newcommand{\I}{{\rm{I}}}
\usepackage{amsfonts}

\newcommand{\gl}{\operatorname{gl}}
\newcommand{\GL}{\operatorname{GL}}
\newcommand{\codim}{\operatorname{codim}}
\newcommand{\orb}{\mathcal{O}}
\newcommand{\comp}{{\scriptscriptstyle \circ}}
\newcommand{\KAM}{\textsc{kam}\ }
\newcommand{\lcu}{\textsc{lcu}\ }

\newcommand{\x}{{\mathsf x}}
\newcommand{\y}{{\mathsf y}}
\newcommand{\z}{{\mathsf z}}

%%%
%my article style
% This file is called `myarticle.sty'

%equations numbered per sections:
\numberwithin{equation}{section}
%%%%%%%%%%%%
\newenvironment{proof}{{\bf Proof.}\;\;}{{\hspace*{\fill}$\Box$}}

%\newenvironment{remark}{\vskip 8pt \noindent {\bf Remark.}\rm}{\vskip 8pt}
%\newenvironment{remarks}{\vskip b8pt \noindent {\bf Remarks.}\rm \begin{itemize}}{\end{itemize}}

\newtheorem{definition}{Definition}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{conjecture}{Conjecture}
\newtheorem{claim}{Claim}
\newtheorem{remark}{Remark}

\newtheorem{ex}{Example}
\newenvironment{example}{\begin{ex}\em}{\end{ex}}

\newcommand{\breukje}[2]{\mbox{\small $\frac{#1}{#2}$}}
\newcommand{\inprod}[2]{\langle #1\,,#2 \rangle}
\newcommand{\dbrak}[2]{\langle\!\langle #1\,,#2 \rangle\!\rangle}
\newcommand{\partieel}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\halfje}{\breukje{1}{2}}
\newcommand{\eps}{\varepsilon}



\font\fr=eufm10  scaled \magstep 1   %Caracteres gticos.
\font\ddpp=msbm10  scaled \magstep 1  %Caracteres "doble palo".


%\setlength{\unitlength}{1cm}
\def\cal#1{\mathcal{#1}}
\def\V{{\cal V}}
\def\v{{\cal v}}
\def\l{\lambda}
\def\a{\alpha}
\def\b{\beta}
\def\t{\tau}
\def\s{\sigma}
\def\w{\omega}
\def\O{\Omega}
\def\G{\Gamma}
\def\g{\gamma}
\def\d{\delta}
\def\e{\epsilon}
\def\T{{\mathbf T}}
\def\an{\Lambda} %Anchor map of the control derivative
\def\kegel#1{VR(#1)}
\def\ekegel#1{VR^e(#1)}
\def\cinfty#1{C^{\scriptscriptstyle\infty}(#1)}
\def\vectorfields#1{{\cal X}(#1)}
\def\vvectorfields#1{{\cal V}(#1)}
\def\voneforms#1{{\cal V}^*(#1)}
\def\forms#1#2{{\bigwedge}^{#1}(#2)}
\def\lie#1{{\cal L}_{#1}}
\def\fpd#1#2{\frac{\partial #1}{\partial #2}}
\def\R{{\rm I\kern-.20em R}}
\def\F{{\rm I\kern-.20em F}}
\def\del{\nabla}
\def\ovl#1{\overline{#1}}
\def\wht#1{\widehat{#1}}
\def\tilde#1{\widetilde{#1}}
\def\alg#1{\mbox{\fr #1}}

\def\vf#1{\frac{\partial}{\partial{#1}}}
\def\half{\mbox{$\frac{1}{2}$}}

\DeclareMathOperator{\sign}{sgn} \DeclareMathOperator{\spn}{span}
\DeclareMathOperator{\dom}{dom} \DeclareMathOperator{\im}{im}
\def\rel#1#2{#1 \leftrightarrow #2}
\def\ot{\leftarrow}

\def\bea{\begin{eqnarray*}}
\def\eea{\end{eqnarray*}}
\def\liea#1{{\cal L}(#1)}
\def\p#1#2{#1_{\!{\scriptscriptstyle #2}}}
\def\fpdt#1#2#3{\frac{\partial^2 #1}{\partial #2 \partial #3}}
\def\oneforms#1{{\cal X}^*(#1)}
\def\lc{\Delta}
\def\ro{\rho}
\def\ka{\kappa}
\def\een{\mbox{id}}
\def\sign{\mathrm{sgn}}
\def\be{{\bf e}}
\def\L{{\bf L}}
\def\bw{{\pmb \omega}}
\def\k{{\bf k}}
\def\F{{\bf F}}
\def\ts{\textstyle}


\begin{document}
\title{Dynamics of the Tippe Top via Routhian Reduction}
\author{ M.C.~Ciocci$^1$ and B. Langerock$^2$ \\
\\
\parbox{12cm}{\small
$^1$ Department of Mathematics, Imperial College London, London SW7 2AZ, UK\\
\small
$^2$ Sint-Lucas school
of Architecture, Hogeschool voor Wetenschap \& Kunst, B-9000
Ghent, Belgium}
}
\maketitle



--- START OF DOCUMENT TAIL ---
qs2} is singular and a coordinate change is necessary. The characteristic polynomial written above is not singular. Indeed, we have that $T_{\ovl\varphi\ovl\varphi}(\theta_0)$ is proportional to $\sin^2\theta_0$ or that $\gamma$ is well-defined in the case $\sin\theta_0=0$. Similarly, we have that $\fpdt{T_1}{\dot{\ovl\varphi}}{\theta}(\theta_0)$ is proportional to $\sin\theta_0$, and $\beta$ is well-defined. If we now write the necessary and sufficient conditions for this polynomial to be Hurwitz~\cite{nagrath}, we obtain the conditions
\begin{align*}
   (\alpha+\gamma)>0, (\alpha+\gamma)(\alpha\gamma+\beta^2+\delta)-\delta\gamma>0 \mbox{ and } \delta \gamma >0.
\end{align*}
The first condition is trivially satisfied. We now show that the third condition $\delta> 0$ implies the second condition. We can rewrite the second condition as
\[
(1+\alpha/\gamma)(\alpha\gamma+\beta^2+\delta) > \delta,
\]
and this is valid if $\delta>0$ or if $\fpd{^2W}{\theta^2}(\theta_0)>0$. 
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2328
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: PiredduZanolin2.tex|>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%% This is a LaTeX file %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



\documentclass[12pt,twoside, reqno]{amsart}
\textheight=9.5truein \textwidth=6truein \oddsidemargin=0.5cm
\evensidemargin=0.5cm \setlength{\topmargin}{-.18in}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{mathrsfs}
\usepackage{eufrak}






\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}{Lemma}[section]
\newtheorem{corollary}{Corollary}[section]
\newtheorem{proposition}{Proposition}[section]
\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
\newtheorem{example}{Example}[section]
\newtheorem{remark}{Remark}[section]
\numberwithin{equation}{section}




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%% Special defintions used for this article
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\graphicspath{{./Figure/}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% This means that a sub-folder named "Figure"
% containing all the figures
% must be placed in the same folder
% containing the tex file of the article

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\def\stretchx{\Bumpeq{\!\!\!\!\!\!\!\!{\longrightarrow}}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%







\begin{document}


\title[Cutting Surfaces]
{Cutting surfaces and applications to periodic points and chaotic$-$like dynamics
{{ \footnote{\tiny{This work has been supported by the project
"Equazioni Differenziali Ordinarie e Applicazioni" (PRIN 2005).}}{$\;^1$}}}}
\author[M. Pireddu, F. Zanolin]
{Marina Pireddu and Fabio Zanolin}





\noindent


--- START OF DOCUMENT TAIL ---
{Sharkovskii's theorem for
multidimensional perturbations of one-dimensional maps},
\textit{Ergodic Theory Dynam. Systems} \textbf{19} (1999),
1655--1684.


\bibitem{Zg-01}
\textsc{P. Zgliczy\'nski}, {On periodic points for systems of
weakly coupled 1-dim maps}, \textit{Nonlinear Anal. Ser. A: Theory
Methods} \textbf{46} (2001), 1039--1062.


\bibitem{ZgGi-04}
\textsc{P. Zgliczy\'nski \and M. Gidea}, {Covering relations for
multidimensional dynamical systems}, \textit{J. Differential
Equations} \textbf{202 } (2004), 32--58.

\end{thebibliography}

\bigskip

\bigskip

\noindent
\address{
$~$
\\
{
\textsc{Fabio Zanolin}\\
University of Udine, Department of Mathematics and Computer Science,\\
via delle Scienze 206, 33100 Udine, Italy.
\\
mailto: \itshape{zanolin@dimi.uniud.it}}
\\
$~$
\\
{
\textsc{Marina Pireddu}\\
University of Udine, Department of Mathematics and Computer Science,\\
via delle Scienze 206, 33100 Udine, Italy.
\\
mailto: \itshape{pireddu@dimi.uniud.it}}
}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1411
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: tcq_short.tex|>
\documentclass[twoside]{IEEEtran}

\usepackage[dvips]{graphicx}
\usepackage{subfigure}
\usepackage{amsmath}
\usepackage{amssymb}

\newcommand{\TCM}{Trellis-Coded Modulation}
\newcommand{\tcm}{trellis-coded modulation}
\newcommand{\TCQ}{Trellis-Coded Quantization}
\newcommand{\tcq}{trellis-coded quantization}
\newcommand{\TCQr}{Trellis-Coded Quantizer}
\newcommand{\tcqr}{trellis-coded quantizer}
\newcommand{\hd}{Hamming-distance}
\newcommand{\ed}{Euclidean-distance}
\newcommand{\od}{one-di\-men\-sional}
\newcommand{\td}{two-di\-men\-sional}



\begin{document}
\title{{\TCQ} Based on Maximum-Hamming-Distance Binary Codes}

\author{Lorenzo~Cappellari,~\IEEEmembership{Member,~IEEE}%
\thanks{L.~Cappellari is with the Dept.~of Information Engineering of the University of Padova, Italy.}}

\maketitle



--- START OF DOCUMENT TAIL ---
erving labeling} of the extended codebook with maximum-{\hd} convolutional codes. In this way, the relation between the minimum distance of the feasible reconstructed sequences and the {\hd} of the underlying convolutional code is exposed. 

Results show that it is possible and somewhat advantageous to conduct the search for good trellis codes into the binary domain, i.e.~to look for \emph{good} convolutional codes. In fact, the codes found are competitive with or somewhat better than the ones in literature. In the $\mathbb{Z}/4\mathbb{Z}$ case better codes have been found for the $16$, $64$, and $256$ states case, while in the $\mathbb{Z}^2/2\mathbb{Z}^2$ case better codes have been found for the $16$, $32$, $64$, and $256$ states cases. In addition, a $1024$ states code is given that, according to the authors' knowledge, was never published before in the context of TCQ.

\bibliographystyle{IEEEtran.bst}
\bibliography{IEEEabrv,nonIEEEabrv,refs_TCQ,refs_DSC,refs_books}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2055
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: bird.tex|>
\documentclass{amsart}
\usepackage{amsfonts,amsthm,amssymb,euscript}
%\usepackage[pdftex]{graphicx}
\usepackage{graphics}
\usepackage[matrix,arrow]{xy}

%\input{theorems}
%
%------------------------ Theorem environments ------------------------------
%
\newtheoremstyle{my}{1.5em}{0.5em}{\em}{}{\sc}{:}{0.5em}{}
% #1 = name
% #2 = preskip
% #3 = postskip
% #4 = bodyfont
% #5 = noindent?
% #6 = headfont
% #7 = headpunct, e.g. "."
% #8 = labelsep (between label and statement}
% #9 = apparently overrides the whole header

\theoremstyle{my}
\newtheorem{thm}{Theorem}
\numberwithin{thm}{section}
\numberwithin{equation}{section}
\newtheorem{theorem}[thm]{Theorem}
\newtheorem*{theorem*}{Theorem}
\newtheorem{cor}[thm]{Corollary}
\newtheorem{corollary}[thm]{Corollary}
\newtheorem*{corollary*}{Corollary}
\newtheorem{lemma}[thm]{Lemma}
\newtheorem{sublemma}[thm]{Sublemma}
\newtheorem{addendum}[thm]{Addendum}
\newtheorem{prop}[thm]{Proposition}
\newtheorem{proposition}[thm]{Proposition}
\newtheorem{conjecture}[thm]{Conjecture}
\newtheorem*{conjecture*}{Conjecture}
\newtheorem{question}[thm]{Question}
\newtheorem*{question*}{Question}
\newtheorem{defn}[thm]{Definition}
\newtheorem{definition}[thm]{Definition}
\newtheorem{definitions}[thm]{Definitions}
\newtheorem*{definitions*}{Definitions}
\newtheorem{rem}[thm]{Remark}
\newtheorem*{rem*}{Remark}
\newtheorem{remark}[thm]{Remark}
\newtheorem{assumption}[thm]{Assumption}
\newtheorem{background}[thm]{Background}
\newtheorem{listthm}[thm]{List}
\newtheorem*{remark*}{Remark}
\newtheorem{remarks}[thm]{Remarks}
\newtheorem*{remarks*}{Remarks}
\newtheorem*{example*}{Example}
\newtheorem{example}[thm]{Example}
\newtheorem*{examples*}{Examples}
\newtheorem{examples}[thm]{Examples}

\newcommand{\acknowledgments}{{\em Acknowledgments.} }

%-------------------------------- standard macros -----------------------------
%\input{standard}

\newcommand{\R}{\mathbb{R}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\half}{{\textstyle\frac{1}{2}}}
\newcommand{\quarter}{{\textstyle\frac{1}{4}}}

\newcommand{\iso}{\cong}           %isomorphism sign
\newcommand{\htp}{\simeq}          %homotopy sign
\newcommand{\smooth}{C^\infty}
\newcommand{\CP}[1]{\C {\mathrm P}^{#1}}
\newcommand{\RP}[1]{\R {\mathrm P}^{#1}}
\newcommand{\leftsc}{\langle}
\newcommand{\rightsc}{\rangle}
\newcommand{\Rgeq}{\R^{\scriptscriptstyle \geq 0}}
\newcommand{\Rleq}{\R^{\scriptscriptstyle \leq 0}}
\newcommand{\suchthat}{\; : \;}

\newcommand{\id}{\mathit{id}}
\newcommand{\re}{\mathrm{re}}
\newcommand{\im}{\mathrm{im}}
\newcommand{\mymod}{\quad\text{mod }}
\newcommand{\Hom}{\mathit{Hom}}
\newcommand{\End}{\mathit{End}}

\renewcommand{\o}{\omega}
\renewcommand{\O}{\Omega}
\newcommand{\Aut}{Aut}
\newcommand{\Ham}{Ham}
\newcommand{\Symp}{Symp}
\newcommand{\Diff}{\textit{Diff}\,}

%-------------------------------------- paper-specific macros --------------------------
\parskip1em
\parindent0em
\renewcommand{\thesubsection}{\arabic{section}\alph{subsection}}
\renewcommand{\subsection}[1]{\hspace{-\parindent}\refstepcounter{subsection}{\bf
(\arabic{section}\alph{subsection}) #1:}}

%
\newcommand{\scrL}{\mathcal{L}}
\newcommand{\scrK}{\mathcal{K}}
\newcommand{\scrM}{\mathcal{M}}
\newcommand{\K}{\mathbb{K}}
\newcommand{\gapprox}{\gtrsim}
\newcommand{\F}{\mathcal{F}}
\newcommand{\maurercartan}{\mathcal{MC}}
\newcommand{\scrH}{\mathcal{H}}
%------------------------------------------------------------------------------------------------

\title{A biased view of symplectic cohomology}
\author{Paul Seidel}
\date{April 13, 2007}
\begin{document}
\maketitle
\tableofcontents
\newpage

\section{Introduction}

Symplectic cohomology is an invariant of a certain kind of symplectic manifolds (open, or with boundary). It is comparatively easy to define, being a variation on classical Hamiltonian Floer homology. Moreover, its behaviour reflects important aspects of symp

--- START OF DOCUMENT TAIL ---
1, 2005.

\bibitem{viterbo97b}
C.~Viterbo.
\newblock Functors and computations in {F}loer homology with applications,
  {P}art {II}.
\newblock Preprint 1996.

\bibitem{viterbo94}
C.~Viterbo.
\newblock Exact {L}agrangian submanifolds, periodic orbits and the cohomology
  of free loop space.
\newblock {\em J. Differential Geom.}, 47:420--468, 1997.

\bibitem{viterbo97a}
C.~Viterbo.
\newblock Functors and computations in {F}loer homology with applications,
  {P}art {I}.
\newblock {\em Geom. Funct. Anal.}, 9:985--1033, 1999.

\bibitem{weber06}
J.~Weber.
\newblock Three approaches towards {F}loer homology of cotangent bundles.
\newblock {\em J. Symplectic Geom.}, 3:671--701, 2005.

\bibitem{weinberger}
S.~Weinberger.
\newblock {\em Computers, Rigidity, and Moduli}.
\newblock Princeton University Press, 2005.

\bibitem{weinstein91}
A.~Weinstein.
\newblock Contact surgery and symplectic handlebodies.
\newblock {\em Hokkaido Math. J.}, 20:241--251, 1991.

\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1526
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: lmov.tex|>
\documentclass[12pt]{article}
\usepackage[dvips]{graphicx}
\usepackage{pp,psfrag,rotating,hyperref}

\newcommand{\cL}{\mathcal{L}}
\newcommand{\hF}{\hat{F}}
\newcommand{\hZ}{\hat{Z}}
\newcommand{\hG}{\hat{G}}
\newcommand{\hH}{\hat{H}}
\newcommand{\fS}{\mathfrak{S}}
\newcommand{\fP}{\mathfrak{P}}
\newcommand{\Tr}{\mathrm{Tr}}
\newcommand{\bQ}{\mathbb{Q}}

\title{Proof of the Labastida-Mari\~{n}o-Ooguri-Vafa Conjecture}
\author{Kefeng Liu and Pan Peng}
\date{}

%%%%%%%%%%%%%%%

\newtheorem*{lmovconj}{Conjecture (LMOV)}

\DeclareMathOperator{\lk}{lk}
\newcommand{\chR}{\check{\mathcal{R}}}
\newcommand{\fsl}{\mathfrak{sl}}
\newcommand{\fu}{\mathfrak{u}}
\newcommand{\Mbar}{\overline{M}}

\def\mathcenter#1{%
  \vcenter{\hbox{#1}}%
}

%\newcommand{\mfig}[2][]{
%       \mathcenter{\includegraphics[#1]{#2}}
%}

\input{YoungDiagram.tex}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{document}
\maketitle



--- START OF DOCUMENT TAIL ---
ssiliev,
\emph{``Cohomology of knot spaces''}, 
\emph{Theory of singularities and its applications}, 
Advances in Soviet Mathematics, vol. 1, Amer. Math. Soc., Providence,
RI, 1990, 23.

\bibitem{W1} E. Witten, 
\emph{``Quantum field theory and the Jones polynomial''}, 
Commun. Math. Phys. 121 (1989) 351.

\bibitem{W2} E. Witten, 
\emph{``Chern-Simons gauge theory as a string theory''}, 
arxiv.org: hel-th/9207094, in \emph{The Floer memorial volume}, 
The Floer memorial volume,  637, Progr. Math., 133, 
Birkh�0�1user, Basel, 1995.

\bibitem{Yamaguchi-Yau} S. Yamaguchi and S.-T. Yau, 
\emph{``Topological string partition functions as polynomials''}, 
J. High Energy Phys.  2004,  no. 7, 047, 20 pp.

\bibitem{Zheng} H. Zheng, 
\emph{``Proof of the volume conjecture for Whitehead doubles of a family of
torus knots''}, arxiv.org: math.GT/0508138.

\bibitem{Z1} J. Zhou, \emph{Hodge integrals, Hurwitz numbers, and Symmetric
Groups}, preprint, arxiv.org: math.AG/0308024.

\end{thebibliography}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0022
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: gsdes.tex|>
\documentclass[final]{siamltex}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{graphicx}
\usepackage{amscd}
\newcommand*{\I}{{\mathsf{id}}}
\newcommand*{\G}{{\mathcal{G}}}
\newcommand*{\HH}{{\mathcal{H}}}
\newcommand*{\g}{{\mathfrak{g}}}
\newcommand*{\M}{{\mathcal{M}}}
\newcommand*{\R}{{\mathbb{R}}}
\newcommand*{\X}{{\mathfrak{X}}}
\newcommand*{\oo}{{\mathsf{o}}}
\newcommand*{\Ad}{{\mathrm{Ad}}}
\newcommand*{\ra}{{\rightarrow}}


\title{Stochastic Lie group integrators}
\author{Simon J.A. Malham\thanks{Maxwell Institute 
for Mathematical Sciences and School of Mathematical and Computer Sciences, 
Heriot-Watt University, Edinburgh EH14 4AS, UK. (\texttt{S.J.Malham@ma.hw.ac.uk},
\texttt{A.Wiese@hw.ac.uk}). (16/10/2007)} \and Anke Wiese$^\ast$}

\begin{document}
\maketitle
\label{firstpage}




--- START OF DOCUMENT TAIL ---
reprint, 2000.

\bibitem{S} \textsc{R.~S. Strichartz}, 
\emph{The Campbell--Baker--Hausdorff--Dynkin formula
and solutions of differential equations},
J. Funct. Anal., 72 (1987), pp.~320--345.

\bibitem{Su} \textsc{H.~J. Sussmann}, 
\emph{Product expansions of 
exponential Lie series and the discretization of
stochastic differential equations,
in Stochastic Differential Systems}, 
Stochastic Control Theory, and Applications, 
W.~Fleming and J.~Lions, eds.,
Springer IMA Series, Vol. 10 (1988), pp.~563--582.

\bibitem{V} \textsc{V.~S. Varadarajan}, 
\emph{Lie groups, Lie algebras, and their representations}, 
Springer, 1984.

\bibitem{W} \textsc{F.~W. Warner},
\emph{Foundations of differentiable manifolds and Lie groups},
Graduate Texts in Mathematics, Springer--Verlag, 1983.

\bibitem{Y} \textsc{Y.~Yamato}, 
\emph{Stochastic differential equations and nilpotent Lie algebras},
Z. Wahrsch. Verw. Gebiete, 47(2) (1979), pp~213--229.


\end{thebibliography}

\label{lastpage}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0283
```latex
--- START OF DOCUMENT HEAD ---
% <|FILE: mark_qalg.tex|>
%common header stuff

\documentstyle{amsppt}
%\input amsppt.sty
\baselineskip18pt
\magnification=\magstep1
%\NoPageNumbers
%\NoRunningHeads
%\pagewidth{4.5in}
%\pageheight{7.0in}
\pagewidth{30pc}
\pageheight{45pc}
%\hoffset .5in
%\hsize 6in

\hyphenation{co-deter-min-ant co-deter-min-ants pa-ra-met-rised
pre-print pro-pa-gat-ing pro-pa-gate
fel-low-ship Cox-et-er dis-trib-ut-ive}
\def\leaderfill{\leaders\hbox to 1em{\hss.\hss}\hfill}
\def\A{{\Cal A}}
\def\C{{\Cal C}}
\def\D{{\Cal D}}
\def\H{{\Cal H}}
\def\J{{\Cal J}}
\def\L{{\Cal L}}
\def\latl#1{{\Cal L}_L^{#1}}
\def\latr#1{{\Cal L}_R^{#1}}
\def\Pl{{\Cal P}}
\def\Sy{{\Cal S}}\
\def\TL{{\Cal T}\!{\Cal L}}
\def\ldescent#1{{\Cal L (#1)}}
\def\rdescent#1{{\Cal R (#1)}}
\def\lcell#1{{{\bold L}(#1)}}
\def\rcell#1{{{\bold R}(#1)}}
\def\tcell#1{{{\bold T}(#1)}}
\def\lem{\le^M}
\def\simm{\sim^M}
\def\afn{{\text {\bf a}}}
\def\tr{{\text {\rm tr}}}
\def\Co{\text {\rm Co}}
\def\cm{\text {\ cm}}
\def\met{\text {\ m}}
\def\cmps{\text {\ cm\ s}}
%\def\qed{\hfill\vrule height4pt width3pt depth2pt}
\def\idest{i.e.,\ }
\def\wh{\widehat}
\def\ti{\widetilde}
\def\a{{\alpha}}
\def\be{{\beta}}
\def\g{{\gamma}}
\def\G{{\Gamma}}
\def\d{{\delta}}
\def\De{{\Delta}}
\def\e{{\varepsilon}}
\def\z{{\zeta}}
\def\th{{\theta}}
\def\i{{\iota}}
\def\k{{\kappa}}
\def\l{{\lambda}}
\def\m{{\mu}}
\def\s{{\sigma}}
\def\t{{\tau}}
\def\w{{\omega}}
\def\ephi{{\varphi}}
\def\E{{\widehat E}}
\def\P{{\widetilde P}}
\def\Q{{\widetilde Q}}
\def\T{{\widetilde T}}
\def\te{\widetilde t}
\def\O{{\widehat O}}
\def\W{{\widehat W}}
\def\tmu{\tilde{\mu}}
\def\tem{\tilde{M}}
\def\ba{{\bold a}}
\def\bb{{\bold b}}
\def\bc{{\bold c}}
\def\bd{{\bold d}}
\def\bF{{\bold F}}
\def\bi{{\bold i}}
\def\bj{{\bold j}}
\def\bk{{\bold k}}
\def\bm{{\bold m}}
\def\bn{{\bold n}}
\def\wbn{{\widehat{\bold n}}}
\def\bp{{\bold p}}
\def\bq{{\bold q}}
\def\br{{\bold r}}
\def\bs{{\bold s}}
\def\bt{{\bold t}}
\def\bu{{\bold u}}
\def\bv{{\bold v}}
\def\bw{{\boldsymbol \omega}}
\def\bx{{\bold x}}
\def\BB{{\bold B}}
\def\uu{{\underline u}}
\def\uv{{\underline v}}
\def\brr{{\bar r}}
\def\b0{\text{\bf 0}}
\def\wrho{{\widehat \rho}}
\def\ra{{\ \longrightarrow \ }}
\def\sra{{\rightarrow}}
\def\ora{\overrightarrow}
\def\cast{\circledast}
\def\ds{\displaystyle}
%\def\lim#1{{{\text{\rm \, lim}} \atop {_{#1}}}}
\def\rad{\text{\rm \, rad}}
\def\arg{\text{\rm \, arg}}
\def\smod{\text{\rm \, mod \ }}
\def\char{\text{\rm \, char}}
\def\cosec{\text{\rm \, cosec }}
\def\cot{\text{\rm \, cot }}
\def\sp{\text{\rm \, span }}
\def\hei{\text{\rm \, ht }}
\def\supp{\text{\rm \, supp}}
\def\aut{\text{\rm \, Aut}}
\def\coker{\text{\rm \, coker}}
\def\adj{{\text {\rm \, adj\,}}}
\def\coms{\text{\rm Co}(X, S)}
\def\cjs#1{{\cos #1 + \j \sin #1}}
\def\cmjs#1{{\cos #1 - \j \sin #1}}
\def\exp#1{{e^{#1}}}
\def\varexp{\text{\rm exp}}
\def\lan{{\langle}}
\def\ran{{\rangle}}
\def\lal{{\langle\langle}}
\def\rar{{\rangle\rangle}}
\def\lrt#1#2{\left\langle {#1}, {#2} \right\rangle}
\def\lrh#1#2{\left\langle {#1}, {#2} \right\rangle_\H}
\def\wf{{\widehat F}}
\def\extln{{{\Cal D}(\widehat A_{n-1})}}
\def\extll{{{\Cal D}(\widehat A_l)}}
\def\tln{{TL(\widehat A_n)}}
\def\tll{{TL(\widehat A_l)}}
\def\otll{{O(\widehat A_l)}}
\def\annn{\text{\rm Ann({\bf n})}}
\def\ct{{\Bbb C \Bbb T}}
\def\dt{{\Bbb D \Bbb T}}
\def\qv{{{\Bbb Q}(v)}}
\def\ugn{{U(\widehat{{\frak g \frak l}_n})}}
\def\usn{{U(\widehat{{\frak s \frak l}_n})}}
\def\ugln{{U({\frak g \frak l}_n})}
\def\usln{{U(\frak s \frak l_n)}}
\def\sln{{\frak s \frak l_n}}
\def\sqnr{{\widehat S_q(n, r)}}
\def\ct{{\Bbb C \Bbb T}}
\def\dt{{\Bbb D \Bbb T}}
\def\real{{\Bbb R}}
\def\complex{{\Bbb C}}
\def\zed{{\Bbb Z}}
\def\kyu{{\Bbb Q}}
\def\enn{{\Bbb N}}
\def\j{\text{\rm j}}
\def\Re{\text{\rm Re}}
\def\Im{\text{\rm Im}}
\def\End{\text{\rm End}}
\def\Hom{\text{\rm Hom}}
\def\labt{{\Bbb L \Bbb T}}
\def\du{{\text{ d}u}}
\def\dx{{\text{ d}x}}
\def\dy{{\text{ d}y}}
\def\dtee{{\text{ d}t}}
\def\dee{{\text{ d}}}
\def\ddx{{\text{d} \over {\te

--- START OF DOCUMENT TAIL ---
d and Kinokuniya
\publaddr Tokyo and Amsterdam
\yr 1985
\pages 255--287
\endref

\ref\key{{\bf 22}}
\by B.G. Seifert
\paper The spherical trace on inductive limits of Hecke algebras of type 
$A$, $B$, $C$, $D$ and factors
\jour Quart J. Math.
\vol 41 \yr 1990 \pages 109--126
\endref

\ref\key{{\bf 23}}
\by J.Y. Shi
\paper Fully commutative elements and Kazhdan--Lusztig cells in the
finite and affine Coxeter groups, II
\jour Proc. Amer. Math. Soc.
\vol 133 \yr 2005 \pages 2525--2531
\endref

\ref\key{{\bf 24}}
\by J.R. Stembridge 
\paper On the fully commutative elements of Coxeter groups 
\jour J. Algebraic Combin.
\vol 5 
\yr 1996 
\pages 353--385
\endref

\ref\key{{\bf 25}}
\by H.N.V. Temperley and E.H. Lieb
\paper Relations between percolation
and colouring problems and other graph theoretical problems associated
with regular planar lattices: some exact results for the percolation
problem
\jour Proc. Roy. Soc. London Ser. A 
\vol 322 \yr 1971 \pages 251--280
\endref

\endRefs

\end
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2452
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: final.tex|>


\documentclass[conference]{IEEEtran}
\usepackage{cite}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{array}
\usepackage{amssymb,hhline,enumerate,dsfont}


\newtheorem{example}{Example}
\newtheorem{theorem}{Theorem}

\begin{document}

\title{Optimum Linear LLR Calculation for Iterative Decoding on Fading Channels}


\author{\authorblockN{Raman Yazdani, Masoud Ardakani}
\authorblockA{Department of Electrical and Computer Engineering,
University of Alberta\\
Edmonton, Alberta T6G 2V4, Canada\\
Email: \{yazdani, ardakani\}@ece.ualberta.ca} }


\maketitle



--- START OF DOCUMENT TAIL ---
es.

%On a Rayleigh
%channel, this improvement would become significant %(more than 1~dB)
%for code rates above 0.7 bits/channel use.

We then extended our approach to the cases that the additive noise
power of the fading channel is also unknown at the receiver. With a
careful choice of linear LLR calculation, we were able to obtain a
performance almost identical to the previous case, where the
additive noise power was known.

For applications that channel estimation results in significant
overheads or suffers from severe imperfections, our proposed
solution can be of interest.

While we verified some of our results through study and design of
LDPC codes on Rayleigh channel, our approach for maximizing the
achievable transmission rate and convergence range of the decoder is
general. The only reason for using LDPC codes is that, they can
approach theoretical limits and thus verify some of our asymptotic
results.

\bibliographystyle{IEEEtran}
\bibliography{IEEEabrv,ldpc}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1009
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: tehran.tex|>
% AMS-LaTeX Paper ************************************************
% **** -----------------------------------------------------------

\documentclass{amsart}
\usepackage{amssymb}
\usepackage{eucal}
\usepackage{amsfonts}
\usepackage{epsfig}
\usepackage{color}
\usepackage[frame,ps,dvips,matrix,arrow,curve,rotate]{xy}
% ----------------------------------------------------------------
\vfuzz2pt % Don't report over-full v-boxes if over-edge is small
\hfuzz2pt % Don't report over-full h-boxes if over-edge is small
% LABELS --------------------------------------------------------

\let\oldcite\cite                                  %   Comment this out

\newcommand{\separate}{{\center \rule{9cm}{0cm} \\ \rule{9cm}{0.5pt} \\
\rule{9cm}{0cm}}}


% THEOREMS -------------------------------------------------------
\newtheorem{thm}{Theorem}[section]
\newtheorem{cor}[thm]{Corollary}
\newtheorem{lem}[thm]{Lemma}
\newtheorem{prop}[thm]{Proposition}
\theoremstyle{definition}
\newtheorem{defn}[thm]{Definition}
\theoremstyle{remark}
\newtheorem{rem}[thm]{Remark}
\numberwithin{equation}{section} \theoremstyle{remark}
\newtheorem{ex}[thm]{Example}


% MATH -----------------------------------------------------------

\newcommand{\U}{\mathcal{U}}
\newcommand{\D}{\mathcal{D}}
\newcommand{\OO}{\mathcal{O}}
\newcommand{\F}{\mathcal{F}}
\newcommand{\G}{\mathcal{G}}
\newcommand{\T}{\mathcal{T}}

\newcommand{\C}{\mathsf{C}}
\newcommand{\B}{\mathsf{B}}
\newcommand{\A}{\mathsf{A}}

\newcommand{\bbX}{\mathbb{X}}
\newcommand{\bbY}{\mathbb{Y}}
\newcommand{\bbZ}{\mathbb{Z}}
\newcommand{\bbF}{\mathbb{F}}
\newcommand{\bbT}{\mathbb{T}}
\newcommand{\bbD}{\mathbb{D}}


\let\:=\colon


\newcommand{\al}{\alpha}
\newcommand{\be}{\beta}


\newcommand{\lra}{\longrightarrow}
\newcommand{\llra}[1]{\stackrel{#1}{\lra}}


\newcommand{\im}{\operatorname{im}}
\newcommand{\coker}{\operatorname{coker}}
\newcommand{\End}{\operatorname{End}}
\newcommand{\Hom}{\operatorname{Hom}}
\newcommand{\colim}{\operatorname{colim}}
\newcommand{\PreSh}{\mathbf{PreSh}}
\newcommand{\Sh}{\mathbf{Sh}}
\newcommand{\Spec}{\operatorname{Spec}}
\newcommand{\Ch}{\operatorname{Ch}}
\newcommand{\Tor}{\operatorname{Tor}}
\newcommand{\Ext}{\operatorname{Ext}}
\newcommand{\Cyl}{\operatorname{Cyl}}
\newcommand{\Cone}{\operatorname{Cone}}

\newcommand{\id}{\operatorname{id}}
\newcommand{\pr}{\operatorname{pr}}

\newcommand{\tul}[1]{\T^{\leq #1}}
\newcommand{\tug}[1]{\T^{\geq #1}}
\newcommand{\tdl}[1]{\T_{\leq #1}}
\newcommand{\tdg}[1]{\T_{\geq #1}}

\newcommand{\tauul}[1]{\tau^{\leq #1}}
\newcommand{\tauug}[1]{\tau^{\geq #1}}
\newcommand{\taudl}[1]{\tau_{\leq #1}}
\newcommand{\taudg}[1]{\tau_{\geq #1}}

\def\smashedlongrightarrow{\setbox0=\hbox{$\longrightarrow$}\ht0=1pt\box0}
\def\risom{\buildrel\sim\over{\smashedlongrightarrow}}
\def\smashedst{\setbox0=\hbox{$\rightrightarrows$}\ht0=4pt\box0}
\newcommand{\sst}[1]{\stackrel{#1}{\smashedst}}

\def\twomorphism{\setbox0=\hbox{$\Rightarrow$}\ht0=4pt\box0}
\newcommand{\twomor}[1]{\stackrel{#1}{\twomorphism}}


\newcommand{\torel}[1]{\stackrel{#1}{\to}}

% ------------------- Xy arrows ---------------------------------
\newcommand{\thar}[7]{\ar    #4  @{#1} @<0.5pt> [#5]   #6       % |!{[#9];[#10]}\hole
                      \ar    #4  @{#2}          [#5]   #6   #7     % |!{[#9];[#10]}\hole
                      \ar    #4  @{#3} @<-0.5pt> [#5]   #6        %  |!{[#9];[#10]}\hole
                                           }


\newcommand{\dashar}[3]{\thar{-}{-->}{-}{#1}{#2}{}{#3}}                % #1=extra leftt command   #2=direction
\newcommand{\perfar}[3]{\thar{-}{..>}{-}{#1}{#2}{}{#3}}                % #3=extra right command
\newcommand{\dentar}[3]{\thar{--}{>}{--}{#1}{#2}{}{#3}}
\newcommand{\thickar}[3]{\thar{-}{->}{-}{#1}{#2}{}{#3}}


% ------------------------------------------------------------
\begin{document}



\title[Lectures on derived and triangulated categories]
{Lectures on derived and triangulated categories}%
\author{Behrang N

--- START OF DOCUMENT TAIL ---
ive
  projective varieties}, J. Geom. Phys. \textsf{50}, no. 1-4, 162-187.

\bibitem[Pu]{Puppe} D.~Puppe, \emph{On the formal structure of
stable homotopy theory}, in \emph{Colloq. Alg. Topology}, Aarhus
University (1962), 65-71.

\bibitem[Ro]{Ro} A.~Rosenberg, \emph{The spectrum of abelian categories and
 reconstructions
 of schemes}, in \emph{Rings, Hopf Algebras, and Brauer groups},
 257--274, Lectures Notes in Pure and Appl. Math. 197, Marcel Dekker, New York,
 1998.

\bibitem[Ve]{Verdier} J.-L.~Verdier,  \emph{Des cat\'egories d\'eriv\'ees des
  cat\'egories ab\'eliennes}, Ast\'erisque  239,  1996.

\bibitem[We]{Weibel} C.~A.~Weibel, \emph{Introduction to homological algebra},
  Cambridge Studies in Advanced Mathematics 38, Cambridge University Press, 1994.

\end{thebibliography}
% ------------------------------------------------------------
% ------------------------------------------------------------
\end{document}
% ------------------------------------------------------------
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1818
```latex
--- START OF DOCUMENT HEAD ---
debit}{\ensuremath{X}}
\newcommand{\Infobit}{\ensuremath{Y}}
\newcommand{\Recbit}{\ensuremath{V}}


\newcommand{\numcodebit}{\ensuremath{n}}
\newcommand{\numinfobit}{\ensuremath{m}}
\newcommand{\mycode}{\ensuremath{\mathbb{C}}}


\newcommand{\acoeff}{\ensuremath{a}}
\newcommand{\bcoeff}{\ensuremath{b}}
\newcommand{\ccoeff}{\ensuremath{c}}

\newcommand{\mywei}{\ensuremath{w}}
\newcommand{\myweibar}{\ensuremath{\widetilde{\mywei}}}
\newcommand{\Qprob}{\ensuremath{\mathbb{Q}}}
\newcommand{\AvWtEnum}[1]{\ensuremath{\mathbb{A}_{#1}}}
\newcommand{\BouWtEnum}{\ensuremath{B}}
\newcommand{\AsympWtEnum}{\ensuremath{B}}



\newcommand{\delfun}[1]{\ensuremath{\delta^*(#1; \topdeg)}}
\newcommand{\tmpvar}{\ensuremath{t}}


\newcommand{\Tmpfun}{\ensuremath{g}}

\newcommand{\order}{\ensuremath{\mathcal{O}}}

\newcommand{\myrate}{\ensuremath{R}}


\newcommand{\lowcdeg}{\ensuremath{d'_c}}
\newcommand{\tstar}{\ensuremath{t^*}}

\newcommand{\mytvar}{\ensuremath{t}}

\newcommand{\mylam}{\ensuremath{\lambda}}

\newcommand{\ProofFun}{\ensuremath{K}}



\newcommand{\epsup}{\ensuremath{\epsilon_2}}
\newcommand{\epslow}{\ensuremath{\epsilon_1}}

\newcommand{\midWtEnum}{\ensuremath{\mathcal{A}_\midbit}}
%\newcommand{\midbit}{\ensuremath{m}}


\newcommand{\Wnoise}{\ensuremath{W}}
\newcommand{\wnoise}{\ensuremath{w}}
\newcommand{\myeps}{\ensuremath{\epsilon_\topbit}}

\newcommand{\Wzside}{\ensuremath{Z}}



\newcommand{\Kset}{\ensuremath{K}}
\newcommand{\mycodepar}{\ensuremath{\mycode(\Genmat, \Parmat_1)}}


\newcommand{\msca}{\ensuremath{\genericS{m}}}
\newcommand{\Msca}{\ensuremath{\genericS{M}}}

\newcommand{\Gpmess}{\ensuremath{\msca}}
\newcommand{\gpmsca}{\ensuremath{\msca}}



\newcommand{\Chaninput}{\ensuremath{V}}
\newcommand{\Chanoutput}{\ensuremath{Z}}
\newcommand{\Shost}{\ensuremath{S}}



\newcommand{\mycodegp}{\ensuremath{\mycode}}

\newcommand{\ustar}{\ensuremath{u^*}}

\newcommand{\ratesha}{\ensuremath{R_{\operatorname{Sha}}}}


\newcommand{\Complexnumc}{\ensuremath{T_\topbit(\Ssca, \mycode;
\distor)}}



\newcommand{\rvdistcom}{\ensuremath{d_\topbit(\Ssca, \mycode)}}

\newcommand{\mycodeldpc}{\ensuremath{\mycode_{\operatorname{LDPC}}}}

\newcommand{\mycodetop}{\ensuremath{\mycode_1}}
\newcommand{\mycodebot}{\ensuremath{\mycode_2}}
\newcommand{\mycodebarbot}{\ensuremath{\bar{\mycode}_2}}
\newcommand{\mycodebar}{\ensuremath{\bar{\mycode}}}

\newcommand{\mycodebarldpc}{\mycodebarbot}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\Yspace}{\ensuremath{\mathcal{Y}}}
\newcommand{\Sspace}{\ensuremath{\mathcal{S}}}


\newcommand{\mycond}[2]{\ensuremath{\mprob(#1 \mid #2)}}
\newcommand{\cond}{\mycond}
\newcommand{\xml}{\ensuremath{\widehat{x}}}
\newcommand{\yhat}{\ensuremath{\widehat{Y}}}
\newcommand{\shat}{\ensuremath{\widehat{S}}}

%\newcommand{\mycode}{\ensuremath{\mathbb{C}}}
\newcommand{\myxcode}{\ensuremath{\mathbf{x}}}
\newcommand{\myycode}{\ensuremath{\mathbf{y}}}
\newcommand{\myzcode}{\ensuremath{\mathbf{z}}}
\newcommand{\myxvec}{\ensuremath{\mathbf{X}}}
\newcommand{\myzvec}{\ensuremath{\mathbf{Z}}}
\newcommand{\myyvec}{\ensuremath{\mathbf{Y}}}
\newcommand{\myuvec}{\ensuremath{\mathbf{U}}}
\newcommand{\myvvec}{\ensuremath{\mathbf{V}}}
\newcommand{\mywvec}{\ensuremath{\mathbf{W}}}

\newcommand{\real}{\ensuremath{\mathbb{R}}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{document}
\begin{center}


{{\LARGE \bf{Low-density graph codes that are optimal for
source/channel coding and binning}}}

\begin{center}
\begin{tabular}{ccc}
Martin J. Wainwright & & Emin Martinian\\
%
Dept. of Statistics, and  & &   Tilda Consulting, Inc. \\
%
Dept. of Electrical Engineering and Computer Sciences  & & Arlington, MA \\
%
University of California, Berkeley & &  \texttt{emin@alum.mit.edu} \\
%
 \texttt{wainwrig@\{eecs,stat\}.berkeley.edu} & & 
\end{tabular}
\end{center}

\vspace*{.5in}

Technical Report 730, \\
Department of Statistics, UC Berkeley, \\
April 2007
\end{center}



--- START OF DOCUMENT TAIL ---
5}
M.~J. Wainwright and E.~Maneva.
\newblock Lossy source coding by message-passing and decimation over
  generalized codewords of {LDGM} codes.
\newblock In {\em International Symposium on Information Theory}, Adelaide,
  Australia, September 2005.
\newblock Available at arxiv:cs.IT/0508068.

\bibitem{WynerZiv76}
A.~D. Wyner and J.~Ziv.
\newblock The rate-distortion function for source encoding with side
  information at the encoder.
\newblock {\em IEEE Trans. Info. Theory}, IT-22:1--10, January 1976.

\bibitem{Yang05}
Y.~Yang, V.~Stankovic, Z.~Xiong, and W.~Zhao.
\newblock On multiterminal source code design.
\newblock In {\em Proceedings of the Data Compression Conference}, 2005.

\bibitem{Zamir02}
R.~Zamir, S.~S. (Shitz), and U.~Erez.
\newblock Nested linear/lattice codes for structured multiterminal binning.
\newblock {\em IEEE Trans. Info. Theory}, 6(48):1250--1276, 2002.

\end{thebibliography}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1033
```latex
--- START OF DOCUMENT HEAD ---
ackage{a4,fullpage,amssymb,epsf,psfrag,times}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{enumerate}
\usepackage{latexsym}
\usepackage{epsfig}
\usepackage{amsthm}  
\usepackage{amsmath}
\usepackage{amssymb} 
\usepackage{latexsym}
\usepackage{epsfig} 
\usepackage{amssymb,latexsym}
\usepackage[all]{xy}
%
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{enumerate}
\usepackage{latexsym}
\usepackage{epsfig}
\usepackage{amsthm}  
\usepackage{amsmath}
\usepackage{amssymb} 
\usepackage{latexsym}
\usepackage{epsfig} 

\renewcommand{\theequation}{\thesection.\arabic{equation}}
%\renewcommand{\thefigure}{\arabic{figure}}
\renewcommand{\thetable}{\thesection.\arabic{table}}
\makeatletter\@addtoreset{equation}{section}\makeatother
%\makeatletter\@addtoreset{figure}{section}\makeatother
\makeatletter\@addtoreset{table}{section}\makeatother
\def\niveau{section}


\newtheorem{conjecture}{Conjecture}[section]
\newtheorem{theorem}{Theorem}[section]
\newtheorem{prop}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{tablethm}[theorem]{Table}
\newtheorem{cor}[theorem]{Corollary}
\newtheorem{assumption}[theorem]{Assumption}
\newtheorem{assumptions}[theorem]{Assumptions}
\newtheorem{conclusions}[theorem]{Conclusions}

\newcommand{\sfrac}[2]{\mbox{$\frac{#1}{#2}$}}
\newcommand{\va}{\mbox{~~voor~alle~~}}
\newcommand{\Rl}{\mathop{{\rm Re}}\nolimits}
\newcommand{\Imag}{\mathop{{\rm Im}}\nolimits}
\newcommand{\R}{{\mathbb R}}
\newcommand{\C}{{\mathbb C}}
\newcommand{\Z}{{\mathbb Z}}
\newcommand{\Q}{{\mathbb Q}}
\newcommand{\N}{{\mathbb N}}
\newcommand{\T}{{\mathbb T}}
\newcommand{\D}{{\mathbb D}}
\newcommand{\norm}[1]{\| #1\|} 
\newcommand{\Cknorm}[1]{\norm{#1}_{_{C^k}}}
\newcommand{\kK}[1]{\norm{#1}_{_{C^k,\, K}}}

\newcommand{\op}[1]{\!\!\mathop{\rm ~#1}\nolimits}
\newcommand{\fop}[1]{\!\!\mathop{\mbox{\rm \footnotesize ~#1}}\nolimits}
\newcommand{\scriptop}[1]{\!\!\mathop{\mbox{\rm \scriptsize ~#1}}\nolimits}
\newcommand{\tinyop}[1]{\!\!\mathop{\mbox{\rm \tiny ~#1}}\nolimits}
\newcommand{\dd}[2]{\frac{\fop{d}\! #1}{\fop{d}\! #2}}

%%\newenvironment{proof}{\par\medskip\noindent{\bf Proof}~~}
%%{\unskip\nobreak\hfill\hbox{$\Box$}\par \bigskip}        

%\newcounter{exerc}[section]
%\renewcommand{\theexerc}{\thesection.\arabic{exerc}}
%\newenvironment{exerc}{\refstepcounter{exerc}\par\medskip\noindent{\bf Exercise~\theexerc~~}}{\unskip\nobreak\hfill\hbox{ $\oslash$}\par\bigskip}

%\newcounter{remark}[section]
%\renewcommand{\theremark}{\thesection.\arabic{remark}}
\newenvironment{remark}{\refstepcounter{theorem}\par\medskip\noindent{\bf Remark~\thetheorem~~}}{\unskip\nobreak\hfill\hbox{ $\oslash$}\par\bigskip}

\newenvironment{question}{\refstepcounter{theorem}\par\medskip\noindent{\bf Question~\thetheorem~~}}{\unskip\nobreak\hfill\hbox{ $\oslash$}\par\bigskip}

%\newcounter{example}[section]
%\renewcommand{\theexample}{\thesection.\arabic{example}}
\newenvironment{example}{\refstepcounter{theorem}\par\medskip\noindent{\bf Example~\thetheorem~~}}{\unskip\nobreak\hfill\hbox{ $\oslash$}\par\bigskip}

%\newcounter{definition}[section]
%\renewcommand{\thedefinition}{\thesection.\arabic{definition}}
\newenvironment{definition}{\refstepcounter{theorem}\par\medskip\noindent{\bf Definition~\thetheorem~~}}{\unskip\nobreak\hfill\hbox{ $\oslash$}\par\bigskip}

%\newcounter{condition}[section]
%\renewcommand{\thecondition}{\thesection.\arabic{condition}}
\newenvironment{condition}{\refstepcounter{theorem}\par\medskip\noindent{\bf Condition~\thetheorem~~}}{\unskip\nobreak\hfill\hbox{ $\oslash$}\par\bigskip}

%\newfont{\gothic}{eufm10 scaled\magstep0}
%\newcommand{\got}[1]{\mbox{\gothic #1}}
\newcommand{\got}[1]{\mathfrak{#1}}


\newenvironment{skproof}{\par\noindent\emph{{Sketch of Proof.}}}{
\unskip\nobreak\hfill\hbox{$\Box$}\par \bigskip}        

\begin{document}

\title{Topology of spaces\linebreak[1] of equivariant symplectic embeddings}
\date{}
\author{Alvaro Pelayo}

\maketitle




--- START OF DOCUMENT TAIL ---
rational 4-manifolds, {\it Duke Math. J.} {\bf
122} (2004), no. 2, 
347--397.

\bibitem{KT} Y. Karshon and S. Tolman, Centered complexity
one Hamiltonian torus actions, {\it Trans. Amer. Math. Soc.} {\bf 353} 
(2001), no. 12, 4831--4861 (electronic). 

\bibitem{KT2} Y. Karshon and S. Tolman, The Gromov width of complex Grasmannians,
{\it Alg. and Geom. Topol.}  {\bf 5} paper 38, 911--922.

\bibitem{M1} D. McDuff, From deformation to isotopy, 
{\it Topics in Symplectic $4$-manifolds}, Internat. Press,
Cambridge, MA (1998).

\bibitem{M2} D. McDuff, The structure of rational and ruled symplectic
$4$\--manifolds,  
{\it J. Amer. Math. Soc.} {\bf 3(3)} (1990) 679--712.


\bibitem{P2} A. Pelayo, Toric symplectic ball
packing, \emph{Top. and its Appl.} {\bf 153} (2006) 3633--3644. 

\end{thebibliography}

\noindent
A. Pelayo\\
Department of Mathematics, University of Michigan\\
2074 East Hall, 530 Church Street, Ann Arbor, MI 48109--1043, USA\\
e\--mail: apelayo@umich.edu



\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1313
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: Mutants-04-10-07.tex|>


\documentclass[12pt]{article}
\usepackage{amsmath,amssymb,amsfonts,epsfig}
%\baselineskip=20pt
%\hsize=340pt
%\vsize=490pt
\addtolength{\topmargin}{-67pt}
\addtolength{\textheight}{100pt}
\oddsidemargin=0pt
\textwidth=6in


\author{S.~V.~Chmutov\thanks{The Ohio State University, Mansfield.}, S.~K.~Lando
\thanks{Institute for System Research RAS and the Poncelet Laboratory, Independent
University of Moscow, partly supported by the grant
ACI-NIM-2004-243 (Noeuds et tresses), RFBR 05-01-01012-a, NWO-RFBR
047.011.2004.026 (RFBR 05-02-89000-NWOa), GIMP
ANR-05-BLAN-0029-01.}}

\title{Mutant knots and intersection graphs}
\date{April 10, 2007}

\usepackage{theorem}
%\usepackage{hyperref}

\def\smallX{{\bf \scriptsize X}}
\def\C{{\mathbb C}}
\def\R{{\bf R}}
\def\N{{\bf N}}
\def\X{{\bf X}}
\def\I{{\bf I}}
\def\Q{{\mathbb Q}}
\def\Z{{\mathbb Z}}
\def\a{{\bf a}}
\def\A{{\widehat{\cal P}}}
\def\B{{\cal B}}
\def\D{{\cal D}}
\def\P{{\cal P}}
\def\cC{{\cal C}}
\def\cA{{\cal A}}
\def\cF{{\cal F}}
\def\cH{{\cal H}}
\def\ocH{{\overline{{\cal H}}}}
\def\cG{{\cal G}}
\def\cL{{\cal L}}
\def\cM{{\cal M}}
\def\ocM{{\overline{{\cal M}}}}
\def\cO{{\cal O}}
\def\cR{{\cal R}}
\def\gR{{\mathfrak R}}
\def\cT{{\cal T}}
\def\cU{{\cal U}}
\def\ocU{{\overline{{\cal U}}}}
\def\f{{\tilde f}}
\def\V{{\tilde V}}
\def\cP{{\cal P}}
\def\T{{\widehat{\cal D}}}
\def\deg{{\rm deg}}
\def\Hom{{\rm Hom}}
\newcommand{\sL}{\mathfrak{sl}} % for the Lie algebra sl
\newcommand{\gl}{\mathfrak{gl}}
%\def\sl{{\rm sl}}
%\def\gl{{\rm gl}}
\def\tr{{\rm tr}}
\def\st{{\rm st}}
\def\discrim{{\rm discrim}}
\def\Aut{{\rm Aut}}
\def\LL{{\rm LL}}
\def\ch{{\rm ch}}
\def\oH{{\overline H}}

\def\p{{\partial}}

\def\td{{\rm td}}
\def\tLL{{\widehat{\rm LL}}}
\def\tH{{\widehat{\H}}}
\def\tS{{\widehat{\Sigma}}}
\def\tD{{\widehat{\Delta}}}
\def\CP{{\C P}}
\def\dim{{\rm dim}}
\def\barX{{\overline X}}
\def\barXX{{\bf \overline X}}

\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}

{\theorembodyfont{\rmfamily}    % No need in ``\rm'' command after ``\begin''
\newtheorem{remark}[theorem]{Remark}
\newtheorem{example}[theorem]{Example}
\newtheorem{definition}{Definition}
\newtheorem{problem}[theorem]{Problem}
}

% added by S.Ch 03.10.07 from cdbook
\newcommand{\rb}{\raisebox}
\newcommand{\ig}{\includegraphics}
\newcommand\risS[6]{\rb{#1pt}[#5pt][#6pt]{\begin{picture}(#4,15)(0,0)
  \put(0,0){\ig[width=#4pt]{#2.eps}} #3
     \end{picture}}}


%\include{epsf}

\begin{document}

\maketitle
%\tableofcontents



--- START OF DOCUMENT TAIL ---
oery. A volume dedicated to Professor Kunio Murasugi for his 70th birthday.
   Editors: M. Sakuma et al., Osaka University, March 2000. Preprint is available at
   \verb#http://www.f.waseda.jp/murakami/papers/finitetype.pdf#

\bibitem{V} A.~Vaintrob, {\it Vassiliev knot invariants and Lie
$S$-algebras}, Math. Res. Lett. {\bf 1}, no. 5, 579--595~(1994)

\bibitem{W} D.~J.~A.~Welsh, {\it Matroid theory}, Academic Press,
London (1976)

\end{thebibliography}

\end{document}


\bibitem{CDL2} S.~V.~Chmutov, S.~V.~Duzhin, S.~K.~Lando
   {\it Vassiliev knot invariants II. Intersection graph conjecture
   for trees}, Advances in Soviet Mathematics, {\bf 21}, 127-134~(1994)

\bibitem{MR} H.~R.~Morton, H.~J.~Ryder, {\it Mutants and ${\rm SU}(3)\sb q$
   invariants}.
   The Epstein birthday schrift, (electronic), Geom. Topol. Monogr., {\bf 1},
   Geom. Topol. Publ., Coventry 365--381~(1998).

\bibitem{N} W.~Naji,
{\it Reconnaissance des graphes de cordes}, Discrete Math., {\bf
54}, 329--337~(1985)
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2380
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: due-revised.tex|>
\documentclass[a4paper,11pt]{article}
\usepackage{amsmath,amsfonts,amsthm}
%\usepackage{showkeys}

\addtolength{\hoffset}{-0.75cm}
\addtolength{\textwidth}{1.5cm}
\addtolength{\voffset}{-0.5cm}
\addtolength{\textheight}{1cm}


\newtheorem{prop}{Proposition}[section]
\newtheorem{thm}[prop]{Theorem}
\newtheorem{lemma}[prop]{Lemma}
\newtheorem{defi}[prop]{Definition}
\theoremstyle{remark}
\newtheorem{rmk}[prop]{Remark}
\theoremstyle{definition}

\numberwithin{equation}{section}

\renewcommand{\P}{\mathbb{P}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\F}{\mathfrak{F}}
\renewcommand{\H}{\mathcal{H}}
\newcommand{\fH}{\mathfrak{H}}
\renewcommand{\L}{\mathcal{L}}
\newcommand{\erre}{\mathbb{R}}
\newcommand{\enne}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\renewcommand{\epsilon}{\varepsilon}
\newcommand{\ip}[2]{\langle#1,#2\rangle}
\newcommand{\bip}[2]{\Big\langle#1,#2\Big\rangle}
\newcommand{\ds}{\displaystyle}
\newcommand{\tr}{\mathop{\mathrm{Tr}}\nolimits}

\newsymbol\lesssim 132E

%\hyphenation{quad-rat-ic}

\title{Local well-posedness of Musiela's SPDE with L\'evy noise}

\author{Carlo Marinelli\thanks{Institut f\"ur Angewandte Mathematik,
    Universit\"at Bonn, Wegelerstr. 6, D-53115 Bonn, Germany. URL:
\texttt{http://www.uni-bonn.de/$\sim$cm788}}}

\date{\normalsize April 7, 2007. Revised April 21, 2008 and June 11, 2008.}




\begin{document}
\maketitle



--- START OF DOCUMENT TAIL ---
t''
space to study Musiela's SPDE, satisfying the minimum requirement that
its elements admit a continuous modification, and allowing at the same
time to obtain existence and uniqueness of global mild solutions. This
problem, to the best of our knowledge, is not solved also in the case
of Brownian noise.


\subsection*{Acknowledgments}
This work was partially supported by the DFG through the SFB 611,
Bonn, and by the ESF through grant AMaMeF 969. This work was carried
out while the author was visiting the Max-Planck-Institut f\"ur
Mathematik in Leipzig supported by an EPDI fellowship. The author is
sincerely grateful to S.~Albeverio for helpful discussions on some
parts of the paper, to two anonymous referees and to E.~Eberlein for
suggestions which led to improvements of the presentation.



\let\oldbibliography\thebibliography
\renewcommand{\thebibliography}[1]{%
  \oldbibliography{#1}%
  \setlength{\itemsep}{-1pt}%
}

\bibliographystyle{amsplain}
\bibliography{ref}


\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0542
```latex
--- START OF DOCUMENT HEAD ---
%%   For authorindex
\ifthenelse{\equal{\finalized}{no}}{
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Authorindex works only when you are using bibtex.   That is it needs
% bib file to look up.   
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage[editors,firstabbrev,miniindex]{authorindex}
%\usepackage{miniindex}
\usepackage{multicol}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% options: 
% editors	will cause the editor names to be included in the index
% avoideditors	will cause the editor names to be included only if author
% 		names are not present
% onlyauthors	(the default) will restrict index to author names
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% options: 
% lastname 	will only include last names of authors (and  titles like
%	"von" if present)
% firstabbrev	will also include the abbreviated first name(s) (and eventually
%	also a ``jr.''), following the last name
% fullname  (the default) will spell the names in full, to the extent given
%	in the .bib file
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\renewcommand{\cite}{\aicite}    % for purposes of authorindex
\renewcommand{\aisize}{\small}  % will cause author
				%index to be typeset in small size
\aisee{, see }% This is for the following purpose:
	%  e.g.  Wolfgang Pauli, \aisee Einstein (will appear in enc.ain)
	%  If you are using German, you would want ", siehe"
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%  authorindexcommands over %%%%%%%%%%%%%%%%%%%
}{\newcommand\bibindex[1]{\{\begin{bfseries}#1\end{bfseries}\}}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\typein[\includeonly]
%{Please enter the files to be included (for \protect\includeonly),  thank you:}
\includeonly{introduction,set-up,%
theorem,reduction,%
notation,further-red,%
odepth,pi,phi,lemmas,proof,%
interpretations,index,%
bibliography}
\begin{document}
\maketitle
\input{abstract}
\vfill\eject
\tableofcontents
\vfill\eject
\input{introduction}
%\input{erratum}
\mypart{The theorem}\mylabel{p.theorem}
Definitions are recalled, the problem formulated, and the theorem stated.
\input{set-up}
\input{theorem}
\mypart{From geometry to combinatorics}\mylabel{p.gtoc}
The problem is translated from geometry to combinatorics.
The main combinatorial results are formulated.
\input{reduction}
\input{further-red}
\mypart{The proof}\mylabel{p.proof}
The main combinatorial results formulated in~\S\ref{ss.p.main} are proved.   
An attempt is made to maintain parallelism with the proofs in~\cite{kr}.    
\input{notation}
\input{odepth}
\input{opi}
\input{ophi}
\input{lemmas}
\input{proof}
\mypart{An Application}\mylabel{p.app}
As an application of the main theorem (Theorem~\ref{t.main}),
an interpretation of the multiplicity is presented.
% In a later publication~\cite{ru},  another application
% will be presented, namely, the computation
% of the initial ideal, with respect to a certain monomial order, of the
% defining ideal of the tangent cone to the Schubert variety.
% Unlike in the Grassmannian and symplectic Grassmannian,  the
% natural set of generators of the ideal of the tangent cone do not
% form a Gr\"obner basis.    
\input{multiplicity}
%\input{groebner}
%\input{shyama-groebner}
\input{bibliography}
%\input{bbl-file}
\vfill\eject
\addcontentsline{toc}{section}{Index of definitions and notation}
%\printindex
\input{freeze-index}
\end{document}


<|FILE_SEP|>

% <|FILE: abstract.tex|>


--- START OF DOCUMENT TAIL ---
25,2.75){diagonal}
%%%%%%%%%%%%%%%%%%%%%%%%% boundary of $\andposv$ %%%%%%%%%%%%%%%%%%%%%
\thicklines
\color{red}
\put(5.25,10.25){boundary}\put(5.25,9.25){of $\andposv$}
\put(0,12){\line(1,0){3}}
\put(3,12){\line(0,-1){1}}
\put(3,11){\line(1,0){2}}
\put(5,11){\line(0,-1){2}}
\put(5,9){\line(1,0){2}}
\put(7,9){\line(0,-1){1}}
\put(7,8){\line(1,0){1}}
\put(8,8){\line(0,-1){1}}
\put(8,7){\line(1,0){1}}
\put(9,7){\line(0,-1){2}}
\put(9,5){\line(1,0){2}}
\put(11,5){\line(0,-1){2}}
\put(11,3){\line(1,0){1}}
\put(12,3){\line(0,-1){3}}
%%%%%%%%%%%%%%%%%%  A point and its legs %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\color{green}
\put(1,5){\circle{.4}}
\put(.25,5.5){$(r,c)$}
\put(1.25,.75){$(c^*,c)$}
\put(5.25,4.75){$(r,r^*)$}
\put(1.25,3){leg}
\put(2.75,5.25){leg}
\multiput(1,5)(0,-.5){8}{\line(0,-1){.3}}
\multiput(1,5)(.5,0){8}{\line(1,0){.3}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\end{picture}
%\end{center}
% \caption{The picutre of $\androotsv$}
%\end{figure}
%\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1632
```latex
--- START OF DOCUMENT HEAD ---
}{\renewcommand{\theenumi}{{\bf (A\arabic{enumi})$_{\mathbf +}$}} \renewcommand{\labelenumi}{\theenumi} \begin{enumerate} \setcounter{enumi}{\value{hypo}} \item}{\stepcounter{hypo} \end{enumerate}}

\newenvironment{hypm}{\renewcommand{\theenumi}{{\bf (A\arabic{enumi})$_{\mathbf -}$}} \renewcommand{\labelenumi}{\theenumi}\begin{enumerate} \setcounter{enumi}{\value{hypo}} \item}{\stepcounter{hypo} \end{enumerate}}

\newcommand{\refh}[1]{{\bf (A\ref{#1})}}

\newcommand{\refhp}[1]{{\bf (A\ref{#1})_{+}}}

\newcommand{\refhm}[1]{{\bf (A\ref{#1})_{-}}}


% Sets of Numbers


\def\C{{\mathbb C}}
\def\N{{\mathbb N}} 
\def\R{{\mathbb R}} 
\def\Q{{\mathbb Q}}
\def\Z{{\mathbb Z}}

% Others 
\def\A{{\mathbb A}}
\def\T{{\mathbb T}}
\def\S{{\mathbb S}}

\def\CC{\mathcal {C}}
%\def\CC{C}
\def\CA{\mathcal {A}}
\def\CD{\mathcal {D}}
\def\CE{\mathcal {E}}
\def\CF{\mathcal {F}}
\def\CG{\mathcal {G}}
\def\CH{\mathcal {H}}
\def\CK{\mathcal {K}}
\def\CL{\mathcal {L}}
\def\CM{\mathcal {M}}
\def\CN{\mathcal {N}}
\def\CO{\mathcal {O}}
\def\CP{\mathcal {P}}
\def\CR{\mathcal {R}}
\def\CS{\mathcal {S}}
\def\CT{\mathcal {T}}
\def\CW{\mathcal {W}}

\def\CI{{\mathcal I}}
\def\CJ{{\mathcal J}}
\def\codim{\mathop{\rm codim}\nolimits}
\def\ker{\mathop{\rm Ker}\nolimits}
\def\graph{\mathop{\rm graph}\nolimits}

% Maths

\def\re{\mathop{\rm Re}\nolimits}
 \def\im{\mathop{\rm Im}\nolimits}
\def\mod{\mathop{\rm mod}\nolimts}

\def\Op{\mathop{\rm Op}\nolimits}
\def\Vect{\mathop{\rm Vect}\nolimits}
\def\oph{\mathop{\rm Op}_{h}\nolimits}
\def\op{\mathop{\rm Op}^{w}_{h}\nolimits}

\def\supp{\mathop {\rm supp}\nolimits} 
\def\arg{\mathop{\rm arg}\nolimits}
\def\dist{\mathop{\rm dist}\nolimits}
\def\bra{\langle} \def\ket{\rangle}
\def\diag{\mathop{\rm diag}\nolimits}
\def\sgn{\mathop{\rm sgn}\nolimits}
\def\Hess{\mathop{\rm Hess}\nolimits}
\def\<{\langle}
\def\>{\rangle}

\def\Tr{\mathop{\rm Tr}\nolimits}
\def\MS{\mathop{\rm MS}\nolimits}
\def\square{\hbox{\vrule\vbox{\hrule\phantom{o}\hrule}\vrule}}
\def\cqfd{\hfill\square}
\def\fin{\hfill{$\Box$}}
\def\jj{\widehat\jmath}

\def\ds{\displaystyle}

\def\Partial#1#2{\frac{\partial #2}{\partial{#1}}}

\newcommand{\fract}[2]{\genfrac{}{}{0pt}{}{\scriptstyle #1}{\scriptstyle #2}}
\newcommand{\fractt}[3]{\fract{\fract{\scriptstyle #1}{\scriptstyle #2}}{\scriptstyle #3}}
\newcommand{\fracttt}[4]{\fract{\fract{\scriptstyle #1}{\scriptstyle #2}}{\fract{\scriptstyle #3}{\scriptstyle #4}}}

\def\comment#1{\medskip \hskip -2em\begin{minipage}[l]{6in} \noindent\sf
#1\end{minipage}\bigskip}

\renewcommand{\theenumi}{\sl{\roman{enumi}}}
\renewcommand{\labelenumi}{\theenumi)}

%----------------------------------


%\linespread {1,6}


%----------------------------------

\makeatletter
 \@addtoreset{equation}{section}
 \makeatother
 \renewcommand{\theequation}{\thesection.\arabic{equation}}


%--------------------------------------------------------


\author{Ivana Alexandrova} 
\address{Ivana Alexandrova, Department of Mathematics, East Carolina University, Greenville, NC 27858, USA}
\email{alexandrovai@ecu.edu}
\author{Jean-Fran\c{c}ois Bony}
\address{Jean-Fran\c{c}ois Bony, Institut de Math\'ematiques de Bordeaux, (UMR CNRS 5251), Universit\'e de Bordeaux I, 33405 Talence, France}
\email{bony@math.u-bordeaux1.fr} 
\author{Thierry Ramond}
\address{Thierry Ramond, Math\'ematiques, Universit\'e Paris Sud, (UMR CNRS 8628), 91405 Orsay, France}
\email{thierry.ramond@math.u-psud.fr}


\title{Semiclassical scattering amplitude at the maximum point of the potential}

\keywords{Scattering amplitude, critical energy, Schr\"odinger equation}
\subjclass[2000]{81U20,35P25,35B38,35C20}

\thanks{\textbf{Acknowledgments:}  We would like to thank Johannes Sj\"ostrand for helpful discussions during the preparation of this paper.  The first author also thanks Victor Ivrii for supporting visits to Universit\'{e} Paris Sud, Orsay, and the Department of Mathematics at Orsay for the extended hospitality.}




\date{April 12, 2007}




\begin{document}








--- START OF DOCUMENT TAIL ---
, \emph{Semiclassical study of quantum scattering on the line}, Comm.
  Math. Phys. \textbf{177} (1996), no.~1, 221--254.

\bibitem{RoTa87}
D.~Robert and H.~Tamura, \emph{Semiclassical estimates for resolvents and
  asymptotics for total scattering cross-sections}, Ann. Inst. H. Poincar\'e
  Phys. Th\'eor. \textbf{46} (1987), no.~4, 415--442.

\bibitem{RoTa89_01}
\bysame, \emph{Asymptotic behavior of scattering amplitudes in semi-classical
  and low energy limits}, Ann. Inst. Fourier (Grenoble) \textbf{39} (1989),
  no.~1, 155--192.

\bibitem{Sj87_01}
J.~Sj{\"o}strand, \emph{Semiclassical resonances generated by nondegenerate
  critical points}, Pseudodifferential operators (Oberwolfach, 1986), Lecture
  Notes in Math., vol. 1256, Springer, Berlin, 1987, pp.~402--429.

\bibitem{Va77_01}
B.~Va{\u\i}nberg, \emph{Quasiclassical approximation in stationary scattering
  problems}, Funkcional. Anal. i Prilo\v zen. \textbf{11} (1977), no.~4, 6--18,
  96.

\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1948
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: gautier.tex|>

\documentclass[a4paper,10pt]{article}

\usepackage{color}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{epsfig}
\bibliographystyle{alpha}
%\usepackage{showkeys}
\newtheorem{montheo}{Theorem}
\newtheorem{defin}{definition}
\newtheorem{cor}{Corollaire}
\newtheorem{prop}{Proposition}
\newtheorem {lem}{Lemma}
\newtheorem {rem}{\textit{Remark}}


\setlength{\textwidth}{15.5cm}              % fixe la largeur du texte
\setlength{\textheight}{23.6cm}            % fixe la hauteur du texte
\setlength{\oddsidemargin}{0.5cm}         % marge gauche des pages impaires
\setlength{\evensidemargin}{0.5cm}        % marge gauche des pages paires
\setlength{\topmargin}{-2cm}            % espace en haut de page


%opening
\title{Quadratic centers defining Elliptic Surfaces}
\author{S\'ebastien GAUTIER}

\begin{document}

\maketitle



--- START OF DOCUMENT TAIL ---
nolou: \textsl{Equations de Pfaff alg\'ebriques}, Lec. Notes in Math., 708 (1979).
\bibitem[Ka75]{K75} K. Kas: \textsl{Weirstrass normal forms and invariants of elliptic surfaces}, Trans. of the A.M.S, 225, (1977).
\bibitem[Ko60]{singular}K. Kodaira: \textsl{On compact analytic surfaces}, I, Annals of Math., 71 (1960),111-152.
\bibitem[Ko63]{singularbis}K. Kodaira: \textsl{On compact analytic
    surfaces}, II, Annals of Math., 77 (1963),563-626.
\bibitem[M89]{mir}R. Miranda, \textsl{The basic theory of elliptic
    surfaces}, Dottorato di Ricerca in Matematica. [Doctorate in
  Mathematical Research], ETS Editrice, Pisa, 1989.
\bibitem[P90]{Petrov}G. S. Petrov: \textsl{Nonoscillation of elliptic integrals}, Funct. Anal. Appl., 3 (1990), 45-50
\bibitem[YL02]{yu} J. Yu, C. Li: \textsl{Bifurcation of a class of planar
    non-Hamiltonian integrable systems with one center and one homoclinic loop},
    J. Math. Anal. Appl., 269 (2002), no. 1, 227--243.
\end{thebibliography}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0739
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: arxiv.tex|>
\documentclass{article}

\usepackage[latin1]{inputenc}
\usepackage{newcent}
\usepackage{amssymb}
\usepackage{graphicx}

\hyphenation{ma-xi-mi-zing mi-ni-mi-zing}
\title{Computation of Power Loss in
Likelihood Ratio Tests for Probability Densities Extended by Lehmann
Alternatives}
\author{Lucas Gallindo Martins Soares\\
\small\it
Departamento de Estat�stica e Inform�tica\\
\small\it
Universidade Federal Rural de Pernambuco, Brasil\\
\normalsize\tt lucasgallindo@gmail.com}
\date{}
\begin{document}
\maketitle


--- START OF DOCUMENT TAIL ---
Neyman-Pearson
lemma. \emph{Journal of Multivariate Analysis}, vol. \textbf{97},
Issue 9, pages 2034-2040.
\bibitem[Gupta et alii 1998]{GuptaQueSoAPorra}\textsc{Gupta, R. C., Gupta, P. L. and Gupta, R. D.} (1998).
Modeling failure time data by Lehman alternatives.
\emph{Communication in Statistics: Theory and Methods}, vol.
\textbf{27}, pages 887-904.
\bibitem[Kullback and Leibler 1951]{KullbackLiebler}\textsc{Kullback, S. and Leibler, R. A.} (1951).
On information and sufficiency. \emph{The Annals of Mathematical
Statistics}, vol. \textbf{22}, Number 1, pages 79-86.
\bibitem[Nadarajah and Kotz 2006]{NadarajahKotz}\textsc{Nadarajah, S., Kotz, S.} (2006).
The Exponentiated Type Distributions. \emph{Acta Applicandae
Mathematicae}, vol. \textbf{92}, pages 97-111.
\bibitem[Nadarajah 2006]{Nadarajah}\textsc{Nadarajah, S.} 2006. The exponentiated Gumbel distribution
with climate application. \emph{Environmetrics}, vol. \textbf{17},
Number 1, pages 13-23.
\end{thebibliography}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1782
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: EulerNumber.tex|>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% pdf settings
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%\pdfpagewidth=8.5truein
%\pdfpageheight=11truein
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%
%
%  This is a LaTeX file containing the paper
%
%    Asymptotic of the Euler number of a bipartite graphs
%
%  by Richard Ehrenborg and Yossi Farjoun
%
%
%	Last edited: January 12, 2007
%
%%%%%%%

\documentclass[11pt]{article}
\usepackage{latexsym,amsmath}
\usepackage{version}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{amsthm}
\usepackage{amssymb}
\usepackage{alltt}
%\usepackage{color}
\usepackage{epic}
\usepackage{eepic}
\usepackage{fancyheadings}
\usepackage{shadow}
\usepackage{array}
%\usepackage{caption}
\usepackage{enumerate}
\usepackage[normalem]{ulem}
\usepackage{epsfig}
\usepackage{multicol}
\usepackage{ifthen}
\usepackage{bbold}


%%%%% Here is the command to make the graphics package
%%%%% to work with pdfLaTeX
%\ifx\pdftexversion\undefined
%  \usepackage[dvips]{graphics}
%\else
%  \usepackage[pdftex]{graphics}
%\fi
%%%%%

\listfiles

\setlength{\topmargin}{ -1.5cm}
\setlength{\oddsidemargin}{ -0.5cm}
\textwidth 17cm
\textheight 22.4cm

\renewcommand{\baselinestretch}{1.0}

\font\german = eufm10 scaled\magstep1
\font\Cp = msbm10

\newcommand{\Nnn}{\hbox{\Cp N}}
\newcommand{\Ppp}{\hbox{\Cp P}}
\newcommand{\Rrr}{\hbox{\Cp R}}
\newcommand{\Zzz}{\hbox{\Cp Z}}

\newcommand{\binomial}[2]{\genfrac{(}{)}{0pt}{}{#1}{#2}}

\newcommand{\bigcenter}[1]{\begin{center} {\Large\bf #1} \end{center}}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{example}[theorem]{Example}
\newtheorem{definition}[theorem]{Definition}

\renewcommand{\theequation}{\thesection.\arabic{equation}}

%the next three lines make a new section reset the equation counter
\makeatletter
\@addtoreset{equation}{section}
\makeatother

\newcommand{\pair}[2]{\left\langle#1, #2\right\rangle}

\newcommand{\bfo}{{\mathbf 1}}
\newcommand{\Comb}{\mbox{\rm Comb}}
\newcommand{\onethingatopanother}[2]{\genfrac{}{}{0pt}{}{#1}{#2}}

\parskip=12pt

\begin{document}

\title{Asymptotics of the Euler number of bipartite graphs}

\author{{\sc Richard EHRENBORG}
        and
        {\sc Yossi FARJOUN}}

\date{}
\maketitle




--- START OF DOCUMENT TAIL ---
e pattern avoiding permutations}
         {2007}


\bibitem{Ehrenborg_Levin_Readdy}
\journal{R.\ Ehrenborg, M.\ Levin and M.\ Readdy}
        {A probabilistic approach to the descent statistic}
        {\JCTA}
        {98}{2002}{150--162}


\bibitem{Krein_Rutman}
{\sc M.\ G.\ Kre\u{\i}n and M.\ A.\ Rutman,}
Linear operators leaving invariant a cone in a Banach space.
\emph{Uspehi Matem. Nauk (N.S.)}
\textbf{3} (1948), no.\ 1 (23), 3--95.
English translation in \emph{Amer.\ Math.\ Soc.\ Translation}
\textbf{1950} (1950), no.\ 26, 1--128.

\bibitem{MacMahon}
\book{P.\ A.\ MacMahon}
     {Combinatory Analysis, Vol. I}
     {Chelsea Publishing Company, New York}
     {1960}

\end{thebibliography}

}


\bigskip
\noindent
{\em R.\ Ehrenborg,
Department of Mathematics,
University of Kentucky,
Lexington, KY~40506-0027}, \\
{\tt jrge@ms.uky.edu} \\

\noindent
{\em Y.\ Farjoun,
Department of Mathematics,
MIT,
Cambridge, MA~02139-4307}, \\
{\tt yfarjoun@math.mit.edu}.

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2183
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: boolean-cellular-automata-Arxiv-2.tex|>
\documentclass[12pt]{amsart}
%\usepackage{refcheck}
\usepackage{graphicx}
\usepackage{amscd}
\usepackage{amsmath}
\usepackage{amsfonts}
%\usepackage{yfonts}
%\usepackage{psfrag}
\usepackage{amssymb}
\usepackage{verbatim}
%%%%%%%%%%%%%%%%\usepackage[pdftex]{graphicx}% for jpg and pdf images
%\usepackage{comment}
%\input prepictex
%\input pictexwd
%\input postpictex

\textwidth=30cc \baselineskip=16pt

% voor tabellen
\newcommand{\toplines}{\hline \hline \\[-1.06ex]}
\newcommand{\sepline}{\\[-2.13ex] \hline \\[-2.13ex]}
\newcommand{\partsepline}[1]{\\[-2.13ex] \cline{#1} \\[-2.13ex]}
\newcommand{\botlines}{\\[+0.8ex] \hline \hline}
\newcommand{\source}[2][\vskip1ex]{#1\scriptsize\centerline{
\begin{minipage}[t]{0.8\textwidth}#2\end{minipage}}}


% macros voor kansrekening/statistiek
\newcommand{\pr}{\ensuremath{{\rm P}}}
\newcommand{\prob}[1]{\ensuremath{{\rm P}\!\left( #1 \right)}}
\newcommand{\prc}[2]{\ensuremath{{\rm P}( #1 \, |\, #2)}}
\newcommand{\expec}[1]{\ensuremath{{\rm E}\mspace{-1mu}\left[#1\right]}}
\newcommand{\ber}[1]{\textit{Ber\ensuremath{\mspace{2mu}(#1)}}}
\newcommand{\firule}[1]{\varphi_{\mathtt{#1}}}
\newcommand{\jfi}[1]{\mathtt{#1}}
\newcommand{\jf}{\mathtt{j}}
\newcommand{\Supp}[1]{\mathrm{Supp}{(#1)}}

\newtheorem{theorem}{Theorem}
\theoremstyle{plain}
\newtheorem{lemma}{Lemma}
\newtheorem{proposition}{Proposition}

\newcommand{\norm}[1]{\left\Vert#1\right\Vert}
\newcommand{\mb}[1]{\mathbf{#1}}
\newcommand{\Madn}{\left\{0,\dots,M\!-\!1\right\}^n}
\newcommand{\HD}[2]{V(#1,#2)}
\newcommand{\IC}[1]{({#1}_1,{#1}_2, \dots {#1}_N)}
\newcommand{\x}{x}
\newcommand{\X}{X}
\newcommand{\PN}[1]{{\mathbb P\!}_N\!\left({#1}\right)}
\newcommand{\PI}[1]{{\mathbb P\!}_*\!\left({#1}\right)}
\newcommand{\PIkaal}{{\mathbb P\!}_*}
\newcommand{\prcI}[2]{\ensuremath{{\mathbb P\!}_*\!}\left( #1 \, |\, #2\right)}
\newcommand{\prcN}[2]{\ensuremath{{\mathbb P\!}_N\!}\left( #1 \, |\, #2\right)}
\newcommand{\vecphi}{\varphi}
\newcommand{\map}{\Psi_{\varphi}}
\newcommand{\Map}{\Psi_{\!\Phi}}
\newcommand{\e}[1]{\varepsilon_{#1}}
\newcommand{\D}{{\Large$\cdot$}}



\begin{document}
\DeclareGraphicsExtensions{.jpg,.pdf,.png}


\parindent0pt

\title[Cellular Automata]
{Stability in random Boolean cellular automata on the integer lattice}



\author{F. Michel Dekking, Leonard van Driel and Anne Fey}
\address{ Delft Institute of Applied Mathematics,
 Technical University of Delft,  Mekelweg 4, 2628 CD Delft, The Netherlands\\
 email: F.M.Dekking@tudelft.nl}
\address{  Eurandom, Eindhoven, The Netherlands \\
 email: Fey@eurandom.tue.nl}






\maketitle


--- START OF DOCUMENT TAIL ---
\begin{center}
 \begin{tabular}{c|c|c|c|c|c}
 %\toplines
\; &$\firule{11}$ & $\firule{11}$&$\varphi_{\jfi{j_3}}$&$\varphi_{\cdot}$&\ldots\\
\sepline
 $x$ & $\cdot$ & $1$ & $\cdot$ & $\cdot$ & $\ldots$ \\
 $x'$ & $1$ & $1$ & $1$ & $\cdot$ &  $\ldots$ \\
 $x''$ & $1$ & $1$ & $1$ & $\cdot$ & $\ldots$
\end{tabular}
\end{center}
Conclusion: also $\jfi{j_3}=11$. Continuing in this fashion we
find that the (string of indices of the) $\varphi$-block has the
form $(\jfi{j_1},\ldots,\jfi{j_p})=(11,\ldots,11)$. But then we
have a problem in the $p^{\rm th}$ column since
$\firule{11}(1,y)=y$ depends on $y$. Hence for any $p$ this
possibility is ruled out.


\nocite{*}

\bibliographystyle{plain}
%\bibliographystyle{unsrt}

\bibliography{RBCA}

%\begin{thebibliography}{99}
%\bibitem{DG} Dekking, F. M. and Grimmett, G. R.,
% \emph{Superbranching processes and projections of random {C}antor sets},
% {Probab. Theory Related Fields}, {78}, (1988), {3}, {335--355},
%\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1975
```latex
--- START OF DOCUMENT HEAD ---
b T}}\newcommand{\ttt}{{\mathcal T}}
\renewcommand{\u}{{\mathfrak u}}\newcommand{\uu}{{\mathfrak u}}\newcommand{\UU}{{\mathcal U}}
\newcommand{\V}{{\mathcal V}}
\newcommand{\x}{{\mathcal X}}
\newcommand{\z}{{\mathcal Z}}\newcommand{\Z}{{\mathbb Z}}\newcommand{\ZZ}{\mathbb Z^2}



\newcommand{\ad}{\text{adm}}
\newcommand{\adj}{\text{Ad}}
\newcommand{\av}{\text{anguvol}}
\newcommand{\ar}{\text{area}}  %%%%%%%%%% AREA
\newcommand{\reg}{\text{reg}}
\newcommand{\sing}{\text{sing}}
\newcommand{\bo}{\partial} %%%%%%%%%% BOUNDARY
\newcommand{\cl}{\mbox{cl}} %%%%%%%%%% CLOSURE
\newcommand{\const}{\mbox{const}} %%%%%%%%%% CONSTANT
\newcommand{\codim}{\mbox{codim}} %%%%%%%%%% CODIMENSION
\newcommand{\den}{\text{den}}   %%%%%%%%%%%%% DENOMINATOR
\newcommand{\diam}{\text{diameter}}
\newcommand{\diff}{\text{Aff}}
\newcommand{\grexp}{\text{exp}}
\newcommand{\riexp}{\text{Exp}}
\newcommand{\Eig}{\text{Eig}}
\newcommand{\ex}{\text{ex}}
\newcommand{\fin}{\text{Per}} %%%%%%%%%%%%% FINITE-PERIODIC
\newcommand{\hyp}{\HH} %%%%%%%%%%%%% HYPERBOLIC PLANE
\newcommand{\hp}{\R^{n-1}} %%%%%%%%%%%%% HYPERPLANE
\newcommand{\id}{\text{Id}}   %%%%%%%%%%%%%%%% IDENTITY
\newcommand{\iso}{\text{Iso}}   %%%%%%%%%%%%%%%% ISOMETRIES
\newcommand{\ins}{\II\NN}     %%%%%%%%%%%%%%%%% INSECURE
\newcommand{\inter}{\text{interior}}     %%%%%%%%%%%%%%%%% INTERIOR
\newcommand{\Leb}{\text{Leb}}
\newcommand{\li}{\ell}     %%%%%%%%%%%%%%%%% STRAIGHT LINE
\newcommand{\mc}{\text{SL}}   %%%%%%%%%%%%% SL (FOR McMULLEN)
\newcommand{\mac}{\text{SL}(2,\R)}   %%%%%%%%%%%%% SL(2,R) (FOR McMULLEN)
\newcommand{\mcz}{\text{SL}(2,\Z)}   %%%%%%%%%%%%% SL(2,Z) (FOR McMULLEN)
\newcommand{\mes}{\text{mes}}   %%%%%%%%%%%%% MEASURE
\newcommand{\op}{\text{opt}}   %%%%%%%%%%%%% OPTICAL
\newcommand{\out}{\text{out}}  %%%%%%%%%%%%% OUTER
\newcommand{\per}{\text{Per}}  %%%%%%%%%%%%% PERIODIC
\newcommand{\rat}{\text{rat}} %%%%%%%%%%%%% RATIONAL
\newcommand{\rec}{\text{rec}}  %%%%%%%%%%%%%%
\newcommand{\rk}{\text{rk}} %%%%%%%%%%%%% RANK
\newcommand{\rayn}{\RRR^n} %%%%%%%%%%%%% SPACE OF RAYS
\newcommand{\sph}{S^2} %%%%%%%%%%%%% SPHERE
%\newcommand{\tot}{\text{full}} %%%%%%%%%%%%% FULL
\newcommand{\tot}{\Sigma} %%%%%%%%%%%%% FULL or CUMULATIVE
\newcommand{\val}{\text{val}}  %%%%%%%%%% VALENCE
\newcommand{\vol}{\text{vol}}  %%%%%%%%%% VOLUME
\newcommand{\wan}{\text{wan}}




\newcommand{\ta}{\tilde{a}}
\newcommand{\tB}{\tilde{B}}
\newcommand{\tc}{\tilde{c}}\newcommand{\tC}{\tilde{C}}
\newcommand{\tE}{\tilde{E}}
\newcommand{\tM}{\tilde{M}}
\newcommand{\tF}{\tilde{F}}
\newcommand{\tG}{\tilde{G}}
\newcommand{\tilh}{\tilde{h}}
\newcommand{\tp}{\tilde{p}}\newcommand{\tP}{\tilde{P}}
\newcommand{\ts}{\tilde{s}}
\newcommand{\tu}{\tilde{u}}
\newcommand{\tx}{\tilde{x}}\newcommand{\tX}{\tilde{X}}
\newcommand{\ty}{\tilde{y}}\newcommand{\tY}{\tilde{Y}}
\newcommand{\tz}{\tilde{z}}
\newcommand{\tw}{\tilde{w}}\newcommand{\tW}{\tilde{W}}
\newcommand{\tg}{\tilde{g}}
\newcommand{\tga}{\tilde{\ga}}
\newcommand{\tGa}{\tilde{\Ga}}
\newcommand{\tsig}{\tilde{\sig}}






\newcommand{\al}{\alpha}
\newcommand{\be}{\beta}
\newcommand{\ga}{\gamma}\newcommand{\Ga}{\Gamma}
\newcommand{\del}{\delta}\newcommand{\Del}{\Delta}
\newcommand{\ep}{\varepsilon}
\newcommand{\la}{\lambda}
\newcommand{\ka}{\kappa}
\newcommand{\sig}{\sigma}
\newcommand{\tht}{\theta}\newcommand{\Tht}{\Theta}
\newcommand{\om}{\omega}
\newcommand{\vp}{\varphi}
\newcommand{\PS}{\Psi}




\begin{document}

\bibliographystyle{plain}

\title[Complexity, etc]
{Growth rates  for geometric complexities and counting functions
in polygonal billiards}


\author{Eugene Gutkin and Michal Rams}
\address{IMPA, Rio de Janeiro, Brasil and UMK, Torun,
Poland;\hfill\hfill IMPAN, Warszawa, Poland}
\email{gutkin@impa.br,gutkin@mat.uni.torun.pl;rams@impan.gov.pl}



\keywords{Geodesic polygon, billiard map, billiard flow,
complexity, counting functions, unfolding of orbits, covering
space, exponential map}

%\subjclass{30F35, 30F60, 37B05, 37E35}


%\date{June 13, 2006}
\date{\today}




--- START OF DOCUMENT TAIL ---
=\lim_{l\to\infty}\tau(z,l).
$$

%
\begin{prop}  \label{crof_cont_prop}
Let the setting be as above. Let $\Phi\subset\Psi$ be a submanifold  satisfying the
Crofton-type formula equation~\ref{crof_flo_eq}.
Let $w$ be a weight function on $\R_+$ which is $L^1$
with respect to the density $\nu$:
$$
\int_0^{\infty}w(s)\nu(s)ds<\infty.
$$
Then
%
\begin{equation}            \label{crof_flo_ave_eq}
\int_{Z}gc_{z}(\Phi;w)dz\ =\ \vol(\Phi)\int_0^{\infty}w(s)\nu(s)ds.
\end{equation}
%
In particular, for the pure counting we have
%
\begin{equation}            \label{crof_flo_ave_eq1}
\int_{Z}gc_{z}(\Phi;l)dz\ =\ \vol(\Phi)\int_0^l\nu(s)ds.
\end{equation}
%
\begin{proof}
{\bf later}
%From equation~\ref{crof_eq} and the volume preservation,
%we deduce the formula
%$$
%\int_{\Tht}|\Ga_{\tht}(Y,k)|d\tht\ =\int_{\Tht}|T^{-k}Y\cap R_{\tht}|d\tht\ =\vol(T^{-k}Y)=\vol(Y).
%$$
%This identity directly implies equation~\ref{crof_ave_eq}. Equation~\ref{crof_ave_eq1} is a special case.
\end{proof}
\end{prop}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0002
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: sparsity-certifying.tex|>
\pdfoutput=1
\documentclass[Svgc,nospthms]{Svgc} 
\journalname{Graphs and Combinatorics}

\usepackage[utf8]{inputenc}

\usepackage{amssymb,amstext,amsmath,amsthm}
\usepackage{mathptmx}

\usepackage[numbers,sort&compress]{natbib}

\newcommand{\ellteekay}{\ensuremath{\ell{\mathsf T}k}\,}

\usepackage{graphicx}
\newcommand{\fig}[3]{
  \begin{figure}[h]
  \centering
  \includegraphics[#1]{#3}
  \caption{#2}
    \label{fig.#3}
  \end{figure}
}



\newcommand{\reffig}[1]{Figure \ref{fig.#1}}


\makeatletter
\newcommand{\Pr@}{\operatorname{Pr}}
\newcommand{\E@}{\operatorname{E}}
\newcommand{\Var@}{\operatorname{Var}}
\renewcommand{\Pr}[1]{\ensuremath{\Pr@\left[{#1}\right]}}
\newcommand{\E}[1]{\ensuremath{\E@\left[{#1}\right]}}
\newcommand{\Var}[1]{\ensuremath{\Var@\left[{#1}\right]}}
\makeatother

\newcommand{\card}[1]{\ensuremath{\left\vert #1 \right\vert}}
\newcommand{\abs}[1]{\ensuremath{\left\vert #1 \right\vert}}
\newcommand{\ceil}[1]{\ensuremath{\left\lceil #1 \right\rceil}}
\newcommand{\floor}[1]{\ensuremath{\left\lfloor #1 \right\rfloor}}
\newcommand{\where}{~|~}

\newcommand{\N}{\ensuremath{\mathbb{N}}}
\newcommand{\R}{\ensuremath{\mathbb{R}}} 
\newcommand{\Zplus}{\ensuremath{\mathbb{Z}^+}}
\newcommand{\Lang}[1]{\ensuremath{\mathcal{L}(#1)}}

\newcommand{\partdev}[2]{\ensuremath{\frac{\partial #1}{\partial #2}}}

\usepackage{url}

\newcommand{\pfrac}[2]{{\left(\frac{#1}{#2}\right)}}
\newcommand{\bfrac}[2]{{\left[\frac{#1}{#2}\right]}}

\newcommand{\F}{\ensuremath{\mathcal{F}}}

\newcommand{\B}{\ensuremath{\mathcal{B}}}


\newtheorem{theorem}{Theorem}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{algorithm}[theorem]{Algorithm}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{problem}{Problem}


\newcommand{\refsec}[1]{Section \ref{sec.#1}}
\newcommand{\reflem}[1]{Lemma \ref{lem.#1}}
\newcommand{\refthm}[1]{Theorem \ref{thm.#1}}
\newcommand{\refalg}[1]{Algorithm \ref{alg.#1}}
\newcommand{\refcor}[1]{Corollary \ref{cor.#1}}
\newcommand{\refprop}[1]{Proposition \ref{prop.#1}}
\newcommand{\refeq}[1]{(\ref{eq.#1})}
\newcommand{\labelsec}[1]{\label{sec.#1}}
\newcommand{\labellem}[1]{\label{lem.#1}}
\newcommand{\labelthm}[1]{\label{thm.#1}}
\newcommand{\labelalg}[1]{\label{alg.#1}}
\newcommand{\labeleq}[1]{\label{eq.#1}}
\newcommand{\labelcor}[1]{\label{cor.#1}}
\newcommand{\labelprop}[1]{\label{prop.#1}}


\usepackage[colorlinks=false]{hyperref}

\author{Ileana Streinu\inst{1}\thanks{Research of both authors funded by the NSF under grants NSF CCF-0430990 and NSF-DARPA CARGO CCR-0310661 to the first author.} \and Louis Theran\inst{2}}
\institute{Department of Computer Science, Smith College, Northampton, MA. \email{streinu@cs.smith.edu} 
\and Department of Computer Science, University of Massachusetts Amherst. \email{theran@cs.umass.edu}} 
\title{Sparsity-certifying Graph Decompositions} 

\newcommand{\restateenv}{ZZZ}
\newenvironment{restate}[1]{
  \renewcommand{\restateenv}{restate.#1}
  \newtheorem*{\restateenv}{\refthm{#1}}
  \begin{\restateenv}
}{\end{\restateenv}}

\newenvironment{restatecor}[1]{
  \renewcommand{\restateenv}{restate.#1}
  \newtheorem*{\restateenv}{\refcor{#1}}
  \begin{\restateenv}
}{\end{\restateenv}}


\usepackage{subfigure} 

\newcommand{\peb}{\ensuremath{\operatorname{peb}}} 
\newcommand{\grsp}{\ensuremath{\operatorname{span}}} 
\newcommand{\out}{\ensuremath{\operatorname{out}}} 
\newcommand{\colors}{\ensuremath{\operatorname{colors}}}
\begin{document}
	\maketitle
		

--- START OF DOCUMENT TAIL ---
orial genericity and minimal rigidity.
\newblock In: SCG '08: Proceedings of the twenty-fourth annual Symposium on
  Computational Geometry, pp. 365--374. ACM, New York, NY, USA (2008).

\bibitem[{Tay(1984)}]{tay:rigidityMultigraphs-I:1984}
Tay, T.S.: Rigidity of multigraphs {I}: linking rigid bodies in $n$-space.
\newblock Journal of Combinatorial Theory, Series B \textbf{26}, 95--112 (1984)

\bibitem[{Tay(1993)}]{Tay93}
Tay, T.S.: A new proof of {L}aman's theorem.
\newblock Graphs and Combinatorics \textbf{9}, 365--370 (1993)

\bibitem[{Tutte(1961)}]{tutte:decomposing-graph-in-factors-1961}
Tutte, W.T.: On the problem of decomposing a graph into $n$ connected factors.
\newblock Journal of the London Mathematical Society \textbf{142}, 221--230 (1961)

\bibitem[{Whiteley(1988)}]{whiteley:union-matroids}
Whiteley, W.: The union of matroids and the rigidity of frameworks.
\newblock SIAM Journal on Discrete Mathematics \textbf{1}(2), 237--255 (1988)

\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0923
```latex
--- START OF DOCUMENT HEAD ---
idth}{2.2cm}\addtolength{\hoffset}{-1.1cm}
\renewcommand{\baselinestretch}{1.85}

\newtheorem{thm}{Theorem}[section]
\newtheorem{lem}[thm]{Lemma}
\newtheorem{defi}[thm]{Definition}
\theoremstyle{definition}
\newtheorem{rek}[thm]{Remark}

\newcommand\ben{\begin{enumerate}}
\newcommand\een{\end{enumerate}}


%The groups%
\renewcommand{\d}{{\mathrm{d}}} % differential, used in integrals

\renewcommand{\^}{\widehat} %Fourier transform

\newcommand{\soe}{\text{SO(even)}}
\newcommand{\soo}{\text{SO(odd)}}
\newcommand{\sym}{\text{sym}}
\newcommand{\SO}{{\mathrm{SO}}} %orthogonal group

\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
%Greek%

\newcommand{\ga}{\alpha}    %lowercase alpha
\newcommand{\gb}{\beta}      %lowercase beta
\newcommand{\gd}{\delta}    %lowercase delta
\newcommand{\gep}{\epsilon}  %lowercase epsilon
\newcommand{\G}{\Gamma}      %Capital Gamma
\newcommand{\g}{\gamma}      %lowercase gamma
\newcommand{\gL}{\Lambda}    %capital lamda
\newcommand{\gl}{\lambda}    %lowercase lambda
\newcommand{\gt}{\theta}    %lowercase theta


\newcommand{\twocase}[5]{#1 \begin{cases} #2 & \text{#3}\\ #4
&\text{#5} \end{cases}  }


\newcommand\be{\begin{equation}}
\newcommand\ee{\end{equation}}
\newcommand\bea{\begin{eqnarray}}
\newcommand\eea{\end{eqnarray}}


\newcommand{\fof}{\frac{1}{4}}  %oneforth
\newcommand{\foh}{\frac{1}{2}}  %onehalf
\newcommand{\fot}{\frac{1}{3}}  %onethird


\newcommand{\dettwo}[4]
{\left|\begin{array}{cc}
                        #1  & #2  \\
                        #3 &  #4
                          \end{array}\right| }

\newcommand{\detthree}[9]
{\left|\begin{array}{ccc}
                        #1  & #2 & #3  \\
                        #4 &  #5 & #6 \\
                        #7 &  #8 & #9
                          \end{array}\right| }

%  **********************************************
%  NEW COMMANDS FOR N-LEVEL DENSITIES
%  **********************************************

\newcommand{\hkpn}{H_k^+(N)}
\newcommand{\hkmn}{H_k^-(N)}
\newcommand{\hkpmn}{H_k^\pm(N)}
\newcommand{\hkn}{H_k^\ast(N)}
\newcommand{\hksn}{H_k^\sigma(N)}

\newcommand{\jk}[2]{J_{k-1}\left( 4\pi \frac{ \sqrt{ #1 } }{ #2 }\right) }
\newcommand{\phir}[1]{\widehat{\phi}\left( \frac{ \log p_{#1} }{\log R}\right) }
\newcommand{\phirx}[1]{\widehat{\phi}\left( \frac{ \log x_{#1} }{\log R}\right) }
\newcommand{\phiv}[1]{\widehat{\phi}\left( \frac{ \log #1 }{\log R}\right) }
\newcommand{\hphiv}[1]{\widehat{\phi}\left( #1 \right) }
\newcommand{\flogr}[1]{\frac{ #1 }{\log R}}
\newcommand{\pfrac}[1]{\frac{2\log p_{#1}}{\sqrt{p_{#1}} \log R}}
\newcommand{\glp}[1]{\gl_f(p_{#1})}
\newcommand{\ils}{\cite{ILS}}
\newcommand\eq{{Equation\ }}
\newcommand{\chib}[1]{\overline{\chi}(#1)}
\newcommand{\chibt}[1]{\overline{\chi_2}(#1)}
\newcommand{\chibo}[1]{\overline{\chi_1}(#1)}
\newcommand{\chibthree}[1]{\overline{\chi_3}(#1)}
\newcommand{\db}{\overline{d}}


\newcommand{\hphi}{\widehat{\phi}}  %phi^

\newcommand{\Zf}{Z_\phi} % scaled level density

\renewcommand{\mod}{\;\operatorname{mod}}
\newcommand{\smod}[1]{(\operatorname{mod} #1)}
\newcommand{\supp}{\operatorname{supp}}
\newcommand{\notdiv}{\nmid}
\newcommand{\intinf}{\int_{-\infty}^\infty}
\newcommand{\E}{{\mathbb E}} % expectation
\newcommand{\I}{1\!\!1} % indicator function

\renewcommand{\i}{{\mathrm{i}}} % sqrt -1
\renewcommand{\d}{{\mathrm{d}}} % differential, used in integrals


\renewcommand{\Re}{{\mathfrak{Re}}}
\renewcommand{\Im}{{\mathfrak{Im}}}

\newcommand{\<}{\left\langle}
\renewcommand{\>}{\right\rangle}


\numberwithin{equation}{section}


\begin{document}

\title{When the Cram\'{e}r-Rao Inequality provides no information}

\author{Steven J. Miller}
\address{Department of Mathematics, Brown University, 151 Thayer
 Street, Providence, RI 02912}
 \email{sjmiller@math.brown.edu}

\subjclass[2000]{62B10 (primary), 62F12, 60E05 (secondary).}

\keywords{Cram\'{e}r-Rao Inequality, Pareto distribution, power law}

\date{\today}




--- START OF DOCUMENT TAIL ---
e of analysis.  The Cramer-Rao inequality is
a special version of Cauchy-Schwartz inequality. So, if one of the
random variables is not square integrable, like in the example
considered by the author, the inequality cannot be deduced,� and it
is clear that no information on the variance of the other variable
can be obtained.

I have also an additional comment: Are there unbiased estimators for
the parameter \theta, such that for theta=1 have finite variance? A
positive answer to this question should be provided in the paper to
have some interest.

------------------------------------------------------------------------

The paper WHEN THE CRAMER-RAO INEQUALITY PROVIDES NO INFORMATION by
Steven J. Miller is certainly correct.  It is not clear how
significant the result is, however.  The paper would be much
improved by including a brief discussion of the use of the
Cramer-Rao lower bound in statistical inference and using this
discussion to provide a context for the result of the paper.
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0349
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: Ax2CdVP.tex|>
\documentclass[a4paper,11pt]{article}

\usepackage{amsmath,amssymb}

\usepackage{graphicx}
\usepackage{epsfig}
\usepackage{color}

\graphicspath{{Fig/}}

\newenvironment{proof}{\begin{trivlist}
	\item[\noindent]{\it Proof\:}}{\quad $\square$\end{trivlist}}

\newenvironment{exl}{\begin{trivlist}
	\item[\noindent]{\bf Example\:}}{\end{trivlist}}

\newenvironment{exls}{\begin{trivlist}
	\item[\noindent]{\bf Examples\:}}{\end{trivlist}}

\newtheorem{dfn}{Definition}[section]
\newtheorem{thm}[dfn]{Theorem}
\newtheorem{prp}[dfn]{Proposition}
\newtheorem{lem}[dfn]{Lemma}
\newtheorem{cor}[dfn]{Corollary}

\def\N{{\mathbb N}}
\def\R{{\mathbb R}}
\def\Z{{\mathbb Z}}
\def\Sph{{\mathbb S}}
\def\phi{\varphi}
\def\epsilon{\varepsilon}
\def\inn{\mathrm{int}}
\def\grad{\mathrm{grad}\,}
\def\vol{\mathrm{vol}}
\def\area{\mathrm{area}}
\def\M{{\mathcal M}}
\def\P{{\mathcal P}}
\def\im{\mathrm{im}\,}
\def\ker{\mathrm{ker}\,}
\def\aff{\mathrm{aff}\,}
\def\span{\mathrm{span}\,}


\title{The Colin de Verdi\`ere number\\ and graphs of polytopes}
\author{Ivan Izmestiev
\thanks{Research for this article was supported by the DFG Research Unit 565 ``Polyhedral Surfaces''.}\\
Institut f\"ur Mathematik\\
Technische Universit\"at Berlin\\
Str. des 17. Juni 136\\
10623 Berlin, Germany\\
{\tt izmestiev@math.tu-berlin.de}}
\date{July 25, 2008}

\begin{document}

\maketitle



--- START OF DOCUMENT TAIL ---
#5{%
  \reset@font\fontsize{#1}{#2pt}%
  \fontfamily{#3}\fontseries{#4}\fontshape{#5}%
  \selectfont}%
\fi\endgroup%
\begin{picture}(3174,1824)(529,-1603)
\put(1306,-1051){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\color[rgb]{0,0,0}$\theta_{ij}$}%
}}}}
\put(3376,-376){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\color[rgb]{0,0,0}$\Delta x_i$}%
}}}}
\put(631,-241){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\color[rgb]{0,0,0}$\Delta \vol_1(F_j)$}%
}}}}
\put(2071,-421){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\color[rgb]{0,0,0}$\Delta \vol_2(P)$}%
}}}}
\put(2386,-1051){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\color[rgb]{0,0,0}$F_i$}%
}}}}
\put(541,-1186){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\color[rgb]{0,0,0}$F_j$}%
}}}}
\end{picture}%
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0105
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: rigid-subsets-20081024-1.tex|>
%M.'s version-revision- 24 Oct 2008
\documentclass[12pt]{article}
\usepackage{amsmath,amssymb,amsthm,amsfonts,graphicx,caption}
\usepackage[all]{xy}

\hyphenation{displa-ce-able}



\newtheorem{thm}{Theorem}[section]
\newtheorem{lemma}[thm]{Lemma}
\newtheorem{prop}[thm]{Proposition}
\newtheorem{cor}[thm]{Corollary}
\newtheorem{defin}[thm]{Definition}
\newtheorem{rem}[thm]{Remark}
\newtheorem{exam}[thm]{Example}
\newtheorem{problem}[thm]{Problem}
\newtheorem{question}[thm]{Question}
\newtheorem{convention}[thm]{Convention}

%\newcommand{\prlabel}[1]{\label{#1}}%\fbox{#1}}
%\newcommand{\prbibitem}[2]{\bibitem[#1]{#2}}%\fbox{#2}}

\newcommand{\R}{{\mathbb{R}}}
\newcommand{\D}{{\mathbb{D}}}
\newcommand{\Q}{{\mathbb{Q}}}
\newcommand{\T}{{\mathbb{T}}}
\newcommand{\Z}{{\mathbb{Z}}}
\newcommand{\N}{{\mathbb{N}}}
\newcommand{\C}{{\mathbb{C}}}
\newcommand{\SP}{{\mathbb{S}}}
\newcommand{\Id}{{\mathbb{1}}}

\newcommand{\La}{{\Lambda}}
\newcommand{\tLa}{{\widetilde{\Lambda}}}
\newcommand{\tP}{{\widetilde{\mathcal{P}}}}

\newcommand{\hJ}{{\hat{J}}}

\newcommand{\cA}{{\mathcal{A}}}
\newcommand{\cB}{{\mathcal{A}}}
\newcommand{\cD}{{\mathcal{D}}}
\newcommand{\cE}{{\mathcal{E}}}
\newcommand{\cF}{{\mathcal{F}}}
\newcommand{\cG}{{\mathcal{G}}}
\newcommand{\cH}{{\mathcal{H}}}
\newcommand{\cI}{{\mathcal{I}}}
\newcommand{\cK}{{\mathcal{K}}}
\newcommand{\cL}{{\mathcal{L}}}
\newcommand{\tcL}{{\widetilde{\mathcal{L}}}}

\newcommand{\cM}{{\mathcal{M}}}
\newcommand{\cN}{{\mathcal{N}}}
\newcommand{\cP}{{\mathcal{P}}}
\newcommand{\cR}{{\mathcal{R}}}
\newcommand{\cS}{{\mathcal{S}}}
\newcommand{\cT}{{\mathcal{T}}}
\newcommand{\cU}{{\mathcal{U}}}
\newcommand{\cV}{{\mathcal{V}}}
\newcommand{\cW}{{\mathcal{W}}}
\newcommand{\cC}{{\mathcal{C}}}
\newcommand{\oQ}{{\overline{QH}_{ev} (M)}}

\newcommand{\tG}{{\widetilde{G}}}
\newcommand{\tmu}{{\tilde{\mu}}}
\newcommand{\tf}{{\tilde{f}}}
\newcommand{\tg}{{\tilde{g}}}
\newcommand{\tlambda}{{\tilde{\lambda}}}
\newcommand{\tphi}{{\tilde{\phi}}}
\newcommand{\tpsi}{{\tilde{\psi}}}
\newcommand{\tih}{{\tilde{h}}}
\newcommand{\bF}{{\bar{F}}}
\newcommand{\Cal}{{\hbox{\it Cal\,}}}
\newcommand{\tCal}{{\widetilde{\hbox{\it Cal}}}}
\newcommand{\grad}{{\hbox{\rm grad\,}}}
\newcommand{\Fix}{{\hbox{\rm Fix\,}}}
\newcommand{\PathCZ}{{\hbox{\rm Path}_{CZ}\,}}
\newcommand{\indCZ}{{\hbox{\rm ind}_{CZ}\,}}
\newcommand{\Maslov}{{\hbox{\it Maslov\,}}}

\newcommand{\Ham}{{\it Ham}}
\newcommand{\spec}{{\it spec}}
\newcommand{\id}{{\text{{\bf 1}}}}
%\def\square{{\vrule height6pt width6pt depth2pt}}
\newcommand{\tHam}{\widetilde{\hbox{\it Ham}\, }}
\newcommand{\Symp}{{\hbox{\it Symp} }}
\newcommand{\supp}{{supp}}
%----------------------------------------------------------------------

\newcommand{\Qed}{\hfill \qedsymbol \medskip}

%----------------------------------------------------------------------




\begin{document}


\title{Rigid subsets of symplectic manifolds\\
%{\it (preliminary version)}
}


\renewcommand{\thefootnote}{\alph{footnote}}
%\setcounter{footnote}{1}


\author{\textsc Michael Entov$^{a}$\ and Leonid
Polterovich$^{b}$ }


\footnotetext[1]{Partially supported by E. and J. Bishop Research
Fund and by the Israel Science Foundation grant $\#$ 881/06.}
\footnotetext[2]{Partially supported by the Israel Science
Foundation grant $\#$ 11/03.}



\date{\today}



\maketitle



\bigskip



--- START OF DOCUMENT TAIL ---
e geometry of generating functions},
Math. Ann. {\bf 292}:4 (1992), 685-710.

\bibitem{VanDerWaerden} van der Waerden, B., {\it Algebra.} Vol. 2,
Springer-Verlag, 1991.

\bibitem{Wang-Zhu} Wang, X.-J., Zhu, X.,
{\it K\"ahler-Ricci solitons on toric manifolds with positive
first Chern class},  Adv. Math.  {\bf 188}:1  (2004), 87-103.

\bibitem{Weinst} Weinstein, A., {\it
Cohomology of symplectomorphism groups and critical values of
Hamiltonians}, Math. Z. {\bf 201}:1 (1989), 75-82.




\bibitem{Wi} Witten, E.,
{\it Two-dimensional gravity and intersection theory on moduli
space}, Surveys in Diff. Geom. {\bf 1} (1991), 243-310.

\end{thebibliography}

\bigskip

\noindent

\begin{tabular}{@{} l @{\ \ \ \ \ \ \ \ \ \ \,} l }
Michael Entov & Leonid Polterovich \\
Department of Mathematics & School of Mathematical Sciences \\
Technion & Tel Aviv University \\
Haifa 32000, Israel & Tel Aviv 69978, Israel \\
entov@math.technion.ac.il &
polterov@post.tau.ac.il\\
\end{tabular}



\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0302
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: singleindex.tex|>
\documentclass[11pt]{book}
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{graphics}
\usepackage{epsfig,amssymb,latexsym,verbatim}
\usepackage{graphicx}
\usepackage{multirow}
\usepackage{multicol}
\usepackage{hypernat}
\usepackage{float}
\usepackage{hyperref}
\floatstyle{ruled}
\newfloat{algorithm}{tbp}{loa}
\floatname{algorithm}{Algorithm}
\usepackage{graphicx, amssymb}

\textwidth=37.4pc \textheight=50.5pc \oddsidemargin=0.4pc
\evensidemargin=0.4pc \headsep=15pt
%\headheight=.2cm
\topmargin=.6cm
\parindent=1.6pc
\parskip=0pt
\newtheorem{theorem}{{\bf Theorem}}
\newtheorem{lemma}{{\bf Lemma}}
\newtheorem{corollary}{{\bf Corollary}}
\newtheorem{proposition}{{\bf Proposition}}

\setcounter{page}{1}
\begin{document}
\renewcommand{\baselinestretch}{1.2}
\markboth{\hfill{\footnotesize\rm LI WANG AND LIJIAN YANG}\hfill}
{\hfill {\footnotesize\rm SINGLE-INDEX PREDICTION MODEL} \hfill}
\renewcommand{\thefootnote}{}
$\ $\par \fontsize{10.95}{14pt plus.8pt minus .6pt}\selectfont
\vspace{0.8pc} \centerline{\large\bf SPLINE SINGLE-INDEX
PREDICTION MODEL} %\vspace{2pt}
%\centerline{\large\bf IF A SECOND LINE IS NEEDED}
\vspace{.4cm} \centerline{Li Wang and Lijian Yang
\footnote{\emph{Address for correspondence}: Lijian Yang,
Department of Statistics and Probability, Michigan State
University, East Lansing, MI 48824, USA. E-mail:
yang@stt.msu.edu}} \vspace{.4cm} \centerline{\it University of
Georgia and Michigan State University} \vspace{.55cm}
\fontsize{9}{11.5pt plus.8pt minus .6pt}\selectfont

\begin{quotation}
\noindent \textit{Abstract:} For the past two decades,
single-index model, a special case of projection pursuit
regression, has proven to be an efficient way of coping with the
high dimensional problem in nonparametric regression. In this
paper, based on weakly dependent sample, we investigate the
single-index prediction (SIP) model which is robust against
deviation from the single-index model. The single-index is
identified by the best approximation to the multivariate
prediction function of the response variable, regardless of
whether the prediction function is a genuine single-index
function. A polynomial spline estimator is proposed for the
single-index prediction coefficients, and is shown to be root-n
consistent and asymptotically normal. An iterative optimization
routine is used which is sufficiently fast for the user to analyze
large data of high dimension within seconds. Simulation
experiments have provided strong evidence that corroborates with
the asymptotic theory. Application of the proposed procedure to
the rive flow data of Iceland has yielded superior out-of-sample
rolling forecasts.

\vspace{9pt} \noindent \textit{Key words and phrases:} B-spline, geometric
mixing, knots, nonparametric regression, root-n rate, strong consistency.
\end{quotation}

\fontsize{10.95}{14pt plus.8pt minus .6pt}\selectfont

\thispagestyle{empty}

\setcounter{chapter}{1} \label{SEC:introduction}
\setcounter{equation}{0}
%-1
\noindent \textbf{1. Introduction} \vskip 0.1in

Let $\left\{ \mathbf{X}_{i}^{T},Y_{i}\right\} _{i=1}^{n}=\left\{
X_{i,1},...,X_{i,d},Y_{i}\right\} _{i=1}^{n}$ be a length $n$ realization of
a $\left( d+1\right) $-dimensional strictly stationary process following the
heteroscedastic model
\begin{equation}
Y_{i}=m\left( \mathbf{X}_{i}\right) +\sigma \left( \mathbf{X}_{i}\right)
\varepsilon _{i},m\left( \mathbf{X}_{i}\right) =E\left( Y_{i}|\mathbf{X}%
_{i}\right) ,  \label{sindmodel}
\end{equation}
in which $E\left( \varepsilon _{i}\left| \mathbf{X}_{i}\right. \right) =0$, $%
E\left( \varepsilon _{i}^{2}\left| \mathbf{X}_{i}\right. \right)
=1$, $1\leq i\leq n$. The $d$-variate functions $m$, $\sigma $ are
the unknown mean and standard deviation of the response $Y_{i}$
conditional on the predictor vector $\mathbf{X}_{i}$, often
estimated nonparametrically. In what follows, we let $\left(
\mathbf{X}^{T},Y,\varepsilon \right) $ have the stationary
distribution of $\left

--- START OF DOCUMENT TAIL ---
rature $X_t$ (solid line) with its trend
(dashed line) (c) precipitation $Z_t$ (solid line) with its trend
(dashed line).} \label{FIG:riverflow}
\end{figure}

\newpage % This is the figure to see the convergence behavior
\setlength{\unitlength}{1cm} \pagestyle{empty}
\begin{figure}[th]
\begin{center}
\begin{picture}(-19.5,20)
\put(-16.5,9.4){\special{psfile=flow_fitted.ps hscale=65 vscale=55 angle=0}}%
\put(-9.4,13.8){(a)}%
\put(-16.5,3.4){\special{psfile=flow_resi.ps hscale=65 vscale=55 angle=0}}%
\put(-9.4,7.8){(b)}%
\put(-16.5,-2.6){\special{psfile=k365.ps hscale=65 vscale=55 angle=0}}%
\put(-9.4,1.8){(c)}%
\end{picture}
\end{center}
\par
\vskip -2.0cm \caption{(a) The scatter plot of the river flow
(``+") and the fitted plot of the river flow (line) and (b)
Residuals of the fitted SIP model (c) Out-of-sample rolling
forecasts (line) of the river flow for the entire third year
(``+") based on the first two years' river flow.}
\label{FIG:riverflow_fitted}
\end{figure}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0416
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: ncg.tex|>
\documentclass[12pt]{article}

\usepackage{amsfonts}
\usepackage[centertags]{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{newlfont}
\usepackage{graphics}
\usepackage{graphicx}
%\usepackage{german}
%\usepackage{psfig}
%\usepackage[latin1]{inputenc}
%\usepackage[T1]{fontenc}
\usepackage[all]{xy}
\usepackage[german]{varioref}
\usepackage{a4,latexsym}
\hfuzz2pt \pagestyle{headings}



\input{vorspann22.tex}


\setlength{\parindent}{0cm}

\begin{document}

\begin{center}
\section*{Origamis with non congruence Veech groups}
{\it Gabriela Schmith\"usen}
\end{center}

\input{intro.tex}
\newpage
\input{origamis.tex}
\input{veechgroups.tex}
\input{ovgs.tex}
\newpage
\input{literatur.tex}

\end{document}



<|FILE_SEP|>

% <|FILE: d.tex|>
\setlength{\unitlength}{1cm}
\begin{picture}(4,3.2)
% Die Kaestchen des Origamis:
%\put(-2.7,1.2){ $\mbox{Loc}(n) =$}
\put(0,0){\framebox(1,1){1}}
\put(1,0){\framebox(1,1){2}}
\put(2,0){\framebox(1,1){3}}
\put(0,1){\framebox(1,1){4}}
\put(0,2){\framebox(1,1){5}}

% Beschriftung:
\put(1.55,-.35){$a$}
\put(2.55,1.1){$a$}
\put(1.55,1.1){$b$}
\put(2.55,-.35){$b$}

% labels for the vertices:
\put(-.1,-.1){\Large $\bullet$}
\put( .9,-.1){\Large $\bullet$}
\put(2.9,-.1){\Large $\bullet$}
\put(1.9, .9){\Large $\bullet$}
\put(-.1,2.9){\Large $\bullet$}
\put( .9,2.9){\Large $\bullet$}
\put(-.13, 1.87){\Large $\circ$}
\put( .87, 1.87){\Large $\circ$}
\put(-.25,  .7){\LARGE \bf *}
\put( .75,  .7){\LARGE \bf *}
\put(1.7,  -.3){\LARGE \bf *}
\put(2.7,  .7){\LARGE \bf *}
\end{picture}




<|FILE_SEP|>

% <|FILE: dn.tex|>
\setlength{\unitlength}{1cm}
\hspace*{1cm}
\begin{picture}(12,3.2)
% Die labels of the vertices des Origamis:
%\put(-2.7,1.2){ $\mbox{Loc}(n) =$}
\put(0,0){\framebox(1,1){1}}
\put(1,0){\framebox(1,1){2}}
\put(2,0){\framebox(1,1){3}}
\put(0,1){\framebox(1,1){4}}
\put(0,2){\framebox(1,1){5}}

\put(3,0){\framebox(1,1){6}}
\put(4,0){\framebox(1,1){7}}
\put(5,0){\framebox(1,1){8}}
\put(3,1){\framebox(1,1){9}}
\put(3,2){\framebox(1,1){10}}
 
\put(6.3,0){\ldots\ldots\ldots}

\put(8,0){\framebox(1,1){5n-4}}
\put(9,0){\framebox(1,1){5n-3}}
\put(10,0){\framebox(1,1){5n-2}}
\put(8,1){\framebox(1,1){5n-1}}
\put(8,2){\framebox(1,1){5n}}

% labels:
\put(1.4,-.4){$a_1$}
\put(2.4,1.2){$a_1$}
\put(1.4,1.2){$b_1$}
\put(2.4,-.4){$b_1$}

\put(4.4,-.4){$a_2$}
\put(5.4,1.2){$a_2$}
\put(4.4,1.2){$b_2$}
\put(5.4,-.4){$b_2$}

\put(9.4,-.4){$a_{n}$}
\put(10.4,1.2){$a_{n}$}
\put(9.4,1.2){$b_{n}$}
\put(10.4,-.4){$b_{n}$}


% labels Punkte:
\put(-.1,-.1){\Large $\bullet$}
\put( .9,-.1){\Large $\bullet$}
\put(2.9,-.1){\Large $\bullet$}
\put(1.9, .9){\Large $\bullet$}
\put(-.1,2.9){\Large $\bullet$}
\put( .9,2.9){\Large $\bullet$}
\put(-.12, 1.88){\Large $\circ$}
\put( .88, 1.88){\Large $\circ$}
\put(-.17,  .69){\LARGE \bf *}
\put( .83,  .69){\LARGE \bf *}
\put(1.83,  -.31){\LARGE \bf *}
%\put(2.83,  .69){\LARGE \bf *}


\put(2.9,-.1){\Large $\bullet$}
\put(3.9,-.1){\Large $\bullet$}
\put(5.9,-.1){\Large $\bullet$}
\put(4.9, .9){\Large $\bullet$}
\put(2.9,2.9){\Large $\bullet$}
\put(3.9,2.9){\Large $\bullet$}
\put(2.88, 1.88){\Large $\circ$}
\put(3.88, 1.88){\Large $\circ$}
\put(2.83,  .69){\LARGE \bf *}
\put(3.83,  .69){\LARGE \bf *}
\put(4.83,  -.31){\LARGE \bf *}
\put(5.83,  .69){\LARGE \bf *}

\put(7.9,-.1){\Large $\bullet$}
\put(8.9,-.1){\Large $\bullet$}
\put(10.9,-.1){\Large $\bullet$}
\put(9.9, .9){\Large $\bullet$}
\put(7.9,2.9){\Large $\bullet$}
\put(8.9,2.9){\Large $\bullet$}
\put(7.88, 1.88){\Large $\circ$}
\put(8.88, 1.88){\Large $\circ$}
\put(7.83,  .69){\LARGE \bf *}
\put(8.83,  .69){\LARGE \bf *}
\put(9.83,  -.31){\LARGE \bf *}
\put(10.83,  .69){\LARGE \bf *}

\end{picture}


<|FILE_SEP|>

% <|FILE: intro.tex|>
\thispagestyle{plain}
In this article we give an introduction to origamis (often also called 
square-tiled surfaces) and their Veech groups. As main theorem we prove 
that  in each genus there exist origamis, whose Veech groups 
are non congruence subgroups of $\slzwei(\ZZ

--- START OF DOCUMENT TAIL ---
_1(p)}

\newcommand{\Hquer}{\overline{H}}


%%%% aus definitions1.tex zu xorigamis:
\newcommand{\len}{\mbox{le}}
\newcommand{\nbx}{\sharp_x}
\newcommand{\nby}{\sharp_y}
\newcommand{\nbxb}{\sharp_{|x|}}
\newcommand{\nbyb}{\sharp_{|y|}}

\newcommand{\betahat}{\hat{\beta}}
\newcommand{\dy}{\Delta_y}


\newcommand{\norm}{\mbox{Norm}}
\newcommand{\emnorm}{\mbox{\em Norm}}
\newcommand{\asnt}{_{\mbox{\small{NT}}}}
\newcommand{\nt}{\mbox{NT}}
\newcommand{\ntn}{\unlhd}

\newcommand{\gk}{G_k}
\newcommand{\uk}{St_k}

\newcommand{\outplus}{\mbox{Out}^+} % for xorigami1.tex

%%%%%%%%%%%%%%%%%%%%% fuer congr.tex:
\newcommand{\gbh}{\Gammaquer_B} 

%%%%%%%%%%%%%%%%%%%% fuer org.tex
\newcommand{\tgn}{T_{g,n}}
\newcommand{\mgn}{M_{g,n}}
\newcommand{\mg}{M_g}
\newcommand{\tg}{T_g}

%%%%%%%%%%%%%%%%%%%%% fuer char.tex
\newcommand{\Xtilde}{\tilde{X}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\bpm}{\begin{pmatrix}}
\newcommand{\epm}{\end{pmatrix}}
\newcommand{\re}{\mbox{Re}}
\newcommand{\im}{\mbox{Im}}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2259
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: feedbackwirtap_ITv3.tex|>
%%Tex file of three-node for Allerton 2005
%%Lifeng Lai, OSU, 6-16-05
%\documentclass[12pt]{article}
\documentclass[12pt,draftcls, onecolumn,journal]{IEEEtran}
%\documentclass[12pt,twocolumn,journal]{IEEEtran}
\usepackage{times}
\usepackage[final]{graphicx}
\usepackage[reqno]{amsmath}
\usepackage{amsfonts}
%\renewcommand{\baselinestretch}{1.6}
%\usepackage{caption2}
\usepackage{times,amsmath,epsfig}
\usepackage{latexsym,amssymb}
%\usepackage{rotating,color}
\usepackage{cite}
%\evensidemargin=0.20in \oddsidemargin=0.20in \textwidth=6.25in
%\topmargin=0in \headheight=0.0in \headsep=0.0in \textheight=9.5in

%---------------
%\topmargin=0.5in \headheight=.2in \headsep=.2in \textwidth=6in
%\textheight=9in \footskip=.4in \oddsidemargin=.5in
%\evensidemargin=0.5in \hoffset=-0.7in \voffset=-.7in
%---------------

\setlength{\intextsep}{8pt plus 2pt minus 2pt}
%\renewcommand{\baselinestretch}{1.45}
%\setlength{\floatsep}{6pt plus 2pt minus 2pt}
%% Define Proof Environment
\def\myQED{\mbox{\rule[0pt]{1.5ex}{1.5ex}}}
\newenvironment{pf}{\noindent\hspace{2em}{\it Proof: }}
{\hspace*{\fill}~\myQED\par\endtrivlist\unskip}

\DeclareMathOperator{\mvec}{vec}
\DeclareMathOperator{\rank}{rank}
\DeclareMathOperator{\card}{card}
\DeclareMathOperator{\diag}{diag}

%% Define Theorem Enviroment
\newtheorem{thm}{Theorem}%[section]
\newtheorem{alg}[thm]{Algorithm}
\newtheorem{rl}[thm]{Rule}
\newtheorem{prop}[thm]{Proposition}
\newtheorem{lem}[thm]{Lemma}
%\newtheorem{cor}[thm]{Corollary}
\newtheorem{cor}{Corollary}
\newtheorem{define}[thm]{Definition}
%\newtheorem{define}{Definition}
%\newtheorem{rmk}[thm]{Remark}
\newtheorem{rmk}{Remark}
\newtheorem{exmpl}[thm]{Example}
\newcommand{\qed}{\hfill $\Box$}
\newcommand{\no}{\nonumber}
%\newenvironment{proof}{{\sl Proof\/}:\ \ }{\qed\vspace{\baselineskip}}

%\newenvironment{proof}{{\sl Proof\/}:\ \ }{\qed}
%-----------------------

%-----------------------


%\pagestyle{empty}

\begin{document}
%\renewcommand{\textfraction}{0}

\title{The Wiretap Channel with Feedback: Encryption over the Channel}

\author{%\normalsize
Lifeng Lai, Hesham El Gamal and H. Vincent Poor
\thanks{Lifeng Lai (llai@princeton.edu) was with
the Department of Electrical and Computer Engineering at the Ohio
State University, he is now is with the Department of Electrical
Engineering at Princeton University. Hesham El Gamal
(helgamal@ece.osu.edu) is with the Department of Electrical and
Computer Engineering at the Ohio State University. H. Vincent Poor
(poor@princeton.edu) is with the Department of Electrical
Engineering at Princeton University. This research was supported
by the National Science Foundation under Grants ANI-03-38807 and
CNS-06-25637.}}
\date{}
\maketitle %\pagestyle{plain}

%%%%%%%%%%%%%%% Article Body %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%=======================================================



--- START OF DOCUMENT TAIL ---
Computing}, (Monticello, IL), 2003.

\bibitem{Forney:TIT:00}
G.~D. {Forney, Jr.}, ``Sphere-bound-achieving coset codes and
multilevel coset
  codes,'' {\em IEEE Trans. on Information Theory}, vol.~46, pp.~820--850, May
  2000.

\bibitem{Eyuboglu:TIT:92}
M.~V. Eyuboglu and G.~D. {Forney, Jr.}, ``Trellis precoding:
Combined coding,
  precoding and shaping for intersymbol interference channels,'' {\em IEEE
  Trans. on Information Theory}, vol.~38, pp.~301--314, Mar. 1992.

\bibitem{Erez:TIT:04}
U.~Erez and R.~Zamir, ``Achieving $\frac{1}{2}\log(1 +
\text{SNR})$ on the
  {AWGN} channel with lattice encoding and decoding,'' {\em IEEE Trans. on
  Information Theory}, vol.~50, pp.~2293--2314, Oct. 2004.

\bibitem{ElGamal:TIT:041}
H.~{El Gamal}, G.~Caire, and M.~O. Damen, ``Lattice coding and
decoding achieve
  the optimal diversity-vs-multiplexing tradeoff of {MIMO} channels,'' {\em
  IEEE Trans. on Information Theory}, vol.~50, pp.~968--985, June 2004.

\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0112
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: PHSS_PartIII.tex|>
\documentclass[12pt]{article}
\usepackage{mathptmx}
\usepackage{graphicx}
\usepackage{bm}
\usepackage{amssymb}
\makeatletter
\author{Robert P. C. de Marrais \footnote{Email address:  rdemarrais@alum.mit.edu} \\ \noindent
\emph{Thothic Technology Partners, P.O.Box 3083, Plymouth MA 02361}}


\title{Placeholder Substructures III:~~  A Bit-String-Driven ``Recipe Theory'' for Infinite-Dimensional Zero-Divisor Spaces}

\begin{document}
\maketitle
\makeatother



--- START OF DOCUMENT TAIL ---
ontemporary Phenomenology and Cognitive Science} (Stanford
University Press:  Stanford, 1999)

\item \verb|[13]| Edward L. Robertson, ``An Algebra for Triadic
Relations,'' Technical Report No. 606, Computer Science Department,
Indiana University, Bloomington IN 47404-4101, January 2005; online
at http://www.cs.indiana.edu/ \newline
pub/techreports/TR606.pdf

\item \verb|[14]| E. F. Codd, \textit{The Relational Model for
Database Management:  Version 2} (Addison-Wesley:  Reading MA, 1990)
is the great visionary's most recent and comprehensive statement.

\item \verb|[15]| E. F. Codd, \textit{Cellular Automata} (Academic
Press:  New York, 1968)

\item \verb|[16]| Quinn Tyler Jackson, \textit{Adapting to Babel --
Adaptivity and Context-Sensiti- vity in Parsing:  From
$a^{n}b^{n}c^{n}$ to RNA} (Ibis Publishing:  P.O. Box3083, Plymouth
MA 02361, 2006; for purchasing information, contact Thothic
Technology Partners, LLC, at their website, www.thothic.com).

\end{description}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1070
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: DPSK_ISIT.tex|>
\documentclass[a4paper,10pt,conference]{IEEEtran}

%\topmargin -0.2in

\usepackage[dvipdf]{graphicx}
\usepackage{epsfig}
\usepackage{color}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\usepackage{amsmath}
\usepackage{amssymb}



\begin{document}

\title{\huge{Differential Diversity Reception of MDPSK over Independent Rayleigh Channels with Nonidentical Branch 
Statistics and Asymmetric Fading Spectrum}}

\author{
\authorblockN{Hua Fu and Pooi Yuen Kam}
\authorblockA{ECE Department, National University of Singapore \\ 
Singapore 117576, Email: \{elefh, elekampy\}@nus.edu.sg}
\vspace{-20pt}
}

\maketitle




--- START OF DOCUMENT TAIL ---
ncludegraphics[height=0.1\textwidth,width=0.45\textwidth]
{Goodman.eps}
\caption{Illustration of complex channel fading process.}
\end{figure}
%%--------------------------------------------------------------------
\begin{figure}[ht]
\center
\includegraphics[height=0.4\textwidth,width=0.45\textwidth]
{PSK_8.eps}
\caption{8-DPSK constellation and decision region.}
\end{figure}
%%--------------------------------------------------------------------
%%-------------------------
\begin{figure}[h]
\centerline{\epsfxsize=8.5cm\epsfysize=7.0cm\epsffile{DPSK_ISIT.eps}}
\caption{BEP comparison of the three individual bits and the average of all bits for 8-DPSK.}
\end{figure}
%%-------------------------
%\begin{figure}[h]
%\center
%\includegraphics[height=0.43\textwidth,width=0.5\textwidth]
%{DPSK_ISIT.eps}
%\caption{BEP comparison of the three individual bits and the average of all bits for 8-DPSK.}
%\end{figure}
%%--------------------------------------------------------------------
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2362
```latex
--- START OF DOCUMENT HEAD ---
eme]{Exemple}
\newtheorem{Definition}[Theoreme]{D\'efinition}
\newtheorem{Remark1}[Theorem]{Remark}
\newtheorem{Not}[Theoreme]{Notation}
\newtheorem{Nota}[Theorem]{Notation}
\newtheorem{Propo}[Theorem]{Proposition}
\newtheorem{exercice1}[Th]{Lemme-Confii au lecteur}
\newtheorem{Corollary}[Theorem]{Corollary}
\newtheorem{PPtes}[Th]{Propri\'et\'es}
\newtheorem{Def}[Theorem]{Definition}
\newtheorem{Defi}[Theorem]{Definition}
\newtheorem{Example1}[Theorem]{Example}
\newenvironment{Proof}{\medbreak{\noindent\bf Proof }}{~{\hfill $\bullet$\bigbreak}}

\newenvironment{Demonstration}{\medbreak{\noindent\bf D\'emonstration
 }}{~{\hskip 3pt$\bullet$\bigbreak}} 

\newenvironment{Remarque}{\begin{Remarque1}\em}{\end{Remarque1}} 
\newenvironment{Remark}{\begin{Remark1}\em}{\end{Remark1}}
\newenvironment{Exemple}{\begin{Ex}\em}{~{\hskip
3pt$\bullet$}\end{Ex}} 
\renewenvironment{abstract}{\medbreak{\noindent\bf Abstract :
 }}{\bigbreak}
\newenvironment{Notation}{\begin{Not}\em}{\end{Not}}
\newenvironment{Notation1}{\begin{Nota}\em}{\end{Nota}}
\newenvironment{Example}{\begin{Example1}\em}{~{\hskip
3pt$\bullet$}\end{Example1}} 

\newenvironment{Remarques}{\begin{Remarque1}\em \ \\* }{\end{Remarque1}}

\renewcommand{\Re}{{\cal R}}
\newcommand{\Dim}{{\rm Dim\,}}
\renewcommand{\Im}{{\cal F}}
\newcommand{\finpreuve}{~{\hskip 3pt$\bullet$\bigbreak}}
\newcommand{\hp}{\hskip 3pt}
\newcommand{\hph}{\hskip 8pt}
\newcommand{\hphh}{\hskip 15pt}
\newcommand{\vp}{\vskip 3pt}
\newcommand{\vpv}{\vskip 15pt}
\newcommand{\IP}{{\mathbb{IP}}}
\newcommand{\rd}{{\mathbb R}^2}
\newcommand{\R}{{\mathbb R}}

\newcommand{\Hyper}{{\mathbb H}}
\newcommand{\Int}{{\mathbb I}}
\newcommand{\Boule}{{\mathbb B}(0,1)}
\newcommand{\Cantor}{{\mathbb K}}
\newcommand{\dist}{{\mbox{\em dist}}}
\newcommand{\K}{{\mathbb K}}
\newcommand{\B}{{\mathbb B}}
\newcommand{\Ho}{{\mathbb H}}
\newcommand{\Nat}{{\mathbb N}}
\newcommand{\N}{{\mathbb N}}
\renewcommand{\P}{{\mathbb P}}
\newcommand{\Esp}{{\mathbb E}}
\newcommand{\Complex}{{\mathbb C}}
\newcommand{\Ha}{{\cal H}}
\newcommand{\Harm}{{\bold H}}
\newcommand{\Lcal}{{\cal L}}
\newcommand{\ds}{\displaystyle}
\newcommand{\un}{\bold 1}
\newcommand{\Cone}{C(x,r,\varepsilon ,\Phi)}
\newcommand{\Cn}{C(x,2^{-n},\varepsilon ,\Phi )}
\newcommand{\Tranche}{W(x,r,\varepsilon,\Phi)}
\newcommand{\Wn}{W(x,2^{-n},\varepsilon,\Phi)}
\newcommand{\WFn}{W(x,2^{-n},\varepsilon,\Phi)\cap F}
\newcommand{\ovec}{\overrightarrow}
\newcommand{\red}{{\bold R}}
\newcommand{\dimH}{\dim_{\Ha}}
\newcommand{\diam}{\mbox{diam}}
\newcommand{\diamit}{\mbox{\em diam}}
\newcommand{\para}{\vskip 2mm}
\newcommand{\cod}{\stackrel{\mbox{\tiny cod}}{\sim}}
\newcommand{\cardit}{\mbox{\em card}}
\newcommand{\card}{\mbox{card}}
\newcommand{\Sphere}{{\mathbb S}_d}
\newcommand{\distit}{\mbox{\em dist}}
\newcommand{\Tri}{{\cal P}}
\newcommand{\LL}{{\mathcal L}}
\newcommand{\infess}{\mbox{inf\,ess}}
\newcommand{\supess}{\mbox{sup\,ess}}
\newcommand{\I}{\vert}

\definecolor{darkblue}{rgb}{0,0,.5}
\def\u{\underline }
\def\o{\overline}
\def\h{\hskip 3pt}
\def\hh{\hskip 8pt}
\def\hhh{\hskip 15pt}
\def\v{\vskip 8pt}
\def\vv{\vskip 15pt}
\font\courrier=cmr12
\font\grand=cmbxti10
%\font\larger=cmbxti10
\font\large=cmbx12
\font\largeplus=cmr17
\font\small=cmbx8
\font\nor=cmbxti10
\font\smaller=cmr8
\font\smallo=cmbxti10
\openup 0.3mm
%\setbox1\vbox{\hspace{.1cm}{\Large \bf\color{darkblue}Athanasios BATAKIS}%
%
%{\small\em \noindent \hskip 10mm  D\'epartement de Math\'ematiques
%\vskip-2mm
%\noindent \hskip 20mm  Universit\'e d'Orl\'eans
%\vskip-2mm
%\noindent \hskip 18mm  45067 Orl\'eans cedex 2
%\vskip-2mm
%\noindent \hskip 21mm T\'el : 02.38.41.73.15}
%
%\noindent e-mail : Athanasios.Batakis@univ-orleans.fr}
%\ht1=12mm \dp1=10mm \wd1=0mm
%
%\setbox3\hbox {\box1  \hskip 115mm}
%\
%\vskip -1cm \hskip -2cm \box3

\title{\color{blue} On Brownian flights}
\author{Athanasios BATAKIS\footnote{MAPMO} , Pierre LEVITZ\footnote{LPMC, Ecole Polytechnique} and Michel ZINSMEISTER{$^*$}}
\date{}
\maketitle


--- START OF DOCUMENT TAIL ---
low from the previous discussion because the corresponding domains do not have the corkscrew property. But, as Rohde and Schramm have proved, these domains are H\" older, i.e. the Riemann mapping from the upper half-plane onto the half-plane minus the $SLE_{\kappa}$ curve up to time $t$ is H\"'older continuous . This condition implies a weaker form of the the corkscrew condition which is sufficient to ensure the possibility to compute the Minkowski dimension of the $SLE_{8/3}$ curve via the counting of Whitney cubes. As we have seen this is enough to prove the main result about statistics of flights at least for a sequence of times going to $\infty$.

%This rigorous result, combined with the preceeding simulations,  may serve as a new argument to support the conjecture.

 %It is to be noticed that, using quantum gravity arguments, Duplantier  also obtained the right exponents for all  $SLE_{\kappa}$(cf. \cite{Duplantier})
\bibliographystyle{alpha}
\bibliography{biblio}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2471
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: tropJ-TodaBBSFinal.tex|>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%  Tropical spectral curves and integrable cellular automata
%
%  by Rei Inoue and Tomoyuki Takenawa
%  
%  Submitted version: April 19, 2007
%  Accepted by IMRN: February 4, 2008
%  Final version: February 7, 2008
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\documentclass[a4paper,11pt]{amsart}
\pagestyle{plain}
\def\baselinestretch{1.3}
\tolerance 2000
\textwidth 15cm
\textheight 23cm
\topmargin -.0cm
\oddsidemargin 0.5cm
\evensidemargin 0.5cm


\usepackage{amsmath}
\usepackage{amstext,amsfonts,amsbsy,eucal,amssymb}

\usepackage{arrow}

\numberwithin{equation}{section}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\newtheorem{remark}[theorem]{Remark}

\newcommand{\e}{\operatorname{\mathrm{e}}}
\newcommand{\R}{\operatorname{\mathbb{R}}}
\newcommand{\Z}{\operatorname{\mathbb{Z}}}
\newcommand{\C}{\operatorname{\mathbb{C}}}
\newcommand{\I}{\operatorname{\mathbb{I}}}
\newcommand{\Div}{\operatorname{\mathrm{Div}}}
\newcommand{\Log}{\operatorname{\mathrm{Log}}}

\def\ba{\begin{array}}
\def\ea{\end{array}}
\def\pic{{\rm Pic}}
\def\div{{\rm Div}}
\def\rank{{\rm rank}}
\def\noi{\noindent}
\def\nn{\nonumber}
\def\vp{\varphi}
\def\al{\alpha}
\def\ve{\varepsilon}
\def\chal{\alpha^{\vee}}
\def\mc{{\mathbb C}}
\def\mz{{\mathbb Z}}
\def\mq{{\mathbb Q}}
\def\mr{{\mathbb R}}
\def\mpp{{\mathbb P}}
\def\disp{\displaystyle}

%% color 
\usepackage[dvipdfm]{graphicx,color}
%\usepackage[dviout]{graphicx,color}
%\usepackage[dvips]{graphicx,color}

\definecolor{spot}{cmyk}{1,0,0,0}
%\usepackage[abs]{overpic}
%\usepackage{mediabb}
%\usepackage{pict2e}


\begin{document}

%\parskip 7pt
%\baselineskip 16pt



\title{\large 
Tropical spectral curves and integrable cellular automata
}

\author{Rei Inoue}
\address{Department of Physics, Graduate School of Science,
The University of Tokyo,
7-3-1 Hongo, Bunkyo-ku, Tokyo 113-0033, Japan
\newline
CREST, JST, 4-1-8 Honcho Kawaguchi, Saitama 332-0012, Japan}
\email{reiiy@spin.phys.s.u-tokyo.ac.jp}


\author{Tomoyuki Takenawa} 
\address{Faculty of Marine Technology, 
Tokyo University of Marine Science and Technology,  
2-1-6 Etchu-jima, Koto-Ku, Tokyo, 135-8533, Japan}
\email{takenawa@kaiyodai.ac.jp }



--- START OF DOCUMENT TAIL ---
4 (1979). 

\bibitem{NagaiTokihiroSatsuma98}
A.~Nagai, T.~Tokohiro and J.~Satsuma,
{\it Ultra-discrete Toda molecule equation},
Phys. Lett. A, \textbf{244}, 383-388 (1998).

\bibitem{SpeyerSturm04}
D.~Speyer and B.~Sturmfels,
{\it Tropical Mathematics},
math.CO/0408099.

\bibitem{TakaMatsu95}
D.~Takahashi and J.~Matsukidaira,
{\it On discrete soliton equations related to cellular automata},
Phys. Lett. A, \textbf{209}, 184-188 (1995). 

\bibitem{TakahashiSastuma90}
D. Takahashi and J. Satsuma, 
{\it A soliton cellular automaton},
J. Phys. Soc. Japan, \textbf{59}, 3514-3519 (1990).

\bibitem{TTMS96}
T.~Tokihiro, D.~Takahashi, J.~Matsukidaira and J.~Satsuma,
{\it From Soliton Equations to Integrable Cellular Automata 
through a Limiting Procedure},
Phys. Rev. Lett., \textbf{76}, 3247-3250 (1996).
 
\bibitem{YuraTokihiro02}
F.~Yura and T.~Tokihiro,
{\it On a periodic soliton cellular automaton},
J. Phys. A: Math. Gen. \textbf{35}, 3787-3801 (2002).

\end{thebibliography}


\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1613
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: 07jpa.tex|>
\documentclass[12pt]{iopart}
\eqnobysec
% Uncomment next line if AMS fonts required
\usepackage{iopams,amsthm,graphicx,cite}
%\usepackage{epsf,latexsym}
%\usepackage{amssymb,amsmath}
%\usepackage{times}
%\usepackage{amscd}
 

\topmargin-1.2cm


\begin{document}


%%%%%%%%%%%%---ARROWS FOR CONVERGENCE----%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\llra{\relbar\joinrel\longrightarrow}              %THIS IS LONG
\def\mapright#1{\smash{\mathop{\llra}\limits_{#1}}}    %ARROW ON LINE
\def\mapup#1{\smash{\mathop{\llra}\limits^{#1}}}     %CAN PUT SOMETHING OVER IT
\def\mapupdown#1#2{\smash{\mathop{\llra}\limits^{#1}_{#2}}} %over&under it%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%% These are the AMS constructs for multiline limits %%%%%%%%%%%%
\catcode`\@=11

\def\BF#1{{\bf {#1}}}
\def\NEG#1{{\rlap/#1}}

\def\Let@{\relax\iffalse{\fi\let\\=\cr\iffalse}\fi}
\def\vspace@{\def\vspace##1{\crcr\noalign{\vskip##1\relax}}}
\def\multilimits@{\bgroup\vspace@\Let@
 \baselineskip\fontdimen10 \scriptfont\tw@
 \advance\baselineskip\fontdimen12 \scriptfont\tw@
 \lineskip\thr@@\fontdimen8 \scriptfont\thr@@
 \lineskiplimit\lineskip
 \vbox\bgroup\ialign\bgroup\hfil$\m@th\scriptstyle{##}$\hfil\crcr}
\def\Sb{_\multilimits@}
\def\endSb{\crcr\egroup\egroup\egroup}
\def\Sp{^\multilimits@}
\let\endSp\endSb

%%%%%%%%%%%%%%%%%%%%END of explanations for multiline limits %%%%%%%%%%%%%%%%

\title[]{Reply to ``Comment on `On the inconsistency of the Bohm-Gadella
theory with quantum mechanics'\,''}


\author{Rafael de la Madrid}
\address{Department of Physics, University of California at San Diego,
La Jolla, CA 92093 \\
E-mail: \texttt{rafa@physics.ucsd.edu}}


\date{\small{(March 14, 2007)}}





--- START OF DOCUMENT TAIL ---
5);
{\sf quant-ph/0502053}.

\bibitem{LS1} R.~de la Madrid, J.~Phys.~A:~Math.~Gen.~{\bf 39}, 3949 (2006);
{\sf quant-ph/0603176}. 

\bibitem{LS2} R.~de la Madrid, J.~Phys.~A:~Math.~Gen.~{\bf 39}, 3981 (2006);
{\sf quant-ph/0603177}. 

\bibitem{TAYLOR} J.R.~Taylor, \emph{Scattering theory}, John Wiley \& 
Sons, Inc., New York (1972).

\bibitem{BLUNDER} A.~Bohm, P.~Kielanowski, S.~Wickramasekara, 
``Complex energies and beginnings of time suggest a theory of scattering
and decay,'' {\sf quant-ph/0510060}.

\bibitem{BG} A.~Bohm, M.~Gadella, \emph{Dirac Kets, Gamow 
Vectors and Gelfand Triplets}, Springer Lecture Notes in 
Physics~{\bf 348}, Berlin (1989).

\bibitem{SIMON} M.~Reed, B.~Simon, {\it Methods of Modern Mathematical
Physics,} Vol.~II, Academic Press, New York (1975).

\bibitem{YOSHI} Y.~Strauss, L.P.~Hortwitz, A.~Volovick,
``Approximate resonance states in the semigroup decomposition of
resonance evolution,'' {\sf quant-ph/0612027}. 




\end{thebibliography}




\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1696
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: helsi0.tex|>


%Example of contribution to ICANN'94
%\documentstyle[twoside,icann94]{article}
%\pagestyle{empty}
%
%documentstyle[a4wide,12pt]{article}
%\usepackage{a4wide}
%\usepackage{a4wide,french}
%\usepackage[francais]{babel}
%
\documentclass[12pt]{article}
\usepackage{Wsom97}
%\usepackage[cp850]{inputenc}
%\usepackage[pc850]{inputenc}  %%% acquisition 8 bits : accents � � ..
%\usepackage{t1enc}
% TITLE
\begin{document}
\title{\bf Theoretical Aspects of the SOM Algorithm}
%
% AUTHORS
\author{\large M.Cottrell$^\dagger$,
J.C.Fort$^\ddagger$, G.Pag\`es$^\ast$\\
  \normalsize $\dagger$ SAMOS/Universit\'e Paris 1\\
  \normalsize 90, rue de Tolbiac, F-75634 Paris Cedex 13, France\\
  \normalsize Tel/Fax : 33-1-40-77-19-22, E-mail: cottrell@univ-paris1.fr\\
  \normalsize $\ddagger$ Institut Elie Cartan/Universit\'e Nancy 1 et SAMOS\\
  \normalsize F-54506 Vand\oe uvre-L\`es-Nancy Cedex, France\\
  \normalsize E-mail: fortjc@iecn.u-nancy.fr\\
  \normalsize $\ast$ Universit\'e Paris 12 et Laboratoire de Probabilit\'es
                        /Paris 6\\
  \normalsize F-75252 Paris Cedex 05, France\\
  \normalsize E-mail:gpa@ccr.jussieu.fr}

\date{}

\newtheorem{madef}{Definition}
\newtheorem{monthe}{Theorem}


\maketitle
\thispagestyle{empty}
%
%


--- START OF DOCUMENT TAIL ---
nancial applications.

\section{Conclusion}

So far, the theoretical study in the one-dimensional case is nearly complete. 
It remains to find the convenient decreasing rate to ensure the ordering. 
For the multidimensional setting, the problem is difficult. It seems that 
the Markov chain is irreducible and that further results could come from 
the careful study of the Ordinary Differential Equation (ODE) and from the 
powerful existing results about the cooperative dynamical systems. 

On the other hand, the applications are more and more numerous, especially 
in data analysis, where the representation capability of the organized data 
is very valuable. The related methods make up a large and useful set of 
methods which can be substituted to the classical ones. To increase their 
use in the statistical community, it would be necessary to continue the 
theoretical study, in order to provide quality criteria and performance 
indices with the same rigour as for the classical methods.
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2402
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: indicesLyapunov.tex|>
\documentclass[a4paper,11pt]{article}
\usepackage[latin1]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{eurosym}
\usepackage[pdftex,usenames,dvipsnames]{color}
\usepackage[pdftex]{graphicx}

\usepackage{hyperref}

\usepackage{caption2}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{fancybox}
\usepackage{amscd}
\usepackage{amsthm}


\theoremstyle{plain}
\newtheorem{Thm}{Theorem}
\newtheorem{Cor}{Corollary}
\newtheorem{Main}{Main Theorem}
\newtheorem{Lem}{Lemma}
\newtheorem{Prop}{Proposition}
\theoremstyle{definition}
\newtheorem{Def}{Definition}
\newtheorem{Remark}{Remark}
\theoremstyle{remark}
\newtheorem{notation}{Notation}
\numberwithin{equation}{section}



\title{
Indices of
   the iterates of \({\Bbb R}^3\)-homeomorphisms at Lyapunov stable fixed points}




\author{Francisco R. Ruiz del Portal and Jos� M. Salazar \thanks{ The authors have been supported by MEC,
MTM 2006-0825. \newline 2000 {\em Mathematics Subject
Classification}: 37C25, 37B30, 54H25.
\newline {\em Keywords and phrases.} Fixed point index, Conley index.}}







\begin{document}








\maketitle































--- START OF DOCUMENT TAIL ---
}, preprint.


\bibitem{RS2}
F.R. Ruiz del Portal, J.M. Salazar, {\em Fixed point indices of
the iterations of \({\Bbb R}^3\)-homeomorphisms}, preprint.


\bibitem{SS}
M. Shub and D. Sullivan, {\em A remark on the Lefschetz fixed
point formula for differentiable maps}, Topology, 13 (1974),
189-191.

\bibitem{Va}
J. Vaughan Ed.  {\em Open problems collected from the Spring
Topology and Dynamical Systems Conference 2006}.
http://www.uncg.edu/mat/stdc

\bibitem{W}
F.W. Wilson, {\em On the minimal sets of non-singular vector
fields}, Annals of Math. 84 (1966) 529-536.


\end{thebibliography}


\medskip
\medskip

Francisco R. Ruiz del Portal

Departamento de Geometr�a y Topolog�a, Facultad de
CC.Mate\-m\'{a}\-ti\-cas, Universidad Complutense de Madrid,
Madrid 28040, Spain.

E-mail: R\(_{-}\)Portal@mat.ucm.es

\medskip
\medskip

Jos� Manuel Salazar.

Departamento de Matem�ticas. Universidad de Alcal�.  Alcal�
de Henares. Madrid 28871, Spain.

E-mail: josem.salazar@uah.es





\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1272
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: arxiv_final.tex|>

\documentclass[12pt,titlepage,aps,amssymb]{amsart}
\usepackage{graphicx,amsmath,amsthm, amssymb}
\newcommand{\ben}{\begin{enumerate}}
\newcommand{\een}{\end{enumerate}}
\newcommand{\tf}{\tilde f}
\newcommand{\tg}{\tilde g}
\newcommand{\T}{ \mathrm{T}}
\def\wh{\widehat}

\def\half{\frac{1}{2}}
\def\quart{\frac{1}{4}}
\def\third{\frac{1}{3}}
\def \bc{\vskip 0cm \begin{center}}
\def \ec{\end{center} \vskip 0cm}
\def \be{\begin{equation}}
\def \ee{\end{equation}}
\def \bea{\begin{eqnarray}}
\def \eea{\end{eqnarray}}



\newtheorem{thm}{Theorem}[section]
\newtheorem{cor}[thm]{Corollary}
\newtheorem{lem}[thm]{Lemma}
\newtheorem{prop}[thm]{Proposition}
\newtheorem{con}{Conclusion}
\theoremstyle{remark}
\newtheorem*{rem}{Remark}
%\theoremstyle{definition}
\newtheorem{Def}[thm]{Definition}
\newtheorem{exm}{Example}



\begin{document}
\pagestyle{plain}
\begin{center}
\vspace{4cm}

{\Large {\bf Dynamics of shear homeomorphisms of tori and the Bestvina-Handel algorithm
}}\vskip 1cm
\large{Tali Pinsky and Bronislaw Wajnryb}
\end{center}
\vskip 2cm

\section*{Abstract}
Sharkovskii proved that the existence of a periodic orbit of period which is not a power of 2 in a one-dimensional dynamical system implies existence of infinitely many periodic orbits. We obtain an analog of  Sharkovskii's theorem for periodic orbits of shear homeomorphisms of the torus. This is done by obtaining a dynamical order relation on the set of simple orbits and simple pairs.
We then use this order relation for a global analysis of a
quantum chaotic physical system called the kicked
accelerated particle.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Introduction}
Given a dynamical system $(X,f)$, a key question is which periodic orbits exist for this system. Since periodic orbits are in general difficult to compute, we would like to have the means to deduce their existence without having to actually compute them. 

Sharkovskii addressed the dynamics of continuous maps on the real line. He defined an order $\lhd$ on the natural numbers, Sharkovskii's order (see \cite{Misiurewicz}), and proved that the existence of a periodic orbit of a certain period $p$ implies the existence of an orbit of any period $q\lhd p$. We say the $q$ orbit is \emph{forced} by the $p$ orbit. This offers the means of showing the existence of many orbits if one can find a single orbit of ``large" period. For a dynamical system depending on a single parameter, if periodic orbits appear when we change the parameter, they must appear according to the Sharkovskii's order.  Hence, Sharkovskii's theorem gives the global structure of the appearance of periodic orbits for one dimensional systems. 
Ever since the eighties there has been interest in obtaining analogs for Sharkovskii's theorem for two dimensional systems (see \cite{Boy3} and \cite{Matzuoka}). 

A homeomorphism of a torus is said here to be of {\it shear type} if it is isotopic to one Dehn twist along a single closed curve. 
Let $h$ be a shear homeomorphism, and let $x$ be a periodic orbit of $h$. We
can then define the \emph{rotation number} of $x$, see discussion in Section \ref{simple section}. Thus, a rational number in the unit interval $[0,1)$ is associated to each orbit. 

We consider orbits up to conjugation: orbits $(x,f)$  and  $(y,g)$ are
\emph{similar} (of the same type) if there exists a homeomorphism $h$ of the torus $T^2$ such that $h$ is isotopic to the identity, $h$ takes
orbit $x$ onto orbit $y$  and   $hfh^{-1}$ is isotopic to $g$ rel $y$. 
We define below a specific family of periodic orbits we call simple orbits. In this family there is a unique element up to similarity corresponding to each rotation number; hence they can be specified by their rotation numbers. We emphasize it is not true in general that an orbit of a shear homeomorphism is characterized by its rotation number.

Simple orbits 

--- START OF DOCUMENT TAIL ---
des}, submitted for publiaction in Nonlinearity,
(quant-ph/0512086)
\bibitem{Misiurewicz} M. Misiurewicz, \emph{Rotation Theory} in: Online Proceedings of the RIMS  Workshop on "Dynamical Systems and Applications: Recent Progress".

\bibitem{exp} Z-Y. Ma, M.B. d'Arcy and S. Gardiner, {Phys. Rev. Lett.} \textbf{93} (2004), 
164101-1-4.

\bibitem{Matzuoka} T. Matsuoka, \emph{Braids of periodic points and a 2-dimensional analogue of Sharkovskii’s ordering}, {World Sci. Adv. Ser. in Dynamical Systems} \textbf{1} (1986), 58–72.

\bibitem{ox} M.K. Oberthaler, R.M. Godun, M.B. d'Arcy, G.S. Summy, and K.
Burnett, {Phys. Rev. Lett.}  \textbf{83} (1999), 4447-4451.

\end{thebibliography}
\vskip 1cm

Tali Pinsky

Department of Mathematics

The Technion

32000 Haifa, Israel

e-mail:  otali@tx.technion.ac.il

\par\bigskip

Bronislaw Wajnryb

Department of Mathematics 

Rzeszow University of Technology

ul. W. Pola 2, 35-959 Rzeszow, Poland

e-mail:  dwajnryb@prz.edu.pl
\par\bigskip

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1764
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: RF2.tex|>
\documentclass[reqno]{article}
\usepackage{amsmath, amsthm, graphicx}
\theoremstyle{plain}
\newtheorem*{thm}{Theorem}
\usepackage{setspace}
\doublespacing
\parindent=0pt
\usepackage{ifthen}
\def\defas{\; \buildrel\rm def\over= \;}
\def\multsp{\>}
\begin{document}
\bibliographystyle{amsalpha}
\title{Another Riemann-Farey Computation}
\author{Scott B. Guthery\\sguthery@mobile-mind.com}
\maketitle

The Riemann hypothesis is true if and only if
\begin{equation}\label{EQ1}
R(m) = \sum_{i=2}^{T_{m}}\left({F_m(i) - \frac{i}{n}}\right)^2 =
O(m^{-1+\epsilon})
\end{equation}
where $F_m(i)$ is the $i^{th}$ element in the Farey sequence of
order $m$ and
$$
T_m=\sum_{k=2}^m \phi(k)\text{.}
$$

Let $P_m(k)$ be sum of the $\phi(k)$ terms in (\ref{EQ1}) with Farey
denominator $k$ so that

\begin{equation}\label{EQ2}
R(m) = \sum_{k=2}^m P_m(k)
\end{equation}

\pagebreak

Figure~\ref{FIG1} is a plot of $P_m(k)$ for $m = 500$.

\begin{figure}[h!]
\begin{center}
\leavevmode
  \includegraphics[width=100mm]{ThirdFareyFigure1.eps}\\
  \end{center}\caption{$P_{m}(k)$ for $m=500$}\label{FIG1}
\end{figure}


Let $Q_{m}(k,i)$ denote the term with numerator $i$ in $P_{m}(k)$ so
that

\begin{equation}\label{EQ3}
P_m(k) = \sum_{i=1}^m Q_{m}(k,i)
\end{equation}

and we note in passing that for all but small values of $m$ and $k$,

\begin{equation}\label{EQ4}
Q_{m}(k,1) \gg Q_{m}(k,j)
\end{equation}

for $j>1$.

\pagebreak

The solid line in Figure~\ref{FIG3} is four times $Q_{500}(k,1)$
plotted with $P_{500}(k)$.

\begin{figure}[h!]
\begin{center}
\leavevmode
  \includegraphics[width=100mm]{ThirdFareyFigure3.eps}\\
  \end{center}\caption{$P_{500}(k)$ and $4 Q_{500}(k,1)$}\label{FIG3}
\end{figure}

Thus, we are led to consider

\begin{equation}\label{EQ5}
R(m) < C \sum_{k=2}^m Q_m(k,1)
\end{equation}

\pagebreak

For $83 \leq k \leq 500$, $Q_{500}(k,1)$ is given by

\begin{equation}\label{EQ6}
Q_{500}(k,1) =
\begin{cases}

\left(\frac{501-k}{76116} - \frac{1}{k}\right)^2,&

250 \leq k \leq 500\\

\left(\frac{249+2(251-k)}{76116} - \frac{1}{k}\right)^2,&

167 \leq k < 250\\

\left(\frac{413+4(168-k)}{76116} - \frac{1}{k}\right)^2,&

125 \leq k < 167\\

\left(\frac{579+6(126-k)}{76116} - \frac{1}{k}\right)^2,&

100 \leq k < 125\\

\left(\frac{725+10(101-k)}{76116} - \frac{1}{k}\right)^2,&

83 \leq k < 100
\end{cases}
\end{equation}

Each case in (\ref{EQ5}) corresponds to a constant step size between
adjacent Farey numbers of the form $\frac{1}{k}$. This step size is
the factor of $(a-k)$ in the case.

\pagebreak

Considering the top case in equation (\ref{EQ4}), for $\frac{m}{2}
\leq k \leq m$ we have in general

\begin{equation}
Q_m(k,1) = \left(\frac{m+1-k}{\sum_{j=2}^m
\phi(j)}-\frac{1}{k}\right)^2
\end{equation}

Substituting the approximation $\frac{3 m^2}{\pi ^2}$ for the
totient sum and integrating from $m/2$ to $m$, we have

\begin{equation}
\begin{split}
\hat{R}(m) = \frac{12\pi^4 + 6m(\pi^4-24\pi^2 \log{2})+
m^2(216+\pi^4-72\pi^2(\log{4}-1))}{216 m^3}\\
\approx \frac{0.180 m^2-1.855 m+5.41}{m^3}
\end{split}
\end{equation}

with

\begin{equation}
\lim_{m\to \infty} \hat{R}(m)/m^{-1+\epsilon} = 0
\end{equation}

 \pagebreak

In general, each of the $n$ terms in (\ref{EQ1}) can be represented
as

\begin{equation}\label{EQ7}
\left(\frac{a + b k}{\sum_{j=2}^m \phi(j)} - \frac{i}{k}\right)^2
\end{equation}

for $[m/c] \le k < [m/c]+1$ and $a$, $b$ and $c$ depending on $m$,
$k$ and $i$.

As above, substituting the approximation $\frac{3 m^2}{\pi ^2}$ for
the totient sum, integrating from $\frac{m}{c}$ to $\frac{m}{c}+1$
for each term and then summing over the $n$ terms, we have

\begin{equation}
\begin{split}
R(m) < \hat{R}(m) = C \sum_{k,i}{\frac{27 c^4 i^2 m^3 - 18 b c^2 i
m^2 (c+m) \pi^2 +
18 a c^2 i m^2(c+m)\pi^2\log{\frac{m}{(m + c)}}}{27 c^2(m + c) m^4}}\\
+\frac{(m + c)(3 a^2 c^2 + 3a b c (c+2m) + b^2(c^2+3 c m + 3 m^2))
\pi^4}{27 c^2(m + c) m^4}
\end{split}
\end{equation}

where the constant $C$ accounts for the totient sum appr

--- START OF DOCUMENT TAIL ---
nfty} \hat{R}(m)/m^{-1+\epsilon} = 0
\end{equation}

 \pagebreak

In general, each of the $n$ terms in (\ref{EQ1}) can be represented
as

\begin{equation}\label{EQ7}
\left(\frac{a + b k}{\sum_{j=2}^m \phi(j)} - \frac{i}{k}\right)^2
\end{equation}

for $[m/c] \le k < [m/c]+1$ and $a$, $b$ and $c$ depending on $m$,
$k$ and $i$.

As above, substituting the approximation $\frac{3 m^2}{\pi ^2}$ for
the totient sum, integrating from $\frac{m}{c}$ to $\frac{m}{c}+1$
for each term and then summing over the $n$ terms, we have

\begin{equation}
\begin{split}
R(m) < \hat{R}(m) = C \sum_{k,i}{\frac{27 c^4 i^2 m^3 - 18 b c^2 i
m^2 (c+m) \pi^2 +
18 a c^2 i m^2(c+m)\pi^2\log{\frac{m}{(m + c)}}}{27 c^2(m + c) m^4}}\\
+\frac{(m + c)(3 a^2 c^2 + 3a b c (c+2m) + b^2(c^2+3 c m + 3 m^2))
\pi^4}{27 c^2(m + c) m^4}
\end{split}
\end{equation}

where the constant $C$ accounts for the totient sum approximation
and

\begin{equation}
\lim_{m\to \infty}\hat{R}(m)/m^{-1+\epsilon} = 0
\end{equation}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1625
```latex
--- START OF DOCUMENT HEAD ---

% The file compiles with the IJFCS package, however
% the definitions of theorems, lemmas, etc, and
% the temporary defintions of title, author font style, etc
% below should be removed.
%
% There is one problem with the proof environment.
% We use proof with
%
% \begin{proof}[Optional text]
% ...
% \end{proof}
%
% I am not sure how to use it with the IFCS package to get the optional text show correctly.
% Two proofs use this optional text:
% The proof right after Equation 8 and the proof in Section 3.2.
% If necessary, remove the Optional text. The paper would still be ok without this
% optional text.



\documentclass[a4paper,12pt]{article}

\usepackage{graphicx}
\usepackage{fullpage}

\usepackage{amsthm, amsmath, amsfonts, amssymb}

\theoremstyle{plain}
\newtheorem{definition}{Definition}
\theoremstyle{plain}
\newtheorem{theorem}[definition]{Theorem}
\newtheorem{lemma}[definition]{Lemma}
\newtheorem{corollary}[definition]{Corollary}
\theoremstyle{definition}
\newtheorem{example}[definition]{Example}

% To make the IJFCS commands to work
\def\copyrightheading{~}
\newcommand{\fcstitle}[1]{{\LARGE {#1}}}
\def\authorfont{\large}
\def\addressfont{\normalfont}
\def\smalllineskip{\smallskip}
\def\textlineskip{\medskip}
\def\keywords{\\~\\\textit{Keywords:}~}





% OWN DEFINITIONS
% ---------------

\def\epsilon{\varepsilon}

\def\dtv{d_{\textup{TV}}}

\def\Prob{\textnormal{Pr}}
\def\colour{\textup{colour}}

\def\Pk{P^{[k]}}
\def\Pj{P^{[j]}}
\def\PI{P^{[i]}}
\def\P1{P^{[1]}}
\def\Pm{P^{[m]}}
\def\Ham{\textnormal{Ham}}

\def\Pgrid{P_{\textup{grid}}}

\def\M{\mathcal{M}}
\def\gridscan{\mathcal{M}_{\textup{grid}}}
\def\scan{\mathcal{M}_{\rightarrow}}

\def\Mix{\textup{Mix}}

% The probabilities of mismatch at the vertices v1,...,v4 in the 2x2-block and alpha:
\def\pone{0.283}
\def\ptwo{0.079}
\def\pthree{0.051}
\def\pfour{0.079}
\def\alphasum{0.984}

% The lower bounds on the probabilities of mismatch at the vertices v1,...,v4 in the 2x2-block.
% The name is p - vertex number - and then small for 2x2-block.
\def\ponesmall{0.379}
\def\ptwosmall{0.107}
\def\pthreesmall{0.050}
\def\pfoursmall{0.107}
\def\alphasumsmall{1.286}

% The lower bounds on the probabilities of mismatch at the vertices v1,...,v6 in the 2x3-block when z1 is adjacent to a corner.
% The name is p - vertex number - and then medium for 2x3-block.
\def\ponemedium{0.3671}
\def\pthreemedium{0.0298}
\def\pfourmedium{0.0997}
\def\psixmedium{0.0174}
\def\alphasummedium{1.028}

% The lower bounds on the probabilities of mismatch at the vertices v1,...,v9 in the 3x3-block and alpha.
% The name is p - vertex number - corner or middle depending on where z1 is - and then big for 3x3-block.
\def\ponecornerbig{0.3537}
\def\pthreecornerbig{0.0245}
\def\psevencornerbig{0.0245}
\def\pninecornerbig{0.0071}
\def\ponemiddlebig{0.0838}
\def\pthreemiddlebig{0.0838}
\def\psevenmiddlebig{0.0138}
\def\pninemiddlebig{0.0138}
\def\alphasumbig{1.0148}

\def\scanURL{\texttt{http://www.csc.liv.ac.uk/\nolinebreak[3]$\sim$markus/\nolinebreak[3]systematicscan/}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\begin{document}
%% print out the publisher copyright heading
\copyrightheading

%% use symbolic footnote
%\symbolfootnote

%% use normal text like skip (13pt)
%\textlineskip

\begin{center}

%% print out titles in IJFCS format
\fcstitle{A Systematic Scan for $7$-colourings of the Grid}

\vspace{24pt}

{\authorfont Markus Jalsenius}

\vspace{2pt}

%% use smaller line skip here
\smalllineskip
{\addressfont Department of Computer Science, University of Liverpool\\
Ashton Street, Liverpool, L69 3BX, United Kingdom}

\vspace{10pt}

and

\vspace{10pt}

{\authorfont Kasper Pedersen}

\vspace{2pt}
\smalllineskip
{\addressfont Department of Computer Science, University of Liverpool\\
Ashton Street, Liverpool, L69 3BX, United Kingdom}

\vspace{20pt}
%% authors need not care about this
%\publisher{(received date)}{(revised date)}{Editor's name}

\end{center}

%\alphfootnote





--- START OF DOCUMENT TAIL ---
ll, and A.~Sinclair.
\newblock Markov chain algorithms for planar lattice structures.
\newblock {\em SIAM Journal on Computing}, 31(1):167--192, 2001.

\bibitem{dobrushin_paper}
K.~Pedersen.
\newblock Dobrushin conditions for systematic scan with block dynamics.
\newblock In {\em Mathematical Foundations of Computer Science 2007}, volume
  4708 of {\em Lecture Notes in Computer Science}, pages 264--275. Springer,
  2007.

\bibitem{thesis}
K.~Pedersen.
\newblock {\em On Systematic Scan}.
\newblock PhD thesis, University of Liverpool, 2008.

\bibitem{salas-sokal}
J.~Salas and A.~D. Sokal.
\newblock Absence of phase transition for antiferromagnetic {P}otts models via
  the {D}obrushin uniqueness theorem.
\newblock {\em Journal of Statistical Physics}, 86(3--4):551, 1997.

\bibitem{dror_combinatorial}
D.~Weitz.
\newblock Combinatorial criteria for uniqueness of {G}ibbs measures.
\newblock {\em Random Structures and Algorithms}, 27(4):445--475, 2005.

\end{thebibliography}


\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1157
```latex
--- START OF DOCUMENT HEAD ---
]
\newtheorem{fact}{Fact}[section]
\newtheorem{lemma}{Lemma}[section]
\newtheorem{remark}{Remark}[section]
\newtheorem{remarks}[remark]{Remarks}
\def\mod{\,\hbox{mod}\,}
\def\un{\underline}
\def\bx{\begin{example}}
\def\ex{\end{example}}
\def\bxs{\begin{examps}. \rm\begin{enumerate}}
\def\exs{\end{enumerate}\end{examps}}
\def\bd{\begin{definition}}
\def\ed{\end{definition}}
%\def\bt{\begin{theorem}}
%\def\et{\end{theorem}}
\def\bp{\begin{proposition}\rm}
\def\ep{\end{proposition}}
\def\bc{\begin{corollary}}
\def\ec{\end{corollary}}
\def\bl{\begin{lemma}\em}
\def\el{\end{lemma}}
\def\be{\begin{equation}}
\def\ee{\end{equation}}
\def\br{\begin{remark}\rm\small}
\def\er{\end{remark}}
\def\brs{\begin{remarks}.\\ \rm\
\begin{enumerate}}
\def\ers{\end{enumerate}\end{remarks}}
\def\bea{\begin{eqnarray}}
\def\eea{\end{eqnarray}}
\def\bfig{\begin{figure}[!ht]}
\def\efig{\end{figure}}
%%%%%%%%%%%%%%%%%  Definitions: abbreviated special symbols %%%%%%%
\def\sd{\ltimes}
\def\m{\mathop}
\def \pa{\partial}
\def\ra{{\rightarrow}}
\def\wt{\widetilde}
\def\Tr{\mathrm {Tr}}
\def\tr{\mathrm {tr}}
\def\det{\mathrm {det}}
\def\sgn{\mathrm {sgn}}
\def\ln{\mathrm {ln}}
\def\Diag{\mathrm {Diag}}
\def\diag{\mathrm {diag}}
\def\res{\mathop{\mathrm {res}}\limits_}
\def\ri{\right}
\def\ds{\displaystyle}
\def\un{\underline}
\def\&{&{\hskip -20pt}}

%%%%%%%%%%%%%%%%%% Definitions: lettering %%%%%%%%%%%%

\def\AA{{\mathcal A}}
\def\BB{{\mathcal B}}
\def\CC{{\mathcal C}}
\def\DD {{\mathcal D}}
\def\HH{{\mathcal H}}
\def\KK{{\mathcal K}}
\def\OO{{\mathcal O}}
\def\PP{{\mathcal P}}
\def\SS{{\mathcal S}}
\def\VV{{\mathcal V}}

\def\Ab{{\mathbf A}}
\def\Bb{{\mathbf B}}
\def\Cb{{\mathbf C}}
\def\Ib{{\mathbf I}}
\def\eb{{\mathbf e}}
\def\kb{{\mathbf k}}
\def\Nb{{\mathbf N}}
\def\Pb{{\mathbf P}}
\def\Rb{{\mathbf R}}
\def\Ub{{\mathbf U}}
\def\Wb{{\mathbf W}}
\def\Zb{{\mathbf Z}}
\def\wb{{\mathbf w}}
\def\WbT{{\widetildet{\mathbf W}}}
\def\Hb{{\mathbf H}}
\def\HbC{\check{\mathbf H}}
\def\HbT{\hat{\mathbf H}}

\def\Abb{{\mathbb A}}
\def\Cbb{{\mathbb C}}
\def\Nbb{{\mathbb N}}
\def\Rbb{{\mathbb R}}
\def\Zbb{{\mathbb Z}}

\def\time{{\textsc t}}
\def\Tt{{\textsf T}}
\def\bt{{\bf t}}
\def\n{|\nu \rangle}
\def\nn{|\nu,n \rangle}
\def\llambda{\langle\lambda |}
\def\lll{\langle \lambda,l |}
\def\lr{|\lambda \rangle}
\def\lrl{|\lambda,l \rangle}
\def\ml{\langle\mu |}
\def\mlm{\langle\mu,m |}
\def\mr{|\mu \rangle}
\def\mrm{|\mu,m \rangle}


\newcount\YDcount\YDcount=0
\def\YDsize{10pt}

\def\YD#1{%
\ifnum#1=0
 \ifnum\YDcount=0 \ifx\varnothing\undefined\emptyset\else\varnothing\fi
 \else\vskip1.4pt\egroup\YDcount=0\fi
\else
 \ifnum\YDcount=0 \YDcount=1\vcenter\bgroup\vskip1pt
 \else\nointerlineskip\fi
 \vbox{\hrule\hbox{\vrule height\YDsize
 \loop\hskip\YDsize\vrule\ifnum\YDcount<#1\advance\YDcount1\repeat}\hrule
 \kern-0.4pt}\expandafter\YD
\fi}

\begin{document}


\begin{center}
\begin{Large}\fontfamily{cmss}
\fontsize{17pt}{27pt} \selectfont \textbf{Fermionic construction
of tau functions and random processes} \footnote{Work of (J.H.)
supported in part by the Natural Sciences and Engineering Research
Council of Canada (NSERC) and the Fonds FCAR du Qu\'ebec; that of
(A.O.) by the Russian Academy of Science program  ``Fundamental
Methods in Nonlinear Dynamics" and  RFBR grant No 05-01-00498.}
\end{Large}\\
\bigskip
\begin{large} {J. Harnad}$^{\dagger \ddagger}$\footnote{harnad@crm.umontreal.ca}
and {A. Yu. Orlov}$^{\star}$\footnote{orlovs@wave.sio.rssi.ru}
\end{large}
\\
\bigskip
\begin{small}
$^{\dagger}$ {\em Centre de recherches math\'ematiques,
Universit\'e de Montr\'eal\\ C.~P.~6128, succ. centre ville,
Montr\'eal,
Qu\'ebec, Canada H3C 3J7} \\
\smallskip
$^{\ddagger}$ {\em Department of Mathematics and Statistics,
Concordia University\\ 7141 Sherbrooke W., Montr\'eal, Qu\'ebec,
Canada H4B 1R6} \\
\smallskip
$^{\star}$ {\em Nonlinear Wave Processes Laboratory, \\
Oceanology Institute, 36 Nakhimovskii Prospect\\
Moscow 117997, Russia } \\
\end{small}
\end{center}
\bigskip




--- START OF DOCUMENT TAIL ---
erarchy, {\em Adv. Stud. Pure Math.} {\bf 4}
 (1984) 139-163

\bibitem{Tak1} Takebe, T.: Representation Theoretical Meaning
of Initial Value Problem for the Toda Lattice Hierarchy I, {\em
Lett. Math. Phys.} {\bf 21} (1991), 77-84.

\bibitem{Tak2} Takebe, T.: Representation Theoretical Meaning
of Initial Value Problem for the Toda Lattice Hierarchy II, {\em
Publ. RIMS, Kyoto Univ.} {\bf 27} (1991), 491-503.

%\bibitem{TT-disp}   Takasaki,K. and Takebe, T., "Quasi-classical limit of
%Toda hierarchy and $W$-infinity symmetries", {\it Letters in Math.
%Phys.} {\bf 28} (1993) 165-176

\bibitem{TW} C. A. Tracy, H. Widom,
``Nonintersecting Brownian Excursions'', math.PR/0607321

\bibitem{UT} K. Ueno and K. Takasaki, {\it Adv. Stud. Pure
Math.}{\bf 4}, 1-95, (1984).

\bibitem{Zchains} A.Zabrodin, ``A survey of Hirota's difference equations'', solv-int/9704001

\bibitem{ZSh} V.E. Zakharov and A.B. Shabat, {\it J. Funct.
 Anal. Appl.} {\bf 8} 226, (1974)



\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0669
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: bcpreview.tex|>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% BCP style %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\documentclass{bcp}

\usepackage{tocbibind}


\def\LaTeX{L\kern -.36em\raise .3ex\hbox{\sc a}\kern -.15em T\kern -.1667em%
\lower .7ex\hbox{E}\kern -.125em X}

\font\tt=cmtt10
\setlength{\textwidth}{13.5cm}

\def\refname{References}
\def\thebibliography#1{\vskip24pt plus4pt minus4pt
\small
\centerline{\bf \refname}
\vglue11pt plus2pt minus2pt
\nobreak\list
 {[\arabic{enumi}]}{\settowidth\labelwidth{[#1]}\leftmargin\labelwidth
 \parsep-3pt plus1pt \itemindent0pt
 \itemsep 4pt plus 2pt minus 1pt
 \advance\leftmargin\labelsep
 \usecounter{enumi}}
 \def\newblock{\hskip .11em plus .33em minus .07em}
 \sloppy\clubpenalty4000\widowpenalty4000
 \sfcode`\.=1000\relax}
\let\endthebibliography=\endlist


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\usepackage[centertags]{amsmath}
\usepackage{amsmath}

\usepackage[dutch,british]{babel}
\usepackage{amsfonts}
\usepackage{amssymb}
%\usepackage{amsthm}
\usepackage{newlfont}
%\usepackage{color}
% \usepackage{bbm}



% THEOREM-LIKE ENVIRONMENTS -----------------------------------------

%\theoremstyle{plain}
  \newtheorem{theorem}{Theorem}[section]
  \newtheorem{corollary}[theorem]{Corollary}
  \newtheorem{proposition}[theorem]{Proposition}
  \newtheorem{lemma}[theorem]{Lemma}
  \newtheorem{remark}[theorem]{Remark}
  \newtheorem{assumption}[theorem]{Assumption}
%\theoremstyle{definition}
  \newtheorem{definition}{Definition}[section]


%\theoremstyle{remark}

  \newtheorem{note}[theorem]{Note}
  \newtheorem{notes}[theorem]{Notes}
  \newtheorem{example}[theorem]{Example}

\numberwithin{equation}{section}



\newtheorem{vetremark}[theorem]{\bf{Remark}}

% \MATHOPERATOR -----------------------------------------------------
\DeclareMathOperator{\Tr}{Tr}
\DeclareMathOperator{\Prob}{\boldsymbol{Prob} }
\DeclareMathOperator{\ex}{Ex} \DeclareMathOperator{\ext}{Ext}
\DeclareMathOperator{\Int}{Int} \DeclareMathOperator{\supp}{Supp}
\newcommand{\re}{\mathrm{Re}\,}
\newcommand{\im}{\mathrm{Im}\,}

\newcommand{\HH}{\mathsf{H}}
\newcommand{\PP}{\mathsf{P}}

\newcommand\otimesal{\mathop{\hbox{\raise 1.6 ex
  \hbox{$\scriptscriptstyle\mathrm{al}$}
\kern -0.92 em \hbox{$\otimes$}}}}
\newcommand\oplusal{\mathop{\hbox{\raise 1.6 ex
  \hbox{$\scriptscriptstyle\mathrm{al}$}
\kern -0.92 em \hbox{$\oplus$}}}}
\newcommand\Gammal{\hbox{\raise 1.7 ex
\hbox{$\scriptscriptstyle\mathrm{al}$}\kern -0.50 em $\Gamma$}}
\renewcommand\i{\mathrm{i}}

% GREEK - 2 letters ------------------------------------------------

\let\al=\alpha \let\be=\beta \let\de=\delta \let\ep=\epsilon
\newcommand{\RR}{\mathsf{R}}
\let\ve=\varepsilon \let\vp=\varphi \let\ga=\gamma \let\io=\iota
\let\ka=\kappa \let\la=\lambda \let\om=\omega \let\vr=\varrho
\let\si=\sigma \let\vs=\varsigma \let\th=\theta \let\vt=\vartheta
\let\ze=\zeta \let\up=\upsilon

\let\De=\Delta \let\Ga=\Gamma \let\La=\Lambda \let\Om=\Omega
\let\Th=\Theta  \let\Si=\Sigma
\newcommand\loplus{\mathop{\oplus}\limits}
% \MATHCAL - \ca ----------------------------------------------------

\newcommand{\caA}{{\mathcal A}}
\newcommand{\cB}{{\mathcal B}}
\newcommand{\caC}{{\mathcal C}}
\newcommand{\cD}{{\mathcal D}}
\newcommand{\cE}{{\mathcal E}}
\newcommand{\cF}{{\mathcal F}}
\newcommand{\caG}{{\mathcal G}}
\newcommand{\cH}{{\mathcal H}}
\newcommand{\caI}{{\mathcal I}}
\newcommand{\caJ}{{\mathcal J}}
\newcommand{\cK}{{\mathcal K}}
\newcommand{\caL}{{\mathcal L}}
\newcommand{\caM}{{\mathcal M}}
\newcommand{\cN}{{\mathcal N}}
\newcommand{\caO}{{\mathcal O}}
\newcommand{\cP}{{\mathcal P}}
\newcommand{\cQ}{{\mathcal Q}}
\newcommand{\cR}{{\mathcal R}}
\newcommand{\caS}{{\mathcal S}}
\newcommand{\caT}{{\mathcal T}}
\newcommand{\caU}{{\mathcal U}}
\newcommand{\caV}{{\mathcal V}}
\newcommand{\caW}{{\mathcal W}}
\newcommand{\caX}{{\mathcal X}}
\newcommand{\caY}{{\mathcal Y}}
\newcommand{\cZ}{{\mathcal Z}}
\renewcommand\c{{\mathrm c}}
\newcommand\cl{{\math

--- START OF DOCUMENT TAIL ---
ay*}
\d\Gamma(H_\res)&=&\int x(\xi)a_\xi^*a_\xi\d \xi,\\ a^*(V)&=&\int v(\xi)
a_\xi^*\d
\xi,\\ a(V)&=&\int v^*(k) a_\xi\d \xi,\\
H&=&K+\int x(\xi)a_\xi^*a_\xi\d \xi+
\lambda\int\left( v(\xi) a_\xi^*
+v^*(\xi) a_\xi\right)\d \xi.
\end{eqnarray*}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


The cocycle
$W_t:=\e^{\i t\d\Gamma( Z_\res)} \e^{-\i t Z}$ solves
\begin{eqnarray*}
&&\i\frac{\d}{\d t}W_t\\\!\!\!\!\!&=&
\left(\frac12(\Upsilon+\Upsilon^*) +a^*\left(\nu\otimes|\e^{-\i
tZ_\res}1)\right) +a\left(\nu\otimes|\e^{-\i
tZ_\res}1)\right)\right) W_t,\end{eqnarray*}

 Apply the Fourier transformation on $L^2(\rr)$, so that $|1)$
will  correspond to
$(2\pi)^{-\frac12}|\delta_0)$. Writing $\tilde W_t$  for
 $W_t$ after this transformation,
we obtain the quantum Langevin equation in a more familiar form:
\begin{eqnarray*}
&&\i\frac{\d}{\d t}\tilde W_t\\&=&
\left(\frac12(\Upsilon+\Upsilon^*)+a^*\left(\nu\otimes|\delta_t)\right)+a\left(\nu\otimes|\delta_t)\right)
\right) \tilde W_t.\end{eqnarray*}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1174
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: PolyOnConics.tex|>
\documentclass[11pt]{article}
\usepackage{graphicx}
\usepackage{amssymb}
\usepackage{epstopdf}
\DeclareGraphicsRule{.tif}{png}{.png}{`convert #1 `dirname #1`/`basename #1 .tif`.png}

\textwidth = 6.5 in
\textheight = 9 in
\oddsidemargin = 0.0 in
\evensidemargin = 0.0 in
\topmargin = 0.0 in
\headheight = 0.0 in
\headsep = 0.0 in
\parskip = 0.2in
\parindent = 0.0in

\newtheorem{theorem}{Theorem}
\newtheorem{cor}[theorem]{Corollary}
\newtheorem{lem}{Lemma}
\newtheorem{definition}{Definition}

\title{Deconstructing  Functions on Quadratic Surfaces into Multipoles}
\author{Gabriel Katz}


\begin{document}
%
%\address{Department of Mathematics, Brandeis University, Waltham, MA 02454}
%
%\email{gabrielkatz@rcn.com}
%\date{\today}

\maketitle



--- START OF DOCUMENT TAIL ---
Press, Oxford, reprinted by Dover, 1954.

[N] Narasimhan, R., {\it Introduction to the Theory of Analytic Spaces}, Lecture Notes in Mathematics 25 (1966), Springer-Verlag.

[Sh] Shubin, M. A., {\it Pseudo-differential Operators and Spectral Theory}, Nauka, Moscow, 1978.

[S] Sylvester, J.J.,  {\it Note on Spherical Harmonics}, Philosophical  Magazine, v. 2m, 1876, 291-307 \& 400.
  
[S1] Sylvester, J.J., 400. {\it Collected Mathematical Papers}, v.3, 37-51, Cambridge University Press, Cambridge, 1909.

[TOH]  Tegmark, M., de Oliveira-Costa and Hamilton A.J.S., {\it A high resolution foreground cleaned CMB map from WMAP}, Phys. Rev. D. 68 (2003) 123523, (arXiv:astro-ph/0302496).

[W] Weeks, J., {\it Maxwell's Multipole Vectors and the CMB}, preprint (arXiv:astro-ph/ 0412231).

\bigskip



%Department of Mathematics \newline 
William Paterson University,\newline Wayne, NJ 07470-2103, U.S.A.\hfill\break
e-mail: {\it katzg@wpunj.edu}\quad\& \quad {\it ygkatz@yahoo.com}

 \end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0286
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: KuchKun.tex|>
\documentclass[12pt]{article}
%\documentclass[referee]{ejm}
\usepackage{amsmath,amssymb,latexsym,graphicx}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{conjecture}[theorem]{Conjecture}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\NN}{\mathbb{N}}
\newcommand{\ZZ}{\mathbb{Z}}
\newcommand{\CC}{\mathbb{C}}
\newcommand{\TT}{\mathbb{T}}
\newcommand{\E}{\mathcal{E}}
\newcommand{\G}{\Gamma}
\newcommand{\g}{\gamma}
\newcommand{\U}{\mathcal{U}_\G}
\newcommand{\V}{\mathcal{V}_\G}
\newcommand{\fh}{\hat{f}}
\newcommand{\ma}{\mathbf{a}}
\newcommand{\mb}{\mathbf{b}}
\newcommand{\mk}{\mathbf{k}}
\newcommand{\B}{\mathcal{B}}
\newcommand{\D}{\mathcal{D}}
\newcommand{\mS}{\mathcal{S}}
\newcommand{\dn}{d\,'}
%\newcommand{\if}{if and only if }
\newcommand{\PW}{Paley-Wiener }
\newcommand{\Pl}{Plancherel}
\newcommand{\So}{Sobolev }
%\usepackage{showkeys}
\begin{document}
\author{Peter Kuchment\footnote{Mathematics Department,
Texas A\& M University, College Station, TX 77843-3368, USA.
kuchment@math.tamu.edu} and Leonid Kunyansky\footnote{Mathematics Department,
University of Arizona, Tucson, AZ 77843-3368, USA.
leonk@math.arizona.edu}}
\title{Mathematics of thermoacoustic tomography}
%\date{}
\maketitle
%\tableofcontents


--- START OF DOCUMENT TAIL ---
graphy.
Phys. Rev. E {\bf 71}, 016706.

\bibitem{MXW_review} Xu, M. \& Wang, L.-H.~V. 2006
Photoacoustic imaging in biomedicine.
Review of Scientific Instruments {\bf 77}, 041101-01 -- 041101-22.

\bibitem{XFW} Xu, Y., Feng, D. \& Wang, L.-H.~V. 2002
Exact frequency-domain reconstruction for thermoacoustic tomography:
I. Planar geometry.
IEEE Trans. Med. Imag. {\bf 21}, 823--828.

\bibitem{XXW} Xu, Y., Xu, M. \& ~Wang, L.-H.~V. 2002
Exact frequency-domain reconstruction for thermoacoustic tomography:
II. Cylindrical geometry.
IEEE Trans. Med. Imag. {\bf 21}, 829--833.

\bibitem{XWAK} Xu, Y., Wang, L., Ambartsoumian, G. \& Kuchment, P. 2004
Reconstructions in limited view thermoacoustic tomography.
Medical Physics, \textbf{31}(4), 724--733.

\bibitem{Zob} Zobin, N. 1993. Unpublished.

\end{thebibliography}


\end{document}

\bibitem{etti} Bouzaglo-Burov, E. 2005
Inversion of spherical Radon transform, methods and numerical
experiments.
MS Thesis, Bar-Ilan University, 1--30. (In Hebrew)
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0991
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: switch.tex|>
\documentclass[11pt]{article}

\usepackage{latexsym,amssymb,amsmath,natbib,graphicx, amsthm, times}%,bbm}
\usepackage[margin=1in,left=1in]{geometry}
\usepackage{times}
%\usepackage{srcltx}
\usepackage{natbib}
\renewcommand{\cite}{\citeyearpar}

\linespread{1.2}
\newcommand {\ME}{\mathbb{E}^{x}}
\newcommand {\MEt}{\mathbb{E}^{x}_{t}}
\newcommand {\uEt}{\tilde{\mathbbm{E}}}
\newcommand {\ud}{\, \textup{d}}
\newcommand {\bracks}[1]{\left[#1\right]}
\newcommand {\parens}[1]{\left(#1\right)}
\newcommand {\braces}[1]{\left\{#1\right\}}
\newcommand {\I}[1]{\mathbbm{1}_{\{#1\}}}
\newcommand {\myBox}{\hspace{\stretch{1}}$\diamondsuit$}
\renewcommand{\S}{\mathcal{S}}
\renewcommand{\theequation}{\thesection. \arabic{equation}}
\numberwithin{equation}{section}
\newtheorem{proposition}{Proposition}[section]
\newtheorem{coro}{Corollary}[section]
\newtheorem{remark}{Remark}[section]
\newtheorem{lemma}{Lemma}[section]
\newtheorem{example}{Example}[section]
\newtheorem{assump}{Assumption}[section]

\newcommand {\R}{\mathbb{R}}
\newcommand {\C}{\mathbf{C}}
\newcommand {\D}{e^{-\alpha\tau}}
\newcommand {\F}{\mathcal{F}}
\newcommand {\A}{\mathcal{A}}
\newcommand {\M}{\mathcal{M}}
\newcommand {\p}{\mathbb{P}}
\newcommand {\G}{\mathcal{G}}
\newcommand {\E}{\mathbb{E}}
\newcommand {\LL}{\mathcal{L}}
\newcommand{\work}{\marginpar{\textbf{Need some Work}}}
\title{A Direct Method for Solving Optimal Switching Problems of One-Dimensional Diffusions}
\author{
Masahiko Egami}
\date{}

\begin{document}

\maketitle


--- START OF DOCUMENT TAIL ---
w c}\frac{h^+(x)}{\varphi(x)}\quad
\text{and}\quad l_d\triangleq \limsup_{x\uparrow
d}\frac{h^+(x)}{\psi(x)}
\end{equation}
are both finite.
\end{proposition}
In the finite case, furthermore,
\begin{proposition}\normalfont \label{prop:A6}
The value function $V(\cdot)$ is continuous on $(c, d)$.  If $h: (c,
d)\rightarrow \R$ is continuous and $l_c=l_d=0$, then $\tau^*$ of
(\ref{eq:opt}) is an optimal stopping time.
\end{proposition}
\begin{proposition}\normalfont\label{prop:A7}
Suppose that $l_c$ and $l_d$ are finite and one of them is strictly
positive, and $h(\cdot)$ is continuous.  Define the continuation
region $C\triangleq (c, d)\setminus\Gamma$.  Then $\tau^*$ of
(\ref{eq:opt}) is an optimal stopping time, if and only if
\begin{align*}
&\text{there is no $r\in (c, d)$ such that $(c, r)\subset C$ if
$l_c>0$}\quad \text{and}\\
&\text{there is no $l\in (c, d)$ such that $(l, d)\subset C$ if
$l_d>0$}.
\end{align*}
\end{proposition}

\end{appendix}
\bibliography{switch}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0495
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: sigma07-075.tex|>
\RequirePackage{ifpdf}
\ifpdf % We are running pdfTeX in pdf mode
\documentclass[pdftex]{sigma}
\else
\documentclass{sigma}
\fi

%\numberwithin{equation}{section}

\renewcommand{\textfraction}{0.0}
\renewcommand{\topfraction}{1} 

\begin{document}

\renewcommand{\PaperNumber}{075}

\FirstPageHeading

\ShortArticleName{The Veldkamp Space of Two-Qubits}

\ArticleName{The Veldkamp Space of Two-Qubits}


\Author{Metod SANIGA~$^\dag$, Michel PLANAT~$^\ddag$, Petr PRACNA~$^\S$ and Hans HAVLICEK~$^\P$}

\AuthorNameForHeading{M. Saniga, M. Planat, P. Pracna and H. Havlicek}



\Address{$^\dag$~Astronomical Institute, Slovak Academy of Sciences,\\
$\phantom{^\dag}$~SK-05960 Tatransk\' a Lomnica, Slovak Republic}
\EmailD{\href{mailto:msaniga@astro.sk}{msaniga@astro.sk}}
\URLaddressD{\url{http://www.ta3.sk/~msaniga/}}


\Address{$^\ddag$~Institut FEMTO-ST, CNRS, D\' epartement LPMO,
32 Avenue de
l'Observatoire,\\ 
$\phantom{^\dag}$~F-25044 Besan\c con Cedex, France}
\EmailD{\href{mailto:michel.planat@femto-st.fr}{michel.planat@femto-st.fr}}


\Address{$^\S$~J. Heyrovsk\' y Institute of Physical
Chemistry, Academy of Sciences of the Czech Republic,\\ 
$\phantom{^\S}$~Dolej\v skova 3, CZ-182 23 Prague 8, Czech
Republic}
\EmailD{\href{mailto:pracna@jh-inst.cas.cz}{pracna@jh-inst.cas.cz}}

\Address{$^\P$~Institut f\" ur Diskrete Mathematik und Geometrie,
Technische Universit\" at Wien,\\
$\phantom{^\P}$~Wiedner Hauptstra\ss e 8--10, A-1040 Vienna, Austria}
\EmailD{\href{mailto:havlicek@geometrie.tuwien.ac.at}{havlicek@geometrie.tuwien.ac.at}}


\ArticleDates{Received April 13, 2007, in f\/inal form June 18, 2007; Published online June 29, 2007}



\Abstract{Given a remarkable representation of the generalized
Pauli operators of two-qubits in terms of the points of the
generalized quadrangle of order two, $W(2)$, it is shown that
specif\/ic subsets of these operators can also be associated with
the points and lines of the four-dimensional projective space over
the Galois f\/ield with two elements -- the so-called Veldkamp
space of $W(2)$. An intriguing novelty is the recognition of (uni- and tri-centric) triads
and specif\/ic pentads of the Pauli operators in addition to the ``classical" subsets
answering to geometric hyperplanes of $W(2)$.}

\Keywords{generalized quadrangles; Veldkamp spaces; Pauli operators of two-qubits}


\Classification{51Exx; 81R99}

\vspace{-4mm}
\section{Introduction}
A deeper understanding of the structure of Hilbert spaces of
f\/inite dimensions is of utmost importance for quantum information
theory. Recently, we made an important step in this respect by
demonstrating that the commutation algebra of the generalized Pauli operators
on the $2^N$-dimensional Hilbert spaces is embodied in the
geometry of the symplectic polar space of rank $N$ and order two
\cite{saplpr,sapl,plsa}. The case of two-qubit operator space,
$N=2$, was scrutinized in very detail \cite{saplpr,plsa} by explicitly demonstrating,
in dif\/ferent ways, the correspondence between various subsets of
the generalized Pauli operators/matrices and the fundamental
subgeometries of the associated rank-two polar space -- the
(unique) generalized quadrangle of order two. In
this paper we will reveal another interesting geometry hidden
behind the Pauli operators of two-qubits, namely that of the
Veldkamp space def\/ined on this generalized quadrangle.

\section{Finite generalized quadrangles and Veldkamp spaces}

{\samepage In this section we will brief\/ly highlight the basics of the theory of f\/inite generalized
quadrangles~\cite{paythas} and introduce the concept of the Veldkamp space of a point-line incidence geometry~\cite{buek}
to be employed in what follows.}

A {\it finite generalized quadrangle} of order $(s, t)$, usually
denoted GQ($s, t$), is an incidence structure $S = (P, B, {\rm
I})$, where $P$ and $B$ are disjoint (non-empty) sets of objects,
called respectively points and lines, and where I is a symmetric
point-line

--- START OF DOCUMENT TAIL ---
 
{\it J. Opt. B: Quantum Semiclass. Opt.} {\bf 6} (2004), L19--L20, 
\href{http://arxiv.org/abs/math-ph/0403057}{math-ph/0403057}.

\bibitem{thmp}
Saniga M., Planat M., Minarovjech M., Projective line over the f\/inite quotient ring $GF(2)[x]/(x^3 - x)$ and
quantum entanglement: the Mermin ``magic'' square/pentagram, {\it Theor. Math. Phys.} {\bf 151} (2007), 625--631,
\href{http://arxiv.org/abs/quant-ph/0603206}{quant-ph/0603206}.


\bibitem{spie}
Planat M., Saniga M., Pauli graph and f\/inite 
projective lines/geometries, {\it Optics and Optoelectronics}, to appear,
\href{http://arxiv.org/abs/quant-ph/0703154}{quant-ph/0703154}.

\bibitem{koen}
Thas K., Pauli operators of {\it N}-qubit Hilbert spaces and the Saniga--Planat conjecture, {\it Chaos Solitons
Fractals}, to appear.


\bibitem{koen2}
Thas K., The geometry of generalized Pauli operators of $N$-qudit Hilbert space, 
{\it Quantum Information and Computation}, submitted.\LastPageEnding


\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2242
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: glt1.tex|>
\documentclass[11pt,reqno]{amsart}
\usepackage{amssymb,amsthm,amsfonts,amstext}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage[american]{babel}
\usepackage[ansinew]{inputenc}
%\usepackage[notcite,notref]{showkeys}
\makeatletter \@addtoreset{equation}{section} \makeatother
\renewcommand\theequation{\thesection.\arabic{equation}}
\renewcommand\thetable{\thesection.\@arabic\c@table}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}[section]
\newtheorem*{note}{Note added in proof}


\usepackage{a4wide}

\newcommand{\<}{\langle}
\renewcommand{\>}{\rangle}

\newcommand{\med}[1]{\langle #1 \rangle}
\DeclareMathOperator{\supp}{supp} \DeclareMathOperator{\diam}{diam}


\title[H. L. for a Particle System with degenerate rates]{Hydrodynamic
  Limit for a Particle System \\ with degenerate rates}

\date{\today}

\author{Gon�alves, P.}

\address{IMPA, Estrada Dona Castorina 110, CEP 22460 Rio de Janeiro, Brasil}
\email{patg@impa.br}

\author{Landim, C.}


\address{IMPA, Estrada Dona Castorina 110,
CEP 22460-320 Rio de Janeiro, Brasil\\
CNRS UMR 6085, Universit\'e de Rouen, UMR 6085, Avenue de
l'Universit\'e, BP.12, Technop\^ole du Madrillet, F76801
Saint-\'Etienne-du-Rouvray, France}
\email{landim@impa.br}

\author{Toninelli, C.}

\address{ Laboratoire de Probabilit{\'e}s et Mod{\`e}les
  Al{\`e}atoires CNRS-UMR 7599, Univ.Paris VI-VII, 4 Pl.Jussieu,
Paris, FRANCE} \email{ctoninel@ccr.jussieu.fr}




\begin{document}



--- START OF DOCUMENT TAIL ---
em[7]{Q}
Quastel, J. (1992): \textit{Diffusion of Color in the Simple Exclusion Process}. Communications on Pure and Apllied Mathematics \textbf{XLV},
623-679.
\bibitem[8]{HS.}
Spohn, H. (1991): \textit{Large scale Dynamics of Interacting Particles}. Springer-Verlag.
\bibitem[9]{R.S.} Ritort, F.; Sollich, P.(2003): \textit{Glassy dynamics of kinetically constrained models}, Adv.in Phys {\bf 52} 219-342.
\bibitem[10] {Bi.T.}
Toninelli,C.; Biroli, G.: \textit{Jamming Percolation and Glassy Dynamics} to appear in J.Stat.Phys. - published online, ISSN 1572-9613
\bibitem[11]{V.}
Vazquez, J.L. (1992): \textit{An introduction to the mathematical theory of the porous medium equation}, in: Delfour, M.C. and Sabidussi, G.
editors, Shape Optimization and Free Boundaries, Kluwer, Dordrecht 261-286.
\bibitem[12]{Y.}
Yau, Horng-Tzer (1991): \textit{Relative Entropy and Hydrodyamics of Ginzburg-Landau Models}, Letters in Mathematical Physics, \textbf{22},
63-80.
\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2376
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: Taise.tex|>
% ------------------------------------------------------------------------
% ************ Taise Santiago C. Oliveira, December 2005 ************
% ------------------------------------------------------------------------
% "catalan Traffic" at the beach
% ------------------------------------------------------------------------


\documentclass[12pt]{article}
\usepackage{geometry}
\geometry{letterpaper}
\usepackage{graphicx}
\usepackage[dvips,arrow,matrix,ps,color,line]{xy}
\usepackage{theorem,amsfonts,amssymb,amscd,graphics,shapepar,bm}
\usepackage{epstopdf}
\usepackage{hyperref}
%\usepackage[pagebackref=true]{hyperref}
%\usepackage[notref,notcite]{showkeys}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\geometry{letterpaper}


\hypersetup{ pdftitle={Catalan},
      pdfauthor={Taise Santiago},
      pdfsubject={Integral on Grassmanninans},
    colorlinks = true,
    linkcolor = blue,
    anchorcolor = red,
    citecolor = blue,
    filecolor = red,
    pagecolor = red,
    urlcolor = blue
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\DeclareGraphicsRule{.tif}{png}{.png}{`convert #1 `dirname #1`/`basename #1 .tif`.png}
\makeindex

\hyphenation{spe-ci-fi-ca-tion}
\hyphenation{to-po-lo-gy}
\hyphenation{in-ver-ti-ble}



\setcounter{secnumdepth}{2}

%--------Defini��es------------------------------------------


\def\NN{\mathbb N}
\def\ZZ{\mathbb Z}
\def\CC{\mathbb C}
\def\PP{\mathbb P}
\def\ep{{\epsilon}}
\def\w{\wedge }
\def\lra{\longrightarrow}
\def\proof{\noindent{\bf Proof.}\,\,}
\def\qed{{\hfill\vrule height4pt width4pt depth0pt}\medskip}

%-------Theorems--------------------------------------------------

\theoremstyle{change} \theorembodyfont{\rmfamily}
\newtheorem{thm}{Theorem}[section]
\newtheorem{defin}{Definition}[section]
\newtheorem{example}{Example}[section]
\newtheorem{prop}{Proposition}[section]
\newtheorem{rmk}{Remark}[section]
\newtheorem{claim}{}[section]


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\title{``Catalan Traffic" and Integrals on the Grassmannian of Lines\thanks{AMS 2000 Math. Subject
Classification: 14M15, 14N15, 05A15, 05A19.}}
\author{Ta\'{i}se Santiago Costa Oliveira \thanks{This work was supported in part by ScuDo - Politecnico di Torino, FAPESB proc. n� 8057/2006 and CNPq proc. n� 350259/2006-2.}}
%{\small Dipartimento di Matematica}\\
%\emph{\small Politecnico di Torino}\\
%\emph{\small C.so Duca degli Abruzzi 24, 10129 - Torino-Italia}\\
%\emph{\small e-mail: taise@calvino.polito.it}}
\date{}                                           % Activate to display a given date or no date



\begin{document}
\maketitle



--- START OF DOCUMENT TAIL ---
/ec/catadd.pdf}{http://www-math.mit.edu/$\sim$rstan/ec/catadd.pdf}.

\bibitem{Stan1} R.~P.~Stanley, {\em Catalan Addendum}, version of 30 October
2005.\\
\href{http://www-math.mit.edu/~rstan/ec/catadd.pdf}{
http://www-math.mit.edu/$\sim$rstan/ec/catadd.pdf}.



%
%\bibitem {Wa} G. N. Watson, \emph{A Treatise on the Theory of  Bessel
%Functions}, Second Edition (Cambridge University Press, 1966).


\end{thebibliography}


\bigskip

\begin{small}

\texttt{Dipartimento di Matematica, Politecnico di Torino\\
\indent  C.so Duca degli Abruzzi 24, 10129 - Torino-Italia \\
\indent E-mail address: \href{mailto: taise@calvino.polito.it}{
taise@calvino.polito.it}\\
\\
\indent Departamento de Ci\^{e}ncias Exatas e da Terra \\
\indent Universidade
Estadual de Feira de Santana \\
\indent Av. Universit�ria, s/n - Km 03 da BR 116 \\
\indent  44031-460,Feira de Santana - BA - Brasil \\ \indent
E-mail address: \href{mailto: taisesantiago@gmail.com}{
taisesantiago@gmail.com}}

\end{small}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1943
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: R-IdealValued_ATA2010_-arxiv.tex|>

\documentclass[10pt,a4paper]{article}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{amsmath,amsthm}
\usepackage{url,paralist}
\usepackage{anysize}
\usepackage{diagrams}


\setcounter{MaxMatrixCols}{10}

%\diagramstyle[centredisplay,PostScript=dvips]
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\newtheorem{remark*}[theorem]{Remark}
\newtheorem{rremark*}[theorem]{Final remark}
\newtheorem{problem}[theorem]{Problem}

\newcommand{\mathLARGE}[1]{{\begingroup\everymath{\scriptstyle}\begin{LARGE}{#1}\end{LARGE}\endgroup}}
\newcommand{\mathLarge}[1]{{\begingroup\everymath{\scriptstyle}\begin{Large}{#1}\end{Large}\endgroup}}
\newcommand{\mathlarge}[1]{{\begingroup\everymath{\scriptstyle}\begin{large}{#1}\end{large}\endgroup}}
\newcommand{\mathnormalsize}[1]{{\begingroup\everymath{\scriptstyle}\begin{normalsize}{#1}\end{normalsize}\endgroup}}
\newcommand{\mathsmall}[1]{{\begingroup\everymath{\scriptstyle}\small{#1}\endgroup}}
\newcommand{\mathfootnotesize}[1]{{\begingroup\everymath{\scriptstyle}\footnotesize{#1}\endgroup}}
\newcommand{\mathscriptsize}[1]{{\begingroup\everymath{\scriptstyle}\scriptsize{#1}\endgroup}}
\newcommand{\mathtiny}[1]{{\begingroup\everymath{\scriptstyle}\tiny{#1}\endgroup}}

\begin{document}

\title{{\huge The ideal-valued index for a dihedral group action,}\\
{\huge and mass partition by two hyperplanes}}
\author{Pavle V. M. Blagojevi\'c\thanks{%
The research leading to these results has received funding from the European Research
Council under the European Union's Seventh Framework Programme (FP7/2007-2013) /
ERC Grant agreement no.~247029-SDModels. Also supported by the grant ON 174008 of the Serbian
Ministry of Science and Environment.} \\
%EndAName
Mathemati\v cki Institut\\
Knez Michailova 35/1\\
11001 Beograd, Serbia\\
\url{pavleb@mi.sanu.ac.rs} \and \setcounter{footnote}{6} G\"unter M. Ziegler%
\thanks{The research leading to these results has received funding from the European Research
Council under the European Union's Seventh Framework Programme (FP7/2007-2013) /
ERC Grant agreement no.~247029-SDModels.} \\
%EndAName
Inst.\ Mathematics, MA 6-2\\
TU Berlin\\
D-10623 Berlin, Germany\\
\url{ziegler@math.tu-berlin.de}}
\date{{\small December 9, 2010}}
\maketitle



--- START OF DOCUMENT TAIL ---
 Methods in Combinatorics and
Geometry, 2nd, corrected printing}, Universitext, Springer-Verlag,
Heidelberg, 2008. }

\bibitem{miln-sta} {\small \textsc{J.~Milnor, J. Stasheff},\emph{\
Characteristic classes}, Annals of Mathematics Studies, No. 76. Princeton
University Press, Princeton, N. J.; University of Tokyo Press, Tokyo, 1974,
vii+331 pp.}

\bibitem{Ramos} {\small \textsc{E. Ramos,} \emph{Equipartitions of mass
distributions by hyperplanes,} Discrete Comput. Geom. 15 (1996), 147-167. }

\bibitem{Zivaljevic-topmeth}  {\small \textsc{R. T. {\v{Z}}ivaljevi{\'{c}}},
\emph{Topological methods}, Chap.~14 in CRC Handbook on Discrete and Computational
Geometry, J.~E. Goodman and J.~O'Rourke, eds., 2nd edition 2004,
CRC Press, Boca Raton FL, pp.~305-329. }

\bibitem{guide2} {\small \textsc{R. \v{Z}ivaljevi\'{c},} \emph{User's guide
to equivariant methods in combinatorics II}, Publ. Inst. Math. Belgrade,
64(78), 1998, 107-132. }
\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2216
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: Max-Solid-Amoeba-5.tex|>
\documentclass[a4paper,12pt]{amsart}

\usepackage{epsfig}
\usepackage{graphicx}

\usepackage[latin1]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{indentfirst}
\usepackage{amssymb}
\usepackage{eufrak}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amsthm}
\usepackage{mathrsfs}
\usepackage[bookmarks]{hyperref}
% I hope rsfs doesn't cause any problems.  If it does and no solution
% can be found, please remove the previous line and replace mathscr by
% mathcal everywhere.
\usepackage{xypic}
% I *must* have xypic as I use it for many commutative diagrams.
%
%
% A few useful things (this shouldn't cause any problems)
%
\newcommand{\Rt}{\mathop{\mathbb{R}_{\rm trop}}\nolimits}
\newcommand{\Qt}{\mathop{\mathbb{Q}_{\rm trop}}\nolimits}
\newcommand{\prof}{\mathop{\rm prof}\nolimits}
\newcommand{\R}{\mathop{\rm Re}\nolimits}
\newcommand{\Proj}{\mathop{\rm Proj}\nolimits}
\newcommand{\Spec}{\mathop{\rm Spec}\nolimits}
\newcommand{\Hom}{\mathop{\rm Hom}\nolimits}
\newcommand{\Ext}{\mathop{\rm Ext}\nolimits}
\newcommand{\gen}{{\mathop{\rm gen}\nolimits}}
\newcommand{\coker}{\mathop{\rm coker}\nolimits}
\newcommand{\Iim}{\mathop{\rm Im}\nolimits}
\newcommand{\Log}{\mathop{\rm Log}\nolimits}
\newcommand{\val}{\mathop{\rm val}\nolimits}
\newcommand{\Val}{\mathop{\rm Val}\nolimits}
\newcommand{\ord}{\mathop{\rm ord}\nolimits}
\newcommand{\Arg}{\mathop{\rm Arg}\nolimits}
\newcommand{\Vol}{\mathop{\rm Vol}\nolimits}
\newcommand{\Ima}{\mathop{\rm Im}\nolimits}
\newcommand{\GL}{\mathop{\rm GL}\nolimits}
\newcommand{\Sup}{\mathop{\rm Sup}\nolimits}
\newcommand{\Inf}{\mathop{\rm Inf}\nolimits}
\newcommand{\Area}{\mathop{\rm Area}\nolimits}
\newcommand{\supp}{\mathop{\rm supp}\nolimits}
\newcommand{\Verte}{\mathop{\rm Vert}\nolimits}
\newcommand{\medwedge}{\mathop{\textstyle\bigwedge}\nolimits}


\input epsf


\def \square{\smallskip \hfill \vrule width 5 pt height 7
pt depth - 2 pt \smallskip }

\newenvironment{prooof}
{\noindent {{\it Proof} \;}}{\hspace*{\fill}\square\vskip 8pt}


\oddsidemargin=16pt \evensidemargin=16pt \topmargin=16pt
\headheight=8pt \textheight=591pt \textwidth=436pt
%
%
\theoremstyle{plain}
\newtheorem{Lem}[subsection]{Lemma}
\newtheorem{The}[subsection]{Theorem}
\newtheorem{Cor}[subsection]{Corollary}
\newtheorem{Pro}[subsection]{Proposition}
%
\theoremstyle{definition}
\newtheorem{Rem}[subsection]{Remark}
\newtheorem{Remi}[subsection]{\it Remarque}
\newtheorem{RemP}[subsection]{Remarques et propri{\'e}t{\'e}s}
\newtheorem{Dem}[subsection]{Proof}
\newtheorem{Def}[subsection]{Definition}
\newtheorem{Exe}[subsection]{Example}
\newtheorem{Exes}[subsection]{Examples}
\newtheorem{Aff}[subsection]{\it Affirmation}
%\renewcommand{\theex}{}

\newcommand{\bdot}{ {\hspace{-.1em} \mbox{\bf .} } }

\begin{document}

\title{Maximally Sparse Polynomials have Solid Amoebas}


\author{Mounir Nisse}
\address{Universit� Pierre et Marie Curie-Paris 6, IMJ (UMR 7586),
Labo: Analyse Alg�brique, Office: 7C14, 175, rue du Chevaleret,\\ 75013
Paris, France}
\email{nisse@math.jussieu.fr}


\maketitle




--- START OF DOCUMENT TAIL ---
7]{N2-07}{\sc M. Nisse}, {\em  Coamoebas of curves in $(\mathbb{C}^*)^2$, Dimer Models on Torus and Planar Quivers}, in preparation.


\bibitem[PR1-04]{PR1-04}{Passare and Rullg\aa rd}{\sc M. Passare and H.
Rullg\aa rd}, {\em Amoebas, Monge-Amp{\`e}re measures, and triangulations
of the Newton polytope}, Duke Math. J. {\bf 121}, (2004), 481-507.

 %Preprint , Stockholm University, 2000.

\bibitem[PR2-01]{PR2-01}{\sc M. Passare and H.
Rullg\aa rd}, {\em Multiple Laurent series and polynomial amoebas},
pp.123-130 in: Actes des rencontres d'analyse complexe, Atlantique,
{\'E}ditions de l'actualit{\'e} scientifique, Poitou-Charentes 2001.

\bibitem[R-01]{R-01}{\sc H. Rullg\aa rd}, {\em Polynomial
amoebas and convexity}, Research Reports In Mathematics Number 8,2001,
Department Of Mathematics Stockholm University.

\bibitem[V-90]{V-90}{\sc O. Viro}, {\em  Patchworking real
 algebraic varieties}, preprint: http://www.math.uu.se/ oleg; Arxiv: AG/0611382

\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2152
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: HAND.tex|>
\documentclass[12pt]{amsart} 
\usepackage{amssymb,amsmath,amscd,a4,graphicx,latexsym,psfrag,epsfig}

\setlength{\textwidth}{155mm} \setlength{\textheight}{225mm}
\setlength{\oddsidemargin}{0mm} \setlength{\evensidemargin}{10mm}
\setlength{\topmargin}{-10mm} \setlength{\headheight}{20mm}
\setlength{\headsep}{10mm} \setlength{\footskip}{20mm}
\setlength{\parindent}{0mm}

\usepackage[all]{xy}
\everymath{\displaystyle}

\newtheorem{teo}{Theorem}[section]
\newtheorem{lem}[teo]{Lemma}
\newtheorem{cor}[teo]{Corollary}
\newtheorem{exa}[teo]{Example}
\newtheorem{prop}[teo]{Proposition}
\newtheorem{defi}[teo]{Definition}
\newtheorem{ques}[teo]{Question}
\newtheorem{conj}[teo]{Conjecture}
\newtheorem{remark}[teo]{Remark}
\newtheorem{remarks}[teo]{Remarks}
\newtheorem{prob}[teo]{Problem}
\newtheorem{defis}[teo]{Definitions}

%% math simboli  Riccardo%%
\newcommand{\Pm}{\mathbb{P}}
\newcommand{\mr}{\mathbb{R}}
\newcommand{\mc}{\mathbb{C}}
\newcommand{\mz}{\mathbb{Z}}
\newcommand{\mh}{\mathbb{H}}
\newcommand{\mk}{\mathbb{K}}
\newcommand{\mn}{\mathbb{N}}
\newcommand{\mq}{\mathbb{Q}}
\newcommand{\mm}{\mathbb{M}}
\newcommand{\mi}{\mathbb{I}}
\newcommand{\mx}{\mathbb{X}}
\newcommand{\ma}{\mathbb{A}}
\newcommand{\md}{\mathbb{D}}
\newcommand{\ms}{\mathbb{S}}
\newcommand{\mP}{\mathbb{P}}
\newcommand{\mpi}{\mathbb P}
%%%%%%%%% calligraphic %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Yy}{{\mathcal Y}}
\newcommand{\Aa}{{\mathcal A}}
\newcommand{\Bb}{{\mathcal B}}
\newcommand{\Cc}{{\mathcal C}}
\newcommand{\Dd}{{\mathcal D}}
\newcommand{\Ee}{{\mathcal E}}
\newcommand{\Ff}{{\mathcal F}}
\newcommand{\Gg}{{\mathcal G}}
\newcommand{\Hh}{{\mathcal H}}
\newcommand{\Ii}{{\mathcal I}}
\newcommand{\Jj}{{\mathcal J}}
\newcommand{\Kk}{{\mathcal K}}
\newcommand{\Ll}{{\mathcal L}}
\newcommand{\Mm}{{\mathcal M}}
\newcommand{\Nn}{{\mathcal N}}
\newcommand{\Oo}{{\mathcal O}}
\newcommand{\Pp}{{\mathcal P}}
\newcommand{\Qq}{{\mathcal Q}}
\newcommand{\Rr}{{\mathcal R}}
\newcommand{\Ss}{{\mathcal S}}
\newcommand{\Tt}{{\mathcal T}}
\newcommand{\Uu}{{\mathcal U}}
\newcommand{\Ww}{{\mathcal W}}
\newcommand{\Vv}{{\mathcal V}}
\newcommand{\Zz}{{\mathcal Z}}
%%%%%%%%% boldface %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\CC}{{\bf C}}
\newcommand{\HH}{{\bf H}}
\newcommand{\NN}{{\bf N}}
\newcommand{\PP}{{\bf P}}
\newcommand{\RR}{{\bf R}}
\newcommand{\ZZ}{{\bf Z}}

\newcommand{\lL}{{\mathbf l}}
\newcommand{\mM}{{\mathbf m}}
\newcommand{\kaK}{{\mathbf \kappa}}

%%%%%%%%% gothic symbols %%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\SG}{{\mathfrak S}}
\newcommand{\aG}{{\mathfrak a}}
\newcommand{\bG}{{\mathfrak b}}
\newcommand{\cG}{{\mathfrak c}}
\newcommand{\HG}{{\mathfrak H}}
\newcommand{\WG}{{\mathfrak W}}
\newcommand{\gG}{{\mathfrak g}}
\newcommand{\sG}{\mathfrak s}
\newcommand{\lG}{\mathfrak l}
\newcommand{\pG}{\mathfrak p}
\newcommand{\mG}{\mathfrak m}
\newcommand{\CG}{{\mathfrak C}}
\newcommand{\tG}{{\mathfrak t}}
%%%%%%%%% vectors  symbols %%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\naV}{{\vec{\nabla}}}

%%%%%%%%%  hat symbols %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\hF}{{\widehat{F}}}
\newcommand{\hN}{{\widehat{N}}}
\newcommand{\hQ}{{\widehat{Q}}}
\newcommand{\hT}{{\widehat{T}}}
\newcommand{\hX}{{\widehat{X}}}
\newcommand{\hU}{{\widehat{U}}}
\newcommand{\hW}{{\widehat{W}}}
\newcommand{\hL}{{\widehat{L}}}
%%%%%%%%% canonical symbols %%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\C}{{\mathbb C}}
\newcommand{\Q}{{\mathbb Q}}
\newcommand{\Z}{{\mathbb Z}}
\newcommand{\R}{{\mathbb R}}
\newcommand{\X}{{\mathbb X}}
\newcommand{\M}{{\mathbb M}}
\newcommand{\D}{{\mathbb D}}
\newcommand{\N}{{\mathbb N}}


\newcommand{\appunto}[1]{\marginpar{\tiny #1}}
\def\ort#1{#1^\perp}

%%%%%%%%%%%%%%%%%%%%% SIMB FRANCESCO %%%%%%%%%%%%%%%%%%%%%%%%%


\def\arctgh{\mathrm{arctgh\, }}

\def\Dim{\emph{Proof : }}
\def\cvd{\nopagebreak\par\rightline{$_\blacksquare$}}
\def\finecapitolo{\newpage{\pagestyle{empty}\cleardoublepage}}
\def\commento#1{\par\vspace{5pt}{\Small #1}\par\vspace{5pt}}


--- START OF DOCUMENT TAIL ---
 a few analogies with the hyperbolic
3-manifolds arising as $H$-hulls of {\it quasi-Fuchsian} projective
surfaces belonging to $\Pp(S)$. For instance the curves at infinity
$C\subset \partial \mx_{-1}$ of $\Yy(C)$ play a similar r\^ole of the
Jordan curves that bound the universal coverings embedded in $\partial
\mh^3S^2_\infty$ of quasi-Fuchsian surfaces. However, there are
important difference that make the AdS behaviour much more ``tame''.
For example such Jordan curves are in general rather wild, while the
curves $C$ are Lipschitz. Moreover, taking for example
$S$ compact, for every $(F,\lambda)\in \Mm\Ll(S)$, along the ray
$(F,t\lambda)$ there is a critical value $t_0>0$ such that
$S^{t\lambda}\in \Pp(S)$ is quasi-Fuchsian only for $t<t_0$. On the
other hand, the description of $Y^{t\lambda}$ is qualitatively the
same for {\it every} $t>0$; in particular all AdS developing maps are
embeddings.
}
\end{remark}


%%% Local Variables: 
%%% mode: latex
%%% TeX-master: "HAND"
%%% End:
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1877
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: schur.tex|>
\documentclass[12pt]{amsart}
\usepackage{amsmath,amssymb,amsthm,amscd}
\usepackage{epsfig} 
%\usepackage[margin=3cm]{geometry} % To enlarge margins

\newtheorem{thm}{Theorem}
\newtheorem{lem}[thm]{Lemma}
\newtheorem{prop}[thm]{Proposition}
\newtheorem{cor}[thm]{Corollary}
\theoremstyle{remark}
\newtheorem{rmk}[thm]{Remark}
\newtheorem{ex}[thm]{Example}
\newenvironment{pf}{{\em Proof.}}{{\hfill$\Box$\medskip}}
\newcommand{\R}{{\mathbb R}}
\newcommand{\C}{{\mathbb C}}
\newcommand{\E}{{\mathsf E}}
\newcommand{\U}{{\mathfrak U}}
\newcommand{\UU}{{\mathbf U}}
\renewcommand{\H}{\mathbf{H}}
\renewcommand{\a}{\mathbf{a}}
\newcommand{\divided}[2]{#1^{(#2)}}
\renewcommand{\ge}{\geqslant}
\renewcommand{\le}{\leqslant}
\newcommand{\gl}{\mathfrak{gl}}
\renewcommand{\sl}{\mathfrak{sl}}
\newcommand{\so}{\mathfrak{so}}
\renewcommand{\sp}{\mathfrak{sp}}
\newcommand{\GL}{\mathsf{GL}}
\newcommand{\SL}{\mathsf{SL}}
\newcommand{\Sp}{\mathsf{Sp}}
\renewcommand{\O}{\mathsf{O}}
\newcommand{\SO}{\mathsf{SO}}
\newcommand{\End}{\operatorname{End}}
\newcommand{\Lie}{\operatorname{Lie}}
\newcommand{\g}{\mathfrak{g}}
\newcommand{\h}{\mathfrak{h}}
\newcommand{\N}{{\mathbb N}}
\newcommand{\Z}{{\mathbb Z}}
\newcommand{\Q}{{\mathbb Q}}
\renewcommand{\S}{\mathfrak{S}}
\renewcommand{\SS}{\mathbf{S}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\B}{\mathcal{B}}

%\numberwithin{equation}{subsection}
\parskip=3pt
\allowdisplaybreaks

\begin{document}
\title{New versions of Schur-Weyl duality}
\author{Stephen Doty}
\address{Mathematics and Statistics, Loyola University Chicago, 
 Chicago, Illinois 60626 U.S.A.}
%\curraddr{}
\thanks{These notes are based on a lecture, various versions of which I have
given in the past year, in a number of locations, including Stuttgart,
Birmingham, Queen Mary (London), Lancaster, Manchester, Oxford, and
Cambridge. I'm grateful to the organizers of those events for the
opportunity to present these ideas.}
\email{doty@math.luc.edu}


--- START OF DOCUMENT TAIL ---
 updated Jan. 2000. 
[http://www.liv.ac.uk/~su14/knotprints.html]

\bibitem[\sf Mu]{Murakami} Murakami, J., {\em The Kauffman polynomial
of links and representation theory}, Osaka J. Math. {\bf24} (1987),
745--758; {\em The representations of the $q$-analogue of Brauer's
centralizer algebras and the Kauffman polynomial of links},
Publ. Res. Inst. Math. Sci. {\bf26} (1990), 935--945.

\bibitem[\sf R]{Ringel} Ringel, C., {\em The category of modules with
good filtrations over a quasi-hereditary algebra has almost split
sequences}, Math. Z. {\bf208} (1991), 209--223.

\bibitem[\sf Sc]{S} Schur, I., {\em \"Uber die rationalen Darstellungen der
allgemeinen linearen Gruppe}, (1927). Reprinted in Schur, I., {\em
Gesammelte Abhandlungen}, Vol. III, pp. 68--85, Springer-Verlag,
Berlin, 1973.

\bibitem[\sf St]{Stanley} Stanley, R.P., {\em Enumerative
combinatorics} Vol. 1, Cambridge Studies in Advanced Math., {\bf49},
Cambridge Univ. Press, Cambridge, 1997.

\end{thebibliography}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0716
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: limit.tex|>
\documentclass[12pt]{article}

\usepackage{a4wide,amssymb,graphicx}

\usepackage{amsmath, amsthm}

%\theoremstyle{definition}
\newtheorem{definition}{Definition}
\newtheorem{theorem}{Theorem}
\newtheorem{ass}{Assumption}
\newtheorem{fact}{Fact}
\newtheorem{proposition}{Proposition}
\newtheorem{conj}{Conjecture}
\newtheorem{lemma}{Lemma}

\DeclareMathOperator{\Ai}{Ai}
\DeclareMathOperator{\Bi}{Bi}
\DeclareMathOperator{\Ei}{Ei}
\DeclareMathOperator{\Li}{Li}
\DeclareMathOperator{\erfc}{erfc}
\DeclareMathOperator{\Arg}{Arg}
\DeclareMathOperator{\LerchPhi}{LerchPhi}
\DeclareMathOperator{\e}{e}


\newcommand{\book}[1]{}


\begin{document}

%\centerline{Polygons, polyominoes, and polyhedra}

\title{Limit distributions and scaling functions}\label{Ccr}
% Use \titlerunning{Short Title} for an abbreviated version of
% your contribution title if the original one is too long

\author{\sc Christoph Richard
\\
{\it Fakult\"at f\"ur Mathematik, Universit\"at Bielefeld,}\\
{\it Postfach 10 01 31, 33501 Bielefeld, Germany}}  


\maketitle



--- START OF DOCUMENT TAIL ---
ional equation. 
Furthermore, the staircase polygon result indicates
that some generating functions may have in fact
asymptotic expansions for $q\nearrow 1$, which are
valid uniformly in the perimeter variable (i.e., not only
in the limit $x\nearrow x_c$). Such expansions would
yield scaling functions and correction-to-scaling
functions, thereby extending the formal results of the previous
section. This might be worked out for specific models, at least in the 
relevant example of staircase polygons.

\section*{Acknowledgements}

The author would like to thank Tony Guttmann and Iwan Jensen
for comments on the manuscript, and Nadine Eisner, Thomas Prellberg 
and Uwe Schwerdtfeger for helpful discussions. Financial
support by the German Research Council (Deutsche Forschungsgemeinschaft)
within the CRC701 is gratefully acknowledged.

%%%%%%%%%%%%%%%%%%%%%%%%%
% BibTeX
\bibliographystyle{plain}
\bibliography{refs16}
%
% Non-BibTeX
%\input{referenc}
%%%%%%%%%%%%%%%%%%%%%%%%%

\end{document} 
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2123
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: MovGapSol.tex|>
\documentclass[11pt]{article}
\usepackage{amssymb}
\setlength{\topmargin}{-0.5in} \setlength{\textheight}{8.7 in}
\setlength{\oddsidemargin}{-0.1in} \setlength{\evensidemargin}{0.in}
\setlength{\textwidth}{6.75in} \setlength{\headsep}{1.2cm}
\setlength{\parskip}{0.2cm} \setlength{\parindent}{0.4cm}

\pagestyle{plain}
\def\theequation {\thesection.\arabic{equation}}
\makeatletter\@addtoreset {equation}{section}\makeatother

%\renewcommand{\baselinestretch}{1.1}

\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{remark}{Remark}
\newtheorem{corollary}{Corollary}
\newtheorem{assumption}{Assumption}
\newtheorem{example}{Example}
\newtheorem{definition}{Definition}
\newtheorem{proposition}{Proposition}

\newenvironment{proof}{
    \noindent {\it Proof.}}{\hfill$\Box$
}
\newenvironment{proof1}{
    \noindent {\it Proof }}{\hfill$\Box$
}

\usepackage[dvips]{epsfig}
%\usepackage{times}
\usepackage{graphicx}

\begin{document}

\title{\bf Moving gap solitons in periodic potentials}

\author{Dmitry Pelinovsky\footnote{\small On leave from Department of Mathematics, McMaster
University, Hamilton, Ontario, Canada, L8S 4K1} and Guido Schneider \\
{\small Institut f\"{u}r Analysis, Dynamik und
Modellierung Fakult\"{a}t f\"{u}r Mathematik und Physik,} \\
{\small Universit\"{a}t Stuttgart, Pfaffenwaldring 57, D-70569
Stuttgart, Germany} }

\date{\today}
\maketitle



--- START OF DOCUMENT TAIL ---
bitem{KM} Yu.S. Kivshar and B.A. Malomed,
"Dynamics of solitons in nearly integrable systems", Rev. Mod.
Phys. {\bf 61}, 763 - 915 (1989)

\bibitem{Pankov} A. Pankov, "Periodic nonlinear Schr�dinger equation with
application to photonic crystals", Milan J. Math. {\bf 73},
259--287 (2005)

\bibitem{PSn07} D. Pelinovsky and G. Schneider, "Justification of the coupled-mode
approximation for a nonlinear elliptic problem with a periodic
potential", preprint (2007).

\bibitem{SB} A. S\'{a}nchez and A.R. Bishop, "Collective coordinates and
length-scale competition in spatially inhomogeneous
soliton-bearing equations", SIAM Review {\bf 40}, 579--615 (1998).

\bibitem{SU} G. Schneider and H. Uecker, "Nonlinear coupled mode dynamics
in hyperbolic and parabolic periodically structured spatially
extended systems", Asymp. Anal. {\bf 28}, 163--180 (2001)

\bibitem{SS} C.M. de Sterke and J.E. Sipe, ``Gap solitons'', Progress in
Optics, \textbf{33}, 203 (1994)

\end{thebibliography}



\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0688
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: sharpcirc.tex|>
\documentclass[11 pt]{article}
\usepackage{amsmath}
\usepackage{amsthm}
%\usepackage{graphicx}
\usepackage{bbm,amssymb}
\usepackage{bbold}
\usepackage{amsfonts,ifthen}
\usepackage[pdftex]{graphicx,color}
\usepackage[hyperfootnotes=false]{hyperref}

\addtolength{\oddsidemargin}{-.0in}
\addtolength{\evensidemargin}{-.0in}
\addtolength{\textwidth}{.0in}

\def\topfraction{.9}
\def\floatpagefraction{.8}

\newcommand{\floor}[1]{\lfloor {#1} \rfloor}
\newcommand{\ceil}[1]{\lceil {#1} \rceil}
\newcommand{\binomial}[2]{\left( \begin{array}{c} {#1} \\
                        {#2} \end{array} \right)}

\hyphenation{qua-si-ran-dom}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{prop}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}

\theoremstyle{remark}
\newtheorem*{remark}{Remark}
\newtheorem*{example}{Example}

\theoremstyle{definition}

\def\liminf{\mathop{\rm lim\,inf}\limits}
\def\Leb{\mathcal{L}}
\def\normal{{\bf n}}
\def\Points{{::}}
\def\div{{\text{div}\hspace{0.5ex}}}
\def\setcolon{{\hspace{0.5ex}:\hspace{0.5ex}}}
\def\Diam{\,\mbox{Diam}}

\title{Strong Spherical Asymptotics for Rotor-Router Aggregation and the Divisible Sandpile}
\author{Lionel Levine\footnote{supported by an NSF Graduate Research Fellowship, and NSF 
grant DMS-0605166; {\tt levine(at)math.berkeley.edu}}~~and Yuval Peres\footnote{partially supported by NSF grant DMS-0605166; {\tt peres(at)stat.berkeley.edu}} \\ University of California, Berkeley and Microsoft Research}
\date{October 7, 2008}

\DeclareSymbolFont{AMSb}{U}{msb}{m}{n}
\DeclareMathSymbol{\C}{\mathbin}{AMSb}{"43} 
\DeclareMathSymbol{\EE}{\mathbin}{AMSb}{"45} 
\DeclareMathSymbol{\N}{\mathbin}{AMSb}{"4E} 
\DeclareMathSymbol{\PP}{\mathbin}{AMSb}{"50} 
\DeclareMathSymbol{\Q}{\mathbin}{AMSb}{"51} 
\DeclareMathSymbol{\R}{\mathbin}{AMSb}{"52} 
\DeclareMathSymbol{\Z}{\mathbin}{AMSb}{"5A}

\begin{document}

\maketitle
\renewcommand{\thefootnote}{}
\footnote{{\bf\noindent Keywords:} abelian sandpile, asymptotic shape, discrete Laplacian, divisible sandpile,  growth model, internal diffusion limited aggregation, rotor-router model}
\footnote{{\bf\noindent 2000
Mathematics Subject Classifications:} Primary 60G50; Secondary 35R35}
\renewcommand{\thefootnote}{\arabic{footnote}}



--- START OF DOCUMENT TAIL ---
ncer} {\bf 27} (2005), no. 3, 9--11.

\bibitem{scalinglimit} L. Levine and Y. Peres, Scaling limits for internal aggregation models with multiple sources.  \url{http://arxiv.org/abs/0712.3378}.

\bibitem{Lindvall} T. Lindvall, {\it Lectures on the Coupling Method}, Wiley, 1992.

\bibitem{PDDK} V. B. Priezzhev, D. Dhar, A. Dhar, and S. Krishnamurthy, Eulerian walkers as a model of self-organised criticality, {\it Phys.\ Rev.\ Lett.}  {\bf 77} (1996) 5079--82.

\bibitem{Propp} J. Propp, Three lectures on quasirandomness, available at \url{http://faculty.uml.edu/jpropp/berkeley.html}.

\bibitem{Spitzer} F. Spitzer, {\it Principles of Random Walk}, Springer, 1976.

\bibitem{Uchiyama} K. Uchiyama, Green's functions for random walks on $\Z^N$, \emph{Proc.\ London Math.\ Soc.} \textbf{77} (1998), no.\ 1, 215--240. 

\bibitem{VdH} J. Van den Heuvel, Algorithmic aspects of a chip-firing game, {\it Combin. Probab. Comput.} {\bf 10}, no. 6 (2001), 505--529.

\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1584
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: article.tex|>
%\usepackage{showlabels}
%\setlength{\parskip}{\medskipamount}


\documentclass{article}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{harvard}
\usepackage{latexsym}
\usepackage{amsmath,amsfonts,amssymb}
\usepackage{ifthen}
\usepackage{harvard}
\usepackage{latexsym}
\usepackage[nohead]{geometry}

\setcounter{MaxMatrixCols}{10}
%TCIDATA{OutputFilter=LATEX.DLL}
%TCIDATA{Version=5.00.0.2552}
%TCIDATA{<META NAME="SaveForMode" CONTENT="1">}
%TCIDATA{LastRevised=Wednesday, February 21, 2007 18:51:32}
%TCIDATA{<META NAME="GraphicsSave" CONTENT="32">}
%TCIDATA{Language=American English}
%TCIDATA{CSTFile=article.cst}

\provideboolean{uglystyle}
\setboolean{uglystyle}{true}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{definition}[theorem]{Definition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{remark}[theorem]{Remark}
\newcounter{tcnt}[theorem]
\renewcommand{\thetcnt}{(\alph{tcnt})}
\newcounter{pcnt}[theorem]
\renewcommand{\thepcnt}{(\alph{pcnt})}
\newcounter{ccnt}[theorem]
\renewcommand{\theccnt}{(\alph{ccnt})}
\newcounter{rcnt}[theorem]
\renewcommand{\thercnt}{(\roman{rcnt})}
\ifthenelse{\boolean{uglystyle}}{
\sloppy
\renewcommand{\baselinestretch}{1.45}
\usepackage{leqno}
}{
}
\input{tcilatex}
\renewcommand{\baselinestretch}{1.4}
\fontsize{13pt}{13pt} \selectfont
\renewcommand{\O}{{\cal O}}
\newcommand{\finishProof}{{\hfill $\Box$}}
\newlength{\myparindent}
\renewcommand{\thercnt}{(\roman{rcnt})}
\newcommand{\myenumi}{\renewcommand{\theenumi}{\alph{enumi}}}
\myenumi
\renewcommand{\thercnt}{(\roman{rcnt})}
\sloppy
\geometry{left=1in,right=1in,top=1in,bottom=0.5in}

\begin{document}

\title{\textsc{Can One Estimate The Unconditional Distribution of
Post-Model-Selection Estimators? }}
\author{Hannes Leeb \\
%EndAName
Department of Statistics, Yale University\\
and \and Benedikt M. P\"{o}tscher \\
%EndAName
Department of Statistics, University of Vienna}
\date{First version: \ April 2005\\
Revised version: \ February 2007}
\maketitle



--- START OF DOCUMENT TAIL ---
    \global\tag@false
        \global\@ignoretrue 
      \fi
     \else   
      \iftag@
        \addtocounter{equation}{-1} % undo the increment made in the begin part
        \eqno \hbox{\@taggnum}
        \global\tag@false%
        $$\global\@ignoretrue
      \else
        \eqno \hbox{\@eqnnum}% $$ BRACE MATCHING HACK
        $$\global\@ignoretrue
      \fi
     \fi\fi
 } 

 \newif\iftag@ \tag@false
 
 \def\TCItag{\@ifnextchar*{\@TCItagstar}{\@TCItag}}
 \def\@TCItag#1{%
     \global\tag@true
     \global\def\@taggnum{(#1)}}
 \def\@TCItagstar*#1{%
     \global\tag@true
     \global\def\@taggnum{#1}}

  \@ifundefined{tag}{
     \def\tag{\@ifnextchar*{\@tagstar}{\@tag}}
     \def\@tag#1{%
         \global\tag@true
         \global\def\@taggnum{(#1)}}
     \def\@tagstar*#1{%
         \global\tag@true
         \global\def\@taggnum{#1}}
  }{}
% Do not add anything to the end of this file.  
% The last section of the file is loaded only if 
% amstex has not been.



\makeatother
\endinput
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0378
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: Duits-KuijlaarsArxiv.tex|>
\documentclass[11pt,reqno]{amsart}

\usepackage{amssymb}
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{graphicx}

\newcommand{\C}{\mathbb{C}}
\newcommand{\T}{\mathbb{T}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Linfty}{{\mathbb{L}_{\infty}}}
\newcommand{\OO}{\mathcal O}
\newcommand{\eps}{\varepsilon}
\newcommand{\dist}{\mathop{\mathrm{dist}}}
\newcommand{\supp}{\mathop{\mathrm{supp}}}
\newlength{\intwidth}
\DeclareMathOperator{\spec}{sp}
\newcommand{\h}{{\frac{1}{2}}}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{Remark}[theorem]{Remark}
\newtheorem{Example}[theorem]{Example}

\newenvironment{remark}{\begin{Remark}\rm}{\end{Remark}}
\newenvironment{example}{\begin{Example}\rm}{\end{Example}}
\numberwithin{equation}{section}

\title{An equilibrium problem for the limiting eigenvalue distribution of
banded Toeplitz matrices}
\author{Maurice Duits \and Arno B.J. Kuijlaars}
\thanks{Department of Mathematics, Katholieke Universiteit Leuven,
 Celestijnenlaan 200B, 3001 Leuven, Belgium.
 (maurice.duits@wis.kuleuven.be,
arno.kuijlaars@wis.kuleuven.be). The first author is a research
assistant of the Fund for Scientific Research -- Flanders. The
authors were supported by the European Science Foundation Program
MISGAM. The second author is supported by FWO-Flanders project
G.0455.04, by K.U. Leuven research grant OT/04/21, by Belgian
Interuniversity Attraction Pole NOSY P06/02, and by a grant from the
Ministry of Education and Science of Spain, project code
MTM2005-08648-C02-01. }


\begin{document}


\maketitle



--- START OF DOCUMENT TAIL ---
s 28,
    Cambridge University Press, Cambridge, 1995.
\bibitem{Saff-Totik}
    E.B. Saff and V. Totik,
    Logartihmic Potentials with External Fields,
    Grundlehren der Mathematischen Wissenschaften {316},
    Springer-Verlag, Berlin, 1997.
\bibitem{Schmidt-Spitzer}
    P. Schmidt and F. Spitzer,
    The Toeplitz matrices of an arbitrary Laurent polynomial,
    Math. Scand., 8 (1960), pp. 15-38.
\bibitem{Simeonov}
    P. Simeonov,
    A weigthed energy problem for a class of admissible weights,
    Houston J. Math., 31 (2005), pp.  1245-1260.
\bibitem{trefethenembree}
    L.N. Trefethen and M. Embree,
    Spectra and Pseudospectra,
    Princeton University Press, Princeton, NJ, 2005.
\bibitem{Ullman}
    J.L. Ullman,
    A problem of Schmidt and Spitzer,
    Bull. Amer. Math. Soc., 73 (1967), pp. 883-885.
\bibitem{Widom}
    H. Widom,
    On the eigenvalues of certain Hermitean operators,
    {Trans. Amer. Math. Soc.}, {88} (1958), pp. 491-522.
\end{thebibliography}
\end{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2133
```latex
--- START OF DOCUMENT HEAD ---
% <|ROOT: spccmp06-19.tex|>

\documentclass[oneside,12pt]{article}
\usepackage{amsfonts,amsmath,amssymb,mathrsfs}
\usepackage{dsfont}
\usepackage{graphicx}% Include figure files
%\usepackage{dcolumn}% Align table columns on decimal point
\usepackage{bm}
\begin{document}
\title{On Adiabatic Pair Creation}

\author{Peter Pickl\footnote{Institut f\"ur theoretische Physik, Universit\"{a}t
        Wien, Boltzmanngasse 5, 1090 Vienna, Austria
         E-mail: pickl@mathematik.uni-muenchen.de}, Detlef Duerr\footnote{Mathematisches Institut der Universit\"{a}t
         M\"{u}nchen, Theresienstra{\ss}e 39, 80333 M\"{u}nchen, Germany.
         E-mail: duerr@mathematik.uni-muenchen.de}}
\date{\today}% It is always \today, today,
             %  but any date may be explicitly specified




%\documentclass[showpacs,preprintnumbers,amsmath,amssymb]{revtex4}
%\documentclass[preprint,showpacs,preprintnumbers,amsmath,amssymb]{revtex4}

% Some other (several out of many)  possibilities
%\documentclass[preprint,aps]{revtex4}
%\documentclass[preprint,aps,draft]{revtex4}
%\documentclass[prb]{revtex4}% Physical Review B

% bold math



\newtheorem{thm}{Theorem}[section]
\newtheorem{cor}[thm]{Corollary}
\newtheorem{lem}[thm]{Lemma}
\newtheorem{proof}[thm]{Proof}
\newtheorem{prop}[thm]{Proposition}
%\theoremstyle{definition}
\newtheorem{defn}[thm]{Definition}
%\theoremstyle{remark}
\newtheorem{rem}[thm]{Remark}
\newtheorem{con}[thm]{Condition}
\newtheorem{nota}[thm]{Notation}
%\numberwithin{equation}{section}


\newcommand{\ed}{\bf}
\newcommand{\eed}{\rm}

\sloppy

%\preprint{APS/123-QED}
\maketitle


--- START OF DOCUMENT TAIL ---
 S. Ito, R. Schule, D. Schwalm, K. E. Stiebing, N. Trautmann, P. Vincent
%and M. Waldschmidt,
Observation of a Peak Structure in Positron Spectra from U+Cm
Collisions, Phys. Rev. Letters {\bf 51}, 2261--2264 (1983).

\bibitem{PRLgreiner} Smith K., Peitz H., M\"uller B. and Greiner W.:
Induced Decay of the Neutral Vaccum in Overcritical Fields Occurring
in Heavy-Ion Collisions, Phys. Rev. Lett. {\bf 32}, 554--556 (1974).


\bibitem{stefan} Teufel S.:
Adiabatic Perturbation Theory in Quantum Dynamics, Springer Verlag,
Berlin (2000).

\bibitem{teufel} Teufel S.:
The flux-across-surfaces theorem and its implications for scattering
theory, Dissertiation an der Ludwig-Maximilians-Universit\"at,
M\"unchen (1999).

\bibitem{thaller} Thaller B.: The Dirac equation, Springer Verlag,
Berlin (1992).






\bibitem{yamada}  Yamada O.:  Eigenfunction expansions and scattering theory for Dirac operators, Publ. RIMS. Kyoto Univ., {\bf 11},
651-689 (1976).








\end{thebibliography}

\end{document}
```
--------------------------------------------------------------------------------

