# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCcRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'mode': 'int',
        'url': 'str',
        'conditions': 'list[CcCondition]',
        'action': 'CreateCcRuleRequestBodyAction',
        'tag_type': 'str',
        'tag_index': 'str',
        'tag_condition': 'CcrulesListInfoTagCondition',
        'limit_num': 'int',
        'limit_period': 'int',
        'unlock_num': 'int',
        'lock_time': 'int',
        'domain_aggregation': 'bool',
        'region_aggregation': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'mode': 'mode',
        'url': 'url',
        'conditions': 'conditions',
        'action': 'action',
        'tag_type': 'tag_type',
        'tag_index': 'tag_index',
        'tag_condition': 'tag_condition',
        'limit_num': 'limit_num',
        'limit_period': 'limit_period',
        'unlock_num': 'unlock_num',
        'lock_time': 'lock_time',
        'domain_aggregation': 'domain_aggregation',
        'region_aggregation': 'region_aggregation',
        'description': 'description'
    }

    def __init__(self, name=None, mode=None, url=None, conditions=None, action=None, tag_type=None, tag_index=None, tag_condition=None, limit_num=None, limit_period=None, unlock_num=None, lock_time=None, domain_aggregation=None, region_aggregation=None, description=None):
        """UpdateCcRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
        :param mode: cc规则防护模式，对应console上的mode，现在只支持创建高级cc规则防护模式。   - 0：标准，只支持对域名的防护路径做限制。  - 1：高级，支持对路径、IP、Cookie、Header、Params字段做限制。
        :type mode: int
        :param url: 需要防护的域名路径，当cc防护规则为标准模式（mode参数值为0）时，该参数必填。
        :type url: str
        :param conditions: cc规则防护规则限速条件，当cc防护规则为高级模式（mode参数值为1）时，该参数必填。
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CcCondition`]
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.CreateCcRuleRequestBodyAction`
        :param tag_type: 限速模式：   - ip：IP限速，根据IP区分单个Web访问者。   - cookie：用户限速，根据Cookie键值区分单个Web访问者。   - header：用户限速，根据Header区分单个Web访问者。   - other：根据Referer（自定义请求访问的来源）字段区分单个Web访问者。   - policy: 策略限速   - domain: 域名限速     - url: url限速
        :type tag_type: str
        :param tag_index: 用户标识，当限速模式为用户限速(cookie或header)时，需要传该参数。   - 选择cookie时，设置cookie字段名，即用户需要根据网站实际情况配置唯一可识别Web访问者的cookie中的某属性变量名。用户标识的cookie，不支持正则，必须完全匹配。例如：如果网站使用cookie中的某个字段name唯一标识用户，那么可以选取name字段来区分Web访问者。   - 选择header时，设置需要防护的自定义HTTP首部，即用户需要根据网站实际情况配置可识别Web访问者的HTTP首部。
        :type tag_index: str
        :param tag_condition: 
        :type tag_condition: :class:`huaweicloudsdkwaf.v1.CcrulesListInfoTagCondition`
        :param limit_num: 限制频率，单位为次，范围为1~2147483647
        :type limit_num: int
        :param limit_period: 限速周期，单位为秒，范围1~3600
        :type limit_period: int
        :param unlock_num: 放行频率，单位为次，范围为0~2147483647。只有当防护动作类型为dynamic_block时，才需要传该参数。
        :type unlock_num: int
        :param lock_time: 阻断时间，单位为秒，范围为0~65535。当“防护动作”选择“阻断”时，可设置阻断后恢复正常访问页面的时间。
        :type lock_time: int
        :param domain_aggregation: 是否开启域名聚合统计。
        :type domain_aggregation: bool
        :param region_aggregation: 是否开启全局计数。
        :type region_aggregation: bool
        :param description: 规则描述
        :type description: str
        """
        
        

        self._name = None
        self._mode = None
        self._url = None
        self._conditions = None
        self._action = None
        self._tag_type = None
        self._tag_index = None
        self._tag_condition = None
        self._limit_num = None
        self._limit_period = None
        self._unlock_num = None
        self._lock_time = None
        self._domain_aggregation = None
        self._region_aggregation = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.mode = mode
        if url is not None:
            self.url = url
        self.conditions = conditions
        self.action = action
        self.tag_type = tag_type
        if tag_index is not None:
            self.tag_index = tag_index
        if tag_condition is not None:
            self.tag_condition = tag_condition
        self.limit_num = limit_num
        self.limit_period = limit_period
        if unlock_num is not None:
            self.unlock_num = unlock_num
        if lock_time is not None:
            self.lock_time = lock_time
        if domain_aggregation is not None:
            self.domain_aggregation = domain_aggregation
        if region_aggregation is not None:
            self.region_aggregation = region_aggregation
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this UpdateCcRuleRequestBody.

        规则名称

        :return: The name of this UpdateCcRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCcRuleRequestBody.

        规则名称

        :param name: The name of this UpdateCcRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def mode(self):
        """Gets the mode of this UpdateCcRuleRequestBody.

        cc规则防护模式，对应console上的mode，现在只支持创建高级cc规则防护模式。   - 0：标准，只支持对域名的防护路径做限制。  - 1：高级，支持对路径、IP、Cookie、Header、Params字段做限制。

        :return: The mode of this UpdateCcRuleRequestBody.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this UpdateCcRuleRequestBody.

        cc规则防护模式，对应console上的mode，现在只支持创建高级cc规则防护模式。   - 0：标准，只支持对域名的防护路径做限制。  - 1：高级，支持对路径、IP、Cookie、Header、Params字段做限制。

        :param mode: The mode of this UpdateCcRuleRequestBody.
        :type mode: int
        """
        self._mode = mode

    @property
    def url(self):
        """Gets the url of this UpdateCcRuleRequestBody.

        需要防护的域名路径，当cc防护规则为标准模式（mode参数值为0）时，该参数必填。

        :return: The url of this UpdateCcRuleRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpdateCcRuleRequestBody.

        需要防护的域名路径，当cc防护规则为标准模式（mode参数值为0）时，该参数必填。

        :param url: The url of this UpdateCcRuleRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def conditions(self):
        """Gets the conditions of this UpdateCcRuleRequestBody.

        cc规则防护规则限速条件，当cc防护规则为高级模式（mode参数值为1）时，该参数必填。

        :return: The conditions of this UpdateCcRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CcCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this UpdateCcRuleRequestBody.

        cc规则防护规则限速条件，当cc防护规则为高级模式（mode参数值为1）时，该参数必填。

        :param conditions: The conditions of this UpdateCcRuleRequestBody.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CcCondition`]
        """
        self._conditions = conditions

    @property
    def action(self):
        """Gets the action of this UpdateCcRuleRequestBody.

        :return: The action of this UpdateCcRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateCcRuleRequestBodyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateCcRuleRequestBody.

        :param action: The action of this UpdateCcRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.CreateCcRuleRequestBodyAction`
        """
        self._action = action

    @property
    def tag_type(self):
        """Gets the tag_type of this UpdateCcRuleRequestBody.

        限速模式：   - ip：IP限速，根据IP区分单个Web访问者。   - cookie：用户限速，根据Cookie键值区分单个Web访问者。   - header：用户限速，根据Header区分单个Web访问者。   - other：根据Referer（自定义请求访问的来源）字段区分单个Web访问者。   - policy: 策略限速   - domain: 域名限速     - url: url限速

        :return: The tag_type of this UpdateCcRuleRequestBody.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        """Sets the tag_type of this UpdateCcRuleRequestBody.

        限速模式：   - ip：IP限速，根据IP区分单个Web访问者。   - cookie：用户限速，根据Cookie键值区分单个Web访问者。   - header：用户限速，根据Header区分单个Web访问者。   - other：根据Referer（自定义请求访问的来源）字段区分单个Web访问者。   - policy: 策略限速   - domain: 域名限速     - url: url限速

        :param tag_type: The tag_type of this UpdateCcRuleRequestBody.
        :type tag_type: str
        """
        self._tag_type = tag_type

    @property
    def tag_index(self):
        """Gets the tag_index of this UpdateCcRuleRequestBody.

        用户标识，当限速模式为用户限速(cookie或header)时，需要传该参数。   - 选择cookie时，设置cookie字段名，即用户需要根据网站实际情况配置唯一可识别Web访问者的cookie中的某属性变量名。用户标识的cookie，不支持正则，必须完全匹配。例如：如果网站使用cookie中的某个字段name唯一标识用户，那么可以选取name字段来区分Web访问者。   - 选择header时，设置需要防护的自定义HTTP首部，即用户需要根据网站实际情况配置可识别Web访问者的HTTP首部。

        :return: The tag_index of this UpdateCcRuleRequestBody.
        :rtype: str
        """
        return self._tag_index

    @tag_index.setter
    def tag_index(self, tag_index):
        """Sets the tag_index of this UpdateCcRuleRequestBody.

        用户标识，当限速模式为用户限速(cookie或header)时，需要传该参数。   - 选择cookie时，设置cookie字段名，即用户需要根据网站实际情况配置唯一可识别Web访问者的cookie中的某属性变量名。用户标识的cookie，不支持正则，必须完全匹配。例如：如果网站使用cookie中的某个字段name唯一标识用户，那么可以选取name字段来区分Web访问者。   - 选择header时，设置需要防护的自定义HTTP首部，即用户需要根据网站实际情况配置可识别Web访问者的HTTP首部。

        :param tag_index: The tag_index of this UpdateCcRuleRequestBody.
        :type tag_index: str
        """
        self._tag_index = tag_index

    @property
    def tag_condition(self):
        """Gets the tag_condition of this UpdateCcRuleRequestBody.

        :return: The tag_condition of this UpdateCcRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.CcrulesListInfoTagCondition`
        """
        return self._tag_condition

    @tag_condition.setter
    def tag_condition(self, tag_condition):
        """Sets the tag_condition of this UpdateCcRuleRequestBody.

        :param tag_condition: The tag_condition of this UpdateCcRuleRequestBody.
        :type tag_condition: :class:`huaweicloudsdkwaf.v1.CcrulesListInfoTagCondition`
        """
        self._tag_condition = tag_condition

    @property
    def limit_num(self):
        """Gets the limit_num of this UpdateCcRuleRequestBody.

        限制频率，单位为次，范围为1~2147483647

        :return: The limit_num of this UpdateCcRuleRequestBody.
        :rtype: int
        """
        return self._limit_num

    @limit_num.setter
    def limit_num(self, limit_num):
        """Sets the limit_num of this UpdateCcRuleRequestBody.

        限制频率，单位为次，范围为1~2147483647

        :param limit_num: The limit_num of this UpdateCcRuleRequestBody.
        :type limit_num: int
        """
        self._limit_num = limit_num

    @property
    def limit_period(self):
        """Gets the limit_period of this UpdateCcRuleRequestBody.

        限速周期，单位为秒，范围1~3600

        :return: The limit_period of this UpdateCcRuleRequestBody.
        :rtype: int
        """
        return self._limit_period

    @limit_period.setter
    def limit_period(self, limit_period):
        """Sets the limit_period of this UpdateCcRuleRequestBody.

        限速周期，单位为秒，范围1~3600

        :param limit_period: The limit_period of this UpdateCcRuleRequestBody.
        :type limit_period: int
        """
        self._limit_period = limit_period

    @property
    def unlock_num(self):
        """Gets the unlock_num of this UpdateCcRuleRequestBody.

        放行频率，单位为次，范围为0~2147483647。只有当防护动作类型为dynamic_block时，才需要传该参数。

        :return: The unlock_num of this UpdateCcRuleRequestBody.
        :rtype: int
        """
        return self._unlock_num

    @unlock_num.setter
    def unlock_num(self, unlock_num):
        """Sets the unlock_num of this UpdateCcRuleRequestBody.

        放行频率，单位为次，范围为0~2147483647。只有当防护动作类型为dynamic_block时，才需要传该参数。

        :param unlock_num: The unlock_num of this UpdateCcRuleRequestBody.
        :type unlock_num: int
        """
        self._unlock_num = unlock_num

    @property
    def lock_time(self):
        """Gets the lock_time of this UpdateCcRuleRequestBody.

        阻断时间，单位为秒，范围为0~65535。当“防护动作”选择“阻断”时，可设置阻断后恢复正常访问页面的时间。

        :return: The lock_time of this UpdateCcRuleRequestBody.
        :rtype: int
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this UpdateCcRuleRequestBody.

        阻断时间，单位为秒，范围为0~65535。当“防护动作”选择“阻断”时，可设置阻断后恢复正常访问页面的时间。

        :param lock_time: The lock_time of this UpdateCcRuleRequestBody.
        :type lock_time: int
        """
        self._lock_time = lock_time

    @property
    def domain_aggregation(self):
        """Gets the domain_aggregation of this UpdateCcRuleRequestBody.

        是否开启域名聚合统计。

        :return: The domain_aggregation of this UpdateCcRuleRequestBody.
        :rtype: bool
        """
        return self._domain_aggregation

    @domain_aggregation.setter
    def domain_aggregation(self, domain_aggregation):
        """Sets the domain_aggregation of this UpdateCcRuleRequestBody.

        是否开启域名聚合统计。

        :param domain_aggregation: The domain_aggregation of this UpdateCcRuleRequestBody.
        :type domain_aggregation: bool
        """
        self._domain_aggregation = domain_aggregation

    @property
    def region_aggregation(self):
        """Gets the region_aggregation of this UpdateCcRuleRequestBody.

        是否开启全局计数。

        :return: The region_aggregation of this UpdateCcRuleRequestBody.
        :rtype: bool
        """
        return self._region_aggregation

    @region_aggregation.setter
    def region_aggregation(self, region_aggregation):
        """Sets the region_aggregation of this UpdateCcRuleRequestBody.

        是否开启全局计数。

        :param region_aggregation: The region_aggregation of this UpdateCcRuleRequestBody.
        :type region_aggregation: bool
        """
        self._region_aggregation = region_aggregation

    @property
    def description(self):
        """Gets the description of this UpdateCcRuleRequestBody.

        规则描述

        :return: The description of this UpdateCcRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCcRuleRequestBody.

        规则描述

        :param description: The description of this UpdateCcRuleRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateCcRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
