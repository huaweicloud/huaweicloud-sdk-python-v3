# coding: utf-8

import pprint
import re

import six





class ModCorpDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'basic_info': 'ModCorpBasicDTO',
        'admin_info': 'ModAdminDTO'
    }

    attribute_map = {
        'basic_info': 'basicInfo',
        'admin_info': 'adminInfo'
    }

    def __init__(self, basic_info=None, admin_info=None):
        """ModCorpDTO - a model defined in huaweicloud sdk"""
        
        

        self._basic_info = None
        self._admin_info = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if admin_info is not None:
            self.admin_info = admin_info

    @property
    def basic_info(self):
        """Gets the basic_info of this ModCorpDTO.


        :return: The basic_info of this ModCorpDTO.
        :rtype: ModCorpBasicDTO
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this ModCorpDTO.


        :param basic_info: The basic_info of this ModCorpDTO.
        :type: ModCorpBasicDTO
        """
        self._basic_info = basic_info

    @property
    def admin_info(self):
        """Gets the admin_info of this ModCorpDTO.


        :return: The admin_info of this ModCorpDTO.
        :rtype: ModAdminDTO
        """
        return self._admin_info

    @admin_info.setter
    def admin_info(self, admin_info):
        """Sets the admin_info of this ModCorpDTO.


        :param admin_info: The admin_info of this ModCorpDTO.
        :type: ModAdminDTO
        """
        self._admin_info = admin_info

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
        if not isinstance(other, ModCorpDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
