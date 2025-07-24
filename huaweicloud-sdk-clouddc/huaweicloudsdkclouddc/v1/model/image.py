# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Image:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'os_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'os_type': 'os_type'
    }

    def __init__(self, id=None, name=None, os_type=None):
        r"""Image

        The model defined in huaweicloud sdk

        :param id: 镜像ID，格式为UUID。
        :type id: str
        :param name: 镜像名称
        :type name: str
        :param os_type: 镜像os类型
        :type os_type: str
        """
        
        

        self._id = None
        self._name = None
        self._os_type = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.os_type = os_type

    @property
    def id(self):
        r"""Gets the id of this Image.

        镜像ID，格式为UUID。

        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Image.

        镜像ID，格式为UUID。

        :param id: The id of this Image.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Image.

        镜像名称

        :return: The name of this Image.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Image.

        镜像名称

        :param name: The name of this Image.
        :type name: str
        """
        self._name = name

    @property
    def os_type(self):
        r"""Gets the os_type of this Image.

        镜像os类型

        :return: The os_type of this Image.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this Image.

        镜像os类型

        :param os_type: The os_type of this Image.
        :type os_type: str
        """
        self._os_type = os_type

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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
