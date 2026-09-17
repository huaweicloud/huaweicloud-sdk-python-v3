# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatusVoIpd:

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
        'belonging': 'str'
    }

    attribute_map = {
        'name': 'name',
        'belonging': 'belonging'
    }

    def __init__(self, name=None, belonging=None):
        r"""StatusVoIpd

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 状态名称。 **取值范围**： 不涉及
        :type name: str
        :param belonging: **参数解释**： 工作项的状态属性。 **取值范围**： START、IN_PROGRESS、END。
        :type belonging: str
        """
        
        

        self._name = None
        self._belonging = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if belonging is not None:
            self.belonging = belonging

    @property
    def name(self):
        r"""Gets the name of this StatusVoIpd.

        **参数解释**： 状态名称。 **取值范围**： 不涉及

        :return: The name of this StatusVoIpd.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StatusVoIpd.

        **参数解释**： 状态名称。 **取值范围**： 不涉及

        :param name: The name of this StatusVoIpd.
        :type name: str
        """
        self._name = name

    @property
    def belonging(self):
        r"""Gets the belonging of this StatusVoIpd.

        **参数解释**： 工作项的状态属性。 **取值范围**： START、IN_PROGRESS、END。

        :return: The belonging of this StatusVoIpd.
        :rtype: str
        """
        return self._belonging

    @belonging.setter
    def belonging(self, belonging):
        r"""Sets the belonging of this StatusVoIpd.

        **参数解释**： 工作项的状态属性。 **取值范围**： START、IN_PROGRESS、END。

        :param belonging: The belonging of this StatusVoIpd.
        :type belonging: str
        """
        self._belonging = belonging

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
        if not isinstance(other, StatusVoIpd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
