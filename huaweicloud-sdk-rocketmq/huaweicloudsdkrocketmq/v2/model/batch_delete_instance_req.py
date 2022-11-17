# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteInstanceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instances': 'list[str]',
        'action': 'str',
        'all_failure': 'str'
    }

    attribute_map = {
        'instances': 'instances',
        'action': 'action',
        'all_failure': 'all_failure'
    }

    def __init__(self, instances=None, action=None, all_failure=None):
        """BatchDeleteInstanceReq

        The model defined in huaweicloud sdk

        :param instances: 实例的ID列表。
        :type instances: list[str]
        :param action: 对实例的操作：delete
        :type action: str
        :param all_failure: 参数值为reliability,表示删除租户所有创建失败的RocketMQ实例。
        :type all_failure: str
        """
        
        

        self._instances = None
        self._action = None
        self._all_failure = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        self.action = action
        if all_failure is not None:
            self.all_failure = all_failure

    @property
    def instances(self):
        """Gets the instances of this BatchDeleteInstanceReq.

        实例的ID列表。

        :return: The instances of this BatchDeleteInstanceReq.
        :rtype: list[str]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this BatchDeleteInstanceReq.

        实例的ID列表。

        :param instances: The instances of this BatchDeleteInstanceReq.
        :type instances: list[str]
        """
        self._instances = instances

    @property
    def action(self):
        """Gets the action of this BatchDeleteInstanceReq.

        对实例的操作：delete

        :return: The action of this BatchDeleteInstanceReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BatchDeleteInstanceReq.

        对实例的操作：delete

        :param action: The action of this BatchDeleteInstanceReq.
        :type action: str
        """
        self._action = action

    @property
    def all_failure(self):
        """Gets the all_failure of this BatchDeleteInstanceReq.

        参数值为reliability,表示删除租户所有创建失败的RocketMQ实例。

        :return: The all_failure of this BatchDeleteInstanceReq.
        :rtype: str
        """
        return self._all_failure

    @all_failure.setter
    def all_failure(self, all_failure):
        """Sets the all_failure of this BatchDeleteInstanceReq.

        参数值为reliability,表示删除租户所有创建失败的RocketMQ实例。

        :param all_failure: The all_failure of this BatchDeleteInstanceReq.
        :type all_failure: str
        """
        self._all_failure = all_failure

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
        if not isinstance(other, BatchDeleteInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
