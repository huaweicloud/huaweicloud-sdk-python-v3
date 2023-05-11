# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyFilterDefinition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'resource_provider': 'str',
        'resource_type': 'str',
        'resource_id': 'str',
        'tag_key': 'str',
        'tag_value': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'resource_provider': 'resource_provider',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'tag_key': 'tag_key',
        'tag_value': 'tag_value'
    }

    def __init__(self, region_id=None, resource_provider=None, resource_type=None, resource_id=None, tag_key=None, tag_value=None):
        """PolicyFilterDefinition

        The model defined in huaweicloud sdk

        :param region_id: 区域ID
        :type region_id: str
        :param resource_provider: 云服务名称
        :type resource_provider: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param tag_key: 标签键
        :type tag_key: str
        :param tag_value: 标签值
        :type tag_value: str
        """
        
        

        self._region_id = None
        self._resource_provider = None
        self._resource_type = None
        self._resource_id = None
        self._tag_key = None
        self._tag_value = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if resource_provider is not None:
            self.resource_provider = resource_provider
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id
        if tag_key is not None:
            self.tag_key = tag_key
        if tag_value is not None:
            self.tag_value = tag_value

    @property
    def region_id(self):
        """Gets the region_id of this PolicyFilterDefinition.

        区域ID

        :return: The region_id of this PolicyFilterDefinition.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this PolicyFilterDefinition.

        区域ID

        :param region_id: The region_id of this PolicyFilterDefinition.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_provider(self):
        """Gets the resource_provider of this PolicyFilterDefinition.

        云服务名称

        :return: The resource_provider of this PolicyFilterDefinition.
        :rtype: str
        """
        return self._resource_provider

    @resource_provider.setter
    def resource_provider(self, resource_provider):
        """Sets the resource_provider of this PolicyFilterDefinition.

        云服务名称

        :param resource_provider: The resource_provider of this PolicyFilterDefinition.
        :type resource_provider: str
        """
        self._resource_provider = resource_provider

    @property
    def resource_type(self):
        """Gets the resource_type of this PolicyFilterDefinition.

        资源类型

        :return: The resource_type of this PolicyFilterDefinition.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PolicyFilterDefinition.

        资源类型

        :param resource_type: The resource_type of this PolicyFilterDefinition.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this PolicyFilterDefinition.

        资源ID

        :return: The resource_id of this PolicyFilterDefinition.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this PolicyFilterDefinition.

        资源ID

        :param resource_id: The resource_id of this PolicyFilterDefinition.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def tag_key(self):
        """Gets the tag_key of this PolicyFilterDefinition.

        标签键

        :return: The tag_key of this PolicyFilterDefinition.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        """Sets the tag_key of this PolicyFilterDefinition.

        标签键

        :param tag_key: The tag_key of this PolicyFilterDefinition.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def tag_value(self):
        """Gets the tag_value of this PolicyFilterDefinition.

        标签值

        :return: The tag_value of this PolicyFilterDefinition.
        :rtype: str
        """
        return self._tag_value

    @tag_value.setter
    def tag_value(self, tag_value):
        """Sets the tag_value of this PolicyFilterDefinition.

        标签值

        :param tag_value: The tag_value of this PolicyFilterDefinition.
        :type tag_value: str
        """
        self._tag_value = tag_value

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
        if not isinstance(other, PolicyFilterDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
