# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesUrlRedirection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url_redirection_enable': 'bool',
        'options': 'UrlRedirectionOptions'
    }

    attribute_map = {
        'url_redirection_enable': 'url_redirection_enable',
        'options': 'options'
    }

    def __init__(self, url_redirection_enable=None, options=None):
        r"""PoliciesUrlRedirection

        The model defined in huaweicloud sdk

        :param url_redirection_enable: 配置url重定向开关： false: 表示关闭 true: 表示开启
        :type url_redirection_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.UrlRedirectionOptions`
        """
        
        

        self._url_redirection_enable = None
        self._options = None
        self.discriminator = None

        if url_redirection_enable is not None:
            self.url_redirection_enable = url_redirection_enable
        if options is not None:
            self.options = options

    @property
    def url_redirection_enable(self):
        r"""Gets the url_redirection_enable of this PoliciesUrlRedirection.

        配置url重定向开关： false: 表示关闭 true: 表示开启

        :return: The url_redirection_enable of this PoliciesUrlRedirection.
        :rtype: bool
        """
        return self._url_redirection_enable

    @url_redirection_enable.setter
    def url_redirection_enable(self, url_redirection_enable):
        r"""Sets the url_redirection_enable of this PoliciesUrlRedirection.

        配置url重定向开关： false: 表示关闭 true: 表示开启

        :param url_redirection_enable: The url_redirection_enable of this PoliciesUrlRedirection.
        :type url_redirection_enable: bool
        """
        self._url_redirection_enable = url_redirection_enable

    @property
    def options(self):
        r"""Gets the options of this PoliciesUrlRedirection.

        :return: The options of this PoliciesUrlRedirection.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UrlRedirectionOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this PoliciesUrlRedirection.

        :param options: The options of this PoliciesUrlRedirection.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.UrlRedirectionOptions`
        """
        self._options = options

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
        if not isinstance(other, PoliciesUrlRedirection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
