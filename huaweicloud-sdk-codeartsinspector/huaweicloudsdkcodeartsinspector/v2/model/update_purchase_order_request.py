# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePurchaseOrderRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service': 'str',
        'body': 'UpdateCbcOrderRequestBody'
    }

    attribute_map = {
        'service': 'service',
        'body': 'body'
    }

    def __init__(self, service=None, body=None):
        """UpdatePurchaseOrderRequest

        The model defined in huaweicloud sdk

        :param service: servicename,购买vss服务时使用\&quot;webscan\&quot;
        :type service: str
        :param body: Body of the UpdatePurchaseOrderRequest
        :type body: :class:`huaweicloudsdkcodeartsinspector.v2.UpdateCbcOrderRequestBody`
        """
        
        

        self._service = None
        self._body = None
        self.discriminator = None

        self.service = service
        if body is not None:
            self.body = body

    @property
    def service(self):
        """Gets the service of this UpdatePurchaseOrderRequest.

        servicename,购买vss服务时使用\"webscan\"

        :return: The service of this UpdatePurchaseOrderRequest.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this UpdatePurchaseOrderRequest.

        servicename,购买vss服务时使用\"webscan\"

        :param service: The service of this UpdatePurchaseOrderRequest.
        :type service: str
        """
        self._service = service

    @property
    def body(self):
        """Gets the body of this UpdatePurchaseOrderRequest.

        :return: The body of this UpdatePurchaseOrderRequest.
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v2.UpdateCbcOrderRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdatePurchaseOrderRequest.

        :param body: The body of this UpdatePurchaseOrderRequest.
        :type body: :class:`huaweicloudsdkcodeartsinspector.v2.UpdateCbcOrderRequestBody`
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
        if not isinstance(other, UpdatePurchaseOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
