# coding: utf-8

import pprint
import re

import six





class ApplyConfigurationResponseApplyResults:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'restart_required': 'bool',
        'success': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'restart_required': 'restart_required',
        'success': 'success'
    }

    def __init__(self, instance_id=None, instance_name=None, restart_required=None, success=None):
        """ApplyConfigurationResponseApplyResults - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._instance_name = None
        self._restart_required = None
        self._success = None
        self.discriminator = None

        self.instance_id = instance_id
        self.instance_name = instance_name
        self.restart_required = restart_required
        self.success = success

    @property
    def instance_id(self):
        """Gets the instance_id of this ApplyConfigurationResponseApplyResults.

        实例ID。

        :return: The instance_id of this ApplyConfigurationResponseApplyResults.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ApplyConfigurationResponseApplyResults.

        实例ID。

        :param instance_id: The instance_id of this ApplyConfigurationResponseApplyResults.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this ApplyConfigurationResponseApplyResults.

        实例名称。

        :return: The instance_name of this ApplyConfigurationResponseApplyResults.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ApplyConfigurationResponseApplyResults.

        实例名称。

        :param instance_name: The instance_name of this ApplyConfigurationResponseApplyResults.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def restart_required(self):
        """Gets the restart_required of this ApplyConfigurationResponseApplyResults.

        实例是否需要重启。  - “true”需要重启。 - “false”不需要重启。

        :return: The restart_required of this ApplyConfigurationResponseApplyResults.
        :rtype: bool
        """
        return self._restart_required

    @restart_required.setter
    def restart_required(self, restart_required):
        """Sets the restart_required of this ApplyConfigurationResponseApplyResults.

        实例是否需要重启。  - “true”需要重启。 - “false”不需要重启。

        :param restart_required: The restart_required of this ApplyConfigurationResponseApplyResults.
        :type: bool
        """
        self._restart_required = restart_required

    @property
    def success(self):
        """Gets the success of this ApplyConfigurationResponseApplyResults.

        参数模板是否应用成功。  - “true”表示参数模板应用成功。 - “false”表示参数模板应用失败。

        :return: The success of this ApplyConfigurationResponseApplyResults.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ApplyConfigurationResponseApplyResults.

        参数模板是否应用成功。  - “true”表示参数模板应用成功。 - “false”表示参数模板应用失败。

        :param success: The success of this ApplyConfigurationResponseApplyResults.
        :type: bool
        """
        self._success = success

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
        if not isinstance(other, ApplyConfigurationResponseApplyResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
