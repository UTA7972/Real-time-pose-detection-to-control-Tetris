import copy
import random
import tkinter

class block_type:
    def __init__(self, cell):
        self.tags = ["tag1", "tag2", "tag3", "tag4"]
        self.cell = cell

    def gen(self):
        a = random.randrange(0, 7)
        self.cnt = 0
        if a == 0:
            self.block = [[4, 0, "tag1"], [4, -1, "tag2"], [4, -2, "tag3"], [4, -3, "tag4"]]
            self._round = [
                {"tag1": [1, -1], "tag2": [0, 0], "tag3": [-1, 1], "tag4": [-2, 2]},
                {"tag1": [-1, 1], "tag2": [0, 0], "tag3": [1, -1], "tag4": [2, -2]},
            ]
        elif a == 1:
            self.block = [[4, 0, "tag1"], [4, -1, "tag2"], [3, -1, "tag3"], [5, -1, "tag4"]]
            self._round = [
                {"tag1": [1, -1], "tag2": [0, 0], "tag3": [1, 1], "tag4": [-1, -1]},
                {"tag1": [-1, -1], "tag2": [0, 0], "tag3": [1, -1], "tag4": [-1, 1]},
                {"tag1": [-1, 1], "tag2": [0, 0], "tag3": [-1, -1], "tag4": [1, 1]},
                {"tag1": [1, 1], "tag2": [0, 0], "tag3": [-1, 1], "tag4": [1, -1]},
            ]
        elif a == 2:
            self.block = [[4, 0, "tag1"], [3, 0, "tag2"], [4, -1, "tag3"], [3, -1, "tag4"]]
            self._round = [
                {"tag1": [0, 0], "tag2": [0, 0], "tag3": [0, 0], "tag4": [0, 0]},
            ]
        elif a == 3:
            self.block = [[4, 0, "tag1"], [4, -1, "tag2"], [5, -1, "tag3"], [5, -2, "tag4"]]
            self._round = [
                {"tag1": [0, 0], "tag2": [0, 0], "tag3": [-2, 0], "tag4": [0, 2]},
                {"tag1": [0, 0], "tag2": [0, 0], "tag3": [2, 0], "tag4": [0, -2]},
            ]
        elif a == 4:
            self.block = [[4, 0, "tag1"], [4, -1, "tag2"], [3, -1, "tag3"], [3, -2, "tag4"]]
            self._round = [
                {"tag1": [0, -2], "tag2": [0, 0], "tag3": [0, 0], "tag4": [2, 0]},
                {"tag1": [0, 2], "tag2": [0, 0], "tag3": [0, 0], "tag4": [-2, 0]},
            ]
        elif a == 5:
            self.block = [[4, 0, "tag1"], [4, -1, "tag2"], [4, -2, "tag3"], [3, -2, "tag4"]]
            self._round = [
                {"tag1": [0, 0], "tag2": [0, 0], "tag3": [-2, 2], "tag4": [0, 2]},
                {"tag1": [0, 0], "tag2": [0, 0], "tag3": [2, -2], "tag4": [2, 0]},
                {"tag1": [0, 0], "tag2": [0, 0], "tag3": [2, 1], "tag4": [0, -1]},
                {"tag1": [0, 0], "tag2": [0, 0], "tag3": [-2, -1], "tag4": [-2, -1]},
            ]
        else:
            self.block = [[4, 0, "tag1"], [4, -1, "tag2"], [4, -2, "tag3"], [5, -2, "tag4"]]
            self._round = [
                {"tag1": [-1, -2], "tag2": [0, 0], "tag3": [0, 0], "tag4": [-3, 0]},
                {"tag1": [0, 1], "tag2": [0, 0], "tag3": [0, 0], "tag4": [2, -1]},
                {"tag1": [2, 0], "tag2": [0, 0], "tag3": [0, 0], "tag4": [2, 2]},
                {"tag1": [1, -1], "tag2": [0, 0], "tag3": [0, 0], "tag4": [-1, -1]},
            ]

        for i in range(len(self._round)):
            for tag in self.tags:
                for n in range(2):
                    self._round[i][tag][n] = self._round[i][tag][n]*self.cell

        return self.block

    def gen_round(self):
        self.round = self._round[self.cnt % len(self._round)]
        return self.round

    def gen_ok(self):
        self.cnt += 1


class tetris_class:
    def __init__(self):
        self.app = tkinter.Tk()
        self.app.title("Tetris")

        self.start_button = tkinter.Button(
            self.app,
            text = "Start",
            fg = "black",
            command = self.click_button,
        )
        self.start_button.pack()

        self.height_num, self.width_num = 20, 10
        self.cell = 20
        self._offset_w, self._offset_h, = 100, 100
        self._width = self._offset_w*2 + self.cell*self.width_num
        self._height = self._offset_h*2 + self.cell*self.height_num
        self.toggle = False
        self.block_exist_pos = []

        self.blocks = block_type(self.cell)

        self.canvas = tkinter.Canvas(
            self.app,
            width=self._width,
            height=self._height,
            bg="black"
        )
        self.canvas.pack()

        self.initialize()

    def initialize(self):
        self.block_exist_pos = []
        for i in self.canvas.find_all():
            self.canvas.delete(i)

        # Draw grid with 10x20
        for w in range(self.width_num+1):
            self.canvas.create_line(
                self._offset_w + self.cell*w, self._offset_h,
                self._offset_w + self.cell*w, self._offset_h + self.cell*self.height_num,
                tag=w, fill="gray",width=1)

        for h in range(self.height_num+1):
            self.canvas.create_line(
                 self._offset_w, self._offset_h + self.cell*h,
                 self._offset_w + self.cell*self.width_num, self._offset_h + self.cell*h,
                 tag=h, fill="gray",width=1)

    def click_button(self):
        if self.toggle:
            self.toggle = False
            self.start_button["text"] = "Start"
        else:
            self.toggle = True
            self.initialize()
            self.start_button["text"] = "Reset"
            self.gen_block()
            self.app.after(500, self.move_block)

    def press_a(self, _):
        if self.toggle:
            a = {i: (-self.cell, 0) for i in self.blocks.tags}
            if self.move_en_frame(a, "side"):
                for tag in self.blocks.tags:
                    self.canvas.move(tag, -self.cell, 0)

    def press_d(self, _):
        if self.toggle:
            a = {i: (self.cell, 0) for i in self.blocks.tags}
            if self.move_en_frame(a, "side"):
                for tag in self.blocks.tags:
                    self.canvas.move(tag, self.cell, 0) 

    def press_s(self, _):
        if self.toggle:
            a = {i: (0, self.cell) for i in self.blocks.tags}
            if self.move_en_frame(a):
                for tag in self.blocks.tags:
                    self.canvas.move(tag, 0, self.cell) 

    def press_space(self, _):
        if self.toggle:
            if self.move_en_frame(self.blocks.gen_round(), "round"):
                self.blocks.gen_ok()
                for tag in self.blocks.tags:
                    x = self.blocks.round[tag][0]
                    y = self.blocks.round[tag][1]
                    self.canvas.move(tag, x, y)

    def move_block(self):
        if self.toggle:
            a = {i: (0, self.cell) for i in self.blocks.tags}
            if self.move_en_frame(a):
                for tag in self.blocks.tags:
                    self.canvas.move(tag, 0, self.cell)
            self.app.after(500, self.move_block)

    def gen_block(self):
        if self.toggle:
            for x, y, tag in self.blocks.gen():
                self.canvas.create_rectangle(
                    self._offset_w + self.cell*x, self._offset_h + self.cell*y,
                    self._offset_w + self.cell*(x+1), self._offset_h + self.cell*(y+1),
                    tag=tag, fill="gray", width=1)
    
    def delete_line(self):
        # ブロックが詰まっている行のIDとy座標の辞書を作成
        cnt = {self._offset_h + self.cell*i: {} for i in range(20)}
        for n, m, id in self.block_exist_pos:
            try:
                cnt[m].update({id: n})
            except KeyError:  # ワークアラウンド
                self.toggle = False
                return

        # ブロックが10列ある行を削除
        delete_line_pos = []
        for m, v in cnt.items():
            if len(v.keys()) != 10:
                continue

            delete_line_pos.append(m)

            for id, n in v.items():
                self.block_exist_pos.remove([n, m, id])
                self.canvas.delete(id)

        # 削除された行より上にあるブロックを下に移動
        buf = []
        for n, m, id in self.block_exist_pos:
            a = 0
            for i in delete_line_pos:
                if i > m:
                    a = a + self.cell
            self.canvas.move(id, 0, a)
            buf.append([n, m + a, id])
        self.block_exist_pos = copy.deepcopy(buf)

    def prepare_next_block(self):
        # 次のブロックを生成する準備
        for tag in self.blocks.tags:
            pos = self.canvas.bbox(tag)
            self.canvas.delete(tag)
            x_s = pos[0] + 1  # ワークアラウンド
            y_s = pos[1] + 1  # ワークアラウンド

            id = self.canvas.create_rectangle(
                x_s, y_s, x_s + self.cell, y_s + self.cell, fill="red", width=1)
            self.block_exist_pos.append([x_s, y_s, id])

        # 一行そろったら消す
        self.delete_line()

        # 次のBlockを生成
        self.gen_block()

    def move_en_frame(self, a, meta=""):
        # Blockの位置を変えて良いか
        for tag in self.blocks.tags:
            pos = self.canvas.bbox(tag)
            x_s = pos[0] + 1
            y_s = pos[1] + 1

            # BlockとBlockが重なったら次のBlock
            for n, m, _ in self.block_exist_pos:
                if y_s + a[tag][1] == m and x_s + a[tag][0] == n:
                    if meta == "":
                        self.prepare_next_block()
                    return False

            # Blockが一番下についたら次のBlock
            if y_s + a[tag][1] > self._height - self._offset_h - 1:
                if meta != "round":
                    self.prepare_next_block()
                return False

            # Blockが両端に来たらFalse
            if x_s + a[tag][0] < self._offset_w or x_s + a[tag][0] >= self._width - self._offset_w:
                return False

        return True

    def run(self):
        self.app.bind("<a>", self.press_a)
        self.app.bind("<d>", self.press_d)
        self.app.bind("<s>", self.press_s)
        self.app.bind("<space>", self.press_space)
        self.app.mainloop()


if __name__ == "__main__":
    a = tetris_class()
    a.run()