# revision 20061
# category Package
# catalog-ctan /macros/latex/contrib/progressbar/
# catalog-date 2010-10-11 16:49:40 +0200
# catalog-license lppl
# catalog-version v1.0b
Name:		texlive-progressbar
Version:	v1.0b
Release:	1
Summary:	Visualize shares of total amounts in the form of a (progress-)bar
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/progressbar/
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/progressbar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/progressbar.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package allows you to easily visualize shares of total
amounts in the form of a bar. So basically you can convert any
number between 0 and 1 to a progressbar using the command
\progressbar{<number>}. Also a lot of customizations are
possible, allowing you to create an unique progressbar on your
own.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/progressbar/progressbar.sty
%doc %{_texmfdistdir}/doc/latex/progressbar/README
%doc %{_texmfdistdir}/doc/latex/progressbar/progressbar.pdf
%doc %{_texmfdistdir}/doc/latex/progressbar/progressbar.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
