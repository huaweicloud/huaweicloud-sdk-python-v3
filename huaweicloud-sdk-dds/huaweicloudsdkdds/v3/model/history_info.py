# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HistoryInfo:

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
        'updated_at': 'str'
    }

    attribute_map = {
        'parameter_name': 'parameter_name',
        'old_value': 'old_value',
        'new_value': 'new_value',
        'updated_at': 'updated_at'
    }

    def __init__(self, parameter_name=None, old_value=None, new_value=None, updated_at=None):
        """HistoryInfo

        The model defined in huaweicloud sdk

        :param parameter_name: 参数名称
        :type parameter_name: str
        :param old_value: 修改前的值。
        :type old_value: str
        :param new_value: 修改后的值。
        :type new_value: str
        :param updated_at: 修改时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type updated_at: str
        """
        
        

        self._parameter_name = None
        self._old_value = None
        self._new_value = None
        self._updated_at = None
        self.discriminator = None

        self.parameter_name = parameter_name
        self.old_value = old_value
        self.new_value = new_value
        self.updated_at = updated_at

    @property
    def parameter_name(self):
        """Gets the parameter_name of this HistoryInfo.

        参数名称

        :return: The parameter_name of this HistoryInfo.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this HistoryInfo.

        参数名称

        :param parameter_name: The parameter_name of this HistoryInfo.
        :type parameter_name: str
        """
        self._parameter_name = parameter_name

    @property
    def old_value(self):
        """Gets the old_value of this HistoryInfo.

        修改前的值。

        :return: The old_value of this HistoryInfo.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this HistoryInfo.

        修改前的值。

        :param old_value: The old_value of this HistoryInfo.
        :type old_value: str
        """
        self._old_value = old_value

    @property
    def new_value(self):
        """Gets the new_value of this HistoryInfo.

        修改后的值。

        :return: The new_value of this HistoryInfo.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this HistoryInfo.

        修改后的值。

        :param new_value: The new_value of this HistoryInfo.
        :type new_value: str
        """
        self._new_value = new_value

    @property
    def updated_at(self):
        """Gets the updated_at of this HistoryInfo.

        修改时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The updated_at of this HistoryInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this HistoryInfo.

        修改时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param updated_at: The updated_at of this HistoryInfo.
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
        if not isinstance(other, HistoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
