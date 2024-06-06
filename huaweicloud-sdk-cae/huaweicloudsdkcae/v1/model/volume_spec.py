# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_sub_type': 'str',
        'resources': 'list[str]',
        'resources_credentials': 'list[ResourcesCredential]'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_sub_type': 'resource_sub_type',
        'resources': 'resources',
        'resources_credentials': 'resources_credentials'
    }

    def __init__(self, resource_type=None, resource_sub_type=None, resources=None, resources_credentials=None):
        """VolumeSpec

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型，当前只支持“obs”和“sfs”。
        :type resource_type: str
        :param resource_sub_type: 对象存储类型。
        :type resource_sub_type: str
        :param resources: 云存储名称。
        :type resources: list[str]
        :param resources_credentials: 云存储和授权凭证，获取环境列表接口响应中env_category字段为v2时需添加该字段的值。
        :type resources_credentials: list[:class:`huaweicloudsdkcae.v1.ResourcesCredential`]
        """
        
        

        self._resource_type = None
        self._resource_sub_type = None
        self._resources = None
        self._resources_credentials = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_sub_type = resource_sub_type
        self.resources = resources
        if resources_credentials is not None:
            self.resources_credentials = resources_credentials

    @property
    def resource_type(self):
        """Gets the resource_type of this VolumeSpec.

        资源类型，当前只支持“obs”和“sfs”。

        :return: The resource_type of this VolumeSpec.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this VolumeSpec.

        资源类型，当前只支持“obs”和“sfs”。

        :param resource_type: The resource_type of this VolumeSpec.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_sub_type(self):
        """Gets the resource_sub_type of this VolumeSpec.

        对象存储类型。

        :return: The resource_sub_type of this VolumeSpec.
        :rtype: str
        """
        return self._resource_sub_type

    @resource_sub_type.setter
    def resource_sub_type(self, resource_sub_type):
        """Sets the resource_sub_type of this VolumeSpec.

        对象存储类型。

        :param resource_sub_type: The resource_sub_type of this VolumeSpec.
        :type resource_sub_type: str
        """
        self._resource_sub_type = resource_sub_type

    @property
    def resources(self):
        """Gets the resources of this VolumeSpec.

        云存储名称。

        :return: The resources of this VolumeSpec.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this VolumeSpec.

        云存储名称。

        :param resources: The resources of this VolumeSpec.
        :type resources: list[str]
        """
        self._resources = resources

    @property
    def resources_credentials(self):
        """Gets the resources_credentials of this VolumeSpec.

        云存储和授权凭证，获取环境列表接口响应中env_category字段为v2时需添加该字段的值。

        :return: The resources_credentials of this VolumeSpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.ResourcesCredential`]
        """
        return self._resources_credentials

    @resources_credentials.setter
    def resources_credentials(self, resources_credentials):
        """Sets the resources_credentials of this VolumeSpec.

        云存储和授权凭证，获取环境列表接口响应中env_category字段为v2时需添加该字段的值。

        :param resources_credentials: The resources_credentials of this VolumeSpec.
        :type resources_credentials: list[:class:`huaweicloudsdkcae.v1.ResourcesCredential`]
        """
        self._resources_credentials = resources_credentials

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
        if not isinstance(other, VolumeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
