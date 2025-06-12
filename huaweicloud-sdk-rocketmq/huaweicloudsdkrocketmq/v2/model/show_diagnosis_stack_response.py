# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDiagnosisStackResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'thread_name': 'str',
        'stack': 'str'
    }

    attribute_map = {
        'thread_name': 'thread_name',
        'stack': 'stack'
    }

    def __init__(self, thread_name=None, stack=None):
        r"""ShowDiagnosisStackResponse

        The model defined in huaweicloud sdk

        :param thread_name: **参数解释**： 线程名。 **取值范围**： 不涉及。
        :type thread_name: str
        :param stack: **参数解释**： 堆信息。 **取值范围**： 不涉及。
        :type stack: str
        """
        
        super(ShowDiagnosisStackResponse, self).__init__()

        self._thread_name = None
        self._stack = None
        self.discriminator = None

        if thread_name is not None:
            self.thread_name = thread_name
        if stack is not None:
            self.stack = stack

    @property
    def thread_name(self):
        r"""Gets the thread_name of this ShowDiagnosisStackResponse.

        **参数解释**： 线程名。 **取值范围**： 不涉及。

        :return: The thread_name of this ShowDiagnosisStackResponse.
        :rtype: str
        """
        return self._thread_name

    @thread_name.setter
    def thread_name(self, thread_name):
        r"""Sets the thread_name of this ShowDiagnosisStackResponse.

        **参数解释**： 线程名。 **取值范围**： 不涉及。

        :param thread_name: The thread_name of this ShowDiagnosisStackResponse.
        :type thread_name: str
        """
        self._thread_name = thread_name

    @property
    def stack(self):
        r"""Gets the stack of this ShowDiagnosisStackResponse.

        **参数解释**： 堆信息。 **取值范围**： 不涉及。

        :return: The stack of this ShowDiagnosisStackResponse.
        :rtype: str
        """
        return self._stack

    @stack.setter
    def stack(self, stack):
        r"""Sets the stack of this ShowDiagnosisStackResponse.

        **参数解释**： 堆信息。 **取值范围**： 不涉及。

        :param stack: The stack of this ShowDiagnosisStackResponse.
        :type stack: str
        """
        self._stack = stack

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
        if not isinstance(other, ShowDiagnosisStackResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
