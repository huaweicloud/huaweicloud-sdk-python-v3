# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CcrulesListInfo:

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
        'id': 'str',
        'policyid': 'str',
        'url': 'str',
        'prefix': 'bool',
        'mode': 'int',
        'status': 'int',
        'conditions': 'list[CcCondition]',
        'action': 'CcrulesListInfoAction',
        'tag_type': 'str',
        'tag_index': 'str',
        'tag_condition': 'CcrulesListInfoTagCondition',
        'limit_num': 'int',
        'limit_period': 'int',
        'unlock_num': 'int',
        'lock_time': 'int',
        'domain_aggregation': 'bool',
        'region_aggregation': 'bool',
        'description': 'str',
        'total_num': 'int',
        'unaggregation': 'bool',
        'aging_time': 'int',
        'producer': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'policyid': 'policyid',
        'url': 'url',
        'prefix': 'prefix',
        'mode': 'mode',
        'status': 'status',
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
        'description': 'description',
        'total_num': 'total_num',
        'unaggregation': 'unaggregation',
        'aging_time': 'aging_time',
        'producer': 'producer',
        'timestamp': 'timestamp'
    }

    def __init__(self, name=None, id=None, policyid=None, url=None, prefix=None, mode=None, status=None, conditions=None, action=None, tag_type=None, tag_index=None, tag_condition=None, limit_num=None, limit_period=None, unlock_num=None, lock_time=None, domain_aggregation=None, region_aggregation=None, description=None, total_num=None, unaggregation=None, aging_time=None, producer=None, timestamp=None):
        """CcrulesListInfo

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
        :param id: Rule ID.
        :type id: str
        :param policyid: Policy ID.
        :type policyid: str
        :param url: 当mode值为0时，该参数有返回值。规则应用的URL链接，不包含域名。
        :type url: str
        :param prefix: 路径是否为前缀模式，当防护url以*结束，则为前缀模式。当mode值为0时，该参数有返回值。
        :type prefix: bool
        :param mode: cc规则防护模式，对应console上的mode，现在只支持创建高级cc规则防护模式。   - 0：标准，只支持对域名的防护路径做限制。  - 1：高级，支持对路径、IP、Cookie、Header、Params字段做限制。
        :type mode: int
        :param status: 规则状态，0：关闭，1：开启
        :type status: int
        :param conditions: cc规则防护规则限速条件，当cc防护规则为高级模式（mode参数值为1）时，该参数必填。
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CcCondition`]
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.CcrulesListInfoAction`
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
        :param total_num: 该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数
        :type total_num: int
        :param unaggregation: 该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数
        :type unaggregation: bool
        :param aging_time: 规则老化时间，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数
        :type aging_time: int
        :param producer: 规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数
        :type producer: int
        :param timestamp: 创建规则时间戳
        :type timestamp: int
        """
        
        

        self._name = None
        self._id = None
        self._policyid = None
        self._url = None
        self._prefix = None
        self._mode = None
        self._status = None
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
        self._total_num = None
        self._unaggregation = None
        self._aging_time = None
        self._producer = None
        self._timestamp = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if url is not None:
            self.url = url
        if prefix is not None:
            self.prefix = prefix
        if mode is not None:
            self.mode = mode
        if status is not None:
            self.status = status
        if conditions is not None:
            self.conditions = conditions
        if action is not None:
            self.action = action
        if tag_type is not None:
            self.tag_type = tag_type
        if tag_index is not None:
            self.tag_index = tag_index
        if tag_condition is not None:
            self.tag_condition = tag_condition
        if limit_num is not None:
            self.limit_num = limit_num
        if limit_period is not None:
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
        if total_num is not None:
            self.total_num = total_num
        if unaggregation is not None:
            self.unaggregation = unaggregation
        if aging_time is not None:
            self.aging_time = aging_time
        if producer is not None:
            self.producer = producer
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def name(self):
        """Gets the name of this CcrulesListInfo.

        规则名称

        :return: The name of this CcrulesListInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CcrulesListInfo.

        规则名称

        :param name: The name of this CcrulesListInfo.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this CcrulesListInfo.

        Rule ID.

        :return: The id of this CcrulesListInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CcrulesListInfo.

        Rule ID.

        :param id: The id of this CcrulesListInfo.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this CcrulesListInfo.

        Policy ID.

        :return: The policyid of this CcrulesListInfo.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CcrulesListInfo.

        Policy ID.

        :param policyid: The policyid of this CcrulesListInfo.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def url(self):
        """Gets the url of this CcrulesListInfo.

        当mode值为0时，该参数有返回值。规则应用的URL链接，不包含域名。

        :return: The url of this CcrulesListInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CcrulesListInfo.

        当mode值为0时，该参数有返回值。规则应用的URL链接，不包含域名。

        :param url: The url of this CcrulesListInfo.
        :type url: str
        """
        self._url = url

    @property
    def prefix(self):
        """Gets the prefix of this CcrulesListInfo.

        路径是否为前缀模式，当防护url以*结束，则为前缀模式。当mode值为0时，该参数有返回值。

        :return: The prefix of this CcrulesListInfo.
        :rtype: bool
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this CcrulesListInfo.

        路径是否为前缀模式，当防护url以*结束，则为前缀模式。当mode值为0时，该参数有返回值。

        :param prefix: The prefix of this CcrulesListInfo.
        :type prefix: bool
        """
        self._prefix = prefix

    @property
    def mode(self):
        """Gets the mode of this CcrulesListInfo.

        cc规则防护模式，对应console上的mode，现在只支持创建高级cc规则防护模式。   - 0：标准，只支持对域名的防护路径做限制。  - 1：高级，支持对路径、IP、Cookie、Header、Params字段做限制。

        :return: The mode of this CcrulesListInfo.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CcrulesListInfo.

        cc规则防护模式，对应console上的mode，现在只支持创建高级cc规则防护模式。   - 0：标准，只支持对域名的防护路径做限制。  - 1：高级，支持对路径、IP、Cookie、Header、Params字段做限制。

        :param mode: The mode of this CcrulesListInfo.
        :type mode: int
        """
        self._mode = mode

    @property
    def status(self):
        """Gets the status of this CcrulesListInfo.

        规则状态，0：关闭，1：开启

        :return: The status of this CcrulesListInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CcrulesListInfo.

        规则状态，0：关闭，1：开启

        :param status: The status of this CcrulesListInfo.
        :type status: int
        """
        self._status = status

    @property
    def conditions(self):
        """Gets the conditions of this CcrulesListInfo.

        cc规则防护规则限速条件，当cc防护规则为高级模式（mode参数值为1）时，该参数必填。

        :return: The conditions of this CcrulesListInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CcCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this CcrulesListInfo.

        cc规则防护规则限速条件，当cc防护规则为高级模式（mode参数值为1）时，该参数必填。

        :param conditions: The conditions of this CcrulesListInfo.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CcCondition`]
        """
        self._conditions = conditions

    @property
    def action(self):
        """Gets the action of this CcrulesListInfo.

        :return: The action of this CcrulesListInfo.
        :rtype: :class:`huaweicloudsdkwaf.v1.CcrulesListInfoAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CcrulesListInfo.

        :param action: The action of this CcrulesListInfo.
        :type action: :class:`huaweicloudsdkwaf.v1.CcrulesListInfoAction`
        """
        self._action = action

    @property
    def tag_type(self):
        """Gets the tag_type of this CcrulesListInfo.

        限速模式：   - ip：IP限速，根据IP区分单个Web访问者。   - cookie：用户限速，根据Cookie键值区分单个Web访问者。   - header：用户限速，根据Header区分单个Web访问者。   - other：根据Referer（自定义请求访问的来源）字段区分单个Web访问者。   - policy: 策略限速   - domain: 域名限速     - url: url限速

        :return: The tag_type of this CcrulesListInfo.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        """Sets the tag_type of this CcrulesListInfo.

        限速模式：   - ip：IP限速，根据IP区分单个Web访问者。   - cookie：用户限速，根据Cookie键值区分单个Web访问者。   - header：用户限速，根据Header区分单个Web访问者。   - other：根据Referer（自定义请求访问的来源）字段区分单个Web访问者。   - policy: 策略限速   - domain: 域名限速     - url: url限速

        :param tag_type: The tag_type of this CcrulesListInfo.
        :type tag_type: str
        """
        self._tag_type = tag_type

    @property
    def tag_index(self):
        """Gets the tag_index of this CcrulesListInfo.

        用户标识，当限速模式为用户限速(cookie或header)时，需要传该参数。   - 选择cookie时，设置cookie字段名，即用户需要根据网站实际情况配置唯一可识别Web访问者的cookie中的某属性变量名。用户标识的cookie，不支持正则，必须完全匹配。例如：如果网站使用cookie中的某个字段name唯一标识用户，那么可以选取name字段来区分Web访问者。   - 选择header时，设置需要防护的自定义HTTP首部，即用户需要根据网站实际情况配置可识别Web访问者的HTTP首部。

        :return: The tag_index of this CcrulesListInfo.
        :rtype: str
        """
        return self._tag_index

    @tag_index.setter
    def tag_index(self, tag_index):
        """Sets the tag_index of this CcrulesListInfo.

        用户标识，当限速模式为用户限速(cookie或header)时，需要传该参数。   - 选择cookie时，设置cookie字段名，即用户需要根据网站实际情况配置唯一可识别Web访问者的cookie中的某属性变量名。用户标识的cookie，不支持正则，必须完全匹配。例如：如果网站使用cookie中的某个字段name唯一标识用户，那么可以选取name字段来区分Web访问者。   - 选择header时，设置需要防护的自定义HTTP首部，即用户需要根据网站实际情况配置可识别Web访问者的HTTP首部。

        :param tag_index: The tag_index of this CcrulesListInfo.
        :type tag_index: str
        """
        self._tag_index = tag_index

    @property
    def tag_condition(self):
        """Gets the tag_condition of this CcrulesListInfo.

        :return: The tag_condition of this CcrulesListInfo.
        :rtype: :class:`huaweicloudsdkwaf.v1.CcrulesListInfoTagCondition`
        """
        return self._tag_condition

    @tag_condition.setter
    def tag_condition(self, tag_condition):
        """Sets the tag_condition of this CcrulesListInfo.

        :param tag_condition: The tag_condition of this CcrulesListInfo.
        :type tag_condition: :class:`huaweicloudsdkwaf.v1.CcrulesListInfoTagCondition`
        """
        self._tag_condition = tag_condition

    @property
    def limit_num(self):
        """Gets the limit_num of this CcrulesListInfo.

        限制频率，单位为次，范围为1~2147483647

        :return: The limit_num of this CcrulesListInfo.
        :rtype: int
        """
        return self._limit_num

    @limit_num.setter
    def limit_num(self, limit_num):
        """Sets the limit_num of this CcrulesListInfo.

        限制频率，单位为次，范围为1~2147483647

        :param limit_num: The limit_num of this CcrulesListInfo.
        :type limit_num: int
        """
        self._limit_num = limit_num

    @property
    def limit_period(self):
        """Gets the limit_period of this CcrulesListInfo.

        限速周期，单位为秒，范围1~3600

        :return: The limit_period of this CcrulesListInfo.
        :rtype: int
        """
        return self._limit_period

    @limit_period.setter
    def limit_period(self, limit_period):
        """Sets the limit_period of this CcrulesListInfo.

        限速周期，单位为秒，范围1~3600

        :param limit_period: The limit_period of this CcrulesListInfo.
        :type limit_period: int
        """
        self._limit_period = limit_period

    @property
    def unlock_num(self):
        """Gets the unlock_num of this CcrulesListInfo.

        放行频率，单位为次，范围为0~2147483647。只有当防护动作类型为dynamic_block时，才需要传该参数。

        :return: The unlock_num of this CcrulesListInfo.
        :rtype: int
        """
        return self._unlock_num

    @unlock_num.setter
    def unlock_num(self, unlock_num):
        """Sets the unlock_num of this CcrulesListInfo.

        放行频率，单位为次，范围为0~2147483647。只有当防护动作类型为dynamic_block时，才需要传该参数。

        :param unlock_num: The unlock_num of this CcrulesListInfo.
        :type unlock_num: int
        """
        self._unlock_num = unlock_num

    @property
    def lock_time(self):
        """Gets the lock_time of this CcrulesListInfo.

        阻断时间，单位为秒，范围为0~65535。当“防护动作”选择“阻断”时，可设置阻断后恢复正常访问页面的时间。

        :return: The lock_time of this CcrulesListInfo.
        :rtype: int
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this CcrulesListInfo.

        阻断时间，单位为秒，范围为0~65535。当“防护动作”选择“阻断”时，可设置阻断后恢复正常访问页面的时间。

        :param lock_time: The lock_time of this CcrulesListInfo.
        :type lock_time: int
        """
        self._lock_time = lock_time

    @property
    def domain_aggregation(self):
        """Gets the domain_aggregation of this CcrulesListInfo.

        是否开启域名聚合统计。

        :return: The domain_aggregation of this CcrulesListInfo.
        :rtype: bool
        """
        return self._domain_aggregation

    @domain_aggregation.setter
    def domain_aggregation(self, domain_aggregation):
        """Sets the domain_aggregation of this CcrulesListInfo.

        是否开启域名聚合统计。

        :param domain_aggregation: The domain_aggregation of this CcrulesListInfo.
        :type domain_aggregation: bool
        """
        self._domain_aggregation = domain_aggregation

    @property
    def region_aggregation(self):
        """Gets the region_aggregation of this CcrulesListInfo.

        是否开启全局计数。

        :return: The region_aggregation of this CcrulesListInfo.
        :rtype: bool
        """
        return self._region_aggregation

    @region_aggregation.setter
    def region_aggregation(self, region_aggregation):
        """Sets the region_aggregation of this CcrulesListInfo.

        是否开启全局计数。

        :param region_aggregation: The region_aggregation of this CcrulesListInfo.
        :type region_aggregation: bool
        """
        self._region_aggregation = region_aggregation

    @property
    def description(self):
        """Gets the description of this CcrulesListInfo.

        规则描述

        :return: The description of this CcrulesListInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CcrulesListInfo.

        规则描述

        :param description: The description of this CcrulesListInfo.
        :type description: str
        """
        self._description = description

    @property
    def total_num(self):
        """Gets the total_num of this CcrulesListInfo.

        该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :return: The total_num of this CcrulesListInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this CcrulesListInfo.

        该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :param total_num: The total_num of this CcrulesListInfo.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def unaggregation(self):
        """Gets the unaggregation of this CcrulesListInfo.

        该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :return: The unaggregation of this CcrulesListInfo.
        :rtype: bool
        """
        return self._unaggregation

    @unaggregation.setter
    def unaggregation(self, unaggregation):
        """Sets the unaggregation of this CcrulesListInfo.

        该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :param unaggregation: The unaggregation of this CcrulesListInfo.
        :type unaggregation: bool
        """
        self._unaggregation = unaggregation

    @property
    def aging_time(self):
        """Gets the aging_time of this CcrulesListInfo.

        规则老化时间，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :return: The aging_time of this CcrulesListInfo.
        :rtype: int
        """
        return self._aging_time

    @aging_time.setter
    def aging_time(self, aging_time):
        """Sets the aging_time of this CcrulesListInfo.

        规则老化时间，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :param aging_time: The aging_time of this CcrulesListInfo.
        :type aging_time: int
        """
        self._aging_time = aging_time

    @property
    def producer(self):
        """Gets the producer of this CcrulesListInfo.

        规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :return: The producer of this CcrulesListInfo.
        :rtype: int
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this CcrulesListInfo.

        规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :param producer: The producer of this CcrulesListInfo.
        :type producer: int
        """
        self._producer = producer

    @property
    def timestamp(self):
        """Gets the timestamp of this CcrulesListInfo.

        创建规则时间戳

        :return: The timestamp of this CcrulesListInfo.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CcrulesListInfo.

        创建规则时间戳

        :param timestamp: The timestamp of this CcrulesListInfo.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, CcrulesListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
