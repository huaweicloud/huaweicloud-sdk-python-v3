# coding: utf-8

import re
import six





class CcrulesListInfoActionDetail:


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
        'response': 'CcrulesListInfoActionDetailResponse'
    }

    attribute_map = {
        'redirect_url': 'redirect_url',
        'response': 'response'
    }

    def __init__(self, redirect_url=None, response=None):
        """CcrulesListInfoActionDetail - a model defined in huaweicloud sdk"""
        
        

        self._redirect_url = None
        self._response = None
        self.discriminator = None

        if redirect_url is not None:
            self.redirect_url = redirect_url
        if response is not None:
            self.response = response

    @property
    def redirect_url(self):
        """Gets the redirect_url of this CcrulesListInfoActionDetail.

        返回页面重定向的url

        :return: The redirect_url of this CcrulesListInfoActionDetail.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this CcrulesListInfoActionDetail.

        返回页面重定向的url

        :param redirect_url: The redirect_url of this CcrulesListInfoActionDetail.
        :type: str
        """
        self._redirect_url = redirect_url

    @property
    def response(self):
        """Gets the response of this CcrulesListInfoActionDetail.


        :return: The response of this CcrulesListInfoActionDetail.
        :rtype: CcrulesListInfoActionDetailResponse
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this CcrulesListInfoActionDetail.


        :param response: The response of this CcrulesListInfoActionDetail.
        :type: CcrulesListInfoActionDetailResponse
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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CcrulesListInfoActionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
