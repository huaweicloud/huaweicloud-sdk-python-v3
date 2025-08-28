# coding: utf-8

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
        'conditions': 'list[RuleCondition]',
        'created_at': 'str',
        'updated_at': 'str'
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
        'conditions': 'conditions',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, admin_state_up=None, compare_type=None, key=None, project_id=None, type=None, value=None, provisioning_status=None, invert=None, id=None, conditions=None, created_at=None, updated_at=None):
        r"""L7Rule

        The model defined in huaweicloud sdk

        :param admin_state_up: **参数解释**：转发规则的管理状。  **取值范围**：固定为true。  不支持该字段，请勿使用。
        :type admin_state_up: bool
        :param compare_type: **参数解释**：转发规则的匹配方式。  **取值范围**：type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为REGEX，STARTS_WITH，EQUAL_TO。
        :type compare_type: str
        :param key: **参数解释**：匹配内容的键值。  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:hcso_dt)
        :type key: str
        :param project_id: **参数解释**：转发规则所在的项目ID。  **取值范围**：不涉及
        :type project_id: str
        :param type: **参数解释**：转发规则类别。  **取值范围**： - HOST_NAME：匹配域名。 - PATH：匹配请求路径。 - METHOD：匹配请求方法。 - HEADER：匹配请求头。 - QUERY_STRING：匹配请求查询参数。 - SOURCE_IP：匹配请求源IP地址。 - COOKIE: 匹配cookie信息。
        :type type: str
        :param value: **参数解释**：匹配内容的值。  **取值范围**： - 当type为HOST_NAME时，字符串只能包含英文字母、数字、-.*，必须以字母、数字或*开头。若域名中包含*，则*只能出现在开头且必须以*.开始。当*开头时表示通配0~任一个字符。 - 当type为PATH时，当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~&#39;;@^-%#&amp;$.*+?,&#x3D;!:|\\/()\\[\\]{}，且必须以/开头。 - 当type为METHOD、SOURCE_IP、HEADER, QUERY_STRING时，该字段无意义，使用conditions来指定key，value。
        :type value: str
        :param provisioning_status: **参数解释**：provisioning状态。该字段无效，默认为ACTIVE。  **取值范围**：ACTIVE、PENDING_CREATE 或者ERROR。
        :type provisioning_status: str
        :param invert: **参数解释**：是否反向匹配。  **取值范围**：不涉及
        :type invert: bool
        :param id: **参数解释**：规则ID。  **取值范围**：不涉及
        :type id: str
        :param conditions: **参数解释**：转发规则的匹配条件。  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:hcso_dt)  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type conditions: list[:class:`huaweicloudsdkelb.v3.RuleCondition`]
        :param created_at: **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)
        :type created_at: str
        :param updated_at: **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)
        :type updated_at: str
        """
        
        

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
        self._created_at = None
        self._updated_at = None
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
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this L7Rule.

        **参数解释**：转发规则的管理状。  **取值范围**：固定为true。  不支持该字段，请勿使用。

        :return: The admin_state_up of this L7Rule.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this L7Rule.

        **参数解释**：转发规则的管理状。  **取值范围**：固定为true。  不支持该字段，请勿使用。

        :param admin_state_up: The admin_state_up of this L7Rule.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def compare_type(self):
        r"""Gets the compare_type of this L7Rule.

        **参数解释**：转发规则的匹配方式。  **取值范围**：type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为REGEX，STARTS_WITH，EQUAL_TO。

        :return: The compare_type of this L7Rule.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        r"""Sets the compare_type of this L7Rule.

        **参数解释**：转发规则的匹配方式。  **取值范围**：type为HOST_NAME时可以为EQUAL_TO。type为PATH时可以为REGEX，STARTS_WITH，EQUAL_TO。

        :param compare_type: The compare_type of this L7Rule.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def key(self):
        r"""Gets the key of this L7Rule.

        **参数解释**：匹配内容的键值。  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:hcso_dt)

        :return: The key of this L7Rule.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this L7Rule.

        **参数解释**：匹配内容的键值。  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:hcso_dt)

        :param key: The key of this L7Rule.
        :type key: str
        """
        self._key = key

    @property
    def project_id(self):
        r"""Gets the project_id of this L7Rule.

        **参数解释**：转发规则所在的项目ID。  **取值范围**：不涉及

        :return: The project_id of this L7Rule.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this L7Rule.

        **参数解释**：转发规则所在的项目ID。  **取值范围**：不涉及

        :param project_id: The project_id of this L7Rule.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        r"""Gets the type of this L7Rule.

        **参数解释**：转发规则类别。  **取值范围**： - HOST_NAME：匹配域名。 - PATH：匹配请求路径。 - METHOD：匹配请求方法。 - HEADER：匹配请求头。 - QUERY_STRING：匹配请求查询参数。 - SOURCE_IP：匹配请求源IP地址。 - COOKIE: 匹配cookie信息。

        :return: The type of this L7Rule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this L7Rule.

        **参数解释**：转发规则类别。  **取值范围**： - HOST_NAME：匹配域名。 - PATH：匹配请求路径。 - METHOD：匹配请求方法。 - HEADER：匹配请求头。 - QUERY_STRING：匹配请求查询参数。 - SOURCE_IP：匹配请求源IP地址。 - COOKIE: 匹配cookie信息。

        :param type: The type of this L7Rule.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this L7Rule.

        **参数解释**：匹配内容的值。  **取值范围**： - 当type为HOST_NAME时，字符串只能包含英文字母、数字、-.*，必须以字母、数字或*开头。若域名中包含*，则*只能出现在开头且必须以*.开始。当*开头时表示通配0~任一个字符。 - 当type为PATH时，当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:|\\/()\\[\\]{}，且必须以/开头。 - 当type为METHOD、SOURCE_IP、HEADER, QUERY_STRING时，该字段无意义，使用conditions来指定key，value。

        :return: The value of this L7Rule.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this L7Rule.

        **参数解释**：匹配内容的值。  **取值范围**： - 当type为HOST_NAME时，字符串只能包含英文字母、数字、-.*，必须以字母、数字或*开头。若域名中包含*，则*只能出现在开头且必须以*.开始。当*开头时表示通配0~任一个字符。 - 当type为PATH时，当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:|\\/()\\[\\]{}，且必须以/开头。 - 当type为METHOD、SOURCE_IP、HEADER, QUERY_STRING时，该字段无意义，使用conditions来指定key，value。

        :param value: The value of this L7Rule.
        :type value: str
        """
        self._value = value

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this L7Rule.

        **参数解释**：provisioning状态。该字段无效，默认为ACTIVE。  **取值范围**：ACTIVE、PENDING_CREATE 或者ERROR。

        :return: The provisioning_status of this L7Rule.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this L7Rule.

        **参数解释**：provisioning状态。该字段无效，默认为ACTIVE。  **取值范围**：ACTIVE、PENDING_CREATE 或者ERROR。

        :param provisioning_status: The provisioning_status of this L7Rule.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def invert(self):
        r"""Gets the invert of this L7Rule.

        **参数解释**：是否反向匹配。  **取值范围**：不涉及

        :return: The invert of this L7Rule.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        r"""Sets the invert of this L7Rule.

        **参数解释**：是否反向匹配。  **取值范围**：不涉及

        :param invert: The invert of this L7Rule.
        :type invert: bool
        """
        self._invert = invert

    @property
    def id(self):
        r"""Gets the id of this L7Rule.

        **参数解释**：规则ID。  **取值范围**：不涉及

        :return: The id of this L7Rule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this L7Rule.

        **参数解释**：规则ID。  **取值范围**：不涉及

        :param id: The id of this L7Rule.
        :type id: str
        """
        self._id = id

    @property
    def conditions(self):
        r"""Gets the conditions of this L7Rule.

        **参数解释**：转发规则的匹配条件。  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:hcso_dt)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The conditions of this L7Rule.
        :rtype: list[:class:`huaweicloudsdkelb.v3.RuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this L7Rule.

        **参数解释**：转发规则的匹配条件。  **取值范围**：不涉及  [不支持该字段，请勿使用。](tag:hcso_dt)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param conditions: The conditions of this L7Rule.
        :type conditions: list[:class:`huaweicloudsdkelb.v3.RuleCondition`]
        """
        self._conditions = conditions

    @property
    def created_at(self):
        r"""Gets the created_at of this L7Rule.

        **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :return: The created_at of this L7Rule.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this L7Rule.

        **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :param created_at: The created_at of this L7Rule.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this L7Rule.

        **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :return: The updated_at of this L7Rule.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this L7Rule.

        **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :param updated_at: The updated_at of this L7Rule.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
