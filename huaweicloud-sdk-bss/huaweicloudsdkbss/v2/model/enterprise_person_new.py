# coding: utf-8

import pprint
import re

import six





class EnterprisePersonNew:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'legel_name': 'str',
        'legel_id_number': 'str',
        'certifier_role': 'str'
    }

    attribute_map = {
        'legel_name': 'legel_name',
        'legel_id_number': 'legel_id_number',
        'certifier_role': 'certifier_role'
    }

    def __init__(self, legel_name=None, legel_id_number=None, certifier_role=None):
        """EnterprisePersonNew - a model defined in huaweicloud sdk"""
        
        

        self._legel_name = None
        self._legel_id_number = None
        self._certifier_role = None
        self.discriminator = None

        self.legel_name = legel_name
        self.legel_id_number = legel_id_number
        if certifier_role is not None:
            self.certifier_role = certifier_role

    @property
    def legel_name(self):
        """Gets the legel_name of this EnterprisePersonNew.

        |参数名称：法人姓名| |参数的约束及描述：该参数必填，且只允许字符串|

        :return: The legel_name of this EnterprisePersonNew.
        :rtype: str
        """
        return self._legel_name

    @legel_name.setter
    def legel_name(self, legel_name):
        """Sets the legel_name of this EnterprisePersonNew.

        |参数名称：法人姓名| |参数的约束及描述：该参数必填，且只允许字符串|

        :param legel_name: The legel_name of this EnterprisePersonNew.
        :type: str
        """
        self._legel_name = legel_name

    @property
    def legel_id_number(self):
        """Gets the legel_id_number of this EnterprisePersonNew.

        |参数名称：法人身份证号| |参数的约束及描述：该参数必填，且只允许字符串|

        :return: The legel_id_number of this EnterprisePersonNew.
        :rtype: str
        """
        return self._legel_id_number

    @legel_id_number.setter
    def legel_id_number(self, legel_id_number):
        """Sets the legel_id_number of this EnterprisePersonNew.

        |参数名称：法人身份证号| |参数的约束及描述：该参数必填，且只允许字符串|

        :param legel_id_number: The legel_id_number of this EnterprisePersonNew.
        :type: str
        """
        self._legel_id_number = legel_id_number

    @property
    def certifier_role(self):
        """Gets the certifier_role of this EnterprisePersonNew.

        |参数名称：认证人角色| |参数的约束及描述：该参数非必填，legalPerson ：法人代表 authorizedPerson：授权人|

        :return: The certifier_role of this EnterprisePersonNew.
        :rtype: str
        """
        return self._certifier_role

    @certifier_role.setter
    def certifier_role(self, certifier_role):
        """Sets the certifier_role of this EnterprisePersonNew.

        |参数名称：认证人角色| |参数的约束及描述：该参数非必填，legalPerson ：法人代表 authorizedPerson：授权人|

        :param certifier_role: The certifier_role of this EnterprisePersonNew.
        :type: str
        """
        self._certifier_role = certifier_role

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
        if not isinstance(other, EnterprisePersonNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
