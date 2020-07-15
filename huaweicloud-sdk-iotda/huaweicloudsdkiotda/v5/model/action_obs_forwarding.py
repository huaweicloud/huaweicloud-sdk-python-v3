# coding: utf-8

import pprint
import re

import six





class ActionObsForwarding:


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
        'bucket_name': 'str',
        'location': 'str'
    }

    attribute_map = {
        'region_name': 'region_name',
        'project_id': 'project_id',
        'bucket_name': 'bucket_name',
        'location': 'location'
    }

    def __init__(self, region_name=None, project_id=None, bucket_name=None, location=None):
        """ActionObsForwarding - a model defined in huaweicloud sdk"""
        
        

        self._region_name = None
        self._project_id = None
        self._bucket_name = None
        self._location = None
        self.discriminator = None

        self.region_name = region_name
        self.project_id = project_id
        self.bucket_name = bucket_name
        if location is not None:
            self.location = location

    @property
    def region_name(self):
        """Gets the region_name of this ActionObsForwarding.

        OBS服务对应的region区域

        :return: The region_name of this ActionObsForwarding.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ActionObsForwarding.

        OBS服务对应的region区域

        :param region_name: The region_name of this ActionObsForwarding.
        :type: str
        """
        self._region_name = region_name

    @property
    def project_id(self):
        """Gets the project_id of this ActionObsForwarding.

        OBS服务对应的projectId信息

        :return: The project_id of this ActionObsForwarding.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ActionObsForwarding.

        OBS服务对应的projectId信息

        :param project_id: The project_id of this ActionObsForwarding.
        :type: str
        """
        self._project_id = project_id

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ActionObsForwarding.

        OBS服务对应的桶名称

        :return: The bucket_name of this ActionObsForwarding.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ActionObsForwarding.

        OBS服务对应的桶名称

        :param bucket_name: The bucket_name of this ActionObsForwarding.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def location(self):
        """Gets the location of this ActionObsForwarding.

        OBS服务对应桶的区域

        :return: The location of this ActionObsForwarding.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ActionObsForwarding.

        OBS服务对应桶的区域

        :param location: The location of this ActionObsForwarding.
        :type: str
        """
        self._location = location

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
        if not isinstance(other, ActionObsForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
