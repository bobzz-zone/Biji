frappe.ui.form.on('IUP', {
	land:function(frm){
		var land = parseInt(frm.doc.land);
		var sea=parseInt(frm.doc.sea);
		frm.doc.total=land+sea;
		frm.refresh_field("total");
	},
	sea:function(frm){
		var land = parseInt(frm.doc.land);
		var sea=parseInt(frm.doc.sea);
		frm.doc.total=land+sea;
		frm.refresh_field("total");
	}
}
