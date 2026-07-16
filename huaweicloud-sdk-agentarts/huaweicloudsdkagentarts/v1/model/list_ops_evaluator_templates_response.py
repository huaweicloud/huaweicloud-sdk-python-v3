# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_templates': 'list[ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates]',
        'total': 'int',
        'code': 'int',
        'msg': 'str'
    }

    attribute_map = {
        'evaluator_templates': 'evaluator_templates',
        'total': 'total',
        'code': 'code',
        'msg': 'msg'
    }

    def __init__(self, evaluator_templates=None, total=None, code=None, msg=None):
        r"""ListOpsEvaluatorTemplatesResponse

        The model defined in huaweicloud sdk

        :param evaluator_templates: **参数解释：** 评估器模板列表包含获取到的所有符合条件的评估器模板数据，用于展示和选择。 **取值范围：** 评估器模板对象数组。 
        :type evaluator_templates: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates`]
        :param total: **参数解释：** 符合条件的模板总数。 **取值范围：** 0到2,147,483,647。 
        :type total: int
        :param code: **参数解释：** API执行状态码。 **取值范围：** 32位整数。 
        :type code: int
        :param msg: **参数解释：** 响应状态描述信息。 **取值范围：** 不涉及。 
        :type msg: str
        """
        
        super().__init__()

        self._evaluator_templates = None
        self._total = None
        self._code = None
        self._msg = None
        self.discriminator = None

        if evaluator_templates is not None:
            self.evaluator_templates = evaluator_templates
        if total is not None:
            self.total = total
        if code is not None:
            self.code = code
        if msg is not None:
            self.msg = msg

    @property
    def evaluator_templates(self):
        r"""Gets the evaluator_templates of this ListOpsEvaluatorTemplatesResponse.

        **参数解释：** 评估器模板列表包含获取到的所有符合条件的评估器模板数据，用于展示和选择。 **取值范围：** 评估器模板对象数组。 

        :return: The evaluator_templates of this ListOpsEvaluatorTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates`]
        """
        return self._evaluator_templates

    @evaluator_templates.setter
    def evaluator_templates(self, evaluator_templates):
        r"""Sets the evaluator_templates of this ListOpsEvaluatorTemplatesResponse.

        **参数解释：** 评估器模板列表包含获取到的所有符合条件的评估器模板数据，用于展示和选择。 **取值范围：** 评估器模板对象数组。 

        :param evaluator_templates: The evaluator_templates of this ListOpsEvaluatorTemplatesResponse.
        :type evaluator_templates: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorTemplates`]
        """
        self._evaluator_templates = evaluator_templates

    @property
    def total(self):
        r"""Gets the total of this ListOpsEvaluatorTemplatesResponse.

        **参数解释：** 符合条件的模板总数。 **取值范围：** 0到2,147,483,647。 

        :return: The total of this ListOpsEvaluatorTemplatesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOpsEvaluatorTemplatesResponse.

        **参数解释：** 符合条件的模板总数。 **取值范围：** 0到2,147,483,647。 

        :param total: The total of this ListOpsEvaluatorTemplatesResponse.
        :type total: int
        """
        self._total = total

    @property
    def code(self):
        r"""Gets the code of this ListOpsEvaluatorTemplatesResponse.

        **参数解释：** API执行状态码。 **取值范围：** 32位整数。 

        :return: The code of this ListOpsEvaluatorTemplatesResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListOpsEvaluatorTemplatesResponse.

        **参数解释：** API执行状态码。 **取值范围：** 32位整数。 

        :param code: The code of this ListOpsEvaluatorTemplatesResponse.
        :type code: int
        """
        self._code = code

    @property
    def msg(self):
        r"""Gets the msg of this ListOpsEvaluatorTemplatesResponse.

        **参数解释：** 响应状态描述信息。 **取值范围：** 不涉及。 

        :return: The msg of this ListOpsEvaluatorTemplatesResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this ListOpsEvaluatorTemplatesResponse.

        **参数解释：** 响应状态描述信息。 **取值范围：** 不涉及。 

        :param msg: The msg of this ListOpsEvaluatorTemplatesResponse.
        :type msg: str
        """
        self._msg = msg

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsEvaluatorTemplatesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOpsEvaluatorTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
