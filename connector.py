import sqlite3
import os 
from encrypt import encryptItem, decryptItem
import hashlib
import os

def createVault():
    conn = sqlite3.connect('passwordVault.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE VAULT(NAME, URL, EMAIL, USERNAME, PASSWORD)")
    cursor.execute("CREATE TABLE PM(HASHED_MP, DEVICE_SECRET)")
    conn.close()
def addEntry(masterKey, siteName, email, password, username = '', url = ''):
    conn = sqlite3.connect('passwordVault.db')
    cursor = conn.cursor()
    sqlite_insert = '''INSERT INTO VAULT (NAME, URL, EMAIL, USERNAME, PASSWORD) 
                VALUES (?, ?, ?, ?, ?);'''
    insert_tuple = (siteName, url, encryptItem(masterKey, email), encryptItem(masterKey,username), encryptItem(masterKey,password))
    cursor.execute(sqlite_insert, insert_tuple)
    conn.commit()
    conn.close()
def createAuth(masterPW):
    deviceSecret = os.urandom(16)
    hashedMP = hashlib.sha256(masterPW.encode()).hexdigest()
    conn = sqlite3.connect('passwordVault.db')
    cursor = conn.cursor()
    sqlite_insert = '''INSERT INTO PM (HASHED_MP, DEVICE_SECRET) 
                VALUES (?, ?);'''
    insert_tuple = (hashedMP, deviceSecret)
    cursor.execute(sqlite_insert, insert_tuple)
    conn.commit()
    conn.close()
def getAllEntries(masterKey):
    conn = sqlite3.connect('passwordVault.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VAULT")
    result = []
    for login in cursor:
        result.append(list(login))
    for login in result:
        login[2] = decryptItem(masterKey, login[2])
        login.insert(3, '{hidden}')
        login.insert(3, '{hidden}')
    return result
def burnAll():
    os.remove('passwordVault.db')

def getDeviceSecret():
    conn = sqlite3.connect('passwordVault.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DEVICE_SECRET FROM PM")
    for row in cursor:
        return row[0]

def getHashedPW():
    conn = sqlite3.connect('passwordVault.db')
    cursor = conn.cursor()
    cursor.execute("SELECT HASHED_MP FROM PM")
    for row in cursor:
        return row[0]

def newOrOld():
    conn = sqlite3.connect('passwordVault.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='PM';")
    results = cursor.fetchall()
    return results

def deleteEntry(entryName):
    conn = sqlite3.connect('passwordVault.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM VAULT WHERE NAME = (?)", (entryName,))
    conn.commit()
    conn.close()