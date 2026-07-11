%global tl_name progressbar
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0b~4
Release:	%{tl_revision}.1
Summary:	Visualize shares of total amounts in the form of a (progress-)bar
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/progressbar
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/progressbar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/progressbar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to easily visualize shares of total amounts in
the form of a bar. So basically you can convert any number between 0 and
1 to a progressbar using the command \progressbar{<number>}. Also a lot
of customizations are possible, allowing you to create an unique
progressbar on your own. The package uses TikZ to produce its graphics.

