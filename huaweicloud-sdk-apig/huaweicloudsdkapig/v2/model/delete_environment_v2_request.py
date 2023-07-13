# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEnvironmentV2Request:

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
        'env_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'env_id': 'env_id'
    }

    def __init__(self, instance_id=None, env_id=None):
        """DeleteEnvironmentV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param env_id: 环境的ID
        :type env_id: str
        """
        
        

        self._instance_id = None
        self._env_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.env_id = env_id

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteEnvironmentV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this DeleteEnvironmentV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteEnvironmentV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this DeleteEnvironmentV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def env_id(self):
        """Gets the env_id of this DeleteEnvironmentV2Request.

        环境的ID

        :return: The env_id of this DeleteEnvironmentV2Request.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this DeleteEnvironmentV2Request.

        环境的ID

        :param env_id: The env_id of this DeleteEnvironmentV2Request.
        :type env_id: str
        """
        self._env_id = env_id

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteEnvironmentV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
