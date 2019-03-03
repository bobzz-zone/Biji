from frappe import _

def get_data():
	return [
		{
			"label": _("Transaction"),
			"items": [
				{
					"type": "doctype",
					"name": "Data Produksi",
				},
				{
					"type": "doctype",
					"name": "Pengiriman Batch",
				},
				{
					"type": "doctype",
					"name": "Penerimaan Batch",
				},
				{
					"type": "doctype",
					"name": "BAP",
				},
				{
					"type": "doctype",
					"name": "Process Order",
				},
				{
					"type": "doctype",
					"name": "Pengolahan Bijih",
				},
				{
					"type": "doctype",
					"name": "ID Alat",
				},
				{
					"type": "doctype",
					"name": "Kode Batch",
				},
			]
		},
		{
			"label": _("Master Data"),
			"items": [
				{
					"type": "doctype",
					"name": "Objek Produksi",
				},
				{
					"type": "doctype",
					"name": "Vendor",
				},
				{
					"type": "doctype",
					"name": "kelas",
				},
				{
					"type": "doctype",
					"label": "Nama Tambang / Kapal",
					"name": "DataSpek",
				},
				{
					"type": "doctype",
					"name": "Unit Produksi",
				},
				{
					"type": "doctype",
					"name": "WASPROD",
				},
				{
					"type": "doctype",
					"label" : "Badan usaha",
					"name": "DataSpek BU",
				},
				{
					"type": "doctype",
					"name": "Lokasi",
				},
				{
					"type": "doctype",
					"name": "Lokasi Kecamatan",
				},
				{
					"type": "doctype",
					"name": "IUP",
				},
				{
					"type": "doctype",
					"name": "Lokasi Penyimpanan",
				},
				{
					"type": "doctype",
					"name": "Satuan Produksi",
				},
				{
					"type": "doctype",
					"name": "Uji Kadar",
				},
				{
					"type": "doctype",
					"name": "Kelas",
				},
				{
					"type": "doctype",
					"name": "Staff",
				}
			]
		},
	]