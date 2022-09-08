# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateL7PolicyRuleOption:

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
        'type': 'str',
        'compare_type': 'str',
        'invert': 'bool',
        'key': 'str',
        'value': 'str',
        'conditions': 'list[CreateRuleCondition]'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'type': 'type',
        'compare_type': 'compare_type',
        'invert': 'invert',
        'key': 'key',
        'value': 'value',
        'conditions': 'conditions'
    }

    def __init__(self, admin_state_up=None, type=None, compare_type=None, invert=None, key=None, value=None, conditions=None):
        """CreateL7PolicyRuleOption

        The model defined in huaweicloud sdk

        :param admin_state_up: 转发规则的管理状态；取值范围： true/false，默认为true。  不支持该字段，请勿使用。
        :type admin_state_up: bool
        :param type: 转发规则类别。取值： - HOST_NAME：匹配域名 - PATH：匹配请求路径 [- METHOD：匹配请求方法 - HEADER：匹配请求头 - QUERY_STRING：匹配请求查询参数 - SOURCE_IP：匹配请求源IP地址](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)  使用说明： [一个l7policy下创建的l7rule的HOST_NAME，PATH，METHOD，SOURCE_IP不能重复。HEADER、QUERY_STRING支持重复的rule配置。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test) [一个l7policy下创建的l7rule的HOST_NAME，PATH不能重复。](tag:hcso_dt)
        :type type: str
        :param compare_type: 转发匹配方式。取值： - EQUAL_TO 表示精确匹配。 - REGEX 表示正则匹配。 - STARTS_WITH 表示前缀匹配。  使用说明： - type为HOST_NAME时仅支持EQUAL_TO，支持通配符*。 - type为PATH时可以为REGEX，STARTS_WITH，EQUAL_TO。 [- type为METHOD、SOURCE_IP时，仅支持EQUAL_TO。 - type为HEADER、QUERY_STRING，仅支持EQUAL_TO，支持通配符*、？。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)
        :type compare_type: str
        :param invert: 是否反向匹配；取值范围：true/false。默认值：false。  不支持该字段，请勿使用。
        :type invert: bool
        :param key: 匹配项的名称，比如转发规则匹配类型是请求头匹配，则key表示请求头参数的名称。  不支持该字段，请勿使用。
        :type key: str
        :param value: 匹配项的值，比如转发规则匹配类型是域名匹配，则value表示域名的值。[仅当conditions空时该字段生效。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)  当type为HOST_NAME时，字符串只能包含英文字母、数字、“-”、“.”或“*”，必须以字母、数字或“*”开头。若域名中包含“*”，则“*”只能出现在开头且必须以*.开始。当*开头时表示通配0~任一个字符。 当type为PATH时，当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~&#39;;@^-%#&amp;$.*+?,&#x3D;!:|\\/()\\[\\]{}，且必须以\&quot;/\&quot;开头。 [当type为METHOD、SOURCE_IP、HEADER,QUERY_STRING时，该字段无意义，使用conditions来指定key/value。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)
        :type value: str
        :param conditions: 转发规则的匹配条件。当监听器的高级转发策略功能（enhance_l7policy_enable）开启后才会生效。 配置了conditions后，字段key、字段value的值无意义。 若指定了conditons，该rule的条件数为conditons列表长度。 列表中key必须相同，value不允许重复。  [不支持该字段，请勿使用。](tag:hcso_dt)
        :type conditions: list[:class:`huaweicloudsdkelb.v3.CreateRuleCondition`]
        """
        
        

        self._admin_state_up = None
        self._type = None
        self._compare_type = None
        self._invert = None
        self._key = None
        self._value = None
        self._conditions = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        self.type = type
        self.compare_type = compare_type
        if invert is not None:
            self.invert = invert
        if key is not None:
            self.key = key
        self.value = value
        if conditions is not None:
            self.conditions = conditions

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateL7PolicyRuleOption.

        转发规则的管理状态；取值范围： true/false，默认为true。  不支持该字段，请勿使用。

        :return: The admin_state_up of this CreateL7PolicyRuleOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateL7PolicyRuleOption.

        转发规则的管理状态；取值范围： true/false，默认为true。  不支持该字段，请勿使用。

        :param admin_state_up: The admin_state_up of this CreateL7PolicyRuleOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def type(self):
        """Gets the type of this CreateL7PolicyRuleOption.

        转发规则类别。取值： - HOST_NAME：匹配域名 - PATH：匹配请求路径 [- METHOD：匹配请求方法 - HEADER：匹配请求头 - QUERY_STRING：匹配请求查询参数 - SOURCE_IP：匹配请求源IP地址](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)  使用说明： [一个l7policy下创建的l7rule的HOST_NAME，PATH，METHOD，SOURCE_IP不能重复。HEADER、QUERY_STRING支持重复的rule配置。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test) [一个l7policy下创建的l7rule的HOST_NAME，PATH不能重复。](tag:hcso_dt)

        :return: The type of this CreateL7PolicyRuleOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateL7PolicyRuleOption.

        转发规则类别。取值： - HOST_NAME：匹配域名 - PATH：匹配请求路径 [- METHOD：匹配请求方法 - HEADER：匹配请求头 - QUERY_STRING：匹配请求查询参数 - SOURCE_IP：匹配请求源IP地址](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)  使用说明： [一个l7policy下创建的l7rule的HOST_NAME，PATH，METHOD，SOURCE_IP不能重复。HEADER、QUERY_STRING支持重复的rule配置。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test) [一个l7policy下创建的l7rule的HOST_NAME，PATH不能重复。](tag:hcso_dt)

        :param type: The type of this CreateL7PolicyRuleOption.
        :type type: str
        """
        self._type = type

    @property
    def compare_type(self):
        """Gets the compare_type of this CreateL7PolicyRuleOption.

        转发匹配方式。取值： - EQUAL_TO 表示精确匹配。 - REGEX 表示正则匹配。 - STARTS_WITH 表示前缀匹配。  使用说明： - type为HOST_NAME时仅支持EQUAL_TO，支持通配符*。 - type为PATH时可以为REGEX，STARTS_WITH，EQUAL_TO。 [- type为METHOD、SOURCE_IP时，仅支持EQUAL_TO。 - type为HEADER、QUERY_STRING，仅支持EQUAL_TO，支持通配符*、？。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)

        :return: The compare_type of this CreateL7PolicyRuleOption.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this CreateL7PolicyRuleOption.

        转发匹配方式。取值： - EQUAL_TO 表示精确匹配。 - REGEX 表示正则匹配。 - STARTS_WITH 表示前缀匹配。  使用说明： - type为HOST_NAME时仅支持EQUAL_TO，支持通配符*。 - type为PATH时可以为REGEX，STARTS_WITH，EQUAL_TO。 [- type为METHOD、SOURCE_IP时，仅支持EQUAL_TO。 - type为HEADER、QUERY_STRING，仅支持EQUAL_TO，支持通配符*、？。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)

        :param compare_type: The compare_type of this CreateL7PolicyRuleOption.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def invert(self):
        """Gets the invert of this CreateL7PolicyRuleOption.

        是否反向匹配；取值范围：true/false。默认值：false。  不支持该字段，请勿使用。

        :return: The invert of this CreateL7PolicyRuleOption.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        """Sets the invert of this CreateL7PolicyRuleOption.

        是否反向匹配；取值范围：true/false。默认值：false。  不支持该字段，请勿使用。

        :param invert: The invert of this CreateL7PolicyRuleOption.
        :type invert: bool
        """
        self._invert = invert

    @property
    def key(self):
        """Gets the key of this CreateL7PolicyRuleOption.

        匹配项的名称，比如转发规则匹配类型是请求头匹配，则key表示请求头参数的名称。  不支持该字段，请勿使用。

        :return: The key of this CreateL7PolicyRuleOption.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateL7PolicyRuleOption.

        匹配项的名称，比如转发规则匹配类型是请求头匹配，则key表示请求头参数的名称。  不支持该字段，请勿使用。

        :param key: The key of this CreateL7PolicyRuleOption.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this CreateL7PolicyRuleOption.

        匹配项的值，比如转发规则匹配类型是域名匹配，则value表示域名的值。[仅当conditions空时该字段生效。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)  当type为HOST_NAME时，字符串只能包含英文字母、数字、“-”、“.”或“*”，必须以字母、数字或“*”开头。若域名中包含“*”，则“*”只能出现在开头且必须以*.开始。当*开头时表示通配0~任一个字符。 当type为PATH时，当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:|\\/()\\[\\]{}，且必须以\"/\"开头。 [当type为METHOD、SOURCE_IP、HEADER,QUERY_STRING时，该字段无意义，使用conditions来指定key/value。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)

        :return: The value of this CreateL7PolicyRuleOption.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateL7PolicyRuleOption.

        匹配项的值，比如转发规则匹配类型是域名匹配，则value表示域名的值。[仅当conditions空时该字段生效。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)  当type为HOST_NAME时，字符串只能包含英文字母、数字、“-”、“.”或“*”，必须以字母、数字或“*”开头。若域名中包含“*”，则“*”只能出现在开头且必须以*.开始。当*开头时表示通配0~任一个字符。 当type为PATH时，当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:|\\/()\\[\\]{}，且必须以\"/\"开头。 [当type为METHOD、SOURCE_IP、HEADER,QUERY_STRING时，该字段无意义，使用conditions来指定key/value。](tag:hws,hws_hk,ocb,tlf,ctc,hcs,sbc,g42,tm,cmcc,hk_g42,mix,hk_sbc,hws_ocb,fcs,dt,dt_test)

        :param value: The value of this CreateL7PolicyRuleOption.
        :type value: str
        """
        self._value = value

    @property
    def conditions(self):
        """Gets the conditions of this CreateL7PolicyRuleOption.

        转发规则的匹配条件。当监听器的高级转发策略功能（enhance_l7policy_enable）开启后才会生效。 配置了conditions后，字段key、字段value的值无意义。 若指定了conditons，该rule的条件数为conditons列表长度。 列表中key必须相同，value不允许重复。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :return: The conditions of this CreateL7PolicyRuleOption.
        :rtype: list[:class:`huaweicloudsdkelb.v3.CreateRuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this CreateL7PolicyRuleOption.

        转发规则的匹配条件。当监听器的高级转发策略功能（enhance_l7policy_enable）开启后才会生效。 配置了conditions后，字段key、字段value的值无意义。 若指定了conditons，该rule的条件数为conditons列表长度。 列表中key必须相同，value不允许重复。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :param conditions: The conditions of this CreateL7PolicyRuleOption.
        :type conditions: list[:class:`huaweicloudsdkelb.v3.CreateRuleCondition`]
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
        if not isinstance(other, CreateL7PolicyRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
