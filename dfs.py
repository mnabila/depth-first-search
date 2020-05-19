#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# dfs.py
# Copyright (c) 2020 M. Nabil Adani <nblid48@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, json


def readGraph():
    with open(os.path.join(os.getcwd(), "graph.json"), "r") as fr:
        return json.load(fr)


def dfs(graph: dict, start: str, stop: str):
    visited = [start]
    path = []
    while visited:
        visit = visited.pop()
        if visit not in path:
            path.append(visit)
            if visit == stop:
                break
            if visit in graph.keys():
                nodes = graph.get(visit)
                nodes.reverse()
                visited.extend(nodes)
    return path


if __name__ == "__main__":
    print(dfs(readGraph(), "A", "M"))
