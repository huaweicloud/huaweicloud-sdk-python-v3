# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'replace': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'replace': 'replace'
    }

    def __init__(self, name=None, type=None, replace=None):
        """JobResourceInfo

        The model defined in huaweicloud sdk

        :param name: 资源名
        :type name: str
        :param type: 资源类型
        :type type: str
        :param replace: 替换后的资源名
        :type replace: str
        """
        
        

        self._name = None
        self._type = None
        self._replace = None
        self.discriminator = None

        self.name = name
        self.type = type
        if replace is not None:
            self.replace = replace

    @property
    def name(self):
        """Gets the name of this JobResourceInfo.

        资源名

        :return: The name of this JobResourceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobResourceInfo.

        资源名

        :param name: The name of this JobResourceInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this JobResourceInfo.

        资源类型

        :return: The type of this JobResourceInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JobResourceInfo.

        资源类型

        :param type: The type of this JobResourceInfo.
        :type type: str
        """
        self._type = type

    @property
    def replace(self):
        """Gets the replace of this JobResourceInfo.

        替换后的资源名

        :return: The replace of this JobResourceInfo.
        :rtype: str
        """
        return self._replace

    @replace.setter
    def replace(self, replace):
        """Sets the replace of this JobResourceInfo.

        替换后的资源名

        :param replace: The replace of this JobResourceInfo.
        :type replace: str
        """
        self._replace = replace

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
        if not isinstance(other, JobResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
