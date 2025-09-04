# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCdnDomainTopIpsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_ip_summary': 'list[TopIpSummary]'
    }

    attribute_map = {
        'top_ip_summary': 'top_ip_summary'
    }

    def __init__(self, top_ip_summary=None):
        r"""ListCdnDomainTopIpsResponse

        The model defined in huaweicloud sdk

        :param top_ip_summary: 详情数据对象。
        :type top_ip_summary: list[:class:`huaweicloudsdkcdn.v2.TopIpSummary`]
        """
        
        super(ListCdnDomainTopIpsResponse, self).__init__()

        self._top_ip_summary = None
        self.discriminator = None

        if top_ip_summary is not None:
            self.top_ip_summary = top_ip_summary

    @property
    def top_ip_summary(self):
        r"""Gets the top_ip_summary of this ListCdnDomainTopIpsResponse.

        详情数据对象。

        :return: The top_ip_summary of this ListCdnDomainTopIpsResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.TopIpSummary`]
        """
        return self._top_ip_summary

    @top_ip_summary.setter
    def top_ip_summary(self, top_ip_summary):
        r"""Sets the top_ip_summary of this ListCdnDomainTopIpsResponse.

        详情数据对象。

        :param top_ip_summary: The top_ip_summary of this ListCdnDomainTopIpsResponse.
        :type top_ip_summary: list[:class:`huaweicloudsdkcdn.v2.TopIpSummary`]
        """
        self._top_ip_summary = top_ip_summary

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
        if not isinstance(other, ListCdnDomainTopIpsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
