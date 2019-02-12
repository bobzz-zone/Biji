# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime
class BAP(Document):
	def autoname(self):
		today = now_datetime()
		key = "BAP{}{}".format(self.unit_produksi,today.strftime('%y'))
		current = frappe.db.sql("SELECT `current` FROM `tabSeries` WHERE `name`=%s FOR UPDATE", (key,))
		if current and current[0][0] is not None:
			current = current[0][0]
			# yes, update it
			frappe.db.sql("UPDATE `tabSeries` SET `current` = `current` + 1 WHERE `name`=%s", (key,))
			current = cint(current) + 1
		else:
			# no, create it
			frappe.db.sql("INSERT INTO `tabSeries` (`name`, `current`) VALUES (%s, 1)", (key,))
			current = 1
		
		self.name= "{No urut}/{}/Tbk/BAP-3031/{}-S2.6".format('%04d'%current,self.unit_produksi,today.strftime('%y'))
	def on_submit(self):
		batch=frappe.get_doc("Kode Batch",self.batch)
		if batch.closing and batch.closing > now() :
			frappe.throw("Batch Sudah tidak bisa di pakai untuk produksi")
		x=0
		if batch.sn_def and batch.sn_def >0:
			x=batch.sn_def*self.bruto
		elif batch.sn_tak and batch.sn_tak >0:
			x=batch.sn_tak*self.bruto
		elif batch.sn_est and batch.sn_est >0:
			x=batch.sn_est*self.bruto
		
		doc = frappe.get_doc({
			"doctype": "Data Produksi",
			"id_alat": self.id_alat,
			"batch": self.batch,
			"kode_objek":self.kode_objek,
			"objek":batch.nama_tambang,
			"kelas":self.kelas,
			"nama_tambang":self.nama_tambang,
			"unit_produksi":self.unit_produksi,
			"badan_usaha":self.badan_usaha,
			"kode_du":self.kode_du,
			"nama_bu":self.nama_bu,
			"nama_lokasi":self.nama_lokasi,
			"satuan":self.satuan,
			"qty":self.bruto,
			"sn_est":batch.sn_est,
			"sn_est":batch.sn_tak,
			"sn_est":batch.sn_def,
			"total":x,
			"status":"closed"
		})

		doc.insert()
		self.data_produksi=doc.name
	def on_cancel(self):
		doc=frappe.get_doc("Data Produksi",self.data_produksi)
		doc.cancel(ignore_permissions=True)