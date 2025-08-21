# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'action_mode': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'offset': 'offset',
        'limit': 'limit',
        'action_mode': 'action_mode'
    }

    def __init__(self, cluster_id=None, offset=None, limit=None, action_mode=None):
        r"""UpgradeDetailRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 待升级的集群的ID。
        :type cluster_id: str
        :param offset: 偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。
        :type offset: int
        :param limit: 查询返回终端节点服务的连接列表限制每页个数，即每页返回的个数。
        :type limit: int
        :param action_mode: 查询升级行为。 - 查询集群版本升级详情：不填写该参数。 - 查询切换AZ详情：当前仅支持AZ_MIGRATION。
        :type action_mode: str
        """
        
        

        self._cluster_id = None
        self._offset = None
        self._limit = None
        self._action_mode = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if action_mode is not None:
            self.action_mode = action_mode

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpgradeDetailRequest.

        待升级的集群的ID。

        :return: The cluster_id of this UpgradeDetailRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpgradeDetailRequest.

        待升级的集群的ID。

        :param cluster_id: The cluster_id of this UpgradeDetailRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def offset(self):
        r"""Gets the offset of this UpgradeDetailRequest.

        偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。

        :return: The offset of this UpgradeDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this UpgradeDetailRequest.

        偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。

        :param offset: The offset of this UpgradeDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this UpgradeDetailRequest.

        查询返回终端节点服务的连接列表限制每页个数，即每页返回的个数。

        :return: The limit of this UpgradeDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this UpgradeDetailRequest.

        查询返回终端节点服务的连接列表限制每页个数，即每页返回的个数。

        :param limit: The limit of this UpgradeDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def action_mode(self):
        r"""Gets the action_mode of this UpgradeDetailRequest.

        查询升级行为。 - 查询集群版本升级详情：不填写该参数。 - 查询切换AZ详情：当前仅支持AZ_MIGRATION。

        :return: The action_mode of this UpgradeDetailRequest.
        :rtype: str
        """
        return self._action_mode

    @action_mode.setter
    def action_mode(self, action_mode):
        r"""Sets the action_mode of this UpgradeDetailRequest.

        查询升级行为。 - 查询集群版本升级详情：不填写该参数。 - 查询切换AZ详情：当前仅支持AZ_MIGRATION。

        :param action_mode: The action_mode of this UpgradeDetailRequest.
        :type action_mode: str
        """
        self._action_mode = action_mode

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
        if not isinstance(other, UpgradeDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
