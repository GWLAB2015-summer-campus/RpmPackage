# RPM Package

### 1. 구현 환경
* centOs 6.8

### 2. 파일, 디렉터리 설명
* gridwiz.spec : RPM Package 생성을 위해 사용되는 spec 파일

* gridwiz-1.0.0/ : Package로 만들 실제 파일들을 담아둔 디렉터리

  > config.txt : 프로젝트 설정 파일(basePath, DB config)

  > config : 프로젝트 설정을 셋팅하는 스크립트

  > gridwiz : 실행 파일..

* install : RPM Package 생성과 설치를 하는 스크립트, 설치할 Package의 Name, Version, Release를 입력 받음

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
* spec 파일은 Name Version Release만 수정 가능(스크립트 작동 안될수 있음).
* package디렉터리(gridwiz-1.0.0)의 이름은 spec파일 항목의 Name-Version 으로 이름지어야 함.
* sh install 에서 입력받는 Name, Version Release는 spec파일의 항목과 일치해야 함.
