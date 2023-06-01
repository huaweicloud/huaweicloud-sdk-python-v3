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

    def __init__(self, f, content_type=None):
        """This class is used for the formdata.

        :param f: An opened file or file path, for example, f = open("demo.txt", "rb") or f = "/tmp/log.txt"
        :type f: stream or str
        :param content_type: the content type of the file
        :type content_type: str
        """
        self._file = self._ensure_file_in_rb_mode(f)
        self._content_type = content_type

    @classmethod
    def _ensure_file_in_rb_mode(cls, _file):
        if isinstance(_file, str):
            if not os.path.isfile(_file):
                raise ValueError("invalid file path: " + _file)
            return open(_file, "rb")

        if not hasattr(_file, "read") or not hasattr(_file, "mode"):
            raise TypeError("invalid file type")

        if _file.mode != "rb":
            _file.close()
            raise ValueError("invalid file mode, please open the file in 'rb' mode")
        return _file

    def close(self):
        if hasattr(self._file, "closed") and not self._file.closed:
            self._file.close()

    @property
    def path(self):
        return self._file.name

    @property
    def abs_path(self):
        return os.path.abspath(self.path)

    @property
    def name(self):
        name = self._file.name
        if "\\" in name:
            return name.split("\\")[-1]
        elif "/" in name:
            return name.split("/")[-1]
        else:
            return name

    @property
    def content_type(self):
        mime_type = MimeTypes().guess_type(self.abs_path)
        return mime_type[0]

    def convert_to_file_tuple(self):
        return (self.name, self._file, str(self._content_type)) if self._content_type else (self.name, self._file)

    def __del__(self):
        self.close()
