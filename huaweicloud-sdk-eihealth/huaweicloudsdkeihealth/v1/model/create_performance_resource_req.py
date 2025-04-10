# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePerformanceResourceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'space': 'int',
        'count': 'int'
    }

    attribute_map = {
        'space': 'space',
        'count': 'count'
    }

    def __init__(self, space=None, count=None):
        r"""CreatePerformanceResourceReq

        The model defined in huaweicloud sdk

        :param space: 存储空间，单位GB
        :type space: int
        :param count: 购买数量
        :type count: int
        """
        
        

        self._space = None
        self._count = None
        self.discriminator = None

        self.space = space
        self.count = count

    @property
    def space(self):
        r"""Gets the space of this CreatePerformanceResourceReq.

        存储空间，单位GB

        :return: The space of this CreatePerformanceResourceReq.
        :rtype: int
        """
        return self._space

    @space.setter
    def space(self, space):
        r"""Sets the space of this CreatePerformanceResourceReq.

        存储空间，单位GB

        :param space: The space of this CreatePerformanceResourceReq.
        :type space: int
        """
        self._space = space

    @property
    def count(self):
        r"""Gets the count of this CreatePerformanceResourceReq.

        购买数量

        :return: The count of this CreatePerformanceResourceReq.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this CreatePerformanceResourceReq.

        购买数量

        :param count: The count of this CreatePerformanceResourceReq.
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
        if not isinstance(other, CreatePerformanceResourceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
