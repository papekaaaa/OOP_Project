import streamlit as st
     
st.title('1 วันควรกินเท่าไหร่ถึงจะพอนะ?')
number_input = st.number_input('กรอกน้ำหนัก (กิโลกรัม) ')
c1_input = st.checkbox('ผู้ชาย')
c2_input = st.checkbox('ผู้หญิง ')
select_box = st.selectbox('กรอกช่วงวัย', ['กรุณาเลือกช่วงวัย','เด็กอายุ 6-13 ปี', 'วัยรุ่น', 'วัยทำงาน','ผู้ใช้แรงงาน','ผู้สูงอายุ'])


st.title('***กินตามนี้สิ!***')
if not number_input:
    pass
elif 0 < number_input < 600 : 
    Weight = number_input * 2.2 * 30 / 2 
    if Weight:
        st.write(f'ควรดื่มน้ำ {round(Weight, 2)} มิลลิลิตรต่อวัน')
else : 
    st.write('กรุณากรอกน้ำหนักใหม่')

if select_box == 'กรุณาเลือกช่วงวัย':
    if c1_input and c2_input :
        st.write('กรุณากรอกเพียงตัวเลือกเดียว')
    elif c1_input or c2_input:
        st.write('กรุณากรอกช่วงวัย')
elif (not c1_input and not c2_input):
    st.write('กรุณากรอกเพศ')
elif ( c1_input and  c2_input):
    st.write('กรุณากรอกเพียงตัวเลือกเดียว')
elif c1_input  :
    if  select_box == 'วัยทำงาน' or select_box ==  'วัยรุ่น':
        st.markdown(
            '''

            - ควรรับประทานอาหารปริมาณ 2,000 kcal ต่อวัน
            - ข้าว-แป้ง = 10 ทัพพี
            - ผัก = 5 ทัพพี (ผักดิบ 1 ถ้วยตวง หรือผักสุก 1/2 ถ้วยตวง)
            - ผลไม้หวานน้อย = 4 ส่วน (1 ส่วน = ผลไม้ประมาณ 6-10 คำ)
            - เนื้อสัตว์ = 9 ช้อนทานข้าว (1 ช้อน = 15 กรัม)
            - นม 1 แก้ว (240 มล.)

            <span style="color: orange;">ส่วนนี้ก็สำคัญ</span>
            
            - ปริมาณน้ำตาล 

                เด็ก 4 ช้อนชา
                ผู้ใหญ่ 6 ช้อนชา
            - ปริมาณไขมัน 

                ไม่เกิน 65 กรัม(ประมาณ 16 ช้อนชา)
            - ปริมาณโซเดียม 

                ไม่เกิน 2300 มิลลิกรัม (ประมาณ 1 ช้อนชา)
            ''',
            unsafe_allow_html=True
        )
        st.image('อาหาร2.jpg')

        
    elif  select_box == 'เด็กอายุ 6-13 ปี' or select_box ==  'ผู้สูงอายุ':
          st.markdown(
            '''
            - ควรรับประทานอาหารปริมาณ 1,600 kcal ต่อวัน
            - ข้าว-แป้ง = 8 ทัพพี
            - ผัก = 4-6 ทัพพี (ผักดิบ 1 ถ้วยตวง หรือผักสุก 1/2 ถ้วยตวง)
            - ผลไม้หวานน้อย = 3-4 ส่วน (1 ส่วน = ผลไม้ประมาณ 6-10 คำ)
            - เนื้อสัตว์ = 6 ช้อนทานข้าว (1 ช้อน = 15 กรัม)
            - นม 1-2 แก้ว (1 แก้ว = 240 มล.)

            <span style="color: orange;">ส่วนนี้ก็สำคัญ</span>
                
            - ปริมาณน้ำตาล 

                เด็ก 4 ช้อนชา
                ผู้ใหญ่ 6 ช้อนชา
            - ปริมาณไขมัน 

                ไม่เกิน 65 กรัม(ประมาณ 16 ช้อนชา)
            - ปริมาณโซเดียม 

                ไม่เกิน 2300 มิลลิกรัม (ประมาณ 1 ช้อนชา)
                ''',
                unsafe_allow_html=True
        )
          st.image('อาหาร1.jpg')

    else:    
          st.markdown(
        '''
        - ควรรับประทานอาหารปริมาณ 2,400 kcal ต่อวัน
        - ข้าว-แป้ง = 12 ทัพพี
        - ผัก = 6 ทัพพี (ผักดิบ 1 ถ้วยตวง หรือผักสุก 1/2 ถ้วยตวง)
        - ผลไม้หวานน้อย = 5 ส่วน (1 ส่วน = ผลไม้ประมาณ 6-10 คำ)
        - เนื้อสัตว์ = 12 ช้อนทานข้าว (1 ช้อน = 15 กรัม)
        - นม 1 แก้ว (1 แก้ว = 240 มล.)

        <span style="color: orange;">ส่วนนี้ก็สำคัญ</span>
            
        - ปริมาณน้ำตาล 

            เด็ก 4 ช้อนชา
            ผู้ใหญ่ 6 ช้อนชา
        - ปริมาณไขมัน 

            ไม่เกิน 65 กรัม(ประมาณ 16 ช้อนชา)
        - ปริมาณโซเดียม 

            ไม่เกิน 2300 มิลลิกรัม (ประมาณ 1 ช้อนชา)
            ''',
            unsafe_allow_html=True
        )
          st.image('อาหาร3.jpg')
          

elif c2_input:
    if select_box == 'วัยทำงาน' or select_box == 'เด็กอายุ 6-13 ปี'or select_box ==  'ผู้สูงอายุ':
        st.markdown(
        '''
        - ควรรับประทานอาหารปริมาณ 1,600 kcal ต่อวัน
        - ข้าว-แป้ง = 8 ทัพพี
        - ผัก = 4-6 ทัพพี (ผักดิบ 1 ถ้วยตวง หรือผักสุก 1/2 ถ้วยตวง)
        - ผลไม้หวานน้อย = 3-4 ส่วน (1 ส่วน = ผลไม้ประมาณ 6-10 คำ)
        - เนื้อสัตว์ = 6 ช้อนทานข้าว (1 ช้อน = 15 กรัม)
        - นม 1-2 แก้ว (1 แก้ว = 240 มล.)
        
        <span style="color: orange;">ส่วนนี้ก็สำคัญ</span>
            
        - ปริมาณน้ำตาล 

            เด็ก 4 ช้อนชา
            ผู้ใหญ่ 6 ช้อนชา
        - ปริมาณไขมัน 

            ไม่เกิน 65 กรัม(ประมาณ 16 ช้อนชา)
        - ปริมาณโซเดียม 

            ไม่เกิน 2300 มิลลิกรัม (ประมาณ 1 ช้อนชา)
            ''',
            unsafe_allow_html=True
        ) 
        st.image('อาหาร1.jpg')

    elif select_box == 'วัยรุ่น':
        st.markdown(
            '''
            - ควรรับประทานอาหารปริมาณ 2,000 kcal ต่อวัน
            - ข้าว-แป้ง = 10 ทัพพี
            - ผัก = 5 ทัพพี (ผักดิบ 1 ถ้วยตวง หรือผักสุก 1/2 ถ้วยตวง)
            - ผลไม้หวานน้อย = 4 ส่วน (1 ส่วน = ผลไม้ประมาณ 6-10 คำ)
            - เนื้อสัตว์ = 9 ช้อนทานข้าว (1 ช้อน = 15 กรัม)
            - นม 1 แก้ว (240 มล.)
            
            <span style="color: orange;">ส่วนนี้ก็สำคัญ</span>
            
        - ปริมาณน้ำตาล 

            เด็ก 4 ช้อนชา
            ผู้ใหญ่ 6 ช้อนชา
        - ปริมาณไขมัน 

            ไม่เกิน 65 กรัม(ประมาณ 16 ช้อนชา)
        - ปริมาณโซเดียม 

            ไม่เกิน 2300 มิลลิกรัม (ประมาณ 1 ช้อนชา)
            ''',
            unsafe_allow_html=True
        )
        st.image('อาหาร2.jpg')

    else:
          st.markdown(
        '''
        - ควรรับประทานอาหารปริมาณ 2,400 kcal ต่อวัน
        - ข้าว-แป้ง = 12 ทัพพี
        - ผัก = 6 ทัพพี (ผักดิบ 1 ถ้วยตวง หรือผักสุก 1/2 ถ้วยตวง)
        - ผลไม้หวานน้อย = 5 ส่วน (1 ส่วน = ผลไม้ประมาณ 6-10 คำ)
        - เนื้อสัตว์ = 12 ช้อนทานข้าว (1 ช้อน = 15 กรัม)
        - นม 1 แก้ว (1 แก้ว = 240 มล.)
        
        <span style="color: orange;">ส่วนนี้ก็สำคัญ</span>
            
        - ปริมาณน้ำตาล 

            เด็ก 4 ช้อนชา
            ผู้ใหญ่ 6 ช้อนชา
        - ปริมาณไขมัน 

            ไม่เกิน 65 กรัม(ประมาณ 16 ช้อนชา)
        - ปริมาณโซเดียม 

            ไม่เกิน 2300 มิลลิกรัม (ประมาณ 1 ช้อนชา)
            ''',
            unsafe_allow_html=True
        )
          st.image('อาหาร3.jpg')
          

          
elif c1_input and c2_input and select_box == 'กรุณาเลือกช่วงวัย'or select_box == 'วัยทำงาน' or select_box == 'เด็กอายุ 6-13 ปี'or select_box ==  'ผู้สูงอายุ ' or select_box == 'วัยรุ่น' or select_box == 'ผู้ใช้แรงงาน':
    if c1_input and c2_input:
        st.write('กรุณากรอกใหม่')



# พื้นหลัง
import base64

def add_bg_from_local(image_file, footer_link):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{encoded_string}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            align-items: center;
            position: relative;
        }}
        .custom-footer {{
            position: absolute;
            bottom: 10px;
            font-size: 14px;
            color: white;
        }}
        .custom-footer a {{
            color: white;
            text-decoration: underline;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local('พื้นหลัง3.jpg', 'http://localhost:8502/')







# # streamlit run C:\Users\Asus\OneDrive\เดสก์ท็อป\oop\OOP_Project\food01.py
