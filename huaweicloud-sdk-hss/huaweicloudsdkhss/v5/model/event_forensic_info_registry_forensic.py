# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventForensicInfoRegistryForensic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reg_key': 'str',
        'reg_value': 'str',
        'reg_new_key': 'str',
        'reg_op_type': 'str'
    }

    attribute_map = {
        'reg_key': 'reg_key',
        'reg_value': 'reg_value',
        'reg_new_key': 'reg_new_key',
        'reg_op_type': 'reg_op_type'
    }

    def __init__(self, reg_key=None, reg_value=None, reg_new_key=None, reg_op_type=None):
        r"""EventForensicInfoRegistryForensic

        The model defined in huaweicloud sdk

        :param reg_key: **参数解释**： 注册表KEY **取值范围**： 不涉及
        :type reg_key: str
        :param reg_value: **参数解释**： 注册表VALUE **取值范围**： 不涉及
        :type reg_value: str
        :param reg_new_key: **参数解释**： 注册表新KEY **取值范围**： 不涉及
        :type reg_new_key: str
        :param reg_op_type: **参数解释**： 注册表KEY/VALUE操作类型 **取值范围**： 不涉及
        :type reg_op_type: str
        """
        
        

        self._reg_key = None
        self._reg_value = None
        self._reg_new_key = None
        self._reg_op_type = None
        self.discriminator = None

        if reg_key is not None:
            self.reg_key = reg_key
        if reg_value is not None:
            self.reg_value = reg_value
        if reg_new_key is not None:
            self.reg_new_key = reg_new_key
        if reg_op_type is not None:
            self.reg_op_type = reg_op_type

    @property
    def reg_key(self):
        r"""Gets the reg_key of this EventForensicInfoRegistryForensic.

        **参数解释**： 注册表KEY **取值范围**： 不涉及

        :return: The reg_key of this EventForensicInfoRegistryForensic.
        :rtype: str
        """
        return self._reg_key

    @reg_key.setter
    def reg_key(self, reg_key):
        r"""Sets the reg_key of this EventForensicInfoRegistryForensic.

        **参数解释**： 注册表KEY **取值范围**： 不涉及

        :param reg_key: The reg_key of this EventForensicInfoRegistryForensic.
        :type reg_key: str
        """
        self._reg_key = reg_key

    @property
    def reg_value(self):
        r"""Gets the reg_value of this EventForensicInfoRegistryForensic.

        **参数解释**： 注册表VALUE **取值范围**： 不涉及

        :return: The reg_value of this EventForensicInfoRegistryForensic.
        :rtype: str
        """
        return self._reg_value

    @reg_value.setter
    def reg_value(self, reg_value):
        r"""Sets the reg_value of this EventForensicInfoRegistryForensic.

        **参数解释**： 注册表VALUE **取值范围**： 不涉及

        :param reg_value: The reg_value of this EventForensicInfoRegistryForensic.
        :type reg_value: str
        """
        self._reg_value = reg_value

    @property
    def reg_new_key(self):
        r"""Gets the reg_new_key of this EventForensicInfoRegistryForensic.

        **参数解释**： 注册表新KEY **取值范围**： 不涉及

        :return: The reg_new_key of this EventForensicInfoRegistryForensic.
        :rtype: str
        """
        return self._reg_new_key

    @reg_new_key.setter
    def reg_new_key(self, reg_new_key):
        r"""Sets the reg_new_key of this EventForensicInfoRegistryForensic.

        **参数解释**： 注册表新KEY **取值范围**： 不涉及

        :param reg_new_key: The reg_new_key of this EventForensicInfoRegistryForensic.
        :type reg_new_key: str
        """
        self._reg_new_key = reg_new_key

    @property
    def reg_op_type(self):
        r"""Gets the reg_op_type of this EventForensicInfoRegistryForensic.

        **参数解释**： 注册表KEY/VALUE操作类型 **取值范围**： 不涉及

        :return: The reg_op_type of this EventForensicInfoRegistryForensic.
        :rtype: str
        """
        return self._reg_op_type

    @reg_op_type.setter
    def reg_op_type(self, reg_op_type):
        r"""Sets the reg_op_type of this EventForensicInfoRegistryForensic.

        **参数解释**： 注册表KEY/VALUE操作类型 **取值范围**： 不涉及

        :param reg_op_type: The reg_op_type of this EventForensicInfoRegistryForensic.
        :type reg_op_type: str
        """
        self._reg_op_type = reg_op_type

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
        if not isinstance(other, EventForensicInfoRegistryForensic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
