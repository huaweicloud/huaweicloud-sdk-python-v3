# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneCreateAgencyTokenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nocatalog': 'str',
        'body': 'KeystoneCreateAgencyTokenRequestBody'
    }

    attribute_map = {
        'nocatalog': 'nocatalog',
        'body': 'body'
    }

    def __init__(self, nocatalog=None, body=None):
        r"""KeystoneCreateAgencyTokenRequest

        The model defined in huaweicloud sdk

        :param nocatalog: 如果设置该参数，返回的响应体中将不显示catalog信息。任何非空字符串都将解释为true，并使该字段生效。
        :type nocatalog: str
        :param body: Body of the KeystoneCreateAgencyTokenRequest
        :type body: :class:`huaweicloudsdkiam.v3.KeystoneCreateAgencyTokenRequestBody`
        """
        
        

        self._nocatalog = None
        self._body = None
        self.discriminator = None

        if nocatalog is not None:
            self.nocatalog = nocatalog
        if body is not None:
            self.body = body

    @property
    def nocatalog(self):
        r"""Gets the nocatalog of this KeystoneCreateAgencyTokenRequest.

        如果设置该参数，返回的响应体中将不显示catalog信息。任何非空字符串都将解释为true，并使该字段生效。

        :return: The nocatalog of this KeystoneCreateAgencyTokenRequest.
        :rtype: str
        """
        return self._nocatalog

    @nocatalog.setter
    def nocatalog(self, nocatalog):
        r"""Sets the nocatalog of this KeystoneCreateAgencyTokenRequest.

        如果设置该参数，返回的响应体中将不显示catalog信息。任何非空字符串都将解释为true，并使该字段生效。

        :param nocatalog: The nocatalog of this KeystoneCreateAgencyTokenRequest.
        :type nocatalog: str
        """
        self._nocatalog = nocatalog

    @property
    def body(self):
        r"""Gets the body of this KeystoneCreateAgencyTokenRequest.

        :return: The body of this KeystoneCreateAgencyTokenRequest.
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateAgencyTokenRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this KeystoneCreateAgencyTokenRequest.

        :param body: The body of this KeystoneCreateAgencyTokenRequest.
        :type body: :class:`huaweicloudsdkiam.v3.KeystoneCreateAgencyTokenRequestBody`
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
        if not isinstance(other, KeystoneCreateAgencyTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
