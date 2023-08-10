# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListXelLogResponseResult:

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
        'file_size': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_size': 'file_size'
    }

    def __init__(self, file_name=None, file_size=None):
        """ListXelLogResponseResult

        The model defined in huaweicloud sdk

        :param file_name: 文件名
        :type file_name: str
        :param file_size: 日志大小，单位：KB
        :type file_size: str
        """
        
        

        self._file_name = None
        self._file_size = None
        self.discriminator = None

        self.file_name = file_name
        self.file_size = file_size

    @property
    def file_name(self):
        """Gets the file_name of this ListXelLogResponseResult.

        文件名

        :return: The file_name of this ListXelLogResponseResult.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ListXelLogResponseResult.

        文件名

        :param file_name: The file_name of this ListXelLogResponseResult.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this ListXelLogResponseResult.

        日志大小，单位：KB

        :return: The file_size of this ListXelLogResponseResult.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this ListXelLogResponseResult.

        日志大小，单位：KB

        :param file_size: The file_size of this ListXelLogResponseResult.
        :type file_size: str
        """
        self._file_size = file_size

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
        if not isinstance(other, ListXelLogResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
