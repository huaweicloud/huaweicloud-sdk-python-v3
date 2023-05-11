# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterCnResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_num': 'int',
        'max_num': 'int',
        'instances': 'list[CoordinatorNode]'
    }

    attribute_map = {
        'min_num': 'min_num',
        'max_num': 'max_num',
        'instances': 'instances'
    }

    def __init__(self, min_num=None, max_num=None, instances=None):
        """ListClusterCnResponse

        The model defined in huaweicloud sdk

        :param min_num: 集群支持的最小CN节点数量。
        :type min_num: int
        :param max_num: 集群支持的最大CN节点数量。
        :type max_num: int
        :param instances: CN节点详情列表。
        :type instances: list[:class:`huaweicloudsdkdws.v2.CoordinatorNode`]
        """
        
        super(ListClusterCnResponse, self).__init__()

        self._min_num = None
        self._max_num = None
        self._instances = None
        self.discriminator = None

        if min_num is not None:
            self.min_num = min_num
        if max_num is not None:
            self.max_num = max_num
        if instances is not None:
            self.instances = instances

    @property
    def min_num(self):
        """Gets the min_num of this ListClusterCnResponse.

        集群支持的最小CN节点数量。

        :return: The min_num of this ListClusterCnResponse.
        :rtype: int
        """
        return self._min_num

    @min_num.setter
    def min_num(self, min_num):
        """Sets the min_num of this ListClusterCnResponse.

        集群支持的最小CN节点数量。

        :param min_num: The min_num of this ListClusterCnResponse.
        :type min_num: int
        """
        self._min_num = min_num

    @property
    def max_num(self):
        """Gets the max_num of this ListClusterCnResponse.

        集群支持的最大CN节点数量。

        :return: The max_num of this ListClusterCnResponse.
        :rtype: int
        """
        return self._max_num

    @max_num.setter
    def max_num(self, max_num):
        """Sets the max_num of this ListClusterCnResponse.

        集群支持的最大CN节点数量。

        :param max_num: The max_num of this ListClusterCnResponse.
        :type max_num: int
        """
        self._max_num = max_num

    @property
    def instances(self):
        """Gets the instances of this ListClusterCnResponse.

        CN节点详情列表。

        :return: The instances of this ListClusterCnResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.CoordinatorNode`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListClusterCnResponse.

        CN节点详情列表。

        :param instances: The instances of this ListClusterCnResponse.
        :type instances: list[:class:`huaweicloudsdkdws.v2.CoordinatorNode`]
        """
        self._instances = instances

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
        if not isinstance(other, ListClusterCnResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
