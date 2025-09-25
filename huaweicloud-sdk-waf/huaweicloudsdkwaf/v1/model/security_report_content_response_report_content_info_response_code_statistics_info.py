# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'response_source_waf_info_list': 'list[SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoResponseSourceWafInfoList]',
        'response_source_upstream_info_list': 'list[SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoResponseSourceUpstreamInfoList]'
    }

    attribute_map = {
        'response_source_waf_info_list': 'response_source_waf_info_list',
        'response_source_upstream_info_list': 'response_source_upstream_info_list'
    }

    def __init__(self, response_source_waf_info_list=None, response_source_upstream_info_list=None):
        r"""SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo

        The model defined in huaweicloud sdk

        :param response_source_waf_info_list: **参数解释：** WAF响应码统计列表，包含各响应码按时间线的WAF返回数量。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type response_source_waf_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoResponseSourceWafInfoList`]
        :param response_source_upstream_info_list: **参数解释：** 上游响应码统计列表，包含各响应码按时间线的上游返回数量。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type response_source_upstream_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoResponseSourceUpstreamInfoList`]
        """
        
        

        self._response_source_waf_info_list = None
        self._response_source_upstream_info_list = None
        self.discriminator = None

        if response_source_waf_info_list is not None:
            self.response_source_waf_info_list = response_source_waf_info_list
        if response_source_upstream_info_list is not None:
            self.response_source_upstream_info_list = response_source_upstream_info_list

    @property
    def response_source_waf_info_list(self):
        r"""Gets the response_source_waf_info_list of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo.

        **参数解释：** WAF响应码统计列表，包含各响应码按时间线的WAF返回数量。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The response_source_waf_info_list of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoResponseSourceWafInfoList`]
        """
        return self._response_source_waf_info_list

    @response_source_waf_info_list.setter
    def response_source_waf_info_list(self, response_source_waf_info_list):
        r"""Sets the response_source_waf_info_list of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo.

        **参数解释：** WAF响应码统计列表，包含各响应码按时间线的WAF返回数量。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param response_source_waf_info_list: The response_source_waf_info_list of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo.
        :type response_source_waf_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoResponseSourceWafInfoList`]
        """
        self._response_source_waf_info_list = response_source_waf_info_list

    @property
    def response_source_upstream_info_list(self):
        r"""Gets the response_source_upstream_info_list of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo.

        **参数解释：** 上游响应码统计列表，包含各响应码按时间线的上游返回数量。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The response_source_upstream_info_list of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoResponseSourceUpstreamInfoList`]
        """
        return self._response_source_upstream_info_list

    @response_source_upstream_info_list.setter
    def response_source_upstream_info_list(self, response_source_upstream_info_list):
        r"""Sets the response_source_upstream_info_list of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo.

        **参数解释：** 上游响应码统计列表，包含各响应码按时间线的上游返回数量。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param response_source_upstream_info_list: The response_source_upstream_info_list of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo.
        :type response_source_upstream_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoResponseSourceUpstreamInfoList`]
        """
        self._response_source_upstream_info_list = response_source_upstream_info_list

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
        if not isinstance(other, SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
