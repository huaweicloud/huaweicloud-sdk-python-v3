# coding: utf-8

import pprint
import re

import six





class CreateScalingConfigRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_configuration_name': 'str',
        'instance_config': 'InstanceConfig'
    }

    attribute_map = {
        'scaling_configuration_name': 'scaling_configuration_name',
        'instance_config': 'instance_config'
    }

    def __init__(self, scaling_configuration_name=None, instance_config=None):
        """CreateScalingConfigRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._scaling_configuration_name = None
        self._instance_config = None
        self.discriminator = None

        self.scaling_configuration_name = scaling_configuration_name
        self.instance_config = instance_config

    @property
    def scaling_configuration_name(self):
        """Gets the scaling_configuration_name of this CreateScalingConfigRequestBody.

        伸缩配置名称(1-64个字符)，只能包含中文、字母、数字、下划线或中划线。

        :return: The scaling_configuration_name of this CreateScalingConfigRequestBody.
        :rtype: str
        """
        return self._scaling_configuration_name

    @scaling_configuration_name.setter
    def scaling_configuration_name(self, scaling_configuration_name):
        """Sets the scaling_configuration_name of this CreateScalingConfigRequestBody.

        伸缩配置名称(1-64个字符)，只能包含中文、字母、数字、下划线或中划线。

        :param scaling_configuration_name: The scaling_configuration_name of this CreateScalingConfigRequestBody.
        :type: str
        """
        self._scaling_configuration_name = scaling_configuration_name

    @property
    def instance_config(self):
        """Gets the instance_config of this CreateScalingConfigRequestBody.


        :return: The instance_config of this CreateScalingConfigRequestBody.
        :rtype: InstanceConfig
        """
        return self._instance_config

    @instance_config.setter
    def instance_config(self, instance_config):
        """Sets the instance_config of this CreateScalingConfigRequestBody.


        :param instance_config: The instance_config of this CreateScalingConfigRequestBody.
        :type: InstanceConfig
        """
        self._instance_config = instance_config

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
        if not isinstance(other, CreateScalingConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
