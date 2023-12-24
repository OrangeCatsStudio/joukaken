#GASでフォーム内容を蓄積　－　GASの勉強しなきゃだ～！！！！
#GoogleDriveからファイルを取得　ー　そういうモジュールあるんじゃない？？？
###それをもとにHTMLを作成　－　どうやって？？　ー　テンプレ作ってそれに当てはめると簡単にできるかも
#Githubにアップする前にチェックをするべきでは？？　ー　LINEBOTで知らせよう！！！　ー　でもどうやって見るの？？　ー　テスト版を上げるテストサーバーがあれば完結　ー　あるわけないやろ
#それをgithubにあげることができたら完璧　－　これもなんかそういうモジュールありそうww


#そもそも、このプログラムをどのタイミングで実行するの？？？　＜＝そりゃ投稿したときだろ　＜＝そのタイミングでどうやって実行するの？？？　＜＝わんちゃんGASでそういう関数ある説　＜＝なかったらどうすんねん　＜＝わからんやろがい
#正式に投稿が終了したタイミングでSlackBOTで知らせるのはどうかな？？？　＜＝いいじゃん！
#SlackBOTの勉強しなあかへんやろ！！！！

img_filename = ""
img_filepass= f"../img/{img_filename}.png"
title = ""
maker_name = ""
explain_text = ""
template_pass = ".\\template.html"
work_type = "p"
work_id = work_type + "_" + "2"

#テンプレートから文字の読み込み
with open(template_pass, 'r', encoding='utf-8') as f:
    template = f.read()

#テンプレートから新しいHTMLファイルの中身を作成
content = template.format(img_filepass,title,maker_name,explain_text)

new_file = ".\\{}.html".format(work_id+"_unchecked")
#contentからHTMLファイルを作成
with open(new_file, 'w', encoding="utf-8") as fa:
    fa.write(content)

#LINE_BOTでお知らせしたうえで自分で確認=>ファイルの名前から_uncheckedを外す
