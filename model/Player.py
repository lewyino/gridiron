
class Player:

    def __init__(self, id, name, bpos, age, rating, energy, wage, health):
        self.id = int(id)
        self.name = name
        self.bpos = bpos
        self.age = age
        self.rating = rating
        self.energy = energy
        self.wage = int(str(wage).replace(',', ''))
        self.health = health

    def __setattr__(self, *args, **kwargs):
        return super().__setattr__(*args, **kwargs)

    def __getattribute__(self, *args, **kwargs):
        try:
            if args[0] in ('rating', 'experience', 'talent', 'teamChemistry'):
                return super().__getattribute__(*args, **kwargs) / 2
            return super().__getattribute__(*args, **kwargs)
        except:
            if args[0] in ('name', 'bpos', 'wage', 'health'):
                return ''
            else:
                return 0

    def __str__(self):
        return 'id: %d\n' \
               'name: %s\n' \
               'bpos: %s\n' \
               'age: %d\n' \
               'rating: %.1f*\n' \
               'energy: %d%%\n' \
               'wage: %d$\n' \
               'health: %s\n' \
               'experience: %.1f*\n' \
               'talent: %.1f*\n' \
               'teamChemistry: %.1f*\n' \
               'skills: %s\n' \
               'weight: %d\n' \
               'height: %d\n' \
               'bmi: %.1f\n' \
               'teamwork: %d\n' \
               'consistency: %d\n' \
               'weeks at club: %d\n' \
               'last update week: %d' % \
               (
                   self.id,
                   self.name,
                   self.bpos,
                   self.age,
                   self.rating,
                   self.energy,
                   self.wage,
                   self.health,
                   self.experience,
                   self.talent,
                   self.teamChemistry,
                   self.skills_list,
                   self.weight,
                   self.height,
                   self.bmi,
                   self.teamwork,
                   self.consistency,
                   self.weeks_at_club,
                   self.last_update_week
               )

    def __repr__(self):
        return self.__str__()

    def update_stars_data(self, stars_list):
        self.experience = float(stars_list[1])
        self.talent = float(stars_list[2])
        self.teamChemistry = float(stars_list[3])

    def update_skills_data(self, skills_list):
        self.skills_list = skills_list
        if len(skills_list) >= 15:
            self.positioning = int(skills_list[0])
            self.passing = int(skills_list[1])
            self.tackling = int(skills_list[2])
            self.speed = int(skills_list[3])
            self.vision = int(skills_list[4])
            self.catching = int(skills_list[5])
            self.blocking = int(skills_list[6])
            self.strength = int(skills_list[7])
            self.intelligence = int(skills_list[8])
            self.carrying = int(skills_list[9])
            self.kicking = int(skills_list[10])
            self.agility = int(skills_list[11])
            self.aggression = int(skills_list[12])
            self.footwork = int(skills_list[13])
            self.punting = int(skills_list[14])
            self.stamina = int(skills_list[15])

    def update_size_data(self, size_list):
        self.size_list = size_list
        self.weight = int(size_list[0])
        self.height = int(size_list[1])
        self.bmi = float(size_list[2])

    def update_other_data(self, other_list):
        self.other_list = other_list
        self.teamwork = int(other_list[0])
        self.consistency = int(other_list[1])
        self.weeks_at_club = int(other_list[2])

    @classmethod
    def convert_from_tuple(cls, tuple_data):
        player = cls(
            tuple_data[0],
            tuple_data[1],
            tuple_data[2],
            tuple_data[3],
            tuple_data[4] * 2,
            tuple_data[5],
            tuple_data[6],
            tuple_data[7]
        )
        player.experience = tuple_data[8] * 2
        player.talent = tuple_data[9] * 2
        player.teamChemistry = tuple_data[10] * 2
        player.positioning = tuple_data[11]
        player.passing = tuple_data[12]
        player.tackling = tuple_data[13]
        player.speed = tuple_data[14]
        player.vision = tuple_data[15]
        player.catching = tuple_data[16]
        player.blocking = tuple_data[17]
        player.strength = tuple_data[18]
        player.intelligence = tuple_data[19]
        player.carrying = tuple_data[20]
        player.kicking = tuple_data[21]
        player.agility = tuple_data[22]
        player.aggression = tuple_data[23]
        player.footwork = tuple_data[24]
        player.punting = tuple_data[25]
        player.stamina = tuple_data[26]
        player.weight = tuple_data[27]
        player.height = tuple_data[28]
        player.bmi = tuple_data[29]
        player.teamwork = tuple_data[30]
        player.consistency = tuple_data[31]
        player.weeks_at_club = tuple_data[32]
        player.last_update_week = tuple_data[33]
        return player

    def print_player_difference(self, player, verbose: bool = True):
        if player is not None:
            diff = self.__print_basic_data_difference(player)
            diff += self.get_skills_difference(player)
            if diff is not None and len(diff) > 0 and verbose:
                print('print player difference %s' % (self.name,))
                print(diff)
        else:
            if verbose:
                print('new player')
                print(self)

    def __print_basic_data_difference(self, player, with_bmi: bool = False):
        diff = ''
        if self.bpos != player.bpos:
            diff += ("difference bpos: %s => %s\n" % (player.bpos, self.bpos))
        if self.age != player.age:
            diff += ("difference age: %d => %d\n" % (player.age, self.age))
        if self.rating != player.rating:
            diff += ("difference rating: %.1f => %.1f\n" % (player.rating, self.rating))
        if self.energy != player.energy:
            diff += ("difference energy: %s => %s\n" % (player.energy, self.energy))
        if self.wage != player.wage:
            diff += ("difference wage: %s => %s\n" % (player.wage, self.wage))
        if self.health != player.health:
            diff += ("difference health: %s => %s\n" % (player.health, self.health))
        if self.experience != player.experience:
            diff += ("difference experience: %.1f => %.1f\n" % (player.experience, self.experience))
        if self.teamChemistry != player.teamChemistry:
            diff += ("difference teamChemistry: %.1f => %.1f\n" % (player.teamChemistry, self.teamChemistry))
        if self.weight != player.weight:
            diff += ("difference weight: %d => %d\n" % (player.weight, self.weight))
        if self.height != player.height:
            diff += ("difference height: %d => %d\n" % (player.height, self.height))
        if with_bmi and self.bmi != player.bmi:
            diff += ("difference bmi: %.1f => %.1f\n" % (player.bmi, self.bmi))
        return diff

    def get_skills_difference(self, player):
        diff = ''
        if self.positioning != player.positioning:
            diff += "difference positing: %d => %d (%d)\n" % (player.positioning, self.positioning, self.positioning - player.positioning)
        if self.passing != player.passing:
            diff += ("difference passing: %d => %d (%d)\n" % (player.passing, self.passing, self.passing - player.passing))
        if self.tackling != player.tackling:
            diff += ("difference tackling: %d => %d (%d)\n" % (player.tackling, self.tackling, self.tackling - player.tackling))
        if self.speed != player.speed:
            diff += ("difference speed: %d => %d (%d)\n" % (player.speed, self.speed, self.speed - player.speed))
        if self.vision != player.vision:
            diff += ("difference vision: %d => %d (%d)\n" % (player.vision, self.vision, self.vision - player.vision))
        if self.catching != player.catching:
            diff += ("difference catching: %d => %d (%d)\n" % (player.catching, self.catching, self.catching - player.catching))
        if self.blocking != player.blocking:
            diff += ("difference blocking: %d => %d (%d)\n" % (player.blocking, self.blocking, self.blocking - player.blocking))
        if self.strength != player.strength:
            diff += ("difference strength: %d => %d (%d)\n" % (player.strength, self.strength, self.strength - player.strength))
        if self.intelligence != player.intelligence:
            diff += ("difference intelligence: %d => %d (%d)\n" % (player.intelligence, self.intelligence, self.intelligence - player.intelligence))
        if self.carrying != player.carrying:
            diff += ("difference carrying: %d => %d (%d)\n" % (player.carrying, self.carrying, self.carrying - player.carrying))
        if self.kicking != player.kicking:
            diff += ("difference kicking: %d => %d (%d)\n" % (player.kicking, self.kicking, self.kicking - player.kicking))
        if self.agility != player.agility:
            diff += ("difference agility: %d => %d (%d)\n" % (player.agility, self.agility, self.agility - player.agility))
        if self.aggression != player.aggression:
            diff += ("difference aggression: %d => %d (%d)\n" % (player.aggression, self.aggression, self.aggression - player.aggression))
        if self.footwork != player.footwork:
            diff += ("difference footwork: %d => %d (%d)\n" % (player.footwork, self.footwork, self.footwork - player.footwork))
        if self.punting != player.punting:
            diff += ("difference punting: %d => %d (%d)\n" % (player.punting, self.punting, self.punting - player.punting))
        if self.stamina != player.stamina:
            diff += ("difference stamina: %d => %d (%d)\n" % (player.stamina, self.stamina, self.stamina - player.stamina))
        return diff

    def calculate_best_position(self, with_talent: bool = False):
        qb_points = self.__calculate_qb_points(with_talent)
        bpos = 'QB %.1f' % (qb_points,)
        bpos_point = qb_points
        rb_point = self.__calculate_rb_points(with_talent)
        if rb_point > bpos_point:
            bpos = 'RB %.1f' % (rb_point,)
            bpos_point = rb_point
        wr_point = self.__calculate_wr_points(with_talent)
        if wr_point > bpos_point:
            bpos = 'WR %.1f' % (wr_point,)
            bpos_point = wr_point
        te_point = self.__calculate_te_points(with_talent)
        if te_point > bpos_point:
            bpos = 'TE %.1f' % (te_point,)
            bpos_point = te_point
        ol_point = self.__calculate_ol_points(with_talent)
        if ol_point > bpos_point:
            bpos = 'OL %.1f' % (ol_point,)
            bpos_point = ol_point
        dl_point = self.__calculate_dl_points(with_talent)
        if dl_point > bpos_point:
            bpos = 'DL %.1f' % (dl_point,)
            bpos_point = dl_point
        de_point = self.__calculate_de_points(with_talent)
        if de_point > bpos_point:
            bpos = 'DE %.1f' % (de_point,)
            bpos_point = de_point
        mlb_point = self.__calculate_mlb_points(with_talent)
        if mlb_point > bpos_point:
            bpos = 'MLB %.1f' % (mlb_point,)
            bpos_point = mlb_point
        olb_point = self.__calculate_olb_points(with_talent)
        if olb_point > bpos_point:
            bpos = 'OLB %.1f' % (olb_point,)
            bpos_point = olb_point
        cb_point = self.__calculate_cb_points(with_talent)
        if cb_point > bpos_point:
            bpos = 'CB %.1f' % (cb_point,)
            bpos_point = cb_point
        sf_point = self.__calculate_sf_points(with_talent)
        if sf_point > bpos_point:
            bpos = 'SF %.1f' % (sf_point,)
            bpos_point = sf_point
        k_point = self.__calculate_k_points(with_talent)
        if k_point > bpos_point:
            bpos = 'K %.1f' % (k_point,)
        return bpos

    def __calculate_qb_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += ((self.intelligence if self.intelligence >= 15 else self.intelligence - 5) * 4)
        max_point += 20 * 4
        point += self.consistency * 4
        max_point += 20 * 4
        point += self.passing * 3
        max_point += 20 * 3
        point += self.vision * 2
        max_point += 20 * 2
        point += self.agility
        point += self.footwork
        point += self.strength
        max_point += 60
        self.qb_point = float(point) / max_point * 100
        return self.qb_point

    def __calculate_rb_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += self.speed * 3
        max_point += 20 * 3
        point += self.strength * 3
        max_point += 20 * 3
        point += self.carrying * 2
        max_point += 20 * 2
        point += self.blocking * 2
        max_point += 20 * 2
        point += self.agility * 2
        max_point += 20 * 2
        point += self.footwork
        max_point += 20
        self.rb_point = float(point) / max_point * 100
        return self.rb_point

    def __calculate_wr_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += self.speed * 4
        max_point += 20 * 4
        point += self.strength
        max_point += 20
        point += self.catching * 3
        max_point += 20 * 3
        point += self.agility * 2
        max_point += 20 * 2
        point += self.footwork * 2
        max_point += 20 * 2
        point += self.positioning * 2
        max_point += 20 * 2
        point += self.vision
        max_point += 20
        self.wr_point = float(point) / max_point * 100
        return self.wr_point

    def __calculate_te_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += self.speed * 4
        max_point += 20 * 4
        point += self.strength * 4
        max_point += 20 * 4
        point += self.catching * 3
        max_point += 20 * 3
        point += self.blocking * 3
        max_point += 20 * 3
        point += self.agility * 2
        max_point += 20 * 2
        point += self.positioning * 2
        max_point += 20 * 2
        self.te_point = float(point) / max_point * 100
        return self.te_point

    def __calculate_ol_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += self.strength * 4
        max_point += 20 * 4
        point += self.speed
        max_point += 20
        point += self.blocking * 3
        max_point += 20 * 3
        point += self.footwork * 2
        max_point += 20 * 2
        point += self.vision * 2
        max_point += 20 * 2
        point += self.agility
        max_point += 20
        self.ol_point = float(point) / max_point * 100
        return self.ol_point

    def __calculate_dl_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += self.strength * 4
        max_point += 20 * 4
        point += self.tackling * 3
        max_point += 20 * 3
        point += self.vision * 2
        max_point += 20 * 2
        point += self.positioning * 2
        max_point += 20 * 2
        point += self.agility * 2
        max_point += 20 * 2
        point += self.footwork
        max_point += 20
        self.dl_point = float(point) / max_point * 100
        return self.dl_point

    def __calculate_de_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += self.strength * 4
        max_point += 20 * 4
        point += self.speed * 3
        max_point += 20 * 3
        point += self.tackling * 3
        max_point += 20 * 3
        point += self.vision * 2
        max_point += 20 * 2
        point += self.positioning * 2
        max_point += 20 * 2
        point += self.agility * 2
        max_point += 20 * 2
        point += self.footwork
        max_point += 20
        self.de_point = float(point) / max_point * 100
        return self.de_point

    def __calculate_mlb_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += self.intelligence * 4
        max_point += 20 * 4
        point += self.strength * 4
        max_point += 20 * 4
        point += self.speed
        max_point += 20
        point += self.tackling * 3
        max_point += 20 * 3
        point += self.vision * 2
        max_point += 20 * 2
        point += self.positioning * 2
        max_point += 20 * 2
        point += self.agility * 2
        max_point += 20 * 2
        point += self.footwork
        max_point += 20
        self.mlb_point = float(point) / max_point * 100
        return self.mlb_point

    def __calculate_olb_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += self.strength * 4
        max_point += 20 * 4
        point += self.speed * 3
        max_point += 20 * 3
        point += self.tackling * 3
        max_point += 20 * 3
        point += self.vision * 2
        max_point += 20 * 2
        point += self.positioning * 2
        max_point += 20 * 2
        point += self.agility * 2
        max_point += 20 * 2
        point += self.footwork
        max_point += 20
        self.olb_point = float(point) / max_point * 100
        return self.olb_point

    def __calculate_cb_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += self.speed * 4
        max_point += 20 * 4
        point += self.strength
        max_point += 20
        point += self.tackling * 3
        max_point += 20 * 3
        point += self.agility * 2
        max_point += 20 * 2
        point += self.vision * 2
        max_point += 20 * 2
        point += self.positioning * 2
        max_point += 20 * 2
        point += self.footwork
        point += self.catching
        max_point += 40
        self.cb_point = float(point) / max_point * 100
        return self.cb_point

    def __calculate_sf_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += self.speed * 3
        max_point += 20 * 3
        point += self.strength * 3
        max_point += 20 * 3
        point += self.intelligence * 3
        max_point += 20 * 3
        point += self.tackling * 3
        max_point += 20 * 3
        point += self.agility * 2
        max_point += 20 * 2
        point += self.vision * 2
        max_point += 20 * 2
        point += self.positioning * 2
        max_point += 20 * 2
        point += self.footwork
        max_point += 20
        self.sf_point = float(point) / max_point * 100
        return self.sf_point

    def __calculate_k_points(self, with_talent: bool = False):
        point = 1
        max_point = 1
        if with_talent:
            point += self.talent * 4
            max_point += 20
        point += self.intelligence * 4
        max_point += 20 * 4
        point += self.consistency * 4
        max_point += 20 * 3
        point += self.kicking * 3
        max_point += 20 * 4
        point += self.punting * 3
        max_point += 20 * 4
        point += self.strength
        max_point += 20
        self.k_point = float(point) / max_point * 100
        return self.k_point
