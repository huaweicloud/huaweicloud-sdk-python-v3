# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluationTaskCustomLabelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'msg': 'str',
        'code': 'int',
        'data': 'list[OpsTaskCustomLabel]',
        'total': 'int'
    }

    attribute_map = {
        'msg': 'msg',
        'code': 'code',
        'data': 'data',
        'total': 'total'
    }

    def __init__(self, msg=None, code=None, data=None, total=None):
        r"""ListOpsEvaluationTaskCustomLabelsResponse

        The model defined in huaweicloud sdk

        :param msg: **参数解释：** 提示信息。 **约束限制：** 不涉及。 **取值范围：** 固定为 query succeed。 **默认取值：** 不涉及。 
        :type msg: str
        :param code: **参数解释：** 业务状态码。 **约束限制：** 不涉及。 **取值范围：** 固定为 200。 **默认取值：** 不涉及。 
        :type code: int
        :param data: **参数解释：** 自定义标签记录列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type data: list[:class:`huaweicloudsdkagentarts.v1.OpsTaskCustomLabel`]
        :param total: **参数解释：** 满足查询条件的记录总数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 **默认取值：** 不涉及。 
        :type total: int
        """
        
        super().__init__()

        self._msg = None
        self._code = None
        self._data = None
        self._total = None
        self.discriminator = None

        if msg is not None:
            self.msg = msg
        if code is not None:
            self.code = code
        if data is not None:
            self.data = data
        if total is not None:
            self.total = total

    @property
    def msg(self):
        r"""Gets the msg of this ListOpsEvaluationTaskCustomLabelsResponse.

        **参数解释：** 提示信息。 **约束限制：** 不涉及。 **取值范围：** 固定为 query succeed。 **默认取值：** 不涉及。 

        :return: The msg of this ListOpsEvaluationTaskCustomLabelsResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this ListOpsEvaluationTaskCustomLabelsResponse.

        **参数解释：** 提示信息。 **约束限制：** 不涉及。 **取值范围：** 固定为 query succeed。 **默认取值：** 不涉及。 

        :param msg: The msg of this ListOpsEvaluationTaskCustomLabelsResponse.
        :type msg: str
        """
        self._msg = msg

    @property
    def code(self):
        r"""Gets the code of this ListOpsEvaluationTaskCustomLabelsResponse.

        **参数解释：** 业务状态码。 **约束限制：** 不涉及。 **取值范围：** 固定为 200。 **默认取值：** 不涉及。 

        :return: The code of this ListOpsEvaluationTaskCustomLabelsResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListOpsEvaluationTaskCustomLabelsResponse.

        **参数解释：** 业务状态码。 **约束限制：** 不涉及。 **取值范围：** 固定为 200。 **默认取值：** 不涉及。 

        :param code: The code of this ListOpsEvaluationTaskCustomLabelsResponse.
        :type code: int
        """
        self._code = code

    @property
    def data(self):
        r"""Gets the data of this ListOpsEvaluationTaskCustomLabelsResponse.

        **参数解释：** 自定义标签记录列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The data of this ListOpsEvaluationTaskCustomLabelsResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTaskCustomLabel`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListOpsEvaluationTaskCustomLabelsResponse.

        **参数解释：** 自定义标签记录列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param data: The data of this ListOpsEvaluationTaskCustomLabelsResponse.
        :type data: list[:class:`huaweicloudsdkagentarts.v1.OpsTaskCustomLabel`]
        """
        self._data = data

    @property
    def total(self):
        r"""Gets the total of this ListOpsEvaluationTaskCustomLabelsResponse.

        **参数解释：** 满足查询条件的记录总数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 **默认取值：** 不涉及。 

        :return: The total of this ListOpsEvaluationTaskCustomLabelsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOpsEvaluationTaskCustomLabelsResponse.

        **参数解释：** 满足查询条件的记录总数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 **默认取值：** 不涉及。 

        :param total: The total of this ListOpsEvaluationTaskCustomLabelsResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsEvaluationTaskCustomLabelsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListOpsEvaluationTaskCustomLabelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
