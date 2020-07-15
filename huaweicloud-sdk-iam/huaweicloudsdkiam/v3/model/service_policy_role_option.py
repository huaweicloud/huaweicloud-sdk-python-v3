# coding: utf-8

import pprint
import re

import six





class ServicePolicyRoleOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'type': 'str',
        'description': 'str',
        'description_cn': 'str',
        'policy': 'ServicePolicy'
    }

    attribute_map = {
        'display_name': 'display_name',
        'type': 'type',
        'description': 'description',
        'description_cn': 'description_cn',
        'policy': 'policy'
    }

    def __init__(self, display_name=None, type=None, description=None, description_cn=None, policy=None):
        """ServicePolicyRoleOption - a model defined in huaweicloud sdk"""
        
        

        self._display_name = None
        self._type = None
        self._description = None
        self._description_cn = None
        self._policy = None
        self.discriminator = None

        self.display_name = display_name
        self.type = type
        self.description = description
        if description_cn is not None:
            self.description_cn = description_cn
        self.policy = policy

    @property
    def display_name(self):
        """Gets the display_name of this ServicePolicyRoleOption.

        自定义策略展示名。

        :return: The display_name of this ServicePolicyRoleOption.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ServicePolicyRoleOption.

        自定义策略展示名。

        :param display_name: The display_name of this ServicePolicyRoleOption.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """Gets the type of this ServicePolicyRoleOption.

        自定义策略的显示模式。   > - AX表示在domain层显示。   > - XA表示在project层显示。   > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :return: The type of this ServicePolicyRoleOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServicePolicyRoleOption.

        自定义策略的显示模式。   > - AX表示在domain层显示。   > - XA表示在project层显示。   > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :param type: The type of this ServicePolicyRoleOption.
        :type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this ServicePolicyRoleOption.

        自定义策略的描述信息。

        :return: The description of this ServicePolicyRoleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServicePolicyRoleOption.

        自定义策略的描述信息。

        :param description: The description of this ServicePolicyRoleOption.
        :type: str
        """
        self._description = description

    @property
    def description_cn(self):
        """Gets the description_cn of this ServicePolicyRoleOption.

        自定义策略的中文描述信息。

        :return: The description_cn of this ServicePolicyRoleOption.
        :rtype: str
        """
        return self._description_cn

    @description_cn.setter
    def description_cn(self, description_cn):
        """Sets the description_cn of this ServicePolicyRoleOption.

        自定义策略的中文描述信息。

        :param description_cn: The description_cn of this ServicePolicyRoleOption.
        :type: str
        """
        self._description_cn = description_cn

    @property
    def policy(self):
        """Gets the policy of this ServicePolicyRoleOption.


        :return: The policy of this ServicePolicyRoleOption.
        :rtype: ServicePolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this ServicePolicyRoleOption.


        :param policy: The policy of this ServicePolicyRoleOption.
        :type: ServicePolicy
        """
        self._policy = policy

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
        if not isinstance(other, ServicePolicyRoleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
