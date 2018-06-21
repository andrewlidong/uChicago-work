%--------Problem Set Class v1.01-----------
%				Simion Filip
%	
%
%Invoking \maketitle will produce a title page.
%	One can use the following:
%	\student{Your Name}
%	\classname{}
%	\duedate{}
%	\instructor{}
%	\university{}
%	\term{}
%	\psdescr{Description of the problem set}
%	\psnumber{}
%
%
%There are three environments:
%
%	\begin{problem}[extra param] - automatically numbered
%	\begin{problem*}[extra param] - unnumbered, can use extra %			param for you own numbering system 
%	\begin{solution} - no extra param, has qed symbol 
%			at the end.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{pset}[2011/03/28 PSet Class by Simion Filip]


\LoadClassWithOptions{article}
\RequirePackage{graphicx,ctable,booktabs}
\RequirePackage{amssymb,amsmath,amsthm} 
\RequirePackage{fancyhdr}
\RequirePackage[left=1.2in, right=1.4in, bottom=0.7in, top=1.4in]{geometry}


%Customizing a problem and solution environment
\newtheoremstyle{problem}
{3pt}% measure of space to leave above the theorem. E.g.: 3pt
{3pt}% measure of space to leave below the theorem. E.g.: 3pt
{\itshape}% name of font to use in the body of the theorem
{}% measure of space to indent
{\bfseries}% name of head font
{}% punctuation between head and body
{ }% space after theorem head; " " = normal interword space
{\textbf{\thmname{#1}\thmnumber{ #2}\thmnote{ #3}}
}% Manually specify head


\theoremstyle{problem}
\newtheorem{problem}{Problem}
\newtheorem*{problem*}{Problem}


\newenvironment{solution}
{\noindent\textsc{Solution:} }
{\hfill \qed}

\newenvironment{solutionn}
{\noindent\textsc{Solution:} }

%-----Standard Variables in Use---------
\def\@student{\relax}
\newcommand{\student}[1]{\gdef \@student{#1}}

\def\@duedate{\relax}
\newcommand{\duedates}[1]{\gdef \@duedates{#1}}

\def\@classname{\relax}
\newcommand{\classname}[1]{\gdef \@classname{#1}}

\def\@instructor{\relax}
\newcommand{\instructor}[1]{\gdef \@instructor{#1}}

\def\@university{\relax}
\newcommand{\university}[1]{\gdef \@university{#1}}

\def\@term{\relax}
\newcommand{\term}[1]{\gdef \@term{#1}}

\def\@psdescr{\relax}
\newcommand{\psdescr}[1]{\gdef \@psdescr{#1}}

\def\@psnumber{\relax}
\newcommand{\psnumber}[1]{\gdef \@psnumber{#1}}


%Fancy-header package to modify header/page numbering 

\pagestyle{fancy}
%\addtolength{\headwidth}{\marginparsep} %these change header-rule width
%\addtolength{\headwidth}{\marginparwidth}
\headheight 15pt
\chead{} 
\lfoot{} 
\cfoot{\thepage} 
\rfoot{} 
\renewcommand{\headrulewidth}{.3pt} 
\renewcommand{\footrulewidth}{.3pt}


\renewcommand{\maketitle}
{
\lhead{\@student}
\rhead{\@term}


}