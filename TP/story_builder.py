#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Story:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print(self.parts)


class Builder:
    def __init__(self):
        self.story = Story()

    def _build_image(self):
        raise NotImplementedError

    def _build_music(self):
        raise NotImplementedError

    def _build_effect(self):
        raise NotImplementedError

    def _build_video(self):
        raise NotImplementedError


class FacebookConcreteBuilder(Builder):
    def _build_image(self):
        self.story.add("Facebook Image")

    def _build_music(self):
        self.story.add("Facebook Music")

    def _build_effect(self):
        self.story.add("Facebook Effect")

    def _build_video(self):
        self.story.add("Facebook Video")


class InstagramConcreteBuilder(Builder):
    def _build_image(self):
        self.story.add("Instagram Image")

    def _build_music(self):
        self.story.add("Instagram Music")

    def _build_effect(self):
        self.story.add("Instagram Effect")

    def _build_video(self):
        self.story.add("Instagram Video")


class StoryDirector:
    def construct(self, builder):
        self.builder = builder

    def basic_story(self):
        self.builder.story = Story()
        self.builder._build_image()

    def music_story(self):
        self.builder.story = Story()
        self.builder._build_image()
        self.builder._build_music()

    def video_story(self):
        self.builder.story = Story()
        self.builder._build_video()
        self.builder._build_effect()


def main():
    concrete_builder = FacebookConcreteBuilder()
    director = StoryDirector()
    director.construct(concrete_builder)
    director.basic_story()
    story = concrete_builder.story
    story.show()

    concrete_builder2 = InstagramConcreteBuilder()
    director = StoryDirector()
    director.construct(concrete_builder2)
    director.video_story()
    story = concrete_builder2.story
    story.show()


if __name__ == "__main__":
    main()
