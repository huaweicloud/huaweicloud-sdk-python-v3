# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEvaluationStateByAssignmentIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_assignment_id': 'str',
        'state': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'policy_assignment_id': 'policy_assignment_id',
        'state': 'state',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'error_message': 'error_message'
    }

    def __init__(self, policy_assignment_id=None, state=None, start_time=None, end_time=None, error_message=None):
        r"""ShowEvaluationStateByAssignmentIdResponse

        The model defined in huaweicloud sdk

        :param policy_assignment_id: 规则ID
        :type policy_assignment_id: str
        :param state: 评估任务执行状态
        :type state: str
        :param start_time: 评估任务开始时间
        :type start_time: str
        :param end_time: 评估任务结束时间
        :type end_time: str
        :param error_message: 评估任务失败信息
        :type error_message: str
        """
        
        super(ShowEvaluationStateByAssignmentIdResponse, self).__init__()

        self._policy_assignment_id = None
        self._state = None
        self._start_time = None
        self._end_time = None
        self._error_message = None
        self.discriminator = None

        if policy_assignment_id is not None:
            self.policy_assignment_id = policy_assignment_id
        if state is not None:
            self.state = state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if error_message is not None:
            self.error_message = error_message

    @property
    def policy_assignment_id(self):
        r"""Gets the policy_assignment_id of this ShowEvaluationStateByAssignmentIdResponse.

        规则ID

        :return: The policy_assignment_id of this ShowEvaluationStateByAssignmentIdResponse.
        :rtype: str
        """
        return self._policy_assignment_id

    @policy_assignment_id.setter
    def policy_assignment_id(self, policy_assignment_id):
        r"""Sets the policy_assignment_id of this ShowEvaluationStateByAssignmentIdResponse.

        规则ID

        :param policy_assignment_id: The policy_assignment_id of this ShowEvaluationStateByAssignmentIdResponse.
        :type policy_assignment_id: str
        """
        self._policy_assignment_id = policy_assignment_id

    @property
    def state(self):
        r"""Gets the state of this ShowEvaluationStateByAssignmentIdResponse.

        评估任务执行状态

        :return: The state of this ShowEvaluationStateByAssignmentIdResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowEvaluationStateByAssignmentIdResponse.

        评估任务执行状态

        :param state: The state of this ShowEvaluationStateByAssignmentIdResponse.
        :type state: str
        """
        self._state = state

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowEvaluationStateByAssignmentIdResponse.

        评估任务开始时间

        :return: The start_time of this ShowEvaluationStateByAssignmentIdResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowEvaluationStateByAssignmentIdResponse.

        评估任务开始时间

        :param start_time: The start_time of this ShowEvaluationStateByAssignmentIdResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowEvaluationStateByAssignmentIdResponse.

        评估任务结束时间

        :return: The end_time of this ShowEvaluationStateByAssignmentIdResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowEvaluationStateByAssignmentIdResponse.

        评估任务结束时间

        :param end_time: The end_time of this ShowEvaluationStateByAssignmentIdResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_message(self):
        r"""Gets the error_message of this ShowEvaluationStateByAssignmentIdResponse.

        评估任务失败信息

        :return: The error_message of this ShowEvaluationStateByAssignmentIdResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ShowEvaluationStateByAssignmentIdResponse.

        评估任务失败信息

        :param error_message: The error_message of this ShowEvaluationStateByAssignmentIdResponse.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, ShowEvaluationStateByAssignmentIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
