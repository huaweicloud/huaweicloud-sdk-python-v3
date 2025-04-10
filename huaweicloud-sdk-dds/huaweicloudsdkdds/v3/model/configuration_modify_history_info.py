# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationModifyHistoryInfo:

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
        'updated_at': 'str',
        'applied_at': 'str'
    }

    attribute_map = {
        'parameter_name': 'parameter_name',
        'old_value': 'old_value',
        'new_value': 'new_value',
        'update_result': 'update_result',
        'applied': 'applied',
        'updated_at': 'updated_at',
        'applied_at': 'applied_at'
    }

    def __init__(self, parameter_name=None, old_value=None, new_value=None, update_result=None, applied=None, updated_at=None, applied_at=None):
        r"""ConfigurationModifyHistoryInfo

        The model defined in huaweicloud sdk

        :param parameter_name: 参数名称。
        :type parameter_name: str
        :param old_value: 修改前的值。
        :type old_value: str
        :param new_value: 修改后的值。
        :type new_value: str
        :param update_result: 更新结果。
        :type update_result: str
        :param applied: 是否被应用。 - true: 已被应用。 - false: 未被应用。
        :type applied: bool
        :param updated_at: 修改时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type updated_at: str
        :param applied_at: 应用时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type applied_at: str
        """
        
        

        self._parameter_name = None
        self._old_value = None
        self._new_value = None
        self._update_result = None
        self._applied = None
        self._updated_at = None
        self._applied_at = None
        self.discriminator = None

        self.parameter_name = parameter_name
        self.old_value = old_value
        self.new_value = new_value
        self.update_result = update_result
        self.applied = applied
        self.updated_at = updated_at
        self.applied_at = applied_at

    @property
    def parameter_name(self):
        r"""Gets the parameter_name of this ConfigurationModifyHistoryInfo.

        参数名称。

        :return: The parameter_name of this ConfigurationModifyHistoryInfo.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        r"""Sets the parameter_name of this ConfigurationModifyHistoryInfo.

        参数名称。

        :param parameter_name: The parameter_name of this ConfigurationModifyHistoryInfo.
        :type parameter_name: str
        """
        self._parameter_name = parameter_name

    @property
    def old_value(self):
        r"""Gets the old_value of this ConfigurationModifyHistoryInfo.

        修改前的值。

        :return: The old_value of this ConfigurationModifyHistoryInfo.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        r"""Sets the old_value of this ConfigurationModifyHistoryInfo.

        修改前的值。

        :param old_value: The old_value of this ConfigurationModifyHistoryInfo.
        :type old_value: str
        """
        self._old_value = old_value

    @property
    def new_value(self):
        r"""Gets the new_value of this ConfigurationModifyHistoryInfo.

        修改后的值。

        :return: The new_value of this ConfigurationModifyHistoryInfo.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        r"""Sets the new_value of this ConfigurationModifyHistoryInfo.

        修改后的值。

        :param new_value: The new_value of this ConfigurationModifyHistoryInfo.
        :type new_value: str
        """
        self._new_value = new_value

    @property
    def update_result(self):
        r"""Gets the update_result of this ConfigurationModifyHistoryInfo.

        更新结果。

        :return: The update_result of this ConfigurationModifyHistoryInfo.
        :rtype: str
        """
        return self._update_result

    @update_result.setter
    def update_result(self, update_result):
        r"""Sets the update_result of this ConfigurationModifyHistoryInfo.

        更新结果。

        :param update_result: The update_result of this ConfigurationModifyHistoryInfo.
        :type update_result: str
        """
        self._update_result = update_result

    @property
    def applied(self):
        r"""Gets the applied of this ConfigurationModifyHistoryInfo.

        是否被应用。 - true: 已被应用。 - false: 未被应用。

        :return: The applied of this ConfigurationModifyHistoryInfo.
        :rtype: bool
        """
        return self._applied

    @applied.setter
    def applied(self, applied):
        r"""Sets the applied of this ConfigurationModifyHistoryInfo.

        是否被应用。 - true: 已被应用。 - false: 未被应用。

        :param applied: The applied of this ConfigurationModifyHistoryInfo.
        :type applied: bool
        """
        self._applied = applied

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ConfigurationModifyHistoryInfo.

        修改时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The updated_at of this ConfigurationModifyHistoryInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ConfigurationModifyHistoryInfo.

        修改时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param updated_at: The updated_at of this ConfigurationModifyHistoryInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def applied_at(self):
        r"""Gets the applied_at of this ConfigurationModifyHistoryInfo.

        应用时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The applied_at of this ConfigurationModifyHistoryInfo.
        :rtype: str
        """
        return self._applied_at

    @applied_at.setter
    def applied_at(self, applied_at):
        r"""Sets the applied_at of this ConfigurationModifyHistoryInfo.

        应用时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param applied_at: The applied_at of this ConfigurationModifyHistoryInfo.
        :type applied_at: str
        """
        self._applied_at = applied_at

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
        if not isinstance(other, ConfigurationModifyHistoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
