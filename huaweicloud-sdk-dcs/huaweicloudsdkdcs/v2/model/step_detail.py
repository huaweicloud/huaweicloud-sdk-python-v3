# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StepDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step_id': 'str',
        'step_name': 'str',
        'step_status': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'error_code': 'str',
        'sub_step_details': 'list[SubStepDetail]'
    }

    attribute_map = {
        'step_id': 'step_id',
        'step_name': 'step_name',
        'step_status': 'step_status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'error_code': 'error_code',
        'sub_step_details': 'sub_step_details'
    }

    def __init__(self, step_id=None, step_name=None, step_status=None, begin_time=None, end_time=None, error_code=None, sub_step_details=None):
        """StepDetail

        The model defined in huaweicloud sdk

        :param step_id: 任务id
        :type step_id: str
        :param step_name: 任务名
        :type step_name: str
        :param step_status: 任务状态
        :type step_status: str
        :param begin_time: 任务启动时间，格式为2020-06-17T07:38:42.503Z
        :type begin_time: str
        :param end_time: 任务结束时间，格式为2020-06-17T07:38:42.503Z
        :type end_time: str
        :param error_code: 错误码
        :type error_code: str
        :param sub_step_details: 子任务详情列表
        :type sub_step_details: list[:class:`huaweicloudsdkdcs.v2.SubStepDetail`]
        """
        
        

        self._step_id = None
        self._step_name = None
        self._step_status = None
        self._begin_time = None
        self._end_time = None
        self._error_code = None
        self._sub_step_details = None
        self.discriminator = None

        if step_id is not None:
            self.step_id = step_id
        if step_name is not None:
            self.step_name = step_name
        if step_status is not None:
            self.step_status = step_status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if error_code is not None:
            self.error_code = error_code
        if sub_step_details is not None:
            self.sub_step_details = sub_step_details

    @property
    def step_id(self):
        """Gets the step_id of this StepDetail.

        任务id

        :return: The step_id of this StepDetail.
        :rtype: str
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        """Sets the step_id of this StepDetail.

        任务id

        :param step_id: The step_id of this StepDetail.
        :type step_id: str
        """
        self._step_id = step_id

    @property
    def step_name(self):
        """Gets the step_name of this StepDetail.

        任务名

        :return: The step_name of this StepDetail.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """Sets the step_name of this StepDetail.

        任务名

        :param step_name: The step_name of this StepDetail.
        :type step_name: str
        """
        self._step_name = step_name

    @property
    def step_status(self):
        """Gets the step_status of this StepDetail.

        任务状态

        :return: The step_status of this StepDetail.
        :rtype: str
        """
        return self._step_status

    @step_status.setter
    def step_status(self, step_status):
        """Sets the step_status of this StepDetail.

        任务状态

        :param step_status: The step_status of this StepDetail.
        :type step_status: str
        """
        self._step_status = step_status

    @property
    def begin_time(self):
        """Gets the begin_time of this StepDetail.

        任务启动时间，格式为2020-06-17T07:38:42.503Z

        :return: The begin_time of this StepDetail.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this StepDetail.

        任务启动时间，格式为2020-06-17T07:38:42.503Z

        :param begin_time: The begin_time of this StepDetail.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this StepDetail.

        任务结束时间，格式为2020-06-17T07:38:42.503Z

        :return: The end_time of this StepDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this StepDetail.

        任务结束时间，格式为2020-06-17T07:38:42.503Z

        :param end_time: The end_time of this StepDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_code(self):
        """Gets the error_code of this StepDetail.

        错误码

        :return: The error_code of this StepDetail.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this StepDetail.

        错误码

        :param error_code: The error_code of this StepDetail.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def sub_step_details(self):
        """Gets the sub_step_details of this StepDetail.

        子任务详情列表

        :return: The sub_step_details of this StepDetail.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.SubStepDetail`]
        """
        return self._sub_step_details

    @sub_step_details.setter
    def sub_step_details(self, sub_step_details):
        """Sets the sub_step_details of this StepDetail.

        子任务详情列表

        :param sub_step_details: The sub_step_details of this StepDetail.
        :type sub_step_details: list[:class:`huaweicloudsdkdcs.v2.SubStepDetail`]
        """
        self._sub_step_details = sub_step_details

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
        if not isinstance(other, StepDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
