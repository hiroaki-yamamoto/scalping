#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Scalping notification app."""

import click
import yaml


def calc_price_to_sell(price, fee:float):
    """Calculate the fee to sell."""
    fee_perc = fee / 100
    return (1 + fee_perc) / (1 - fee_perc) * price


@click.command()
@click.argument("price", type=float)
def main(price):
    """Mein entrypoint."""
    config = None
    with open("config.yml") as f_in:
        config = yaml.load(f_in, yaml.loader.SafeLoader)
    print(calc_price_to_sell(price, config["fee"]))


if __name__ == "__main__":
    main()
