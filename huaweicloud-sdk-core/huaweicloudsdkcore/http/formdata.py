# coding: utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

import os
from mimetypes import MimeTypes


class FormFile(object):
    TYPE = "file"

    def __init__(self, f):
        """This class is used for the formdata.

        :param f: An opened file, for example, f = open("demo.txt", "r")
        :type f: stream
        """
        self._file = f

    def close(self):
        self._file.close()

    def get_path(self):
        return self._file.name

    def get_abs_path(self):
        return os.path.abspath(self.get_path())

    def get_file_name(self):
        file_name = self._file.name
        if "\\" in file_name:
            return file_name.split("\\")[-1]
        elif "/" in file_name:
            return file_name.split("/")[-1]
        else:
            return file_name

    def convert_to_file_tuple(self):
        mime_type = MimeTypes().guess_type(self.get_abs_path())
        file_name = self.get_file_name()
        return (file_name, self._file, mime_type[0]) if mime_type[0] else (file_name, self._file)

    def __del__(self):
        self.close()







