# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FrequencyControlRule:

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
        'producer': 'int',
        'name': 'str',
        'url': 'str',
        'limit_num': 'str',
        'limit_period': 'str',
        'lock_time': 'str',
        'tag_type': 'str',
        'tag_index': 'str',
        'tag_condition': 'TagCondition',
        'action': 'ActionInfo',
        'mode': 'str',
        'conditions': 'list[Condition]',
        'unlock_num': 'int',
        'domain_aggregation': 'bool',
        'region_aggregation': 'bool',
        'captcha_lock_time': 'int',
        'grayscale_time': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'producer': 'producer',
        'name': 'name',
        'url': 'url',
        'limit_num': 'limit_num',
        'limit_period': 'limit_period',
        'lock_time': 'lock_time',
        'tag_type': 'tag_type',
        'tag_index': 'tag_index',
        'tag_condition': 'tag_condition',
        'action': 'action',
        'mode': 'mode',
        'conditions': 'conditions',
        'unlock_num': 'unlock_num',
        'domain_aggregation': 'domain_aggregation',
        'region_aggregation': 'region_aggregation',
        'captcha_lock_time': 'captcha_lock_time',
        'grayscale_time': 'grayscale_time'
    }

    def __init__(self, id=None, producer=None, name=None, url=None, limit_num=None, limit_period=None, lock_time=None, tag_type=None, tag_index=None, tag_condition=None, action=None, mode=None, conditions=None, unlock_num=None, domain_aggregation=None, region_aggregation=None, captcha_lock_time=None, grayscale_time=None):
        r"""FrequencyControlRule

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param producer: 判断是否是智能cc生成的规则
        :type producer: int
        :param name: 规则名称
        :type name: str
        :param url: 规则应用的url
        :type url: str
        :param limit_num: 限速频率，单位为次，范围为1~2147483647
        :type limit_num: str
        :param limit_period: 限速周期，单位为秒，范围1~3600
        :type limit_period: str
        :param lock_time: 阻断时间，单位为秒，范围为0~65535
        :type lock_time: str
        :param tag_type: 限速模式：ip、cookie、header、other、policy、domain、url。 源限速：ip：IP限速，根据IP区分单个Web访问者。cookie：用户限速，根据Cookie键值区分单个Web访问者。header：用户限速，根据Header区分单个Web访问者。other：根据Referer（自定义请求访问的来源）字段区分单个Web访问者。-目的限速：policy: 策略限速、domain: 域名限速、url: url限速
        :type tag_type: str
        :param tag_index: 用户标识，当限速模式为用户限速(cookie或header)时
        :type tag_index: str
        :param tag_condition: 
        :type tag_condition: :class:`huaweicloudsdkaad.v2.TagCondition`
        :param action: 
        :type action: :class:`huaweicloudsdkaad.v2.ActionInfo`
        :param mode: cc规则防护模式，0：标准(老版本)，只支持对域名的防护路径做限制。1：高级(新版本)，支持对路径、IP、Cookie、Header、Params字段做限制。修改CC规则时必须传mode
        :type mode: str
        :param conditions: cc规则防护规则限速条件
        :type conditions: list[:class:`huaweicloudsdkaad.v2.Condition`]
        :param unlock_num: 放行频率，单位为次，范围为0~2147483647
        :type unlock_num: int
        :param domain_aggregation: 域名聚合统计
        :type domain_aggregation: bool
        :param region_aggregation: 全局计数
        :type region_aggregation: bool
        :param captcha_lock_time: 锁定验证时间
        :type captcha_lock_time: int
        :param grayscale_time: 是否灰度生效
        :type grayscale_time: bool
        """
        
        

        self._id = None
        self._producer = None
        self._name = None
        self._url = None
        self._limit_num = None
        self._limit_period = None
        self._lock_time = None
        self._tag_type = None
        self._tag_index = None
        self._tag_condition = None
        self._action = None
        self._mode = None
        self._conditions = None
        self._unlock_num = None
        self._domain_aggregation = None
        self._region_aggregation = None
        self._captcha_lock_time = None
        self._grayscale_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if producer is not None:
            self.producer = producer
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if limit_num is not None:
            self.limit_num = limit_num
        if limit_period is not None:
            self.limit_period = limit_period
        if lock_time is not None:
            self.lock_time = lock_time
        if tag_type is not None:
            self.tag_type = tag_type
        if tag_index is not None:
            self.tag_index = tag_index
        if tag_condition is not None:
            self.tag_condition = tag_condition
        if action is not None:
            self.action = action
        if mode is not None:
            self.mode = mode
        if conditions is not None:
            self.conditions = conditions
        if unlock_num is not None:
            self.unlock_num = unlock_num
        if domain_aggregation is not None:
            self.domain_aggregation = domain_aggregation
        if region_aggregation is not None:
            self.region_aggregation = region_aggregation
        if captcha_lock_time is not None:
            self.captcha_lock_time = captcha_lock_time
        if grayscale_time is not None:
            self.grayscale_time = grayscale_time

    @property
    def id(self):
        r"""Gets the id of this FrequencyControlRule.

        id

        :return: The id of this FrequencyControlRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FrequencyControlRule.

        id

        :param id: The id of this FrequencyControlRule.
        :type id: str
        """
        self._id = id

    @property
    def producer(self):
        r"""Gets the producer of this FrequencyControlRule.

        判断是否是智能cc生成的规则

        :return: The producer of this FrequencyControlRule.
        :rtype: int
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        r"""Sets the producer of this FrequencyControlRule.

        判断是否是智能cc生成的规则

        :param producer: The producer of this FrequencyControlRule.
        :type producer: int
        """
        self._producer = producer

    @property
    def name(self):
        r"""Gets the name of this FrequencyControlRule.

        规则名称

        :return: The name of this FrequencyControlRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FrequencyControlRule.

        规则名称

        :param name: The name of this FrequencyControlRule.
        :type name: str
        """
        self._name = name

    @property
    def url(self):
        r"""Gets the url of this FrequencyControlRule.

        规则应用的url

        :return: The url of this FrequencyControlRule.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this FrequencyControlRule.

        规则应用的url

        :param url: The url of this FrequencyControlRule.
        :type url: str
        """
        self._url = url

    @property
    def limit_num(self):
        r"""Gets the limit_num of this FrequencyControlRule.

        限速频率，单位为次，范围为1~2147483647

        :return: The limit_num of this FrequencyControlRule.
        :rtype: str
        """
        return self._limit_num

    @limit_num.setter
    def limit_num(self, limit_num):
        r"""Sets the limit_num of this FrequencyControlRule.

        限速频率，单位为次，范围为1~2147483647

        :param limit_num: The limit_num of this FrequencyControlRule.
        :type limit_num: str
        """
        self._limit_num = limit_num

    @property
    def limit_period(self):
        r"""Gets the limit_period of this FrequencyControlRule.

        限速周期，单位为秒，范围1~3600

        :return: The limit_period of this FrequencyControlRule.
        :rtype: str
        """
        return self._limit_period

    @limit_period.setter
    def limit_period(self, limit_period):
        r"""Sets the limit_period of this FrequencyControlRule.

        限速周期，单位为秒，范围1~3600

        :param limit_period: The limit_period of this FrequencyControlRule.
        :type limit_period: str
        """
        self._limit_period = limit_period

    @property
    def lock_time(self):
        r"""Gets the lock_time of this FrequencyControlRule.

        阻断时间，单位为秒，范围为0~65535

        :return: The lock_time of this FrequencyControlRule.
        :rtype: str
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this FrequencyControlRule.

        阻断时间，单位为秒，范围为0~65535

        :param lock_time: The lock_time of this FrequencyControlRule.
        :type lock_time: str
        """
        self._lock_time = lock_time

    @property
    def tag_type(self):
        r"""Gets the tag_type of this FrequencyControlRule.

        限速模式：ip、cookie、header、other、policy、domain、url。 源限速：ip：IP限速，根据IP区分单个Web访问者。cookie：用户限速，根据Cookie键值区分单个Web访问者。header：用户限速，根据Header区分单个Web访问者。other：根据Referer（自定义请求访问的来源）字段区分单个Web访问者。-目的限速：policy: 策略限速、domain: 域名限速、url: url限速

        :return: The tag_type of this FrequencyControlRule.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        r"""Sets the tag_type of this FrequencyControlRule.

        限速模式：ip、cookie、header、other、policy、domain、url。 源限速：ip：IP限速，根据IP区分单个Web访问者。cookie：用户限速，根据Cookie键值区分单个Web访问者。header：用户限速，根据Header区分单个Web访问者。other：根据Referer（自定义请求访问的来源）字段区分单个Web访问者。-目的限速：policy: 策略限速、domain: 域名限速、url: url限速

        :param tag_type: The tag_type of this FrequencyControlRule.
        :type tag_type: str
        """
        self._tag_type = tag_type

    @property
    def tag_index(self):
        r"""Gets the tag_index of this FrequencyControlRule.

        用户标识，当限速模式为用户限速(cookie或header)时

        :return: The tag_index of this FrequencyControlRule.
        :rtype: str
        """
        return self._tag_index

    @tag_index.setter
    def tag_index(self, tag_index):
        r"""Sets the tag_index of this FrequencyControlRule.

        用户标识，当限速模式为用户限速(cookie或header)时

        :param tag_index: The tag_index of this FrequencyControlRule.
        :type tag_index: str
        """
        self._tag_index = tag_index

    @property
    def tag_condition(self):
        r"""Gets the tag_condition of this FrequencyControlRule.

        :return: The tag_condition of this FrequencyControlRule.
        :rtype: :class:`huaweicloudsdkaad.v2.TagCondition`
        """
        return self._tag_condition

    @tag_condition.setter
    def tag_condition(self, tag_condition):
        r"""Sets the tag_condition of this FrequencyControlRule.

        :param tag_condition: The tag_condition of this FrequencyControlRule.
        :type tag_condition: :class:`huaweicloudsdkaad.v2.TagCondition`
        """
        self._tag_condition = tag_condition

    @property
    def action(self):
        r"""Gets the action of this FrequencyControlRule.

        :return: The action of this FrequencyControlRule.
        :rtype: :class:`huaweicloudsdkaad.v2.ActionInfo`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this FrequencyControlRule.

        :param action: The action of this FrequencyControlRule.
        :type action: :class:`huaweicloudsdkaad.v2.ActionInfo`
        """
        self._action = action

    @property
    def mode(self):
        r"""Gets the mode of this FrequencyControlRule.

        cc规则防护模式，0：标准(老版本)，只支持对域名的防护路径做限制。1：高级(新版本)，支持对路径、IP、Cookie、Header、Params字段做限制。修改CC规则时必须传mode

        :return: The mode of this FrequencyControlRule.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this FrequencyControlRule.

        cc规则防护模式，0：标准(老版本)，只支持对域名的防护路径做限制。1：高级(新版本)，支持对路径、IP、Cookie、Header、Params字段做限制。修改CC规则时必须传mode

        :param mode: The mode of this FrequencyControlRule.
        :type mode: str
        """
        self._mode = mode

    @property
    def conditions(self):
        r"""Gets the conditions of this FrequencyControlRule.

        cc规则防护规则限速条件

        :return: The conditions of this FrequencyControlRule.
        :rtype: list[:class:`huaweicloudsdkaad.v2.Condition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this FrequencyControlRule.

        cc规则防护规则限速条件

        :param conditions: The conditions of this FrequencyControlRule.
        :type conditions: list[:class:`huaweicloudsdkaad.v2.Condition`]
        """
        self._conditions = conditions

    @property
    def unlock_num(self):
        r"""Gets the unlock_num of this FrequencyControlRule.

        放行频率，单位为次，范围为0~2147483647

        :return: The unlock_num of this FrequencyControlRule.
        :rtype: int
        """
        return self._unlock_num

    @unlock_num.setter
    def unlock_num(self, unlock_num):
        r"""Sets the unlock_num of this FrequencyControlRule.

        放行频率，单位为次，范围为0~2147483647

        :param unlock_num: The unlock_num of this FrequencyControlRule.
        :type unlock_num: int
        """
        self._unlock_num = unlock_num

    @property
    def domain_aggregation(self):
        r"""Gets the domain_aggregation of this FrequencyControlRule.

        域名聚合统计

        :return: The domain_aggregation of this FrequencyControlRule.
        :rtype: bool
        """
        return self._domain_aggregation

    @domain_aggregation.setter
    def domain_aggregation(self, domain_aggregation):
        r"""Sets the domain_aggregation of this FrequencyControlRule.

        域名聚合统计

        :param domain_aggregation: The domain_aggregation of this FrequencyControlRule.
        :type domain_aggregation: bool
        """
        self._domain_aggregation = domain_aggregation

    @property
    def region_aggregation(self):
        r"""Gets the region_aggregation of this FrequencyControlRule.

        全局计数

        :return: The region_aggregation of this FrequencyControlRule.
        :rtype: bool
        """
        return self._region_aggregation

    @region_aggregation.setter
    def region_aggregation(self, region_aggregation):
        r"""Sets the region_aggregation of this FrequencyControlRule.

        全局计数

        :param region_aggregation: The region_aggregation of this FrequencyControlRule.
        :type region_aggregation: bool
        """
        self._region_aggregation = region_aggregation

    @property
    def captcha_lock_time(self):
        r"""Gets the captcha_lock_time of this FrequencyControlRule.

        锁定验证时间

        :return: The captcha_lock_time of this FrequencyControlRule.
        :rtype: int
        """
        return self._captcha_lock_time

    @captcha_lock_time.setter
    def captcha_lock_time(self, captcha_lock_time):
        r"""Sets the captcha_lock_time of this FrequencyControlRule.

        锁定验证时间

        :param captcha_lock_time: The captcha_lock_time of this FrequencyControlRule.
        :type captcha_lock_time: int
        """
        self._captcha_lock_time = captcha_lock_time

    @property
    def grayscale_time(self):
        r"""Gets the grayscale_time of this FrequencyControlRule.

        是否灰度生效

        :return: The grayscale_time of this FrequencyControlRule.
        :rtype: bool
        """
        return self._grayscale_time

    @grayscale_time.setter
    def grayscale_time(self, grayscale_time):
        r"""Sets the grayscale_time of this FrequencyControlRule.

        是否灰度生效

        :param grayscale_time: The grayscale_time of this FrequencyControlRule.
        :type grayscale_time: bool
        """
        self._grayscale_time = grayscale_time

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
        if not isinstance(other, FrequencyControlRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
