#!/usr/bin/env python3

import os

current_dir = os.getcwd()
print('Working on directory: {}'.format(current_dir))

def check_expected(directory, file_exists, file_expected):
  exists_full = os.path.join(directory, file_exists)
  expected_full = os.path.join(directory, file_expected)
  if os.path.isfile(exists_full) and not os.path.isfile(expected_full):
    print('Removing file:')
    print('- {}'.format(exists_full))
    os.remove(exists_full)

def check_dir(directory):
  check_expected(directory, 'CACHE.DONE', '../basic-deps.DONE')

  check_expected(directory, 'internal_deps.id', 'basic-deps.DONE')
  check_expected(directory, 'basic-deps.info', 'basic-deps.DONE')

  check_expected(directory, 'cache.sha1', 'CACHE.DONE')
  check_expected(directory, 'deps.info', 'CACHE.DONE')

for (dirpath, dirnames, filenames) in os.walk(current_dir):
  for x in dirnames:
    full_path = os.path.join(dirpath, x)
    check_dir(full_path)
