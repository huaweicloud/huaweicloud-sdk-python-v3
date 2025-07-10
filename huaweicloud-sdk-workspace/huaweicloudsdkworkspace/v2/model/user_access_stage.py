# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserAccessStage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stage': 'str',
        'duration': 'int',
        'is_success': 'bool',
        'start_time': 'int',
        'end_time': 'int',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'stage': 'stage',
        'duration': 'duration',
        'is_success': 'is_success',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, stage=None, duration=None, is_success=None, start_time=None, end_time=None, error_code=None, error_msg=None):
        r"""UserAccessStage

        The model defined in huaweicloud sdk

        :param stage: 接入阶段 | LOGIN - 登录 PRECONNECT - 预连接 CONNECT - 正式连接。
        :type stage: str
        :param duration: 花费时长，单位：ms。
        :type duration: int
        :param is_success: 接入阶段是否成功。
        :type is_success: bool
        :param start_time: 开始时间戳。
        :type start_time: int
        :param end_time: 结束时间戳。
        :type end_time: int
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误描述。
        :type error_msg: str
        """
        
        

        self._stage = None
        self._duration = None
        self._is_success = None
        self._start_time = None
        self._end_time = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if stage is not None:
            self.stage = stage
        if duration is not None:
            self.duration = duration
        if is_success is not None:
            self.is_success = is_success
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def stage(self):
        r"""Gets the stage of this UserAccessStage.

        接入阶段 | LOGIN - 登录 PRECONNECT - 预连接 CONNECT - 正式连接。

        :return: The stage of this UserAccessStage.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this UserAccessStage.

        接入阶段 | LOGIN - 登录 PRECONNECT - 预连接 CONNECT - 正式连接。

        :param stage: The stage of this UserAccessStage.
        :type stage: str
        """
        self._stage = stage

    @property
    def duration(self):
        r"""Gets the duration of this UserAccessStage.

        花费时长，单位：ms。

        :return: The duration of this UserAccessStage.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this UserAccessStage.

        花费时长，单位：ms。

        :param duration: The duration of this UserAccessStage.
        :type duration: int
        """
        self._duration = duration

    @property
    def is_success(self):
        r"""Gets the is_success of this UserAccessStage.

        接入阶段是否成功。

        :return: The is_success of this UserAccessStage.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this UserAccessStage.

        接入阶段是否成功。

        :param is_success: The is_success of this UserAccessStage.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def start_time(self):
        r"""Gets the start_time of this UserAccessStage.

        开始时间戳。

        :return: The start_time of this UserAccessStage.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this UserAccessStage.

        开始时间戳。

        :param start_time: The start_time of this UserAccessStage.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this UserAccessStage.

        结束时间戳。

        :return: The end_time of this UserAccessStage.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this UserAccessStage.

        结束时间戳。

        :param end_time: The end_time of this UserAccessStage.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def error_code(self):
        r"""Gets the error_code of this UserAccessStage.

        错误码。

        :return: The error_code of this UserAccessStage.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this UserAccessStage.

        错误码。

        :param error_code: The error_code of this UserAccessStage.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this UserAccessStage.

        错误描述。

        :return: The error_msg of this UserAccessStage.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this UserAccessStage.

        错误描述。

        :param error_msg: The error_msg of this UserAccessStage.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, UserAccessStage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
