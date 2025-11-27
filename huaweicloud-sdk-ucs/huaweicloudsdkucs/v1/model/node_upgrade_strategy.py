# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeUpgradeStrategy:

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
        'rolling_update': 'RollingUpdateNodeUpgradeStrategy'
    }

    attribute_map = {
        'type': 'type',
        'rolling_update': 'rollingUpdate'
    }

    def __init__(self, type=None, rolling_update=None):
        r"""NodeUpgradeStrategy

        The model defined in huaweicloud sdk

        :param type: 策略类型
        :type type: str
        :param rolling_update: 
        :type rolling_update: :class:`huaweicloudsdkucs.v1.RollingUpdateNodeUpgradeStrategy`
        """
        
        

        self._type = None
        self._rolling_update = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if rolling_update is not None:
            self.rolling_update = rolling_update

    @property
    def type(self):
        r"""Gets the type of this NodeUpgradeStrategy.

        策略类型

        :return: The type of this NodeUpgradeStrategy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NodeUpgradeStrategy.

        策略类型

        :param type: The type of this NodeUpgradeStrategy.
        :type type: str
        """
        self._type = type

    @property
    def rolling_update(self):
        r"""Gets the rolling_update of this NodeUpgradeStrategy.

        :return: The rolling_update of this NodeUpgradeStrategy.
        :rtype: :class:`huaweicloudsdkucs.v1.RollingUpdateNodeUpgradeStrategy`
        """
        return self._rolling_update

    @rolling_update.setter
    def rolling_update(self, rolling_update):
        r"""Sets the rolling_update of this NodeUpgradeStrategy.

        :param rolling_update: The rolling_update of this NodeUpgradeStrategy.
        :type rolling_update: :class:`huaweicloudsdkucs.v1.RollingUpdateNodeUpgradeStrategy`
        """
        self._rolling_update = rolling_update

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
        if not isinstance(other, NodeUpgradeStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
