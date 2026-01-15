# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiOpsRequest:

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
        'limit': 'int',
        'offset': 'int',
        'report': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'limit': 'limit',
        'offset': 'offset',
        'report': 'report'
    }

    def __init__(self, cluster_id=None, limit=None, offset=None, report=None):
        r"""ListAiOpsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 指定查询的集群ID。获取方法请参见[获取集群ID](css_03_0101.xml)。 **约束限制**： 不涉及 **取值范围**： 集群ID。 **默认取值**： 不涉及
        :type cluster_id: str
        :param limit: **参数解释**： 分页参数，列表当前分页的数量限制。默认值为10，即一次查询10个任务信息。 **约束限制**： 不涉及 **取值范围**： 1-1000 **默认取值**： 10
        :type limit: int
        :param offset: **参数解释**： 偏移量，表示从偏移量后面的计数开始查询。 **约束限制**： 不涉及 **取值范围**： 0-1000 **默认取值**： 0
        :type offset: int
        :param report: **参数解释**： 获取当前最新一份报告或历史报告 **约束限制**： 不涉及 **取值范围**： - current   仅获取当前最新一次检测报告 - history   仅获取当前历史检测报告  **默认取值**： 不涉及
        :type report: str
        """
        
        

        self._cluster_id = None
        self._limit = None
        self._offset = None
        self._report = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if report is not None:
            self.report = report

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListAiOpsRequest.

        **参数解释**： 指定查询的集群ID。获取方法请参见[获取集群ID](css_03_0101.xml)。 **约束限制**： 不涉及 **取值范围**： 集群ID。 **默认取值**： 不涉及

        :return: The cluster_id of this ListAiOpsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListAiOpsRequest.

        **参数解释**： 指定查询的集群ID。获取方法请参见[获取集群ID](css_03_0101.xml)。 **约束限制**： 不涉及 **取值范围**： 集群ID。 **默认取值**： 不涉及

        :param cluster_id: The cluster_id of this ListAiOpsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAiOpsRequest.

        **参数解释**： 分页参数，列表当前分页的数量限制。默认值为10，即一次查询10个任务信息。 **约束限制**： 不涉及 **取值范围**： 1-1000 **默认取值**： 10

        :return: The limit of this ListAiOpsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAiOpsRequest.

        **参数解释**： 分页参数，列表当前分页的数量限制。默认值为10，即一次查询10个任务信息。 **约束限制**： 不涉及 **取值范围**： 1-1000 **默认取值**： 10

        :param limit: The limit of this ListAiOpsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAiOpsRequest.

        **参数解释**： 偏移量，表示从偏移量后面的计数开始查询。 **约束限制**： 不涉及 **取值范围**： 0-1000 **默认取值**： 0

        :return: The offset of this ListAiOpsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAiOpsRequest.

        **参数解释**： 偏移量，表示从偏移量后面的计数开始查询。 **约束限制**： 不涉及 **取值范围**： 0-1000 **默认取值**： 0

        :param offset: The offset of this ListAiOpsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def report(self):
        r"""Gets the report of this ListAiOpsRequest.

        **参数解释**： 获取当前最新一份报告或历史报告 **约束限制**： 不涉及 **取值范围**： - current   仅获取当前最新一次检测报告 - history   仅获取当前历史检测报告  **默认取值**： 不涉及

        :return: The report of this ListAiOpsRequest.
        :rtype: str
        """
        return self._report

    @report.setter
    def report(self, report):
        r"""Sets the report of this ListAiOpsRequest.

        **参数解释**： 获取当前最新一份报告或历史报告 **约束限制**： 不涉及 **取值范围**： - current   仅获取当前最新一次检测报告 - history   仅获取当前历史检测报告  **默认取值**： 不涉及

        :param report: The report of this ListAiOpsRequest.
        :type report: str
        """
        self._report = report

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAiOpsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
