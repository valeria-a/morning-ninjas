import observer as observer


class FacebookPost(observer.Subject):
    def __init__(self, post_id, content):
        super().__init__()
        self.post_id = post_id
        self.content = content

    def edit_post(self, new_content):
        self.content = new_content
        self.notify(post=self)


class UserNotification(observer.Observer):
    def __init__(self, user_id):
        self.user_id = user_id

    def update(self, post):
        # todo: send notification to this user on each post update
        print(f"User {self.user_id} notification: "
              f"Post {post.post_id} has been updated with new content: {post.content}")


class HashtagNotification(observer.Observer):
    def __init__(self, hashtag):
        self.hashtag = hashtag

    def update(self, post):
        if self.hashtag in post.content:
            # todo: get all the users subscribed to this hashtag and send notification to them
            print(f"Hashtag notification: "
                  f"Post {post.post_id} has been updated with new content containing {self.hashtag}")


if __name__ == "__main__":
    post = FacebookPost(post_id=123, content="This is my first post!")
    user_notifier_1 = UserNotification(user_id=1)
    user_notifier_2 = UserNotification(user_id=2)
    hashtag_notifier = HashtagNotification(hashtag="python")

    post.attach(user_notifier_1)
    post.attach(user_notifier_2)
    post.attach(hashtag_notifier)

    post.edit_post("This is an updated post with #python in it.")

    post.detach(user_notifier_1)
    post.detach(hashtag_notifier)

    post.edit_post("This is a second update to the post.")
