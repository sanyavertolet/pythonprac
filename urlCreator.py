#!/usr/bin/env python3

import re
import os
import sys
import argparse
import subprocess
from io import StringIO
from checkerNN import main as tester

########################################################################
FIND_TESTS = 3
OTHER_REPOS_DIR = './others_tests'
ALLOWED_PROG_NAMES = { 'task1.py', 'task2.py', 'task3.py', 'task4.py', 'prog.py' }
IGNORED_DIRS = [ '20210909', '20210916' ]
REPOS = [
  {
    "owner": "Дарья Озерова",
    "group": "321",
    "url": "https://github.com/OzerovaDaria/pythonprac"
  },
  {
    "owner": "Павел Шибаев",
    "group": "321",
    "url": "https://git.cs.msu.ru/s02190248/pythonprac"
  },
  {
    "owner": "Вениамин Арефьев",
    "group": "321",
    "url": "https://github.com/Veniamin-Arefev/pythonprac-2021"
  },
  {
    "owner": "Иван Ушаков",
    "group": "321",
    "url": "https://git.cs.msu.ru/s02190226/pythonprac"
  },
  {
    "owner": "Дмитрий Хасанов",
    "group": "321",
    "url": "https://git.cs.msu.ru/s02190234/pythonprac2021"
  },
  {
    "owner": "Илья Савицкий",
    "group": "321",
    "url": "https://github.com/ipsavitsky/pythonprac"
  },
  {
    "owner": "Александр Колесников",
    "group": "321",
    "url": "https://git.cs.msu.ru/s02190290/python-prac-2021"
  },
  {
    "owner": "Александр Фролов",
    "group": "321",
    "url": "https://github.com/sanyavertolet/pythonprac"
  },
  {
    "owner": "Егор Князев",
    "group": "321",
    "url": "https://github.com/KH9IZ/PythonPrac"
  },
  {
    "owner": "Ривзан Зайдуллин",
    "group": "321",
    "url": "https://git.cs.msu.ru/s02190101/pythonprac-2021"
  },
  {
    "owner": "Юрий Лебединский",
    "group": "321",
    "url": "https://git.cs.msu.ru/s02190141/pythonprac-2021"
  },
  {
    "owner": "Илья Федоренко",
    "group": "321",
    "url": "https://github.com/FluFFka/python-prac"
  },
  {
    "owner": "Дмитрий Стамплевский",
    "group": "321",
    "url": "https://github.com/stamplevskiyd/pythonprac-2021"
  },
  {
    "owner": "Геннадий Шутков",
    "group": "321",
    "url": "https://github.com/gen-gematogen/pythonprac"
  },
  {
    "owner": "Максим Порывай",
    "group": "321",
    "url": "https://git.cs.msu.ru/s90190054/pythonprac-2021"
  },
  {
    "owner": "Арий Оконишников",
    "group": "321",
    "url": "https://github.com/Uberariy/pythonprac"
  },
  {
    "owner": "Юлия Задорожная",
    "group": "321",
    "url": "https://git.cs.msu.ru/s02190029/prakpython"
  },
  {
    "owner": "Владислав Рубцов",
    "group": "321",
    "url": "https://git.cs.msu.ru/s02190700/pythonprac"
  },
  {
    "owner": "Дарья Скворцова",
    "group": "321",
    "url": "https://git.cs.msu.ru/s02180534/pythonprac2021"
  },
  {
    "owner": "Виктор Панферов",
    "group": "321",
    "url": "https://git.cs.msu.ru/s02190692/python-prac"
  }
]
########################################################################

class Logger:
    def __init__(self):
        self.debugging = False
        self.colors = True
        self.disabled = False

    def info(self, *args):
        if not self.disabled:
            if self.colors: print('[\033[35minfo\033[0m]     ', *args)
            else: print('[info]     ', *args)

    def warning(self, *args):
        if not self.disabled:
            if self.colors: print('[\033[93mwarning\033[0m]  ', *args)
            else: print('[warning]  ', *args)

    def debug(self, *args):
        if self.debugging and not self.disabled:
            if self.colors: print('[\033[96mdebug\033[0m] ', *args)
            else: print('[debug] ', *args)

    def error(self, *args):
        if self.colors: print('[\033[31mERROR\033[0m]    ', *args)
        else: print('[ERROR]    ', *args)

    def success(self, *args):
        if self.colors: print('[\033[32msuccess\033[0m] ', *args)
        else: print('[success] ', *args)

    def abort(self, *args, exitCode=1):
        if self.colors: print('[\033[91mCRITICAL\033[0m] ', *args)
        else: print('[CRITICAL] ', *args)
        exit(exitCode)

    def debugOn(self): self.debugging = True
    def colorsOff(self): self.colors = False
    def disable(self): self.disabled = True
log = Logger()

########################################################################

argParser = argparse.ArgumentParser()
argParser.add_argument('--alloweval', action='store_true',
        help='Dosen\'t skip tasks were eval is used')
argParser.add_argument('-o', '--only', default='',
        help='Find for only theese dirs')
argParser.add_argument('-e', '--exclude', default='',
        help='Exclude folders wrong checking')
argParser.add_argument('--debug', action='store_true',
        help='Print debug output')
argParser.add_argument('-su', '--skipupdate', action='store_true',
        help='Print debug output')
argParser.add_argument('-f', '--force', action='store_true',
        help='Forcefully update URLS file')
argParser.add_argument('repo', default='.', type=str,
        help='Path to repository for test')
argParser.add_argument('me', type=str,
        help='Your own name')

########################################################################

args = argParser.parse_args()
args.exclude = [ *map(str.strip, args.exclude.split(',')) ]
args.only = [ *filter(len, map(str.strip, args.only.split(','))) ]
ownrepo = args.repo
basedir = os.getcwd()

#######################

if not os.path.isdir(ownrepo):
    log.critical('Path to own repo is not valid')

if args.debug: log.debugOn()
if not sys.stdout.isatty(): log.colorsOff()

log.debug(args)
log.debug(args.only, len(args.only))

#######################
def findRepoByName(name):
    regex = f'(?:{"|".join(name.split())})'

    choosen = None
    bestMatch = ''
    for repo in REPOS:
        match = ' '.join(re.findall(regex, repo['owner'], flags=re.I))
        if len(match) == 0: continue
        if len(bestMatch) < len(match):
            choosen = repo
            bestMatch = match
        elif len(bestMatch) == len(match):
            log.warning(f'Same owner name for {name} ({repo["owner"]}), using {choosen["owner"]}')
    return choosen

me = findRepoByName(args.me)
if me == None:
    log.critical('Your name "{args.me}" wasnt found in repos')

#######################

if os.path.exists(OTHER_REPOS_DIR) and not os.path.isdir(OTHER_REPOS_DIR):
    log.abort(f'Unable to open {OTHER_REPOS_DIR}: file with this name already exists')
else:
    log.info('Updating REPOS storage')

    uptodate = True

    for repo in REPOS:
        repo['dir'] = os.path.join(basedir, OTHER_REPOS_DIR, repo['url'].split("/")[3])
        log.debug(repo['dir'], os.path.exists(repo['dir']))
        if not os.path.exists(repo['dir']):
            uptodate = False
            subprocess.run(['git', 'clone', repo['url'], repo['dir']])
        elif not args.skipupdate:
            uptodate = False
            os.chdir(repo['dir'])
            subprocess.run(['git', 'pull', 'origin'])

    os.chdir(basedir)
    if uptodate: log.info('Repos are up to date')

#######################

stat = {
    'ok': 0,
    'fail': 0,
    'skipped': 0,
}
results = dict()

dirs = sorted([ *filter(lambda x: re.match('^2021\d+$', x), os.listdir(ownrepo)) ])
for dir in dirs:
    if dir in IGNORED_DIRS: continue
    if dir in args.exclude: continue
    if len(args.only) and dir not in args.only: continue

    condir = os.path.join(ownrepo, dir)
    tasks = sorted([ *filter(lambda x: re.match('^\d+$', x), os.listdir(condir)) ])
    log.debug('condir - ', condir, ':', tasks)

    for task in tasks:
        taskFullName = f'{dir}/{task}'
        taskdir = os.path.join(condir, task)

        if taskFullName in args.exclude: continue
        if os.path.exists(os.path.join(taskdir, 'URLS')) and not args.force:
            stat['ok'] += 1
            continue

        pyfiles = { *filter(lambda x: re.match('.*\.py$', x), os.listdir(taskdir)) }
        log.debug('taskdi - ', taskdir, ':', pyfiles)

        taskfile = [ *(pyfiles & ALLOWED_PROG_NAMES) ]
        if len(taskfile) == 0:
            log.error(f'No python program found for {taskFullName}, skipping...')
            stat['skipped'] += 1
            results[taskFullName] = None
            continue
        elif len(taskfile) > 1:
            log.warning(f'Too many python programs to choose from: {taskfile}, using {taskfile[0]}')
        taskfile = os.path.join(ownrepo, dir, task, taskfile[0])

        if not args.alloweval:
            with open(taskfile, 'r') as f:
                if f.read().find('eval') != -1:
                    stat['skipped'] += 1
                    results[taskFullName] = None
                    log.warning('Program uses eval, skipping...')
                    continue

        found = 0
        testList = []
        for repo in REPOS:
            if repo["owner"] == me["owner"]:
                log.debug(f'Skipping own repo: {repo["owner"]}')
                continue

            testsdir = os.path.join(repo['dir'], dir, task, 'tests')
            testname = ': '.join([repo['owner'], os.path.join(dir, task)])
            log.debug('testdir - ', testsdir)

            if not os.path.exists(testsdir):
                log.debug(f'No tests for {taskFullName} give by {repo["owner"]}')
            else:
                oldstdout = sys.stdout
                sys.stdout = tesout = StringIO()
                try:
                    res = tester(taskfile, testsdir)
                except Exception as e:
                    sys.stdout = oldstdout
                    log.debug('Tester crashed')
                    log.debug('crash report')
                    log.debug(e)
                    continue
                else:
                    sys.stdout = oldstdout
                    log.debug(tesout.getvalue())

                if res == 0:
                    testList.append(repo)
                    found += 1
                    log.info(f'{taskFullName} matched tests of {repo["owner"]}: {found}/{FIND_TESTS}')
                    if found == FIND_TESTS:
                        break

        if found != FIND_TESTS:
            stat['fail'] += 1
            log.warning(f'For task {taskFullName} wasnt found enough tests: {found}/{FIND_TESTS}')
            results[taskFullName] = None
        else:
            stat['ok'] += 1
            log.success(f'For task {taskFullName} all {FIND_TESTS} were found')
            results[taskFullName] = { 'dir': taskdir, 'repos': testList }

log.info('Writing url files...')
for task, res in results.items():
    if res == None: continue

    urlfile = os.path.join(res['dir'], 'URLS')

    createUrl = lambda x: f'{x["url"]}/tree/main/{task}/tests'
    joinUrls = lambda repos: '\n'.join(map(createUrl, repos))
    joined = joinUrls(res['repos'])

    log.debug(f'Writing urls for {task} on {res["dir"]} in {urlfile}')
    log.debug(joined)

    with open(urlfile, 'w') as f: f.write(joined)


print('============ RESULTS ============')
print('ok:      ', stat['ok'])
print('fail:    ', stat['fail'])
print('skipped: ', stat['skipped'])

print('Falied tasks:')
for task, res in results.items():
    if res == None:
        print(task)
