# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BAP(Document):
	pass
	def on_submit(self):
		batch=frappe.get_doc("Kode Batch",self.batch)
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
			"objek":self.objek,
			"kelas":self.kelas,
			"nama_tambang":self.nama_tambang,
			"unit_produksi":self.unit_produksi,
			"badan_usaha":self.badan_usaha,
			"kode_du":self.kode_du,
			"nama_lokasi":self.nama_lokasi,
			"satuan":self.satuan,
			"qty":self.bruto,
			"sn_est":batch.sn_est,
			"sn_est":batch.sn_tak,
			"sn_est":batch.sn_def,
			"total":x
		})
		doc.insert()
		doc.on_submit()