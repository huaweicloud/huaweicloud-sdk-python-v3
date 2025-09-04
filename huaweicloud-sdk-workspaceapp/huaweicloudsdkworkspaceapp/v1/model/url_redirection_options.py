# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlRedirectionOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url_include_list': 'str',
        'url_exclude_list': 'str'
    }

    attribute_map = {
        'url_include_list': 'url_include_list',
        'url_exclude_list': 'url_exclude_list'
    }

    def __init__(self, url_include_list=None, url_exclude_list=None):
        r"""UrlRedirectionOptions

        The model defined in huaweicloud sdk

        :param url_include_list: 允许重定向url。
        :type url_include_list: str
        :param url_exclude_list: 拒绝重定向url。
        :type url_exclude_list: str
        """
        
        

        self._url_include_list = None
        self._url_exclude_list = None
        self.discriminator = None

        if url_include_list is not None:
            self.url_include_list = url_include_list
        if url_exclude_list is not None:
            self.url_exclude_list = url_exclude_list

    @property
    def url_include_list(self):
        r"""Gets the url_include_list of this UrlRedirectionOptions.

        允许重定向url。

        :return: The url_include_list of this UrlRedirectionOptions.
        :rtype: str
        """
        return self._url_include_list

    @url_include_list.setter
    def url_include_list(self, url_include_list):
        r"""Sets the url_include_list of this UrlRedirectionOptions.

        允许重定向url。

        :param url_include_list: The url_include_list of this UrlRedirectionOptions.
        :type url_include_list: str
        """
        self._url_include_list = url_include_list

    @property
    def url_exclude_list(self):
        r"""Gets the url_exclude_list of this UrlRedirectionOptions.

        拒绝重定向url。

        :return: The url_exclude_list of this UrlRedirectionOptions.
        :rtype: str
        """
        return self._url_exclude_list

    @url_exclude_list.setter
    def url_exclude_list(self, url_exclude_list):
        r"""Sets the url_exclude_list of this UrlRedirectionOptions.

        拒绝重定向url。

        :param url_exclude_list: The url_exclude_list of this UrlRedirectionOptions.
        :type url_exclude_list: str
        """
        self._url_exclude_list = url_exclude_list

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
        if not isinstance(other, UrlRedirectionOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
