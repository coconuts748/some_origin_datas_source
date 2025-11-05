from 未完成.数据综合获取.control_all_tasks import control_all_tasks
from 未完成.数据综合获取.further_tidy_up_datas import further_tidy_up_datas
from 未完成.数据综合获取.build_client_pool import build_client_pool
from 未完成.数据综合获取.stored_files_methods import creat_txt_file,creat_json_file
from 未完成.数据综合获取.datas_hrefs_combine import combine_hrefs,hrefs_combine
from loguru import logger
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.ttk import Progressbar
import time

def main_running_frame(choose_frame_mode):
    def ui_version():
        logger.info('ui_version running...')
        def inner_ui_version():
            if messagebox.askyesno('提示','是否使用代理以进行初步访问?'):
                def pool_progress_bar():
                    ####进度条适配#####
                    def ui_transmit_pool_api():
                        def inner_ui_transmit_pool_api():
                            api_cite = str(input_api_source.get().strip())
                            if len(api_cite) == 0:
                                messagebox.showwarning('错误', 'api输入无效!')
                            else:
                                if messagebox.askyesno('提示', '输入的api为{}\n是否继续?'.format(api_cite)):
                                    def ui_progress_show():
                                        def start_bar():
                                            ui_progress_bar.start()

                                        def end_bar():
                                            ui_progress_bar.stop()

                                        ui_transmit_pool_api_root.destroy()   #caution:不是本体root!
                                        start_bar()
                                        build_client_pool(api_source=api_cite)
                                        end_bar()
                                        ui_progress_show_root.destroy()   #这是..

                                        first_label.config(text='加载完成,点击下方可退出...')
                                        ui_progress_show_root.update_idletasks()
                                        def quit_ui_progress_show():
                                            if messagebox.askyesno('提示','确认退出?'):
                                                ui_progress_show_root.destroy()

                                        ttk.Button(ui_progress_show_root,text='退出',command =quit_ui_progress_show).pack()
                                        ui_progress_show_root.update_idletasks()

                                    ui_progress_show_root = tk.Tk()
                                    ui_progress_show_root.title('加载进度')

                                    first_label = ttk.Label(ui_progress_show_root,text='加载中....')
                                    first_label.pack()

                                    ui_progress_bar = ttk.Progressbar(ui_progress_show_root, length=200, mode='indeterminate')
                                    ui_progress_bar.pack()

                                    ttk.Button(ui_progress_show_root,text='start',command=ui_progress_show).pack()
                                    ui_progress_show_root.mainloop()

                                    def two_data_proceeds():
                                        def inner_first_data_proceed():
                                            select_thing = str(select_input.get().strip())
                                            if len(select_thing) == 0:
                                                messagebox.showwarning('错误','搜索内容无效!')
                                            else:
                                                if messagebox.askyesno('提示',f'此次搜索的内容为{select_thing}\n是否继续?'):
                                                    control_all_tasks(search_here=select_thing,control_mode='with_client')
                                                    #########终止保存或下一步处理后保存##########
                                                    def disturbing_next_proceed():
                                                        if messagebox.askyesno('提示','是否确认?'):
                                                            ui_continue_or_disturb_root.destroy()
                                                            def saved_txt_format():
                                                                if messagebox.askyesno('提示', '是否确认?'):
                                                                    disturbing_next_proceed_root.destroy()
                                                                    hrefs_combine()
                                                                    creat_txt_file(writing_file_name='txt_oring_hrefs',writing_content=str(combine_hrefs),whether_been_seen=False)

                                                            def saved_json_format():
                                                                if messagebox.askyesno('提示', '是否确认?'):
                                                                    disturbing_next_proceed_root.destroy()
                                                                    hrefs_combine()
                                                                    creat_json_file(writing_file_name='json_oring_hrefs',writing_content=str(combine_hrefs),whether_been_seen=False)

                                                            def quit_disturbing_next_proceed():
                                                                if messagebox.askyesno('提示', '是否确认退出当前界面?'):
                                                                    disturbing_next_proceed_root.destroy()

                                                            disturbing_next_proceed_root = tk.Tk()
                                                            disturbing_next_proceed_root.title('储存方式')

                                                            ttk.Button(disturbing_next_proceed_root, text='txt格式',
                                                                       command=saved_txt_format).pack()
                                                            ttk.Button(disturbing_next_proceed_root, text='json格式',
                                                                       command=saved_json_format).pack()
                                                            ttk.Button(disturbing_next_proceed_root, text='退出',
                                                                       command=quit_disturbing_next_proceed).pack()
                                                            disturbing_next_proceed_root.mainloop()

                                                    def continue_next_proceed():
                                                        if messagebox.askyesno('提示','是否确认?'):
                                                            ui_continue_or_disturb_root.destroy()
                                                            try:
                                                                def with_client_async():
                                                                    if messagebox.askyesno('提示','是否确认?'):
                                                                        client_async_root.destroy()
                                                                        further_tidy_up_datas(tidy_mode='with_client')

                                                                def without_client_async():
                                                                    if messagebox.askyesno('提示','是否确认?'):
                                                                        client_async_root.destroy()
                                                                        further_tidy_up_datas(tidy_mode='without_client')

                                                                def quit_client_async():
                                                                    if messagebox.askyesno('提示','是否退出当前页面?'):
                                                                        client_async_root.destroy()

                                                                client_async_root = tk.Tk()
                                                                client_async_root.title('链接访问方式选择')

                                                                ttk.Button(client_async_root,text='使用代理',command=with_client_async).pack()
                                                                ttk.Button(client_async_root,text='本地访问',command=without_client_async).pack()
                                                                ttk.Button(client_async_root,text='退出',command=quit_client_async).pack()
                                                                client_async_root.mainloop()
                                                            except Exception as p:
                                                                logger.error(p)

                                                    def quit_ui_continue_next_proceed():
                                                        if messagebox.askyesno('提示','是否退出当前页面?'):
                                                            ui_continue_or_disturb_root.destroy()

                                                    ui_continue_or_disturb_root = tk.Tk()
                                                    ui_continue_or_disturb_root.title('mode_1_next')

                                                    ttk.Button(ui_continue_or_disturb_root,text='终止并保存数据',command=disturbing_next_proceed).pack()
                                                    ttk.Button(ui_continue_or_disturb_root,text='进行下一步',command=continue_next_proceed).pack()
                                                    ttk.Button(ui_continue_or_disturb_root,text='退出',command=quit_ui_continue_next_proceed).pack()
                                                    ui_continue_or_disturb_root.mainloop()

                                        first_data_proceed_root = tk.Tk()
                                        first_data_proceed_root.title('传入搜索')

                                        ttk.Label(first_data_proceed_root,text='搜索:').grid(row=0,column=0,columnspan=2)
                                        select_input = tk.Entry(first_data_proceed_root)
                                        select_input.grid(row=0,column=3,columnspan=5)

                                        ttk.Button(first_data_proceed_root,text='完成输入',command=inner_first_data_proceed).grid(row=1,column=0,columnspan=2)
                                        first_data_proceed_root.mainloop()

                                    two_data_proceeds()

                        ui_transmit_pool_api_root = tk.Tk()
                        ui_transmit_pool_api_root.title('代理api获取')

                        ttk.Label(ui_transmit_pool_api_root,text='api:').grid(row=1,column=0,columnspan=2)
                        input_api_source = ttk.Entry(ui_transmit_pool_api_root)
                        input_api_source.grid(row=1,column=3,columnspan=5)

                        ttk.Button(ui_transmit_pool_api_root,text='next_step',command=inner_ui_transmit_pool_api).grid(row=2,column=0,columnspan=2)
                        ui_transmit_pool_api_root.mainloop()

                    ui_transmit_pool_api()

                def quit_pool_progress_bar():
                    if messagebox.askyesno('提示','确认退出当前页面?'):
                        ui_progress_bar_root.destroy()

                ui_progress_bar_root = tk.Tk()
                ui_progress_bar_root.title('运行代理池中.....')

                origin_progress_label = ttk.Label(ui_progress_bar_root,text='点击下方运行代理池进程')
                origin_progress_label.pack()

                ttk.Button(ui_progress_bar_root,text='开始运行',command=pool_progress_bar).pack()
                ttk.Button(ui_progress_bar_root,text='退出',command=quit_pool_progress_bar).pack()
                ui_progress_bar_root.mainloop()

            else:
                def without_client_transmit_search_things():
                    without_input_search = str(without_input_search__.get().strip())
                    if len(without_input_search) == 0:
                        messagebox.showwarning('错误','搜索内容无效!')
                    if messagebox.askyesno('提示',f'搜索的内容为:{without_input_search}\n是否继续？'):
                        without_client_transmit_search_things_root.destroy()

                        control_all_tasks(search_here=without_input_search,control_mode='without_client')

                        def stored_message():
                            if messagebox.askyesno('提示','是否确认?'):
                                condition_two_root.destroy()
                                def condition_json_format():
                                    creat_json_file(writing_file_name='初始无代理',writing_content=str(combine_hrefs),whether_been_seen='True')
                                    if messagebox.showinfo('提示','信息已储存成功!\n是否退出？'):
                                        condition_format_root.destroy()
                                def condition_txt_format():
                                    creat_txt_file(writing_file_name='初始无代理',writing_content=str(combine_hrefs),whether_been_seen='False')
                                    if messagebox.askyesno('提示','信息已储存成功!\n是否退出？'):
                                        condition_format_root.destroy()

                                def quit_condition_format():
                                    if messagebox.askyesno('提示','是否确认退出?'):
                                        condition_format_root.destroy()

                                condition_format_root = tk.Tk()
                                condition_format_root.title('储存方式')

                                ttk.Button(condition_format_root,text='txt格式',command=condition_txt_format).pack()
                                ttk.Button(condition_format_root,text='json格式',command=condition_json_format).pack()
                                ttk.Button(condition_format_root,text='退出',command=quit_condition_format).pack()
                                condition_format_root.mainloop()


                        def condition_two_with_href_async():
                            if messagebox.askyesno('提示','是否确认?'):
                                condition_two_root.destroy()
                                further_tidy_up_datas(tidy_mode='with_client')

                        def condition_two_without_href_async():
                            if messagebox.askyesno('提示','是否确认?'):
                                condition_two_root.destroy()
                                further_tidy_up_datas(tidy_mode='without_client')

                        def quit_condition_two():
                            if messagebox.askyesno('提示','是否退出?'):
                                condition_two_root.destroy()

                        condition_two_root = tk.Tk()
                        condition_two_root.title('mode_2_next')

                        ttk.Button(condition_two_root,text='储存初始搜索链接',command=stored_message).pack()
                        ttk.Button(condition_two_root,text='使用代理',command=condition_two_with_href_async).pack()
                        ttk.Button(condition_two_root,text='本地访问',command=condition_two_without_href_async).pack()
                        ttk.Button(condition_two_root,text='退出',command=quit_condition_two).pack()
                        condition_two_root.mainloop()

                def quit_without_client_transmit_search_things():
                    if messagebox.askyesno('提示','是否确认退出?'):
                        without_client_transmit_search_things_root.destroy()

                without_client_transmit_search_things_root = tk.Tk()
                without_client_transmit_search_things_root.title('搜索内容传输')

                ttk.Label(without_client_transmit_search_things_root,text='搜索:').grid(row=1,column=0,columnspan=2)
                without_input_search__ = ttk.Entry(without_client_transmit_search_things_root)
                without_input_search__.grid(row=1,column=3,columnspan=5)

                ttk.Button(without_client_transmit_search_things_root,text='进行搜索',command=without_client_transmit_search_things).grid(row=2,column=0,columnspan=2)
                ttk.Button(without_client_transmit_search_things_root,text='退出',command=quit_without_client_transmit_search_things).grid(row=3,column=0,columnspan=2)
                without_client_transmit_search_things_root.mainloop()

        inner_ui_version()

    def normal_version():
        logger.info('normal_version running...')
        ask_whether_use_client = str(input('是否使用代理?(回答yes/no) :'))
        try:
            if ask_whether_use_client == 'yes':
                ask_api_source = str(input('在此输入api以提取代理 :'))
                if len(ask_api_source) == 0:
                    logger.error('输入无效!')
                else:
                    ask_api_source_again = str(input(f'确认api无误?当前输入的api为:\n{ask_api_source}:(回答yes/no) :)'))
                    if ask_api_source_again == 'yes':
                        build_client_pool(api_source=ask_api_source)
                        ask_searching_things = str(input('在此输入搜索内容:'))
                        if len(ask_searching_things) == 0:
                            logger.error('搜索内容无效!')
                        else:
                            control_all_tasks(search_here=ask_searching_things, control_mode='with_client')

                    elif ask_api_source_again == 'no':
                        ask_search_things_ = str(input('在此输入搜索内容:'))
                        if len(ask_search_things_) == 0:
                            logger.error('搜索内容无效!')
                        else:
                            control_all_tasks(search_here=ask_search_things_, control_mode='with_client')
                    else:
                        logger.error('回答无效!')

            elif ask_whether_use_client == 'no':
                running = True
                while running:
                    without_client_search_input = str(input('在此输入搜索内容:'))
                    if len(without_client_search_input) != 0:
                        running = False
                        control_all_tasks(search_here=without_client_search_input, control_mode='without_client')
                        logger.info('数据已初步整理成功,,,,,,,')
                        ask_next_proceed = str(input('是否进行进一步处理?:'))
                        if ask_next_proceed == 'yes':
                            ask_tidy_option = str(input('是否使用代理?(yes/no) :)'))
                            if ask_tidy_option == 'yes':
                                further_tidy_up_datas(tidy_mode='with_client')
                            elif ask_tidy_option == 'no':
                                further_tidy_up_datas(tidy_mode='without_client')
                            else:
                                logger.error('回答无效!')
                        elif ask_next_proceed == 'no':
                            ask_stored_now = str(input('是否进行储存? (yes/no) :)'))
                            if ask_stored_now == 'yes':
                                logger.info('储存初始数据中....')
                        else:
                            logger.error('代理回答无效!')
                    else:
                        logger.error('搜索内容输入无效！')
            else:
                logger.error('代理使用回答无效!')

        except Exception as e:
            logger.error(e)

    if choose_frame_mode == 'ui_version':
        ui_version()
    elif choose_frame_mode == 'input_column':
        normal_version()
    else:
        logger.error('模式选择无效!')

if __name__ == '__main__':
    main_running_frame(choose_frame_mode='ui_version')
