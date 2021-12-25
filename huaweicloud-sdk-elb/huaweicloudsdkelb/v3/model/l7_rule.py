# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class L7Rule:


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
        'key': 'str',
        'project_id': 'str',
        'type': 'str',
        'value': 'str',
        'provisioning_status': 'str',
        'invert': 'bool',
        'id': 'str',
        'conditions': 'list[RuleCondition]'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'compare_type': 'compare_type',
        'key': 'key',
        'project_id': 'project_id',
        'type': 'type',
        'value': 'value',
        'provisioning_status': 'provisioning_status',
        'invert': 'invert',
        'id': 'id',
        'conditions': 'conditions'
    }

    def __init__(self, admin_state_up=None, compare_type=None, key=None, project_id=None, type=None, value=None, provisioning_status=None, invert=None, id=None, conditions=None):
        """L7Rule - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._compare_type = None
        self._key = None
        self._project_id = None
        self._type = None
        self._value = None
        self._provisioning_status = None
        self._invert = None
        self._id = None
        self._conditions = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.compare_type = compare_type
        self.key = key
        self.project_id = project_id
        self.type = type
        self.value = value
        self.provisioning_status = provisioning_status
        self.invert = invert
        self.id = id
        self.conditions = conditions

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this L7Rule.

        转发规则的管理状，默认为true。  不支持该字段，请勿使用。

        :return: The admin_state_up of this L7Rule.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this L7Rule.

        转发规则的管理状，默认为true。  不支持该字段，请勿使用。

        :param admin_state_up: The admin_state_up of this L7Rule.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def compare_type(self):
        """Gets the compare_type of this L7Rule.

        转发规则的匹配方式。type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为Perl类型的REGEX， STARTS_WITH，EQUAL_TO。

        :return: The compare_type of this L7Rule.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this L7Rule.

        转发规则的匹配方式。type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为Perl类型的REGEX， STARTS_WITH，EQUAL_TO。

        :param compare_type: The compare_type of this L7Rule.
        :type: str
        """
        self._compare_type = compare_type

    @property
    def key(self):
        """Gets the key of this L7Rule.

        匹配内容的键值。目前匹配内容为HOST_NAME和PATH时，该字段不生效。该字段能更新但不会生效。

        :return: The key of this L7Rule.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this L7Rule.

        匹配内容的键值。目前匹配内容为HOST_NAME和PATH时，该字段不生效。该字段能更新但不会生效。

        :param key: The key of this L7Rule.
        :type: str
        """
        self._key = key

    @property
    def project_id(self):
        """Gets the project_id of this L7Rule.

        转发规则所在的项目ID。

        :return: The project_id of this L7Rule.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this L7Rule.

        转发规则所在的项目ID。

        :param project_id: The project_id of this L7Rule.
        :type: str
        """
        self._project_id = project_id

    @property
    def type(self):
        """Gets the type of this L7Rule.

        一个l7policy下创建的l7rule的HOST_NAME，PATH，METHOD，SOURCE_IP 不能重复。HEADER、QUERY_STRING支持重复的rule配置。  匹配内容：可以为HOST_NAME,PATH,METHOD,HEADER,QUERY_STRING,SOURCE_IP

        :return: The type of this L7Rule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this L7Rule.

        一个l7policy下创建的l7rule的HOST_NAME，PATH，METHOD，SOURCE_IP 不能重复。HEADER、QUERY_STRING支持重复的rule配置。  匹配内容：可以为HOST_NAME,PATH,METHOD,HEADER,QUERY_STRING,SOURCE_IP

        :param type: The type of this L7Rule.
        :type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this L7Rule.

        匹配内容的值。仅当conditions空时该字段生效。 当type为HOST_NAME时，字符串只能包含英文字母、数字、“-”、“.”或“*”，必须以字母、数字或“*”开头。 若域名中包含“*”，则“*”只能出现在开头且必须以*.开始。当*开头时表示通配0~任一个字符。 当type为PATH时，当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!&#58;|/()[]{}，且必须以\"/\"开头。 当type为METHOD、SOURCE_IP、HEADER, QUERY_STRING时，该字段无意义，使用condition_pair来指定key，value。

        :return: The value of this L7Rule.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this L7Rule.

        匹配内容的值。仅当conditions空时该字段生效。 当type为HOST_NAME时，字符串只能包含英文字母、数字、“-”、“.”或“*”，必须以字母、数字或“*”开头。 若域名中包含“*”，则“*”只能出现在开头且必须以*.开始。当*开头时表示通配0~任一个字符。 当type为PATH时，当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!&#58;|/()[]{}，且必须以\"/\"开头。 当type为METHOD、SOURCE_IP、HEADER, QUERY_STRING时，该字段无意义，使用condition_pair来指定key，value。

        :param value: The value of this L7Rule.
        :type: str
        """
        self._value = value

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this L7Rule.

        provisioning状态，可以为ACTIVE、PENDING_CREATE 或者ERROR。 说明：该字段无实际含义，默认为ACTIVE。

        :return: The provisioning_status of this L7Rule.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this L7Rule.

        provisioning状态，可以为ACTIVE、PENDING_CREATE 或者ERROR。 说明：该字段无实际含义，默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this L7Rule.
        :type: str
        """
        self._provisioning_status = provisioning_status

    @property
    def invert(self):
        """Gets the invert of this L7Rule.

        是否反向匹配。 使用说明： - 固定为false。该字段能更新但不会生效。

        :return: The invert of this L7Rule.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        """Sets the invert of this L7Rule.

        是否反向匹配。 使用说明： - 固定为false。该字段能更新但不会生效。

        :param invert: The invert of this L7Rule.
        :type: bool
        """
        self._invert = invert

    @property
    def id(self):
        """Gets the id of this L7Rule.

        规则ID。

        :return: The id of this L7Rule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this L7Rule.

        规则ID。

        :param id: The id of this L7Rule.
        :type: str
        """
        self._id = id

    @property
    def conditions(self):
        """Gets the conditions of this L7Rule.

        转发规则的匹配条件。当监听器的高级转发策略功能（enhance_l7policy_enable）开启后才会生效。 配置了conditions后，字段key、字段value的值无意义。 若指定了conditons，该rule的条件数为conditons列表长度。 列表中key必须相同，value不允许重复。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :return: The conditions of this L7Rule.
        :rtype: list[RuleCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this L7Rule.

        转发规则的匹配条件。当监听器的高级转发策略功能（enhance_l7policy_enable）开启后才会生效。 配置了conditions后，字段key、字段value的值无意义。 若指定了conditons，该rule的条件数为conditons列表长度。 列表中key必须相同，value不允许重复。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :param conditions: The conditions of this L7Rule.
        :type: list[RuleCondition]
        """
        self._conditions = conditions

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
        if not isinstance(other, L7Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
