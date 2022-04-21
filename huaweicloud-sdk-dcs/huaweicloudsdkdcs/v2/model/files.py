# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Files:

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
        'size': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'size': 'size',
        'update_at': 'update_at'
    }

    def __init__(self, file_name=None, size=None, update_at=None):
        """Files

        The model defined in huaweicloud sdk

        :param file_name: 备份文件名。
        :type file_name: str
        :param size: 文件大小（单位：Byte）。
        :type size: str
        :param update_at: 文件最后修改时间（格式YYYY-MM-DD HH:MM:SS）。
        :type update_at: str
        """
        
        

        self._file_name = None
        self._size = None
        self._update_at = None
        self.discriminator = None

        self.file_name = file_name
        if size is not None:
            self.size = size
        if update_at is not None:
            self.update_at = update_at

    @property
    def file_name(self):
        """Gets the file_name of this Files.

        备份文件名。

        :return: The file_name of this Files.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Files.

        备份文件名。

        :param file_name: The file_name of this Files.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def size(self):
        """Gets the size of this Files.

        文件大小（单位：Byte）。

        :return: The size of this Files.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Files.

        文件大小（单位：Byte）。

        :param size: The size of this Files.
        :type size: str
        """
        self._size = size

    @property
    def update_at(self):
        """Gets the update_at of this Files.

        文件最后修改时间（格式YYYY-MM-DD HH:MM:SS）。

        :return: The update_at of this Files.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this Files.

        文件最后修改时间（格式YYYY-MM-DD HH:MM:SS）。

        :param update_at: The update_at of this Files.
        :type update_at: str
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
        if not isinstance(other, Files):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
