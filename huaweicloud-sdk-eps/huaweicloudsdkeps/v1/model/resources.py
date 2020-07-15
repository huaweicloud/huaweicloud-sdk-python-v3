# coding: utf-8

import pprint
import re

import six





class Resources:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'resource_detail': 'object',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'resource_detail': 'resource_detail',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type'
    }

    def __init__(self, enterprise_project_id=None, project_id=None, project_name=None, resource_detail=None, resource_id=None, resource_name=None, resource_type=None):
        """Resources - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self._project_id = None
        self._project_name = None
        self._resource_detail = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.project_id = project_id
        self.project_name = project_name
        self.resource_detail = resource_detail
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Resources.

        企业项目ID

        :return: The enterprise_project_id of this Resources.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Resources.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this Resources.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        """Gets the project_id of this Resources.

        ProjectID

        :return: The project_id of this Resources.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Resources.

        ProjectID

        :param project_id: The project_id of this Resources.
        :type: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this Resources.

        Project名称

        :return: The project_name of this Resources.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this Resources.

        Project名称

        :param project_name: The project_name of this Resources.
        :type: str
        """
        self._project_name = project_name

    @property
    def resource_detail(self):
        """Gets the resource_detail of this Resources.

        资源详情

        :return: The resource_detail of this Resources.
        :rtype: object
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        """Sets the resource_detail of this Resources.

        资源详情

        :param resource_detail: The resource_detail of this Resources.
        :type: object
        """
        self._resource_detail = resource_detail

    @property
    def resource_id(self):
        """Gets the resource_id of this Resources.

        资源ID

        :return: The resource_id of this Resources.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Resources.

        资源ID

        :param resource_id: The resource_id of this Resources.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this Resources.

        资源名称

        :return: The resource_name of this Resources.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this Resources.

        资源名称

        :param resource_name: The resource_name of this Resources.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this Resources.

        资源类型

        :return: The resource_type of this Resources.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Resources.

        资源类型

        :param resource_type: The resource_type of this Resources.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Resources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
