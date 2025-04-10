# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGaussDbInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'subscription_agency': 'str',
        'body': 'OpenGaussInstanceRequestBody'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'subscription_agency': 'Subscription-Agency',
        'body': 'body'
    }

    def __init__(self, x_language=None, subscription_agency=None, body=None):
        r"""CreateGaussDbInstanceRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param subscription_agency: 委托urn。使用RAM共享的KMS秘钥创建包周期实例时必填,格式iam::{account_id}:agency:{agency_name}。
        :type subscription_agency: str
        :param body: Body of the CreateGaussDbInstanceRequest
        :type body: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussInstanceRequestBody`
        """
        
        

        self._x_language = None
        self._subscription_agency = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if subscription_agency is not None:
            self.subscription_agency = subscription_agency
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this CreateGaussDbInstanceRequest.

        语言

        :return: The x_language of this CreateGaussDbInstanceRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this CreateGaussDbInstanceRequest.

        语言

        :param x_language: The x_language of this CreateGaussDbInstanceRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def subscription_agency(self):
        r"""Gets the subscription_agency of this CreateGaussDbInstanceRequest.

        委托urn。使用RAM共享的KMS秘钥创建包周期实例时必填,格式iam::{account_id}:agency:{agency_name}。

        :return: The subscription_agency of this CreateGaussDbInstanceRequest.
        :rtype: str
        """
        return self._subscription_agency

    @subscription_agency.setter
    def subscription_agency(self, subscription_agency):
        r"""Sets the subscription_agency of this CreateGaussDbInstanceRequest.

        委托urn。使用RAM共享的KMS秘钥创建包周期实例时必填,格式iam::{account_id}:agency:{agency_name}。

        :param subscription_agency: The subscription_agency of this CreateGaussDbInstanceRequest.
        :type subscription_agency: str
        """
        self._subscription_agency = subscription_agency

    @property
    def body(self):
        r"""Gets the body of this CreateGaussDbInstanceRequest.

        :return: The body of this CreateGaussDbInstanceRequest.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussInstanceRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateGaussDbInstanceRequest.

        :param body: The body of this CreateGaussDbInstanceRequest.
        :type body: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussInstanceRequestBody`
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
        if not isinstance(other, CreateGaussDbInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
