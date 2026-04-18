import requests
import json
import urllib.parse
from datetime import datetime
import re
import os
import sys

def clear_screen():
    """Bersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Tampilkan banner ASCII"""
    banner = """
\033[96m
$$$$$$$$\ $$\                                           $$\            $$$$$$\  $$\       $$$$$$\ 
\__$$  __|$$ |                                          $$ |          $$  __$$\ $$ |      \_$$  _|
   $$ |   $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$ | $$$$$$$\ $$ /  \__|$$ |        $$ |  
   $$ |   $$  __$$\ $$  __$$\ $$  __$$\  \____$$\ $$  __$$ |$$  _____|$$ |      $$ |        $$ |  
   $$ |   $$ |  $$ |$$ |  \__|$$$$$$$$ | $$$$$$$ |$$ /  $$ |\$$$$$$\  $$ |      $$ |        $$ |  
   $$ |   $$ |  $$ |$$ |      $$   ____|$$  __$$ |$$ |  $$ | \____$$\ $$ |  $$\ $$ |        $$ |  
   $$ |   $$ |  $$ |$$ |      \$$$$$$$\ \$$$$$$$ |\$$$$$$$ |$$$$$$$  |\$$$$$$  |$$$$$$$$\ $$$$$$\ 
   \__|   \__|  \__|\__|       \_______| \_______| \_______|\_______/  \______/ \________|\______|
\033[0m
                                                                                                  
\033[93m═══════════════════════════════════════════════════════════════════════════════════════════\033[0m
\033[92m                    THREADS SEARCH TOOL - PROFESSIONAL SCRAPER v1.0\033[0m
\033[93m═══════════════════════════════════════════════════════════════════════════════════════════\033[0m
    """
    print(banner)

def print_progress_bar(current, total, bar_length=50):
    """Tampilkan progress bar"""
    progress = current / total
    arrow = '=' * int(round(progress * bar_length))
    spaces = ' ' * (bar_length - len(arrow))
    
    percent = int(round(progress * 100))
    
    sys.stdout.write(f'\r\033[94mProgress: [{arrow}{spaces}] {percent}% ({current}/{total})\033[0m')
    sys.stdout.flush()

def search_threads(keyword, total_posts=50, sessionid=None, consecutive_empty_limit=5):
    url = "https://www.threads.com/graphql/query"
    
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-csrftoken': 'xxx',
        'x-fb-lsd': 'oHcYqc36gPPz6efiGBSLPQ',
        'x-fb-friendly-name': 'BarcelonaSearchResultsRefetchableQuery',
        'x-ig-app-id': '238260118697367'
    }
    
    cookies = {
        'sessionid': sessionid
    }
    
    base_payload = 'av=17841476995564122&__user=0&__a=1&__req=1&dpr=1&__ccg=GOOD&__rev=1037579319&__s=tl8h7e:4gjbo9:xtmv9r&__hsi=7629834632183724114&__dyn=7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awgo9oO0n24oaEd82lwv89k2C1Fwc60D85m1mzXwae4UaEW0Loco5G0zK5o4q0HU1IEGdwtU2ewbS1LyUaUbGw4mwr86C2q6omwxwiQ1mwLwHxW17y9UjgbVEeEuw9y1swoo7y0sO1iwg8&__csr=gkgH9R4Zncx95Rvb5ljHFbVeGWciCinmmtproyAaz-9DxKbiJ5hqhd2aUKlQagy9DKjSczGCHoKFEC9xXxmczEjwSwbK1txK325U9kT8FLFai4FE01rUEzgmg0AYm8gK0t20gTK9w6kxm5gI19wsEdQ0qii0lqii3i3Z01hi04Mp6Ow8u0c3F2mEKt1r81pKe2RaiN8l5Qt3GxKb41yi1poDxu3i3O1uzo2Cx2Urwau684Wa8q8w17m1JwKg7l8MC01SlK9w0E4Bw1dp2At0bO5U1FU3zz81zC8xmmm4A8w&__hsdp=gqp0dpw6zc5ECSgc9QzIu3lpkw9Yay8wmxBMYgaPXYyexm4FQNi4lPg4926zVgLFhB4z3zQ5k84ocq52a1ifgtg5EFm971pUjaa41N0DgF0k182exq1JyE9k0L2zEnw9oE9kq78jweO1Fw9S223R0cu14wVwlEzw&__hblp=0Jg1xk449wjayKh0m8qhA2B0xxyaw-G0zE9EqK3Hz99Eak1gxS3C2mm48lybxubxC9xW8z8cEuxGU3wwzxa58aFUbUcUsy-eyEO0BUO79Esxe788U5XwiEdoaFbw9S6VaKcG2p0Vxa15xq7odaAAG5E8EaU7bw&__sjsp=gq70R60mi8wycxq9JAe5QzD83NpkFw94ay8wmxBMWkaPBIxqzoqj58hHGQc40hEd24fB2-A588A7Onw2JE&__comet_req=29&fb_dtsg=NAfsmy-bpAqvWUoVGaa2zAHdht_KssQnO1RBa8BAxGvs6qN-pYPLg7g%3A17843709688147332%3A1776459306&jazoest=26428&lsd=vz6UkeqalhWQS_9qpjJ2Kx&__spin_r=1037579319&__spin_b=trunk&__spin_t=1776459308&__crn=comet.threads.BarcelonaSearchResultsColumnRoute&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=BarcelonaSearchResultsRefetchableQuery&server_timestamps=true'
    
    all_posts = []
    seen_ids = set()
    page = 0
    posts_per_request = 10
    consecutive_empty = 0
    
    total_requests = (total_posts + posts_per_request - 1) // posts_per_request
    
    print(f"\n\033[96m🔍 Mencari keyword: \033[93m'{keyword}'\033[0m")
    print(f"\033[96m📊 Target: \033[93m{total_posts} post\033[0m\n")
    
    while len(all_posts) < total_posts and page < total_requests:
        if page == 0:
            cursor = None
        else:
            cursor = f"cd5631221957472c81df355041a440f8:{page}"
        
        variables = {
            "after": cursor,
            "before": None,
            "first": 10,
            "has_communities": True,
            "has_serp_header": False,
            "last": None,
            "meta_place_id": None,
            "pinned_ids": None,
            "power_search_info": None,
            "query": keyword,
            "recent": 0,
            "search_surface": "default",
            "tagID": None,
            "trend_fbid": None,
            "use_caching_improvements": False,
            "__relay_internal__pv__BarcelonaHasSERPHeaderrelayprovider": False,
            "__relay_internal__pv__BarcelonaHasCommunitiesrelayprovider": True,
            "__relay_internal__pv__BarcelonaThreadsWebCachingImprovementsrelayprovider": False,
            "__relay_internal__pv__BarcelonaHasCommunityTopContributorsrelayprovider": False,
            "__relay_internal__pv__BarcelonaHasCommunityBobbleheadsrelayprovider": False,
            "__relay_internal__pv__BarcelonaIsLoggedInrelayprovider": True,
            "__relay_internal__pv__BarcelonaHasDearAlgoConsumptionrelayprovider": True,
            "__relay_internal__pv__BarcelonaHasEventBadgerelayprovider": False,
            "__relay_internal__pv__BarcelonaIsSearchDiscoveryEnabledrelayprovider": False,
            "__relay_internal__pv__BarcelonaHasGameScoreSharerelayprovider": True,
            "__relay_internal__pv__BarcelonaHasPublicViewCountCardrelayprovider": True,
            "__relay_internal__pv__BarcelonaHasCommunityEntityCardrelayprovider": True,
            "__relay_internal__pv__BarcelonaHasScorecardCommunityrelayprovider": True,
            "__relay_internal__pv__BarcelonaHasMusicrelayprovider": False,
            "__relay_internal__pv__BarcelonaHasNewspaperLinkStylerelayprovider": False,
            "__relay_internal__pv__BarcelonaHasMessagingrelayprovider": False,
            "__relay_internal__pv__BarcelonaHasGhostPostEmojiActivationrelayprovider": False,
            "__relay_internal__pv__BarcelonaOptionalCookiesEnabledrelayprovider": True,
            "__relay_internal__pv__BarcelonaHasDearAlgoWebProductionrelayprovider": False,
            "__relay_internal__pv__BarcelonaIsCrawlerrelayprovider": False,
            "__relay_internal__pv__BarcelonaCanSeeSponsoredContentrelayprovider": False,
            "__relay_internal__pv__BarcelonaShouldShowFediverseM075Featuresrelayprovider": True,
            "__relay_internal__pv__BarcelonaIsInternalUserrelayprovider": False
        }
        
        variables_json = json.dumps(variables, separators=(',', ':'))
        payload = f"{base_payload}&variables={urllib.parse.quote(variables_json)}&doc_id=25588584157484270"
        
        # Clear current line and print status
        sys.stdout.write(f'\r\033[K\033[94m📄 Halaman {page + 1}/{total_requests} (cursor: {cursor})...\033[0m')
        sys.stdout.flush()
        
        try:
            response = requests.post(url, headers=headers, cookies=cookies, data=payload)
            response.raise_for_status()
            result = response.json()
            
            if 'errors' in result:
                print(f"\n\033[91m❌ Error: {result['errors']}\033[0m")
                break
            
            search_results = result.get('data', {}).get('searchResults', {})
            edges = search_results.get('edges', [])
            
            if not edges:
                print("\n\033[93m⚠️ Tidak ada post lagi.\033[0m")
                break
            
            new_posts_count = 0
            duplicate_count = 0
            
            for edge in edges:
                if len(all_posts) >= total_posts:
                    break
                    
                thread = edge.get('node', {}).get('thread', {})
                thread_items = thread.get('thread_items', [])
                
                for item in thread_items:
                    post = item.get('post', {})
                    if post and len(all_posts) < total_posts:
                        post_id = post.get('pk', '')
                        
                        if post_id in seen_ids:
                            duplicate_count += 1
                            continue
                        
                        simplified_post = extract_important_fields(post)
                        all_posts.append(simplified_post)
                        seen_ids.add(post_id)
                        new_posts_count += 1
            
            # Clear line and show result
            sys.stdout.write(f'\r\033[K')
            if duplicate_count > 0:
                print(f"\033[92m✅ {len(edges)} thread (new: {new_posts_count}, duplicate: {duplicate_count}, total: {len(all_posts)}/{total_posts})\033[0m")
            else:
                print(f"\033[92m✅ {len(edges)} thread (total: {len(all_posts)}/{total_posts})\033[0m")
            
            # Update progress bar
            print_progress_bar(len(all_posts), total_posts)
            print()  # New line after progress bar
            
            if new_posts_count == 0:
                consecutive_empty += 1
                if consecutive_empty >= consecutive_empty_limit:
                    print(f"\n\033[93m⚠️ Tidak ada post baru dalam {consecutive_empty_limit} halaman berturut-turut. Menghentikan pencarian.\033[0m")
                    break
            else:
                consecutive_empty = 0
            
            page += 1
            
        except requests.exceptions.RequestException as e:
            print(f"\n\033[91m❌ Request error: {e}\033[0m")
            break
        except json.JSONDecodeError as e:
            print(f"\n\033[91m❌ JSON decode error: {e}\033[0m")
            break
    
    print(f"\n\033[96m✨ Selesai! Mengambil {len(all_posts)} post unik.\033[0m")
    return all_posts

def extract_important_fields(post):
    user = post.get('user', {})
    
    taken_at = post.get('taken_at', 0)
    post_date = datetime.fromtimestamp(taken_at).strftime('%Y-%m-%d %H:%M:%S') if taken_at else 'Unknown'
    
    tag_header = post.get('text_post_app_info', {}).get('tag_header', {})
    
    simplified = {
        'id': post.get('pk', ''),
        'code': post.get('code', ''),
        'timestamp': taken_at,
        'date': post_date,
        'user': {
            'username': user.get('username', ''),
            'full_name': user.get('full_name', ''),
            'is_verified': user.get('is_verified', False),
            'profile_pic_url': user.get('profile_pic_url', '')
        },
        'caption': post.get('caption', {}).get('text', '') if isinstance(post.get('caption'), dict) else '',
        'like_count': post.get('like_count', 0),
        'reply_count': post.get('text_post_app_info', {}).get('direct_reply_count', 0),
        'repost_count': post.get('text_post_app_info', {}).get('repost_count', 0),
        'quote_count': post.get('text_post_app_info', {}).get('quote_count', 0),
        'url': f"https://threads.net/@{user.get('username', '')}/post/{post.get('code', '')}",
        'hashtags': extract_hashtags(post.get('caption', {}).get('text', '')),
        'mentions': extract_mentions(post.get('caption', {}).get('text', '')),
        'tag': {
            'name': tag_header.get('display_name', ''),
            'id': tag_header.get('id', '')
        } if tag_header else None
    }
    
    return simplified

def extract_hashtags(text):
    if not text:
        return []
    hashtags = re.findall(r'#(\w+)', text)
    return hashtags

def extract_mentions(text):
    if not text:
        return []
    mentions = re.findall(r'@(\w+)', text)
    return mentions

def save_to_json(posts, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    print(f"\033[92m💾 Data disimpan ke {filename}\033[0m")

def save_to_csv(posts, filename):
    import csv
    
    if not posts:
        print("\033[93mTidak ada data untuk disimpan ke CSV\033[0m")
        return
    
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, escapechar='\\')
        
        writer.writerow([
            'id', 'username', 'full_name', 'date', 'caption', 
            'like_count', 'reply_count', 'repost_count', 'quote_count', 
            'hashtags', 'mentions', 'tag_name', 'url'
        ])
        
        for post in posts:
            caption = post.get('caption', '') or ''
            caption_clean = ' '.join(caption.replace('\r', ' ').splitlines())
            caption_clean = caption_clean.replace('"', '""')
            
            hashtags_str = ', '.join(post.get('hashtags', []))
            mentions_str = ', '.join(post.get('mentions', []))
            tag_name = post.get('tag', {}).get('name', '') if post.get('tag') else ''
            
            writer.writerow([
                post.get('id', ''),
                post.get('user', {}).get('username', ''),
                post.get('user', {}).get('full_name', ''),
                post.get('date', ''),
                caption_clean,
                post.get('like_count', 0),
                post.get('reply_count', 0),
                post.get('repost_count', 0),
                post.get('quote_count', 0),
                hashtags_str,
                mentions_str,
                tag_name,
                post.get('url', '')
            ])
    
    print(f"\033[92m💾 Data disimpan ke {filename}\033[0m")

def save_to_excel(posts, filename):
    try:
        import pandas as pd
    except ImportError:
        print("\033[91m❌ Library pandas tidak terinstall. Install dengan: pip install pandas openpyxl\033[0m")
        return
    
    if not posts:
        print("\033[93mTidak ada data untuk disimpan ke Excel\033[0m")
        return
    
    data = []
    for post in posts:
        row = {
            'ID': post.get('id', ''),
            'Username': post.get('user', {}).get('username', ''),
            'Full Name': post.get('user', {}).get('full_name', ''),
            'Verified': post.get('user', {}).get('is_verified', False),
            'Date': post.get('date', ''),
            'Caption': post.get('caption', ''),
            'Like Count': post.get('like_count', 0),
            'Reply Count': post.get('reply_count', 0),
            'Repost Count': post.get('repost_count', 0),
            'Quote Count': post.get('quote_count', 0),
            'Hashtags': ', '.join(post.get('hashtags', [])),
            'Mentions': ', '.join(post.get('mentions', [])),
            'Tag Name': post.get('tag', {}).get('name', '') if post.get('tag') else '',
            'URL': post.get('url', '')
        }
        data.append(row)
    
    df = pd.DataFrame(data)
    
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Threads Results', index=False)
        worksheet = writer.sheets['Threads Results']
        
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)
            worksheet.column_dimensions[column_letter].width = adjusted_width
    
    print(f"\033[92m💾 Data disimpan ke {filename}\033[0m")

def save_posts(posts, keyword):
    """Menu untuk menyimpan hasil scraping"""
    if not posts:
        print("\n\033[93m❌ Tidak ada data untuk disimpan.\033[0m")
        return
    
    print("\n" + "\033[93m" + "="*60 + "\033[0m")
    print("\033[96m💾 SAVE OPTIONS\033[0m")
    print("\033[93m" + "="*60 + "\033[0m")
    print("1. JSON")
    print("2. CSV")
    print("3. Excel")
    print("4. All formats (JSON + CSV + Excel)")
    print("5. Skip saving")
    
    save_choice = input("\n\033[96mPilihan (1/2/3/4/5): \033[0m").strip()
    
    if save_choice == '1':
        filename = f"results/threads_{keyword}_{len(posts)}posts.json"
        save_to_json(posts, filename)
    elif save_choice == '2':
        filename = f"results/threads_{keyword}_{len(posts)}posts.csv"
        save_to_csv(posts, filename)
    elif save_choice == '3':
        filename = f"results/threads_{keyword}_{len(posts)}posts.xlsx"
        save_to_excel(posts, filename)
    elif save_choice == '4':
        json_file = f"results/threads_{keyword}_{len(posts)}posts.json"
        csv_file = f"results/threads_{keyword}_{len(posts)}posts.csv"
        excel_file = f"results/threads_{keyword}_{len(posts)}posts.xlsx"
        save_to_json(posts, json_file)
        save_to_csv(posts, csv_file)
        save_to_excel(posts, excel_file)
        print(f"\n\033[92m✅ Semua file telah disimpan!\033[0m")
    elif save_choice == '5':
        print("\033[93mData tidak disimpan.\033[0m")
    else:
        print("\033[91mPilihan tidak valid, data tidak disimpan.\033[0m")

def main():
    clear_screen()
    print_banner()
    
    # Input session ID sekali di awal
    print("\n\033[93m⚠️  PENTING: Anda perlu mengambil session ID dari browser:\033[0m")
    print("   1. Login ke threads.com")
    print("   2. Buka Developer Tools (F12)")
    print("   3. Pergi ke tab Application/Storage → Cookies → https://www.threads.com")
    print("   4. Cari cookie 'sessionid' dan copy nilainya\n")
    
    sessionid = input("\033[96m🔑 Masukkan session ID: \033[0m").strip()
    if not sessionid:
        print("\n\033[91m❌ Session ID wajib diisi!\033[0m")
        return
    
    print("\n\033[92m✅ Session ID berhasil disimpan!\033[0m\n")
    
    # Loop untuk multiple keywords
    while True:
        print("\033[93m" + "="*60 + "\033[0m")
        keyword = input("\033[96m🔎 Keyword pencarian (atau 'exit' untuk keluar): \033[0m").strip()
        
        if keyword.lower() == 'exit':
            print("\n\033[92m👋 Terima kasih telah menggunakan Threads Search Tool!\033[0m")
            break
        
        if not keyword:
            print("\033[93m⚠️ Keyword tidak boleh kosong!\033[0m\n")
            continue
        
        try:
            total = int(input("\033[96m📝 Jumlah post yang ingin diambil: \033[0m"))
            if total <= 0:
                total = 50
                print(f"\033[93m⚠️ Menggunakan default: {total} post\033[0m")
        except ValueError:
            total = 50
            print(f"\033[93m⚠️ Menggunakan default: {total} post\033[0m")
        
        print("\n" + "\033[93m" + "="*60 + "\033[0m")
        
        # Clear screen but keep banner
        clear_screen()
        print_banner()
        
        # Jalankan scraping
        results = search_threads(keyword, total, sessionid)
        
        if results:
            print(f"\n\033[92m✅ Berhasil mengambil {len(results)} post untuk keyword '{keyword}'\033[0m")
            save_posts(results, keyword)
        else:
            print(f"\n\033[91m❌ Tidak ada hasil ditemukan untuk keyword '{keyword}'\033[0m")
        
        print("\n" + "\033[93m" + "="*60 + "\033[0m")
        again = input("\n\033[96mIngin mencari keyword lain? (y/n): \033[0m").strip().lower()
        if again != 'y':
            print("\n\033[92m👋 Terima kasih telah menggunakan Threads Search Tool!\033[0m")
            break
        else:
            clear_screen()
            print_banner()
            print("\n\033[92m✅ Session ID masih tersimpan!\033[0m\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[93m⚠️ Program dihentikan oleh user. Sampai jumpa!\033[0m")
    except Exception as e:
        print(f"\n\033[91m❌ Terjadi error: {e}\033[0m")