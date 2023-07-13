# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicListResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota': 'int',
        'total': 'int',
        'offset': 'int',
        'count': 'int'
    }

    attribute_map = {
        'quota': 'quota',
        'total': 'total',
        'offset': 'offset',
        'count': 'count'
    }

    def __init__(self, quota=None, total=None, offset=None, count=None):
        """BasicListResp

        The model defined in huaweicloud sdk

        :param quota: 配额
        :type quota: int
        :param total: 总数
        :type total: int
        :param offset: 偏移
        :type offset: int
        :param count: 返回数量
        :type count: int
        """
        
        

        self._quota = None
        self._total = None
        self._offset = None
        self._count = None
        self.discriminator = None

        self.quota = quota
        self.total = total
        self.offset = offset
        self.count = count

    @property
    def quota(self):
        """Gets the quota of this BasicListResp.

        配额

        :return: The quota of this BasicListResp.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this BasicListResp.

        配额

        :param quota: The quota of this BasicListResp.
        :type quota: int
        """
        self._quota = quota

    @property
    def total(self):
        """Gets the total of this BasicListResp.

        总数

        :return: The total of this BasicListResp.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BasicListResp.

        总数

        :param total: The total of this BasicListResp.
        :type total: int
        """
        self._total = total

    @property
    def offset(self):
        """Gets the offset of this BasicListResp.

        偏移

        :return: The offset of this BasicListResp.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this BasicListResp.

        偏移

        :param offset: The offset of this BasicListResp.
        :type offset: int
        """
        self._offset = offset

    @property
    def count(self):
        """Gets the count of this BasicListResp.

        返回数量

        :return: The count of this BasicListResp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BasicListResp.

        返回数量

        :param count: The count of this BasicListResp.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, BasicListResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
