# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectableAgentStatusResource:

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
        'resource_type': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type'
    }

    def __init__(self, resource_id=None, resource_name=None, resource_type=None):
        """ProtectableAgentStatusResource

        The model defined in huaweicloud sdk

        :param resource_id: 待检查资源ID
        :type resource_id: str
        :param resource_name: 待检查资源name
        :type resource_name: str
        :param resource_type: 待检查的资源类型。当前支持的取值包含两个：OS::Nova::Server，该值代表保护的资源为云服务器，OS::Ironic::BareMetalServer，该值代表保护的资源为裸金属服务器。
        :type resource_type: str
        """
        
        

        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self.discriminator = None

        self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        self.resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this ProtectableAgentStatusResource.

        待检查资源ID

        :return: The resource_id of this ProtectableAgentStatusResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ProtectableAgentStatusResource.

        待检查资源ID

        :param resource_id: The resource_id of this ProtectableAgentStatusResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ProtectableAgentStatusResource.

        待检查资源name

        :return: The resource_name of this ProtectableAgentStatusResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ProtectableAgentStatusResource.

        待检查资源name

        :param resource_name: The resource_name of this ProtectableAgentStatusResource.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this ProtectableAgentStatusResource.

        待检查的资源类型。当前支持的取值包含两个：OS::Nova::Server，该值代表保护的资源为云服务器，OS::Ironic::BareMetalServer，该值代表保护的资源为裸金属服务器。

        :return: The resource_type of this ProtectableAgentStatusResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ProtectableAgentStatusResource.

        待检查的资源类型。当前支持的取值包含两个：OS::Nova::Server，该值代表保护的资源为云服务器，OS::Ironic::BareMetalServer，该值代表保护的资源为裸金属服务器。

        :param resource_type: The resource_type of this ProtectableAgentStatusResource.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ProtectableAgentStatusResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
