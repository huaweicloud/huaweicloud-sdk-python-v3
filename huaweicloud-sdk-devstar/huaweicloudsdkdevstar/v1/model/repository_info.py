# coding: utf-8

import pprint
import re

import six





class RepositoryInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'project_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'project_id': 'project_id',
        'region_id': 'region_id'
    }

    def __init__(self, name=None, project_id=None, region_id=None):
        """RepositoryInfo - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._project_id = None
        self._region_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id

    @property
    def name(self):
        """Gets the name of this RepositoryInfo.

        代码仓的名称

        :return: The name of this RepositoryInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositoryInfo.

        代码仓的名称

        :param name: The name of this RepositoryInfo.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this RepositoryInfo.

        项目id

        :return: The project_id of this RepositoryInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RepositoryInfo.

        项目id

        :param project_id: The project_id of this RepositoryInfo.
        :type: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        """Gets the region_id of this RepositoryInfo.

        区域id

        :return: The region_id of this RepositoryInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this RepositoryInfo.

        区域id

        :param region_id: The region_id of this RepositoryInfo.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RepositoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
