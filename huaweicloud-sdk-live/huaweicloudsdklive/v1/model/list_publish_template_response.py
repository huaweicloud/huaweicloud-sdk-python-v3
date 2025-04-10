# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublishTemplateResponse(SdkResponse):

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
        'auth_sign_key': 'str',
        'call_back_area': 'str'
    }

    attribute_map = {
        'url': 'url',
        'auth_sign_key': 'auth_sign_key',
        'call_back_area': 'call_back_area'
    }

    def __init__(self, url=None, auth_sign_key=None, call_back_area=None):
        r"""ListPublishTemplateResponse

        The model defined in huaweicloud sdk

        :param url: 回调地址
        :type url: str
        :param auth_sign_key: 鉴权密钥
        :type auth_sign_key: str
        :param call_back_area: 接收回调通知服务器所在区域。 包含如下取值： - mainland_china：中国大陆区域。 - outside_mainland_china：中国大陆以外区域。
        :type call_back_area: str
        """
        
        super(ListPublishTemplateResponse, self).__init__()

        self._url = None
        self._auth_sign_key = None
        self._call_back_area = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if auth_sign_key is not None:
            self.auth_sign_key = auth_sign_key
        if call_back_area is not None:
            self.call_back_area = call_back_area

    @property
    def url(self):
        r"""Gets the url of this ListPublishTemplateResponse.

        回调地址

        :return: The url of this ListPublishTemplateResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ListPublishTemplateResponse.

        回调地址

        :param url: The url of this ListPublishTemplateResponse.
        :type url: str
        """
        self._url = url

    @property
    def auth_sign_key(self):
        r"""Gets the auth_sign_key of this ListPublishTemplateResponse.

        鉴权密钥

        :return: The auth_sign_key of this ListPublishTemplateResponse.
        :rtype: str
        """
        return self._auth_sign_key

    @auth_sign_key.setter
    def auth_sign_key(self, auth_sign_key):
        r"""Sets the auth_sign_key of this ListPublishTemplateResponse.

        鉴权密钥

        :param auth_sign_key: The auth_sign_key of this ListPublishTemplateResponse.
        :type auth_sign_key: str
        """
        self._auth_sign_key = auth_sign_key

    @property
    def call_back_area(self):
        r"""Gets the call_back_area of this ListPublishTemplateResponse.

        接收回调通知服务器所在区域。 包含如下取值： - mainland_china：中国大陆区域。 - outside_mainland_china：中国大陆以外区域。

        :return: The call_back_area of this ListPublishTemplateResponse.
        :rtype: str
        """
        return self._call_back_area

    @call_back_area.setter
    def call_back_area(self, call_back_area):
        r"""Sets the call_back_area of this ListPublishTemplateResponse.

        接收回调通知服务器所在区域。 包含如下取值： - mainland_china：中国大陆区域。 - outside_mainland_china：中国大陆以外区域。

        :param call_back_area: The call_back_area of this ListPublishTemplateResponse.
        :type call_back_area: str
        """
        self._call_back_area = call_back_area

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
        if not isinstance(other, ListPublishTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
