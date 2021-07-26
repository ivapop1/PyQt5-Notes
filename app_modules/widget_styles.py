app_window_stylesheet = """

#main_window{
    background-color: #121212;
}

"""

tab_window_stylesheet = """
QTabWidget::pane {
    
    border: 0px solid #535353;
    border-radius: 5px;
}

QTabBar::tab {
    background: #535353;
    margin-left: 10px;
    padding: 10px;
    min-width: 100px;
    
    
    font-size: 10pt;
    font-family: Century Gothic;
    color: #FFFFFF;
    
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QTabBar::tab:hover {
    background: gray;
    margin-left: 10px;
    padding: 10px;
    font-size: 11pt;
    
    
    font-family: Century Gothic;
    color: #FFFFFF;
    
}

QTabBar::tab:selected {
    background: #121212;
    margin-left: 15px;
    padding: 10px;
    
    
    font-size: 2pt;
    font-family: Century Gothic;
    color: #FFFFFF;
    
}

"""

title_label_stylesheet = """

#title_label{
    background-color: #232323;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 30px;
    padding-right: 30px;
    
     
    font-family: Century Gothic; 
    color: #B3B3B3; 
    font-size: 14pt;

}
"""



task_list_label_stylesheet = """

#task_list_label{
    
    font-family: Century Gothic; 
    color: #FFFFFF; 
    font-size: 11pt
}

"""

task_list_stylesheet = """

#task_list_widget{
    height: 500px; 
    background-color: #282828;
    color: #B3B3B3;
    font-size: 10pt;
    
    font-family: Century Gothic;
    padding-top: 2px;
    padding-left: 2px;
    padding-bottom: 15px;
    border-radius: 5;
    alternate-background-color: #212121;
}
#task_list_widget::item:hover{
    color: #FFFFFF;
    background: #212121;
}
#task_list_widget::item:selected{
    border: none;
    color: #FFFFF1;
    outline: none;
}
#task_list_widget QScrollBar{
    border: none;
    background: #282828;
    width: 0px
}

"""

add_button_stylesheet = """

#add_button{
    background-color: #282828; 
    
    font-size: 10pt;
    font-family: Century Gothic;
    color: #B3B3B3; 
    border-radius: 10;
}
#add_button::hover{
    background-color: #383838; 
    color: #FFFFFF; 
    border-radius: 10;
    font-size: 11pt;
}

"""

update_button_stylesheet = """

#update_button{
    background-color: #282828; 
    
    font-size: 10pt;
    font-family: Century Gothic;
    color: #B3B3B3; 
    border-radius: 10;
}
#update_button::hover{ 
    background-color: #383838; 
    font-family: Century Gothic;
    color: #FFFFFF; 
    border-radius: 10;
    font-size: 11pt;
}

"""

arch_button_stylesheet = """

#arch_button{
    background-color: #282828; 
    
    font-size: 10pt;
    font-family: Century Gothic;
    color: #B3B3B3; 
    border-radius: 10;
}
#arch_button::hover{
    background-color: #383838; 
    font-family: Century Gothic;
    color: #FFFFFF; 
    border-radius: 10;
    font-size: 11pt;
}

"""

task_details_label_stylesheet = """
#task_details_label{
    
    font-family: Century Gothic;
    color: #FFFFFF; 
    font-size: 11pt;
}   
"""

task_details_text_stylesheet = """
#task_details_text {
    background-color: #B3B3B3; 
    font-family: Courier;
    padding-top: 5px;
    padding-left: 12px;
    padding-right: 12px;
    font-style: italic; 
    font-size: 12pt;
    font-family: Century Gothic;
    border-radius: 5;
}
"""

task_deadline_label_stylesheet = """
#task_deadline_label {
    margin-top: 12px;
    font-size: 12pt;
  
    font-family: Century Gothic;
    color: #FFFFFF;
}
"""

task_deadline_date_stylesheet = """
#task_deadline_date {
    background-color: #B3B3B3;
    margin-top: 12px;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 5px;
    color: red;
    font-size: 14pt;
    
    font-family: Century Gothic;
    border-radius: 5;
}

"""



close_button_stylesheet = """

#close_button{
    background-color: #282828; 
    font-family: Century Gothic; 
    color: #B3B3B3;
    border-radius: 5; 
   
}
#close_button::hover{
    background-color: #383838; 
    font-family: Century Gothic;
    font-size: 9pt;
    color: #FFFFFF; 
    border-radius: 5;
    
}

"""

dialog_style_sheet = """

#dialog_window{
    background-color: #151617;
}

#task_title_group_box{
    margin-top: 10px;
    padding-bottom: 5px;
    background-color: #3a3b3c;
    border-radius: 2px;
}

#task_title_label{
    font-size: 9pt;
    font-family: Century Gothic;
    color: #e4e6eb;
}

#task_title_edit{
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 5px;
    background-color: #e4e6eb;
    color: #3a3b3c;
    font-size: 9pt;
    font-family: Century Gothic;
    border-radius: 3;
}

#task_details_group_box{
    margin-top: 10px;
    margin-bottom: 10px;
    padding-bottom: 10px;
    background-color: #3a3b3c;
    border-radius: 10;
    font-size: 4pt;
    font-family: Century Gothic;
    color: #FFFFFF;
}

#task_details_label{
    font-size: 9pt;
    font-family: Century Gothic;
    color: #e4e6eb;
}

#task_details_edit{
    padding-top: 5px;
    padding-bottom: 5px;
    background-color: #e4e6eb;
    color: #3a3b3c;
    font-size: 9pt;
    font-family: Century Gothic;
}

#task_deadline_group_box{
    margin-bottom: 5px;
    padding-bottom: 5px;
    background-color: #3a3b3c;
    border-radius: 10;
}

#task_deadline_label{
    font-size: 14pt;
    font-family: Century Gothic;
    color: #e4e6eb;
}

#task_deadline_edit{
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 5px;
    background-color: #e4e6eb;
    color: #3a3b3c;
    font-size: 9pt;
    font-family: Century Gothic;
    border-radius: 3;
}

#save_button{
    width: 100px;
    height: 30px;
    background-color: #282828; 
    font-family: Century Gothic;
    font-size: 10pt;
    color: #B3B3B3; 
    border-radius: 10;
}

#save_button::hover{
    background-color: #383838; 
    font-family: Century Gothic; 
    color: #FFFFFF; 
    border-radius: 10;
    font-size: 11pt;

}

#cancel_button{
    height: 30px;
    background-color: #282828; 
    font-family: Century Gothic;
    font-size: 10pt;
    color: #B3B3B3; 
    border-radius: 10;
}

#cancel_button::hover{
    background-color: #383838; 
    font-family: Century Gothic;
    color: #FFFFFF; 
    border-radius: 10;
    font-size: 11pt;

}

"""

StyleSheet = '''
/* Верхняя область навигации                            */
#qt_calendar_navigationbar {
    background-color: rgb(0, 188, 212);
    min-width: 800px;
    max-width: 800px;
    min-height: 35px;
    max-height: 35px;
}

/*  Кнопка последнего месяца и кнопка следующего месяца */
#qt_calendar_prevmonth, #qt_calendar_nextmonth {
    border: none;                     /* убрать границу */
    margin-top: 0px;
    color: white;
    min-width: 30px;
    max-width: 30px;
    min-height: 30px;
    max-height: 30px;
    border-radius: 10px;            /* выглядит как эллипс */
    font-weight: bold;              /* шрифт полужирный    */
    qproperty-icon: none;    
    background-color: transparent; /* Цвет фона прозрачный */
}

#qt_calendar_prevmonth {
    qproperty-text: "<";         /* Изменить текст кнопки  */
}
#qt_calendar_nextmonth {
    qproperty-text: ">";
}
#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
    background-color: rgba(225, 225, 225, 100);
}
#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
    background-color: rgba(235, 235, 235, 100);
}

/*  год, месяц                                                */
#qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: white;
    margin: -1px;
    min-width: -1px;
    border-radius: 15px;
    background-color: rgba(0, 188, 212, 100)
}
#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgba(225, 225, 225, 100);
}
#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgba(235, 235, 235, 100);
}

/* Поле ввода года                                                        */
#qt_calendar_yearedit {
    min-width: 85px;
    color: white;
    background: transparent;         /* Сделать фон окна ввода прозрачным */
}
#qt_calendar_yearedit::up-button {   /* Кнопка вверх                      */
    width: 25px;
    subcontrol-position: right;      
}
#qt_calendar_yearedit::down-button { /* Кнопка вниз     */
    width: 25px;
    subcontrol-position: left;       
}

/* меню выбора месяца                                          */
CalendarWidget_QToolButton_QMenu {
     background-color: white;
}

CalendarWidget_QToolButton_QMenu_item {
    padding: 10px;
}
CalendarWidget_QToolButton_QMenu_item_selected_enabled {
    background-color: rgb(230, 230, 230);
    selection-color: rgb(45, 86, 100);
    selection-background-color: rgb(205, 217, 226);
}
CalendarWidget_QToolButton_menu-indicator {
    subcontrol-position: right center;                
}

/* ниже календарной формы */
#qt_calendar_calendarview {
    outline: 0px;                                 /* Удалить выделенную пунктирную рамку */
    selection-background-color: rgb(0, 188, 212); 
}
'''
