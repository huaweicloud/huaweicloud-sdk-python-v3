# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryOperationsResult:

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
        'updated_at': 'str'
    }

    attribute_map = {
        'parameter_name': 'parameter_name',
        'old_value': 'old_value',
        'new_value': 'new_value',
        'update_result': 'update_result',
        'updated_at': 'updated_at'
    }

    def __init__(self, parameter_name=None, old_value=None, new_value=None, update_result=None, updated_at=None):
        """ListHistoryOperationsResult

        The model defined in huaweicloud sdk

        :param parameter_name: 参数名称。
        :type parameter_name: str
        :param old_value: 修改前参数值。
        :type old_value: str
        :param new_value: 修改后参数值。
        :type new_value: str
        :param update_result: 修改状态 (SUCCESS | FAILED)。
        :type update_result: str
        :param updated_at: 修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type updated_at: str
        """
        
        

        self._parameter_name = None
        self._old_value = None
        self._new_value = None
        self._update_result = None
        self._updated_at = None
        self.discriminator = None

        self.parameter_name = parameter_name
        self.old_value = old_value
        self.new_value = new_value
        self.update_result = update_result
        self.updated_at = updated_at

    @property
    def parameter_name(self):
        """Gets the parameter_name of this ListHistoryOperationsResult.

        参数名称。

        :return: The parameter_name of this ListHistoryOperationsResult.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this ListHistoryOperationsResult.

        参数名称。

        :param parameter_name: The parameter_name of this ListHistoryOperationsResult.
        :type parameter_name: str
        """
        self._parameter_name = parameter_name

    @property
    def old_value(self):
        """Gets the old_value of this ListHistoryOperationsResult.

        修改前参数值。

        :return: The old_value of this ListHistoryOperationsResult.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this ListHistoryOperationsResult.

        修改前参数值。

        :param old_value: The old_value of this ListHistoryOperationsResult.
        :type old_value: str
        """
        self._old_value = old_value

    @property
    def new_value(self):
        """Gets the new_value of this ListHistoryOperationsResult.

        修改后参数值。

        :return: The new_value of this ListHistoryOperationsResult.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this ListHistoryOperationsResult.

        修改后参数值。

        :param new_value: The new_value of this ListHistoryOperationsResult.
        :type new_value: str
        """
        self._new_value = new_value

    @property
    def update_result(self):
        """Gets the update_result of this ListHistoryOperationsResult.

        修改状态 (SUCCESS | FAILED)。

        :return: The update_result of this ListHistoryOperationsResult.
        :rtype: str
        """
        return self._update_result

    @update_result.setter
    def update_result(self, update_result):
        """Sets the update_result of this ListHistoryOperationsResult.

        修改状态 (SUCCESS | FAILED)。

        :param update_result: The update_result of this ListHistoryOperationsResult.
        :type update_result: str
        """
        self._update_result = update_result

    @property
    def updated_at(self):
        """Gets the updated_at of this ListHistoryOperationsResult.

        修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The updated_at of this ListHistoryOperationsResult.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListHistoryOperationsResult.

        修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param updated_at: The updated_at of this ListHistoryOperationsResult.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ListHistoryOperationsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
