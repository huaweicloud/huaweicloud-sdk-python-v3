# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeInstanceStatusBody:

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
        'action': 'str'
    }

    attribute_map = {
        'instances': 'instances',
        'action': 'action'
    }

    def __init__(self, instances=None, action=None):
        r"""ChangeInstanceStatusBody

        The model defined in huaweicloud sdk

        :param instances: 实例的ID列表。
        :type instances: list[str]
        :param action: 对实例的操作：  restart: 强制重启  soft_restart: 软重启，只重启进程  flush: 清空数据 &gt; 当前版本，只有Redis 4.0和Redis 5.0实例支持清空数据功能，即flush操作。 
        :type action: str
        """
        
        

        self._instances = None
        self._action = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        if action is not None:
            self.action = action

    @property
    def instances(self):
        r"""Gets the instances of this ChangeInstanceStatusBody.

        实例的ID列表。

        :return: The instances of this ChangeInstanceStatusBody.
        :rtype: list[str]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ChangeInstanceStatusBody.

        实例的ID列表。

        :param instances: The instances of this ChangeInstanceStatusBody.
        :type instances: list[str]
        """
        self._instances = instances

    @property
    def action(self):
        r"""Gets the action of this ChangeInstanceStatusBody.

        对实例的操作：  restart: 强制重启  soft_restart: 软重启，只重启进程  flush: 清空数据 > 当前版本，只有Redis 4.0和Redis 5.0实例支持清空数据功能，即flush操作。 

        :return: The action of this ChangeInstanceStatusBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ChangeInstanceStatusBody.

        对实例的操作：  restart: 强制重启  soft_restart: 软重启，只重启进程  flush: 清空数据 > 当前版本，只有Redis 4.0和Redis 5.0实例支持清空数据功能，即flush操作。 

        :param action: The action of this ChangeInstanceStatusBody.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, ChangeInstanceStatusBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
