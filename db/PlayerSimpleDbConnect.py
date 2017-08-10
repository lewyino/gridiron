import sqlite3

from model.Player import *


class PlayerSimpleDbConnect:
    __table_name = 'player'
    __conn = None
    __cursor = None

    def __init__(self, table_name: str = None):
        if table_name is not None:
            self.__table_name = table_name
        self.create_connection()

    def create_connection(self):
        try:
            conn = sqlite3.connect('sqlite_database.db')
            cursor = conn.cursor()
            cursor.execute('SELECT SQLITE_VERSION()')
            data = cursor.fetchone()
            print("Database connected! SQLite version: %s" % data)
            query = 'CREATE TABLE IF NOT EXISTS %s ' \
                    '(id INT, name TEXT, bpos REAL, age INT, rating REAL, energy INT, wage TEXT, ' \
                    'health TEXT, experience REAL, talent REAL, teamChemistry REAL, ' \
                    'positioning INT, passing INT, tackling INT, speed INT, ' \
                    'vision INT, catching INT, blocking INT, strength INT, ' \
                    'intelligence INT, carrying INT, kicking INT, agility INT, ' \
                    'aggression INT, footwork INT, punting INT, stamina INT, ' \
                    'weight INT, height REAL, bmi REAL, ' \
                    'teamwork INT, consistency INT, weeksAtClub INT, ' \
                    'myBpos TEXT, qbPoint REAL, rbPoint REAL, wrPoint REAL, tePoint REAL, olPoint REAL, ' \
                    'dlPoint REAL, dePoint REAL, mlbPoint REAL, olbPoint REAL, cbPoint REAL, sfPoint REAL, kPoint REAL)'\
                    % self.__table_name
            cursor.execute(query)
            self.__conn = conn
            self.__cursor = cursor
        except:
            print("Error: Unable to connect to SQLite")
            conn.close()
            exit(1)

    def save_player(self, player: Player, verbose: bool = False):
        result = False
        if self.check_is_player_exist(player):
            if self.check_is_player_updated(player):
                if verbose:
                    print('player updated! nothing to do')
            else:
                if verbose:
                    print('player exist, add new player data')
                result = self.__add_player(player)
        else:
            if verbose:
                print('player not exist, add player')
            result = self.__add_player(player)
        self.__conn.commit()
        return result

    def __add_player(self, player: Player):
        player_as_tuple = (player.id, player.name, player.bpos, player.age, player.rating, player.energy, player.wage, player.health, player.experience, player.talent, player.teamChemistry,
                          player.positioning, player.passing, player.tackling, player.speed,
                          player.vision, player.catching, player.blocking, player.strength,
                          player.intelligence, player.carrying, player.kicking, player.agility,
                          player.aggression, player.footwork, player.punting, player.stamina,
                          player.weight, player.height, player.bmi,
                          player.teamwork, player.consistency, player.weeks_at_club,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, player.last_update_week)
        query = 'INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)' % self.__table_name
        try:
            self.__cursor.execute(query, player_as_tuple)
            return True
        except Exception as error:
            print(error)
            return False

    def check_is_player_exist(self, player: Player):
        query = 'SELECT COUNT(*) FROM %s WHERE id=:id' % self.__table_name
        self.__cursor.execute(query, {'id': player.id})
        exist = self.__cursor.fetchone()
        return True if exist[0] > 0 else False

    def check_is_player_updated(self, player: Player):
        query = 'SELECT COUNT(*) FROM %s WHERE id = :id AND weeksAtClub = :wac' % self.__table_name
        self.__cursor.execute(query, {'id': player.id, 'wac': player.weeks_at_club})
        exist = self.__cursor.fetchone()
        return True if exist[0] > 0 else False

    def get_count_players_in_db(self):
        query = 'SELECT COUNT(*) FROM %s' % self.__table_name
        self.__cursor.execute(query)
        return self.__cursor.fetchone()[0]

    def get_player(self, player_id: int, player_week_at_club: int = None):
        if player_week_at_club is None:
            player_as_tuple = self.__get_last_player_data(player_id)
        else:
            player_as_tuple = self.__get_player_data_from_week_at_club(player_id, player_week_at_club)
        return None if player_as_tuple is None else Player.convert_from_tuple(player_as_tuple)

    def __get_last_player_data(self, player_id: int):
        query = 'SELECT * FROM %s WHERE id = :id ORDER BY weeksAtClub DESC' % self.__table_name
        self.__cursor.execute(query, {'id': player_id})
        exist = self.__cursor.fetchone()
        return exist if exist is not None and exist[0] is not None and exist[0] > 0 else None

    def __get_player_data_from_week_at_club(self, player_id: int, player_week_at_club: int):
        query = 'SELECT * FROM %s WHERE id = :id AND weeksAtClub = :wac' % self.__table_name
        self.__cursor.execute(query, {'id': player_id, 'wac': player_week_at_club})
        exist = self.__cursor.fetchone()
        return exist if exist is not None and exist[0] is not None and exist[0] > 0 else None

    def get_all_players(self):
        query = 'SELECT * FROM %s GROUP BY id' % self.__table_name
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def save_player_calculated_bpos(self, player: Player):
        try:
            query = 'UPDATE %s SET qbPoint = :qb_point, ' \
                    'rbPoint = :rb_point, ' \
                    'wrPoint = :wr_point, ' \
                    'tePoint = :te_point, ' \
                    'olPoint = :ol_point, ' \
                    'dlPoint = :dl_point, ' \
                    'dePoint = :de_point, ' \
                    'mlbPoint = :mlb_point, ' \
                    'olbPoint = :olb_point, ' \
                    'cbPoint = :cb_point, ' \
                    'sfPoint = :sf_point, ' \
                    'kPoint = :k_point ' \
                    'WHERE id = :id AND weeksAtClub = :wac' % self.__table_name
            data = dict(
                qb_point = round(player.qb_point, 1),
                rb_point = round(player.rb_point, 1),
                wr_oint = round(player.wr_point, 1),
                te_toint = round(player.te_point, 1),
                ol_point = round(player.ol_point, 1),
                dl_point = round(player.dl_point, 1),
                de_point = round(player.de_point, 1),
                mlb_point = round(player.mlb_point, 1),
                olb_point = round(player.olb_point, 1),
                cb_point = round(player.cb_point, 1),
                sf_point = round(player.sf_point, 1),
                k_point = round(player.k_point, 1),
                id = player.id,
                wac = player.weeks_at_club
            )
            self.__cursor.execute(query, data)
            self.__conn.commit()
            return True
        except Exception as error:
            print(error)
            return False

    def get_best_qb_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY qbPoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_rb_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY rbPoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_wr_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY wrPoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_te_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY tePoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_ol_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY olPoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_dl_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY dlPoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_de_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY dePoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_mlb_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY mlbPoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_olb_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY olbPoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_cb_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY cbPoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_sf_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY sfPoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_k_players(self, players_quantity: int = 5):
        query = 'SELECT * FROM %s GROUP BY id ORDER BY kPoint DESC LIMIT %d' % (self.__table_name, players_quantity)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_players_with_potential(
            self,
            min_talent: float = 3.5,
            min_teamwork: int = 10,
            min_consistency: int = 10,
            max_age: int = None
    ):
        if max_age is not None:
            query = 'SELECT * FROM %s ' \
                    'WHERE talent >= :talent AND teamwork >= :teamwork AND consistency >= :consistency AND age <= :age ' \
                    'GROUP BY id' \
                    % (self.__table_name,)
        else:
            query = 'SELECT * FROM %s ' \
                    'WHERE talent >= :talent AND teamwork >= :teamwork AND consistency >= :consistency ' \
                    'GROUP BY id' \
                    % (self.__table_name,)
        data = dict(
            talent = min_talent,
            teamwork = min_teamwork,
            consistency = min_consistency,
            age = max_age
        )
        self.__cursor.execute(query, data)
        return self.__cursor.fetchall()

    def get_best_players_by_position(self, position: str, players_number: int):
        query = 'SELECT * FROM %s ' \
                'GROUP BY id ' \
                'ORDER BY %sPoint ' \
                'DESC LIMIT %d' \
                % (self.__table_name, position, players_number)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_best_players_by_skill(self, skill: str, min_skill_value: int):
        query = 'SELECT * FROM %s ' \
                'WHERE %s >= %d ' \
                'GROUP BY id ' \
                'ORDER BY %s DESC' \
                % (self.__table_name, skill, min_skill_value, skill)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()
