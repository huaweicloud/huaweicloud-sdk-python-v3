# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateServiceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_response': 'ServiceResponse'
    }

    attribute_map = {
        'service_response': 'serviceResponse'
    }

    def __init__(self, service_response=None):
        """ValidateServiceResponse

        The model defined in huaweicloud sdk

        :param service_response: 
        :type service_response: :class:`huaweicloudsdkorgid.v1.ServiceResponse`
        """
        
        super(ValidateServiceResponse, self).__init__()

        self._service_response = None
        self.discriminator = None

        if service_response is not None:
            self.service_response = service_response

    @property
    def service_response(self):
        """Gets the service_response of this ValidateServiceResponse.

        :return: The service_response of this ValidateServiceResponse.
        :rtype: :class:`huaweicloudsdkorgid.v1.ServiceResponse`
        """
        return self._service_response

    @service_response.setter
    def service_response(self, service_response):
        """Sets the service_response of this ValidateServiceResponse.

        :param service_response: The service_response of this ValidateServiceResponse.
        :type service_response: :class:`huaweicloudsdkorgid.v1.ServiceResponse`
        """
        self._service_response = service_response

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
        if not isinstance(other, ValidateServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
