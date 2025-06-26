# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckClusterShrinkRequest:

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
        'check_item': 'str',
        'shrink_count': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'check_item': 'check_item',
        'shrink_count': 'shrink_count'
    }

    def __init__(self, cluster_id=None, check_item=None, shrink_count=None):
        r"""CheckClusterShrinkRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param check_item: **参数解释**： 检查项，取值当前仅包含3种。 **约束限制**： 不涉及。 **取值范围**： guc：检查当前guc参数是否满足缩容条件。 schema：检查所有schema下有无影响缩容的表。 disk：检查缩容后磁盘容量是否满足要求。 **默认取值**： 不涉及。
        :type check_item: str
        :param shrink_count: **参数解释**： 待缩容节点数。 **约束限制**： 不涉及。 **取值范围**： 最小值为3，最大值为当前节点总数减3。 **默认取值**： 不涉及。
        :type shrink_count: int
        """
        
        

        self._cluster_id = None
        self._check_item = None
        self._shrink_count = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.check_item = check_item
        self.shrink_count = shrink_count

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CheckClusterShrinkRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :return: The cluster_id of this CheckClusterShrinkRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CheckClusterShrinkRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this CheckClusterShrinkRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def check_item(self):
        r"""Gets the check_item of this CheckClusterShrinkRequest.

        **参数解释**： 检查项，取值当前仅包含3种。 **约束限制**： 不涉及。 **取值范围**： guc：检查当前guc参数是否满足缩容条件。 schema：检查所有schema下有无影响缩容的表。 disk：检查缩容后磁盘容量是否满足要求。 **默认取值**： 不涉及。

        :return: The check_item of this CheckClusterShrinkRequest.
        :rtype: str
        """
        return self._check_item

    @check_item.setter
    def check_item(self, check_item):
        r"""Sets the check_item of this CheckClusterShrinkRequest.

        **参数解释**： 检查项，取值当前仅包含3种。 **约束限制**： 不涉及。 **取值范围**： guc：检查当前guc参数是否满足缩容条件。 schema：检查所有schema下有无影响缩容的表。 disk：检查缩容后磁盘容量是否满足要求。 **默认取值**： 不涉及。

        :param check_item: The check_item of this CheckClusterShrinkRequest.
        :type check_item: str
        """
        self._check_item = check_item

    @property
    def shrink_count(self):
        r"""Gets the shrink_count of this CheckClusterShrinkRequest.

        **参数解释**： 待缩容节点数。 **约束限制**： 不涉及。 **取值范围**： 最小值为3，最大值为当前节点总数减3。 **默认取值**： 不涉及。

        :return: The shrink_count of this CheckClusterShrinkRequest.
        :rtype: int
        """
        return self._shrink_count

    @shrink_count.setter
    def shrink_count(self, shrink_count):
        r"""Sets the shrink_count of this CheckClusterShrinkRequest.

        **参数解释**： 待缩容节点数。 **约束限制**： 不涉及。 **取值范围**： 最小值为3，最大值为当前节点总数减3。 **默认取值**： 不涉及。

        :param shrink_count: The shrink_count of this CheckClusterShrinkRequest.
        :type shrink_count: int
        """
        self._shrink_count = shrink_count

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
        if not isinstance(other, CheckClusterShrinkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
