# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsModelTuningTaskProductsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name'
    }

    def __init__(self, task_id=None, offset=None, limit=None, name=None):
        r"""ListOpsModelTuningTaskProductsRequest

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 模型优化任务ID，标识任务的唯一标识符。获取方法请参考查询模型优化任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无
        :type task_id: str
        :param offset: **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 
        :type offset: int
        :param limit: **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。
        :type limit: int
        :param name: **参数解释：** 产物名称，用于根据产物名称关键词筛选。  **约束限制：** 选填参数，支持模糊匹配。  **取值范围：** 合法的产物名称字符串。  **默认取值：** 无
        :type name: str
        """
        
        

        self._task_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self.discriminator = None

        self.task_id = task_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name

    @property
    def task_id(self):
        r"""Gets the task_id of this ListOpsModelTuningTaskProductsRequest.

        **参数解释：** 模型优化任务ID，标识任务的唯一标识符。获取方法请参考查询模型优化任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :return: The task_id of this ListOpsModelTuningTaskProductsRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListOpsModelTuningTaskProductsRequest.

        **参数解释：** 模型优化任务ID，标识任务的唯一标识符。获取方法请参考查询模型优化任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :param task_id: The task_id of this ListOpsModelTuningTaskProductsRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def offset(self):
        r"""Gets the offset of this ListOpsModelTuningTaskProductsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :return: The offset of this ListOpsModelTuningTaskProductsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOpsModelTuningTaskProductsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :param offset: The offset of this ListOpsModelTuningTaskProductsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsModelTuningTaskProductsRequest.

        **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。

        :return: The limit of this ListOpsModelTuningTaskProductsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsModelTuningTaskProductsRequest.

        **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。

        :param limit: The limit of this ListOpsModelTuningTaskProductsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListOpsModelTuningTaskProductsRequest.

        **参数解释：** 产物名称，用于根据产物名称关键词筛选。  **约束限制：** 选填参数，支持模糊匹配。  **取值范围：** 合法的产物名称字符串。  **默认取值：** 无

        :return: The name of this ListOpsModelTuningTaskProductsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListOpsModelTuningTaskProductsRequest.

        **参数解释：** 产物名称，用于根据产物名称关键词筛选。  **约束限制：** 选填参数，支持模糊匹配。  **取值范围：** 合法的产物名称字符串。  **默认取值：** 无

        :param name: The name of this ListOpsModelTuningTaskProductsRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListOpsModelTuningTaskProductsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
