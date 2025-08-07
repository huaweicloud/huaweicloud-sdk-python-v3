# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Listener:

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
        'id': 'str',
        'protocol': 'str',
        'protocol_port': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'protocol': 'protocol',
        'protocol_port': 'protocol_port'
    }

    def __init__(self, name=None, id=None, protocol=None, protocol_port=None):
        r"""Listener

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 监听器的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param id: **参数解释：** 监听器的ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: str
        :param protocol: **参数解释：** 监听器的监听协议 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type protocol: str
        :param protocol_port: **参数解释：** 监听器的监听端口 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type protocol_port: int
        """
        
        

        self._name = None
        self._id = None
        self._protocol = None
        self._protocol_port = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if protocol is not None:
            self.protocol = protocol
        if protocol_port is not None:
            self.protocol_port = protocol_port

    @property
    def name(self):
        r"""Gets the name of this Listener.

        **参数解释：** 监听器的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this Listener.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Listener.

        **参数解释：** 监听器的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this Listener.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this Listener.

        **参数解释：** 监听器的ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this Listener.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Listener.

        **参数解释：** 监听器的ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this Listener.
        :type id: str
        """
        self._id = id

    @property
    def protocol(self):
        r"""Gets the protocol of this Listener.

        **参数解释：** 监听器的监听协议 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The protocol of this Listener.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this Listener.

        **参数解释：** 监听器的监听协议 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param protocol: The protocol of this Listener.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this Listener.

        **参数解释：** 监听器的监听端口 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The protocol_port of this Listener.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this Listener.

        **参数解释：** 监听器的监听端口 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param protocol_port: The protocol_port of this Listener.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

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
        if not isinstance(other, Listener):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
