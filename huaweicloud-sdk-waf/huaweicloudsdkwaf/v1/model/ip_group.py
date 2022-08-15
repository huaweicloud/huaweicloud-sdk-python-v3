# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpGroup:

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
        'size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'size': 'size'
    }

    def __init__(self, id=None, name=None, size=None):
        """IpGroup

        The model defined in huaweicloud sdk

        :param id: Ip地址组id，在新增Ip地址组时系统自动生成的唯一标识
        :type id: str
        :param name: Ip地址组名
        :type name: str
        :param size: Ip地址组中包含Ip/Ip段的数量
        :type size: int
        """
        
        

        self._id = None
        self._name = None
        self._size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size

    @property
    def id(self):
        """Gets the id of this IpGroup.

        Ip地址组id，在新增Ip地址组时系统自动生成的唯一标识

        :return: The id of this IpGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IpGroup.

        Ip地址组id，在新增Ip地址组时系统自动生成的唯一标识

        :param id: The id of this IpGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this IpGroup.

        Ip地址组名

        :return: The name of this IpGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IpGroup.

        Ip地址组名

        :param name: The name of this IpGroup.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this IpGroup.

        Ip地址组中包含Ip/Ip段的数量

        :return: The size of this IpGroup.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this IpGroup.

        Ip地址组中包含Ip/Ip段的数量

        :param size: The size of this IpGroup.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, IpGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
