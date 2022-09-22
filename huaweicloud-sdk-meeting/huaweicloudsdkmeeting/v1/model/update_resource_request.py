# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResourceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'corp_id': 'str',
        'body': 'list[ModResourceDTO]'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'corp_id': 'corp_id',
        'body': 'body'
    }

    def __init__(self, x_request_id=None, accept_language=None, corp_id=None, body=None):
        """UpdateResourceRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。
        :type x_request_id: str
        :param accept_language: 语言参数，默认为中文zh-CN，英文为en-US。
        :type accept_language: str
        :param corp_id: 企业id。
        :type corp_id: str
        :param body: Body of the UpdateResourceRequest
        :type body: list[:class:`huaweicloudsdkmeeting.v1.ModResourceDTO`]
        """
        
        

        self._x_request_id = None
        self._accept_language = None
        self._corp_id = None
        self._body = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        self.corp_id = corp_id
        if body is not None:
            self.body = body

    @property
    def x_request_id(self):
        """Gets the x_request_id of this UpdateResourceRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :return: The x_request_id of this UpdateResourceRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this UpdateResourceRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :param x_request_id: The x_request_id of this UpdateResourceRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this UpdateResourceRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :return: The accept_language of this UpdateResourceRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this UpdateResourceRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :param accept_language: The accept_language of this UpdateResourceRequest.
        :type accept_language: str
        """
        self._accept_language = accept_language

    @property
    def corp_id(self):
        """Gets the corp_id of this UpdateResourceRequest.

        企业id。

        :return: The corp_id of this UpdateResourceRequest.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        """Sets the corp_id of this UpdateResourceRequest.

        企业id。

        :param corp_id: The corp_id of this UpdateResourceRequest.
        :type corp_id: str
        """
        self._corp_id = corp_id

    @property
    def body(self):
        """Gets the body of this UpdateResourceRequest.


        :return: The body of this UpdateResourceRequest.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.ModResourceDTO`]
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateResourceRequest.


        :param body: The body of this UpdateResourceRequest.
        :type body: list[:class:`huaweicloudsdkmeeting.v1.ModResourceDTO`]
        """
        self._body = body

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
        if not isinstance(other, UpdateResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
