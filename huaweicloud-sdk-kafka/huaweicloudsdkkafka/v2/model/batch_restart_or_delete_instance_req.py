# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRestartOrDeleteInstanceReq:

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
        'all_failure': 'str',
        'force_delete': 'bool'
    }

    attribute_map = {
        'instances': 'instances',
        'action': 'action',
        'all_failure': 'all_failure',
        'force_delete': 'force_delete'
    }

    def __init__(self, instances=None, action=None, all_failure=None, force_delete=None):
        r"""BatchRestartOrDeleteInstanceReq

        The model defined in huaweicloud sdk

        :param instances: 实例的ID列表。
        :type instances: list[str]
        :param action: 对实例的操作：restart、delete
        :type action: str
        :param all_failure: 参数值为kafka，表示删除租户所有创建失败的Kafka实例。
        :type all_failure: str
        :param force_delete: 是否强删除，强删除实例不进入收回站。
        :type force_delete: bool
        """
        
        

        self._instances = None
        self._action = None
        self._all_failure = None
        self._force_delete = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        self.action = action
        if all_failure is not None:
            self.all_failure = all_failure
        if force_delete is not None:
            self.force_delete = force_delete

    @property
    def instances(self):
        r"""Gets the instances of this BatchRestartOrDeleteInstanceReq.

        实例的ID列表。

        :return: The instances of this BatchRestartOrDeleteInstanceReq.
        :rtype: list[str]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this BatchRestartOrDeleteInstanceReq.

        实例的ID列表。

        :param instances: The instances of this BatchRestartOrDeleteInstanceReq.
        :type instances: list[str]
        """
        self._instances = instances

    @property
    def action(self):
        r"""Gets the action of this BatchRestartOrDeleteInstanceReq.

        对实例的操作：restart、delete

        :return: The action of this BatchRestartOrDeleteInstanceReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchRestartOrDeleteInstanceReq.

        对实例的操作：restart、delete

        :param action: The action of this BatchRestartOrDeleteInstanceReq.
        :type action: str
        """
        self._action = action

    @property
    def all_failure(self):
        r"""Gets the all_failure of this BatchRestartOrDeleteInstanceReq.

        参数值为kafka，表示删除租户所有创建失败的Kafka实例。

        :return: The all_failure of this BatchRestartOrDeleteInstanceReq.
        :rtype: str
        """
        return self._all_failure

    @all_failure.setter
    def all_failure(self, all_failure):
        r"""Sets the all_failure of this BatchRestartOrDeleteInstanceReq.

        参数值为kafka，表示删除租户所有创建失败的Kafka实例。

        :param all_failure: The all_failure of this BatchRestartOrDeleteInstanceReq.
        :type all_failure: str
        """
        self._all_failure = all_failure

    @property
    def force_delete(self):
        r"""Gets the force_delete of this BatchRestartOrDeleteInstanceReq.

        是否强删除，强删除实例不进入收回站。

        :return: The force_delete of this BatchRestartOrDeleteInstanceReq.
        :rtype: bool
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        r"""Sets the force_delete of this BatchRestartOrDeleteInstanceReq.

        是否强删除，强删除实例不进入收回站。

        :param force_delete: The force_delete of this BatchRestartOrDeleteInstanceReq.
        :type force_delete: bool
        """
        self._force_delete = force_delete

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
        if not isinstance(other, BatchRestartOrDeleteInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
