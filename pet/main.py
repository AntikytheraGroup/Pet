#! /usr/bin/env python


import argparse
import init, commit, branch, checkout, log


def main():

    parser = argparse.ArgumentParser(prog='pet')
    sub_parser = parser.add_subparsers(description='')

    init_parser = sub_parser.add_parser('init', description='Initialize a Pet architecture.')
    init_parser.set_defaults(func=init)
    init_parser.add_argument('--filename', '-f', type=str, default='temp', 
         help='Optional parameter for an existing architecture file.')

    commit_parser = sub_parser.add_parser('commit', description='Manage architecture commits.')
    commit_parser.set_defaults(func=commit)
    commit_parser.add_argument('--message', '-m', type=str, required=True, 
         help='Message describing training conditions.')

    branch_parser = sub_parser.add_parser('branch', description='Manage architecture branches.')
    branch_parser.set_defaults(func=branch)
    branch_parser.add_argument('--delete', '-d', action='store_true', help='Delete a branch')
    branch_parser.add_argument('--create', '-c', action='store_true', help='Create a branch')

    checkout_parser = sub_parser.add_parser('checkout', description='Change architecture branches.')
    checkout_parser.set_defaults(func=checkout)

    log_parser = sub_parser.add_parser('log', description='Display change log.')
    log_parser.set_defaults(func=log)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__': main()
