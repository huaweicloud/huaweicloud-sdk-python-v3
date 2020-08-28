# coding: utf-8

import pprint
import re

import six





class MeetingFileBase:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'file_code': 'str',
        'topic': 'str',
        'file_id': 'str',
        'file_name': 'str',
        'file_size': 'int',
        'thumbnail_file_id': 'str',
        'thumbnail_file_name': 'str',
        'thumbnail_file_size': 'int',
        'pdf_file_id': 'str',
        'pdf_file_name': 'str',
        'pdf_file_size': 'int'
    }

    attribute_map = {
        'file_code': 'fileCode',
        'topic': 'topic',
        'file_id': 'fileId',
        'file_name': 'fileName',
        'file_size': 'fileSize',
        'thumbnail_file_id': 'thumbnailFileId',
        'thumbnail_file_name': 'thumbnailFileName',
        'thumbnail_file_size': 'thumbnailFileSize',
        'pdf_file_id': 'pdfFileId',
        'pdf_file_name': 'pdfFileName',
        'pdf_file_size': 'pdfFileSize'
    }

    def __init__(self, file_code=None, topic=None, file_id=None, file_name=None, file_size=None, thumbnail_file_id=None, thumbnail_file_name=None, thumbnail_file_size=None, pdf_file_id=None, pdf_file_name=None, pdf_file_size=None):
        """MeetingFileBase - a model defined in huaweicloud sdk"""
        
        

        self._file_code = None
        self._topic = None
        self._file_id = None
        self._file_name = None
        self._file_size = None
        self._thumbnail_file_id = None
        self._thumbnail_file_name = None
        self._thumbnail_file_size = None
        self._pdf_file_id = None
        self._pdf_file_name = None
        self._pdf_file_size = None
        self.discriminator = None

        if file_code is not None:
            self.file_code = file_code
        if topic is not None:
            self.topic = topic
        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name
        if file_size is not None:
            self.file_size = file_size
        if thumbnail_file_id is not None:
            self.thumbnail_file_id = thumbnail_file_id
        if thumbnail_file_name is not None:
            self.thumbnail_file_name = thumbnail_file_name
        if thumbnail_file_size is not None:
            self.thumbnail_file_size = thumbnail_file_size
        if pdf_file_id is not None:
            self.pdf_file_id = pdf_file_id
        if pdf_file_name is not None:
            self.pdf_file_name = pdf_file_name
        if pdf_file_size is not None:
            self.pdf_file_size = pdf_file_size

    @property
    def file_code(self):
        """Gets the file_code of this MeetingFileBase.

        会议纪要文件码

        :return: The file_code of this MeetingFileBase.
        :rtype: str
        """
        return self._file_code

    @file_code.setter
    def file_code(self, file_code):
        """Sets the file_code of this MeetingFileBase.

        会议纪要文件码

        :param file_code: The file_code of this MeetingFileBase.
        :type: str
        """
        self._file_code = file_code

    @property
    def topic(self):
        """Gets the topic of this MeetingFileBase.

        文件主题

        :return: The topic of this MeetingFileBase.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this MeetingFileBase.

        文件主题

        :param topic: The topic of this MeetingFileBase.
        :type: str
        """
        self._topic = topic

    @property
    def file_id(self):
        """Gets the file_id of this MeetingFileBase.

        文件Id

        :return: The file_id of this MeetingFileBase.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this MeetingFileBase.

        文件Id

        :param file_id: The file_id of this MeetingFileBase.
        :type: str
        """
        self._file_id = file_id

    @property
    def file_name(self):
        """Gets the file_name of this MeetingFileBase.

        文件名

        :return: The file_name of this MeetingFileBase.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this MeetingFileBase.

        文件名

        :param file_name: The file_name of this MeetingFileBase.
        :type: str
        """
        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this MeetingFileBase.

        文件大小，单位字节

        :return: The file_size of this MeetingFileBase.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this MeetingFileBase.

        文件大小，单位字节

        :param file_size: The file_size of this MeetingFileBase.
        :type: int
        """
        self._file_size = file_size

    @property
    def thumbnail_file_id(self):
        """Gets the thumbnail_file_id of this MeetingFileBase.

        缩略图文件Id

        :return: The thumbnail_file_id of this MeetingFileBase.
        :rtype: str
        """
        return self._thumbnail_file_id

    @thumbnail_file_id.setter
    def thumbnail_file_id(self, thumbnail_file_id):
        """Sets the thumbnail_file_id of this MeetingFileBase.

        缩略图文件Id

        :param thumbnail_file_id: The thumbnail_file_id of this MeetingFileBase.
        :type: str
        """
        self._thumbnail_file_id = thumbnail_file_id

    @property
    def thumbnail_file_name(self):
        """Gets the thumbnail_file_name of this MeetingFileBase.

        缩略图文件名

        :return: The thumbnail_file_name of this MeetingFileBase.
        :rtype: str
        """
        return self._thumbnail_file_name

    @thumbnail_file_name.setter
    def thumbnail_file_name(self, thumbnail_file_name):
        """Sets the thumbnail_file_name of this MeetingFileBase.

        缩略图文件名

        :param thumbnail_file_name: The thumbnail_file_name of this MeetingFileBase.
        :type: str
        """
        self._thumbnail_file_name = thumbnail_file_name

    @property
    def thumbnail_file_size(self):
        """Gets the thumbnail_file_size of this MeetingFileBase.

        缩略图文件大小，单位字节

        :return: The thumbnail_file_size of this MeetingFileBase.
        :rtype: int
        """
        return self._thumbnail_file_size

    @thumbnail_file_size.setter
    def thumbnail_file_size(self, thumbnail_file_size):
        """Sets the thumbnail_file_size of this MeetingFileBase.

        缩略图文件大小，单位字节

        :param thumbnail_file_size: The thumbnail_file_size of this MeetingFileBase.
        :type: int
        """
        self._thumbnail_file_size = thumbnail_file_size

    @property
    def pdf_file_id(self):
        """Gets the pdf_file_id of this MeetingFileBase.

        pdf文件Id

        :return: The pdf_file_id of this MeetingFileBase.
        :rtype: str
        """
        return self._pdf_file_id

    @pdf_file_id.setter
    def pdf_file_id(self, pdf_file_id):
        """Sets the pdf_file_id of this MeetingFileBase.

        pdf文件Id

        :param pdf_file_id: The pdf_file_id of this MeetingFileBase.
        :type: str
        """
        self._pdf_file_id = pdf_file_id

    @property
    def pdf_file_name(self):
        """Gets the pdf_file_name of this MeetingFileBase.

        pdf文件名

        :return: The pdf_file_name of this MeetingFileBase.
        :rtype: str
        """
        return self._pdf_file_name

    @pdf_file_name.setter
    def pdf_file_name(self, pdf_file_name):
        """Sets the pdf_file_name of this MeetingFileBase.

        pdf文件名

        :param pdf_file_name: The pdf_file_name of this MeetingFileBase.
        :type: str
        """
        self._pdf_file_name = pdf_file_name

    @property
    def pdf_file_size(self):
        """Gets the pdf_file_size of this MeetingFileBase.

        pdf文件大小，单位字节

        :return: The pdf_file_size of this MeetingFileBase.
        :rtype: int
        """
        return self._pdf_file_size

    @pdf_file_size.setter
    def pdf_file_size(self, pdf_file_size):
        """Sets the pdf_file_size of this MeetingFileBase.

        pdf文件大小，单位字节

        :param pdf_file_size: The pdf_file_size of this MeetingFileBase.
        :type: int
        """
        self._pdf_file_size = pdf_file_size

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MeetingFileBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
