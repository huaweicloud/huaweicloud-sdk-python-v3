# coding: utf-8

import pprint
import re

import six





class Resource:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'resource_infos': 'list[ResourceInfo]'
    }

    attribute_map = {
        'tenant_id': 'tenantId',
        'resource_infos': 'resourceInfos'
    }

    def __init__(self, tenant_id=None, resource_infos=None):
        """Resource - a model defined in huaweicloud sdk"""
        
        

        self._tenant_id = None
        self._resource_infos = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if resource_infos is not None:
            self.resource_infos = resource_infos

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Resource.

        租户Id

        :return: The tenant_id of this Resource.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Resource.

        租户Id

        :param tenant_id: The tenant_id of this Resource.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def resource_infos(self):
        """Gets the resource_infos of this Resource.

        资源信息列表

        :return: The resource_infos of this Resource.
        :rtype: list[ResourceInfo]
        """
        return self._resource_infos

    @resource_infos.setter
    def resource_infos(self, resource_infos):
        """Sets the resource_infos of this Resource.

        资源信息列表

        :param resource_infos: The resource_infos of this Resource.
        :type: list[ResourceInfo]
        """
        self._resource_infos = resource_infos

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
