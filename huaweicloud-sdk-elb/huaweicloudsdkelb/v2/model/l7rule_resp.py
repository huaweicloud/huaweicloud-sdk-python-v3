# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class L7ruleResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'provisioning_status': 'str',
        'tenant_id': 'str',
        'project_id': 'str',
        'admin_state_up': 'bool',
        'type': 'str',
        'compare_type': 'str',
        'invert': 'bool',
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'id': 'id',
        'provisioning_status': 'provisioning_status',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'admin_state_up': 'admin_state_up',
        'type': 'type',
        'compare_type': 'compare_type',
        'invert': 'invert',
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, id=None, provisioning_status=None, tenant_id=None, project_id=None, admin_state_up=None, type=None, compare_type=None, invert=None, key=None, value=None):
        """L7ruleResp

        The model defined in huaweicloud sdk

        :param id: 转发规则ID
        :type id: str
        :param provisioning_status: 转发规则的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。
        :type provisioning_status: str
        :param tenant_id: 转发规则所在的项目ID。
        :type tenant_id: str
        :param project_id: 转发规则所在的项目ID。
        :type project_id: str
        :param admin_state_up: 转发规则的管理状态；该字段为预留字段，暂未启用。默认为true。
        :type admin_state_up: bool
        :param type: 转发规则的匹配内容
        :type type: str
        :param compare_type: 转发规则的匹配方式。type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为REGEX， STARTS_WITH，EQUAL_TO。
        :type compare_type: str
        :param invert: 是否反向匹配。使用说明：固定为false。该字段能更新但不会生效。
        :type invert: bool
        :param key: 匹配内容的键值。目前匹配内容为HOST_NAME和PATH时，该字段不生效。该字段能更新但不会生效。
        :type key: str
        :param value: 匹配内容的值。其值不能包含空格。使用说明：当type为HOST_NAME时，取值范围：String(100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。当type为PATH时，取值范围：String(128)。当转发规则的compare_type为STARTS_WITH，EQUAL_TO时，字符串只能包含英文字母、数字、^-%#&amp;$.*+?,&#x3D;!:| /()[]{}，且必须以\&quot;/\&quot;开头。
        :type value: str
        """
        
        

        self._id = None
        self._provisioning_status = None
        self._tenant_id = None
        self._project_id = None
        self._admin_state_up = None
        self._type = None
        self._compare_type = None
        self._invert = None
        self._key = None
        self._value = None
        self.discriminator = None

        self.id = id
        self.provisioning_status = provisioning_status
        self.tenant_id = tenant_id
        self.project_id = project_id
        self.admin_state_up = admin_state_up
        self.type = type
        self.compare_type = compare_type
        self.invert = invert
        self.key = key
        self.value = value

    @property
    def id(self):
        """Gets the id of this L7ruleResp.

        转发规则ID

        :return: The id of this L7ruleResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this L7ruleResp.

        转发规则ID

        :param id: The id of this L7ruleResp.
        :type id: str
        """
        self._id = id

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this L7ruleResp.

        转发规则的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :return: The provisioning_status of this L7ruleResp.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this L7ruleResp.

        转发规则的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this L7ruleResp.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this L7ruleResp.

        转发规则所在的项目ID。

        :return: The tenant_id of this L7ruleResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this L7ruleResp.

        转发规则所在的项目ID。

        :param tenant_id: The tenant_id of this L7ruleResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this L7ruleResp.

        转发规则所在的项目ID。

        :return: The project_id of this L7ruleResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this L7ruleResp.

        转发规则所在的项目ID。

        :param project_id: The project_id of this L7ruleResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this L7ruleResp.

        转发规则的管理状态；该字段为预留字段，暂未启用。默认为true。

        :return: The admin_state_up of this L7ruleResp.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this L7ruleResp.

        转发规则的管理状态；该字段为预留字段，暂未启用。默认为true。

        :param admin_state_up: The admin_state_up of this L7ruleResp.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def type(self):
        """Gets the type of this L7ruleResp.

        转发规则的匹配内容

        :return: The type of this L7ruleResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this L7ruleResp.

        转发规则的匹配内容

        :param type: The type of this L7ruleResp.
        :type type: str
        """
        self._type = type

    @property
    def compare_type(self):
        """Gets the compare_type of this L7ruleResp.

        转发规则的匹配方式。type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为REGEX， STARTS_WITH，EQUAL_TO。

        :return: The compare_type of this L7ruleResp.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this L7ruleResp.

        转发规则的匹配方式。type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为REGEX， STARTS_WITH，EQUAL_TO。

        :param compare_type: The compare_type of this L7ruleResp.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def invert(self):
        """Gets the invert of this L7ruleResp.

        是否反向匹配。使用说明：固定为false。该字段能更新但不会生效。

        :return: The invert of this L7ruleResp.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        """Sets the invert of this L7ruleResp.

        是否反向匹配。使用说明：固定为false。该字段能更新但不会生效。

        :param invert: The invert of this L7ruleResp.
        :type invert: bool
        """
        self._invert = invert

    @property
    def key(self):
        """Gets the key of this L7ruleResp.

        匹配内容的键值。目前匹配内容为HOST_NAME和PATH时，该字段不生效。该字段能更新但不会生效。

        :return: The key of this L7ruleResp.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this L7ruleResp.

        匹配内容的键值。目前匹配内容为HOST_NAME和PATH时，该字段不生效。该字段能更新但不会生效。

        :param key: The key of this L7ruleResp.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this L7ruleResp.

        匹配内容的值。其值不能包含空格。使用说明：当type为HOST_NAME时，取值范围：String(100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。当type为PATH时，取值范围：String(128)。当转发规则的compare_type为STARTS_WITH，EQUAL_TO时，字符串只能包含英文字母、数字、^-%#&$.*+?,=!:| /()[]{}，且必须以\"/\"开头。

        :return: The value of this L7ruleResp.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this L7ruleResp.

        匹配内容的值。其值不能包含空格。使用说明：当type为HOST_NAME时，取值范围：String(100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。当type为PATH时，取值范围：String(128)。当转发规则的compare_type为STARTS_WITH，EQUAL_TO时，字符串只能包含英文字母、数字、^-%#&$.*+?,=!:| /()[]{}，且必须以\"/\"开头。

        :param value: The value of this L7ruleResp.
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
        if not isinstance(other, L7ruleResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
