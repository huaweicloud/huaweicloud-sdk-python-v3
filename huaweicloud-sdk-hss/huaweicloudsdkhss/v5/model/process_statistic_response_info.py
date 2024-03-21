# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessStatisticResponseInfo:

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
        'num': 'int'
    }

    attribute_map = {
        'path': 'path',
        'num': 'num'
    }

    def __init__(self, path=None, num=None):
        """ProcessStatisticResponseInfo

        The model defined in huaweicloud sdk

        :param path: 进程的可执行文件路径
        :type path: str
        :param num: 进程数量
        :type num: int
        """
        
        

        self._path = None
        self._num = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if num is not None:
            self.num = num

    @property
    def path(self):
        """Gets the path of this ProcessStatisticResponseInfo.

        进程的可执行文件路径

        :return: The path of this ProcessStatisticResponseInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ProcessStatisticResponseInfo.

        进程的可执行文件路径

        :param path: The path of this ProcessStatisticResponseInfo.
        :type path: str
        """
        self._path = path

    @property
    def num(self):
        """Gets the num of this ProcessStatisticResponseInfo.

        进程数量

        :return: The num of this ProcessStatisticResponseInfo.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this ProcessStatisticResponseInfo.

        进程数量

        :param num: The num of this ProcessStatisticResponseInfo.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, ProcessStatisticResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
