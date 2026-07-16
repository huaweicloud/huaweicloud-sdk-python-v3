# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkloadsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_name': 'str',
        'hostip': 'list[str]',
        'type': 'str',
        'status': 'str',
        'sort': 'str',
        'ascend': 'bool',
        'offset': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'pool_name': 'pool_name',
        'hostip': 'hostip',
        'type': 'type',
        'status': 'status',
        'sort': 'sort',
        'ascend': 'ascend',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, pool_name=None, hostip=None, type=None, status=None, sort=None, ascend=None, offset=None, limit=None):
        r"""ListWorkloadsRequest

        The model defined in huaweicloud sdk

        :param pool_name: **参数解释**：资源池的ID，取值自资源池详情的metadata.name字段。 **约束限制**：不涉及。 **取值范围**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为[36-63]个字符。 **默认取值**：不涉及。
        :type pool_name: str
        :param hostip: **参数解释**：节点IP地址，用于过滤在该节点上运行的workload。支持多个IP，传递多个参数或用逗号分隔. **约束限制**：指定此参数时，不支持分页（limit/offset会被忽略）。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type hostip: list[str]
        :param type: **参数解释**：根据作业类型查询资源池作业列表。 **约束限制**：不涉及。 **取值范围**：可选值如下： - train：训练作业 - infer：推理服务 - notebook：Notebook作业 - x-infer：新版推理作业 **默认取值**：不涉及。
        :type type: str
        :param status: **参数解释**：根据作业状态查询资源池作业列表。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Queue：排队中的作业。 - Pending：等待中的作业。 - Abnormal：异常的作业。 - Terminating：中止中的作业。 - Creating：创建中的作业。 - Running：运行中的作业。 - Completed：已完成的作业。 - Terminated：已终止的作业。 - Failed：运行失败的作业。 **默认取值**：不涉及。
        :type status: str
        :param sort: **参数解释**：查询资源池作业列表的排序条件。 **约束限制**：不涉及。 **取值范围**：可选值如下： - create_time：根据作业创建时间排序。 **默认取值**：不涉及。
        :type sort: str
        :param ascend: **参数解释**：指定查询资源池作业列表是否按照升序排序。 **约束限制**：需要配合sort查询参数使用。 **取值范围**：可选值如下： - true：按照升序排序。 - false：按照降序排序。 **默认取值**：false。
        :type ascend: bool
        :param offset: **参数解释**：分页查询的偏移量。 **约束限制**：不涉及。 **取值范围**：0-2147483647。 **默认取值**：0。
        :type offset: str
        :param limit: **参数解释**：分页单次查询返回的资源数量。 **约束限制**：不涉及。 **取值范围**：0 - 500。 **默认取值**：500。
        :type limit: int
        """
        
        

        self._pool_name = None
        self._hostip = None
        self._type = None
        self._status = None
        self._sort = None
        self._ascend = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.pool_name = pool_name
        if hostip is not None:
            self.hostip = hostip
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if sort is not None:
            self.sort = sort
        if ascend is not None:
            self.ascend = ascend
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def pool_name(self):
        r"""Gets the pool_name of this ListWorkloadsRequest.

        **参数解释**：资源池的ID，取值自资源池详情的metadata.name字段。 **约束限制**：不涉及。 **取值范围**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为[36-63]个字符。 **默认取值**：不涉及。

        :return: The pool_name of this ListWorkloadsRequest.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this ListWorkloadsRequest.

        **参数解释**：资源池的ID，取值自资源池详情的metadata.name字段。 **约束限制**：不涉及。 **取值范围**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为[36-63]个字符。 **默认取值**：不涉及。

        :param pool_name: The pool_name of this ListWorkloadsRequest.
        :type pool_name: str
        """
        self._pool_name = pool_name

    @property
    def hostip(self):
        r"""Gets the hostip of this ListWorkloadsRequest.

        **参数解释**：节点IP地址，用于过滤在该节点上运行的workload。支持多个IP，传递多个参数或用逗号分隔. **约束限制**：指定此参数时，不支持分页（limit/offset会被忽略）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The hostip of this ListWorkloadsRequest.
        :rtype: list[str]
        """
        return self._hostip

    @hostip.setter
    def hostip(self, hostip):
        r"""Sets the hostip of this ListWorkloadsRequest.

        **参数解释**：节点IP地址，用于过滤在该节点上运行的workload。支持多个IP，传递多个参数或用逗号分隔. **约束限制**：指定此参数时，不支持分页（limit/offset会被忽略）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param hostip: The hostip of this ListWorkloadsRequest.
        :type hostip: list[str]
        """
        self._hostip = hostip

    @property
    def type(self):
        r"""Gets the type of this ListWorkloadsRequest.

        **参数解释**：根据作业类型查询资源池作业列表。 **约束限制**：不涉及。 **取值范围**：可选值如下： - train：训练作业 - infer：推理服务 - notebook：Notebook作业 - x-infer：新版推理作业 **默认取值**：不涉及。

        :return: The type of this ListWorkloadsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListWorkloadsRequest.

        **参数解释**：根据作业类型查询资源池作业列表。 **约束限制**：不涉及。 **取值范围**：可选值如下： - train：训练作业 - infer：推理服务 - notebook：Notebook作业 - x-infer：新版推理作业 **默认取值**：不涉及。

        :param type: The type of this ListWorkloadsRequest.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ListWorkloadsRequest.

        **参数解释**：根据作业状态查询资源池作业列表。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Queue：排队中的作业。 - Pending：等待中的作业。 - Abnormal：异常的作业。 - Terminating：中止中的作业。 - Creating：创建中的作业。 - Running：运行中的作业。 - Completed：已完成的作业。 - Terminated：已终止的作业。 - Failed：运行失败的作业。 **默认取值**：不涉及。

        :return: The status of this ListWorkloadsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListWorkloadsRequest.

        **参数解释**：根据作业状态查询资源池作业列表。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Queue：排队中的作业。 - Pending：等待中的作业。 - Abnormal：异常的作业。 - Terminating：中止中的作业。 - Creating：创建中的作业。 - Running：运行中的作业。 - Completed：已完成的作业。 - Terminated：已终止的作业。 - Failed：运行失败的作业。 **默认取值**：不涉及。

        :param status: The status of this ListWorkloadsRequest.
        :type status: str
        """
        self._status = status

    @property
    def sort(self):
        r"""Gets the sort of this ListWorkloadsRequest.

        **参数解释**：查询资源池作业列表的排序条件。 **约束限制**：不涉及。 **取值范围**：可选值如下： - create_time：根据作业创建时间排序。 **默认取值**：不涉及。

        :return: The sort of this ListWorkloadsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListWorkloadsRequest.

        **参数解释**：查询资源池作业列表的排序条件。 **约束限制**：不涉及。 **取值范围**：可选值如下： - create_time：根据作业创建时间排序。 **默认取值**：不涉及。

        :param sort: The sort of this ListWorkloadsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def ascend(self):
        r"""Gets the ascend of this ListWorkloadsRequest.

        **参数解释**：指定查询资源池作业列表是否按照升序排序。 **约束限制**：需要配合sort查询参数使用。 **取值范围**：可选值如下： - true：按照升序排序。 - false：按照降序排序。 **默认取值**：false。

        :return: The ascend of this ListWorkloadsRequest.
        :rtype: bool
        """
        return self._ascend

    @ascend.setter
    def ascend(self, ascend):
        r"""Sets the ascend of this ListWorkloadsRequest.

        **参数解释**：指定查询资源池作业列表是否按照升序排序。 **约束限制**：需要配合sort查询参数使用。 **取值范围**：可选值如下： - true：按照升序排序。 - false：按照降序排序。 **默认取值**：false。

        :param ascend: The ascend of this ListWorkloadsRequest.
        :type ascend: bool
        """
        self._ascend = ascend

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkloadsRequest.

        **参数解释**：分页查询的偏移量。 **约束限制**：不涉及。 **取值范围**：0-2147483647。 **默认取值**：0。

        :return: The offset of this ListWorkloadsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkloadsRequest.

        **参数解释**：分页查询的偏移量。 **约束限制**：不涉及。 **取值范围**：0-2147483647。 **默认取值**：0。

        :param offset: The offset of this ListWorkloadsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkloadsRequest.

        **参数解释**：分页单次查询返回的资源数量。 **约束限制**：不涉及。 **取值范围**：0 - 500。 **默认取值**：500。

        :return: The limit of this ListWorkloadsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkloadsRequest.

        **参数解释**：分页单次查询返回的资源数量。 **约束限制**：不涉及。 **取值范围**：0 - 500。 **默认取值**：500。

        :param limit: The limit of this ListWorkloadsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListWorkloadsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
