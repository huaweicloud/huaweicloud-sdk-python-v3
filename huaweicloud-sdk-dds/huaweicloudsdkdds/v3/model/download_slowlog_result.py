# coding: utf-8

import pprint
import re

import six





class DownloadSlowlogResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'file_link': 'str',
        'file_name': 'str',
        'file_size': 'str',
        'node_name': 'str',
        'status': 'str',
        'update_at': 'int'
    }

    attribute_map = {
        'file_link': 'file_link',
        'file_name': 'file_name',
        'file_size': 'file_size',
        'node_name': 'node_name',
        'status': 'status',
        'update_at': 'update_at'
    }

    def __init__(self, file_link=None, file_name=None, file_size=None, node_name=None, status=None, update_at=None):
        """DownloadSlowlogResult - a model defined in huaweicloud sdk"""
        
        

        self._file_link = None
        self._file_name = None
        self._file_size = None
        self._node_name = None
        self._status = None
        self._update_at = None
        self.discriminator = None

        self.file_link = file_link
        self.file_name = file_name
        self.file_size = file_size
        self.node_name = node_name
        self.status = status
        self.update_at = update_at

    @property
    def file_link(self):
        """Gets the file_link of this DownloadSlowlogResult.

        文件下载链接

        :return: The file_link of this DownloadSlowlogResult.
        :rtype: str
        """
        return self._file_link

    @file_link.setter
    def file_link(self, file_link):
        """Sets the file_link of this DownloadSlowlogResult.

        文件下载链接

        :param file_link: The file_link of this DownloadSlowlogResult.
        :type: str
        """
        self._file_link = file_link

    @property
    def file_name(self):
        """Gets the file_name of this DownloadSlowlogResult.

        文件名称

        :return: The file_name of this DownloadSlowlogResult.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DownloadSlowlogResult.

        文件名称

        :param file_name: The file_name of this DownloadSlowlogResult.
        :type: str
        """
        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this DownloadSlowlogResult.

        文件大小

        :return: The file_size of this DownloadSlowlogResult.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this DownloadSlowlogResult.

        文件大小

        :param file_size: The file_size of this DownloadSlowlogResult.
        :type: str
        """
        self._file_size = file_size

    @property
    def node_name(self):
        """Gets the node_name of this DownloadSlowlogResult.

        文件所属节点名称

        :return: The node_name of this DownloadSlowlogResult.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this DownloadSlowlogResult.

        文件所属节点名称

        :param node_name: The node_name of this DownloadSlowlogResult.
        :type: str
        """
        self._node_name = node_name

    @property
    def status(self):
        """Gets the status of this DownloadSlowlogResult.

        文件查询状态

        :return: The status of this DownloadSlowlogResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DownloadSlowlogResult.

        文件查询状态

        :param status: The status of this DownloadSlowlogResult.
        :type: str
        """
        self._status = status

    @property
    def update_at(self):
        """Gets the update_at of this DownloadSlowlogResult.

        文件最后更新时间

        :return: The update_at of this DownloadSlowlogResult.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this DownloadSlowlogResult.

        文件最后更新时间

        :param update_at: The update_at of this DownloadSlowlogResult.
        :type: int
        """
        self._update_at = update_at

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
        if not isinstance(other, DownloadSlowlogResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
