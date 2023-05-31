#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:51:42 2023

@author: patrickomalley
"""
from Utilities import salaryStats, salaryBarCharts, companyLocation, raceSalaryPieChart

def main():
    salaryStats()
    salaryBarCharts()
    companyLocation()
    raceSalaryPieChart()

if __name__ == "__main__":
    main()