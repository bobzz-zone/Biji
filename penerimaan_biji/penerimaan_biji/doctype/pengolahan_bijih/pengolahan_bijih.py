# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cint,flt
class PengolahanBijih(Document):
	def validate(self):
		if self.type=="Output":
			data = frappe.db.sql("""select total , output from `tabProcess Order Batch` where parent="{}" and batch="{}" """.format(self.po,self.batch),as_list=1)
			for row in data:
				if row[1] and flt(row[1])>0:
					frappe.throw("Sudah ada Output tidak bisa memasukan output lagi")
	def on_submit(self):
		po=frappe.get_doc("Process Order",self.po)
		if self.type == "Input":
			frappe.db.sql("""update `tabKode Batch` set used = 1 where name="{}" """.format(self.batch))
			po.append("batch_list",{"doctype":"Process Order Batch","batch":self.batch,"total":self.total})
		if self.type == "Output":
			for row in po.batch_list:
				if row.batch == self.batch:
					row.output = self.total
			frappe.db.sql("""update `tabKode Batch` set used = 0 where name="{}" """.format(self.batch))
			batch=frappe.get_doc("Kode Batch",self.batch)
			#batch.ton_final=self.total
			batch.tara=self.tara
			batch.kadar_air=self.kadar_air
			batch.berat_air = self.berat_air
			batch.netto = self.netto
			batch.berat_ore = self.berat_ore
			batch.bruto = self.bruto
			#if not batch.sn_tak:
			if self.sn_tak :
			#		batch.sn_tak = self.berat_ore * self.sn_tak / self.qty / 100
				batch.tak_percent = self.sn_tak
			#if not batch.sn_def:
			if self.sn_def:
			#		batch.sn_def = self.berat_ore * self.sn_def / self.qty /100
				batch.def_percent = self.sn_def
			#batch.calculate()
			batch.save(ignore_permissions=1)
		po.recalculate()
		po.save(ignore_permissions=1)
	def on_cancel(self):
		frappe.throw("Dokumen tidak dapat di batalkan")

def patch_output():
	list_ou = frappe.db.sql("""select name,po,batch,total from `tabPengolahan Bijih` where docstatus=1 and type="Output" """,as_list=1)
	for row in list_ou:
		po=frappe.get_doc("Process Order",row[1])
		for row in po.batch_list:
			if row.batch == row[2]:
				row.output = flt(row[3])
		po.recalculate()
		po.save(ignore_permissions=1)
			