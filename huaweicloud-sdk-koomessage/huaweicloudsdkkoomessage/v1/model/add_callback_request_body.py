# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddCallbackRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'callback_url': 'str',
        'url_type': 'int'
    }

    attribute_map = {
        'callback_url': 'callback_url',
        'url_type': 'url_type'
    }

    def __init__(self, callback_url=None, url_type=None):
        """AddCallbackRequestBody

        The model defined in huaweicloud sdk

        :param callback_url: 回调地址。  &gt; - 必须http或https开头，建议使用https &gt; - 支持域名或公网IP回调地址，不支持私网IP回调地址 
        :type callback_url: str
        :param url_type: 回调类型。  - 0：智能信息单条发送回调 - 1：模板状态回调 - 2：智能信息批量发送回调 
        :type url_type: int
        """
        
        

        self._callback_url = None
        self._url_type = None
        self.discriminator = None

        self.callback_url = callback_url
        if url_type is not None:
            self.url_type = url_type

    @property
    def callback_url(self):
        """Gets the callback_url of this AddCallbackRequestBody.

        回调地址。  > - 必须http或https开头，建议使用https > - 支持域名或公网IP回调地址，不支持私网IP回调地址 

        :return: The callback_url of this AddCallbackRequestBody.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this AddCallbackRequestBody.

        回调地址。  > - 必须http或https开头，建议使用https > - 支持域名或公网IP回调地址，不支持私网IP回调地址 

        :param callback_url: The callback_url of this AddCallbackRequestBody.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def url_type(self):
        """Gets the url_type of this AddCallbackRequestBody.

        回调类型。  - 0：智能信息单条发送回调 - 1：模板状态回调 - 2：智能信息批量发送回调 

        :return: The url_type of this AddCallbackRequestBody.
        :rtype: int
        """
        return self._url_type

    @url_type.setter
    def url_type(self, url_type):
        """Sets the url_type of this AddCallbackRequestBody.

        回调类型。  - 0：智能信息单条发送回调 - 1：模板状态回调 - 2：智能信息批量发送回调 

        :param url_type: The url_type of this AddCallbackRequestBody.
        :type url_type: int
        """
        self._url_type = url_type

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
        if not isinstance(other, AddCallbackRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
