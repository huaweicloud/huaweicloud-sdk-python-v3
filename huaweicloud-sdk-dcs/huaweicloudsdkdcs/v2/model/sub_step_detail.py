# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubStepDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_step_id': 'str',
        'sub_step_name': 'str',
        'sub_step_status': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'detail': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'sub_step_id': 'sub_step_id',
        'sub_step_name': 'sub_step_name',
        'sub_step_status': 'sub_step_status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'detail': 'detail',
        'error_code': 'error_code'
    }

    def __init__(self, sub_step_id=None, sub_step_name=None, sub_step_status=None, begin_time=None, end_time=None, detail=None, error_code=None):
        r"""SubStepDetail

        The model defined in huaweicloud sdk

        :param sub_step_id: 任务id
        :type sub_step_id: str
        :param sub_step_name: 任务名
        :type sub_step_name: str
        :param sub_step_status: 任务状态
        :type sub_step_status: str
        :param begin_time: 任务启动时间，格式为2020-06-17T07:38:42.503Z
        :type begin_time: str
        :param end_time: 任务结束时间，格式为2020-06-17T07:38:42.503Z
        :type end_time: str
        :param detail: 子任务的附加属性详情
        :type detail: str
        :param error_code: 错误码
        :type error_code: str
        """
        
        

        self._sub_step_id = None
        self._sub_step_name = None
        self._sub_step_status = None
        self._begin_time = None
        self._end_time = None
        self._detail = None
        self._error_code = None
        self.discriminator = None

        if sub_step_id is not None:
            self.sub_step_id = sub_step_id
        if sub_step_name is not None:
            self.sub_step_name = sub_step_name
        if sub_step_status is not None:
            self.sub_step_status = sub_step_status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if detail is not None:
            self.detail = detail
        if error_code is not None:
            self.error_code = error_code

    @property
    def sub_step_id(self):
        r"""Gets the sub_step_id of this SubStepDetail.

        任务id

        :return: The sub_step_id of this SubStepDetail.
        :rtype: str
        """
        return self._sub_step_id

    @sub_step_id.setter
    def sub_step_id(self, sub_step_id):
        r"""Sets the sub_step_id of this SubStepDetail.

        任务id

        :param sub_step_id: The sub_step_id of this SubStepDetail.
        :type sub_step_id: str
        """
        self._sub_step_id = sub_step_id

    @property
    def sub_step_name(self):
        r"""Gets the sub_step_name of this SubStepDetail.

        任务名

        :return: The sub_step_name of this SubStepDetail.
        :rtype: str
        """
        return self._sub_step_name

    @sub_step_name.setter
    def sub_step_name(self, sub_step_name):
        r"""Sets the sub_step_name of this SubStepDetail.

        任务名

        :param sub_step_name: The sub_step_name of this SubStepDetail.
        :type sub_step_name: str
        """
        self._sub_step_name = sub_step_name

    @property
    def sub_step_status(self):
        r"""Gets the sub_step_status of this SubStepDetail.

        任务状态

        :return: The sub_step_status of this SubStepDetail.
        :rtype: str
        """
        return self._sub_step_status

    @sub_step_status.setter
    def sub_step_status(self, sub_step_status):
        r"""Sets the sub_step_status of this SubStepDetail.

        任务状态

        :param sub_step_status: The sub_step_status of this SubStepDetail.
        :type sub_step_status: str
        """
        self._sub_step_status = sub_step_status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this SubStepDetail.

        任务启动时间，格式为2020-06-17T07:38:42.503Z

        :return: The begin_time of this SubStepDetail.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this SubStepDetail.

        任务启动时间，格式为2020-06-17T07:38:42.503Z

        :param begin_time: The begin_time of this SubStepDetail.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SubStepDetail.

        任务结束时间，格式为2020-06-17T07:38:42.503Z

        :return: The end_time of this SubStepDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SubStepDetail.

        任务结束时间，格式为2020-06-17T07:38:42.503Z

        :param end_time: The end_time of this SubStepDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def detail(self):
        r"""Gets the detail of this SubStepDetail.

        子任务的附加属性详情

        :return: The detail of this SubStepDetail.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this SubStepDetail.

        子任务的附加属性详情

        :param detail: The detail of this SubStepDetail.
        :type detail: str
        """
        self._detail = detail

    @property
    def error_code(self):
        r"""Gets the error_code of this SubStepDetail.

        错误码

        :return: The error_code of this SubStepDetail.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this SubStepDetail.

        错误码

        :param error_code: The error_code of this SubStepDetail.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, SubStepDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
