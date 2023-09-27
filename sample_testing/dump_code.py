
# docs = DocumentFile.from_pdf("./inputs/test_text.pdf")
docs = DocumentFile.from_images("./inputs/test_image2.jpg")
# model = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)
# we will grab only the first two pages from the pdf for demonstration
# result = model(docs[:2])

# xml_outputs = result.export_as_xml()

# init the above parser
parser = HocrParser()

text_xml = """<html><head><title>docTR - XML export (hOCR)</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta name="ocr-system" content="python-doctr 0.7.0a0" /><meta name="ocr-capabilities" content="ocr_page ocr_carea ocr_par ocr_line ocrx_word" /></head><body><div class="ocr_page" id="page_1" title="image; bbox 0 0 1191 1684; ppageno 0" /><div class="ocr_carea" id="block_1" title="bbox 303 150                     337 164"><p class="ocr_par" id="par_1" title="bbox 303 150                     337 164"><span class="ocr_line" id="line_1" title="bbox 303 150                         337 164;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_1" title="bbox 303 150                             337 164;                             x_wconf 12">CAA</span></span></p></div><div class="ocr_carea" id="block_2" title="bbox 594 141                     734 160"><p class="ocr_par" id="par_2" title="bbox 594 141                     734 160"><span class="ocr_line" id="line_2" title="bbox 594 141                         734 160;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_2" title="bbox 594 141                             734 160;                             x_wconf 0">NDIDNEXF\AUR-</span></span></p></div><div class="ocr_carea" id="block_3" title="bbox 202 183                     490 268"><p class="ocr_par" id="par_3" title="bbox 202 183                     490 268"><span class="ocr_line" id="line_3" title="bbox 211 183                         490 227;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_3" title="bbox 211 196                             352 227;                             x_wconf 3">3CY</span><span class="ocrx_word" id="word_4" title="bbox 373 183                             490 225;                             x_wconf 6">faHTST</span></span><span class="ocr_line" id="line_4" title="bbox 202 234                         346 268;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_5" title="bbox 202 237                             299 268;                             x_wconf 98">INCOME</span><span class="ocrx_word" id="word_6" title="bbox 295 234                             346 268;                             x_wconf 96">TAXI</span></span></p></div><div class="ocr_carea" id="block_4" title="bbox 637 181                     870 253"><p class="ocr_par" id="par_4" title="bbox 637 181                     870 253"><span class="ocr_line" id="line_5" title="bbox 637 181                         867 215;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_7" title="bbox 637 184                             730 215;                             x_wconf 44">HRA</span><span class="ocrx_word" id="word_8" title="bbox 750 181                             867 210;                             x_wconf 8">TRCDR</span></span><span class="ocr_line" id="line_6" title="bbox 643 217                         870 253;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_9" title="bbox 643 222                             737 253;                             x_wconf 58">GOVT.</span><span class="ocrx_word" id="word_10" title="bbox 735 217                             785 252;                             x_wconf 99">OF</span><span class="ocrx_word" id="word_11" title="bbox 780 219                             870 250;                             x_wconf 100">INDIA</span></span></p></div><div class="ocr_carea" id="block_5" title="bbox 344 232                     489 263"><p class="ocr_par" id="par_5" title="bbox 344 232                     489 263"><span class="ocr_line" id="line_7" title="bbox 344 232                         489 263;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_12" title="bbox 344 232                             489 263;                             x_wconf 99">DEPARTMENT</span></span></p></div><div class="ocr_carea" id="block_6" title="bbox 395 275                     702 380"><p class="ocr_par" id="par_6" title="bbox 395 275                     702 380"><span class="ocr_line" id="line_8" title="bbox 438 275                         670 314;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_13" title="bbox 438 283                             505 314;                             x_wconf 7">Turrft</span><span class="ocrx_word" id="word_14" title="bbox 503 285                             559 311;                             x_wconf 6">HET</span><span class="ocrx_word" id="word_15" title="bbox 558 283                             622 309;                             x_wconf 13">HGUT</span><span class="ocrx_word" id="word_16" title="bbox 619 275                             670 309;                             x_wconf 5">ahTS</span></span><span class="ocr_line" id="line_9" title="bbox 395 306                         702 340;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_17" title="bbox 395 316                             500 340;                             x_wconf 99">Permanent</span><span class="ocrx_word" id="word_18" title="bbox 500 312                             581 339;                             x_wconf 100">Account</span><span class="ocrx_word" id="word_19" title="bbox 579 309                             655 335;                             x_wconf 100">Number</span><span class="ocrx_word" id="word_20" title="bbox 653 306                             702 334;                             x_wconf 100">Card</span></span><span class="ocr_line" id="line_10" title="bbox 457 350                         635 380;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_21" title="bbox 457 350                             635 380;                             x_wconf 91">FJXPK0005E</span></span></p></div><div class="ocr_carea" id="block_7" title="bbox 204 408                     579 604"><p class="ocr_par" id="par_7" title="bbox 204 408                     579 604"><span class="ocr_line" id="line_11" title="bbox 206 408                         579 454;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_22" title="bbox 206 408                             298 433;                             x_wconf 11">HTA/Name</span><span class="ocrx_word" id="word_23" title="bbox 206 429                             291 454;                             x_wconf 100">KHATRI</span><span class="ocrx_word" id="word_24" title="bbox 288 428                             410 452;                             x_wconf 91">JAYKUMAR</span><span class="ocrx_word" id="word_25" title="bbox 411 421                             579 446;                             x_wconf 53">DASHRATHBHAL</span></span><span class="ocr_line" id="line_12" title="bbox 204 469                         536 511;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_26" title="bbox 204 472                             250 500;                             x_wconf 21">fuat</span><span class="ocrx_word" id="word_27" title="bbox 247 475                             280 497;                             x_wconf 10">fT</span><span class="ocrx_word" id="word_28" title="bbox 276 475                             316 497;                             x_wconf 49">HTH</span><span class="ocrx_word" id="word_29" title="bbox 311 472                             388 497;                             x_wconf 82">/Father\'s</span><span class="ocrx_word" id="word_30" title="bbox 378 487                             536 511;                             x_wconf 55">TALAKSHIBHAI</span><span class="ocrx_word" id="word_31" title="bbox 383 469                             436 493;                             x_wconf 100">Name</span></span><span class="ocr_line" id="line_13" title="bbox 206 490                         380 520;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_32" title="bbox 206 490                             380 520;                             x_wconf 99">DASHRATHBHAI</span></span><span class="ocr_line" id="line_14" title="bbox 206 544                         438 576;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_33" title="bbox 206 553                             249 574;                             x_wconf 2">Se</span><span class="ocrx_word" id="word_34" title="bbox 244 546                             280 576;                             x_wconf 10">at</span><span class="ocrx_word" id="word_35" title="bbox 275 544                             378 574;                             x_wconf 14">arira/Date</span><span class="ocrx_word" id="word_36" title="bbox 373 546                             398 571;                             x_wconf 65">of</span><span class="ocrx_word" id="word_37" title="bbox 392 544                             438 571;                             x_wconf 100">Birth</span></span><span class="ocr_line" id="line_15" title="bbox 207 574                         341 604;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_38" title="bbox 207 574                             341 604;                             x_wconf 95">14/04/1999</span></span></p></div><div class="ocr_carea" id="block_8" title="bbox 517 482                     670 607"><p class="ocr_par" id="par_8" title="bbox 517 482                     670 607"><span class="ocr_line" id="line_16" title="bbox 538 482                         620 507;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_39" title="bbox 538 482                             620 507;                             x_wconf 100">KHATRI</span></span><span class="ocr_line" id="line_17" title="bbox 521 528                         642 594;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_40" title="bbox 521 528                             642 594;                             x_wconf 0">soslls</span></span><span class="ocr_line" id="line_18" title="bbox 517 577                         670 607;                         baseline 0 0; x_size 0; x_descenders 0; x_ascenders 0"><span class="ocrx_word" id="word_41" title="bbox 517 577                             670 607;                             x_wconf 4">EeeR/Signature</span></span></p></div></body></html>"""

test_xml2 = """
"""

xmls = ET.ElementTree(fromstring(test_xml2))
x = fromstring(text_xml)
for child in x:
    print(" 0 ",child.tag,child.attrib)
    for c in child:
        print("   1 ",c.tag,c.attrib)
        for ck in c:
            print("      2 ",ck.tag,ck.attrib)
            for ckg in c:
                print("          3 ",ckg.tag,ckg.attrib)

                

# old impl: #parser.export_pdfa('output.pdf', hocr=xml, invisible_text=False)
# iterate through the xml outputs and images and export to pdf/a
# the image is optional else you can set invisible_text=False and the text will be printed on a blank page
for i, img in enumerate(docs):
    xml_element_tree = xmls
    parser.export_pdfa('test_img.pdf', hocr=xml_element_tree, image = img, invisible_text = False)
