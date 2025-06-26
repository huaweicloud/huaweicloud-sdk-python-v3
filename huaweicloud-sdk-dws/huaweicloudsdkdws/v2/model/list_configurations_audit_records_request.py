# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigurationsAuditRecordsRequest:

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
        'action_time': 'int',
        'filter_by': 'str',
        'filter': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'action_time': 'action_time',
        'filter_by': 'filter_by',
        'filter': 'filter',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, cluster_id=None, action_time=None, filter_by=None, filter=None, limit=None, offset=None):
        r"""ListConfigurationsAuditRecordsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param action_time: **参数解释**： 任务时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type action_time: int
        :param filter_by: **参数解释**： 过滤配置信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type filter_by: str
        :param filter: **参数解释**： 过滤内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type filter: str
        :param limit: **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10
        :type limit: int
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0
        :type offset: int
        """
        
        

        self._cluster_id = None
        self._action_time = None
        self._filter_by = None
        self._filter = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if action_time is not None:
            self.action_time = action_time
        if filter_by is not None:
            self.filter_by = filter_by
        if filter is not None:
            self.filter = filter
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :return: The cluster_id of this ListConfigurationsAuditRecordsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ListConfigurationsAuditRecordsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def action_time(self):
        r"""Gets the action_time of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 任务时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The action_time of this ListConfigurationsAuditRecordsRequest.
        :rtype: int
        """
        return self._action_time

    @action_time.setter
    def action_time(self, action_time):
        r"""Sets the action_time of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 任务时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param action_time: The action_time of this ListConfigurationsAuditRecordsRequest.
        :type action_time: int
        """
        self._action_time = action_time

    @property
    def filter_by(self):
        r"""Gets the filter_by of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 过滤配置信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The filter_by of this ListConfigurationsAuditRecordsRequest.
        :rtype: str
        """
        return self._filter_by

    @filter_by.setter
    def filter_by(self, filter_by):
        r"""Sets the filter_by of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 过滤配置信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param filter_by: The filter_by of this ListConfigurationsAuditRecordsRequest.
        :type filter_by: str
        """
        self._filter_by = filter_by

    @property
    def filter(self):
        r"""Gets the filter of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 过滤内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The filter of this ListConfigurationsAuditRecordsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 过滤内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param filter: The filter of this ListConfigurationsAuditRecordsRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def limit(self):
        r"""Gets the limit of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10

        :return: The limit of this ListConfigurationsAuditRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10

        :param limit: The limit of this ListConfigurationsAuditRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :return: The offset of this ListConfigurationsAuditRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListConfigurationsAuditRecordsRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :param offset: The offset of this ListConfigurationsAuditRecordsRequest.
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
        if not isinstance(other, ListConfigurationsAuditRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
