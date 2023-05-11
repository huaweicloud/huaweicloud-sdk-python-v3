# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateL7ruleReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'admin_state_up': 'bool',
        'type': 'str',
        'compare_type': 'str',
        'key': 'str',
        'value': 'str',
        'invert': 'bool'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'admin_state_up': 'admin_state_up',
        'type': 'type',
        'compare_type': 'compare_type',
        'key': 'key',
        'value': 'value',
        'invert': 'invert'
    }

    def __init__(self, tenant_id=None, admin_state_up=None, type=None, compare_type=None, key=None, value=None, invert=None):
        """CreateL7ruleReq

        The model defined in huaweicloud sdk

        :param tenant_id: 转发规则所在的项目ID。
        :type tenant_id: str
        :param admin_state_up: 转发规则的管理状态；该字段为预留字段，暂未启用。默认为true。
        :type admin_state_up: bool
        :param type: 转发规则的匹配内容
        :type type: str
        :param compare_type: 转发规则的匹配方式。type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为REGEX， STARTS_WITH，EQUAL_TO。
        :type compare_type: str
        :param key: 匹配内容的键值。目前匹配内容为HOST_NAME和PATH时，该字段不生效。该字段能更新但不会生效。
        :type key: str
        :param value: 匹配内容的值。其值不能包含空格。使用说明：当type为HOST_NAME时，取值范围：String(100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。当type为PATH时，取值范围：String(128)。当转发规则的compare_type为STARTS_WITH，EQUAL_TO时，字符串只能包含英文字母、数字、_~&#39;;@^-%#&amp;$.*+?,&#x3D;!:| /()[]{}，且必须以\&quot;/\&quot;开头。
        :type value: str
        :param invert: 是否反向匹配； 取值范围：true/false。默认值：false； 该字段为预留字段，暂未启用。
        :type invert: bool
        """
        
        

        self._tenant_id = None
        self._admin_state_up = None
        self._type = None
        self._compare_type = None
        self._key = None
        self._value = None
        self._invert = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        self.type = type
        self.compare_type = compare_type
        if key is not None:
            self.key = key
        self.value = value
        if invert is not None:
            self.invert = invert

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateL7ruleReq.

        转发规则所在的项目ID。

        :return: The tenant_id of this CreateL7ruleReq.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateL7ruleReq.

        转发规则所在的项目ID。

        :param tenant_id: The tenant_id of this CreateL7ruleReq.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateL7ruleReq.

        转发规则的管理状态；该字段为预留字段，暂未启用。默认为true。

        :return: The admin_state_up of this CreateL7ruleReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateL7ruleReq.

        转发规则的管理状态；该字段为预留字段，暂未启用。默认为true。

        :param admin_state_up: The admin_state_up of this CreateL7ruleReq.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def type(self):
        """Gets the type of this CreateL7ruleReq.

        转发规则的匹配内容

        :return: The type of this CreateL7ruleReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateL7ruleReq.

        转发规则的匹配内容

        :param type: The type of this CreateL7ruleReq.
        :type type: str
        """
        self._type = type

    @property
    def compare_type(self):
        """Gets the compare_type of this CreateL7ruleReq.

        转发规则的匹配方式。type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为REGEX， STARTS_WITH，EQUAL_TO。

        :return: The compare_type of this CreateL7ruleReq.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this CreateL7ruleReq.

        转发规则的匹配方式。type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为REGEX， STARTS_WITH，EQUAL_TO。

        :param compare_type: The compare_type of this CreateL7ruleReq.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def key(self):
        """Gets the key of this CreateL7ruleReq.

        匹配内容的键值。目前匹配内容为HOST_NAME和PATH时，该字段不生效。该字段能更新但不会生效。

        :return: The key of this CreateL7ruleReq.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateL7ruleReq.

        匹配内容的键值。目前匹配内容为HOST_NAME和PATH时，该字段不生效。该字段能更新但不会生效。

        :param key: The key of this CreateL7ruleReq.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this CreateL7ruleReq.

        匹配内容的值。其值不能包含空格。使用说明：当type为HOST_NAME时，取值范围：String(100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。当type为PATH时，取值范围：String(128)。当转发规则的compare_type为STARTS_WITH，EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:| /()[]{}，且必须以\"/\"开头。

        :return: The value of this CreateL7ruleReq.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateL7ruleReq.

        匹配内容的值。其值不能包含空格。使用说明：当type为HOST_NAME时，取值范围：String(100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。当type为PATH时，取值范围：String(128)。当转发规则的compare_type为STARTS_WITH，EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:| /()[]{}，且必须以\"/\"开头。

        :param value: The value of this CreateL7ruleReq.
        :type value: str
        """
        self._value = value

    @property
    def invert(self):
        """Gets the invert of this CreateL7ruleReq.

        是否反向匹配； 取值范围：true/false。默认值：false； 该字段为预留字段，暂未启用。

        :return: The invert of this CreateL7ruleReq.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        """Sets the invert of this CreateL7ruleReq.

        是否反向匹配； 取值范围：true/false。默认值：false； 该字段为预留字段，暂未启用。

        :param invert: The invert of this CreateL7ruleReq.
        :type invert: bool
        """
        self._invert = invert

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
        if not isinstance(other, CreateL7ruleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
