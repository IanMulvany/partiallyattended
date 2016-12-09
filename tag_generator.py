import glob
import ruamel.yaml as yaml
import io

blog_posts = glob.glob("_posts/*")

tags = set([])

for blog_post in blog_posts:
    with open(blog_post) as stream:
        try:
            docs = yaml.load_all(stream)
            for doc in docs:
                try:
                    for item in doc.items():
                        if item[0] == "categories":
                            new_set = set(item[1])
                            tags.update(new_set)
                        # if item[0] == categories:
                        #     print(item[1])
                        # #     tags.extend(item[1])
                except:
                    print(".")
        except yaml.YAMLError as exc:
            print(exc)

print(tags)
print(len(tags))



def create_tag_template(tag):
    html_content = """---
layout: tags
title: {}
category: {}
---""".format(tag, tag)

    file_path = "tags/" + tag + ".html"
    print(html_content)
    with io.FileIO(file_path, "w") as file:
        file.write(html_content.encode('utf-8'))

for tag in tags:
    create_tag_template(tag)
