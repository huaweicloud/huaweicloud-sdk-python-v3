# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditUpgradeStep:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'msg': 'str',
        'result_code': 'str',
        'step_name': 'str',
        'time': 'str'
    }

    attribute_map = {
        'msg': 'msg',
        'result_code': 'result_code',
        'step_name': 'step_name',
        'time': 'time'
    }

    def __init__(self, msg=None, result_code=None, step_name=None, time=None):
        r"""AuditUpgradeStep

        The model defined in huaweicloud sdk

        :param msg: 消息
        :type msg: str
        :param result_code: 结果码
        :type result_code: str
        :param step_name: 步骤名称
        :type step_name: str
        :param time: 升级时间
        :type time: str
        """
        
        

        self._msg = None
        self._result_code = None
        self._step_name = None
        self._time = None
        self.discriminator = None

        if msg is not None:
            self.msg = msg
        if result_code is not None:
            self.result_code = result_code
        if step_name is not None:
            self.step_name = step_name
        if time is not None:
            self.time = time

    @property
    def msg(self):
        r"""Gets the msg of this AuditUpgradeStep.

        消息

        :return: The msg of this AuditUpgradeStep.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this AuditUpgradeStep.

        消息

        :param msg: The msg of this AuditUpgradeStep.
        :type msg: str
        """
        self._msg = msg

    @property
    def result_code(self):
        r"""Gets the result_code of this AuditUpgradeStep.

        结果码

        :return: The result_code of this AuditUpgradeStep.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        r"""Sets the result_code of this AuditUpgradeStep.

        结果码

        :param result_code: The result_code of this AuditUpgradeStep.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def step_name(self):
        r"""Gets the step_name of this AuditUpgradeStep.

        步骤名称

        :return: The step_name of this AuditUpgradeStep.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        r"""Sets the step_name of this AuditUpgradeStep.

        步骤名称

        :param step_name: The step_name of this AuditUpgradeStep.
        :type step_name: str
        """
        self._step_name = step_name

    @property
    def time(self):
        r"""Gets the time of this AuditUpgradeStep.

        升级时间

        :return: The time of this AuditUpgradeStep.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this AuditUpgradeStep.

        升级时间

        :param time: The time of this AuditUpgradeStep.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, AuditUpgradeStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
