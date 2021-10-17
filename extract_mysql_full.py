import pymysql
import csv
import boto3
import configparser

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mysql_config","hostname")
port = parser.get("mysql_config","port")
username = parser.get("mysql_config","username")
dbname = parser.get("mysql_config","dbname")
password = parser.get("mysql_config","parser")


