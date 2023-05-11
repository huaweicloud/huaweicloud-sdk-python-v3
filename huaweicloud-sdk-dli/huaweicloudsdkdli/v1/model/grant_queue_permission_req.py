# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GrantQueuePermissionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_name': 'str',
        'user_name': 'str',
        'action': 'str',
        'privileges': 'list[str]'
    }

    attribute_map = {
        'queue_name': 'queue_name',
        'user_name': 'user_name',
        'action': 'action',
        'privileges': 'privileges'
    }

    def __init__(self, queue_name=None, user_name=None, action=None, privileges=None):
        """GrantQueuePermissionReq

        The model defined in huaweicloud sdk

        :param queue_name: 队列名称。
        :type queue_name: str
        :param user_name: 被赋权用户名称。给该用户赋使用队列的权限，回收其使用权限，或者更新其使用权限。
        :type user_name: str
        :param action: 指定赋权或回收。值为：grant，revoke或update。当用户同时拥有grant和revoke权限的时候才有权限使用update操作。 grant：赋权。 revoke：回收权限。 update：清空原来的所有权限，赋予本次提供的权限数组中的权限。
        :type action: str
        :param privileges: 待赋权、回收或更新的权限列表。可操作的权限可以是以下三种权限中的一种或多种。 SUBMIT_JOB：提交作业 CANCEL_JOB ：取消作业 DROP_QUEUE ：删除队列 说明： 若需更新的权限列表为空，则表示回收用户在该队列的所有权限。
        :type privileges: list[str]
        """
        
        

        self._queue_name = None
        self._user_name = None
        self._action = None
        self._privileges = None
        self.discriminator = None

        self.queue_name = queue_name
        self.user_name = user_name
        self.action = action
        self.privileges = privileges

    @property
    def queue_name(self):
        """Gets the queue_name of this GrantQueuePermissionReq.

        队列名称。

        :return: The queue_name of this GrantQueuePermissionReq.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this GrantQueuePermissionReq.

        队列名称。

        :param queue_name: The queue_name of this GrantQueuePermissionReq.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def user_name(self):
        """Gets the user_name of this GrantQueuePermissionReq.

        被赋权用户名称。给该用户赋使用队列的权限，回收其使用权限，或者更新其使用权限。

        :return: The user_name of this GrantQueuePermissionReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this GrantQueuePermissionReq.

        被赋权用户名称。给该用户赋使用队列的权限，回收其使用权限，或者更新其使用权限。

        :param user_name: The user_name of this GrantQueuePermissionReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def action(self):
        """Gets the action of this GrantQueuePermissionReq.

        指定赋权或回收。值为：grant，revoke或update。当用户同时拥有grant和revoke权限的时候才有权限使用update操作。 grant：赋权。 revoke：回收权限。 update：清空原来的所有权限，赋予本次提供的权限数组中的权限。

        :return: The action of this GrantQueuePermissionReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this GrantQueuePermissionReq.

        指定赋权或回收。值为：grant，revoke或update。当用户同时拥有grant和revoke权限的时候才有权限使用update操作。 grant：赋权。 revoke：回收权限。 update：清空原来的所有权限，赋予本次提供的权限数组中的权限。

        :param action: The action of this GrantQueuePermissionReq.
        :type action: str
        """
        self._action = action

    @property
    def privileges(self):
        """Gets the privileges of this GrantQueuePermissionReq.

        待赋权、回收或更新的权限列表。可操作的权限可以是以下三种权限中的一种或多种。 SUBMIT_JOB：提交作业 CANCEL_JOB ：取消作业 DROP_QUEUE ：删除队列 说明： 若需更新的权限列表为空，则表示回收用户在该队列的所有权限。

        :return: The privileges of this GrantQueuePermissionReq.
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this GrantQueuePermissionReq.

        待赋权、回收或更新的权限列表。可操作的权限可以是以下三种权限中的一种或多种。 SUBMIT_JOB：提交作业 CANCEL_JOB ：取消作业 DROP_QUEUE ：删除队列 说明： 若需更新的权限列表为空，则表示回收用户在该队列的所有权限。

        :param privileges: The privileges of this GrantQueuePermissionReq.
        :type privileges: list[str]
        """
        self._privileges = privileges

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
        if not isinstance(other, GrantQueuePermissionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
