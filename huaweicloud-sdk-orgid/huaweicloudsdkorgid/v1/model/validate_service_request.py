# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateServiceRequest:

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
        'ticket': 'str'
    }

    attribute_map = {
        'service': 'service',
        'ticket': 'ticket'
    }

    def __init__(self, service=None, ticket=None):
        r"""ValidateServiceRequest

        The model defined in huaweicloud sdk

        :param service: 登录时携带的回调地址
        :type service: str
        :param ticket: 登录时系统返回的ticket
        :type ticket: str
        """
        
        

        self._service = None
        self._ticket = None
        self.discriminator = None

        self.service = service
        self.ticket = ticket

    @property
    def service(self):
        r"""Gets the service of this ValidateServiceRequest.

        登录时携带的回调地址

        :return: The service of this ValidateServiceRequest.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this ValidateServiceRequest.

        登录时携带的回调地址

        :param service: The service of this ValidateServiceRequest.
        :type service: str
        """
        self._service = service

    @property
    def ticket(self):
        r"""Gets the ticket of this ValidateServiceRequest.

        登录时系统返回的ticket

        :return: The ticket of this ValidateServiceRequest.
        :rtype: str
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        r"""Sets the ticket of this ValidateServiceRequest.

        登录时系统返回的ticket

        :param ticket: The ticket of this ValidateServiceRequest.
        :type ticket: str
        """
        self._ticket = ticket

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
        if not isinstance(other, ValidateServiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
