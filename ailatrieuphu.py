total=0
def questions(cauhoi=[]):
    cauhoi=[
        ['Ngày mất của Bác Hồ: ',['19/5','30/4','2/9','Không có đáp án đúng'],'2/9']
    ,['Tìm giao của 2 tập hợp này: [-2;5] và [-3;3) ?',['[-3;-2]','[-3;5]','[-3;2)','[-2;3)'],'[-2;3)']
    ,['Nhật Bản là một quần đảo nằm ở?',['Đông Nam Châu Á','Đông Tây Châu Á','Đông Bắc Châu Á','Không có đáp án đúng'],'Đông Bắc Châu Á']
    ,['Trong Python để tìm vị trí của một phần tử trong mảng ta dùng hàm:',['index()','indox()','search()','searchindox()'],'index()']
    ,['Did you see the opening ceremony ... on TV last night?',['which showed','to show','showing','shown'],'shown']
    ,['Một khung dây kín đang ở trong một từ trường đều. Khi đưa nó ra ngoài phạm vi của vùng có từ trường thì',['xuất hiện lực lạ có xu hướng kéo khung dây lại.','không có từ thông qua khung dây nên không có dòng điện cảm ứng.','xuất hiện dòng điện cảm ứng sao cho từ trường tổng cộng tại vị trí khung dây có xu hướng giảm đi.','xuất hiện dòng điện cảm ứng sao cho từ trường qua khung dây giảm đi'],'xuất hiện lực lạ có xu hướng kéo khung dây lại.']
    ,['Đạo hàm của sin(x) là:',['sin(x)','-sin(x)','-cos(x)','cos(x)'],'cos(x)']
    ,['Điền vào chỗ trống:\n------\nTôi muốn tắt nắng đi\nCho màu đừng nhạt mất\nTôi muốn buộc gió lại\nCho ... đừng bay đi\n(Một tác phẩm của Xuân Diệu)',['hạ','nắng','hương','gió'],'hương']
    ,['Quốc gia nào có dân số lớn thứ 4 thế giới',['Mỹ','Pakistan','Indonesia','Brazil'],'Indonesia']
    ,['Số đồng phân của C6H12(anken):',['17','13','15','11'],'17']
    ,['Bài hát '"'Đừng Yêu Nữa, Em Mệt Rồi'"' của nhạc sĩ nào?',['Chi Pu','Tóc Tiên','Min','hnhngan'],'Min']
    ,['Kỷ lục thế giới xoay rubik 3x3 bằng tay hiện tại(2022) ở bao nhiêu giây?',['4.37','3.74','7.43','3.47'],'3.47']
    ,["Năm thành lập của thương hiệu Biti's Việt Nam? ",['1981','1982','1983','1984'],'1982']
    ,["EURO lần đầu tiên tổ chức tại quốc gia nào? ",['Anh','Mỹ','Pháp','Bồ Đào Nha'],'Pháp']
    ,["Vị vua cho lập Văn Miếu ở Kinh Đô Thăng Long vào năm 1070 là :",['Quang Trung','Lê Thánh Tông','Lý Thánh Tông',"Lý Thường Kiệt"],'Lý Thánh Tông']
    ]
    return cauhoi
def gioithieu():
    print('$$$-------------$$$')
    print('Chào mừng đến với ai là triệu phú. Code bởi KhuongXuanDinh\n-----------')
    print('Giới thiệu:\n -Có tổng cộng 15 câu hỏi chia làm 15 vòng thi, mỗi câu trả lời đúng bạn sẽ nhận được 100k\n-Nếu đúng hết bạn sẽ nhận ngay 1tr500k ** \n-Và tất nhiên là sẽ không có sự trợ giúp giành cho người chơi\n -Nếu bạn trả lời sai, bạn sẽ được ra về cùng số tiền tương ứng :))\n -Trong quá trình chơi, bạn có thể chat '"'dừng'"' để dừng cuộc chơi và nhận số tiền tương ứng')
    print('---------------')
def congtien():
    global total
    total =total +100
def taocauhoi(_):
    print(_[0])
    thuvien={}
    thuvien.update(A=_[1][0],B=_[1][1],C=_[1][2],D=_[1][3])
    for i in thuvien:
        print(i+': '+thuvien[i])
    return thuvien
def cautraloi(_,thuvien):
    print('---------')
    print('***Trả lời bằng cách chọn a,b,c hoặc d nhé @@')
    print('Chú ý: Nếu chọn sai bạn sẽ ra về với chỉ một nửa số tiền tương ứng :))')
    print('Bạn có thể dừng cuộc chơi và ra về với số tiền hiện tại bằng cách gõ: "'"dừng"'"')
    answer=input('Nhập câu trả lời của bạn của bạn: ')
    if answer.lower()=='dừng':
        print('Vậy hẹn lại bạn vào lần khác nhé :((')
        print(f'--- số tiền bạn nhận được là {total}k')
        return False
    else:
        if thuvien[answer.upper()]==_[2]:
            congtien()
            print('-------')
            print(f'Chính xác. Bạn thật tuyệt vời! Số tiền bạn có lúc này là: {total}k')
            print('-----**----**-----')
            return True
        else:
            print('Ôi thật tiếc! Câu trả lời của bạn chưa chính xác :((')
            print('-----')
            print('Câu trả lời chính xác là: {0}'.format(_[2]))
            print(f'Số tiền ra về cùng bạn hôm nay là: {round(total/2)} k \n ------\n Hẹn gặp bạn lần sau nhé :))')
            return False
def stargame():
    ready=input('Bạn đã sẵn sàng chơi chưa?(chọn rồi(r) hoặc chưa(c)):').lower()
    if ready =='chưa' or ready=='c':
        print('Thật đáng tiếc! vậy hẹn bạn vào lần khác nhé!')
    elif ready=='rồi' or ready=='r':
        print('Tốt! Cùng bắt đầu với những câu hỏi hóc búa nhé:')
        for i in range(len(cauhoi)):
            print(f'Câu hỏi thứ {i+1}:\n -----------')
            a=taocauhoi(cauhoi[i])
            b=cautraloi(cauhoi[i],a)
            if b==False:
                break
    else: print('Bạn nhập sai cú pháp, chương trình sẽ dừng lại!!')
cauhoi=questions()
gioithieu()
stargame()

    


