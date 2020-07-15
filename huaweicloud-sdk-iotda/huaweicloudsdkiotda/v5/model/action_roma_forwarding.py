# coding: utf-8

import pprint
import re

import six





class ActionRomaForwarding:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'region_name': 'str',
        'project_id': 'str',
        'roma_push_type': 'str'
    }

    attribute_map = {
        'region_name': 'region_name',
        'project_id': 'project_id',
        'roma_push_type': 'roma_push_type'
    }

    def __init__(self, region_name=None, project_id=None, roma_push_type=None):
        """ActionRomaForwarding - a model defined in huaweicloud sdk"""
        
        

        self._region_name = None
        self._project_id = None
        self._roma_push_type = None
        self.discriminator = None

        self.region_name = region_name
        self.project_id = project_id
        if roma_push_type is not None:
            self.roma_push_type = roma_push_type

    @property
    def region_name(self):
        """Gets the region_name of this ActionRomaForwarding.

        ROMA服务对应的region区域

        :return: The region_name of this ActionRomaForwarding.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ActionRomaForwarding.

        ROMA服务对应的region区域

        :param region_name: The region_name of this ActionRomaForwarding.
        :type: str
        """
        self._region_name = region_name

    @property
    def project_id(self):
        """Gets the project_id of this ActionRomaForwarding.

        ROMA服务对应的projectId信息

        :return: The project_id of this ActionRomaForwarding.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ActionRomaForwarding.

        ROMA服务对应的projectId信息

        :param project_id: The project_id of this ActionRomaForwarding.
        :type: str
        """
        self._project_id = project_id

    @property
    def roma_push_type(self):
        """Gets the roma_push_type of this ActionRomaForwarding.

        ROMA服务对应参数类型

        :return: The roma_push_type of this ActionRomaForwarding.
        :rtype: str
        """
        return self._roma_push_type

    @roma_push_type.setter
    def roma_push_type(self, roma_push_type):
        """Sets the roma_push_type of this ActionRomaForwarding.

        ROMA服务对应参数类型

        :param roma_push_type: The roma_push_type of this ActionRomaForwarding.
        :type: str
        """
        self._roma_push_type = roma_push_type

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
        if not isinstance(other, ActionRomaForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
