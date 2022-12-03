import pandas as pd
from graph_structure import *
import os


def menu():
    os.system("cls")
    print("		     	               欢迎使用课程编排系统	                          \n")
    print(
        "____________________________________________________________________________________________________\n"
    )
    print("			                1. 输入课程信息        			                      \n")
    print(
        "____________________________________________________________________________________________________\n"
    )
    print("	 		                2. 查看上次输入课程信息                		                  \n")
    print(
        "____________________________________________________________________________________________________\n"
    )
    print(
        "        		                3. 根据上次输入信息均匀安排课程                   		                  \n"
    )
    print(
        "____________________________________________________________________________________________________\n"
    )
    print(
        "        		                4. 根据上次输入信息尽快安排课程           			                      \n"
    )
    print(
        "____________________________________________________________________________________________________\n"
    )
    print("        		                5. 关闭程序               			                      \n")
    print(
        "____________________________________________________________________________________________________\n"
    )
    print("\n\t ")
    key = input("请选择您需要的功能：")
    key = int(key)
    if key == 1:
        os.system("cls")
        input_data()
        print("\n\n")
        key = input("按任意键返回主菜单")
    elif key == 2:
        os.system("cls")
        read_data()
        print("\n\n")
        key = input("按任意键返回主菜单")
    elif key == 3:
        G = Graph()
        G.read_file()
        G.top_sort()
        G.arrange(1)
        os.system("cls")
        print("课程安排如下：")
        for i in range(len(G.arrangement)):
            print(f"    第{i+1}学期应上课程为：", end="")
            flag = False
            for j in G.arrangement[i]:
                if flag == False:
                    flag = True
                    print(j, end="")
                else:
                    print(",", j, end="")
            print("")
        print("\n\n")
        key = input("按任意键返回主菜单")
    elif key == 4:
        G = Graph()
        G.read_file()
        G.top_sort()
        G.arrange(2)
        os.system("cls")
        print("课程安排如下：")
        for i in range(len(G.arrangement)):
            print(f"    第{i+1}学期应上课程为：", end="")
            flag = False
            for j in G.arrangement[i]:
                if flag == False:
                    flag = True
                    print(j, end="")
                else:
                    print(",", j, end="")
            print("")
        print("\n\n")
        key = input("按任意键返回主菜单")
    elif key == 5:
        os.system("cls")
        return None
    else:
        os.system("cls")
        key = input("指令无效，按任意键返回主菜单")
    menu()


def input_data():
    basic_info = {}
    basic_info["term num"] = int(input("请输入学期总数："))
    basic_info["credits limit"] = int(input("请输入每学期学分上限："))
    basic_info["course num"] = int(input("请输入课程总数："))
    df_info = pd.DataFrame(basic_info, index=[0])
    df_info.to_json(path_or_buf=r"course_arrangement\basic_info.json", orient="records")
    course_info = {"id": [], "credits": [], "previous": []}
    print("请依次输入课程ID，课程学分，需先修课程ID（结束时请输入-1）:")
    course = ""
    couse_list = []
    while True:
        course_info = {}
        course = input()
        if course == "-1":
            break
        info_list = course.split(",")
        if len(info_list) == 3:
            course_info["id"] = info_list[0]
            course_info["credits"] = info_list[1]
            course_info["previous"] = info_list[2]
        else:
            course_info["id"] = info_list[0]
            course_info["credits"] = info_list[1]
            course_info["previous"] = "NULL"
        couse_list.append(course_info.copy())
    df_course = pd.DataFrame(couse_list)
    df_course.to_csv(path_or_buf=r"course_arrangement\course_info.csv")
    return None


def read_data():
    df = pd.read_csv(r"course_arrangement\course_info.csv")
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    df.fillna("无", inplace=True)
    print("课程ID    学分    先修课程")
    for i in range(len(df.index)):
        print(f"{df.iloc[i,0]}         {df.iloc[i,1]}         {df.iloc[i,2]}")


if __name__ == "__main__":
    menu()
