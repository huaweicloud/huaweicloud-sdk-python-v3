# coding: utf-8

import pprint
import re

import six





class RecordDownloadUrlDO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'token': 'str',
        'file_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'token': 'token',
        'file_type': 'fileType',
        'url': 'url'
    }

    def __init__(self, token=None, file_type=None, url=None):
        """RecordDownloadUrlDO - a model defined in huaweicloud sdk"""
        
        

        self._token = None
        self._file_type = None
        self._url = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if file_type is not None:
            self.file_type = file_type
        if url is not None:
            self.url = url

    @property
    def token(self):
        """Gets the token of this RecordDownloadUrlDO.

        下载鉴权token

        :return: The token of this RecordDownloadUrlDO.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this RecordDownloadUrlDO.

        下载鉴权token

        :param token: The token of this RecordDownloadUrlDO.
        :type: str
        """
        self._token = token

    @property
    def file_type(self):
        """Gets the file_type of this RecordDownloadUrlDO.

        文件类型

        :return: The file_type of this RecordDownloadUrlDO.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this RecordDownloadUrlDO.

        文件类型

        :param file_type: The file_type of this RecordDownloadUrlDO.
        :type: str
        """
        self._file_type = file_type

    @property
    def url(self):
        """Gets the url of this RecordDownloadUrlDO.

        录制文件下载URL

        :return: The url of this RecordDownloadUrlDO.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RecordDownloadUrlDO.

        录制文件下载URL

        :param url: The url of this RecordDownloadUrlDO.
        :type: str
        """
        self._url = url

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
        if not isinstance(other, RecordDownloadUrlDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
