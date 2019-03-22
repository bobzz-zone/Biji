# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cint,flt
class PenerimaanBatch(Document):
	def validate(self):
		batch=frappe.get_doc("Kode Batch",self.batch)
		if batch.tak_percent and batch.tak_percent!=self.sn_tak:
			frappe.throw("SN Taksasi tidak boleh berubah")
		if batch.def_percent and batch.def_percent!=self.sn_def:
			frappe.throw("SN Definitif tidak boleh berubah")
		if batch.jalan==0:
			frappe.throw("Batch Tidak dalam proses kirim tidak bisa di terima")
	def on_cancel(self):
		frappe.throw("Dokumen tidak dapat di batalkan")
	def on_update_after_submit(self):
		if self.is_first==1:
			if self.sn_def:
				batch=frappe.get_doc("Kode Batch",self.batch)
				batch.sn_def = self.berat_ore * (flt(self.sn_def)/flt(100)) / flt(self.qty)
				#frappe.throw("""{} == {} -- {} x {} / {}""".format(batch.sn_def ,flt(self.berat_ore) * (self.sn_def/flt(100)) / flt(self.qty),self.berat_ore,self.sn_def,self.qty))
				batch.def_percent = self.sn_def
				batch.total_final = self.total
				if self.type == "PPBT" or self.type == "BPM" :
					batch.ppbt_total = self.total
				elif self.type == "GBT":
					batch.gbt_total = self.total
				elif self.type == "GMP":
					batch.gmp_total = self.total
				batch.calculate()
				batch.save(ignore_permissions=1)
				list_dp = frappe.db.sql("""select name , qty from `tabData Produksi` where batch="{}" and (sn_def is NULL or sn_def=0) and (sn_tak is NULL or sn_tak=0) """.format(self.batch),as_list=1)
				for row in list_dp:
					kadar = batch.sn_tak
					if self.sn_def:
						kadar=batch.sn_def
					frappe.db.sql("""update `tabData Produksi` set sn_tak="{}" , sn_def="{}" , total="{}" where name="{}" """.format(batch.sn_tak,batch.sn_def,cint(row[1])*kadar,row[0]))
		else:
			frappe.throw("Tidak bisa update")
	def on_submit(self):
		num=0
		count = frappe.db.sql("""select count(1) from `tabPenerimaan Batch` where docstatus=1 and batch="{}" """.format(self.batch),as_list=1)
		for row in count:
			num = cint(row[0])+1
		batch=frappe.get_doc("Kode Batch",self.batch)
		#if not batch.sn_tak:
		if self.sn_tak :
			if num==1:
				batch.sn_tak = self.berat_ore * (flt(self.sn_tak)/flt(100)) / flt(self.qty)
			batch.tak_percent = self.sn_tak
		#if not batch.sn_def:
		if self.sn_def:
			if num==1:
				batch.sn_def = self.berat_ore * (flt(self.sn_def)/flt(100)) / flt(self.qty)
			batch.def_percent = self.sn_def
		#batch.ton_final=self.total
		if self.type == "PPBT" or self.type == "BPM" :
			batch.ppbt_total = self.total
		elif self.type == "GBT":
			batch.gbt_total = self.total
		elif self.type == "GMP":
			batch.gmp_total = self.total
		batch.tara=self.tara
		batch.kadar_air=self.kadar_air
		batch.berat_air = self.berat_air
		batch.netto = self.netto
		batch.berat_ore = self.berat_ore
		batch.bruto = self.bruto
		batch.s_loc = self.to_loc
		batch.nama_lokasi_sebelumnya=self.lokasi_to
		batch.type_lokasi_sebelumnya=self.type
		batch.jalan=0
		batch.jalan_temp=""
		batch.lokasi_temp=""
		batch.type_temp=""
		if num==1:
			batch.total_final = self.total
			batch.calculate()
			self.is_first=1
		batch.save(ignore_permissions=1)
		if num==1:
			list_dp = frappe.db.sql("""select name , qty from `tabData Produksi` where batch="{}" and (sn_def is NULL or sn_def=0) and (sn_tak is NULL or sn_tak=0) """.format(self.batch),as_list=1)
			for row in list_dp:
				kadar = batch.sn_tak
				if self.sn_def:
					kadar=batch.sn_def
				frappe.db.sql("""update `tabData Produksi` set sn_tak="{}" , sn_def="{}" , total="{}" where name="{}" """.format(batch.sn_tak,batch.sn_def,cint(row[1])*kadar,row[0]))
