from peewee import PostgresqlDatabase, Model, IntegerField, DoesNotExist

db = PostgresqlDatabase(
	database="desi4lmj6vf82b",
    user="gxvrzprwhagkea",
    password="cc0a33aae4731056843a323d7c803f8573cbf4fa08fc8a711db3b697e1da154b",
    host="ec2-54-225-96-191.compute-1.amazonaws.com",
    port=5432
)

class Person(Model):
    user_id = IntegerField()
    count_messages = IntegerField()
    class Meta:
        database = db

Person.create_table()

class Worker():
    def __init__(self, bot):
        self._bot = bot

    def Counter(self, _user_id):
        try:
            p = Person.get(user_id=_user_id)
            p.count_messages += 1
            p.save()
        except DoesNotExist:
            Person.create(user_id=_user_id, count_messages=1)
        except Exception as ex:
            self._bot.send_message(497551952, str(ex))

    def CurrentWord(self, number):
        iy = ['11', '12', '13', '14', '5', '6', '7', '8', '9', '0']
        if number.endswith('1'):
            return "сообщение"
        elif number.endswith('2') or number.endswith('3') or number.endswith('4'):
            return "сообщения"
        else:
            for i in range(len(iy)):
                if iy[i] in number:
                    return "сообщений"

    def SendStat(self, chat_id):
        stat = ""
        iter = 0
        for one in Person.select().order_by(Person.count_messages.desc()).limit(10):
            try:
                _user = self._bot.get_chat_member(-1001257615874, one.user_id)
                name = "@" + _user.user.username if _user.user.username != None else _user.user.first_name
                if iter == 0: 
                    stat += f"🥇{name} - {one.count_messages}\n"
                    iter += 1
                elif iter == 1:
                    stat += f"🥈{name} - {one.count_messages}\n"
                    iter += 1
                elif iter == 2:
                    stat += f"🥉{name} - {one.count_messages}\n"
                    iter += 1
                else:
                    stat += f"     {name} - {one.count_messages}\n"
            except Exception as ex:
                stat += f"~outgoing - {one.count_messages}\n"
                iter += 1
        total = 0
        for i in Person.select():
            total += i.count_messages
        
        letter = ""
        if total != 0:
            letter = "Вот и подошла к концу ещё одна неделя! И вот вам немного статистики:\n\n<i>Самые активные участники:</i>\n{}\nА всего было напечатано <b>{}</b> {}!\n\nУдачи в наступающей неделе!😉".format(stat, total, self.CurrentWord(str(total)))
        else:
            letter = "Чёт на этой неделе было тихо😔"
        self._bot.send_message(-1001257615874, letter, parse_mode="HTML")

    def ClearDB(self, chat_id):
        persons = Person.select()
        for person in persons:
            person.delete_instance()
        self._bot.send_message(chat_id, "Таблица очищена")

    def StatCommand(self):
        total = 0
        for i in Person.select():
            total += i.count_messages
        self._bot.send_message(497551952, "Всего: " + str(total))