# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetPhoneProperty:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone_id': 'str',
        '_property': 'str',
        'factory_reset_enabled': 'bool'
    }

    attribute_map = {
        'phone_id': 'phone_id',
        '_property': 'property',
        'factory_reset_enabled': 'factory_reset_enabled'
    }

    def __init__(self, phone_id=None, _property=None, factory_reset_enabled=None):
        r"""ResetPhoneProperty

        The model defined in huaweicloud sdk

        :param phone_id: 云手机id。
        :type phone_id: str
        :param _property: 云手机属性列表，为Json格式字符串。
        :type _property: str
        :param factory_reset_enabled: 是否恢复出厂设置，设为true 会在重置手机的基础上，清除手机所有历史属性配置记录。
        :type factory_reset_enabled: bool
        """
        
        

        self._phone_id = None
        self.__property = None
        self._factory_reset_enabled = None
        self.discriminator = None

        self.phone_id = phone_id
        if _property is not None:
            self._property = _property
        if factory_reset_enabled is not None:
            self.factory_reset_enabled = factory_reset_enabled

    @property
    def phone_id(self):
        r"""Gets the phone_id of this ResetPhoneProperty.

        云手机id。

        :return: The phone_id of this ResetPhoneProperty.
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        r"""Sets the phone_id of this ResetPhoneProperty.

        云手机id。

        :param phone_id: The phone_id of this ResetPhoneProperty.
        :type phone_id: str
        """
        self._phone_id = phone_id

    @property
    def _property(self):
        r"""Gets the _property of this ResetPhoneProperty.

        云手机属性列表，为Json格式字符串。

        :return: The _property of this ResetPhoneProperty.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        r"""Sets the _property of this ResetPhoneProperty.

        云手机属性列表，为Json格式字符串。

        :param _property: The _property of this ResetPhoneProperty.
        :type _property: str
        """
        self.__property = _property

    @property
    def factory_reset_enabled(self):
        r"""Gets the factory_reset_enabled of this ResetPhoneProperty.

        是否恢复出厂设置，设为true 会在重置手机的基础上，清除手机所有历史属性配置记录。

        :return: The factory_reset_enabled of this ResetPhoneProperty.
        :rtype: bool
        """
        return self._factory_reset_enabled

    @factory_reset_enabled.setter
    def factory_reset_enabled(self, factory_reset_enabled):
        r"""Sets the factory_reset_enabled of this ResetPhoneProperty.

        是否恢复出厂设置，设为true 会在重置手机的基础上，清除手机所有历史属性配置记录。

        :param factory_reset_enabled: The factory_reset_enabled of this ResetPhoneProperty.
        :type factory_reset_enabled: bool
        """
        self._factory_reset_enabled = factory_reset_enabled

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
        if not isinstance(other, ResetPhoneProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
