# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDbCacheRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dbcache_rule_id': 'str',
        'value_columns': 'list[str]',
        'ttl': 'str',
        'value_separator': 'str'
    }

    attribute_map = {
        'dbcache_rule_id': 'dbcache_rule_id',
        'value_columns': 'value_columns',
        'ttl': 'ttl',
        'value_separator': 'value_separator'
    }

    def __init__(self, dbcache_rule_id=None, value_columns=None, ttl=None, value_separator=None):
        r"""UpdateDbCacheRuleRequestBody

        The model defined in huaweicloud sdk

        :param dbcache_rule_id: 内存加速规则ID。
        :type dbcache_rule_id: str
        :param value_columns: 映射的value使用的column列表。
        :type value_columns: list[str]
        :param ttl: key的生存时间。单位:ms。不传该值，默认取2592000000，表示30天。
        :type ttl: str
        :param value_separator: 映射的value分隔符。只允许一个字符。
        :type value_separator: str
        """
        
        

        self._dbcache_rule_id = None
        self._value_columns = None
        self._ttl = None
        self._value_separator = None
        self.discriminator = None

        self.dbcache_rule_id = dbcache_rule_id
        self.value_columns = value_columns
        if ttl is not None:
            self.ttl = ttl
        if value_separator is not None:
            self.value_separator = value_separator

    @property
    def dbcache_rule_id(self):
        r"""Gets the dbcache_rule_id of this UpdateDbCacheRuleRequestBody.

        内存加速规则ID。

        :return: The dbcache_rule_id of this UpdateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._dbcache_rule_id

    @dbcache_rule_id.setter
    def dbcache_rule_id(self, dbcache_rule_id):
        r"""Sets the dbcache_rule_id of this UpdateDbCacheRuleRequestBody.

        内存加速规则ID。

        :param dbcache_rule_id: The dbcache_rule_id of this UpdateDbCacheRuleRequestBody.
        :type dbcache_rule_id: str
        """
        self._dbcache_rule_id = dbcache_rule_id

    @property
    def value_columns(self):
        r"""Gets the value_columns of this UpdateDbCacheRuleRequestBody.

        映射的value使用的column列表。

        :return: The value_columns of this UpdateDbCacheRuleRequestBody.
        :rtype: list[str]
        """
        return self._value_columns

    @value_columns.setter
    def value_columns(self, value_columns):
        r"""Sets the value_columns of this UpdateDbCacheRuleRequestBody.

        映射的value使用的column列表。

        :param value_columns: The value_columns of this UpdateDbCacheRuleRequestBody.
        :type value_columns: list[str]
        """
        self._value_columns = value_columns

    @property
    def ttl(self):
        r"""Gets the ttl of this UpdateDbCacheRuleRequestBody.

        key的生存时间。单位:ms。不传该值，默认取2592000000，表示30天。

        :return: The ttl of this UpdateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this UpdateDbCacheRuleRequestBody.

        key的生存时间。单位:ms。不传该值，默认取2592000000，表示30天。

        :param ttl: The ttl of this UpdateDbCacheRuleRequestBody.
        :type ttl: str
        """
        self._ttl = ttl

    @property
    def value_separator(self):
        r"""Gets the value_separator of this UpdateDbCacheRuleRequestBody.

        映射的value分隔符。只允许一个字符。

        :return: The value_separator of this UpdateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._value_separator

    @value_separator.setter
    def value_separator(self, value_separator):
        r"""Sets the value_separator of this UpdateDbCacheRuleRequestBody.

        映射的value分隔符。只允许一个字符。

        :param value_separator: The value_separator of this UpdateDbCacheRuleRequestBody.
        :type value_separator: str
        """
        self._value_separator = value_separator

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
        if not isinstance(other, UpdateDbCacheRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
