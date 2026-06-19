def get_all_posts(flatpages):
    pages = flatpages._pages
    all_posts = []

    for path in pages:
        if path=='home' or path=='contacts':
            continue
        post = pages[path]
        title = post['title']
        time = post['published']
        url = '/post/' + path.split('/')[-1]
        all_posts.append((title,url,time))

    all_posts = sorted(all_posts, key=lambda x: x[2], reverse=True)

    return all_posts
