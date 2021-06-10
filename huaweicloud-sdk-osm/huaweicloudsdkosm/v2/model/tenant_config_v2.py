# coding: utf-8

import pprint
import re

import six





class TenantConfigV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'create_case_ccemail_max_count': 'int'
    }

    attribute_map = {
        'create_case_ccemail_max_count': 'create_case_ccemail_max_count'
    }

    def __init__(self, create_case_ccemail_max_count=None):
        """TenantConfigV2 - a model defined in huaweicloud sdk"""
        
        

        self._create_case_ccemail_max_count = None
        self.discriminator = None

        if create_case_ccemail_max_count is not None:
            self.create_case_ccemail_max_count = create_case_ccemail_max_count

    @property
    def create_case_ccemail_max_count(self):
        """Gets the create_case_ccemail_max_count of this TenantConfigV2.

        抄送邮箱最大个数

        :return: The create_case_ccemail_max_count of this TenantConfigV2.
        :rtype: int
        """
        return self._create_case_ccemail_max_count

    @create_case_ccemail_max_count.setter
    def create_case_ccemail_max_count(self, create_case_ccemail_max_count):
        """Sets the create_case_ccemail_max_count of this TenantConfigV2.

        抄送邮箱最大个数

        :param create_case_ccemail_max_count: The create_case_ccemail_max_count of this TenantConfigV2.
        :type: int
        """
        self._create_case_ccemail_max_count = create_case_ccemail_max_count

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
        if not isinstance(other, TenantConfigV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
