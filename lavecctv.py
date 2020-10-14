impor  LIST
dari  LIST . impor id  * 
dari  LIST . itu  mengimpor  *
dari  LIST . jp  import  *
dari  LIST . kami  mengimpor  *
dari  LIST . fr  impor  *
dari  LIST . kr  impor  *
dari  LIST . de  import  *
dari  LIST . tr  impor  *
 permintaan impor , re , os

b = " \ 033 [0; 34m"
g = " \ 033 [1; 32m"
w = " \ 033 [1; 37m"
r = " \ 033 [1; 31m"
y = " \ 033 [1; 33m"
cyan  =  " \ 033 [0; 36m"
lgray  =  " \ 033 [0; 37m"
dgray  =  " \ 033 [1; 30m"
ir  =  " \ 033 [0; 101m"
reset  =  " \ 033 [0m"



def  main ():
    os . sistem ( 'jelas' )
    cetak ( "{} ____" ). format ( r )
    cetak ( "_ [] _ ​​/ ____ \ __ n_" )
    cetak ( "| _____. - .__ () _ |" )
    cetak ( "| Saya // # \\ \ |" )
    cetak ( "{} | P    \\ \ __ // |" ). format ( w )
    cetak ( "| CS '-' |" )
    cetak ( "{} '--------------'---------- {} ----------------- -. " ). format ( r , w )
    cetak ( "{} | {} Penulis: {} LAVEYIK {} | {} BALI {}  |" ). format ( r , w , r , w , r , ir , reset , w )
    cetak ( "{} | {} Youtube: {} Veyik YT {} | {} 081803794492 {} |" ). format ( r , w , w , w , lgray , w )
    cetak ( "{} '------------------------------------ {} ------ - '" ). format ( r , w )
    cetak ( "{} [1] {} Italia" ). format ( r , w )
    cetak ( "{} [2] {} Indonesia" ). format ( r , w )
    cetak ( "{} [3] {} Jepang" ). format ( r , w )
    cetak ( "{} [4] {} Amerika Serikat" ). format ( r , w )
    cetak ( "{} [5] {} Prancis" ). format ( r , w )
    cetak ( "{} [6] {} Korea" ). format ( r , w )
    cetak ( "{} [7] {} Jerman" ). format ( r , w )
    cetak ( "{} [8] {} Turki" ). format ( r , w )
    cetak ( "{} [9] {} Keluar" ). format ( r , w )
    cetak  ""
    pilih  =  masukan ( " \ 033 [1; 31m [ \ 033 [1; 37mPilih @ Nomor \ 033 [1; 31m] \ 033 [1; 37m>" )
    pemfilteran ( pilih )



def  filtering ( pilih ):
    jika  pilih  ==  1 :
        italia ()
    elif  pilih  ==  2 :
        indonesia ()
    elif  pilih  ==  3 :
        jepang ()
    elif  pilih  ==  4 :
        amerika serikat ()
    elif  pilih  ==  5 :
        perancis ()
    elif  pilih  ==  6 :
        korea ()
    elif  pilih  ==  7 :
        jerman ()
    elif  pilih  ==  8 :
        kalkun ()
    elif  pilih  ==  9 :
        cetak ( r + "Keluar ..." + w )
        os . sys . keluar ()
    lain :
        cetak ( r + "Keluar ..." + w )
        os . sys . keluar ()

jika  __name__  ==  '__main__' :
    utama ()
