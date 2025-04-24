# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTaurusDbNodeProcessesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'processes_killed': 'list[int]',
        'processes_not_found': 'list[int]'
    }

    attribute_map = {
        'processes_killed': 'processes_killed',
        'processes_not_found': 'processes_not_found'
    }

    def __init__(self, processes_killed=None, processes_not_found=None):
        r"""DeleteTaurusDbNodeProcessesResponse

        The model defined in huaweicloud sdk

        :param processes_killed: **参数解释**：  已终止的用户会话线程ID列表。
        :type processes_killed: list[int]
        :param processes_not_found: **参数解释**：  不存在的用户会话线程ID列表。
        :type processes_not_found: list[int]
        """
        
        super(DeleteTaurusDbNodeProcessesResponse, self).__init__()

        self._processes_killed = None
        self._processes_not_found = None
        self.discriminator = None

        if processes_killed is not None:
            self.processes_killed = processes_killed
        if processes_not_found is not None:
            self.processes_not_found = processes_not_found

    @property
    def processes_killed(self):
        r"""Gets the processes_killed of this DeleteTaurusDbNodeProcessesResponse.

        **参数解释**：  已终止的用户会话线程ID列表。

        :return: The processes_killed of this DeleteTaurusDbNodeProcessesResponse.
        :rtype: list[int]
        """
        return self._processes_killed

    @processes_killed.setter
    def processes_killed(self, processes_killed):
        r"""Sets the processes_killed of this DeleteTaurusDbNodeProcessesResponse.

        **参数解释**：  已终止的用户会话线程ID列表。

        :param processes_killed: The processes_killed of this DeleteTaurusDbNodeProcessesResponse.
        :type processes_killed: list[int]
        """
        self._processes_killed = processes_killed

    @property
    def processes_not_found(self):
        r"""Gets the processes_not_found of this DeleteTaurusDbNodeProcessesResponse.

        **参数解释**：  不存在的用户会话线程ID列表。

        :return: The processes_not_found of this DeleteTaurusDbNodeProcessesResponse.
        :rtype: list[int]
        """
        return self._processes_not_found

    @processes_not_found.setter
    def processes_not_found(self, processes_not_found):
        r"""Sets the processes_not_found of this DeleteTaurusDbNodeProcessesResponse.

        **参数解释**：  不存在的用户会话线程ID列表。

        :param processes_not_found: The processes_not_found of this DeleteTaurusDbNodeProcessesResponse.
        :type processes_not_found: list[int]
        """
        self._processes_not_found = processes_not_found

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
        if not isinstance(other, DeleteTaurusDbNodeProcessesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
