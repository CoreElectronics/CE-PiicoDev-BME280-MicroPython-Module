_A=None
from PiicoDev_Unified import *
compat_str='\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'
class PiicoDev_BME280:
	def __init__(self,bus=_A,freq=_A,sda=_A,scl=_A,t_mode=2,p_mode=5,h_mode=1,iir=1,address=119):
		try:
			if compat_ind>=1:0
			else:print(compat_str)
		except:print(compat_str)
		self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.t_mode=t_mode;self.p_mode=p_mode;self.h_mode=h_mode;self.iir=iir;self.addr=address;self._t_fine=0;self._T1=self._read16(136);self._T2=self._short(self._read16(138));self._T3=self._short(self._read16(140));self._P1=self._read16(142);self._P2=self._short(self._read16(144));self._P3=self._short(self._read16(146));self._P4=self._short(self._read16(148));self._P5=self._short(self._read16(150));self._P6=self._short(self._read16(152));self._P7=self._short(self._read16(154));self._P8=self._short(self._read16(156));self._P9=self._short(self._read16(158));self._H1=self._read8(161);self._H2=self._short(self._read16(225));self._H3=self._read8(227);a=self._read8(229);self._H4=(self._read8(228)<<4)+a%16;self._H5=(self._read8(230)<<4)+(a>>4);self._H6=self._read8(231)
		if self._H6>127:self._H6-=256
		self._write8(242,self.h_mode);sleep_ms(2);self._write8(244,36);sleep_ms(2);self._write8(245,self.iir<<2)
	def _read8(self,reg):t=self.i2c.readfrom_mem(self.addr,reg,1);return t[0]
	def _read16(self,reg):t=self.i2c.readfrom_mem(self.addr,reg,2);return t[0]+t[1]*256
	def _write8(self,reg,dat):self.i2c.write8(self.addr,bytes([reg]),bytes([dat]))
	def _short(self,dat):
		if dat>32767:return dat-65536
		else:return dat
	def read_raw_data(self):
		self._write8(244,self.p_mode<<5|self.t_mode<<2|1);sleep_time=1250
		if self.t_mode in[1,2,3,4,5]:sleep_time+=2300*(1<<self.t_mode)
		if self.p_mode in[1,2,3,4,5]:sleep_time+=575+2300*(1<<self.p_mode)
		if self.h_mode in[1,2,3,4,5]:sleep_time+=575+2300*(1<<self.h_mode)
		sleep_ms(1+sleep_time//1000)
		while self._read16(243)&8:sleep_ms(1)
		raw_p=(self._read8(247)<<16|self._read8(248)<<8|self._read8(249))>>4;raw_t=(self._read8(250)<<16|self._read8(251)<<8|self._read8(252))>>4;raw_h=self._read8(253)<<8|self._read8(254);return raw_t,raw_p,raw_h
	def read_compensated_data(self):
		A='NaN'
		try:raw_t,raw_p,raw_h=self.read_raw_data()
		except:print(i2c_err_str.format(self.addr));return float(A),float(A),float(A)
		var1=((raw_t>>3)-(self._T1<<1))*(self._T2>>11);var2=(raw_t>>4)-self._T1;var2=var2*((raw_t>>4)-self._T1);var2=(var2>>12)*self._T3>>14;self._t_fine=var1+var2;temp=self._t_fine*5+128>>8;var1=self._t_fine-128000;var2=var1*var1*self._P6;var2=var2+(var1*self._P5<<17);var2=var2+(self._P4<<35);var1=(var1*var1*self._P3>>8)+(var1*self._P2<<12);var1=((1<<47)+var1)*self._P1>>33
		if var1==0:pres=0
		else:p=((1048576-raw_p<<31)-var2)*3125//var1;var1=self._P9*(p>>13)*(p>>13)>>25;var2=self._P8*p>>19;pres=(p+var1+var2>>8)+(self._P7<<4)
		h=self._t_fine-76800;h=((raw_h<<14)-(self._H4<<20)-self._H5*h+16384>>15)*((((h*self._H6>>10)*((h*self._H3>>11)+32768)>>10)+2097152)*self._H2+8192>>14);h=h-(((h>>15)*(h>>15)>>7)*self._H1>>4);h=0 if h<0 else h;h=419430400 if h>419430400 else h;humi=h>>12;return temp,pres,humi
	def values(self):temp,pres,humi=self.read_compensated_data();return temp/100,pres/256,humi/1024
	def pressure_precision(self):p=self.read_compensated_data()[1];pi=float(p//256);pd=p%256/256;return pi,pd
	def altitude(self,pressure_sea_level=1013.25):pi,pd=self.pressure_precision();return 44330*(1-(float(pi+pd)/100/pressure_sea_level)**(1/5.255))