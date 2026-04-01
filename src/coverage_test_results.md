# Window of Interest Coverage Test

Review these outputs to ensure the `\author` and affiliation blocks are caught inside the window.

## Paper ID: 0704.0295
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1822
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1164
```latex
% <|ROOT: persym.tex|>
\documentclass[reqno,centertags, 12pt]{amsart}
\usepackage{amsmath,amsthm,amscd,amssymb}
\usepackage{latexsym,verbatim}
%\usepackage{showkeys}

\usepackage{graphicx,epsf}

\textheight 21cm \topmargin 0cm \leftmargin 0cm \marginparwidth 0mm
\textwidth 16.6cm \hsize \textwidth \advance \hsize by
-\marginparwidth \oddsidemargin -4mm \evensidemargin \oddsidemargin

%%%%%%%%%%%%% fonts/sets %%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\bbN}{{\mathbb{N}}}
\newcommand{\bbR}{{\mathbb{R}}}
\newcommand{\bbD}{{\mathbb{D}}}
\newcommand{\bbP}{{\mathbb{P}}}
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1330
```latex
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
\catcode`\@=12

\newcommand{\ad}{\operatorname{ad}}
\newcommand{\Ad}{\operatorname{Ad}}
\newcommand{\Alt}{\operatorname{Alt}}
\newcommand{\Aut}{\operatorname{Aut}}
\newcommand{\Diff}{\operatorname{Diff}}
\newcommand{\End}{\operatorname{End}}
\newcommand{\gr}{\operatorname{gr}}
\newcommand{\im}{\operatorname{im}}
\newcommand{\mor}{\operatorname{mor}}
\newcommand{\Span}{\operatorname{span}}
\newcommand{\sign}{\operatorname{sign}}
\newcommand{\sym}{\operatorname{sym}}
\newcommand{\tr}{\operatorname{tr}}

\def\eqdef{\overset{\text{def}}{=}}

\newlength{\globalparindent}
\setlength{\globalparindent}{\parindent}

\newcommand{\udot}{{\mathaccent\cdot\cup}}



\def\la{\langle}
\def\ra{\rangle}

\def\bbF{{\mathbb F}}
\def\bbQ{{\mathbb Q}}
\def\bbR{{\mathbb R}}
\def\bbZ{{\mathbb Z}}
\def\hatJ{{\hat J}}
\def\calC{{\mathcal C}}
\def\calF{{\mathcal F}}
\def\calH{{\mathcal H}}
\def\calO{{\mathcal O}}
\def\calX{{\mathcal X}}

\newcommand{\Kh}{{\text{\it Kh}}}
\newcommand{\qdim}{\operatorname{{\it q}dim}}


\d
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0831
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1941
```latex
% <|ROOT: tait.tex|>

\documentclass[twoside]{article}
\usepackage{a4,txmac,%
%case,%
%bibenc,%
%myrot,%
mypic,%
%epsf,%
nocaphead,%
amssymb,times,mathptm}

\makeatletter

\advance\oddsidemargin by -1.7cm
\advance\evensidemargin by -1.7cm
\advance\textwidth by 3.4cm

\def\mynewtheo#1#2{%
\newtheorem{@#1}{#2}[section]%
\newenvironment{#1}{\begin{@#1}\rm}{\end{@#1}}}
 
\mynewtheo{lemma}{Lemma}
\mynewtheo{exer}{Exercise}
\mynewtheo{theo}{Theorem}
\mynewtheo{rem}{Remark}
\mynewtheo{defi}{Definition}
\mynewtheo{conj}{Conjecture}
\mynewtheo{corr}{Corollary}
\mynewtheo{prop}{Proposition}
\mynewtheo{question}{Question}
\mynewtheo{exam}{Example}

\def\inx{\mathop {\operator@font ind}\mathord{}}
\def\mpb{\mathop {\operator@font mpb}\mathord{}}
\def\mwf{\mathop {\operator@font mwf}\mathord{}}
\def\spn{\mathop {\operator@font span}\mathord{}}
\def\len{\mathop {\operator@font len}\mathord{ }}

\def\ffrac#1#2{\mbox{\small$\ds\frac{#1}{#2}$}}

% \newenvironment{eqn}{\begin{equation}}{\end{equation}}
\newenvironment{theorem}{\begin{theo}}{\end{theo}}

\def\eqref#1{\mbox{(\protect\reference{#1}})}
\def\proof{\@ifnextchar[{\@proof}{\@proof[\unskip]}}
\def\@proof[#1]{\noindent{\bf Proof #1.}\enspace}

\pagestyle{headings}

\begin{document}

\author{A. Stoimenow\footnotemark[1]\\[2mm]
\small Research Institute for Mathematical Sciences, \\
\small Kyoto University, Kyoto 606-8502, Japan\\
\small e-mail: {\tt stoimeno@kurims.kyoto-u.ac.jp}\\
\small WWW: {\hbox{\web|http://www.kurims.kyoto-u.ac.jp/~stoimeno/|}}
}

{\def\thefootnote{}
\footnotetext[1]{This is a preprint. I would be grateful
  for any comments and corrections. Current
  version: \today\ \ \ First version: \makedate{13}{4}{2007}}
\def\thefootnote{\fnsymbol{footnote}}
\footnotetext[1]{Financial support by the 21st Century COE Program
% ``Formation of an international center of excellence in the frontiers
% of mathematics and fostering of researchers in future generations''
is acknowledged.}
}

\title{\large\bf
\uppercase{Tait's conjectures and}\\[2mm] 
\uppercase{odd crossing number amphicheiral knots}
}

\date{}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1001
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2146
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2384
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1066
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0787
```latex
% <|ROOT: template.tex|>
%%%%%%%%%%%%%%%%%%%%%%% file template.tex %%%%%%%%%%%%%%%%%%%%%%%%%
%
% This is a template file for the LaTeX package SVJour2 for the
% Springer journal "Numerische Mathematik".
%
%                                    Springer Heidelberg 2004/12/07
%
% Copy it to a new file with a new name and use it as the basis
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2169
```latex
2} & {#3}\\ 
\mapdown{#4} && \mapdown{#5} \\ 
{#6} & \mapright{#7} & {#8} 
\end{array} 
} 
\newcommand{\mapdown}[1]{\Big\downarrow 
\rlap{$\vcenter{\hbox{$\scriptstyle#1$}}$}} 
\newcommand{\mapright}[1]{\smash{ 
\mathop{\longrightarrow}\limits^{#1}}} 
% 
\newcommand{\medskipnoindent}{\par\medskip\par\noindent} 
% 
% 
\newcommand{\one} 
{{{\mathchoice \mathrm{ 1\mskip-4mu l} \mathrm{ 1\mskip-4mu l} 
\mathrm{ 1\mskip-4.5mu l} \mathrm{ 1\mskip-5mu l}}}} 
% 
\newcommand{\dslash}{/\mskip-6mu/} 
% 
% 
\newcommand{\A}{{\mathbb{A}}} 
\newcommand{\B}{{\mathbb{B}}} 
\newcommand{\C}{{\mathbb{C}}} 
\newcommand{\D}{{\mathbb{D}}} 
\newcommand{\F}{{\mathbb{F}}} 
\renewcommand{\H}{{\mathbb{H}}} 
\newcommand{\LL}{{\mathbb{L}}} 
\newcommand{\M}{{\mathbb{M}}} 
\newcommand{\N}{{\mathbb{N}}} 
\newcommand{\Q}{{\mathbb{Q}}} 
\newcommand{\R}{{\mathbb{R}}} 
\renewcommand{\SS}{{\mathbb{S}}} 
\newcommand{\T}{{\mathbb{T}}}  
\renewcommand{\u}{{\mathbf{u}}} 
\renewcommand{\v}{{\mathbf{v}}} 
\newcommand{\W}{{\mathbb{W}}} 
\newcommand{\x}{{\mathbf{x}}} 
\newcommand{\Z}{{\mathbb{Z}}} 
% 
\newcommand{\Arg}{\mathrm{Arg}}  % Arg 
\newcommand{\coker}{\mathrm{ coker }}  % cokernel 
\newcommand{\im}{\mathrm{ im }}        % image 
\newcommand{\range}{\mathrm{ range }}  % range 
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0095
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0665
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1778
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0805
```latex
pported/mdwtools/

% V1.6 of IEEEtran contains the IEEEeqnarray family of commands that can
% be used to generate multiline equations as well as matrices, tables, etc.

% Also of notable interest:

% Scott Pakin's eqparbox package for creating (automatically sized) equal
% width boxes. Available:
% http://www.ctan.org/tex-archive/macros/latex/contrib/supported/eqparbox/

% Notes on hyperref:
% IEEEtran.cls attempts to be compliant with the hyperref package, written
% by Heiko Oberdiek and Sebastian Rahtz, which provides hyperlinks within
% a document as well as an index for PDF files (produced via pdflatex).
% However, it is a tad difficult to properly interface LaTeX classes and
% packages with this (necessarily) complex and invasive package. It is
% recommended that hyperref not be used for work that is to be submitted
% to the IEEE. Users who wish to use hyperref *must* ensure that their
% hyperref version is 6.72u or later *and* IEEEtran.cls is version 1.6b
% or later. The latest version of hyperref can be obtained at:
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1308
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0537
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0469
```latex
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


\email{urzua@math.umass.edu}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1926
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1361
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1231
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1022
```latex
%%%distr of limit process

\def\btil{{\tilde{b}}}
\def\etil{{\tilde{e}}}
\def\mtil{{\tilde{m}}}
\def\ytil{{\tilde{y}}}
\def\omtil{{\tilde{\omega}}}
\def\etatil{{\tilde{\eta}}}
\def\xitil{{\tilde{\xi}}}
\def\gammatil{{\tilde{\gamma}}}
\def\sigmatil{{\tilde{\sigma}}}
\def\ztil{{\tilde{z}}}
\def\xtil{{\tilde{x}}}
\def\Etil{{\widetilde{E}}}
\def\Ptil{{\widetilde{P}}}
\def\Xtil{{\widetilde{X}}}
\def\Sbar{{\widebar{S}}}
\newcommand*{\tfl}[1]{\lfloor{#1}\rfloor}

%%% Firas' defitions

%\def\qed{\hfill{$\Box$}} % No need, since it exists in AMS-LaTex
%% This one is the one PTRF uses:
%\def\squareforqed{\hbox{\rlap{$\sqcap$}$\sqcup$}}
%\def\qed{\ifmmode\else\unskip\quad\fi\squareforqed}
%\def\smartqed{\def\qed{\ifmmode\squareforqed\else{\unskip\nobreak\hfil
%\penalty50\hskip1em\null\nobreak\hfil\squareforqed
%\parfillskip=0pt\finalhyphendemerits=0\endgraf}\fi}}
% I like the AMS box best!

\def\cA{\mathcal{A}} 
\def\Ac{\mathcal{A}} 
\def\cB{\mathcal{B}}
\def\cC{\mathcal{C}}
\def\cE{\mathcal{E}}
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0324
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1340
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0014
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1121
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0231
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0942
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1236
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0813
```latex
mand{\bx}{{\bf x}}
\newcommand{\by}{{\bf y}}
\newcommand{\bz}{{\bf z}}
\newcommand{\bh}{{\bf h}}
\newcommand{\bK}{{\bf K}}
\newcommand{\bn}{{\bf n}}
\newcommand{\bX}{{\bf X}}
\newcommand{\bV}{{\bf V}}
\newcommand{\bY}{{\bf Y}}
\newcommand{\bA}{{\bf A}}
\newcommand{\ve}[1]{\bf #1}
\newcommand{\ax}{{\langle x \rangle}}
\newcommand{\axi}{{\langle \xi \rangle}}
\newcommand{\axil}{{\langle \xi_l \rangle}}
\newcommand{\axij}{{\langle \xi_j \rangle}}
\newcommand{\axik}{{\langle \xi_k \rangle}}
\newcommand{\aeta}{{\langle \eta \rangle}}
\newcommand{\aetal}{{\langle \eta_l \rangle}}
\newcommand{\aetaj}{{\langle \eta_j \rangle}}
\newcommand{\aetak}{{\langle \eta_k \rangle}}
\newcommand{\ay}{{\langle y \rangle}}
\newcommand{\aq}{{\langle q \rangle}}
\newcommand{\at}{{\langle t \rangle}}

\newcommand{\tU}{{\widetilde U}}
\newcommand{\tJ}{{\widetilde J}}
\newcommand{\tA}{{\widetilde A}}
\newcommand{\tb}{{\tilde b}}
\newcommand{\tc}{{\tilde c}}
\newcommand{\tk}{{\tilde k}}
\newcommand{\tp}{{\tilde p}}
\newcommand{\tq}{{\tilde q}}
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0993
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1043
```latex
% <|ROOT: LongAbstractDelahaye2.tex|>
\documentclass{ws-rv9x6}
\usepackage{ws-rv-van}             % numbered citation/references (default)
%\usepackage{ws-index}             % to produce multiple indices
\makeindex
%\newindex{aindx}{adx}{and}{Author Index}       % author index
%\renewindex{default}{idx}{ind}{Subject Index}  % subject index
\begin{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0069
```latex
egin{minipage}[t]{4.25in} \sf  {\small {#1}\normalsize}  \end{minipage}}}\end{table}\medskip}



\newcommand{\bounded}{L^{\infty}_{\text{loc}}}
\newcommand{\continuous}{C^0}
\newcommand{\smooth}{C^{\infty}}
\newcommand{\analytic}{C^{\omega}}
\newcommand{\pluriharmonic}{\sheaf{H}}
\newcommand{\sheaf}{\ms}
\newcommand{\ring}{}
\newcommand{\ringhom}{\hat}
\newcommand{\module}{}
\newcommand{\bundle}{\mc}
\newcommand{\Div}{\operatorname{Div}} % Divisors


% Derivatives
\newcommand{\edhol}{{\partial}} % the holomorphic part of the exterior derivative (p,q)->(p+1,q)
\newcommand{\edantihol}{{\partial}} % the antiholomorphic part of the exterior derivative (p,q)->(p,q+1)
\newcommand{\ed}{\msans{d}} % the exterior derivative
\newcommand{\edconj}{\msans{d}^c} % the conjugate of the exterior derivative, a real operator
\newcommand{\dbar}{{\partial}}


% Common Operations
\newcommand{\abs}[1]{\vert #1\vert}
\newcommand{\norm}[1]{\| #1\|}
\newcommand{\logabs}[1]{\log\vert #1\vert}
\newcommand{\conj}[1]{\overline{#1}}
\newcommand{\rest}[1]{{\big\arrowvert_{#1}}}


% Common Named Operators 
\DeclareMathOperator{\re}{Re}
\DeclareMathOperator{\im}{Im}
\DeclareMathOperator{\supp}{Supp}
\DeclareMathOperator{\spec}{Spec}
\newcommand{\id}[1]{{\operatorname{id}_{#1}}}


% Common Spaces
\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0802
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0914
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2359
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1986
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2403
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0501
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1980
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0098
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1694
```latex
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
yekhanin@mit.edu}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2048
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0994
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1221
```latex
% <|ROOT: Ciocci_Langerock_revision2.tex|>
\documentclass[a4paper,10pt]{article}

\setlength{\unitlength}{1mm}
%\usepackage{float}
\usepackage[english]{babel}
%\usepackage{subeqnarray}
\usepackage{amssymb}
\usepackage{amsbsy}
\usepackage{amsmath}
\usepackage{epsfig}
\usepackage{graphicx}
\usepackage{psfrag}
\usepackage{pstricks}
\usepackage{a4}
%\usepackage{concrete}
% the following makes the references visible
%\usepackage[notcite,notref]{showkeys}

%\newenvironment{remark}{\vskip 12pt \noindent {\bf Remark}\rm}{}
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2328
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1411
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2055
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1526
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0022
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0283
```latex
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
\def\ddx{{\text{d} \over {\text{d}x}}}
\def\dydx{{\text{d}y \over {\text{d}x}}}
\def\dudx{{\text{d}u \over {\text{d}x}}}
\def\dxdt{{\text{d}x \over {\text{d}t}}}
\def\dydt{{\text{d}y \over {\text{d}t}}}
\def\ddt#1{{\text{d} {#1} \over {\text{d}t}}}
\def\dd#1#2{{\text{d} {#1} \over {\text{d} {#2} }}}
\def\pd{\partial}
%\baselineskip=20pt
%\input mssymb
\def\boxit#1{\vbox{\hrule\hbox{\vrule \kern3pt
\vbox{\kern3pt\hbox{#1}\kern3pt}\kern3pt\vrule}\hrule}}
\def\rabbit{\vbox{\hbox{\kern0pt
\vbox{\kern0pt{\hbox{---}}\kern3.5pt}}}}
\def\qchoose#1#2{\left[{{#1} \atop {#2}}\right]}
\def\lchoose#1#2{\left({{#1} \over {#2}}\right)}
\font\bigf=cmbx10 scaled\magstep3
\font\bigmi=cmmi10 scaled\magstep3

\def\Tableau#1{\tableau {#1}}

\def\tableau#1{
        \hbox {
                \hskip -10pt plus0pt minus0pt
                \raise\baselineskip\hbox{
                \offinterlineskip
                \hbox{#1}}
                \hskip0.25em
        }
}

\def\tabCol#1{
\hbox{\vtop{\hrule
\halign{\strut\vrule\hskip0.5em##\hskip0.5
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2452
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1009
```latex
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
\author{Behrang Noohi}
\email{behrang@alum.mit.edu}       % First Author's email
\address{Mathematics Department\\ % First Author's postal address
         Florida State University\\
         208 Love Building\\
         Tallahassee,  FL 32306-4510 \\
         U.S.A.}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1818
```latex
owtay}{\ensuremath{\mu}}

\newcommand{\ErrFun}{\ensuremath{L}}
\newcommand{\ErrFunTil}{\ensuremath{\wtil{\ErrFun}}}

\newcommand{\ldpcthresh}{\ensuremath{\nu^*}}


\newcommand{\zeroes}{\ensuremath{0^\topbit}}

\newcommand{\mybeginproof}{\noindent \emph{Proof: $\;$}}
\newcommand{\myendproof}{\hfill \qed}

% A common width for several of the figures in the paper
\newcommand{\commonwidth}{0.36\textwidth}

\newcommand{\Numc}{\ensuremath{T_\topbit}}
\newcommand{\mprob}{\ensuremath{\mathbb{P}}}
\newcommand{\cwind}[1]{\ensuremath{Z^{#1}}}
\newcommand{\cw}[1]{\ensuremath{X^{#1}}}

\newcommand{\ysca}{\ensuremath{y}}
\newcommand{\Ysca}{\ensuremath{Y}}

\newcommand{\ssca}{\ensuremath{s}}
\newcommand{\Ssca}{\ensuremath{S}}

\newcommand{\svar}{\ensuremath{s}}
\newcommand{\Svar}{\ensuremath{S}}

\newcommand{\Qnoise}{\ensuremath{E}}
\newcommand{\qnoise}{\ensuremath{e}}



\newcommand{\codebit}{\ensuremath{x}}
\newcommand{\infobit}{\ensuremath{y}}
\newcommand{\recbit}{\ensuremath{v}}


\newcommand{\Codebit}{\ensuremath{X}}
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1033
```latex
% <|ROOT: embeddings.tex|>
\documentclass[12pt,psamsfonts]{article} 
\usepackage{a4,fullpage,amssymb,epsf,psfrag,times}
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1313
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2380
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0542
```latex
ow labels %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifthenelse{\equal{\finalized}{yes}}%
{\newcommand\mylabel[1]{\label{#1}}}%
{\newcommand\mylabel[1]{\label{#1}\marginpar{[{\ttfamily\upshape\tiny #1}]}}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%  To indicate checked portions %%%%%%%%%%%%%%%
\usepackage{ragged2e}
\ifthenelse{\equal{\finalized}{yes}}%
{\newcommand\checked[1]{}}%
{\newcommand\checked[1]{\marginpar{[{\ttfamily\upshape\tiny CHECKED: #1}]}}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%  To indicate spell checked portions %%%%%%%%%%%%%%%
\ifthenelse{\equal{\finalized}{yes}}%
{\newcommand\spellchecked[1]{}}%
{\newcommand\spellchecked[1]{\marginpar{[{\ttfamily\upshape\tiny SPELLCHECKED: #1}]}}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%  These commands change on with \version (private or public)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\providecommand\version{public}   %  setting default  
%%%%%%%%%%%%%%%%%%%%%   To show other marginal comments %%%%%%%%%%%%%%%%%%
\ifthenelse{\equal{\version}{public}}%
{\newcommand\mcomment[1]{}}%
{\newcommand\mcomment[1]{\marginpar{{\raggedright\sffamily\upshape\tiny #1}}}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%  For comments as footnotes %%%%%%%%%%%%%%%%%%%%%%
\ifthenelse{\equal{\version}{public}}%
{\newcommand\fcomment[1]{}}%
{\newcommand\fcomment[1]{\footnote{#1}}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%   Reading definitions in %%%%%%%%%%%%%%%%%%%%%%%%%%%%
\input{definitions}
%\input{shyama-definitions}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%   For indexing     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{makeidx}
%\usepackage{makeidx,showidx,index}
%\indexproofstyle{\footnotesize\tiny}
%\shortindexingon
\ifthenelse{\equal{\finalized}{no}}{\makeindex}{}
%\makeatletter\show\@input@\makeatother

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%   For authorindex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1632
```latex
kage{pdfsync} 
% \else
% \usepackage{graphicx}
% \fi

%\textwidth = 6 in
%\textheight = 8 in
%\oddsidemargin = 0.0 in
%\evensidemargin = 0.0 in
%\topmargin = 0.0 in
%\headheight = 0.0 in
%\headsep = 0.0 in
%\parindent = 0.0in
\parskip = 0.1 in

%---------------------------Macros-----------------------------





% Theorems

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark} 
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{example}[theorem]{Example} 
\newtheorem{notation}[theorem]{Notation}
\newtheorem{question}[theorem]{Question}




\newcommand{\Subsection}[1]{\subsection{ #1} ${}^{}$}




\newcounter{hypo}

\newenvironment{hyp}{\renewcommand{\theenumi}{{\bf (A\arabic{enumi})}} \renewcommand{\labelenumi}{\theenumi} \begin{enumerate} \setcounter{enumi}{\value{hypo}} \item}{\stepcounter{hypo} \end{enumerate}}

\newenvironment{hypp}{\renewcommand{\theenumi}{{\bf (A\arabic{enumi})$_{\mathbf +}$}} \renewcommand{\labelenumi}{\theenumi} \begin{enumerate} \setcounter{enumi}{\value{hypo}} \item}{\stepcounter{hypo} \end{enumerate}}

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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1948
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0739
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1782
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2183
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1975
```latex
mathcal C}}
\newcommand{\cc}{{\mathfrak C}}
\newcommand{\D}{{\mathbb D}}\newcommand{\DD}{{\mathbb D}^2}\newcommand{\ddd}{{\mathcal D}}
\newcommand{\e}{{\mathfrak e}}
\newcommand{\f}{{\mathfrak f}}
\newcommand{\FF}{{\mathcal F}}
\newcommand{\g}{{\mathfrak g}}
\newcommand{\h}{{\mathfrak h}}\newcommand{\HH}{{\mathbb H}^2}
\newcommand{\II}{{\mathcal I}}
\renewcommand{\k}{{\mathfrak k}}\newcommand{\kk}{{\mathfrak K}}
\renewcommand{\l}{{\mathfrak l}}
%\newcommand{\ll}{{\mathfrak L}}
\newcommand{\LL}{{\mathcal L}}
\newcommand{\mm}{{\mathcal M}}
\newcommand{\n}{{\mathfrak n}}\newcommand{\N}{{\mathbb N}}\newcommand{\NN}{{\mathcal N}}
\newcommand{\oo}{{\mathcal O}}
\newcommand{\p}{{\mathfrak p}}\newcommand{\PP}{{\mathcal P}}\newcommand{\ppp}{{\mathfrak P}}
\newcommand{\QQ}{{\mathbb Q}}\newcommand{\QQQ}{{\mathcal Q}}
\newcommand{\R}{{\mathbb R}}\newcommand{\RR}{{\mathbb R}^2}\newcommand{\RRR}{{\mathcal R}}
\newcommand{\unisph}{{\mathbb S}^2}\newcommand{\SSS}{{\mathcal S}}
\newcommand{\TT}{{\mathbb T}}\newcommand{\ttt}{{\mathcal T}}
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0002
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0923
```latex
% <|ROOT: CramerRao_arxiv.tex|>

\documentclass[reqno,10pt]{amsart}
\usepackage{amsmath,amssymb}

\usepackage[dvips]{graphics}
\usepackage{epsfig}

%\addtolength{\textheight}{1.8cm} \addtolength{\voffset}{-.02cm}
%\addtolength{\textwidth}{5.8cm} \addtolength{\hoffset}{-2.9cm}
%\addtolength{\marginparwidth}{4.2cm}
%\addtolength{\textheight}{2.1cm} \addtolength{\voffset}{-2.5cm}
%Theorems etc.%
\addtolength{\textwidth}{2.2cm}\addtolength{\hoffset}{-1.1cm}
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0349
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0105
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0302
```latex
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
distribution of $\left( \mathbf{X}_{i}^{T},Y_{i},\varepsilon
_{i}\right) $. When the dimension of $\mathbf{X}$ is high, one
unavoidable issue is the ``curse of dimensionality'', which refers
to the poor convergence rate of nonparametric estimation of
general multivariate function. Much effort has been devoted to the
circumventing of this difficulty. In the words of Xia, Tong, Li
and Zhu (2002), there are essentially two approaches: function
approximation and dimension reduction. A favorite function
approximation technique is the generalized additive model
advocated by Hastie and Tibshirani (1990), see also, for example,
Mammen, Linton and Nielsen (1999), Huang and Yang (2004), Xue and
Yang (2006 a, b), Wang and Yang (2007). An attractive dimension
reduction method is the single-index model, similar to the first
step of projection pursuit regression, see Friedman and Stuetzle
(1981), Hall (1989), Huber (1985), Chen (1991). The basic appeal
of single-index model is its simplicity: the $d $-variate function
$m
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0416
```latex
{\framebox(1,1){4n-4}}
\put(7.3,1){\framebox(1,1){4n-6}}
\put(10.3,0){\framebox(1,1){4n-3}}
\put(11.3,0){\framebox(1,1){4n-1}}
\put(12.3,0){\framebox(1,1){4n}}
\put(10.3,1){\framebox(1,1){4n-2}}




% labels of the vertices:
\put(-.1,-.1){\Large $\bullet$}
%\put(-.2,-.4){$P_1$}
\put(-.1, .88){\Large $\bullet$}
\put(-.1,1.88){\Large $\bullet$}
\put( .88,-.1){\Large $\bullet$}
\put( .88, .88){\Large $\bullet$}
\put( .88,1.88){\Large $\bullet$}
\put(1.88,-.1){\Large\bf $\circ$}
\put(1.88, .88){\Large $\circ$}

\put(2.88,-.1){\Large $\bullet$}
\put(2.88, .88){\Large $\bullet$}
\put(2.88,1.88){\Large $\bullet$}
\put(3.88,-.1){\Large $\bullet$}
\put(3.88, .88){\Large $\bullet$}
\put(3.88,1.88){\Large $\bullet$}
\put(4.86,-.1){\Large\bf $\circ$}
\put(4.86, .88){\Large $\circ$}
\put(7.18,-.1){\Large $\bullet$}
\put(7.18, .88){\Large $\bullet$}
\put(7.18,1.88){\Large $\bullet$}
\put(8.18,-.1){\Large $\bullet$}
\put(8.18, .88){\Large $\bullet$}
\put(8.18,1.88){\Large $\bullet$}
\put(9.17,-.1){\Large\bf $\circ$}
\put(9.17, .86){\Large $\circ$}

\put(10.18,-.1){\Large $\bullet$}
\put(10.18, .88){\Large $\bullet$}
\put(10.18,1.88){\Large $\bullet$}
\put(11.18,-.1){\Large $\bullet$}
\put(11.18, .88){\Large $\bullet$}
\put(11.18,1.88){\Large $\bullet$}
\put(12.17,-.1){\Large\bf $\circ$}
\put(12.17, .86){\Large $\circ$}

\put(13.18, -.1){\Large $\bullet$}
\put(13.18, .88){\Large $\bullet$}

\end{picture}




<|FILE_SEP|>

% <|FILE: literatur.tex|>
\begin{thebibliography}{}
\bibitem[EG 97]{eg} C.J.\ Earle, F.P.\ Gardiner:
        {\it Teichm\"uller disks and Veech's $F$-structures.}
        American Mathematical Society. Contemporary Mathematics 201, 1997 (p.\
        165--189).
%\bibitem[Gu 01]{gu} J.~Gu\`ardia:
%  {\it Explicit geometry on a family of curves of genus 3.}
%J.~London Math.~Soc.\ (2) 64 (2001), 299-310.
\bibitem[GJ 00]{gj} E.\ Gutkin, C.\ Judge:
   {\it Affine mappings of translation surfaces.}
   Duke Mathematical Journal 103 No.\ 2, 2000 (p.\ 191--212).
%\bibitem[HeSc 05]{WMS} F.\ Herrlich, G.\ Schmith\"usen:
%{\it An extraordinary origami curve.} To appear in Math.\ Nachrichten.
\bibitem[HeSc 06]{hesh2}
F.\ Herrlich, G.\ Schmith\"usen:
{\it
On the boundary of Teichm\"uller disks in Teichm\"uller and in Schottky 
space.}
To appear in Handbook of Teichm\"uller theory.
Ed. A. Papadopoulos, European Mathematical Society, 2006.
\bibitem[H 06]{h-yokohama} 
F.\ Herrlich:
{\it A comb of origami curves in $M_3$.}
Proceedings of Symposium on Transformation Groups, Yokohama, November 2006.
\bibitem[HL 05]{hl2} P.\ Hubert, S.\ Leli\`evre: {\it
        Noncongruence subgroups in $H(2)$.}
        International Mathematics Research Notices 2005, No.1\ , 2005
        (p.\ 47--64).
\bibitem[HuSc 01]{hs} P.\ Hubert, T.\ Schmidt:
        {\it Invariants of translation surfaces.}
        Annales de l'Institut Fourier 51 No.\ 2, 2001 (p.\ 461--495).
%\bibitem[KuKo 79]{KK} Kuribayashi,\,A., Komiya,\,K.:
%  {\it On Weierstrass points and
%    automorphisms of curves of genus three.} Algebraic geometry, Proc. 
%Summer Meet., Copenh. 1978,
%    Lect. Notes Math. 732 (1979), 253-299.
\bibitem[Le 02]{li2} S.\ Leli\`evre: {\it Veech surfaces associated with rational billiards.} Preprint, 2002.
arXiv:math.GT/0205249.
\bibitem[Lo 05]{l}
P.~Lochak: {\it On arithmetic curves in the moduli space of curves.}
  J. Inst. Math. Jussieu 4, No.~3, 2005 (p.\ 443--508).
%\bibitem[M\"o 05]{M1} M.~M\"oller:
%{\it Shimura and Teichm\"uller curves.} Preprint 2005, math.AG/0501333.
\bibitem[S 04]{sh1} G.\ Schmith\"usen:
    {\it An algorithm for finding the Veech group of an origami.}
      Experimental Mathematics 13 No.\ 4, 2004 (p.\ 459--472).
\bibitem[S 05]{gabidiss} G.\ Schmith\"usen:
     {\it Veech Groups of Origamis.}
      Dissertation (PhD thesis), Karlsruhe 2005.
      Elektronisches Volltextarchiv EVA Universit\"at Karlsruhe.
     http://www.ubka.uni-karlsruhe.de/eva/
\bibitem[S 06]{sh2} Schmith\"usen,\,G.: 
{\it Examples for Veech groups of origamis.}
In: The Geometry of Riemann Surfaces and Abelian Varieties.
Contemp.\ Math.\ 397, 2006 (p.\ 193--206).
\bibitem[T 88]{th2}W.\ Thurston: {\it On the geometry and dynamics of 
diffeomorphisms of surfaces.} 
Bulletin (New Series) of the American Mathematical 
Society 19 No.\ 2, 1988 (p.\ 417--431). 
\bibitem[V 89]{ve} W.A.\ Veech:
   {\it Teichm\"uller curves in moduli space,
        Eisenstein series and an application to triangular billiards.}
    Inventiones Mathematicae 97 No.3 1989, (p.\ 553--583).
\bibitem[W 64]{wo} K.\ Wohlfahrt:
   {\it An Extension of F.\ Klein's
        Level Concept.}
    Illinois Journal of Mathematics 8, 1964 (p.\ 529--535).
\bibitem[Z 06]{z} A.\ Zorich:
  {\it Flat Surfaces}
  in collection "Frontiers in Number Theory, Physics and Geometry. Volume 1:
  On random matrices, zeta functions and dynamical systems'',
  Ed. P. Cartier, B. Julia, P. Moussa, P. Vanhove,
  Springer-Verlag, 2006 (p.\ 439--586).
\end{thebibliography}


<|FILE_SEP|>

% <|FILE: origamis.tex|>
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2259
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0112
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1070
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2362
```latex
article}
\usepackage{amsfonts}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amscd}
%\usepackage{eepic}
%\usepackage{epic}
\usepackage{color}
\usepackage{graphics}
\usepackage{graphicx}
\usepackage{epsfig}
\headsep 15mm
\headheight 10mm
\voffset -25mm
\hoffset -10mm
%\oddsidemargin 0.8cm
%\evensidemargin -0.8cm
\textheight 24cm
\textwidth 15.7cm
\openup 0.6mm
\parskip 0.5em
\begin{document}
\newtheorem{Theoreme}{Th\'eor\`eme}[section]
\newtheorem{Theorem}{Theorem}[section]
\newtheorem{Th}{Th\'eor\`eme}[section]
\newtheorem{De}[Th]{D\'efinition}
\newtheorem{Pro}[Th]{Proposition}
\newtheorem{Lemma}[Theorem]{Lemma}
\newtheorem{Proposition}[Theorem]{Proposition}
\newtheorem{Lemme}[Theoreme]{Lemme}
\newtheorem{Corollaire}[Theoreme]{Corollaire}
\newtheorem{Consequence}[Theoreme]{Cons\'equence}
\newtheorem{Remarque1}[Theoreme]{Remarque}
\newtheorem{Convention}[Theoreme]{{\sc Convention}}
\newtheorem{PP}[Theoreme]{Propri\'et\'es}
\newtheorem{Conclusion}[Theoreme]{Conclusion}
\newtheorem{Ex}[Theoreme]{Exemple}
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2471
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1613
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1696
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2402
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1272
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1764
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1625
```latex
% <|ROOT: systematic-scan.tex|>
% TO THE EDITOR
% -------------
%
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1157
```latex
ctions
% and random processes
% Type:   Preprint CRM-
% Authors: J. Harnad and  A. Yu. Orlov
% Compiler:  LaTeX
% Date:  December 14, 2006
% ArXiv:
%%%%%%%%%%%%%%% Formatting %%%%%%%%%%%%%%%%%%

\documentclass[a4paper,12pt]{article}
\usepackage{times,cite,amsmath,amsfonts,amsthm,fullpage,graphicx}
%\usepackage{youngtab}

\newcommand{\Pf}{\mathop\mathrm{Pf}\nolimits}
\newcommand{\sgn}{\mathop\mathrm{sgn}\nolimits}
\newcommand{\DP}{\mathop\mathrm{DP}\nolimits}
\newcommand{\bt}{\mathbf{t}}
\renewcommand{\l}{\langle}
\renewcommand{\r}{\rangle}
\def\Tr{\mathop{\rm Tr}\nolimits}

\theoremstyle{plain}
\newtheorem{Lemma}{Lemma}
\newtheorem{Theorem}{Theorem}

\theoremstyle{remark}
\newtheorem{Remark}{Remark}


\newtheorem{corollary}{Corollary}[section]
\newtheorem{definition}{Definition}[section]
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}{Proposition}[section]
\newtheorem{examp}{Example}[section]
\newtheorem{examps}{Examples}[section]
\newtheorem{exercise}{Exercise}[section]
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0669
```latex
l r}}
\newcommand{\bss}{{\boldsymbol s}}
\newcommand{\bst}{{\boldsymbol t}}
\newcommand{\bsu}{{\boldsymbol u}}
\newcommand{\bsv}{{\boldsymbol v}}
\newcommand{\bsw}{{\boldsymbol w}}
\newcommand{\bsx}{{\boldsymbol x}}
\newcommand{\bsy}{{\boldsymbol y}}
\newcommand{\bsz}{{\boldsymbol z}}

\newcommand{\bsA}{{\boldsymbol A}}
\newcommand{\bsB}{{\boldsymbol B}}
\newcommand{\bsC}{{\boldsymbol C}}
\newcommand{\bsD}{{\boldsymbol D}}
\newcommand{\bsE}{{\boldsymbol E}}
\newcommand{\bsF}{{\boldsymbol F}}
\newcommand{\bsG}{{\boldsymbol G}}
\newcommand{\bsH}{{\boldsymbol H}}
\newcommand{\bsI}{{\boldsymbol I}}
\newcommand{\bsJ}{{\boldsymbol J}}
\newcommand{\bsK}{{\boldsymbol K}}
\newcommand{\bsL}{{\boldsymbol L}}
\newcommand{\bsM}{{\boldsymbol M}}
\newcommand{\bsN}{{\boldsymbol N}}
\newcommand{\bsO}{{\boldsymbol O}}
\newcommand{\bsP}{{\boldsymbol P}}
\newcommand{\bsQ}{{\boldsymbol Q}}
\newcommand{\bsR}{{\boldsymbol R}}
\newcommand{\bsS}{{\boldsymbol S}}
\newcommand{\bsT}{{\boldsymbol T}}
\newcommand{\bsU}{{\boldsymbol U}}
\newcommand{\bsV}{{\boldsymbol V}}
\newcommand{\bsW}{{\boldsymbol W}}
\newcommand{\bsX}{{\boldsymbol X}}
\newcommand{\bsY}{{\boldsymbol Y}}
\newcommand{\bsZ}{{\boldsymbol Z}}

\newcommand{\bsalpha}{{\boldsymbol \alpha}}
\newcommand{\bsbeta}{{\boldsymbol \beta}}
\newcommand{\bsgamma}{{\boldsymbol \gamma}}
\newcommand{\bsdelta}{{\boldsymbol \delta}}
\newcommand{\bsepsilon}{{\boldsymbol \epsilon}}
\newcommand{\bsmu}{{\boldsymbol \mu}}
\newcommand{\bsomega}{{\boldsymbol \omega}}

% ABBREVIATION ------------------------------------------------------

\newcommand{\fig}{Fig.\;}
\newcommand{\cf}{cf.\;}
\newcommand{\eg}{e.g.\;}
\newcommand{\ie}{i.e.\;}

% MISCELLANEOUS -----------------------------------------------------

\newcommand{\id}{{\mathrm{id}}}
\newcommand{\un}[1]{\underline{#1}}
%\newcommand{\defin}{\stackrel{\text{def}}{=}}
\newcommand{\bound}{\partial}
\newcommand{\sbound}{\hat{\partial}}
\newcommand{\rel}{\,|\,}
\newcommand{\pnt}{\rightsquigarrow}
\newcommand{\pa}{_\bullet}
\newcommand{\nb}[1]{\marginpar{\tiny {#1}}}
\newcommand{\pair}[1]{\langle{#1}\rangle}
\newcommand{\0}{^{(0)}}
\newcommand{\1}{^{(1)}}
\newcommand{\con}{_{\text{con}}}
\newcommand{\ra}{\rightarrow}


% ROMAN FONTS------------------------------------------------------------

\newcommand{\slim}{{\mathrm s-}\lim}
\newcommand{\e}{{\mathrm e}}
\newcommand{\iu}{{\mathrm i}}
\renewcommand{\d}{{\mathrm d}}
\newcommand{\sys}{{\mathrm S}}
\newcommand{\res}{{\mathrm R}}
\newcommand{\Fr}{\mathrm{Fr}}
\newcommand{\Id}{\mathrm{Id}}
\renewcommand{\sp}{\mathrm{sp}}
\newcommand{\Ran}{\mathrm{Ran}}
\newcommand{\Sym}{\mathrm{Sym}}
\newcommand{\Dom}{\mathrm{Dom}}
\newcommand{\Span}{\mathrm{Span}}
\newcommand{\beq}{ \begin{equation} }
\newcommand{\eeq}{ \end{equation} }
\newcommand{\bet}{ \begin{theorem} }
\newcommand{\eet}{ \end{theorem} }
\newcommand{\w}{{\mathrm w}}
\newcommand{\rep}{\mathrm{rep}}
\newcommand{\refl} {\mathrm{Refl}}
\newcommand{\s}{{\mathrm s}}
\newcommand{\sh}{\mathrm{shift}}
\newcommand{\ren}{\mathrm{ren}}
\newcommand{\Symm}{\mathrm{Sym}}
\newcommand{\dil}{\mathrm{dil}}


 \newcounter{smallarabics}
\newenvironment{arabicenumerate}
{\begin{list}{{\normalfont\textrm{\arabic{smallarabics})}}}
  {\usecounter{smallarabics}\setlength{\itemindent}{0cm}
  \setlength{\leftmargin}{5ex}\setlength{\labelwidth}{4ex}
  \setlength{\topsep}{0.75\parsep}\setlength{\partopsep}{0ex}
   \setlength{\itemsep}{0ex}}}
{\end{list}}


\newcounter{smallroman}
\newenvironment{romanenumerate}
{\begin{list}{{\normalfont\textrm{(\roman{smallroman})}}}
  {\usecounter{smallroman}\setlength{\itemindent}{0cm}
  \setlength{\leftmargin}{5ex}\setlength{\labelwidth}{4ex}
  \setlength{\topsep}{0.75\parsep}\setlength{\partopsep}{0ex}
   \setlength{\itemsep}{0ex}}}
{\end{list}}

\newcommand{\arabicref}[1]{{\normalfont\textrm{(\ref{#1})}}}
\newcommand{\ben}{\begin{arabicenumerate}}
\newcommand{\een}{\end{arabicenumerate}}

\newcommand{\opluslimits}{\mathop{\oplus}\limits}
\newcommand{\dyn}{{\mathrm{dyn}}}
\newcommand{\st}{{\mathrm{st}}}
\newcommand{\off}{\mathrm{o}}
\newcommand{\Ker}{\mathrm{Ker}}
\newcommand{\alg}{\mathrm{al}}
\newcommand{\Pair}{\mathrm{Pair}}
\newcommand{\systeemhamiltoniaan}{{E}}
\newcommand{\systeemhameffectief}{E_{\mathrm{f}}}
\newcommand{\finiteparticlefullspace}{\caE \otimes_{\alg}
\caD_{\res}^{\mathrm{fin}}}

\newcommand{\sfock}{\Ga_{\mathrm{s}}}


%\newcommand{\wdr}{\textcolor{red} }
\newcommand{\wdr}{}

\begin{document}

%\keywords{}

%\mathclass{Primary: Secondary:}


\abbrevauthors{J. Derezi\'{n}ski and W. De Roeck}

\abbrevtitle{Reduced and Extended  Weak Coupling Limit}

\title{Reduced and Extended \\ Weak Coupling Limit}

\author{Jan Derezi\'{n}ski}
\address{ Department of Mathematical Methods in Physics \\
Warsaw University \\
 Ho\.{z}a 74, 00-682, Warszawa, Poland\\
E-mail: jan.derezinski@fuw.edu.pl}

\author{Wojciech De Roeck}
\address{ Instituut voor Theoretische Fysica, K.U.Leuven\\
 Belgium \\
E-mail: wojciech.deroeck@fys.kuleuven.be}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1174
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0286
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0991
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0495
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2242
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2376
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1943
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2216
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2152
```latex
b{K}}
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

%notazioni ricorrenti
\def\E#1#2{\left\langle #1,#2 \right\rangle}  % prodotto scalare lorentziano
\def\fut{\mathrm{I}^+}                         %futuro
\def\pass{\mathrm{I}^-}                         %passato
\def\cfut{\mathrm{J}^+}                         %futuro
\def\cpass{\mathrm{J}^-}
\def\M#1#2{\mathrm{M}(#1,\,\mathbb{#2})}               %  matrici

\def\Gl#1#2{\mathrm{Gl}(#1,\, \mathbb{#2})}            %  gruppo lineare
\def\SL#1#2{\mathrm{SL}(#1,\,\mathbb{#2})}
\def\PSL#1#2{\mathbb P\mathrm{SL}(#1,\,\mathbb{#2})}
\def\OO{\mathrm{O}}
\def\SOO{\mathrm{SO}}
\def\SOOC{\mathrm{SO}_\mathbb{C}}
\def\soo{\mathfrak{so}}
\def\sooc{\mathfrak{so}_\mathbb{C}}
\def\Aff{\mathrm{Aff}}                        % gruppo delle affinita'
\def\Hom{\mathrm{Hom}}                        % scrive Hom in formato normale
\def\ISO{\mathrm{Isom}}
\def\CONF{\mathrm{Conf}}
\def\Diffeo{\mathrm{Diffeo}}
\def\Homeo{\mathrm{Homeo}}
\def\coom{\mathrm{H}^}
%funzioni ricorrenti
\def\eps{\epsilon}                        % scrive epsilon
\def\hol{\mathrm{hol}}
\def\ad{\mathrm{ad}}                          % aggiunta
\def\Ad{\mathrm{Ad}}
\def\tr{\mathrm{tr}}                          % traccia
\def\sign{\mathrm{sign}}                      % segno
\def\im{\mathrm{Im}}                          % immagine
\def\stab{\mathrm{stab}}                      % stabilizzatore
\def\modulo{\mathrm{mod }}                    % modulo
\def\graph{\mathrm{graph}}
\def\der#1#2{\frac{\partial#2}{\partial y_#1}} %derivata parziale
\def\cder#1{\frac{\partial\,}{\partial#1}}  % campo di derivazione direzionale
\def\supp{\mathrm{supp}}
\def\d{\mathrm{d}}
\def\ch{\mathrm{ch\,}}
\def\sh{\mathrm{sh\,}}
\def\tgh{\mathrm{tgh\,}}
\def\cth{\mathrm{cth\,}}
\def\arctgh{\mathrm{arctgh\, }}
\def\grad{\mathrm{grad\, }}
\def\Sov{\overline S}
\def\Stilde {\widetilde S}
\def\Shat{\hat S}
\def\Diff{{\rm Diff}}
\def\rel{{\rm rel}}
\def\Mod{{\rm Mod}}

\title{(2+1) Einstein spacetimes of finite type} 

\author {Riccardo Benedetti and Francesco Bonsante}

%\date{}

\begin{document}
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1877
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0716
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2123
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0688
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.1584
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.0378
```latex
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
```
--------------------------------------------------------------------------------

## Paper ID: 0704.2133
```latex
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
```
--------------------------------------------------------------------------------

