# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_provider': 'str',
        'resource_type': 'str',
        'region_id': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_provider': 'resource_provider',
        'resource_type': 'resource_type',
        'region_id': 'region_id',
        'domain_id': 'domain_id'
    }

    def __init__(self, resource_id=None, resource_name=None, resource_provider=None, resource_type=None, region_id=None, domain_id=None):
        """PolicyResource

        The model defined in huaweicloud sdk

        :param resource_id: 资源id
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_provider: 云服务名称
        :type resource_provider: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param region_id: 区域id
        :type region_id: str
        :param domain_id: 资源所属用户ID
        :type domain_id: str
        """
        
        

        self._resource_id = None
        self._resource_name = None
        self._resource_provider = None
        self._resource_type = None
        self._region_id = None
        self._domain_id = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_provider is not None:
            self.resource_provider = resource_provider
        if resource_type is not None:
            self.resource_type = resource_type
        if region_id is not None:
            self.region_id = region_id
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def resource_id(self):
        """Gets the resource_id of this PolicyResource.

        资源id

        :return: The resource_id of this PolicyResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this PolicyResource.

        资源id

        :param resource_id: The resource_id of this PolicyResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this PolicyResource.

        资源名称

        :return: The resource_name of this PolicyResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this PolicyResource.

        资源名称

        :param resource_name: The resource_name of this PolicyResource.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_provider(self):
        """Gets the resource_provider of this PolicyResource.

        云服务名称

        :return: The resource_provider of this PolicyResource.
        :rtype: str
        """
        return self._resource_provider

    @resource_provider.setter
    def resource_provider(self, resource_provider):
        """Sets the resource_provider of this PolicyResource.

        云服务名称

        :param resource_provider: The resource_provider of this PolicyResource.
        :type resource_provider: str
        """
        self._resource_provider = resource_provider

    @property
    def resource_type(self):
        """Gets the resource_type of this PolicyResource.

        资源类型

        :return: The resource_type of this PolicyResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PolicyResource.

        资源类型

        :param resource_type: The resource_type of this PolicyResource.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def region_id(self):
        """Gets the region_id of this PolicyResource.

        区域id

        :return: The region_id of this PolicyResource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this PolicyResource.

        区域id

        :param region_id: The region_id of this PolicyResource.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def domain_id(self):
        """Gets the domain_id of this PolicyResource.

        资源所属用户ID

        :return: The domain_id of this PolicyResource.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this PolicyResource.

        资源所属用户ID

        :param domain_id: The domain_id of this PolicyResource.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, PolicyResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
