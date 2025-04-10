# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchStartHostTasksRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hosts': 'list[str]',
        'action': 'str'
    }

    attribute_map = {
        'hosts': 'hosts',
        'action': 'action'
    }

    def __init__(self, hosts=None, action=None):
        r"""BatchStartHostTasksRequestBody

        The model defined in huaweicloud sdk

        :param hosts: 主机ID列表
        :type hosts: list[str]
        :param action: 对扫描任务的操作:   * start - 启动   * cancel - 取消 
        :type action: str
        """
        
        

        self._hosts = None
        self._action = None
        self.discriminator = None

        if hosts is not None:
            self.hosts = hosts
        if action is not None:
            self.action = action

    @property
    def hosts(self):
        r"""Gets the hosts of this BatchStartHostTasksRequestBody.

        主机ID列表

        :return: The hosts of this BatchStartHostTasksRequestBody.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this BatchStartHostTasksRequestBody.

        主机ID列表

        :param hosts: The hosts of this BatchStartHostTasksRequestBody.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def action(self):
        r"""Gets the action of this BatchStartHostTasksRequestBody.

        对扫描任务的操作:   * start - 启动   * cancel - 取消 

        :return: The action of this BatchStartHostTasksRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchStartHostTasksRequestBody.

        对扫描任务的操作:   * start - 启动   * cancel - 取消 

        :param action: The action of this BatchStartHostTasksRequestBody.
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
        if not isinstance(other, BatchStartHostTasksRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
