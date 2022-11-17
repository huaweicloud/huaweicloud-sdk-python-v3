# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DropDatabaseV3Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_force_delete': 'bool'
    }

    attribute_map = {
        'is_force_delete': 'is_force_delete'
    }

    def __init__(self, is_force_delete=None):
        """DropDatabaseV3Req

        The model defined in huaweicloud sdk

        :param is_force_delete: 是否强制删除数据库，默认是false。
        :type is_force_delete: bool
        """
        
        

        self._is_force_delete = None
        self.discriminator = None

        if is_force_delete is not None:
            self.is_force_delete = is_force_delete

    @property
    def is_force_delete(self):
        """Gets the is_force_delete of this DropDatabaseV3Req.

        是否强制删除数据库，默认是false。

        :return: The is_force_delete of this DropDatabaseV3Req.
        :rtype: bool
        """
        return self._is_force_delete

    @is_force_delete.setter
    def is_force_delete(self, is_force_delete):
        """Sets the is_force_delete of this DropDatabaseV3Req.

        是否强制删除数据库，默认是false。

        :param is_force_delete: The is_force_delete of this DropDatabaseV3Req.
        :type is_force_delete: bool
        """
        self._is_force_delete = is_force_delete

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
        if not isinstance(other, DropDatabaseV3Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
