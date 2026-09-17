# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueOperateResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'operator': 'str',
        'state': 'str',
        'operate_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'operator': 'operator',
        'state': 'state',
        'operate_time': 'operate_time'
    }

    def __init__(self, id=None, operator=None, state=None, operate_time=None):
        r"""IssueOperateResult

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 变更的工作项ID。 **取值范围**： 不涉及
        :type id: str
        :param operator: **参数解释**： 工作项变更人ID。 **取值范围**： 不涉及
        :type operator: str
        :param state: **参数解释**： 工作项的作废标识，枚举类型。 **取值范围**： - 正在工作：可正常操作的工作项 - 作废：软删除后的工作项，可在回收站恢复 - 删除：彻底删除后的工作项，无法恢复
        :type state: str
        :param operate_time: **参数解释**： 工作项变更时间。 **取值范围**： 不涉及
        :type operate_time: str
        """
        
        

        self._id = None
        self._operator = None
        self._state = None
        self._operate_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if operator is not None:
            self.operator = operator
        if state is not None:
            self.state = state
        if operate_time is not None:
            self.operate_time = operate_time

    @property
    def id(self):
        r"""Gets the id of this IssueOperateResult.

        **参数解释**： 变更的工作项ID。 **取值范围**： 不涉及

        :return: The id of this IssueOperateResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueOperateResult.

        **参数解释**： 变更的工作项ID。 **取值范围**： 不涉及

        :param id: The id of this IssueOperateResult.
        :type id: str
        """
        self._id = id

    @property
    def operator(self):
        r"""Gets the operator of this IssueOperateResult.

        **参数解释**： 工作项变更人ID。 **取值范围**： 不涉及

        :return: The operator of this IssueOperateResult.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this IssueOperateResult.

        **参数解释**： 工作项变更人ID。 **取值范围**： 不涉及

        :param operator: The operator of this IssueOperateResult.
        :type operator: str
        """
        self._operator = operator

    @property
    def state(self):
        r"""Gets the state of this IssueOperateResult.

        **参数解释**： 工作项的作废标识，枚举类型。 **取值范围**： - 正在工作：可正常操作的工作项 - 作废：软删除后的工作项，可在回收站恢复 - 删除：彻底删除后的工作项，无法恢复

        :return: The state of this IssueOperateResult.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this IssueOperateResult.

        **参数解释**： 工作项的作废标识，枚举类型。 **取值范围**： - 正在工作：可正常操作的工作项 - 作废：软删除后的工作项，可在回收站恢复 - 删除：彻底删除后的工作项，无法恢复

        :param state: The state of this IssueOperateResult.
        :type state: str
        """
        self._state = state

    @property
    def operate_time(self):
        r"""Gets the operate_time of this IssueOperateResult.

        **参数解释**： 工作项变更时间。 **取值范围**： 不涉及

        :return: The operate_time of this IssueOperateResult.
        :rtype: str
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        r"""Sets the operate_time of this IssueOperateResult.

        **参数解释**： 工作项变更时间。 **取值范围**： 不涉及

        :param operate_time: The operate_time of this IssueOperateResult.
        :type operate_time: str
        """
        self._operate_time = operate_time

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
        if not isinstance(other, IssueOperateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
