# coding: utf-8

import pprint
import re

import six





class ModVmrDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'vmr_name': 'str',
        'gust_pwd': 'str',
        'chair_pwd': 'str',
        'allow_gust_first': 'bool',
        'gust_first_notice': 'bool'
    }

    attribute_map = {
        'vmr_name': 'vmrName',
        'gust_pwd': 'gustPwd',
        'chair_pwd': 'chairPwd',
        'allow_gust_first': 'allowGustFirst',
        'gust_first_notice': 'gustFirstNotice'
    }

    def __init__(self, vmr_name=None, gust_pwd=None, chair_pwd=None, allow_gust_first=None, gust_first_notice=None):
        """ModVmrDTO - a model defined in huaweicloud sdk"""
        
        

        self._vmr_name = None
        self._gust_pwd = None
        self._chair_pwd = None
        self._allow_gust_first = None
        self._gust_first_notice = None
        self.discriminator = None

        if vmr_name is not None:
            self.vmr_name = vmr_name
        if gust_pwd is not None:
            self.gust_pwd = gust_pwd
        if chair_pwd is not None:
            self.chair_pwd = chair_pwd
        if allow_gust_first is not None:
            self.allow_gust_first = allow_gust_first
        if gust_first_notice is not None:
            self.gust_first_notice = gust_first_notice

    @property
    def vmr_name(self):
        """Gets the vmr_name of this ModVmrDTO.

        云会议室名称 maxLength：128 minLength：1 

        :return: The vmr_name of this ModVmrDTO.
        :rtype: str
        """
        return self._vmr_name

    @vmr_name.setter
    def vmr_name(self, vmr_name):
        """Sets the vmr_name of this ModVmrDTO.

        云会议室名称 maxLength：128 minLength：1 

        :param vmr_name: The vmr_name of this ModVmrDTO.
        :type: str
        """
        self._vmr_name = vmr_name

    @property
    def gust_pwd(self):
        """Gets the gust_pwd of this ModVmrDTO.

        来宾密码，“”代表不设置来宾密码 4~16位的数字 

        :return: The gust_pwd of this ModVmrDTO.
        :rtype: str
        """
        return self._gust_pwd

    @gust_pwd.setter
    def gust_pwd(self, gust_pwd):
        """Sets the gust_pwd of this ModVmrDTO.

        来宾密码，“”代表不设置来宾密码 4~16位的数字 

        :param gust_pwd: The gust_pwd of this ModVmrDTO.
        :type: str
        """
        self._gust_pwd = gust_pwd

    @property
    def chair_pwd(self):
        """Gets the chair_pwd of this ModVmrDTO.

        主席密码 4~16位的数字 

        :return: The chair_pwd of this ModVmrDTO.
        :rtype: str
        """
        return self._chair_pwd

    @chair_pwd.setter
    def chair_pwd(self, chair_pwd):
        """Sets the chair_pwd of this ModVmrDTO.

        主席密码 4~16位的数字 

        :param chair_pwd: The chair_pwd of this ModVmrDTO.
        :type: str
        """
        self._chair_pwd = chair_pwd

    @property
    def allow_gust_first(self):
        """Gets the allow_gust_first of this ModVmrDTO.

        是否允许来宾先入会。

        :return: The allow_gust_first of this ModVmrDTO.
        :rtype: bool
        """
        return self._allow_gust_first

    @allow_gust_first.setter
    def allow_gust_first(self, allow_gust_first):
        """Sets the allow_gust_first of this ModVmrDTO.

        是否允许来宾先入会。

        :param allow_gust_first: The allow_gust_first of this ModVmrDTO.
        :type: bool
        """
        self._allow_gust_first = allow_gust_first

    @property
    def gust_first_notice(self):
        """Gets the gust_first_notice of this ModVmrDTO.

        云会议室被使用后是否通知会议室所有者。

        :return: The gust_first_notice of this ModVmrDTO.
        :rtype: bool
        """
        return self._gust_first_notice

    @gust_first_notice.setter
    def gust_first_notice(self, gust_first_notice):
        """Sets the gust_first_notice of this ModVmrDTO.

        云会议室被使用后是否通知会议室所有者。

        :param gust_first_notice: The gust_first_notice of this ModVmrDTO.
        :type: bool
        """
        self._gust_first_notice = gust_first_notice

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
        if not isinstance(other, ModVmrDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
