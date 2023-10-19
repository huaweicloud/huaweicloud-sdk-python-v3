# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatedAt:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'updated_at': 'datetime'
    }

    attribute_map = {
        'updated_at': 'updated_at'
    }

    def __init__(self, updated_at=None):
        """UpdatedAt

        The model defined in huaweicloud sdk

        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        """
        
        

        self._updated_at = None
        self.discriminator = None

        self.updated_at = updated_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UpdatedAt.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this UpdatedAt.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UpdatedAt.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this UpdatedAt.
        :type updated_at: datetime
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
        if not isinstance(other, UpdatedAt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
