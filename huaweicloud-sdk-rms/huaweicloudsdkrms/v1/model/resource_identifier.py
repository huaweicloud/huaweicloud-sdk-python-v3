# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceIdentifier:

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
        'provider': 'str',
        'type': 'str',
        'source_account_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'provider': 'provider',
        'type': 'type',
        'source_account_id': 'source_account_id',
        'region_id': 'region_id'
    }

    def __init__(self, resource_id=None, resource_name=None, provider=None, type=None, source_account_id=None, region_id=None):
        """ResourceIdentifier

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_name: 资源名称。
        :type resource_name: str
        :param provider: 云服务类型。
        :type provider: str
        :param type: 资源类型。
        :type type: str
        :param source_account_id: 源帐号ID。
        :type source_account_id: str
        :param region_id: 资源所属区域。
        :type region_id: str
        """
        
        

        self._resource_id = None
        self._resource_name = None
        self._provider = None
        self._type = None
        self._source_account_id = None
        self._region_id = None
        self.discriminator = None

        self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        self.provider = provider
        self.type = type
        self.source_account_id = source_account_id
        self.region_id = region_id

    @property
    def resource_id(self):
        """Gets the resource_id of this ResourceIdentifier.

        资源ID。

        :return: The resource_id of this ResourceIdentifier.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ResourceIdentifier.

        资源ID。

        :param resource_id: The resource_id of this ResourceIdentifier.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ResourceIdentifier.

        资源名称。

        :return: The resource_name of this ResourceIdentifier.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ResourceIdentifier.

        资源名称。

        :param resource_name: The resource_name of this ResourceIdentifier.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def provider(self):
        """Gets the provider of this ResourceIdentifier.

        云服务类型。

        :return: The provider of this ResourceIdentifier.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ResourceIdentifier.

        云服务类型。

        :param provider: The provider of this ResourceIdentifier.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        """Gets the type of this ResourceIdentifier.

        资源类型。

        :return: The type of this ResourceIdentifier.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceIdentifier.

        资源类型。

        :param type: The type of this ResourceIdentifier.
        :type type: str
        """
        self._type = type

    @property
    def source_account_id(self):
        """Gets the source_account_id of this ResourceIdentifier.

        源帐号ID。

        :return: The source_account_id of this ResourceIdentifier.
        :rtype: str
        """
        return self._source_account_id

    @source_account_id.setter
    def source_account_id(self, source_account_id):
        """Sets the source_account_id of this ResourceIdentifier.

        源帐号ID。

        :param source_account_id: The source_account_id of this ResourceIdentifier.
        :type source_account_id: str
        """
        self._source_account_id = source_account_id

    @property
    def region_id(self):
        """Gets the region_id of this ResourceIdentifier.

        资源所属区域。

        :return: The region_id of this ResourceIdentifier.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ResourceIdentifier.

        资源所属区域。

        :param region_id: The region_id of this ResourceIdentifier.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, ResourceIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
