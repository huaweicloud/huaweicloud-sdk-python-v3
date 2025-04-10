# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParamGroupHistoryResponse:

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
        'is_applied': 'bool',
        'updated': 'str',
        'applied': 'str'
    }

    attribute_map = {
        'parameter_name': 'parameter_name',
        'old_value': 'old_value',
        'new_value': 'new_value',
        'update_result': 'update_result',
        'is_applied': 'is_applied',
        'updated': 'updated',
        'applied': 'applied'
    }

    def __init__(self, parameter_name=None, old_value=None, new_value=None, update_result=None, is_applied=None, updated=None, applied=None):
        r"""ParamGroupHistoryResponse

        The model defined in huaweicloud sdk

        :param parameter_name: 参数名称。
        :type parameter_name: str
        :param old_value: 修改前参数值。
        :type old_value: str
        :param new_value: 修改后参数值。
        :type new_value: str
        :param update_result: 更新结果。
        :type update_result: str
        :param is_applied: 是否应用。 - true：是。 - false：否。
        :type is_applied: bool
        :param updated: 修改时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type updated: str
        :param applied: 应用时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type applied: str
        """
        
        

        self._parameter_name = None
        self._old_value = None
        self._new_value = None
        self._update_result = None
        self._is_applied = None
        self._updated = None
        self._applied = None
        self.discriminator = None

        if parameter_name is not None:
            self.parameter_name = parameter_name
        if old_value is not None:
            self.old_value = old_value
        if new_value is not None:
            self.new_value = new_value
        if update_result is not None:
            self.update_result = update_result
        if is_applied is not None:
            self.is_applied = is_applied
        if updated is not None:
            self.updated = updated
        if applied is not None:
            self.applied = applied

    @property
    def parameter_name(self):
        r"""Gets the parameter_name of this ParamGroupHistoryResponse.

        参数名称。

        :return: The parameter_name of this ParamGroupHistoryResponse.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        r"""Sets the parameter_name of this ParamGroupHistoryResponse.

        参数名称。

        :param parameter_name: The parameter_name of this ParamGroupHistoryResponse.
        :type parameter_name: str
        """
        self._parameter_name = parameter_name

    @property
    def old_value(self):
        r"""Gets the old_value of this ParamGroupHistoryResponse.

        修改前参数值。

        :return: The old_value of this ParamGroupHistoryResponse.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        r"""Sets the old_value of this ParamGroupHistoryResponse.

        修改前参数值。

        :param old_value: The old_value of this ParamGroupHistoryResponse.
        :type old_value: str
        """
        self._old_value = old_value

    @property
    def new_value(self):
        r"""Gets the new_value of this ParamGroupHistoryResponse.

        修改后参数值。

        :return: The new_value of this ParamGroupHistoryResponse.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        r"""Sets the new_value of this ParamGroupHistoryResponse.

        修改后参数值。

        :param new_value: The new_value of this ParamGroupHistoryResponse.
        :type new_value: str
        """
        self._new_value = new_value

    @property
    def update_result(self):
        r"""Gets the update_result of this ParamGroupHistoryResponse.

        更新结果。

        :return: The update_result of this ParamGroupHistoryResponse.
        :rtype: str
        """
        return self._update_result

    @update_result.setter
    def update_result(self, update_result):
        r"""Sets the update_result of this ParamGroupHistoryResponse.

        更新结果。

        :param update_result: The update_result of this ParamGroupHistoryResponse.
        :type update_result: str
        """
        self._update_result = update_result

    @property
    def is_applied(self):
        r"""Gets the is_applied of this ParamGroupHistoryResponse.

        是否应用。 - true：是。 - false：否。

        :return: The is_applied of this ParamGroupHistoryResponse.
        :rtype: bool
        """
        return self._is_applied

    @is_applied.setter
    def is_applied(self, is_applied):
        r"""Sets the is_applied of this ParamGroupHistoryResponse.

        是否应用。 - true：是。 - false：否。

        :param is_applied: The is_applied of this ParamGroupHistoryResponse.
        :type is_applied: bool
        """
        self._is_applied = is_applied

    @property
    def updated(self):
        r"""Gets the updated of this ParamGroupHistoryResponse.

        修改时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The updated of this ParamGroupHistoryResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ParamGroupHistoryResponse.

        修改时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param updated: The updated of this ParamGroupHistoryResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def applied(self):
        r"""Gets the applied of this ParamGroupHistoryResponse.

        应用时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The applied of this ParamGroupHistoryResponse.
        :rtype: str
        """
        return self._applied

    @applied.setter
    def applied(self, applied):
        r"""Sets the applied of this ParamGroupHistoryResponse.

        应用时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param applied: The applied of this ParamGroupHistoryResponse.
        :type applied: str
        """
        self._applied = applied

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
        if not isinstance(other, ParamGroupHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
