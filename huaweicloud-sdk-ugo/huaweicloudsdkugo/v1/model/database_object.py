# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_type': 'str',
        'total_count': 'int',
        'succeed_count': 'int',
        'failed_count': 'int',
        'ignored_count': 'int',
        'manual_count': 'int',
        'success_rate': 'str'
    }

    attribute_map = {
        'object_type': 'object_type',
        'total_count': 'total_count',
        'succeed_count': 'succeed_count',
        'failed_count': 'failed_count',
        'ignored_count': 'ignored_count',
        'manual_count': 'manual_count',
        'success_rate': 'success_rate'
    }

    def __init__(self, object_type=None, total_count=None, succeed_count=None, failed_count=None, ignored_count=None, manual_count=None, success_rate=None):
        """DatabaseObject

        The model defined in huaweicloud sdk

        :param object_type: 对象类型。
        :type object_type: str
        :param total_count: 该类型对象的总数。
        :type total_count: int
        :param succeed_count: 成功的对象数量。
        :type succeed_count: int
        :param failed_count: 失败的对象数量。
        :type failed_count: int
        :param ignored_count: 忽略的对象数量。
        :type ignored_count: int
        :param manual_count: 手动操作的对象数量。
        :type manual_count: int
        :param success_rate: 成功率。
        :type success_rate: str
        """
        
        

        self._object_type = None
        self._total_count = None
        self._succeed_count = None
        self._failed_count = None
        self._ignored_count = None
        self._manual_count = None
        self._success_rate = None
        self.discriminator = None

        self.object_type = object_type
        self.total_count = total_count
        self.succeed_count = succeed_count
        self.failed_count = failed_count
        self.ignored_count = ignored_count
        self.manual_count = manual_count
        self.success_rate = success_rate

    @property
    def object_type(self):
        """Gets the object_type of this DatabaseObject.

        对象类型。

        :return: The object_type of this DatabaseObject.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this DatabaseObject.

        对象类型。

        :param object_type: The object_type of this DatabaseObject.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def total_count(self):
        """Gets the total_count of this DatabaseObject.

        该类型对象的总数。

        :return: The total_count of this DatabaseObject.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this DatabaseObject.

        该类型对象的总数。

        :param total_count: The total_count of this DatabaseObject.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def succeed_count(self):
        """Gets the succeed_count of this DatabaseObject.

        成功的对象数量。

        :return: The succeed_count of this DatabaseObject.
        :rtype: int
        """
        return self._succeed_count

    @succeed_count.setter
    def succeed_count(self, succeed_count):
        """Sets the succeed_count of this DatabaseObject.

        成功的对象数量。

        :param succeed_count: The succeed_count of this DatabaseObject.
        :type succeed_count: int
        """
        self._succeed_count = succeed_count

    @property
    def failed_count(self):
        """Gets the failed_count of this DatabaseObject.

        失败的对象数量。

        :return: The failed_count of this DatabaseObject.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        """Sets the failed_count of this DatabaseObject.

        失败的对象数量。

        :param failed_count: The failed_count of this DatabaseObject.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def ignored_count(self):
        """Gets the ignored_count of this DatabaseObject.

        忽略的对象数量。

        :return: The ignored_count of this DatabaseObject.
        :rtype: int
        """
        return self._ignored_count

    @ignored_count.setter
    def ignored_count(self, ignored_count):
        """Sets the ignored_count of this DatabaseObject.

        忽略的对象数量。

        :param ignored_count: The ignored_count of this DatabaseObject.
        :type ignored_count: int
        """
        self._ignored_count = ignored_count

    @property
    def manual_count(self):
        """Gets the manual_count of this DatabaseObject.

        手动操作的对象数量。

        :return: The manual_count of this DatabaseObject.
        :rtype: int
        """
        return self._manual_count

    @manual_count.setter
    def manual_count(self, manual_count):
        """Sets the manual_count of this DatabaseObject.

        手动操作的对象数量。

        :param manual_count: The manual_count of this DatabaseObject.
        :type manual_count: int
        """
        self._manual_count = manual_count

    @property
    def success_rate(self):
        """Gets the success_rate of this DatabaseObject.

        成功率。

        :return: The success_rate of this DatabaseObject.
        :rtype: str
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this DatabaseObject.

        成功率。

        :param success_rate: The success_rate of this DatabaseObject.
        :type success_rate: str
        """
        self._success_rate = success_rate

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
        if not isinstance(other, DatabaseObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
