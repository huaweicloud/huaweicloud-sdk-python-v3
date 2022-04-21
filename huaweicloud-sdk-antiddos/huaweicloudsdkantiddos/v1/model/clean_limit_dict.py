# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CleanLimitDict:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cleaning_access_pos_id': 'int',
        'new_connection_limited': 'int',
        'total_connection_limited': 'int'
    }

    attribute_map = {
        'cleaning_access_pos_id': 'cleaning_access_pos_id',
        'new_connection_limited': 'new_connection_limited',
        'total_connection_limited': 'total_connection_limited'
    }

    def __init__(self, cleaning_access_pos_id=None, new_connection_limited=None, total_connection_limited=None):
        """CleanLimitDict

        The model defined in huaweicloud sdk

        :param cleaning_access_pos_id: 清洗时访问限制分段ID
        :type cleaning_access_pos_id: int
        :param new_connection_limited: 单一源IP新建连接个数
        :type new_connection_limited: int
        :param total_connection_limited: 单一源IP连接数总个数
        :type total_connection_limited: int
        """
        
        

        self._cleaning_access_pos_id = None
        self._new_connection_limited = None
        self._total_connection_limited = None
        self.discriminator = None

        self.cleaning_access_pos_id = cleaning_access_pos_id
        self.new_connection_limited = new_connection_limited
        self.total_connection_limited = total_connection_limited

    @property
    def cleaning_access_pos_id(self):
        """Gets the cleaning_access_pos_id of this CleanLimitDict.

        清洗时访问限制分段ID

        :return: The cleaning_access_pos_id of this CleanLimitDict.
        :rtype: int
        """
        return self._cleaning_access_pos_id

    @cleaning_access_pos_id.setter
    def cleaning_access_pos_id(self, cleaning_access_pos_id):
        """Sets the cleaning_access_pos_id of this CleanLimitDict.

        清洗时访问限制分段ID

        :param cleaning_access_pos_id: The cleaning_access_pos_id of this CleanLimitDict.
        :type cleaning_access_pos_id: int
        """
        self._cleaning_access_pos_id = cleaning_access_pos_id

    @property
    def new_connection_limited(self):
        """Gets the new_connection_limited of this CleanLimitDict.

        单一源IP新建连接个数

        :return: The new_connection_limited of this CleanLimitDict.
        :rtype: int
        """
        return self._new_connection_limited

    @new_connection_limited.setter
    def new_connection_limited(self, new_connection_limited):
        """Sets the new_connection_limited of this CleanLimitDict.

        单一源IP新建连接个数

        :param new_connection_limited: The new_connection_limited of this CleanLimitDict.
        :type new_connection_limited: int
        """
        self._new_connection_limited = new_connection_limited

    @property
    def total_connection_limited(self):
        """Gets the total_connection_limited of this CleanLimitDict.

        单一源IP连接数总个数

        :return: The total_connection_limited of this CleanLimitDict.
        :rtype: int
        """
        return self._total_connection_limited

    @total_connection_limited.setter
    def total_connection_limited(self, total_connection_limited):
        """Sets the total_connection_limited of this CleanLimitDict.

        单一源IP连接数总个数

        :param total_connection_limited: The total_connection_limited of this CleanLimitDict.
        :type total_connection_limited: int
        """
        self._total_connection_limited = total_connection_limited

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
        if not isinstance(other, CleanLimitDict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
