import pymysql


class down_db():
    def __init__(self):
        self.connent_sql()
        self.create_table()

    def __del__(self):
        self.connect.commit()
        self.close_db()

    def connent_sql(self):
        self.connect = pymysql.Connect(host = 'localhost',user = 'root',password = 'root',database = 'qianmu',charset = 'utf8')
        self.cur = self.connect.cursor()

    def create_table(self):
        sql = 'create table if not EXISTS qianmu_table(id INTEGER PRIMARY KEY auto_increment,' \
              '学校名称 VARCHAR (100),排名 VARCHAR (100),国家 VARCHAR (100),' \
              '州省 VARCHAR (100),城市 VARCHAR (100),' \
              '校训 VARCHAR (100),汉译 VARCHAR (100),' \
              '性质 VARCHAR (100),成立年份 VARCHAR (100),' \
              '宗教信仰 VARCHAR (100),校园 VARCHAR (100),' \
              '学生人数 VARCHAR (100),本科生人数 VARCHAR (100),' \
              '研究生人数 VARCHAR (100),师生比 VARCHAR (100),' \
              '国际学生比例 VARCHAR (100),学校分类 VARCHAR (100),' \
              '学校集团 VARCHAR (100),认证机构 VARCHAR (100),网址 VARCHAR (100));'
        self.cur.execute(sql)

    def insert_tabale(self,school,it):
        print(school)
        print('----------------------------------------------')
        print(it)

        sql = "insert into qianmu_table VALUES (0,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}'," \
              "'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(school,it[0],it[1],it[2],it[3],it[4],it[5],it[6],it[7],it[8],it[9],it[10],
                                                                     it[11],it[12],it[13],it[14],it[15],it[16],it[17],it[18])

        self.cur.execute(sql)

    def close_db(self):
        self.connect.close()
