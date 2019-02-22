# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now , add_days,cint
class MutasiBijih(Document):
	def validate(self):
		batch=frappe.get_doc("Kode Batch",self.batch)
		if batch.tak_percent and batch.tak_percent!=self.sn_tak:
			frappe.throw("SN Taksasi tidak boleh berubah")
		if batch.def_percent and batch.def_percent!=self.sn_def:
			frappe.throw("SN Definitif tidak boleh berubah")
		data = frappe.db.sql("select name , aktivitas from `tabMutasi Bijih` order by date desc limit 0,1")
		last = "Penerimaan"
		num = 0
		for row in data:
			last = row[1]
			num= num+1
		reason = "Ada Aktifitas Sebelumya , Sehingga hanya bisa melakukan Pengiriman"
		if num > 0 and last == "Penerimaan":
			reason= "Ada Pengiriman"
		elif num > 0 :
			reason= "Ada Penerimaan"
		if last == self.aktivitas:
			frappe.throw("Tidak bisa melakukan {} karena belum {}".format(last,reason))
	def on_cancel(self):
		frappe.throw("Dokumen tidak dapat di batalkan")
	def on_submit(self):
		if self.aktivitas == "Penerimaan":
			batch=frappe.get_doc("Kode Batch",self.batch)
			if not batch.sn_tak:
				if self.sn_tak :
					batch.sn_tak = self.berat_ore * self.sn_tak / self.qty
					batch.tak_percent = self.sn_tak
			if not batch.sn_def:
				if self.sn_def:
					batch.sn_def = self.berat_ore * self.sn_def / self.qty
					batch.def_percent = self.sn_def
			batch.ton_final=self.total
			if self.type == "PPBT" or self.type == "BPM" :
				batch.ppbt_total = self.total
			elif self.type == "GBT":
				batch.gbt_total = self.total
			elif self.type == "GMP":
				batch.gmp_total = self.total
			batch.s_loc = self.to_loc
			batch.update()
			list_dp = frappe.db.sql("""select name , qty from `tabData Produksi` where batch="{}" and (sn_def is NULL or sn_def=0) and (sn_tak is NULL or sn_tak=0) """.format(self.batch),as_list=1)
			for row in list_dp:
				kadar = batch.sn_tak
				if self.sn_def:
					kadar=batch.sn_def
				frappe.db.sql("""update `tabData Produksi` set sn_tak="{}" , sn_def="{}" , total="{}" where name={} """.format(self.sn_tak,self.sn_def,cint(row[1])*kadar,row[0]))

