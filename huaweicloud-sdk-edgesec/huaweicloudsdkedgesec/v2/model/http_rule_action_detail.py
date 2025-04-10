# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpRuleActionDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'redirect_url': 'str',
        'response': 'HttpRuleActionResponse'
    }

    attribute_map = {
        'redirect_url': 'redirect_url',
        'response': 'response'
    }

    def __init__(self, redirect_url=None, response=None):
        r"""HttpRuleActionDetail

        The model defined in huaweicloud sdk

        :param redirect_url: 返回页面重定向的url
        :type redirect_url: str
        :param response: 
        :type response: :class:`huaweicloudsdkedgesec.v2.HttpRuleActionResponse`
        """
        
        

        self._redirect_url = None
        self._response = None
        self.discriminator = None

        if redirect_url is not None:
            self.redirect_url = redirect_url
        if response is not None:
            self.response = response

    @property
    def redirect_url(self):
        r"""Gets the redirect_url of this HttpRuleActionDetail.

        返回页面重定向的url

        :return: The redirect_url of this HttpRuleActionDetail.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        r"""Sets the redirect_url of this HttpRuleActionDetail.

        返回页面重定向的url

        :param redirect_url: The redirect_url of this HttpRuleActionDetail.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

    @property
    def response(self):
        r"""Gets the response of this HttpRuleActionDetail.

        :return: The response of this HttpRuleActionDetail.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpRuleActionResponse`
        """
        return self._response

    @response.setter
    def response(self, response):
        r"""Sets the response of this HttpRuleActionDetail.

        :param response: The response of this HttpRuleActionDetail.
        :type response: :class:`huaweicloudsdkedgesec.v2.HttpRuleActionResponse`
        """
        self._response = response

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
        if not isinstance(other, HttpRuleActionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
