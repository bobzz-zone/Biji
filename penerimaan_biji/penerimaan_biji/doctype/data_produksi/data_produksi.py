# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now
class DataProduksi(Document):
	pass
	def validate(self):
		if self.status=="Closed":
        	frappe.throw("Data Produksi Sudah Tidak Boleh di Update")
	def on_update(self):
		batch = frappe.get_doc("Kode Batch",self.batch)
		if batch.closing &&  batch.closing > now() :
			frappe.throw("Batch Sudah tidak bisa di pakai untuk produksi")
		batch.total = batch.total+self.qty
		batch.ton_def=batch.sn_def*batch.total
		batch.ton_tak=batch.sn_tak*batch.total
		batch.ton_est=batch.sn_est*batch.total
		batch.save(ignore_permissions=True)
	def on_delete(self):
		batch = frappe.get_doc("Kode Batch",self.batch)
		if batch.closing &&  batch.closing > now() :
			frappe.throw("Batch Sudah tidak bisa di ubah")
		batch.total = batch.total-self.qty
		batch.ton_def=batch.sn_def*batch.total
		batch.ton_tak=batch.sn_tak*batch.total
		batch.ton_est=batch.sn_est*batch.total
		batch.save(ignore_permissions=True)
