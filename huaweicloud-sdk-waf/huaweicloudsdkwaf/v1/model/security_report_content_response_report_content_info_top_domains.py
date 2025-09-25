# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportContentResponseReportContentInfoTopDomains:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'num': 'int',
        'host': 'str'
    }

    attribute_map = {
        'num': 'num',
        'host': 'host'
    }

    def __init__(self, num=None, host=None):
        r"""SecurityReportContentResponseReportContentInfoTopDomains

        The model defined in huaweicloud sdk

        :param num: **参数解释：** 该域名在对应统计维度下的数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0
        :type num: int
        :param host: **参数解释：** 域名标识，包含域名及关联标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type host: str
        """
        
        

        self._num = None
        self._host = None
        self.discriminator = None

        if num is not None:
            self.num = num
        if host is not None:
            self.host = host

    @property
    def num(self):
        r"""Gets the num of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 该域名在对应统计维度下的数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :return: The num of this SecurityReportContentResponseReportContentInfoTopDomains.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 该域名在对应统计维度下的数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :param num: The num of this SecurityReportContentResponseReportContentInfoTopDomains.
        :type num: int
        """
        self._num = num

    @property
    def host(self):
        r"""Gets the host of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 域名标识，包含域名及关联标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The host of this SecurityReportContentResponseReportContentInfoTopDomains.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 域名标识，包含域名及关联标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param host: The host of this SecurityReportContentResponseReportContentInfoTopDomains.
        :type host: str
        """
        self._host = host

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
        if not isinstance(other, SecurityReportContentResponseReportContentInfoTopDomains):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
