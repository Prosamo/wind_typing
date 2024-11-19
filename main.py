import asyncio
import pygame, sys, time
from mytyping import *

pygame.init()    # Pygameを初期化
screen = pygame.display.set_mode((600, 500))    # 画面を作成
pygame.display.set_caption("強風タイピング")    # タイトルを作成

# 日本語フォントの読み込み
font_path = "NotoSansJP-VariableFont_wght.ttf"  # フォントファイルのパス

words = dict(承知いたしました = 'しょうちいたしました',
             ディレクターズカット版 = 'でぃれくたーずかっとばん',
             こんなはずじゃなかった = 'こんなはずじゃなかった',
             ラニーニャ現象 = 'らにーにゃげんしょう',
             チャドの首都ンジャメナ = 'ちゃどのしゅとんじゃめな',
             たこ焼きパーティーしよう = 'たこやきぱーてぃーしよう',
             給食の揚げパン = 'きゅうしょくのあげぱん',
             障害物競走 = 'しょうがいぶつきょうそう',
             車のスライドドア = 'くるまのすらいどどあ',
             画竜点睛を欠く = 'がりょうてんせいをかく',
             一着でフィニッシュ = 'いっちゃくでふぃにっしゅ',
             ろうそくの火が消えた = 'ろうそくのひがきえた',
             集中力の限界 = 'しゅうちゅうりょくのげんかい',
             アルファベットの練習 = 'あるふぁべっとのれんしゅう',
             人生の転機となる = 'じんせいのてんきとなる',
             海外に留学する = 'かいがいにりゅうがくする',
             今世紀最大の謎 = 'こんせいきさいだいのなぞ',
             太陽系外惑星 = 'たいようけいがいわくせい',
             エベレスト山頂 = 'えべれすとさんちょう',
             卒業証書授与式 = 'そつぎょうしょうしょじゅよしき',
             関ヶ原の戦い = 'せきがはらのたたかい',
             拒否権を行使する = 'きょひけんをこうしする',
             黄道十二星座 = 'こうどうじゅうにせいざ',
             オーマイゴッド粒子 = 'おーまいごっどりゅうし',
             過マンガン酸カリウム = 'かまんがんさんかりうむ',
             アニリン塩酸塩 = 'あにりんえんさんえん',
             生類憐みの令 = 'しょうるいあわれみのれい',
             公事方御定書 = 'くじかたおさだめがき',
             青色発光ダイオード = 'あおいろはっこうだいおーど',
             アメリカ同時多発テロ = 'あめりかどうじたはつてろ',
             度数法と弧度法 = 'どすうほうとこどほう',
             東海道新幹線 = 'とうかいどうしんかんせん',
             アイスクリーム食べたい = 'あいすくりーむたべたい',
             牛乳じゃんけん = 'ぎゅうにゅうじゃんけん',
             北海道はでっかいどう = 'ほっかいどうはでっかいどう',
             ありがとうございました = 'ありがとうございました',
             ヘラクレスオオカブト = 'へらくれすおおかぶと',
             ファジーネーブル飲みたい = 'ふぁじーねーぶるのみたい',
             プログラミング最高 = 'ぷろぐらみんぐさいこう',
             古都京都の文化財 = 'こときょうとのぶんかざい',
             二重らせん構造 = 'にじゅうらせんこうぞう',
             ヨーロッパの火薬庫 = 'よーろっぱのかやくこ',
             自然が俺を呼んでいる = 'しぜんがおれをよんでいる'
             )
process = Process(words)

def rank_check(score):
    if score >= 25000:
        return'颶 風 級'
    elif score >= 23000:
        return '暴 風 級'
    elif score >= 21000:
        return '全 強 風 級'
    elif score >= 19000:
        return '大 強 風 級'
    elif score >= 17000:
        return '疾 強 風 級'
    elif score >= 15000:
        return '強 風 級'
    elif score >= 13000:
        return '雄 風 級'
    elif score >= 11000:
        return '疾 風 級'
    elif score >= 9000:
        return '和 風 級'
    elif score >= 7000:
        return '軟 風 級'
    elif score >= 5000:
        return '軽 風 級'
    elif score >= 3000:
        return '至 軽 風 級'
    else:
        return '平穏級'

class Time():
    def __init__(self):
        self.last_time = None
        self.counter = 0
        self.deadline = 0
        self.wps = 0
        self.mwps = 0
        self.wpm = 0
        self.miss_count = 0
        self.sentences = 0
    def count(self):
        self.current_time = time.time()
        if self.last_time is None:
           self.last_time = self.current_time
        elif self.current_time - self.last_time >= 1:
            self.counter += 1
            self.deadline += 1
            if self.wps > self.mwps:
                self.mwps = self.wps
            if self.deadline == 10:
                process.set_new_sentence()
                self.deadline = 0
                gw.x = 100
            self.wps = 0
            self.last_time = self.current_time
        if self.counter == 60:
            gw.game_mode = False
            gw.result_mode = True
class GameWindow:
    def __init__(self):
        self.game_mode = False
        self.result_mode = False
        self.x = 100
        # フレームの設定
        self.frame = pygame.Surface((500, 100), pygame.SRCALPHA) # 透明度を有効にしたSurface
        self.frame.fill((0, 0, 0, 207)) # 半透明の黒で塗りつぶす
        pygame.draw.rect(self.frame, (255,255,255), (0,0,500,100), 3)
        # フォントオブジェクトを作成する
        self.font_roman = pygame.font.Font(None, 32) # デフォルトフォントをサイズ20で指定
        self.font_hiragana = pygame.font.Font(font_path, 32) # デフォルトフォントをサイズ32で指定
        self.font_timer = pygame.font.Font(font_path, 48)
        #画像オブジェクトを作成する
        self.background = pygame.image.load('background.png')
        self.human = pygame.image.load('girl.png').convert_alpha()
    def draw(self):
        game_time.count()
        #テキストオブジェクトを再生成する
        screen.fill((235, 235, 245))
        self.text_roman = self.font_roman.render(process.show_roman, True, (128, 128, 128)) # 文字列と色を指定
        self.text_input = self.font_roman.render(process.input, True, (255, 255, 255))
        self.text_sentence = self.font_hiragana.render(process.sentence, True, (255, 255, 255)) # 文字列と色を指定
        self.timer = self.font_timer.render(f'{60-game_time.counter}', True, (0, 0, 0))
        # オブジェクトを画面に描画する
        screen.blit(self.background, (10, 10))
        screen.blit(self.timer, (276,-8))
        screen.blit(self.frame, (50, 50))
        screen.blit(self.text_roman, (60,60))
        screen.blit(self.text_input, (60, 60))
        screen.blit(self.text_sentence, (60, 90)) # 左上の位置を指定
        screen.blit(self.human, (self.x, 300))
        self.x += 0.75
class TitleWindow:
    def __init__(self):
        self.frame = pygame.Surface((560, 100), pygame.SRCALPHA)
        self.frame.fill((255, 255, 255, 207))
        self.font = pygame.font.Font(font_path, 80)
        self.font2 = pygame.font.Font(None, 50)
        title = self.font.render('強風タイピング', True, (255,0,0))
        self.frame.blit(title, (0,-10))
        self.frame.blit(title, (0,-11))
        self.frame.blit(title, (1,-10))
        self.frame.blit(title, (1,-11))
        self.start = self.font2.render('--PLESS SPACE TO START--', True, (0,0,0))
        self.background = pygame.image.load('background.png')
        self.draw()
    def draw(self):
        screen.fill((235, 235, 245))
        screen.blit(self.background, (10, 10))
        screen.blit(self.frame,(20,90))
        screen.blit(self.start, (65,370))
class ResultWindow:
    def __init__(self):
        self.background = pygame.image.load('background.png')
        self.frame = pygame.Surface((500,400), pygame.SRCALPHA)
        self.frame.fill((0, 0, 0, 207))
        pygame.draw.rect(self.frame, (255,255,255), (0,0,500,400), 3)
        font_restart = pygame.font.Font(None, 40)
        restart = font_restart.render('--PLESS SPACE TO RESTART--', True, (255,255,255))
        self.frame.blit(restart, (40,350))
        self.font_rank = pygame.font.Font(font_path, 80)
        self.font = pygame.font.Font(font_path, 20)
    def draw(self):
        wps = game_time.wpm / 60
        wpm = game_time.wpm
        miss = game_time.miss_count
        ws = wps * 2
        mws = game_time.mwps * 2
        accuracy = (wpm / max(1, (wpm + miss)))*100
        score = (ws + mws) * wpm * (accuracy / 100)**2
        screen.fill((235, 235, 245))
        rank = self.font_rank.render(rank_check(score), True, (255, 255, 255))
        text_score = self.font.render(f'スコア　　　：{score:.1f}', True, (255, 255, 255))
        text_ws = self.font.render(f'風速　　　　：{ws:.1f}',True, (255, 255, 255))
        text_mws = self.font.render(f'最大瞬間風速：{mws:.1f}',True, (255, 255, 255))
        sentences = self.font.render(f'飛ばした人数：{game_time.sentences}',True, (255, 255, 255))
        text_wpm = self.font.render(f'打鍵数　　　：{wpm}', True, (255, 255, 255))
        text_wps = self.font.render(f'打鍵／秒　　：{wps:.1f}',True, (255, 255, 255))
        text_miss = self.font.render(f'ミスタイプ数：{miss}', True, (255, 255, 255))
        text_accuracy = self.font.render(f'正確率　　　：{accuracy:.2f}％', True, (255, 255, 255))
        screen.blit(self.background, (10, 10))
        screen.blit(self.frame, (50,50))
        screen.blit(rank, (100,100))
        screen.blit(text_score, (80, 230))
        screen.blit(text_ws, (80,265))
        screen.blit(text_mws, (80,300))
        screen.blit(sentences, (80,335))
        screen.blit(text_wpm, (300,230))
        screen.blit(text_wps, (300,265))
        screen.blit(text_miss, (300,300))
        screen.blit(text_accuracy, (300,335))
class Spin:
    def __init__(self):
        self.spin_mode = False
        self.human = pygame.image.load("girl.png").convert_alpha()
        self.angle = 0
        self.x = gw.x
        self.y = 300
    def draw(self):
        if self.spin_mode:
            self.x -= 8
            self.y -= 2
            self.angle += 20
            rotated_image = pygame.transform.rotate(self.human, self.angle) # 画像を回転させる
            rotated_rect = rotated_image.get_rect() # 回転した画像の矩形を取得する
            rotated_rect.center = (self.x, self.y) # 矩形の中心を画面の中心に合わせる
            screen.blit(rotated_image, rotated_rect) # 回転した画像を矩形に合わせて画面に描画する
            if self.x <= -50:
                self.spin_mode = False

async def main():
    global game_time, gw
    clock = pygame.time.Clock()
    game_time = Time()
    gw = GameWindow()
    tw = TitleWindow()
    rw = ResultWindow()
    spin = Spin()
    screen.fill((235, 235, 245))
    tw.draw()
    while True:
        process.update_show_roman()
        if gw.game_mode == True:
            gw.draw()
            spin.draw()
        elif gw.result_mode == True:
            rw.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # キーを押したとき
                if gw.game_mode == True:
                    if event.key == pygame.K_ESCAPE:# ESCキーならタイトルに戻る
                        gw.game_mode = False
                        tw.draw()
                    else:
                        correct_input = process.check_correct_input(pygame.key.name(event.key))    #ミスタイプを判定
                        if correct_input:
                            game_time.wps += 1
                            game_time.wpm += 1
                            vocalize('input.ogg')
                            chunk_conpleted = process.check_chunk_completion()    #文の打ち終わりを判定
                            if chunk_conpleted:
                                sentence_completed = process.check_sentence_completion()
                                if sentence_completed:
                                    vocalize('wind.ogg')
                                    spin.spin_mode = True
                                    spin.x = gw.x
                                    spin.y = 300
                                    process.set_new_sentence()    #新しい文を用意
                                    game_time.sentences += 1
                                    game_time.deadline = 0
                                    gw.x = 100
                        else:
                            vocalize('miss.ogg')
                            game_time.miss_count += 1
                else:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        gw.game_mode = True
                        gw.result_mode = False
                        spin.spin_mode = False
                        game_time = Time()
                        gw.x = 100
                        process.set_new_sentence()
        pygame.display.update()
        clock.tick(50)
        await asyncio.sleep(0)
def vocalize(a):
    pygame.mixer.init(frequency=44100)
    pygame.mixer.set_num_channels(32)
    sound_key = pygame.mixer.Sound(a)
    sound_key.play()

asyncio.run(main())

