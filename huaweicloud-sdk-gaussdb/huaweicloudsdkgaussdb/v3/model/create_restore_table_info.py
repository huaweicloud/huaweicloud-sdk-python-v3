# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRestoreTableInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'old_name': 'str',
        'new_name': 'str'
    }

    attribute_map = {
        'old_name': 'old_name',
        'new_name': 'new_name'
    }

    def __init__(self, old_name=None, new_name=None):
        """CreateRestoreTableInfo

        The model defined in huaweicloud sdk

        :param old_name: 恢复前表名。
        :type old_name: str
        :param new_name: 恢复后表名。
        :type new_name: str
        """
        
        

        self._old_name = None
        self._new_name = None
        self.discriminator = None

        self.old_name = old_name
        self.new_name = new_name

    @property
    def old_name(self):
        """Gets the old_name of this CreateRestoreTableInfo.

        恢复前表名。

        :return: The old_name of this CreateRestoreTableInfo.
        :rtype: str
        """
        return self._old_name

    @old_name.setter
    def old_name(self, old_name):
        """Sets the old_name of this CreateRestoreTableInfo.

        恢复前表名。

        :param old_name: The old_name of this CreateRestoreTableInfo.
        :type old_name: str
        """
        self._old_name = old_name

    @property
    def new_name(self):
        """Gets the new_name of this CreateRestoreTableInfo.

        恢复后表名。

        :return: The new_name of this CreateRestoreTableInfo.
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this CreateRestoreTableInfo.

        恢复后表名。

        :param new_name: The new_name of this CreateRestoreTableInfo.
        :type new_name: str
        """
        self._new_name = new_name

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
        if not isinstance(other, CreateRestoreTableInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
