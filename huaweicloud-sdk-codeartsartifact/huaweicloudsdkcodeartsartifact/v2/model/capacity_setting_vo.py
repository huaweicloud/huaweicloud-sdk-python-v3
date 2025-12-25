# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CapacitySettingVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'capacity_threshold': 'int',
        'message_type': 'int',
        'is_mail_enabled': 'int',
        'is_sms_enabled': 'int'
    }

    attribute_map = {
        'capacity_threshold': 'capacity_threshold',
        'message_type': 'message_type',
        'is_mail_enabled': 'is_mail_enabled',
        'is_sms_enabled': 'is_sms_enabled'
    }

    def __init__(self, capacity_threshold=None, message_type=None, is_mail_enabled=None, is_sms_enabled=None):
        r"""CapacitySettingVO

        The model defined in huaweicloud sdk

        :param capacity_threshold: **参数解释**: 容量阈值。 **取值范围**: 不涉及。 
        :type capacity_threshold: int
        :param message_type: **参数解释**: 消息类型。 **取值范围**: 不涉及。 
        :type message_type: int
        :param is_mail_enabled: **参数解释**: 是否启用邮件。 **取值范围**: 不涉及。 
        :type is_mail_enabled: int
        :param is_sms_enabled: **参数解释**: 是否启用短信。 **取值范围**: 不涉及。 
        :type is_sms_enabled: int
        """
        
        

        self._capacity_threshold = None
        self._message_type = None
        self._is_mail_enabled = None
        self._is_sms_enabled = None
        self.discriminator = None

        if capacity_threshold is not None:
            self.capacity_threshold = capacity_threshold
        if message_type is not None:
            self.message_type = message_type
        if is_mail_enabled is not None:
            self.is_mail_enabled = is_mail_enabled
        if is_sms_enabled is not None:
            self.is_sms_enabled = is_sms_enabled

    @property
    def capacity_threshold(self):
        r"""Gets the capacity_threshold of this CapacitySettingVO.

        **参数解释**: 容量阈值。 **取值范围**: 不涉及。 

        :return: The capacity_threshold of this CapacitySettingVO.
        :rtype: int
        """
        return self._capacity_threshold

    @capacity_threshold.setter
    def capacity_threshold(self, capacity_threshold):
        r"""Sets the capacity_threshold of this CapacitySettingVO.

        **参数解释**: 容量阈值。 **取值范围**: 不涉及。 

        :param capacity_threshold: The capacity_threshold of this CapacitySettingVO.
        :type capacity_threshold: int
        """
        self._capacity_threshold = capacity_threshold

    @property
    def message_type(self):
        r"""Gets the message_type of this CapacitySettingVO.

        **参数解释**: 消息类型。 **取值范围**: 不涉及。 

        :return: The message_type of this CapacitySettingVO.
        :rtype: int
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        r"""Sets the message_type of this CapacitySettingVO.

        **参数解释**: 消息类型。 **取值范围**: 不涉及。 

        :param message_type: The message_type of this CapacitySettingVO.
        :type message_type: int
        """
        self._message_type = message_type

    @property
    def is_mail_enabled(self):
        r"""Gets the is_mail_enabled of this CapacitySettingVO.

        **参数解释**: 是否启用邮件。 **取值范围**: 不涉及。 

        :return: The is_mail_enabled of this CapacitySettingVO.
        :rtype: int
        """
        return self._is_mail_enabled

    @is_mail_enabled.setter
    def is_mail_enabled(self, is_mail_enabled):
        r"""Sets the is_mail_enabled of this CapacitySettingVO.

        **参数解释**: 是否启用邮件。 **取值范围**: 不涉及。 

        :param is_mail_enabled: The is_mail_enabled of this CapacitySettingVO.
        :type is_mail_enabled: int
        """
        self._is_mail_enabled = is_mail_enabled

    @property
    def is_sms_enabled(self):
        r"""Gets the is_sms_enabled of this CapacitySettingVO.

        **参数解释**: 是否启用短信。 **取值范围**: 不涉及。 

        :return: The is_sms_enabled of this CapacitySettingVO.
        :rtype: int
        """
        return self._is_sms_enabled

    @is_sms_enabled.setter
    def is_sms_enabled(self, is_sms_enabled):
        r"""Sets the is_sms_enabled of this CapacitySettingVO.

        **参数解释**: 是否启用短信。 **取值范围**: 不涉及。 

        :param is_sms_enabled: The is_sms_enabled of this CapacitySettingVO.
        :type is_sms_enabled: int
        """
        self._is_sms_enabled = is_sms_enabled

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
        if not isinstance(other, CapacitySettingVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
