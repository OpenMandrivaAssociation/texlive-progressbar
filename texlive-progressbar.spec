Name:		texlive-progressbar
Version:	1.0b4
Release:	2
Summary:	Visualize shares of total amounts in the form of a (progress-)bar
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/progressbar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/progressbar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/progressbar.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to easily visualize shares of total
amounts in the form of a bar. So basically you can convert any
number between 0 and 1 to a progressbar using the command
\progressbar{<number>}. Also a lot of customizations are
possible, allowing you to create an unique progressbar on your
own. The package uses TikZ to produce its graphics.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/progressbar/progressbar.sty
%doc %{_texmfdistdir}/doc/latex/progressbar/README
%doc %{_texmfdistdir}/doc/latex/progressbar/progressbar.pdf
%doc %{_texmfdistdir}/doc/latex/progressbar/progressbar.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
