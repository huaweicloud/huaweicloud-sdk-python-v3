# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRemediationExceptionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'list[RemediationException]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'value': 'value',
        'page_info': 'page_info'
    }

    def __init__(self, value=None, page_info=None):
        r"""ListRemediationExceptionsResponse

        The model defined in huaweicloud sdk

        :param value: 合规规则修正例外的详情。
        :type value: list[:class:`huaweicloudsdkconfig.v1.RemediationException`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        
        super(ListRemediationExceptionsResponse, self).__init__()

        self._value = None
        self._page_info = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if page_info is not None:
            self.page_info = page_info

    @property
    def value(self):
        r"""Gets the value of this ListRemediationExceptionsResponse.

        合规规则修正例外的详情。

        :return: The value of this ListRemediationExceptionsResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.RemediationException`]
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ListRemediationExceptionsResponse.

        合规规则修正例外的详情。

        :param value: The value of this ListRemediationExceptionsResponse.
        :type value: list[:class:`huaweicloudsdkconfig.v1.RemediationException`]
        """
        self._value = value

    @property
    def page_info(self):
        r"""Gets the page_info of this ListRemediationExceptionsResponse.

        :return: The page_info of this ListRemediationExceptionsResponse.
        :rtype: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListRemediationExceptionsResponse.

        :param page_info: The page_info of this ListRemediationExceptionsResponse.
        :type page_info: :class:`huaweicloudsdkconfig.v1.PageInfo`
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
        if not isinstance(other, ListRemediationExceptionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
