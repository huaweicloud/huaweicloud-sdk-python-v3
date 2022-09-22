# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMeetingFileResponseDTO:

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
        'pdf_file_size': 'int',
        'user_id': 'str',
        'creation_timestamp': 'int'
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
        'pdf_file_size': 'pdfFileSize',
        'user_id': 'userId',
        'creation_timestamp': 'creationTimestamp'
    }

    def __init__(self, file_code=None, topic=None, file_id=None, file_name=None, file_size=None, thumbnail_file_id=None, thumbnail_file_name=None, thumbnail_file_size=None, pdf_file_id=None, pdf_file_name=None, pdf_file_size=None, user_id=None, creation_timestamp=None):
        """ListMeetingFileResponseDTO

        The model defined in huaweicloud sdk

        :param file_code: 会议纪要文件码。
        :type file_code: str
        :param topic: 文件主题。
        :type topic: str
        :param file_id: 文件Id。
        :type file_id: str
        :param file_name: 文件名。
        :type file_name: str
        :param file_size: 文件大小，单位字节。
        :type file_size: int
        :param thumbnail_file_id: 缩略图文件Id。
        :type thumbnail_file_id: str
        :param thumbnail_file_name: 缩略图文件名。
        :type thumbnail_file_name: str
        :param thumbnail_file_size: 缩略图文件大小，单位字节。
        :type thumbnail_file_size: int
        :param pdf_file_id: pdf文件Id。
        :type pdf_file_id: str
        :param pdf_file_name: pdf文件名。
        :type pdf_file_name: str
        :param pdf_file_size: pdf文件大小，单位字节。
        :type pdf_file_size: int
        :param user_id: 用户UUID。
        :type user_id: str
        :param creation_timestamp: 文件创建时间戳。
        :type creation_timestamp: int
        """
        
        

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
        self._user_id = None
        self._creation_timestamp = None
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
        if user_id is not None:
            self.user_id = user_id
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp

    @property
    def file_code(self):
        """Gets the file_code of this ListMeetingFileResponseDTO.

        会议纪要文件码。

        :return: The file_code of this ListMeetingFileResponseDTO.
        :rtype: str
        """
        return self._file_code

    @file_code.setter
    def file_code(self, file_code):
        """Sets the file_code of this ListMeetingFileResponseDTO.

        会议纪要文件码。

        :param file_code: The file_code of this ListMeetingFileResponseDTO.
        :type file_code: str
        """
        self._file_code = file_code

    @property
    def topic(self):
        """Gets the topic of this ListMeetingFileResponseDTO.

        文件主题。

        :return: The topic of this ListMeetingFileResponseDTO.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ListMeetingFileResponseDTO.

        文件主题。

        :param topic: The topic of this ListMeetingFileResponseDTO.
        :type topic: str
        """
        self._topic = topic

    @property
    def file_id(self):
        """Gets the file_id of this ListMeetingFileResponseDTO.

        文件Id。

        :return: The file_id of this ListMeetingFileResponseDTO.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this ListMeetingFileResponseDTO.

        文件Id。

        :param file_id: The file_id of this ListMeetingFileResponseDTO.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def file_name(self):
        """Gets the file_name of this ListMeetingFileResponseDTO.

        文件名。

        :return: The file_name of this ListMeetingFileResponseDTO.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ListMeetingFileResponseDTO.

        文件名。

        :param file_name: The file_name of this ListMeetingFileResponseDTO.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this ListMeetingFileResponseDTO.

        文件大小，单位字节。

        :return: The file_size of this ListMeetingFileResponseDTO.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this ListMeetingFileResponseDTO.

        文件大小，单位字节。

        :param file_size: The file_size of this ListMeetingFileResponseDTO.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def thumbnail_file_id(self):
        """Gets the thumbnail_file_id of this ListMeetingFileResponseDTO.

        缩略图文件Id。

        :return: The thumbnail_file_id of this ListMeetingFileResponseDTO.
        :rtype: str
        """
        return self._thumbnail_file_id

    @thumbnail_file_id.setter
    def thumbnail_file_id(self, thumbnail_file_id):
        """Sets the thumbnail_file_id of this ListMeetingFileResponseDTO.

        缩略图文件Id。

        :param thumbnail_file_id: The thumbnail_file_id of this ListMeetingFileResponseDTO.
        :type thumbnail_file_id: str
        """
        self._thumbnail_file_id = thumbnail_file_id

    @property
    def thumbnail_file_name(self):
        """Gets the thumbnail_file_name of this ListMeetingFileResponseDTO.

        缩略图文件名。

        :return: The thumbnail_file_name of this ListMeetingFileResponseDTO.
        :rtype: str
        """
        return self._thumbnail_file_name

    @thumbnail_file_name.setter
    def thumbnail_file_name(self, thumbnail_file_name):
        """Sets the thumbnail_file_name of this ListMeetingFileResponseDTO.

        缩略图文件名。

        :param thumbnail_file_name: The thumbnail_file_name of this ListMeetingFileResponseDTO.
        :type thumbnail_file_name: str
        """
        self._thumbnail_file_name = thumbnail_file_name

    @property
    def thumbnail_file_size(self):
        """Gets the thumbnail_file_size of this ListMeetingFileResponseDTO.

        缩略图文件大小，单位字节。

        :return: The thumbnail_file_size of this ListMeetingFileResponseDTO.
        :rtype: int
        """
        return self._thumbnail_file_size

    @thumbnail_file_size.setter
    def thumbnail_file_size(self, thumbnail_file_size):
        """Sets the thumbnail_file_size of this ListMeetingFileResponseDTO.

        缩略图文件大小，单位字节。

        :param thumbnail_file_size: The thumbnail_file_size of this ListMeetingFileResponseDTO.
        :type thumbnail_file_size: int
        """
        self._thumbnail_file_size = thumbnail_file_size

    @property
    def pdf_file_id(self):
        """Gets the pdf_file_id of this ListMeetingFileResponseDTO.

        pdf文件Id。

        :return: The pdf_file_id of this ListMeetingFileResponseDTO.
        :rtype: str
        """
        return self._pdf_file_id

    @pdf_file_id.setter
    def pdf_file_id(self, pdf_file_id):
        """Sets the pdf_file_id of this ListMeetingFileResponseDTO.

        pdf文件Id。

        :param pdf_file_id: The pdf_file_id of this ListMeetingFileResponseDTO.
        :type pdf_file_id: str
        """
        self._pdf_file_id = pdf_file_id

    @property
    def pdf_file_name(self):
        """Gets the pdf_file_name of this ListMeetingFileResponseDTO.

        pdf文件名。

        :return: The pdf_file_name of this ListMeetingFileResponseDTO.
        :rtype: str
        """
        return self._pdf_file_name

    @pdf_file_name.setter
    def pdf_file_name(self, pdf_file_name):
        """Sets the pdf_file_name of this ListMeetingFileResponseDTO.

        pdf文件名。

        :param pdf_file_name: The pdf_file_name of this ListMeetingFileResponseDTO.
        :type pdf_file_name: str
        """
        self._pdf_file_name = pdf_file_name

    @property
    def pdf_file_size(self):
        """Gets the pdf_file_size of this ListMeetingFileResponseDTO.

        pdf文件大小，单位字节。

        :return: The pdf_file_size of this ListMeetingFileResponseDTO.
        :rtype: int
        """
        return self._pdf_file_size

    @pdf_file_size.setter
    def pdf_file_size(self, pdf_file_size):
        """Sets the pdf_file_size of this ListMeetingFileResponseDTO.

        pdf文件大小，单位字节。

        :param pdf_file_size: The pdf_file_size of this ListMeetingFileResponseDTO.
        :type pdf_file_size: int
        """
        self._pdf_file_size = pdf_file_size

    @property
    def user_id(self):
        """Gets the user_id of this ListMeetingFileResponseDTO.

        用户UUID。

        :return: The user_id of this ListMeetingFileResponseDTO.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ListMeetingFileResponseDTO.

        用户UUID。

        :param user_id: The user_id of this ListMeetingFileResponseDTO.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this ListMeetingFileResponseDTO.

        文件创建时间戳。

        :return: The creation_timestamp of this ListMeetingFileResponseDTO.
        :rtype: int
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this ListMeetingFileResponseDTO.

        文件创建时间戳。

        :param creation_timestamp: The creation_timestamp of this ListMeetingFileResponseDTO.
        :type creation_timestamp: int
        """
        self._creation_timestamp = creation_timestamp

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListMeetingFileResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
