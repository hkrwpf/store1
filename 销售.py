print("====================王鹏飞的商城==================")
print("日期    服装名称    价格     库存数量     销售量")
print("1号     羽绒服      253.6    500         10")
print("2号     牛仔裤      86.3     600         60")
print("3号     风衣        96.8     335         43")
print("4号     皮草        135.9    855         63")
print("5号	    T血	       65.8	    632	        63")
print("6号	    衬衫	      49.3	   562	       120")
print("7号	    牛仔裤	     86.3	    600	        72")
print("8号	    羽绒服	     253.6	  500	        69")
print("9号	    牛仔裤	     86.3	    600	        35")
print("10号	  羽绒服	     253.6	  500	        140")
print("11号	  牛仔裤	     86.3	    600	        90")
print("12号	  皮草	      135.9	   855	       24")
print("13号	  T血	       65.8	    632	        45")
print("14号    风衣	      96.8	   335	       25")
print("15号	  牛仔裤	     86.3	    600	        60")
print("16号	  T血	       65.8	    632	        129")
print("17号	  羽绒服	     253.6	  500	        10")
print("18号	  风衣	      96.8	   335	       43")
print("19号	  T血	       65.8	    632	        63")
print("20号	  牛仔裤	     86.3	    600	        60")
print("21号	  皮草	      135.9	   855	       63")
print("22号	  风衣	      96.8	   335	       60")
print("23号	  T血	       65.8	    632	        58")
print("24号    牛仔裤	     86.3	    600	        140")
print("25号	  T血	       65.8	    632	        48")
print("26号	  风衣	      96.8	   335	       43")
print("27号	  皮草	      135.9	   855	       57")
print("28号	  羽绒服	     253.6	  500	        10")
print("29号	  T血	       65.8	    632	        63")
print("30号	  风衣	      96.8	   335	       78")
A = 253.6*10+86.3*60+96.8*43+135.9*63+65.8*63+49.3*120+86.3*72+253.6*69+86.3*35+253.6*140+86.3*90+135.9*24+65.8*45+96.8*25+86.3*60+65.8*129+253.6*10+96.8*43+65.8*63+86.3*60+135.9*63+96.8*60+65.8*58+86.3*140+65.8*48+96.8*43+135.9*57+253.6*10+65.8*63+96.8*78
print("总销售额：","%.2f " % A)
i = (10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78)/30
print("销售数量:","%.2f" % i)
B = (253.6*239)/A*100
print("羽绒服占比：","%.2f" % B, "%" )
C = (86.3*1535)/A*100
print("牛仔裤占比：","%.2f" % C, "%")
D = (96.8*1774)/A*100
print("风衣占比：","%.2f" % D, "%")
E = (135.9*1580)/A*100
print("皮草占比：","%.2f" % E, "%")
F = (65.8*1590)/A*100
print("T血占比：","%.2f" % F, "%")
G = (49.3*120)/A*100
print("衬衫占比：","%.2f" % G, "%")


