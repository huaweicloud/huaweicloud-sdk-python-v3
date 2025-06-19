# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePeriodElasticResourcePoolSpecChangeOrderRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody'
    }

    attribute_map = {
        'body': 'body'
    }

    def __init__(self, body=None):
        r"""CreatePeriodElasticResourcePoolSpecChangeOrderRequest

        The model defined in huaweicloud sdk

        :param body: Body of the CreatePeriodElasticResourcePoolSpecChangeOrderRequest
        :type body: :class:`huaweicloudsdkdli.v1.CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody`
        """
        
        

        self._body = None
        self.discriminator = None

        if body is not None:
            self.body = body

    @property
    def body(self):
        r"""Gets the body of this CreatePeriodElasticResourcePoolSpecChangeOrderRequest.

        :return: The body of this CreatePeriodElasticResourcePoolSpecChangeOrderRequest.
        :rtype: :class:`huaweicloudsdkdli.v1.CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreatePeriodElasticResourcePoolSpecChangeOrderRequest.

        :param body: The body of this CreatePeriodElasticResourcePoolSpecChangeOrderRequest.
        :type body: :class:`huaweicloudsdkdli.v1.CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody`
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
        if not isinstance(other, CreatePeriodElasticResourcePoolSpecChangeOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
