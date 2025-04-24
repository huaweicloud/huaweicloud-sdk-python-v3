# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequestLimitRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'priority': 'int',
        'match_type': 'str',
        'match_value': 'str',
        'type': 'str',
        'limit_rate_after': 'int',
        'limit_rate_value': 'int',
        'limit_time': 'str'
    }

    attribute_map = {
        'status': 'status',
        'priority': 'priority',
        'match_type': 'match_type',
        'match_value': 'match_value',
        'type': 'type',
        'limit_rate_after': 'limit_rate_after',
        'limit_rate_value': 'limit_rate_value',
        'limit_time': 'limit_time'
    }

    def __init__(self, status=None, priority=None, match_type=None, match_value=None, type=None, limit_rate_after=None, limit_rate_value=None, limit_time=None):
        r"""RequestLimitRules

        The model defined in huaweicloud sdk

        :param status: status只支持on，off无效。  &gt; request_limit_rules字段置空时代表关闭请求限速功能。  &gt; 旧接口中的参数，后续将下线。
        :type status: str
        :param priority: 优先级，值越大，优先级越高,取值范围：1-100。
        :type priority: int
        :param match_type: 匹配类型，all：所有文件，catalog：目录。
        :type match_type: str
        :param match_value: 匹配类型值。 当match_type为all时传空值，例如：\&quot;\&quot;； 当match_type为catalog时传目录地址，以“/”作为首字符,例如：\&quot;/test\&quot;。  &gt; 值为catalog的时候必填
        :type match_value: str
        :param type: 限速方式，当前仅支持按流量大小限速，取值为size。
        :type type: str
        :param limit_rate_after: 限速条件,type&#x3D;size,limit_rate_after&#x3D;50表示从传输表示传输50个字节后开始限速且限速值为limit_rate_value， 单位byte，取值范围：0-1073741824。
        :type limit_rate_after: int
        :param limit_rate_value: 限速值,单位Bps，取值范围 0-104857600。
        :type limit_rate_value: int
        :param limit_time: 指明限速的时段，按照每天24小时设置限速时段，格式为：HHMM-HHMM（HH为时，MM为分，时区为UTC+8），多个时段限速时用“,”分隔，最多可配置10个时段，例如：0100-0200,2200-2300。不传或传空时默认值为0000-2400，代表限速对所有时段生效。
        :type limit_time: str
        """
        
        

        self._status = None
        self._priority = None
        self._match_type = None
        self._match_value = None
        self._type = None
        self._limit_rate_after = None
        self._limit_rate_value = None
        self._limit_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        self.priority = priority
        self.match_type = match_type
        if match_value is not None:
            self.match_value = match_value
        self.type = type
        self.limit_rate_after = limit_rate_after
        self.limit_rate_value = limit_rate_value
        if limit_time is not None:
            self.limit_time = limit_time

    @property
    def status(self):
        r"""Gets the status of this RequestLimitRules.

        status只支持on，off无效。  > request_limit_rules字段置空时代表关闭请求限速功能。  > 旧接口中的参数，后续将下线。

        :return: The status of this RequestLimitRules.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RequestLimitRules.

        status只支持on，off无效。  > request_limit_rules字段置空时代表关闭请求限速功能。  > 旧接口中的参数，后续将下线。

        :param status: The status of this RequestLimitRules.
        :type status: str
        """
        self._status = status

    @property
    def priority(self):
        r"""Gets the priority of this RequestLimitRules.

        优先级，值越大，优先级越高,取值范围：1-100。

        :return: The priority of this RequestLimitRules.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this RequestLimitRules.

        优先级，值越大，优先级越高,取值范围：1-100。

        :param priority: The priority of this RequestLimitRules.
        :type priority: int
        """
        self._priority = priority

    @property
    def match_type(self):
        r"""Gets the match_type of this RequestLimitRules.

        匹配类型，all：所有文件，catalog：目录。

        :return: The match_type of this RequestLimitRules.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this RequestLimitRules.

        匹配类型，all：所有文件，catalog：目录。

        :param match_type: The match_type of this RequestLimitRules.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def match_value(self):
        r"""Gets the match_value of this RequestLimitRules.

        匹配类型值。 当match_type为all时传空值，例如：\"\"； 当match_type为catalog时传目录地址，以“/”作为首字符,例如：\"/test\"。  > 值为catalog的时候必填

        :return: The match_value of this RequestLimitRules.
        :rtype: str
        """
        return self._match_value

    @match_value.setter
    def match_value(self, match_value):
        r"""Sets the match_value of this RequestLimitRules.

        匹配类型值。 当match_type为all时传空值，例如：\"\"； 当match_type为catalog时传目录地址，以“/”作为首字符,例如：\"/test\"。  > 值为catalog的时候必填

        :param match_value: The match_value of this RequestLimitRules.
        :type match_value: str
        """
        self._match_value = match_value

    @property
    def type(self):
        r"""Gets the type of this RequestLimitRules.

        限速方式，当前仅支持按流量大小限速，取值为size。

        :return: The type of this RequestLimitRules.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RequestLimitRules.

        限速方式，当前仅支持按流量大小限速，取值为size。

        :param type: The type of this RequestLimitRules.
        :type type: str
        """
        self._type = type

    @property
    def limit_rate_after(self):
        r"""Gets the limit_rate_after of this RequestLimitRules.

        限速条件,type=size,limit_rate_after=50表示从传输表示传输50个字节后开始限速且限速值为limit_rate_value， 单位byte，取值范围：0-1073741824。

        :return: The limit_rate_after of this RequestLimitRules.
        :rtype: int
        """
        return self._limit_rate_after

    @limit_rate_after.setter
    def limit_rate_after(self, limit_rate_after):
        r"""Sets the limit_rate_after of this RequestLimitRules.

        限速条件,type=size,limit_rate_after=50表示从传输表示传输50个字节后开始限速且限速值为limit_rate_value， 单位byte，取值范围：0-1073741824。

        :param limit_rate_after: The limit_rate_after of this RequestLimitRules.
        :type limit_rate_after: int
        """
        self._limit_rate_after = limit_rate_after

    @property
    def limit_rate_value(self):
        r"""Gets the limit_rate_value of this RequestLimitRules.

        限速值,单位Bps，取值范围 0-104857600。

        :return: The limit_rate_value of this RequestLimitRules.
        :rtype: int
        """
        return self._limit_rate_value

    @limit_rate_value.setter
    def limit_rate_value(self, limit_rate_value):
        r"""Sets the limit_rate_value of this RequestLimitRules.

        限速值,单位Bps，取值范围 0-104857600。

        :param limit_rate_value: The limit_rate_value of this RequestLimitRules.
        :type limit_rate_value: int
        """
        self._limit_rate_value = limit_rate_value

    @property
    def limit_time(self):
        r"""Gets the limit_time of this RequestLimitRules.

        指明限速的时段，按照每天24小时设置限速时段，格式为：HHMM-HHMM（HH为时，MM为分，时区为UTC+8），多个时段限速时用“,”分隔，最多可配置10个时段，例如：0100-0200,2200-2300。不传或传空时默认值为0000-2400，代表限速对所有时段生效。

        :return: The limit_time of this RequestLimitRules.
        :rtype: str
        """
        return self._limit_time

    @limit_time.setter
    def limit_time(self, limit_time):
        r"""Sets the limit_time of this RequestLimitRules.

        指明限速的时段，按照每天24小时设置限速时段，格式为：HHMM-HHMM（HH为时，MM为分，时区为UTC+8），多个时段限速时用“,”分隔，最多可配置10个时段，例如：0100-0200,2200-2300。不传或传空时默认值为0000-2400，代表限速对所有时段生效。

        :param limit_time: The limit_time of this RequestLimitRules.
        :type limit_time: str
        """
        self._limit_time = limit_time

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
        if not isinstance(other, RequestLimitRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
