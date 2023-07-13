# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceByIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider': 'str',
        'type': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'type': 'type',
        'resource_id': 'resource_id'
    }

    def __init__(self, provider=None, type=None, resource_id=None):
        """ShowResourceByIdRequest

        The model defined in huaweicloud sdk

        :param provider: 云服务名称
        :type provider: str
        :param type: 资源类型名称
        :type type: str
        :param resource_id: 资源ID
        :type resource_id: str
        """
        
        

        self._provider = None
        self._type = None
        self._resource_id = None
        self.discriminator = None

        self.provider = provider
        self.type = type
        self.resource_id = resource_id

    @property
    def provider(self):
        """Gets the provider of this ShowResourceByIdRequest.

        云服务名称

        :return: The provider of this ShowResourceByIdRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ShowResourceByIdRequest.

        云服务名称

        :param provider: The provider of this ShowResourceByIdRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        """Gets the type of this ShowResourceByIdRequest.

        资源类型名称

        :return: The type of this ShowResourceByIdRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowResourceByIdRequest.

        资源类型名称

        :param type: The type of this ShowResourceByIdRequest.
        :type type: str
        """
        self._type = type

    @property
    def resource_id(self):
        """Gets the resource_id of this ShowResourceByIdRequest.

        资源ID

        :return: The resource_id of this ShowResourceByIdRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ShowResourceByIdRequest.

        资源ID

        :param resource_id: The resource_id of this ShowResourceByIdRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, ShowResourceByIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
