# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'size': 'int',
        'last_modified': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'size': 'size',
        'last_modified': 'last_modified'
    }

    def __init__(self, file_name=None, size=None, last_modified=None):
        """ObsObject

        The model defined in huaweicloud sdk

        :param file_name: 对象名
        :type file_name: str
        :param size: 文件大小，单位KB
        :type size: int
        :param last_modified: 上次修改时间，格式如：2020/07/16 15:11:55 GMT+08:00
        :type last_modified: str
        """
        
        

        self._file_name = None
        self._size = None
        self._last_modified = None
        self.discriminator = None

        self.file_name = file_name
        self.size = size
        self.last_modified = last_modified

    @property
    def file_name(self):
        """Gets the file_name of this ObsObject.

        对象名

        :return: The file_name of this ObsObject.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ObsObject.

        对象名

        :param file_name: The file_name of this ObsObject.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def size(self):
        """Gets the size of this ObsObject.

        文件大小，单位KB

        :return: The size of this ObsObject.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ObsObject.

        文件大小，单位KB

        :param size: The size of this ObsObject.
        :type size: int
        """
        self._size = size

    @property
    def last_modified(self):
        """Gets the last_modified of this ObsObject.

        上次修改时间，格式如：2020/07/16 15:11:55 GMT+08:00

        :return: The last_modified of this ObsObject.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ObsObject.

        上次修改时间，格式如：2020/07/16 15:11:55 GMT+08:00

        :param last_modified: The last_modified of this ObsObject.
        :type last_modified: str
        """
        self._last_modified = last_modified

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
        if not isinstance(other, ObsObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
