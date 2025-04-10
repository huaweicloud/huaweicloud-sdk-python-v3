# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainVisibleServiceVo:

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
        'type': 'int',
        'execute_type': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'execute_type': 'execute_type'
    }

    def __init__(self, name=None, type=None, execute_type=None):
        r"""DomainVisibleServiceVo

        The model defined in huaweicloud sdk

        :param name: 第三方服务名
        :type name: str
        :param type: 第三方服务类型
        :type type: int
        :param execute_type: 第三方服务执行方式（0：普通TestHub，1：对接八爪鱼TestHub）
        :type execute_type: int
        """
        
        

        self._name = None
        self._type = None
        self._execute_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if execute_type is not None:
            self.execute_type = execute_type

    @property
    def name(self):
        r"""Gets the name of this DomainVisibleServiceVo.

        第三方服务名

        :return: The name of this DomainVisibleServiceVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DomainVisibleServiceVo.

        第三方服务名

        :param name: The name of this DomainVisibleServiceVo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this DomainVisibleServiceVo.

        第三方服务类型

        :return: The type of this DomainVisibleServiceVo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DomainVisibleServiceVo.

        第三方服务类型

        :param type: The type of this DomainVisibleServiceVo.
        :type type: int
        """
        self._type = type

    @property
    def execute_type(self):
        r"""Gets the execute_type of this DomainVisibleServiceVo.

        第三方服务执行方式（0：普通TestHub，1：对接八爪鱼TestHub）

        :return: The execute_type of this DomainVisibleServiceVo.
        :rtype: int
        """
        return self._execute_type

    @execute_type.setter
    def execute_type(self, execute_type):
        r"""Sets the execute_type of this DomainVisibleServiceVo.

        第三方服务执行方式（0：普通TestHub，1：对接八爪鱼TestHub）

        :param execute_type: The execute_type of this DomainVisibleServiceVo.
        :type execute_type: int
        """
        self._execute_type = execute_type

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
        if not isinstance(other, DomainVisibleServiceVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
