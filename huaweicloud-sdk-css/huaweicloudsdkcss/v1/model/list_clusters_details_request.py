# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClustersDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, start=None, limit=None):
        """ListClustersDetailsRequest

        The model defined in huaweicloud sdk

        :param start: 指定查询起始值，默认值为1，即从第1个集群开始查询。
        :type start: int
        :param limit: 指定查询个数，默认值为10，即一次查询10个集群信息。
        :type limit: int
        """
        
        

        self._start = None
        self._limit = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def start(self):
        """Gets the start of this ListClustersDetailsRequest.

        指定查询起始值，默认值为1，即从第1个集群开始查询。

        :return: The start of this ListClustersDetailsRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListClustersDetailsRequest.

        指定查询起始值，默认值为1，即从第1个集群开始查询。

        :param start: The start of this ListClustersDetailsRequest.
        :type start: int
        """
        self._start = start

    @property
    def limit(self):
        """Gets the limit of this ListClustersDetailsRequest.

        指定查询个数，默认值为10，即一次查询10个集群信息。

        :return: The limit of this ListClustersDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListClustersDetailsRequest.

        指定查询个数，默认值为10，即一次查询10个集群信息。

        :param limit: The limit of this ListClustersDetailsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListClustersDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
