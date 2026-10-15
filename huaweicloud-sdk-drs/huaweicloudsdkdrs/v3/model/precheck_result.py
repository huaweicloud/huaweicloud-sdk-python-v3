# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrecheckResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item': 'str',
        'result': 'str',
        'failed_reason': 'str',
        'data': 'str',
        'raw_error_msg': 'str',
        'group': 'str',
        'failed_sub_jobs': 'list[PrecheckFailSubJobVO]'
    }

    attribute_map = {
        'item': 'item',
        'result': 'result',
        'failed_reason': 'failed_reason',
        'data': 'data',
        'raw_error_msg': 'raw_error_msg',
        'group': 'group',
        'failed_sub_jobs': 'failed_sub_jobs'
    }

    def __init__(self, item=None, result=None, failed_reason=None, data=None, raw_error_msg=None, group=None, failed_sub_jobs=None):
        r"""PrecheckResult

        The model defined in huaweicloud sdk

        :param item: **参数解释**：  预检查的具体检查项名称，用于标识预检查中执行的具体检查项目。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type item: str
        :param result: **参数解释**：  预检查项的检查结果，表示该检查项是否通过。  **约束限制**：  不涉及。  **取值范围**：  - PASSED：通过 - ALARM：告警 - FAILED：失败  **默认取值**：  不涉及
        :type result: str
        :param failed_reason: **参数解释**：  预检查项的失败原因，当检查结果为FAILED或ALARM时返回的具体失败描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type failed_reason: str
        :param data: **参数解释**：  预检查项的加密数据，包含检查项的详细检测数据，以JSON格式加密返回。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type data: str
        :param raw_error_msg: **参数解释**：  原始错误信息，预检查过程中产生的原始错误描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type raw_error_msg: str
        :param group: **参数解释**：  检查项分组，用于将预检查项按类别归类展示。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type group: str
        :param failed_sub_jobs: **参数解释**：  失败的子任务信息集合，包含预检查中失败的子任务详情，详情请参见PrecheckFailSubJobVO对象定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type failed_sub_jobs: list[:class:`huaweicloudsdkdrs.v3.PrecheckFailSubJobVO`]
        """
        
        

        self._item = None
        self._result = None
        self._failed_reason = None
        self._data = None
        self._raw_error_msg = None
        self._group = None
        self._failed_sub_jobs = None
        self.discriminator = None

        if item is not None:
            self.item = item
        if result is not None:
            self.result = result
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if data is not None:
            self.data = data
        if raw_error_msg is not None:
            self.raw_error_msg = raw_error_msg
        if group is not None:
            self.group = group
        if failed_sub_jobs is not None:
            self.failed_sub_jobs = failed_sub_jobs

    @property
    def item(self):
        r"""Gets the item of this PrecheckResult.

        **参数解释**：  预检查的具体检查项名称，用于标识预检查中执行的具体检查项目。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The item of this PrecheckResult.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this PrecheckResult.

        **参数解释**：  预检查的具体检查项名称，用于标识预检查中执行的具体检查项目。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param item: The item of this PrecheckResult.
        :type item: str
        """
        self._item = item

    @property
    def result(self):
        r"""Gets the result of this PrecheckResult.

        **参数解释**：  预检查项的检查结果，表示该检查项是否通过。  **约束限制**：  不涉及。  **取值范围**：  - PASSED：通过 - ALARM：告警 - FAILED：失败  **默认取值**：  不涉及

        :return: The result of this PrecheckResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this PrecheckResult.

        **参数解释**：  预检查项的检查结果，表示该检查项是否通过。  **约束限制**：  不涉及。  **取值范围**：  - PASSED：通过 - ALARM：告警 - FAILED：失败  **默认取值**：  不涉及

        :param result: The result of this PrecheckResult.
        :type result: str
        """
        self._result = result

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this PrecheckResult.

        **参数解释**：  预检查项的失败原因，当检查结果为FAILED或ALARM时返回的具体失败描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The failed_reason of this PrecheckResult.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this PrecheckResult.

        **参数解释**：  预检查项的失败原因，当检查结果为FAILED或ALARM时返回的具体失败描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param failed_reason: The failed_reason of this PrecheckResult.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def data(self):
        r"""Gets the data of this PrecheckResult.

        **参数解释**：  预检查项的加密数据，包含检查项的详细检测数据，以JSON格式加密返回。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The data of this PrecheckResult.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this PrecheckResult.

        **参数解释**：  预检查项的加密数据，包含检查项的详细检测数据，以JSON格式加密返回。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param data: The data of this PrecheckResult.
        :type data: str
        """
        self._data = data

    @property
    def raw_error_msg(self):
        r"""Gets the raw_error_msg of this PrecheckResult.

        **参数解释**：  原始错误信息，预检查过程中产生的原始错误描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The raw_error_msg of this PrecheckResult.
        :rtype: str
        """
        return self._raw_error_msg

    @raw_error_msg.setter
    def raw_error_msg(self, raw_error_msg):
        r"""Sets the raw_error_msg of this PrecheckResult.

        **参数解释**：  原始错误信息，预检查过程中产生的原始错误描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param raw_error_msg: The raw_error_msg of this PrecheckResult.
        :type raw_error_msg: str
        """
        self._raw_error_msg = raw_error_msg

    @property
    def group(self):
        r"""Gets the group of this PrecheckResult.

        **参数解释**：  检查项分组，用于将预检查项按类别归类展示。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The group of this PrecheckResult.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this PrecheckResult.

        **参数解释**：  检查项分组，用于将预检查项按类别归类展示。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param group: The group of this PrecheckResult.
        :type group: str
        """
        self._group = group

    @property
    def failed_sub_jobs(self):
        r"""Gets the failed_sub_jobs of this PrecheckResult.

        **参数解释**：  失败的子任务信息集合，包含预检查中失败的子任务详情，详情请参见PrecheckFailSubJobVO对象定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The failed_sub_jobs of this PrecheckResult.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.PrecheckFailSubJobVO`]
        """
        return self._failed_sub_jobs

    @failed_sub_jobs.setter
    def failed_sub_jobs(self, failed_sub_jobs):
        r"""Sets the failed_sub_jobs of this PrecheckResult.

        **参数解释**：  失败的子任务信息集合，包含预检查中失败的子任务详情，详情请参见PrecheckFailSubJobVO对象定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param failed_sub_jobs: The failed_sub_jobs of this PrecheckResult.
        :type failed_sub_jobs: list[:class:`huaweicloudsdkdrs.v3.PrecheckFailSubJobVO`]
        """
        self._failed_sub_jobs = failed_sub_jobs

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
        if not isinstance(other, PrecheckResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
