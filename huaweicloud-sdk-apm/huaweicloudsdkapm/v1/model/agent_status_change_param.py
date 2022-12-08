# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentStatusChangeParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_list': 'list[int]',
        'target_status': 'int',
        'region': 'str',
        'env_id': 'int'
    }

    attribute_map = {
        'instance_list': 'instance_list',
        'target_status': 'target_status',
        'region': 'region',
        'env_id': 'env_id'
    }

    def __init__(self, instance_list=None, target_status=None, region=None, env_id=None):
        """AgentStatusChangeParam

        The model defined in huaweicloud sdk

        :param instance_list: 探针实例id列表。
        :type instance_list: list[int]
        :param target_status: 期望探针改变后的状态，0或1，0表示启用，1表示停用。
        :type target_status: int
        :param region: 探针所在的区域。
        :type region: str
        :param env_id: 探针所属环境的id。
        :type env_id: int
        """
        
        

        self._instance_list = None
        self._target_status = None
        self._region = None
        self._env_id = None
        self.discriminator = None

        self.instance_list = instance_list
        self.target_status = target_status
        self.region = region
        if env_id is not None:
            self.env_id = env_id

    @property
    def instance_list(self):
        """Gets the instance_list of this AgentStatusChangeParam.

        探针实例id列表。

        :return: The instance_list of this AgentStatusChangeParam.
        :rtype: list[int]
        """
        return self._instance_list

    @instance_list.setter
    def instance_list(self, instance_list):
        """Sets the instance_list of this AgentStatusChangeParam.

        探针实例id列表。

        :param instance_list: The instance_list of this AgentStatusChangeParam.
        :type instance_list: list[int]
        """
        self._instance_list = instance_list

    @property
    def target_status(self):
        """Gets the target_status of this AgentStatusChangeParam.

        期望探针改变后的状态，0或1，0表示启用，1表示停用。

        :return: The target_status of this AgentStatusChangeParam.
        :rtype: int
        """
        return self._target_status

    @target_status.setter
    def target_status(self, target_status):
        """Sets the target_status of this AgentStatusChangeParam.

        期望探针改变后的状态，0或1，0表示启用，1表示停用。

        :param target_status: The target_status of this AgentStatusChangeParam.
        :type target_status: int
        """
        self._target_status = target_status

    @property
    def region(self):
        """Gets the region of this AgentStatusChangeParam.

        探针所在的区域。

        :return: The region of this AgentStatusChangeParam.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AgentStatusChangeParam.

        探针所在的区域。

        :param region: The region of this AgentStatusChangeParam.
        :type region: str
        """
        self._region = region

    @property
    def env_id(self):
        """Gets the env_id of this AgentStatusChangeParam.

        探针所属环境的id。

        :return: The env_id of this AgentStatusChangeParam.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this AgentStatusChangeParam.

        探针所属环境的id。

        :param env_id: The env_id of this AgentStatusChangeParam.
        :type env_id: int
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
        if not isinstance(other, AgentStatusChangeParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
