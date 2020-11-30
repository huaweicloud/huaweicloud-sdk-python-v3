# coding: utf-8

import pprint
import re

import six





class CreateRequestBodyTurboInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'share_type': 'str',
        'type': 'str',
        'available_zone': 'str',
        'resource_spec_code': 'str'
    }

    attribute_map = {
        'share_type': 'share_type',
        'type': 'type',
        'available_zone': 'available_zone',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, share_type=None, type=None, available_zone=None, resource_spec_code=None):
        """CreateRequestBodyTurboInfo - a model defined in huaweicloud sdk"""
        
        

        self._share_type = None
        self._type = None
        self._available_zone = None
        self._resource_spec_code = None
        self.discriminator = None

        if share_type is not None:
            self.share_type = share_type
        if type is not None:
            self.type = type
        if available_zone is not None:
            self.available_zone = available_zone
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code

    @property
    def share_type(self):
        """Gets the share_type of this CreateRequestBodyTurboInfo.

        共享方式

        :return: The share_type of this CreateRequestBodyTurboInfo.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this CreateRequestBodyTurboInfo.

        共享方式

        :param share_type: The share_type of this CreateRequestBodyTurboInfo.
        :type: str
        """
        self._share_type = share_type

    @property
    def type(self):
        """Gets the type of this CreateRequestBodyTurboInfo.

        类型

        :return: The type of this CreateRequestBodyTurboInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateRequestBodyTurboInfo.

        类型

        :param type: The type of this CreateRequestBodyTurboInfo.
        :type: str
        """
        self._type = type

    @property
    def available_zone(self):
        """Gets the available_zone of this CreateRequestBodyTurboInfo.

        可用区

        :return: The available_zone of this CreateRequestBodyTurboInfo.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        """Sets the available_zone of this CreateRequestBodyTurboInfo.

        可用区

        :param available_zone: The available_zone of this CreateRequestBodyTurboInfo.
        :type: str
        """
        self._available_zone = available_zone

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this CreateRequestBodyTurboInfo.

        规格

        :return: The resource_spec_code of this CreateRequestBodyTurboInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this CreateRequestBodyTurboInfo.

        规格

        :param resource_spec_code: The resource_spec_code of this CreateRequestBodyTurboInfo.
        :type: str
        """
        self._resource_spec_code = resource_spec_code

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
        if not isinstance(other, CreateRequestBodyTurboInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
