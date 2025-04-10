# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestartClusterReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, type=None, value=None):
        r"""RestartClusterReq

        The model defined in huaweicloud sdk

        :param type: 操作角色。参数范围： - node - role
        :type type: str
        :param value: 操作参数。参数说明：  - 当操作角色为node时，value为节点ID,通过[查询集群详情](ShowClusterDetail.xml)获取instances中的id属性。  - 当操作角色为role时，value为节点类型(ess、ess-master、ess-client、ess-cold)的多种不同组合。
        :type value: str
        """
        
        

        self._type = None
        self._value = None
        self.discriminator = None

        self.type = type
        self.value = value

    @property
    def type(self):
        r"""Gets the type of this RestartClusterReq.

        操作角色。参数范围： - node - role

        :return: The type of this RestartClusterReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RestartClusterReq.

        操作角色。参数范围： - node - role

        :param type: The type of this RestartClusterReq.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this RestartClusterReq.

        操作参数。参数说明：  - 当操作角色为node时，value为节点ID,通过[查询集群详情](ShowClusterDetail.xml)获取instances中的id属性。  - 当操作角色为role时，value为节点类型(ess、ess-master、ess-client、ess-cold)的多种不同组合。

        :return: The value of this RestartClusterReq.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this RestartClusterReq.

        操作参数。参数说明：  - 当操作角色为node时，value为节点ID,通过[查询集群详情](ShowClusterDetail.xml)获取instances中的id属性。  - 当操作角色为role时，value为节点类型(ess、ess-master、ess-client、ess-cold)的多种不同组合。

        :param value: The value of this RestartClusterReq.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, RestartClusterReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
