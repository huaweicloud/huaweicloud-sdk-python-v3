# coding: utf-8

import pprint
import re

import six





class RelativeResource:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'relative_resource_id': 'str',
        'relative_resource_name': 'str',
        'relative_cloud_service_type': 'str'
    }

    attribute_map = {
        'relative_resource_id': 'relativeResourceId',
        'relative_resource_name': 'relativeResourceName',
        'relative_cloud_service_type': 'relativeCloudServiceType'
    }

    def __init__(self, relative_resource_id=None, relative_resource_name=None, relative_cloud_service_type=None):
        """RelativeResource - a model defined in huaweicloud sdk"""
        
        

        self._relative_resource_id = None
        self._relative_resource_name = None
        self._relative_cloud_service_type = None
        self.discriminator = None

        if relative_resource_id is not None:
            self.relative_resource_id = relative_resource_id
        if relative_resource_name is not None:
            self.relative_resource_name = relative_resource_name
        if relative_cloud_service_type is not None:
            self.relative_cloud_service_type = relative_cloud_service_type

    @property
    def relative_resource_id(self):
        """Gets the relative_resource_id of this RelativeResource.

        关联资源Id

        :return: The relative_resource_id of this RelativeResource.
        :rtype: str
        """
        return self._relative_resource_id

    @relative_resource_id.setter
    def relative_resource_id(self, relative_resource_id):
        """Sets the relative_resource_id of this RelativeResource.

        关联资源Id

        :param relative_resource_id: The relative_resource_id of this RelativeResource.
        :type: str
        """
        self._relative_resource_id = relative_resource_id

    @property
    def relative_resource_name(self):
        """Gets the relative_resource_name of this RelativeResource.

        关联资源名称

        :return: The relative_resource_name of this RelativeResource.
        :rtype: str
        """
        return self._relative_resource_name

    @relative_resource_name.setter
    def relative_resource_name(self, relative_resource_name):
        """Sets the relative_resource_name of this RelativeResource.

        关联资源名称

        :param relative_resource_name: The relative_resource_name of this RelativeResource.
        :type: str
        """
        self._relative_resource_name = relative_resource_name

    @property
    def relative_cloud_service_type(self):
        """Gets the relative_cloud_service_type of this RelativeResource.

        关联云服务名称

        :return: The relative_cloud_service_type of this RelativeResource.
        :rtype: str
        """
        return self._relative_cloud_service_type

    @relative_cloud_service_type.setter
    def relative_cloud_service_type(self, relative_cloud_service_type):
        """Sets the relative_cloud_service_type of this RelativeResource.

        关联云服务名称

        :param relative_cloud_service_type: The relative_cloud_service_type of this RelativeResource.
        :type: str
        """
        self._relative_cloud_service_type = relative_cloud_service_type

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
        if not isinstance(other, RelativeResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
