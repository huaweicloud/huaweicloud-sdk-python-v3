# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'num': 'int',
        'web_tag': 'str'
    }

    attribute_map = {
        'key': 'key',
        'num': 'num',
        'web_tag': 'web_tag'
    }

    def __init__(self, key=None, num=None, web_tag=None):
        r"""SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 域名标识，包含域名及端口（如*:80表示所有域名的80端口）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type key: str
        :param num: **参数解释：** 该域名被攻击的总次数。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0
        :type num: int
        :param web_tag: **参数解释：** 域名的Web标签，用于标识域名所属业务类型。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type web_tag: str
        """
        
        

        self._key = None
        self._num = None
        self._web_tag = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if num is not None:
            self.num = num
        if web_tag is not None:
            self.web_tag = web_tag

    @property
    def key(self):
        r"""Gets the key of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.

        **参数解释：** 域名标识，包含域名及端口（如*:80表示所有域名的80端口）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The key of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.

        **参数解释：** 域名标识，包含域名及端口（如*:80表示所有域名的80端口）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param key: The key of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.
        :type key: str
        """
        self._key = key

    @property
    def num(self):
        r"""Gets the num of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.

        **参数解释：** 该域名被攻击的总次数。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :return: The num of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.

        **参数解释：** 该域名被攻击的总次数。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :param num: The num of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.
        :type num: int
        """
        self._num = num

    @property
    def web_tag(self):
        r"""Gets the web_tag of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.

        **参数解释：** 域名的Web标签，用于标识域名所属业务类型。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The web_tag of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        r"""Sets the web_tag of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.

        **参数解释：** 域名的Web标签，用于标识域名所属业务类型。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param web_tag: The web_tag of this SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList.
        :type web_tag: str
        """
        self._web_tag = web_tag

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
        if not isinstance(other, SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
