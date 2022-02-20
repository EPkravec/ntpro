#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import datetime
import sys
import argparse

data = {}
deposit_dict = {}
withdraw_dict = {}
show_bank_statement_dict = {}


def createParser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    deposit_parser = subparsers.add_parser('deposit')
    deposit_parser.add_argument('--client', nargs='+', default='Имя отсутсвует')
    deposit_parser.add_argument('--amount', type=int, default=1)
    deposit_parser.add_argument('--description', nargs='+', default='Описание отсутсвует')

    withdraw_parser = subparsers.add_parser('withdraw')
    withdraw_parser.add_argument('--client', nargs='+', default='Имя отсутсвует')
    withdraw_parser.add_argument('--amount', type=int, default=1)
    withdraw_parser.add_argument('--description', nargs='+', default='Описание отсутсвует')

    show_bank_statement_parser = subparsers.add_parser('show_bank_statement')
    show_bank_statement_parser.add_argument('--client', nargs='+', default='Имя отсутсвует')
    show_bank_statement_parser.add_argument('--since', nargs='+', default='2021-01-01 00:00:00')
    show_bank_statement_parser.add_argument('--till', nargs='+', default='2021-02-01 00:00:00')

    return parser


def run_deposit(namespace):
    """
    Выполнение команды hello
    """
    global data, deposit_dict
    data['deposit'] = []
    deposit_dict['client'] = namespace.client
    deposit_dict['amount'] = namespace.amount
    deposit_dict['description'] = namespace.description
    deposit_dict['datatime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['deposit'].append(deposit_dict)
    return

def run_withdraw(namespace):
    """
    Выполнение команды goodbye
    """
    global data, withdraw_dict
    data['withdraw'] = []
    withdraw_dict['client'] = namespace.client
    withdraw_dict['amount'] = namespace.amount
    withdraw_dict['description'] = namespace.description
    withdraw_dict['datatime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['withdraw'].append(withdraw_dict)
    return

def run_show_bank_statement(namespace):
    """
    Выполнение команды hello
    """
    global data, show_bank_statement_dict
    data['show_bank_statement'] = []
    show_bank_statement_dict['client'] = namespace.client
    show_bank_statement_dict['since'] = namespace.since
    show_bank_statement_dict['till'] = namespace.till
    show_bank_statement_dict['datatime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['show_bank_statement'].append(show_bank_statement_dict)


if __name__ == '__main__':

    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.command == "deposit":
        run_deposit(namespace)
    elif namespace.command == "withdraw":
        run_withdraw(namespace)
    elif namespace.command == "show_bank_statement":
        run_show_bank_statement(namespace)
    else:
        print("Что-то пошло не так...")
print(data)
