#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import random
import sys

# from inky import InkyWHAT

from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold
from font_fredoka_one import FredokaOne

# import argparse
# from PIL import Image, ImageFont, ImageDraw
from inky.auto import auto
# from font_source_sans_pro import SourceSansProSemibold
# from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
import time

class InkyScreen(object):

    def __init__(self):
        self.scale_size = 1.0
        self.padding = 5
        self.font_size = 16
        
        
            

    def message(self, message, bg): 
        scale_size = 1.0
        padding = 1
                
        numchars = self.count_chars(message)
        font_size = self.get_font_size(numchars)
        
        # print(message)
        # print(numchars)
        # print(font_size)
        
        try:
            inky_display = auto(ask_user=True, verbose=True)
        except TypeError:
            raise TypeError("You need to update the Inky library to >= v1.1.0")
        
        try:
            inky_display.set_border(inky_display.RED)
            # inky_display.set_border(inky_display.WHITE)
        except NotImplementedError:
            pass
        
        # parts = message.split('|')
        # inky_display.set_rotation(180)

        # bold_font = ImageFont.truetype(SourceSansProSemibold, int(font_size * scale_size))
        
        bold_font = ImageFont.truetype(FredokaOne, int(font_size * scale_size))
        
        bgcolour = inky_display.WHITE            
        img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)
        inky_display.set_border(bgcolour)
        
        for x in range(inky_display.WIDTH):
            for y in range(inky_display.HEIGHT):
                img.putpixel((x, y), bgcolour)
              
        w = inky_display.WIDTH
        h = inky_display.HEIGHT  
        
        max_width = w - padding
        max_height = h - padding - bold_font.getsize("ABCD ")[1] 
        
        reflowed = self.reflow_quote(message, max_width, bold_font)
        p_w, p_h = bold_font.getsize(reflowed)  # Width and height of quote
        p_h = p_h * (reflowed.count("\n") + 1)   # Multiply through by number of lines
            
        # print(reflowed.count("\n") + 1)
            
        quote_x = (w - max_width) / 2
        quote_y = ((h - max_height) + (max_height - p_h)) / 2
        
        quote_y = quote_y - 2
           
        # needed this when going above 100 font size
        if font_size > 90:
            quote_y = quote_y - 12
                
        draw.multiline_text((quote_x, quote_y), reflowed, fill=inky_display.BLACK, font=bold_font, align="left")
        
        # print(reflowed + "\n")
                
        inky_display.set_image(img)
        inky_display.show()
        
        print(message + "\n")



    def down_alert(self, message): 
        parts = message.split('|')
        
        scale_size = 1.0
        padding = 1
        
        mes = parts[0].rstrip() + " IS DOWN!"
        mes = mes.lower()
        
        # print(mes)
        
        numchars = self.count_chars(mes)
        font_size = self.get_font_size(numchars)
        
        try:
            inky_display = auto(ask_user=True, verbose=True)
        except TypeError:
            raise TypeError("You need to update the Inky library to >= v1.1.0")
        
        try:
            inky_display.set_border(inky_display.RED)
        except NotImplementedError:
            pass
            
        bold_font = ImageFont.truetype(SourceSansProSemibold, int(font_size * scale_size))
        
        w = inky_display.WIDTH
        h = inky_display.HEIGHT  
        
        bgcolour = inky_display.RED            
        
        img = Image.new("P", (w, h))
        draw = ImageDraw.Draw(img)
        
        inky_display.set_border(bgcolour)
        
        for x in range(w):
            for y in range(h):
                img.putpixel((x, y), bgcolour)
              
        max_width = w - padding
        max_height = h - padding - bold_font.getsize("ABCD ")[1] 
        
        reflowed = self.reflow_quote(mes, max_width, bold_font)
        
        p_w, p_h = bold_font.getsize(reflowed)  # Width and height of quote
        p_h = p_h * (reflowed.count("\n") + 1)   # Multiply through by number of lines
                        
        quote_x = (w - max_width) / 2
        quote_y = ((h - max_height) + (max_height - p_h)) / 2
        
        quote_y = quote_y - 2
           
        # needed this when going above 100 font size
        if font_size > 90:
            quote_y = quote_y - 12
                
        draw.multiline_text((quote_x, quote_y), reflowed, fill=inky_display.WHITE, font=bold_font, align="left")
        
        # print(reflowed + "\n")
                
        inky_display.set_image(img)
        inky_display.show()
        


    # This function will take a quote as a string, a width to fit
    # it into, and a font (one that's been loaded) and then reflow
    # that quote with newlines to fit into the space required.
    
    def reflow_quote(self, quote, width, font):
        words = quote.split(" ")
        reflowed = ''
        line_length = 0
    
        for i in range(len(words)):
            word = words[i] + " "
            word_length = font.getsize(word)[0]
            line_length += word_length
    
            if line_length < width:
                reflowed += word
            else:
                line_length = word_length
                reflowed = reflowed[:-1] + "\n" + word
    
        # reflowed = reflowed.rstrip() + '"'
        reflowed = reflowed.rstrip()
    
        return reflowed
        
    
    def count_chars(self, txt):
        result = 0
        for char in txt:
            result += 1     # same as result = result + 1
        return result
        
    
    def get_font_size(self, numchars):
        font_size = 125
        
        if numchars > 3:
            font_size = 90
            
        if numchars > 4:
            font_size = 54
            
        if numchars > 8:
            font_size = 40
            
        if numchars > 10:
            font_size = 36
            
        if numchars > 16:
            font_size = 34
            
        if numchars > 20:
            font_size = 30
            
        if numchars > 30:
            font_size = 26
            
        if numchars > 40:
            font_size = 23
            
        if numchars > 50:
            font_size = 20
            
        if numchars > 75:
            font_size = 18
            
        if numchars > 95:
            font_size = 16
            
        if numchars > 127:
            font_size = 14
            
        if numchars > 160:
            font_size = 13
            
        if numchars > 175:
            font_size = 12
            
        if numchars > 195:
            font_size = 11
            
        if numchars > 205:
            font_size = 10  
            
        # if numchars > 220:
        #     font_size = 10  
            
        return font_size