# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointService:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'service_name': 'service_name',
        'created_at': 'created_at'
    }

    def __init__(self, service_name=None, created_at=None):
        r"""EndpointService

        The model defined in huaweicloud sdk

        :param service_name: 终端节点服务名称
        :type service_name: str
        :param created_at: 创建时间
        :type created_at: datetime
        """
        
        

        self._service_name = None
        self._created_at = None
        self.discriminator = None

        if service_name is not None:
            self.service_name = service_name
        if created_at is not None:
            self.created_at = created_at

    @property
    def service_name(self):
        r"""Gets the service_name of this EndpointService.

        终端节点服务名称

        :return: The service_name of this EndpointService.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this EndpointService.

        终端节点服务名称

        :param service_name: The service_name of this EndpointService.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def created_at(self):
        r"""Gets the created_at of this EndpointService.

        创建时间

        :return: The created_at of this EndpointService.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this EndpointService.

        创建时间

        :param created_at: The created_at of this EndpointService.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, EndpointService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
