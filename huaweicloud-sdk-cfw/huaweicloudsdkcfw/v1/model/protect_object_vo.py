# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectObjectVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'object_name': 'str',
        'type': 'int'
    }

    attribute_map = {
        'object_id': 'object_id',
        'object_name': 'object_name',
        'type': 'type'
    }

    def __init__(self, object_id=None, object_name=None, type=None):
        r"""ProtectObjectVO

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id。
        :type object_id: str
        :param object_name: 防护对象名称
        :type object_name: str
        :param type: 防护对象类型：0 南北向，1 东西向护对象类型
        :type type: int
        """
        
        

        self._object_id = None
        self._object_name = None
        self._type = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if object_name is not None:
            self.object_name = object_name
        if type is not None:
            self.type = type

    @property
    def object_id(self):
        r"""Gets the object_id of this ProtectObjectVO.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id。

        :return: The object_id of this ProtectObjectVO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ProtectObjectVO.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id。

        :param object_id: The object_id of this ProtectObjectVO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def object_name(self):
        r"""Gets the object_name of this ProtectObjectVO.

        防护对象名称

        :return: The object_name of this ProtectObjectVO.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this ProtectObjectVO.

        防护对象名称

        :param object_name: The object_name of this ProtectObjectVO.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def type(self):
        r"""Gets the type of this ProtectObjectVO.

        防护对象类型：0 南北向，1 东西向护对象类型

        :return: The type of this ProtectObjectVO.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ProtectObjectVO.

        防护对象类型：0 南北向，1 东西向护对象类型

        :param type: The type of this ProtectObjectVO.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, ProtectObjectVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
