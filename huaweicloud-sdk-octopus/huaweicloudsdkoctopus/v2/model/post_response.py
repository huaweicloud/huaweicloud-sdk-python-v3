# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostResponse:

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
        'fields': 'PostResponseField'
    }

    attribute_map = {
        'url': 'url',
        'fields': 'fields'
    }

    def __init__(self, url=None, fields=None):
        """PostResponse

        The model defined in huaweicloud sdk

        :param url: POST地址
        :type url: str
        :param fields: 
        :type fields: :class:`huaweicloudsdkoctopus.v2.PostResponseField`
        """
        
        

        self._url = None
        self._fields = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if fields is not None:
            self.fields = fields

    @property
    def url(self):
        """Gets the url of this PostResponse.

        POST地址

        :return: The url of this PostResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PostResponse.

        POST地址

        :param url: The url of this PostResponse.
        :type url: str
        """
        self._url = url

    @property
    def fields(self):
        """Gets the fields of this PostResponse.

        :return: The fields of this PostResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.PostResponseField`
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this PostResponse.

        :param fields: The fields of this PostResponse.
        :type fields: :class:`huaweicloudsdkoctopus.v2.PostResponseField`
        """
        self._fields = fields

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
        if not isinstance(other, PostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
