# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidatePolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'findings': 'list[ValidatePolicyFinding]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'findings': 'findings',
        'page_info': 'page_info'
    }

    def __init__(self, findings=None, page_info=None):
        r"""ValidatePolicyResponse

        The model defined in huaweicloud sdk

        :param findings: 可用于改进策略的可操作建议。
        :type findings: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.ValidatePolicyFinding`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        
        super(ValidatePolicyResponse, self).__init__()

        self._findings = None
        self._page_info = None
        self.discriminator = None

        if findings is not None:
            self.findings = findings
        if page_info is not None:
            self.page_info = page_info

    @property
    def findings(self):
        r"""Gets the findings of this ValidatePolicyResponse.

        可用于改进策略的可操作建议。

        :return: The findings of this ValidatePolicyResponse.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.ValidatePolicyFinding`]
        """
        return self._findings

    @findings.setter
    def findings(self, findings):
        r"""Sets the findings of this ValidatePolicyResponse.

        可用于改进策略的可操作建议。

        :param findings: The findings of this ValidatePolicyResponse.
        :type findings: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.ValidatePolicyFinding`]
        """
        self._findings = findings

    @property
    def page_info(self):
        r"""Gets the page_info of this ValidatePolicyResponse.

        :return: The page_info of this ValidatePolicyResponse.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ValidatePolicyResponse.

        :param page_info: The page_info of this ValidatePolicyResponse.
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ValidatePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
