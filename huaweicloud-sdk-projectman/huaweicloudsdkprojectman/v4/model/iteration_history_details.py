# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IterationHistoryDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'operate_field_name': 'str',
        'new_value': 'str',
        'old_value': 'str'
    }

    attribute_map = {
        'operate_field_name': 'operate_field_name',
        'new_value': 'new_value',
        'old_value': 'old_value'
    }

    def __init__(self, operate_field_name=None, new_value=None, old_value=None):
        """IterationHistoryDetails

        The model defined in huaweicloud sdk

        :param operate_field_name: 变更的字段
        :type operate_field_name: str
        :param new_value: 操作后的值
        :type new_value: str
        :param old_value: 操作前的值
        :type old_value: str
        """
        
        

        self._operate_field_name = None
        self._new_value = None
        self._old_value = None
        self.discriminator = None

        if operate_field_name is not None:
            self.operate_field_name = operate_field_name
        if new_value is not None:
            self.new_value = new_value
        if old_value is not None:
            self.old_value = old_value

    @property
    def operate_field_name(self):
        """Gets the operate_field_name of this IterationHistoryDetails.

        变更的字段

        :return: The operate_field_name of this IterationHistoryDetails.
        :rtype: str
        """
        return self._operate_field_name

    @operate_field_name.setter
    def operate_field_name(self, operate_field_name):
        """Sets the operate_field_name of this IterationHistoryDetails.

        变更的字段

        :param operate_field_name: The operate_field_name of this IterationHistoryDetails.
        :type operate_field_name: str
        """
        self._operate_field_name = operate_field_name

    @property
    def new_value(self):
        """Gets the new_value of this IterationHistoryDetails.

        操作后的值

        :return: The new_value of this IterationHistoryDetails.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this IterationHistoryDetails.

        操作后的值

        :param new_value: The new_value of this IterationHistoryDetails.
        :type new_value: str
        """
        self._new_value = new_value

    @property
    def old_value(self):
        """Gets the old_value of this IterationHistoryDetails.

        操作前的值

        :return: The old_value of this IterationHistoryDetails.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this IterationHistoryDetails.

        操作前的值

        :param old_value: The old_value of this IterationHistoryDetails.
        :type old_value: str
        """
        self._old_value = old_value

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
        if not isinstance(other, IterationHistoryDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
