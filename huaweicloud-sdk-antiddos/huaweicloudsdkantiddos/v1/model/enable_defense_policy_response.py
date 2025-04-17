# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableDefensePolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'task_id': 'task_id'
    }

    def __init__(self, error_code=None, error_msg=None, task_id=None):
        r"""EnableDefensePolicyResponse

        The model defined in huaweicloud sdk

        :param error_code: 内部错误码
        :type error_code: str
        :param error_msg: 内部错误描述
        :type error_msg: str
        :param task_id: 任务ID，后续可根据该ID查询本任务状态。 本字段为后续的任务审计扩展，暂时不需要，先保留。
        :type task_id: str
        """
        
        super(EnableDefensePolicyResponse, self).__init__()

        self._error_code = None
        self._error_msg = None
        self._task_id = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if task_id is not None:
            self.task_id = task_id

    @property
    def error_code(self):
        r"""Gets the error_code of this EnableDefensePolicyResponse.

        内部错误码

        :return: The error_code of this EnableDefensePolicyResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this EnableDefensePolicyResponse.

        内部错误码

        :param error_code: The error_code of this EnableDefensePolicyResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this EnableDefensePolicyResponse.

        内部错误描述

        :return: The error_msg of this EnableDefensePolicyResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this EnableDefensePolicyResponse.

        内部错误描述

        :param error_msg: The error_msg of this EnableDefensePolicyResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def task_id(self):
        r"""Gets the task_id of this EnableDefensePolicyResponse.

        任务ID，后续可根据该ID查询本任务状态。 本字段为后续的任务审计扩展，暂时不需要，先保留。

        :return: The task_id of this EnableDefensePolicyResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this EnableDefensePolicyResponse.

        任务ID，后续可根据该ID查询本任务状态。 本字段为后续的任务审计扩展，暂时不需要，先保留。

        :param task_id: The task_id of this EnableDefensePolicyResponse.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, EnableDefensePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
