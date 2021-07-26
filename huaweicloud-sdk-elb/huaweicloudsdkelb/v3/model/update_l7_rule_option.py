# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateL7RuleOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'compare_type': 'str',
        'invert': 'bool',
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'compare_type': 'compare_type',
        'invert': 'invert',
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, admin_state_up=None, compare_type=None, invert=None, key=None, value=None):
        """UpdateL7RuleOption - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._compare_type = None
        self._invert = None
        self._key = None
        self._value = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if compare_type is not None:
            self.compare_type = compare_type
        if invert is not None:
            self.invert = invert
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateL7RuleOption.

        转发规则的管理状态；该字段为预留字段，暂未启用。默认为true。

        :return: The admin_state_up of this UpdateL7RuleOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateL7RuleOption.

        转发规则的管理状态；该字段为预留字段，暂未启用。默认为true。

        :param admin_state_up: The admin_state_up of this UpdateL7RuleOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def compare_type(self):
        """Gets the compare_type of this UpdateL7RuleOption.

        转发规则的匹配方式。type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为REGEX， STARTS_WITH，EQUAL_TO。

        :return: The compare_type of this UpdateL7RuleOption.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this UpdateL7RuleOption.

        转发规则的匹配方式。type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为REGEX， STARTS_WITH，EQUAL_TO。

        :param compare_type: The compare_type of this UpdateL7RuleOption.
        :type: str
        """
        self._compare_type = compare_type

    @property
    def invert(self):
        """Gets the invert of this UpdateL7RuleOption.

        是否反向匹配。使用说明：固定为false。该字段能更新但不会生效。

        :return: The invert of this UpdateL7RuleOption.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        """Sets the invert of this UpdateL7RuleOption.

        是否反向匹配。使用说明：固定为false。该字段能更新但不会生效。

        :param invert: The invert of this UpdateL7RuleOption.
        :type: bool
        """
        self._invert = invert

    @property
    def key(self):
        """Gets the key of this UpdateL7RuleOption.

        匹配内容的键值。目前匹配内容为HOST_NAME和PATH时，该字段不生效。该字段能更新但不会生效。

        :return: The key of this UpdateL7RuleOption.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateL7RuleOption.

        匹配内容的键值。目前匹配内容为HOST_NAME和PATH时，该字段不生效。该字段能更新但不会生效。

        :param key: The key of this UpdateL7RuleOption.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this UpdateL7RuleOption.

        匹配内容的值。其值不能包含空格。使用说明：当type为HOST_NAME时，取值范围：String(100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。当type为PATH时，取值范围：String(128)。当转发规则的compare_type为STARTS_WITH，EQUAL_TO时，字符串只能包含英文字母、数字、^-%#&$.*+?,=!:| /()[]{}，且必须以\"/\"开头。

        :return: The value of this UpdateL7RuleOption.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdateL7RuleOption.

        匹配内容的值。其值不能包含空格。使用说明：当type为HOST_NAME时，取值范围：String(100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。当type为PATH时，取值范围：String(128)。当转发规则的compare_type为STARTS_WITH，EQUAL_TO时，字符串只能包含英文字母、数字、^-%#&$.*+?,=!:| /()[]{}，且必须以\"/\"开头。

        :param value: The value of this UpdateL7RuleOption.
        :type: str
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateL7RuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
