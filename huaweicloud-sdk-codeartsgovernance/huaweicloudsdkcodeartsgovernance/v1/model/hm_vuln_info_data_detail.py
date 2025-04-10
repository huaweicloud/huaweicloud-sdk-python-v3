# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HmVulnInfoDataDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vuln_info': 'list[HmVulnInfoDataDetailVulnInfo]'
    }

    attribute_map = {
        'vuln_info': 'vuln_info'
    }

    def __init__(self, vuln_info=None):
        r"""HmVulnInfoDataDetail

        The model defined in huaweicloud sdk

        :param vuln_info: 问题
        :type vuln_info: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HmVulnInfoDataDetailVulnInfo`]
        """
        
        

        self._vuln_info = None
        self.discriminator = None

        if vuln_info is not None:
            self.vuln_info = vuln_info

    @property
    def vuln_info(self):
        r"""Gets the vuln_info of this HmVulnInfoDataDetail.

        问题

        :return: The vuln_info of this HmVulnInfoDataDetail.
        :rtype: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HmVulnInfoDataDetailVulnInfo`]
        """
        return self._vuln_info

    @vuln_info.setter
    def vuln_info(self, vuln_info):
        r"""Sets the vuln_info of this HmVulnInfoDataDetail.

        问题

        :param vuln_info: The vuln_info of this HmVulnInfoDataDetail.
        :type vuln_info: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HmVulnInfoDataDetailVulnInfo`]
        """
        self._vuln_info = vuln_info

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
        if not isinstance(other, HmVulnInfoDataDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
