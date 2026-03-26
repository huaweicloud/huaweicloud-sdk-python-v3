# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleStoreBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'store_name': 'str',
        'action': 'str',
        'cu_num': 'int'
    }

    attribute_map = {
        'store_name': 'store_name',
        'action': 'action',
        'cu_num': 'cu_num'
    }

    def __init__(self, store_name=None, action=None, cu_num=None):
        r"""ScaleStoreBody

        The model defined in huaweicloud sdk

        :param store_name: **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type store_name: str
        :param action: **参数解释：** 变更动作。 **约束限制：** 不涉及 **取值范围：** SCALE_OUT：扩容 SCALE_IN：缩容 **默认取值：** SCALE_OUT
        :type action: str
        :param cu_num: **参数解释：** 扩容或缩容后cu规格的最终数量 **约束限制：** \&quot;action\&quot;为\&quot;SCALE_OUT\&quot;时，cu_num值要大于当前已有cu规格的数量；cu_num不能超过CU配额，如有大量需求，请提工单申请。 \&quot;action\&quot;为\&quot;SCALE_IN\&quot;时，cu_num值要小于当前已有cu规格的数量。 **取值范围：** 大于0 **默认取值：** 不涉及
        :type cu_num: int
        """
        
        

        self._store_name = None
        self._action = None
        self._cu_num = None
        self.discriminator = None

        self.store_name = store_name
        if action is not None:
            self.action = action
        self.cu_num = cu_num

    @property
    def store_name(self):
        r"""Gets the store_name of this ScaleStoreBody.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The store_name of this ScaleStoreBody.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this ScaleStoreBody.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param store_name: The store_name of this ScaleStoreBody.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def action(self):
        r"""Gets the action of this ScaleStoreBody.

        **参数解释：** 变更动作。 **约束限制：** 不涉及 **取值范围：** SCALE_OUT：扩容 SCALE_IN：缩容 **默认取值：** SCALE_OUT

        :return: The action of this ScaleStoreBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ScaleStoreBody.

        **参数解释：** 变更动作。 **约束限制：** 不涉及 **取值范围：** SCALE_OUT：扩容 SCALE_IN：缩容 **默认取值：** SCALE_OUT

        :param action: The action of this ScaleStoreBody.
        :type action: str
        """
        self._action = action

    @property
    def cu_num(self):
        r"""Gets the cu_num of this ScaleStoreBody.

        **参数解释：** 扩容或缩容后cu规格的最终数量 **约束限制：** \"action\"为\"SCALE_OUT\"时，cu_num值要大于当前已有cu规格的数量；cu_num不能超过CU配额，如有大量需求，请提工单申请。 \"action\"为\"SCALE_IN\"时，cu_num值要小于当前已有cu规格的数量。 **取值范围：** 大于0 **默认取值：** 不涉及

        :return: The cu_num of this ScaleStoreBody.
        :rtype: int
        """
        return self._cu_num

    @cu_num.setter
    def cu_num(self, cu_num):
        r"""Sets the cu_num of this ScaleStoreBody.

        **参数解释：** 扩容或缩容后cu规格的最终数量 **约束限制：** \"action\"为\"SCALE_OUT\"时，cu_num值要大于当前已有cu规格的数量；cu_num不能超过CU配额，如有大量需求，请提工单申请。 \"action\"为\"SCALE_IN\"时，cu_num值要小于当前已有cu规格的数量。 **取值范围：** 大于0 **默认取值：** 不涉及

        :param cu_num: The cu_num of this ScaleStoreBody.
        :type cu_num: int
        """
        self._cu_num = cu_num

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
        if not isinstance(other, ScaleStoreBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
