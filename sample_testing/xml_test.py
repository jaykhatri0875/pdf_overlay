from xml.etree.ElementTree import XML, fromstring

txt = """<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""

text_xml = """<body>
 <div class='ocr_page' id='page_1' title='image "test_image.jpg"; bbox 0 0 630 360; ppageno 0; scan_res 96 96'>
   <div class='ocr_photo' id='block_1_1' title="bbox 267 0 600 20"></div>
   <div class='ocr_photo' id='block_1_2' title="bbox 12 2 160 25"></div>
   <div class='ocr_carea' id='block_1_3' title="bbox 16 12 493 86">
    <p class='ocr_par' id='par_1_1' lang='eng' title="bbox 16 12 493 86">
     <span class='ocr_line' id='line_1_1' title="bbox 16 12 493 66; baseline -0.036 -4; x_size 29; x_descenders 5; x_ascenders 9">
      <span class='ocrx_word' id='word_1_1' title='bbox 16 39 37 66; x_wconf 24'>oe</span>
      <span class='ocrx_word' id='word_1_2' title='bbox 61 43 152 59; x_wconf 0'>-sirerenz</span>
      <span class='ocrx_word' id='word_1_3' title='bbox 160 12 247 65; x_wconf 2'>(aan</span>
      <span class='ocrx_word' id='word_1_4' title='bbox 349 35 404 49; x_wconf 0'>aKa</span>
      <span class='ocrx_word' id='word_1_5' title='bbox 423 33 493 47; x_wconf 30'>Wow</span>
     </span>
     <span class='ocr_line' id='line_1_2' title="bbox 58 52 492 86; baseline -0.037 0; x_size 30.5; x_descenders 5.5; x_ascenders 9.5">
      <span class='ocrx_word' id='word_1_6' title='bbox 58 66 243 86; x_wconf 71'>INCOMETAXDEPARTMENT</span>
      <span class='ocrx_word' id='word_1_7' title='bbox 282 52 311 81; x_wconf 0'>22s</span>
      <span class='ocrx_word' id='word_1_8' title='bbox 351 59 492 77; x_wconf 0'>«GOVT.</span>
      <span class='ocrx_word' id='word_1_9' title='bbox 418 48 439 90; x_wconf 89'>OF</span>
      <span class='ocrx_word' id='word_1_10' title='bbox 446 59 492 77; x_wconf 95'>INDIA</span>
     </span>
    </p>
   </div>
   <div class='ocr_photo' id='block_1_4' title="bbox 12 172 630 350"></div>
   <div class='ocr_carea' id='block_1_5' title="bbox 12 90 385 163">
    <p class='ocr_par' id='par_1_2' lang='eng' title="bbox 16 90 385 163">
     <span class='ocr_line' id='line_1_3' title="bbox 16 90 266 106; baseline -0.036 5; x_size 27.794117; x_descenders 6.7941179; x_ascenders 8.0294123">
      <span class='ocrx_word' id='word_1_11' title='bbox 16 90 36 106; x_wconf 0'>&amp;</span>
      <span class='ocrx_word' id='word_1_12' title='bbox 263 100 266 102; x_wconf 25'></span>
     </span>
     <span class='ocr_line' id='line_1_4' title="bbox 12 96 363 132; baseline -0.035 -8.862; x_size 21.238094; x_descenders 5.2380953; x_ascenders 6">
      <span class='ocrx_word' id='word_1_13' title='bbox 12 100 36 132; x_wconf 36'>rg</span>
      <span class='ocrx_word' id='word_1_14' title='bbox 215 101 253 115; x_wconf 19'>ward</span>
      <span class='ocrx_word' id='word_1_15' title='bbox 257 103 290 115; x_wconf 10'>Fron</span>
      <span class='ocrx_word' id='word_1_16' title='bbox 295 103 331 114; x_wconf 19'>wen</span>
      <span class='ocrx_word' id='word_1_17' title='bbox 336 96 363 112; x_wconf 38'>wre</span>
     </span>
     <span class='ocr_line' id='line_1_5' title="bbox 186 117 385 135; baseline -0.035 0; x_size 22.5; x_descenders 5.5; x_ascenders 6.5">
      <span class='ocrx_word' id='word_1_18' title='bbox 186 123 251 135; x_wconf 95'>Permanent</span>
      <span class='ocrx_word' id='word_1_19' title='bbox 255 122 305 133; x_wconf 96'>Account</span>
      <span class='ocrx_word' id='word_1_20' title='bbox 309 120 355 131; x_wconf 96'>Number</span>
      <span class='ocrx_word' id='word_1_21' title='bbox 359 117 385 129; x_wconf 73'>Card</span>
     </span>
     <span class='ocr_line' id='line_1_6' title="bbox 227 145 342 163; baseline -0.043 0; x_size 18.529411; x_descenders 4.5294118; x_ascenders 5.3529415">
      <span class='ocrx_word' id='word_1_22' title='bbox 227 145 342 163; x_wconf 64'>FJXPKOOOSE</span>
     </span>
    </p>
   </div>
   <div class='ocr_carea' id='block_1_6' title="bbox 16 144 35 239">
    <p class='ocr_par' id='par_1_3' lang='eng' title="bbox 16 144 35 239">
     <span class='ocr_line' id='line_1_7' title="bbox 16 144 35 181; baseline 0 0; x_size 49.333332; x_descenders 12.333333; x_ascenders 12.333333">
      <span class='ocrx_word' id='word_1_23' title='bbox 16 144 35 181; x_wconf 71'>a</span>
     </span>
     <span class='ocr_line' id='line_1_8' title="bbox 16 196 35 239; baseline 0 -7; x_size 49.333332; x_descenders 12.333333; x_ascenders 12.333333">
      <span class='ocrx_word' id='word_1_24' title='bbox 16 196 35 239; x_wconf 0'>k</span>
     </span>
    </p>
   </div>
   <div class='ocr_photo' id='block_1_7' title="bbox 12 144 16 286"></div>
  </div>
 </body>"""

xml = fromstring(text_xml) 

for child in xml:
    print(" 0 ",child.tag, child.attrib)
    for c in child:
        print(" 1 ",c.tag, c.attrib)
        for ck in c:
            print(" 2 ",ck.tag)
    