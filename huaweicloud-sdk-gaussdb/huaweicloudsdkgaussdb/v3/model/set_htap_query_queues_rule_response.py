# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetHtapQueryQueuesRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'msg': 'str'
    }

    attribute_map = {
        'status': 'status',
        'msg': 'msg'
    }

    def __init__(self, status=None, msg=None):
        r"""SetHtapQueryQueuesRuleResponse

        The model defined in huaweicloud sdk

        :param status: **参数解释**：  响应返回结果。   **取值范围**：  - success：成功。 - failed：失败。
        :type status: str
        :param msg: **参数解释**：  响应错误信息。  **取值范围**：  不涉及。
        :type msg: str
        """
        
        super(SetHtapQueryQueuesRuleResponse, self).__init__()

        self._status = None
        self._msg = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if msg is not None:
            self.msg = msg

    @property
    def status(self):
        r"""Gets the status of this SetHtapQueryQueuesRuleResponse.

        **参数解释**：  响应返回结果。   **取值范围**：  - success：成功。 - failed：失败。

        :return: The status of this SetHtapQueryQueuesRuleResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SetHtapQueryQueuesRuleResponse.

        **参数解释**：  响应返回结果。   **取值范围**：  - success：成功。 - failed：失败。

        :param status: The status of this SetHtapQueryQueuesRuleResponse.
        :type status: str
        """
        self._status = status

    @property
    def msg(self):
        r"""Gets the msg of this SetHtapQueryQueuesRuleResponse.

        **参数解释**：  响应错误信息。  **取值范围**：  不涉及。

        :return: The msg of this SetHtapQueryQueuesRuleResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this SetHtapQueryQueuesRuleResponse.

        **参数解释**：  响应错误信息。  **取值范围**：  不涉及。

        :param msg: The msg of this SetHtapQueryQueuesRuleResponse.
        :type msg: str
        """
        self._msg = msg

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
        if not isinstance(other, SetHtapQueryQueuesRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
