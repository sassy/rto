rto
====
Open redmine ticket of myself to browser.  

## Description

If your project use Redmine, you should use this command line tool.
This command open your redmine issue in the browser.

You will make tasks clear, by this tool.

## Requirement

* python 3.x

### support platform

* Mac OS X
* Windows

## Usage

```
$ rto
```

### option

```
-h, --help     show this help message and exit
-a ACTION      open is opening issue url in browser, list is printing  commandline.default is open
-et            open issue of over due time
-p PROJECT_ID  open issue of directed project.
```

## Install

```
$ pip install rto
```
or

```
$ pip install git+https://github.com/sassy/rto.git
```

You must set environment variables, REDMINE_URL and REDMINE_API_KEY.

* REDMINE_URL : redmine url of your project.
* REDMINE_API_KEY : the key to use Redmine REST API.

for example:

```
export REDMINE_URL="REDMINE URL"
export REDMINE_API_KEY="API KEY"
```

## Contribution

Wellcome Pull Request.

1. Fork it ( http://github.com//rbdock/fork )
+ Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## LICENCE

[MIT](https://github.com/sassy/rto/blob/master/LICENSE)
