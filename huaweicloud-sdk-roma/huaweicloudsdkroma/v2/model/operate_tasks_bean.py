# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateTasksBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_id': 'str',
        'list': 'list[TaskBean]'
    }

    attribute_map = {
        'action_id': 'action_id',
        'list': 'list'
    }

    def __init__(self, action_id=None, list=None):
        r"""OperateTasksBean

        The model defined in huaweicloud sdk

        :param action_id: 操作类型 - start (启动) - stop (停止)
        :type action_id: str
        :param list: 需要启动或者停止的任务ID列表
        :type list: list[:class:`huaweicloudsdkroma.v2.TaskBean`]
        """
        
        

        self._action_id = None
        self._list = None
        self.discriminator = None

        self.action_id = action_id
        if list is not None:
            self.list = list

    @property
    def action_id(self):
        r"""Gets the action_id of this OperateTasksBean.

        操作类型 - start (启动) - stop (停止)

        :return: The action_id of this OperateTasksBean.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this OperateTasksBean.

        操作类型 - start (启动) - stop (停止)

        :param action_id: The action_id of this OperateTasksBean.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def list(self):
        r"""Gets the list of this OperateTasksBean.

        需要启动或者停止的任务ID列表

        :return: The list of this OperateTasksBean.
        :rtype: list[:class:`huaweicloudsdkroma.v2.TaskBean`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this OperateTasksBean.

        需要启动或者停止的任务ID列表

        :param list: The list of this OperateTasksBean.
        :type list: list[:class:`huaweicloudsdkroma.v2.TaskBean`]
        """
        self._list = list

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
        if not isinstance(other, OperateTasksBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
