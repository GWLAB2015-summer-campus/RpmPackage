# RPM Package

### 1. 구현 환경
* centOs 6.8
* ubuntu 16.04
* centos, ubuntu 에서 패키지 생성 및 설치
* rpmbuild, lsb_release 필요 

### 2. 파일, 디렉터리 설명
* gridwiz.spec : RPM Package 생성을 위해 사용되는 spec 파일

* gridwiz-1.0.0/ : Package로 만들 실제 파일들을 담아둔 디렉터리

  > config.txt : 프로젝트 설정 파일(basePath, DB config)

  > config : 프로젝트 설정을 셋팅하는 스크립트

  > gridwiz : 실행 파일..

* install : RPM Package 생성과 설치를 하는 스크립트, 설치할 Package의 Name, Version, Release를 입력 받음

* install_debian : debian 계열에서 설치하기 위한 스크립트 install에서 판단하여 실행

* unistall : RPM Package 삭제 스크립트

### 3. 사용법 및 명령어

* sh install : 패키지 설치

* sh uninstall : 패키지 삭제

* config : config.txt 설정 변경 (/usr/local/bin 에 있어 어느 경로에서든 사용가능)

* RpmPackage/ 에서 install과 uninstall이 작동됨. 설치 완료후에 config를 이용하여 설정

### 4. Package 설치 경로
```
config : /usr/local/bin/
config.txt : /usr/local/gridwiz/config/
gridwiz : /usr/local/gridwiz/bin/
```
### 5. 주의사항
* spec 파일은 Name Version Release만 수정 가능(수정시 스크립트 작동 안될 수 있음).
* package디렉터리(gridwiz-1.0.0)의 이름은 spec파일 항목의 Name-Version 으로 이름지어야 함.
* sh install 에서 입력받는 Name, Version Release는 spec파일의 항목과 일치해야 함.
* spec파일 Name(gridwiz) 변경 시 install, uninstall 에서 패키지 설치 검사 로직, default 변수 변경 해야함. 
* permission 오류가 뜬다면 sudo sh install , sudo sh uninstall
* install_debian 을 독립적으로 실행시키면 안됨

```
path=$(rpm -qa gridwiz)

defaultName=gridwiz
```

### 6. 새로운 Package 생성 및 설치 구조 변경
gridwiz.spec 에서 새로운 Package 이름과 버전 릴리스 입력, 설치 구조 변경

gridwiz-1.0.0 디렉터리를 새로운 Package 이름과 버전으로 변경

#### gridwiz.spec

```
Name: gridwiz

Version: 1.0.0

Release: 1

mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/gridwiz
mkdir -p $RPM_BUILD_ROOT/usr/local/gridwiz/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/gridwiz/config

cp gridwiz $RPM_BUILD_ROOT/usr/local/gridwiz/bin
cp config $RPM_BUILD_ROOT/usr/local/bin
cp config.txt $RPM_BUILD_ROOT/usr/local/gridwiz/config

%attr(0755,root,root)/usr/local/bin/config
%attr(0755,root,root) /usr/local/gridwiz/config/config.txt
%attr(0755,root,root)/usr/local/gridwiz/bin/gridwiz


```
mkdir,cp 부분은 $RPM_BUILD_ROOT/ 뒤 부터 실제 저장될 경로로 지정

cp는 package의 각 파일들이 어느 위치에 저장 될지 결정

%attr 부분은 cp 부분과 경로가 동일해야함 ex)config 는 /usr/local/bin/config package의 실제 파일들을 옮기는 과정

#### install

```
mkdir -p /usr/local/gridwiz
mkdir -p /usr/local/gridwiz/bin
mkdir -p /usr/local/gridwiz/log
mkdir -p /usr/local/gridwiz/config
```
spec 파일 에서 변경된 경로와 동일하게 변경

#### uninstall

```
rm -rf /usr/local/bin/config
rm -rf /usr/local/gridwiz
```
spec 파일 에서 변경된 경로와 동일하게 변경

Q) ghjf1278@naver.com 
