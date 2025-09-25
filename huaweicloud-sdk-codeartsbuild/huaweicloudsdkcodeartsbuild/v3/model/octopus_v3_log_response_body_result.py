# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OctopusV3LogResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'has_more': 'bool',
        'start_offset': 'str',
        'end_offset': 'str',
        'log': 'str',
        'location': 'str'
    }

    attribute_map = {
        'has_more': 'has_more',
        'start_offset': 'start_offset',
        'end_offset': 'end_offset',
        'log': 'log',
        'location': 'location'
    }

    def __init__(self, has_more=None, start_offset=None, end_offset=None, log=None, location=None):
        r"""OctopusV3LogResponseBodyResult

        The model defined in huaweicloud sdk

        :param has_more: **参数解释**： 是否还有剩余日志标识。 **约束限制**： 不涉及。 **取值范围**： true或false。 **默认取值**： 不涉及。
        :type has_more: bool
        :param start_offset: **参数解释**： 日志查询起始偏移量。 **约束限制**： 不涉及。 **取值范围**： 数字组成。 **默认取值**： 不涉及。
        :type start_offset: str
        :param end_offset: **参数解释**： 日志查询结束偏移量。 **约束限制**： 不涉及。 **取值范围**： 数字组成。 **默认取值**： 不涉及。
        :type end_offset: str
        :param log: **参数解释**： 返回日志内容，可能会空，请再次请求。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type log: str
        :param location: **参数解释**： 日志来源。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type location: str
        """
        
        

        self._has_more = None
        self._start_offset = None
        self._end_offset = None
        self._log = None
        self._location = None
        self.discriminator = None

        if has_more is not None:
            self.has_more = has_more
        if start_offset is not None:
            self.start_offset = start_offset
        if end_offset is not None:
            self.end_offset = end_offset
        if log is not None:
            self.log = log
        if location is not None:
            self.location = location

    @property
    def has_more(self):
        r"""Gets the has_more of this OctopusV3LogResponseBodyResult.

        **参数解释**： 是否还有剩余日志标识。 **约束限制**： 不涉及。 **取值范围**： true或false。 **默认取值**： 不涉及。

        :return: The has_more of this OctopusV3LogResponseBodyResult.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        r"""Sets the has_more of this OctopusV3LogResponseBodyResult.

        **参数解释**： 是否还有剩余日志标识。 **约束限制**： 不涉及。 **取值范围**： true或false。 **默认取值**： 不涉及。

        :param has_more: The has_more of this OctopusV3LogResponseBodyResult.
        :type has_more: bool
        """
        self._has_more = has_more

    @property
    def start_offset(self):
        r"""Gets the start_offset of this OctopusV3LogResponseBodyResult.

        **参数解释**： 日志查询起始偏移量。 **约束限制**： 不涉及。 **取值范围**： 数字组成。 **默认取值**： 不涉及。

        :return: The start_offset of this OctopusV3LogResponseBodyResult.
        :rtype: str
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        r"""Sets the start_offset of this OctopusV3LogResponseBodyResult.

        **参数解释**： 日志查询起始偏移量。 **约束限制**： 不涉及。 **取值范围**： 数字组成。 **默认取值**： 不涉及。

        :param start_offset: The start_offset of this OctopusV3LogResponseBodyResult.
        :type start_offset: str
        """
        self._start_offset = start_offset

    @property
    def end_offset(self):
        r"""Gets the end_offset of this OctopusV3LogResponseBodyResult.

        **参数解释**： 日志查询结束偏移量。 **约束限制**： 不涉及。 **取值范围**： 数字组成。 **默认取值**： 不涉及。

        :return: The end_offset of this OctopusV3LogResponseBodyResult.
        :rtype: str
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        r"""Sets the end_offset of this OctopusV3LogResponseBodyResult.

        **参数解释**： 日志查询结束偏移量。 **约束限制**： 不涉及。 **取值范围**： 数字组成。 **默认取值**： 不涉及。

        :param end_offset: The end_offset of this OctopusV3LogResponseBodyResult.
        :type end_offset: str
        """
        self._end_offset = end_offset

    @property
    def log(self):
        r"""Gets the log of this OctopusV3LogResponseBodyResult.

        **参数解释**： 返回日志内容，可能会空，请再次请求。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The log of this OctopusV3LogResponseBodyResult.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        r"""Sets the log of this OctopusV3LogResponseBodyResult.

        **参数解释**： 返回日志内容，可能会空，请再次请求。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param log: The log of this OctopusV3LogResponseBodyResult.
        :type log: str
        """
        self._log = log

    @property
    def location(self):
        r"""Gets the location of this OctopusV3LogResponseBodyResult.

        **参数解释**： 日志来源。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The location of this OctopusV3LogResponseBodyResult.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this OctopusV3LogResponseBodyResult.

        **参数解释**： 日志来源。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param location: The location of this OctopusV3LogResponseBodyResult.
        :type location: str
        """
        self._location = location

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
        if not isinstance(other, OctopusV3LogResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
