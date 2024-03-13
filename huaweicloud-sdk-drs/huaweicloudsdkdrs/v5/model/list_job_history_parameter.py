# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobHistoryParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'old_value': 'str',
        'new_value': 'str',
        'is_update_success': 'bool',
        'is_applied': 'bool',
        'update_time': 'str',
        'apply_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'old_value': 'old_value',
        'new_value': 'new_value',
        'is_update_success': 'is_update_success',
        'is_applied': 'is_applied',
        'update_time': 'update_time',
        'apply_time': 'apply_time'
    }

    def __init__(self, name=None, old_value=None, new_value=None, is_update_success=None, is_applied=None, update_time=None, apply_time=None):
        """ListJobHistoryParameter

        The model defined in huaweicloud sdk

        :param name: 参数名称。
        :type name: str
        :param old_value: 旧参数值。
        :type old_value: str
        :param new_value: 新参数值。
        :type new_value: str
        :param is_update_success: 更新结果。true：成功，false：失败
        :type is_update_success: bool
        :param is_applied: 是否已应用。true：已应用，false：未应用
        :type is_applied: bool
        :param update_time: 参数修改时间。
        :type update_time: str
        :param apply_time: 参数应用时间。
        :type apply_time: str
        """
        
        

        self._name = None
        self._old_value = None
        self._new_value = None
        self._is_update_success = None
        self._is_applied = None
        self._update_time = None
        self._apply_time = None
        self.discriminator = None

        self.name = name
        self.old_value = old_value
        self.new_value = new_value
        self.is_update_success = is_update_success
        self.is_applied = is_applied
        self.update_time = update_time
        if apply_time is not None:
            self.apply_time = apply_time

    @property
    def name(self):
        """Gets the name of this ListJobHistoryParameter.

        参数名称。

        :return: The name of this ListJobHistoryParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListJobHistoryParameter.

        参数名称。

        :param name: The name of this ListJobHistoryParameter.
        :type name: str
        """
        self._name = name

    @property
    def old_value(self):
        """Gets the old_value of this ListJobHistoryParameter.

        旧参数值。

        :return: The old_value of this ListJobHistoryParameter.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this ListJobHistoryParameter.

        旧参数值。

        :param old_value: The old_value of this ListJobHistoryParameter.
        :type old_value: str
        """
        self._old_value = old_value

    @property
    def new_value(self):
        """Gets the new_value of this ListJobHistoryParameter.

        新参数值。

        :return: The new_value of this ListJobHistoryParameter.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this ListJobHistoryParameter.

        新参数值。

        :param new_value: The new_value of this ListJobHistoryParameter.
        :type new_value: str
        """
        self._new_value = new_value

    @property
    def is_update_success(self):
        """Gets the is_update_success of this ListJobHistoryParameter.

        更新结果。true：成功，false：失败

        :return: The is_update_success of this ListJobHistoryParameter.
        :rtype: bool
        """
        return self._is_update_success

    @is_update_success.setter
    def is_update_success(self, is_update_success):
        """Sets the is_update_success of this ListJobHistoryParameter.

        更新结果。true：成功，false：失败

        :param is_update_success: The is_update_success of this ListJobHistoryParameter.
        :type is_update_success: bool
        """
        self._is_update_success = is_update_success

    @property
    def is_applied(self):
        """Gets the is_applied of this ListJobHistoryParameter.

        是否已应用。true：已应用，false：未应用

        :return: The is_applied of this ListJobHistoryParameter.
        :rtype: bool
        """
        return self._is_applied

    @is_applied.setter
    def is_applied(self, is_applied):
        """Sets the is_applied of this ListJobHistoryParameter.

        是否已应用。true：已应用，false：未应用

        :param is_applied: The is_applied of this ListJobHistoryParameter.
        :type is_applied: bool
        """
        self._is_applied = is_applied

    @property
    def update_time(self):
        """Gets the update_time of this ListJobHistoryParameter.

        参数修改时间。

        :return: The update_time of this ListJobHistoryParameter.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ListJobHistoryParameter.

        参数修改时间。

        :param update_time: The update_time of this ListJobHistoryParameter.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def apply_time(self):
        """Gets the apply_time of this ListJobHistoryParameter.

        参数应用时间。

        :return: The apply_time of this ListJobHistoryParameter.
        :rtype: str
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this ListJobHistoryParameter.

        参数应用时间。

        :param apply_time: The apply_time of this ListJobHistoryParameter.
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
        if not isinstance(other, ListJobHistoryParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
