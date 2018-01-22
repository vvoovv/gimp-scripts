def selection_bucket_fill_with_gradient(numPixels=4.):
    img = gimp.image_list()[0]
    # ensure the active layer is visible
    pdb.gimp_layer_set_visible(img.active_layer, 1)
    drw = pdb.gimp_image_active_drawable(img)
    pdb.gimp_edit_copy(img.active_layer)
    floating_sel = pdb.gimp_edit_paste(drw, False)
    pdb.gimp_floating_sel_to_layer(floating_sel)
    pdb.gimp_selection_layer_alpha(img.active_layer)
    pdb.gimp_selection_feather(img, numPixels)
    drw = pdb.gimp_image_active_drawable(img)
    pdb.gimp_bucket_fill(drw, FG_BUCKET_FILL, NORMAL_MODE, 100, 0, 0, 0, 0)
    #pdb.gimp_image_lower_layer(img, img.active_layer)
    pdb.gimp_image_merge_down(img, img.active_layer, EXPAND_AS_NECESSARY)
