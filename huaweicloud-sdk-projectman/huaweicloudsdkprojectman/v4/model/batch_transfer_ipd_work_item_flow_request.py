# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchTransferIpdWorkItemFlowRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'is_recover': 'bool',
        'body': 'WorkItemFlowVO'
    }

    attribute_map = {
        'project_id': 'project_id',
        'is_recover': 'is_recover',
        'body': 'body'
    }

    def __init__(self, project_id=None, is_recover=None, body=None):
        r"""BatchTransferIpdWorkItemFlowRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param is_recover: **参数解释**： 是否覆盖对应字段。 **约束限制**： 不涉及 **取值范围**： true:本开关开启时，当前弹窗的相应字段值将覆盖全部所选工作项的对应字段值。 false:本开关关闭时，除「当前责任人」之外，所选工作项的对应字段如果已经有值，将保持原状，不会被当前弹窗的相应字段值覆盖。 **默认取值**： false。
        :type is_recover: bool
        :param body: Body of the BatchTransferIpdWorkItemFlowRequest
        :type body: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowVO`
        """
        
        

        self._project_id = None
        self._is_recover = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        if is_recover is not None:
            self.is_recover = is_recover
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this BatchTransferIpdWorkItemFlowRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this BatchTransferIpdWorkItemFlowRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BatchTransferIpdWorkItemFlowRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this BatchTransferIpdWorkItemFlowRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def is_recover(self):
        r"""Gets the is_recover of this BatchTransferIpdWorkItemFlowRequest.

        **参数解释**： 是否覆盖对应字段。 **约束限制**： 不涉及 **取值范围**： true:本开关开启时，当前弹窗的相应字段值将覆盖全部所选工作项的对应字段值。 false:本开关关闭时，除「当前责任人」之外，所选工作项的对应字段如果已经有值，将保持原状，不会被当前弹窗的相应字段值覆盖。 **默认取值**： false。

        :return: The is_recover of this BatchTransferIpdWorkItemFlowRequest.
        :rtype: bool
        """
        return self._is_recover

    @is_recover.setter
    def is_recover(self, is_recover):
        r"""Sets the is_recover of this BatchTransferIpdWorkItemFlowRequest.

        **参数解释**： 是否覆盖对应字段。 **约束限制**： 不涉及 **取值范围**： true:本开关开启时，当前弹窗的相应字段值将覆盖全部所选工作项的对应字段值。 false:本开关关闭时，除「当前责任人」之外，所选工作项的对应字段如果已经有值，将保持原状，不会被当前弹窗的相应字段值覆盖。 **默认取值**： false。

        :param is_recover: The is_recover of this BatchTransferIpdWorkItemFlowRequest.
        :type is_recover: bool
        """
        self._is_recover = is_recover

    @property
    def body(self):
        r"""Gets the body of this BatchTransferIpdWorkItemFlowRequest.

        :return: The body of this BatchTransferIpdWorkItemFlowRequest.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowVO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchTransferIpdWorkItemFlowRequest.

        :param body: The body of this BatchTransferIpdWorkItemFlowRequest.
        :type body: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowVO`
        """
        self._body = body

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
        if not isinstance(other, BatchTransferIpdWorkItemFlowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
