# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductDelFailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'url': 'url',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, url=None, fail_reason=None):
        """ProductDelFailInfo

        The model defined in huaweicloud sdk

        :param url: 删除产物的URL
        :type url: str
        :param fail_reason: 删除产物失败的原因
        :type fail_reason: str
        """
        
        

        self._url = None
        self._fail_reason = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def url(self):
        """Gets the url of this ProductDelFailInfo.

        删除产物的URL

        :return: The url of this ProductDelFailInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProductDelFailInfo.

        删除产物的URL

        :param url: The url of this ProductDelFailInfo.
        :type url: str
        """
        self._url = url

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ProductDelFailInfo.

        删除产物失败的原因

        :return: The fail_reason of this ProductDelFailInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ProductDelFailInfo.

        删除产物失败的原因

        :param fail_reason: The fail_reason of this ProductDelFailInfo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, ProductDelFailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
