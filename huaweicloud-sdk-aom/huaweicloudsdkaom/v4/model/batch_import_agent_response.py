# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchImportAgentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'bool'
    }

    attribute_map = {
        'state': 'state'
    }

    def __init__(self, state=None):
        r"""BatchImportAgentResponse

        The model defined in huaweicloud sdk

        :param state: 执行状态： - true：成功下发任务。 - false：失败下发任务。
        :type state: bool
        """
        
        super(BatchImportAgentResponse, self).__init__()

        self._state = None
        self.discriminator = None

        if state is not None:
            self.state = state

    @property
    def state(self):
        r"""Gets the state of this BatchImportAgentResponse.

        执行状态： - true：成功下发任务。 - false：失败下发任务。

        :return: The state of this BatchImportAgentResponse.
        :rtype: bool
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this BatchImportAgentResponse.

        执行状态： - true：成功下发任务。 - false：失败下发任务。

        :param state: The state of this BatchImportAgentResponse.
        :type state: bool
        """
        self._state = state

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
        if not isinstance(other, BatchImportAgentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
