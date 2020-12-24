# coding: utf-8

import pprint
import re

import six





class SlowlogDownloadRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'file_name': 'file_name'
    }

    def __init__(self, request_id=None, file_name=None):
        """SlowlogDownloadRequest - a model defined in huaweicloud sdk"""
        
        

        self._request_id = None
        self._file_name = None
        self.discriminator = None

        self.request_id = request_id
        if file_name is not None:
            self.file_name = file_name

    @property
    def request_id(self):
        """Gets the request_id of this SlowlogDownloadRequest.

        - 请求ID，uuid，代表此次获取慢日志的请求ID。

        :return: The request_id of this SlowlogDownloadRequest.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this SlowlogDownloadRequest.

        - 请求ID，uuid，代表此次获取慢日志的请求ID。

        :param request_id: The request_id of this SlowlogDownloadRequest.
        :type: str
        """
        self._request_id = request_id

    @property
    def file_name(self):
        """Gets the file_name of this SlowlogDownloadRequest.

        - 需要下载的文件的文件名, 当引擎为SQL Server时为必选。

        :return: The file_name of this SlowlogDownloadRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this SlowlogDownloadRequest.

        - 需要下载的文件的文件名, 当引擎为SQL Server时为必选。

        :param file_name: The file_name of this SlowlogDownloadRequest.
        :type: str
        """
        self._file_name = file_name

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
        if not isinstance(other, SlowlogDownloadRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
