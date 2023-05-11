# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DelegatedServiceDto:

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
        'delegation_enabled_at': 'datetime'
    }

    attribute_map = {
        'service_principal': 'service_principal',
        'delegation_enabled_at': 'delegation_enabled_at'
    }

    def __init__(self, service_principal=None, delegation_enabled_at=None):
        """DelegatedServiceDto

        The model defined in huaweicloud sdk

        :param service_principal: 服务主体的名称。
        :type service_principal: str
        :param delegation_enabled_at: 帐号成为此服务的委托管理员的日期。
        :type delegation_enabled_at: datetime
        """
        
        

        self._service_principal = None
        self._delegation_enabled_at = None
        self.discriminator = None

        self.service_principal = service_principal
        self.delegation_enabled_at = delegation_enabled_at

    @property
    def service_principal(self):
        """Gets the service_principal of this DelegatedServiceDto.

        服务主体的名称。

        :return: The service_principal of this DelegatedServiceDto.
        :rtype: str
        """
        return self._service_principal

    @service_principal.setter
    def service_principal(self, service_principal):
        """Sets the service_principal of this DelegatedServiceDto.

        服务主体的名称。

        :param service_principal: The service_principal of this DelegatedServiceDto.
        :type service_principal: str
        """
        self._service_principal = service_principal

    @property
    def delegation_enabled_at(self):
        """Gets the delegation_enabled_at of this DelegatedServiceDto.

        帐号成为此服务的委托管理员的日期。

        :return: The delegation_enabled_at of this DelegatedServiceDto.
        :rtype: datetime
        """
        return self._delegation_enabled_at

    @delegation_enabled_at.setter
    def delegation_enabled_at(self, delegation_enabled_at):
        """Sets the delegation_enabled_at of this DelegatedServiceDto.

        帐号成为此服务的委托管理员的日期。

        :param delegation_enabled_at: The delegation_enabled_at of this DelegatedServiceDto.
        :type delegation_enabled_at: datetime
        """
        self._delegation_enabled_at = delegation_enabled_at

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
        if not isinstance(other, DelegatedServiceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
