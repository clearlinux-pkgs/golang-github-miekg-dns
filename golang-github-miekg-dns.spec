#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-miekg-dns
Version  : c9d1302d540edfb97d9ecbfe90b4fb515088630b
Release  : 1
URL      : https://github.com/miekg/dns/archive/c9d1302d540edfb97d9ecbfe90b4fb515088630b.tar.gz
Source0  : https://github.com/miekg/dns/archive/c9d1302d540edfb97d9ecbfe90b4fb515088630b.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : go

%description
[![Build Status](https://travis-ci.org/miekg/dns.svg?branch=master)](https://travis-ci.org/miekg/dns)

%prep
%setup -q -n dns-c9d1302d540edfb97d9ecbfe90b4fb515088630b

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/miekg/dns"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done


%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/miekg/dns/client.go
/usr/lib/golang/src/github.com/miekg/dns/client_test.go
/usr/lib/golang/src/github.com/miekg/dns/clientconfig.go
/usr/lib/golang/src/github.com/miekg/dns/clientconfig_test.go
/usr/lib/golang/src/github.com/miekg/dns/defaults.go
/usr/lib/golang/src/github.com/miekg/dns/dns.go
/usr/lib/golang/src/github.com/miekg/dns/dns_test.go
/usr/lib/golang/src/github.com/miekg/dns/dnssec.go
/usr/lib/golang/src/github.com/miekg/dns/dnssec_keygen.go
/usr/lib/golang/src/github.com/miekg/dns/dnssec_keyscan.go
/usr/lib/golang/src/github.com/miekg/dns/dnssec_privkey.go
/usr/lib/golang/src/github.com/miekg/dns/dnssec_test.go
/usr/lib/golang/src/github.com/miekg/dns/dnsutil/util.go
/usr/lib/golang/src/github.com/miekg/dns/dnsutil/util_test.go
/usr/lib/golang/src/github.com/miekg/dns/doc.go
/usr/lib/golang/src/github.com/miekg/dns/dyn_test.go
/usr/lib/golang/src/github.com/miekg/dns/edns.go
/usr/lib/golang/src/github.com/miekg/dns/edns_test.go
/usr/lib/golang/src/github.com/miekg/dns/example_test.go
/usr/lib/golang/src/github.com/miekg/dns/format.go
/usr/lib/golang/src/github.com/miekg/dns/fuzz_test.go
/usr/lib/golang/src/github.com/miekg/dns/idn/code_points.go
/usr/lib/golang/src/github.com/miekg/dns/idn/example_test.go
/usr/lib/golang/src/github.com/miekg/dns/idn/punycode.go
/usr/lib/golang/src/github.com/miekg/dns/idn/punycode_test.go
/usr/lib/golang/src/github.com/miekg/dns/issue_test.go
/usr/lib/golang/src/github.com/miekg/dns/labels.go
/usr/lib/golang/src/github.com/miekg/dns/labels_test.go
/usr/lib/golang/src/github.com/miekg/dns/msg.go
/usr/lib/golang/src/github.com/miekg/dns/nsecx.go
/usr/lib/golang/src/github.com/miekg/dns/nsecx_test.go
/usr/lib/golang/src/github.com/miekg/dns/parse_test.go
/usr/lib/golang/src/github.com/miekg/dns/privaterr.go
/usr/lib/golang/src/github.com/miekg/dns/privaterr_test.go
/usr/lib/golang/src/github.com/miekg/dns/rawmsg.go
/usr/lib/golang/src/github.com/miekg/dns/remote_test.go
/usr/lib/golang/src/github.com/miekg/dns/sanitize.go
/usr/lib/golang/src/github.com/miekg/dns/sanitize_test.go
/usr/lib/golang/src/github.com/miekg/dns/scanner.go
/usr/lib/golang/src/github.com/miekg/dns/server.go
/usr/lib/golang/src/github.com/miekg/dns/server_test.go
/usr/lib/golang/src/github.com/miekg/dns/sig0.go
/usr/lib/golang/src/github.com/miekg/dns/sig0_test.go
/usr/lib/golang/src/github.com/miekg/dns/singleinflight.go
/usr/lib/golang/src/github.com/miekg/dns/tlsa.go
/usr/lib/golang/src/github.com/miekg/dns/tsig.go
/usr/lib/golang/src/github.com/miekg/dns/tsig_test.go
/usr/lib/golang/src/github.com/miekg/dns/types.go
/usr/lib/golang/src/github.com/miekg/dns/types_generate.go
/usr/lib/golang/src/github.com/miekg/dns/types_test.go
/usr/lib/golang/src/github.com/miekg/dns/udp.go
/usr/lib/golang/src/github.com/miekg/dns/udp_linux.go
/usr/lib/golang/src/github.com/miekg/dns/udp_other.go
/usr/lib/golang/src/github.com/miekg/dns/udp_plan9.go
/usr/lib/golang/src/github.com/miekg/dns/udp_windows.go
/usr/lib/golang/src/github.com/miekg/dns/update.go
/usr/lib/golang/src/github.com/miekg/dns/update_test.go
/usr/lib/golang/src/github.com/miekg/dns/xfr.go
/usr/lib/golang/src/github.com/miekg/dns/xfr_test.go
/usr/lib/golang/src/github.com/miekg/dns/zgenerate.go
/usr/lib/golang/src/github.com/miekg/dns/zscan.go
/usr/lib/golang/src/github.com/miekg/dns/zscan_rr.go
/usr/lib/golang/src/github.com/miekg/dns/ztypes.go
