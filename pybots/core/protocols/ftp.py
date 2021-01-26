# -*- coding: UTF-8 -*-
"""Bot client for FTP sessions.

This bot relies on ftplib to manage FTP (or FTP_TLS) sessions.

"""
import ftplib

from ..ssocket import SocketBot


__all__ = __features__ = ["FTPBot", "FTPSBot"]


class __FTP(ftplib.FTP):
    def __init__(self, parent, timeout=ftplib._GLOBAL_DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.sock = parent.socket


class FTPBot(SocketBot):
    """
    FTP session bot.

    :param host:     hostname or IP address
    :param port:     port number
    :param disp:     display all exchanged messages or not
    """
    def __init__(self, host, port=21, username="anonymous", password="", *args, **kwargs):
        super(FTPBot, self).__init__(*args, **kwargs)
        out = self.read_until("\r\n")
        code, msg = out.split(" ", 1)
        self.__connected = False
        if int(code) != 220:
            self.logger.error("Could not connect to FTP server")
        else:
            self.login(username, password)
    
    def _sendcmd(self, cmd, arg=None):
        """
        Send an FTP command to the remote server.
        
        :param cmd: FTP command, case-insensitive
        :param arg: optional argument for the command
        """
        out = self.send_receive("{} {}".format(cmd.upper(), arg or "", "\r\n").rstrip()).strip()
        if out[3] == "-":
            
        code, msg = out.split(" ", 1)
        return int(code), msg

    def login(self, username="anonymous", password="", accounting=""):
        """
        Default preamble to be processed during a session.
        """
        if self.__connected:
            
        if username == "anonymous" and password in ["", "-"]:
            password = "anonymous@"
        code, _ = self._sendcmd("USER", username)
        if 300 <= code < 400:
            code, _ = self._sendcmd("PASS", password)
            self._sendcmd("ACCT", accounting)
            if 300 <= code < 400:
                self.__connected = True
    

