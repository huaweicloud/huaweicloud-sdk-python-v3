# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParamGroupHistoryResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameter_name': 'str',
        'old_value': 'str',
        'new_value': 'str',
        'update_result': 'str',
        'applied': 'bool',
        'update_time': 'str',
        'apply_time': 'str'
    }

    attribute_map = {
        'parameter_name': 'parameter_name',
        'old_value': 'old_value',
        'new_value': 'new_value',
        'update_result': 'update_result',
        'applied': 'applied',
        'update_time': 'update_time',
        'apply_time': 'apply_time'
    }

    def __init__(self, parameter_name=None, old_value=None, new_value=None, update_result=None, applied=None, update_time=None, apply_time=None):
        """ParamGroupHistoryResult

        The model defined in huaweicloud sdk

        :param parameter_name: 参数名称
        :type parameter_name: str
        :param old_value: 旧值
        :type old_value: str
        :param new_value: 新值
        :type new_value: str
        :param update_result: 更新结果 成功：SUCCESS 失败： FAILED
        :type update_result: str
        :param applied: 是否已应用 true：已应用 false：未应用
        :type applied: bool
        :param update_time: 修改时间
        :type update_time: str
        :param apply_time: 应用时间
        :type apply_time: str
        """
        
        

        self._parameter_name = None
        self._old_value = None
        self._new_value = None
        self._update_result = None
        self._applied = None
        self._update_time = None
        self._apply_time = None
        self.discriminator = None

        if parameter_name is not None:
            self.parameter_name = parameter_name
        if old_value is not None:
            self.old_value = old_value
        if new_value is not None:
            self.new_value = new_value
        if update_result is not None:
            self.update_result = update_result
        if applied is not None:
            self.applied = applied
        if update_time is not None:
            self.update_time = update_time
        if apply_time is not None:
            self.apply_time = apply_time

    @property
    def parameter_name(self):
        """Gets the parameter_name of this ParamGroupHistoryResult.

        参数名称

        :return: The parameter_name of this ParamGroupHistoryResult.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this ParamGroupHistoryResult.

        参数名称

        :param parameter_name: The parameter_name of this ParamGroupHistoryResult.
        :type parameter_name: str
        """
        self._parameter_name = parameter_name

    @property
    def old_value(self):
        """Gets the old_value of this ParamGroupHistoryResult.

        旧值

        :return: The old_value of this ParamGroupHistoryResult.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this ParamGroupHistoryResult.

        旧值

        :param old_value: The old_value of this ParamGroupHistoryResult.
        :type old_value: str
        """
        self._old_value = old_value

    @property
    def new_value(self):
        """Gets the new_value of this ParamGroupHistoryResult.

        新值

        :return: The new_value of this ParamGroupHistoryResult.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this ParamGroupHistoryResult.

        新值

        :param new_value: The new_value of this ParamGroupHistoryResult.
        :type new_value: str
        """
        self._new_value = new_value

    @property
    def update_result(self):
        """Gets the update_result of this ParamGroupHistoryResult.

        更新结果 成功：SUCCESS 失败： FAILED

        :return: The update_result of this ParamGroupHistoryResult.
        :rtype: str
        """
        return self._update_result

    @update_result.setter
    def update_result(self, update_result):
        """Sets the update_result of this ParamGroupHistoryResult.

        更新结果 成功：SUCCESS 失败： FAILED

        :param update_result: The update_result of this ParamGroupHistoryResult.
        :type update_result: str
        """
        self._update_result = update_result

    @property
    def applied(self):
        """Gets the applied of this ParamGroupHistoryResult.

        是否已应用 true：已应用 false：未应用

        :return: The applied of this ParamGroupHistoryResult.
        :rtype: bool
        """
        return self._applied

    @applied.setter
    def applied(self, applied):
        """Sets the applied of this ParamGroupHistoryResult.

        是否已应用 true：已应用 false：未应用

        :param applied: The applied of this ParamGroupHistoryResult.
        :type applied: bool
        """
        self._applied = applied

    @property
    def update_time(self):
        """Gets the update_time of this ParamGroupHistoryResult.

        修改时间

        :return: The update_time of this ParamGroupHistoryResult.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ParamGroupHistoryResult.

        修改时间

        :param update_time: The update_time of this ParamGroupHistoryResult.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def apply_time(self):
        """Gets the apply_time of this ParamGroupHistoryResult.

        应用时间

        :return: The apply_time of this ParamGroupHistoryResult.
        :rtype: str
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this ParamGroupHistoryResult.

        应用时间

        :param apply_time: The apply_time of this ParamGroupHistoryResult.
        :type apply_time: str
        """
        self._apply_time = apply_time

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
        if not isinstance(other, ParamGroupHistoryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
