# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTaurusDbNodeProcessesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'processes': 'list[int]'
    }

    attribute_map = {
        'processes': 'processes'
    }

    def __init__(self, processes=None):
        r"""DeleteTaurusDbNodeProcessesRequestBody

        The model defined in huaweicloud sdk

        :param processes: **参数解释**：  待终止用户会话线程ID列表。  通过查询节点用户会话线程接口，或show processlist命令获取。
        :type processes: list[int]
        """
        
        

        self._processes = None
        self.discriminator = None

        self.processes = processes

    @property
    def processes(self):
        r"""Gets the processes of this DeleteTaurusDbNodeProcessesRequestBody.

        **参数解释**：  待终止用户会话线程ID列表。  通过查询节点用户会话线程接口，或show processlist命令获取。

        :return: The processes of this DeleteTaurusDbNodeProcessesRequestBody.
        :rtype: list[int]
        """
        return self._processes

    @processes.setter
    def processes(self, processes):
        r"""Sets the processes of this DeleteTaurusDbNodeProcessesRequestBody.

        **参数解释**：  待终止用户会话线程ID列表。  通过查询节点用户会话线程接口，或show processlist命令获取。

        :param processes: The processes of this DeleteTaurusDbNodeProcessesRequestBody.
        :type processes: list[int]
        """
        self._processes = processes

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
        if not isinstance(other, DeleteTaurusDbNodeProcessesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
