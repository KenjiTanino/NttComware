1 = widgets.Dropdown(options=select_list, value=None,description='(1)')
def on_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        if change['new'] == correct_list[0]:
          result_dic['(1)']='正解'
        else:
          result_dic['(1)']='不正解'
w1.observe(on_change)
display(w1)
