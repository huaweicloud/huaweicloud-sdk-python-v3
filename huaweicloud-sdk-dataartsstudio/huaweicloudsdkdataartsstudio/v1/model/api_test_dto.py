# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiTestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'str',
        'paras': 'ApiTestParas'
    }

    attribute_map = {
        'body': 'body',
        'paras': 'paras'
    }

    def __init__(self, body=None, paras=None):
        r"""ApiTestDTO

        The model defined in huaweicloud sdk

        :param body: 请求体
        :type body: str
        :param paras: 
        :type paras: :class:`huaweicloudsdkdataartsstudio.v1.ApiTestParas`
        """
        
        

        self._body = None
        self._paras = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if paras is not None:
            self.paras = paras

    @property
    def body(self):
        r"""Gets the body of this ApiTestDTO.

        请求体

        :return: The body of this ApiTestDTO.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ApiTestDTO.

        请求体

        :param body: The body of this ApiTestDTO.
        :type body: str
        """
        self._body = body

    @property
    def paras(self):
        r"""Gets the paras of this ApiTestDTO.

        :return: The paras of this ApiTestDTO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApiTestParas`
        """
        return self._paras

    @paras.setter
    def paras(self, paras):
        r"""Sets the paras of this ApiTestDTO.

        :param paras: The paras of this ApiTestDTO.
        :type paras: :class:`huaweicloudsdkdataartsstudio.v1.ApiTestParas`
        """
        self._paras = paras

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
        if not isinstance(other, ApiTestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
