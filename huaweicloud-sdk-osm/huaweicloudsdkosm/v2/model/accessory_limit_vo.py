# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessoryLimitVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit_count': 'str',
        'limit_size': 'str',
        'limit_file_type': 'str'
    }

    attribute_map = {
        'limit_count': 'limit_count',
        'limit_size': 'limit_size',
        'limit_file_type': 'limit_file_type'
    }

    def __init__(self, limit_count=None, limit_size=None, limit_file_type=None):
        """AccessoryLimitVo

        The model defined in huaweicloud sdk

        :param limit_count: 限制文件数量
        :type limit_count: str
        :param limit_size: 限制文件大小，单位是M
        :type limit_size: str
        :param limit_file_type: 限制文件类型
        :type limit_file_type: str
        """
        
        

        self._limit_count = None
        self._limit_size = None
        self._limit_file_type = None
        self.discriminator = None

        if limit_count is not None:
            self.limit_count = limit_count
        if limit_size is not None:
            self.limit_size = limit_size
        if limit_file_type is not None:
            self.limit_file_type = limit_file_type

    @property
    def limit_count(self):
        """Gets the limit_count of this AccessoryLimitVo.

        限制文件数量

        :return: The limit_count of this AccessoryLimitVo.
        :rtype: str
        """
        return self._limit_count

    @limit_count.setter
    def limit_count(self, limit_count):
        """Sets the limit_count of this AccessoryLimitVo.

        限制文件数量

        :param limit_count: The limit_count of this AccessoryLimitVo.
        :type limit_count: str
        """
        self._limit_count = limit_count

    @property
    def limit_size(self):
        """Gets the limit_size of this AccessoryLimitVo.

        限制文件大小，单位是M

        :return: The limit_size of this AccessoryLimitVo.
        :rtype: str
        """
        return self._limit_size

    @limit_size.setter
    def limit_size(self, limit_size):
        """Sets the limit_size of this AccessoryLimitVo.

        限制文件大小，单位是M

        :param limit_size: The limit_size of this AccessoryLimitVo.
        :type limit_size: str
        """
        self._limit_size = limit_size

    @property
    def limit_file_type(self):
        """Gets the limit_file_type of this AccessoryLimitVo.

        限制文件类型

        :return: The limit_file_type of this AccessoryLimitVo.
        :rtype: str
        """
        return self._limit_file_type

    @limit_file_type.setter
    def limit_file_type(self, limit_file_type):
        """Sets the limit_file_type of this AccessoryLimitVo.

        限制文件类型

        :param limit_file_type: The limit_file_type of this AccessoryLimitVo.
        :type limit_file_type: str
        """
        self._limit_file_type = limit_file_type

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
        if not isinstance(other, AccessoryLimitVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
