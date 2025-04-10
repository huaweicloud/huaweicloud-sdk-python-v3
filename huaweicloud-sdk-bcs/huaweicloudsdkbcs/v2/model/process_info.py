# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step_name': 'str',
        'status': 'str',
        'detail': 'str',
        'sub_steps': 'dict(str, SubDetail)',
        'serial_num': 'int'
    }

    attribute_map = {
        'step_name': 'step_name',
        'status': 'status',
        'detail': 'detail',
        'sub_steps': 'sub_steps',
        'serial_num': 'serial_num'
    }

    def __init__(self, step_name=None, status=None, detail=None, sub_steps=None, serial_num=None):
        r"""ProcessInfo

        The model defined in huaweicloud sdk

        :param step_name: 操作名
        :type step_name: str
        :param status: 操作状态
        :type status: str
        :param detail: 操作详情
        :type detail: str
        :param sub_steps: 子操作, \&quot;map[string][SubDetail] key:子操作名 value:子操作结果\&quot;
        :type sub_steps: dict(str, SubDetail)
        :param serial_num: 序列号
        :type serial_num: int
        """
        
        

        self._step_name = None
        self._status = None
        self._detail = None
        self._sub_steps = None
        self._serial_num = None
        self.discriminator = None

        if step_name is not None:
            self.step_name = step_name
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail
        if sub_steps is not None:
            self.sub_steps = sub_steps
        if serial_num is not None:
            self.serial_num = serial_num

    @property
    def step_name(self):
        r"""Gets the step_name of this ProcessInfo.

        操作名

        :return: The step_name of this ProcessInfo.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        r"""Sets the step_name of this ProcessInfo.

        操作名

        :param step_name: The step_name of this ProcessInfo.
        :type step_name: str
        """
        self._step_name = step_name

    @property
    def status(self):
        r"""Gets the status of this ProcessInfo.

        操作状态

        :return: The status of this ProcessInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ProcessInfo.

        操作状态

        :param status: The status of this ProcessInfo.
        :type status: str
        """
        self._status = status

    @property
    def detail(self):
        r"""Gets the detail of this ProcessInfo.

        操作详情

        :return: The detail of this ProcessInfo.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this ProcessInfo.

        操作详情

        :param detail: The detail of this ProcessInfo.
        :type detail: str
        """
        self._detail = detail

    @property
    def sub_steps(self):
        r"""Gets the sub_steps of this ProcessInfo.

        子操作, \"map[string][SubDetail] key:子操作名 value:子操作结果\"

        :return: The sub_steps of this ProcessInfo.
        :rtype: dict(str, SubDetail)
        """
        return self._sub_steps

    @sub_steps.setter
    def sub_steps(self, sub_steps):
        r"""Sets the sub_steps of this ProcessInfo.

        子操作, \"map[string][SubDetail] key:子操作名 value:子操作结果\"

        :param sub_steps: The sub_steps of this ProcessInfo.
        :type sub_steps: dict(str, SubDetail)
        """
        self._sub_steps = sub_steps

    @property
    def serial_num(self):
        r"""Gets the serial_num of this ProcessInfo.

        序列号

        :return: The serial_num of this ProcessInfo.
        :rtype: int
        """
        return self._serial_num

    @serial_num.setter
    def serial_num(self, serial_num):
        r"""Sets the serial_num of this ProcessInfo.

        序列号

        :param serial_num: The serial_num of this ProcessInfo.
        :type serial_num: int
        """
        self._serial_num = serial_num

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
        if not isinstance(other, ProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
