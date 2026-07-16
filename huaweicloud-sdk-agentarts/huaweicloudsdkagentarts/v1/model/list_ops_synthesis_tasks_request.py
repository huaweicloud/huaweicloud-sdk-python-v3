# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsSynthesisTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'status': 'status',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, status=None, name=None, offset=None, limit=None):
        r"""ListOpsSynthesisTasksRequest

        The model defined in huaweicloud sdk

        :param status: **参数解释：** 任务状态过滤条件。用于筛选处于特定生命周期阶段的合成任务。 **约束限制：** 不涉及。 **取值范围：** - &#x60;pending&#x60;: 等待中 - &#x60;running&#x60;: 运行中 - &#x60;completed&#x60;: 已完成 - &#x60;failed&#x60;: 失败 - &#x60;stopped&#x60;: 已停止 **默认取值：** 不涉及。
        :type status: str
        :param name: **参数解释：** 任务名称检索字段。支持根据创建任务时自定义的名称进行筛选。 **约束限制：** 支持模糊匹配，字符串长度限制为0到100个字符。 **取值范围：** 0到100字符。 **默认取值：** 不涉及。
        :type name: str
        :param offset: **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 
        :type offset: int
        :param limit: **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 
        :type limit: int
        """
        
        

        self._status = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def status(self):
        r"""Gets the status of this ListOpsSynthesisTasksRequest.

        **参数解释：** 任务状态过滤条件。用于筛选处于特定生命周期阶段的合成任务。 **约束限制：** 不涉及。 **取值范围：** - `pending`: 等待中 - `running`: 运行中 - `completed`: 已完成 - `failed`: 失败 - `stopped`: 已停止 **默认取值：** 不涉及。

        :return: The status of this ListOpsSynthesisTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListOpsSynthesisTasksRequest.

        **参数解释：** 任务状态过滤条件。用于筛选处于特定生命周期阶段的合成任务。 **约束限制：** 不涉及。 **取值范围：** - `pending`: 等待中 - `running`: 运行中 - `completed`: 已完成 - `failed`: 失败 - `stopped`: 已停止 **默认取值：** 不涉及。

        :param status: The status of this ListOpsSynthesisTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ListOpsSynthesisTasksRequest.

        **参数解释：** 任务名称检索字段。支持根据创建任务时自定义的名称进行筛选。 **约束限制：** 支持模糊匹配，字符串长度限制为0到100个字符。 **取值范围：** 0到100字符。 **默认取值：** 不涉及。

        :return: The name of this ListOpsSynthesisTasksRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListOpsSynthesisTasksRequest.

        **参数解释：** 任务名称检索字段。支持根据创建任务时自定义的名称进行筛选。 **约束限制：** 支持模糊匹配，字符串长度限制为0到100个字符。 **取值范围：** 0到100字符。 **默认取值：** 不涉及。

        :param name: The name of this ListOpsSynthesisTasksRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListOpsSynthesisTasksRequest.

        **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 

        :return: The offset of this ListOpsSynthesisTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOpsSynthesisTasksRequest.

        **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 

        :param offset: The offset of this ListOpsSynthesisTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsSynthesisTasksRequest.

        **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 

        :return: The limit of this ListOpsSynthesisTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsSynthesisTasksRequest.

        **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 

        :param limit: The limit of this ListOpsSynthesisTasksRequest.
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
        if not isinstance(other, ListOpsSynthesisTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
