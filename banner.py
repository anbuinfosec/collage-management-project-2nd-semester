import os
from datetime import datetime
import pytz
from color import yellow, green, reset

banner = f"""{yellow}╔═════════════════════════════════════════════════╗
{yellow}║{reset}      {green}BARISAL POLYTECHNIC INSTITUTE (BPI){reset}        {yellow}║{reset}
{yellow}║{reset}    PROJECT: {green}COLLEGE MANAGEMENT SYSTEM (V1){reset}      {yellow}║{reset}
{yellow}║{reset}            AUTHOR: {green}MOHAMMAD ALAMIN{reset}              {yellow}║{reset}
{yellow}║{reset}      DEPARTMENT: {green}2CST{reset}      ROLL: {green}840749{reset}         {yellow}║{reset}
{yellow}║{reset}      SHIFT: {green}MORNING{reset}        SESSION: {green}23-24{reset}       {yellow}║{reset}
{yellow}║{reset}          CONTACT: {green}anbuinfosec.xyz{reset}               {yellow}║{reset}
{yellow}║{reset}       TIME: %s  {yellow}║{reset}
{yellow}╚═════════════════════════════════════════════════╝{reset}"""

def show_banner():
    dhaka_tz = pytz.timezone('Asia/Dhaka')
    current_time = datetime.now(dhaka_tz).strftime("%A, %Y-%m-%d, %I:%M:%S %p")
    formatted_banner = banner % current_time
    os.system("clear")
    print(formatted_banner)