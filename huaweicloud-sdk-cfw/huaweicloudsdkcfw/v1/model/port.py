# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Port:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port_type': 'int',
        'ports': 'str'
    }

    attribute_map = {
        'port_type': 'port_type',
        'ports': 'ports'
    }

    def __init__(self, port_type=None, ports=None):
        r"""Port

        The model defined in huaweicloud sdk

        :param port_type: **参数解释**： 端口类型 **取值范围**： -1 Any，0 包含，1 排除
        :type port_type: int
        :param ports: **参数解释**： 端口 **取值范围**： 不涉及
        :type ports: str
        """
        
        

        self._port_type = None
        self._ports = None
        self.discriminator = None

        if port_type is not None:
            self.port_type = port_type
        if ports is not None:
            self.ports = ports

    @property
    def port_type(self):
        r"""Gets the port_type of this Port.

        **参数解释**： 端口类型 **取值范围**： -1 Any，0 包含，1 排除

        :return: The port_type of this Port.
        :rtype: int
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        r"""Sets the port_type of this Port.

        **参数解释**： 端口类型 **取值范围**： -1 Any，0 包含，1 排除

        :param port_type: The port_type of this Port.
        :type port_type: int
        """
        self._port_type = port_type

    @property
    def ports(self):
        r"""Gets the ports of this Port.

        **参数解释**： 端口 **取值范围**： 不涉及

        :return: The ports of this Port.
        :rtype: str
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        r"""Sets the ports of this Port.

        **参数解释**： 端口 **取值范围**： 不涉及

        :param ports: The ports of this Port.
        :type ports: str
        """
        self._ports = ports

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
        if not isinstance(other, Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
