# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FsDuInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'used_capacity': 'int',
        'file_count': 'FsFileCount',
        'message': 'str'
    }

    attribute_map = {
        'path': 'path',
        'used_capacity': 'used_capacity',
        'file_count': 'file_count',
        'message': 'message'
    }

    def __init__(self, path=None, used_capacity=None, file_count=None, message=None):
        """FsDuInfo

        The model defined in huaweicloud sdk

        :param path: 文件系统内合法的目录全路径
        :type path: str
        :param used_capacity: 占用容量，单位：byte
        :type used_capacity: int
        :param file_count: 该目录下所有文件数目
        :type file_count: :class:`huaweicloudsdksfsturbo.v1.FsFileCount`
        :param message: 错误信息
        :type message: str
        """
        
        

        self._path = None
        self._used_capacity = None
        self._file_count = None
        self._message = None
        self.discriminator = None

        self.path = path
        self.used_capacity = used_capacity
        self.file_count = file_count
        self.message = message

    @property
    def path(self):
        """Gets the path of this FsDuInfo.

        文件系统内合法的目录全路径

        :return: The path of this FsDuInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FsDuInfo.

        文件系统内合法的目录全路径

        :param path: The path of this FsDuInfo.
        :type path: str
        """
        self._path = path

    @property
    def used_capacity(self):
        """Gets the used_capacity of this FsDuInfo.

        占用容量，单位：byte

        :return: The used_capacity of this FsDuInfo.
        :rtype: int
        """
        return self._used_capacity

    @used_capacity.setter
    def used_capacity(self, used_capacity):
        """Sets the used_capacity of this FsDuInfo.

        占用容量，单位：byte

        :param used_capacity: The used_capacity of this FsDuInfo.
        :type used_capacity: int
        """
        self._used_capacity = used_capacity

    @property
    def file_count(self):
        """Gets the file_count of this FsDuInfo.

        该目录下所有文件数目

        :return: The file_count of this FsDuInfo.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.FsFileCount`
        """
        return self._file_count

    @file_count.setter
    def file_count(self, file_count):
        """Sets the file_count of this FsDuInfo.

        该目录下所有文件数目

        :param file_count: The file_count of this FsDuInfo.
        :type file_count: :class:`huaweicloudsdksfsturbo.v1.FsFileCount`
        """
        self._file_count = file_count

    @property
    def message(self):
        """Gets the message of this FsDuInfo.

        错误信息

        :return: The message of this FsDuInfo.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FsDuInfo.

        错误信息

        :param message: The message of this FsDuInfo.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, FsDuInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
