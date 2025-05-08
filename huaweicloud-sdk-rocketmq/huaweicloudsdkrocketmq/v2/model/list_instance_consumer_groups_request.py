# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceConsumerGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'group': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group': 'group',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, group=None, limit=None, offset=None):
        r"""ListInstanceConsumerGroupsRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。获取方法如下：登录RocketMQ控制台，在RocketMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type instance_id: str
        :param group: **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type group: str
        :param limit: **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10。
        :type limit: int
        :param offset: **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0。
        :type offset: int
        """
        
        

        self._instance_id = None
        self._group = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        if group is not None:
            self.group = group
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceConsumerGroupsRequest.

        **参数解释**： 实例ID。获取方法如下：登录RocketMQ控制台，在RocketMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_id of this ListInstanceConsumerGroupsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceConsumerGroupsRequest.

        **参数解释**： 实例ID。获取方法如下：登录RocketMQ控制台，在RocketMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param instance_id: The instance_id of this ListInstanceConsumerGroupsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group(self):
        r"""Gets the group of this ListInstanceConsumerGroupsRequest.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The group of this ListInstanceConsumerGroupsRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ListInstanceConsumerGroupsRequest.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param group: The group of this ListInstanceConsumerGroupsRequest.
        :type group: str
        """
        self._group = group

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceConsumerGroupsRequest.

        **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10。

        :return: The limit of this ListInstanceConsumerGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceConsumerGroupsRequest.

        **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10。

        :param limit: The limit of this ListInstanceConsumerGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceConsumerGroupsRequest.

        **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0。

        :return: The offset of this ListInstanceConsumerGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceConsumerGroupsRequest.

        **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0。

        :param offset: The offset of this ListInstanceConsumerGroupsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListInstanceConsumerGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
