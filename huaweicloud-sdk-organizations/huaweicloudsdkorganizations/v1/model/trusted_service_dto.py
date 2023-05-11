# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrustedServiceDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_principal': 'str',
        'enabled_at': 'datetime'
    }

    attribute_map = {
        'service_principal': 'service_principal',
        'enabled_at': 'enabled_at'
    }

    def __init__(self, service_principal=None, enabled_at=None):
        """TrustedServiceDto

        The model defined in huaweicloud sdk

        :param service_principal: 可信服务的名称。
        :type service_principal: str
        :param enabled_at: 可信服务与组织集成的日期。
        :type enabled_at: datetime
        """
        
        

        self._service_principal = None
        self._enabled_at = None
        self.discriminator = None

        self.service_principal = service_principal
        self.enabled_at = enabled_at

    @property
    def service_principal(self):
        """Gets the service_principal of this TrustedServiceDto.

        可信服务的名称。

        :return: The service_principal of this TrustedServiceDto.
        :rtype: str
        """
        return self._service_principal

    @service_principal.setter
    def service_principal(self, service_principal):
        """Sets the service_principal of this TrustedServiceDto.

        可信服务的名称。

        :param service_principal: The service_principal of this TrustedServiceDto.
        :type service_principal: str
        """
        self._service_principal = service_principal

    @property
    def enabled_at(self):
        """Gets the enabled_at of this TrustedServiceDto.

        可信服务与组织集成的日期。

        :return: The enabled_at of this TrustedServiceDto.
        :rtype: datetime
        """
        return self._enabled_at

    @enabled_at.setter
    def enabled_at(self, enabled_at):
        """Sets the enabled_at of this TrustedServiceDto.

        可信服务与组织集成的日期。

        :param enabled_at: The enabled_at of this TrustedServiceDto.
        :type enabled_at: datetime
        """
        self._enabled_at = enabled_at

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
        if not isinstance(other, TrustedServiceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
