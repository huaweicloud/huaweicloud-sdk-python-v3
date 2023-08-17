# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentMount:

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
        'sub_path': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'path': 'path',
        'sub_path': 'sub_path',
        'read_only': 'read_only'
    }

    def __init__(self, path=None, sub_path=None, read_only=None):
        """ComponentMount

        The model defined in huaweicloud sdk

        :param path: 挂载路径
        :type path: str
        :param sub_path: 挂载路径的子路径
        :type sub_path: str
        :param read_only: 是否只读
        :type read_only: bool
        """
        
        

        self._path = None
        self._sub_path = None
        self._read_only = None
        self.discriminator = None

        self.path = path
        self.sub_path = sub_path
        self.read_only = read_only

    @property
    def path(self):
        """Gets the path of this ComponentMount.

        挂载路径

        :return: The path of this ComponentMount.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ComponentMount.

        挂载路径

        :param path: The path of this ComponentMount.
        :type path: str
        """
        self._path = path

    @property
    def sub_path(self):
        """Gets the sub_path of this ComponentMount.

        挂载路径的子路径

        :return: The sub_path of this ComponentMount.
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """Sets the sub_path of this ComponentMount.

        挂载路径的子路径

        :param sub_path: The sub_path of this ComponentMount.
        :type sub_path: str
        """
        self._sub_path = sub_path

    @property
    def read_only(self):
        """Gets the read_only of this ComponentMount.

        是否只读

        :return: The read_only of this ComponentMount.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this ComponentMount.

        是否只读

        :param read_only: The read_only of this ComponentMount.
        :type read_only: bool
        """
        self._read_only = read_only

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
        if not isinstance(other, ComponentMount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
