from yt_music_core import yt_music_core


def main():
    downloader = yt_music_core.YtMusicDownloader()

    downloader.preprocedure()

    while True:
        url = input('請輸入播放清單連結：')

        if 'list=' not in url:
            print('沒有偵測到播放清單連結，請確認連結中含有list=')
            continue

        musics = downloader.get_playlist_musics({'URL': url})
        musics = downloader.parse_all(musics)
        downloader.download_all_musics(musics)

        downloader.post_procedure()


if __name__ == '__main__':
    main()
