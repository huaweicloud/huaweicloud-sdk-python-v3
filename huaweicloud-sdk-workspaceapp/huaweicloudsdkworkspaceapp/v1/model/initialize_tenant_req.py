# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InitializeTenantReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_status': 'str'
    }

    attribute_map = {
        'service_status': 'service_status'
    }

    def __init__(self, service_status=None):
        """InitializeTenantReq

        The model defined in huaweicloud sdk

        :param service_status: 服务状态 * &#x60;active&#x60; - 激活 * &#x60;inactive&#x60; - 未激活
        :type service_status: str
        """
        
        

        self._service_status = None
        self.discriminator = None

        self.service_status = service_status

    @property
    def service_status(self):
        """Gets the service_status of this InitializeTenantReq.

        服务状态 * `active` - 激活 * `inactive` - 未激活

        :return: The service_status of this InitializeTenantReq.
        :rtype: str
        """
        return self._service_status

    @service_status.setter
    def service_status(self, service_status):
        """Sets the service_status of this InitializeTenantReq.

        服务状态 * `active` - 激活 * `inactive` - 未激活

        :param service_status: The service_status of this InitializeTenantReq.
        :type service_status: str
        """
        self._service_status = service_status

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
        if not isinstance(other, InitializeTenantReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
