import math


class Aircraft:
    def __init__(self, kwargs, canvas):
        self.canvas = canvas
        print(kwargs)
        # self.flight_no = kwargs["flight_no"]
        # self.alt = kwargs["initial_alt"]
        # self.tgt_alt = kwargs["initial_alt"]
        self.speed = kwargs["speed"]
        # self.tgt_speed = kwargs["speed"]
        self.heading = kwargs["heading"]
        # self.tgt_heading = kwargs["heading"]
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        # self.aircraft = kwargs["aircraft"]
        # self.airport = kwargs["airport"]
        # self.icon_id = kwargs["icon_id"]
        # self.tag_id = kwargs["tag_id"]
        # self.objective = kwargs["objective"]
        # self.bound = kwargs["bound"]

        self.fill = kwargs["fill"]
        self.size = kwargs["size"]

        self.icon_id = None
        self.tag_id = None
        self._create_symbol()
        self._create_tag()
        # self.collision = "black"
        # self.new_orange = False
        # self.new_red = False
        # self.visibility = visibility
        # self.moving = moving
        # self.on_ground = on_ground
        # self.points = 100
        # self.ils_status = "off"
        # self.ils_runway = None
        # self.distance_to_runway = 0
        # self.relative_angle_to_runway = 0
        # self.landing = False
        # self.previous_x = [-1] * 10
        # self.previous_y = [-1] * 10
        # self.last_pos_id = [-1] * 10
        # self.dep_wpt_x = dep_wpt_x
        # self.dep_wpt_y = dep_wpt_y

        self.displacement_x = 0
        self.displacement_y = 0

    # def _compute_initial_state(self):
    #
    # def _compute_initial_altitude

    def _create_symbol(self):
        self.icon_id = self.canvas.create_rectangle(
            self.x-self.size,
            self.y-self.size,
            self.x+self.size,
            self.y+self.size,
            fill=self.fill,
            outline=self.fill
        )

    def _create_tag(self):
        # txt = self.flight_no+"\n"+self.aircraft+" "+self.airport+"\n"+str(self.alt)+" "+str(self.tgt_alt)+"\n"+str(self.speed)+" "+str(self.tgt_speed)
        self.tag_id = self.canvas.create_text(
            self.x-23,
            self.y-20,
            fill=self.fill,
            font="Arial 8",
            text=self._get_tag_text()
        )

        # eval_label = lambda x, y, z: (lambda p: self.add_callsign_to_prompt(x, y, z))
        # game_vars.canvas.tag_bind(tag_id, "<Button-1>", eval_label(self, self.flight_no, cmd_prompt))

    def update(self):
        self._update_state_variables()
        self._update_tag_text()

        self._move()

    def _update_state_variables(self):
        self._compute_displacement()
        self._compute_new_position()

    def _update_tag_text(self):
        self.canvas.itemconfigure(self.tag_id, text=self._get_tag_text(), fill=self.fill)

    def _compute_displacement(self):
        self.displacement_x = self.speed * math.sin(math.pi * self.heading / 180.0)
        self.displacement_y = self.speed * math.cos(math.pi * self.heading / 180.0)

    def _compute_new_position(self):
        self.x += self.displacement_x
        self.y += self.displacement_y

    def _move(self):
        self.canvas.move(self.icon_id, self.displacement_x, self.displacement_y)
        self.canvas.move(self.tag_id, self.displacement_x, self.displacement_y)

    def _get_tag_text(self) -> str:
        return f"{self.x}_{self.y}"
