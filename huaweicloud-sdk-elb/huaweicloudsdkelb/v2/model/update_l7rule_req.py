# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateL7ruleReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compare_type': 'str',
        'admin_state_up': 'bool',
        'invert': 'bool',
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'compare_type': 'compare_type',
        'admin_state_up': 'admin_state_up',
        'invert': 'invert',
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, compare_type=None, admin_state_up=None, invert=None, key=None, value=None):
        """UpdateL7ruleReq

        The model defined in huaweicloud sdk

        :param compare_type: 转发匹配方式： type为HOST_NAME时，取值范围：EQUAL_TO：精确匹配；t ype为PATH时，取值范围：REGEX：正则匹配；STARTS_WITH：前缀匹配；EQUAL_TO：精确匹配。
        :type compare_type: str
        :param admin_state_up: 转发规则的管理状态；取值范围： true/false。该字段为预留字段，暂未启用。默认为true。
        :type admin_state_up: bool
        :param invert: 是否反向匹配；取值范围：true/false。默认值：false；该字段为预留字段，暂未启用。
        :type invert: bool
        :param key: 匹配内容的键值。默认为null。该字段为预留字段，暂未启用。
        :type key: str
        :param value: 匹配内容的值。不能包含空格。 当type为HOST_NAME时，取值范围：String (100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。 当type为PATH时，取值范围：String (128)。当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~&#39;;@^-%#&amp;$.*+?,&#x3D;!:| /()[]{}，且必须以\&quot;/\&quot;开头。
        :type value: str
        """
        
        

        self._compare_type = None
        self._admin_state_up = None
        self._invert = None
        self._key = None
        self._value = None
        self.discriminator = None

        if compare_type is not None:
            self.compare_type = compare_type
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if invert is not None:
            self.invert = invert
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def compare_type(self):
        """Gets the compare_type of this UpdateL7ruleReq.

        转发匹配方式： type为HOST_NAME时，取值范围：EQUAL_TO：精确匹配；t ype为PATH时，取值范围：REGEX：正则匹配；STARTS_WITH：前缀匹配；EQUAL_TO：精确匹配。

        :return: The compare_type of this UpdateL7ruleReq.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this UpdateL7ruleReq.

        转发匹配方式： type为HOST_NAME时，取值范围：EQUAL_TO：精确匹配；t ype为PATH时，取值范围：REGEX：正则匹配；STARTS_WITH：前缀匹配；EQUAL_TO：精确匹配。

        :param compare_type: The compare_type of this UpdateL7ruleReq.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateL7ruleReq.

        转发规则的管理状态；取值范围： true/false。该字段为预留字段，暂未启用。默认为true。

        :return: The admin_state_up of this UpdateL7ruleReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateL7ruleReq.

        转发规则的管理状态；取值范围： true/false。该字段为预留字段，暂未启用。默认为true。

        :param admin_state_up: The admin_state_up of this UpdateL7ruleReq.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def invert(self):
        """Gets the invert of this UpdateL7ruleReq.

        是否反向匹配；取值范围：true/false。默认值：false；该字段为预留字段，暂未启用。

        :return: The invert of this UpdateL7ruleReq.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        """Sets the invert of this UpdateL7ruleReq.

        是否反向匹配；取值范围：true/false。默认值：false；该字段为预留字段，暂未启用。

        :param invert: The invert of this UpdateL7ruleReq.
        :type invert: bool
        """
        self._invert = invert

    @property
    def key(self):
        """Gets the key of this UpdateL7ruleReq.

        匹配内容的键值。默认为null。该字段为预留字段，暂未启用。

        :return: The key of this UpdateL7ruleReq.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateL7ruleReq.

        匹配内容的键值。默认为null。该字段为预留字段，暂未启用。

        :param key: The key of this UpdateL7ruleReq.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this UpdateL7ruleReq.

        匹配内容的值。不能包含空格。 当type为HOST_NAME时，取值范围：String (100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。 当type为PATH时，取值范围：String (128)。当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:| /()[]{}，且必须以\"/\"开头。

        :return: The value of this UpdateL7ruleReq.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdateL7ruleReq.

        匹配内容的值。不能包含空格。 当type为HOST_NAME时，取值范围：String (100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。 当type为PATH时，取值范围：String (128)。当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:| /()[]{}，且必须以\"/\"开头。

        :param value: The value of this UpdateL7ruleReq.
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
        if not isinstance(other, UpdateL7ruleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
