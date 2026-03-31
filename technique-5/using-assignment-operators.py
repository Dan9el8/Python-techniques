#This prevent the excessive use of repetition
if(count := fresh_fruit.get(Apple, 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()
