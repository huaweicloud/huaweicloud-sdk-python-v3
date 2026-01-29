# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_urn': 'str',
        'type': 'str',
        'enable': 'bool'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'type': 'type',
        'enable': 'enable'
    }

    def __init__(self, topic_urn=None, type=None, enable=None):
        r"""AlertConfig

        The model defined in huaweicloud sdk

        :param topic_urn: 关联对应的smn topic；当type&#x3D;smn时，可以填写当前参数默认为空
        :type topic_urn: str
        :param type: 支持的订单告警类型，SMN为消息协议，MC为消息中心
        :type type: str
        :param enable: 开启或关闭当前告警配置，true为开启，false为关闭
        :type enable: bool
        """
        
        

        self._topic_urn = None
        self._type = None
        self._enable = None
        self.discriminator = None

        if topic_urn is not None:
            self.topic_urn = topic_urn
        if type is not None:
            self.type = type
        if enable is not None:
            self.enable = enable

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this AlertConfig.

        关联对应的smn topic；当type=smn时，可以填写当前参数默认为空

        :return: The topic_urn of this AlertConfig.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this AlertConfig.

        关联对应的smn topic；当type=smn时，可以填写当前参数默认为空

        :param topic_urn: The topic_urn of this AlertConfig.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def type(self):
        r"""Gets the type of this AlertConfig.

        支持的订单告警类型，SMN为消息协议，MC为消息中心

        :return: The type of this AlertConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AlertConfig.

        支持的订单告警类型，SMN为消息协议，MC为消息中心

        :param type: The type of this AlertConfig.
        :type type: str
        """
        self._type = type

    @property
    def enable(self):
        r"""Gets the enable of this AlertConfig.

        开启或关闭当前告警配置，true为开启，false为关闭

        :return: The enable of this AlertConfig.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this AlertConfig.

        开启或关闭当前告警配置，true为开启，false为关闭

        :param enable: The enable of this AlertConfig.
        :type enable: bool
        """
        self._enable = enable

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AlertConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
