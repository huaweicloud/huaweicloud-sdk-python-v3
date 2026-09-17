# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluationModelResponse(SdkResponse):

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
        'model': 'Model'
    }

    attribute_map = {
        'msg': 'msg',
        'code': 'code',
        'model': 'model'
    }

    def __init__(self, msg=None, code=None, model=None):
        r"""ShowOpsEvaluationModelResponse

        The model defined in huaweicloud sdk

        :param msg: **参数解释：** 接口返回的提示信息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。
        :type msg: str
        :param code: **参数解释：** 接口返回的状态码。 **约束限制：** 不涉及。 **取值范围：** 不涉及。
        :type code: int
        :param model: 
        :type model: :class:`huaweicloudsdkagentarts.v1.Model`
        """
        
        super().__init__()

        self._msg = None
        self._code = None
        self._model = None
        self.discriminator = None

        if msg is not None:
            self.msg = msg
        if code is not None:
            self.code = code
        if model is not None:
            self.model = model

    @property
    def msg(self):
        r"""Gets the msg of this ShowOpsEvaluationModelResponse.

        **参数解释：** 接口返回的提示信息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :return: The msg of this ShowOpsEvaluationModelResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this ShowOpsEvaluationModelResponse.

        **参数解释：** 接口返回的提示信息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :param msg: The msg of this ShowOpsEvaluationModelResponse.
        :type msg: str
        """
        self._msg = msg

    @property
    def code(self):
        r"""Gets the code of this ShowOpsEvaluationModelResponse.

        **参数解释：** 接口返回的状态码。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :return: The code of this ShowOpsEvaluationModelResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowOpsEvaluationModelResponse.

        **参数解释：** 接口返回的状态码。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :param code: The code of this ShowOpsEvaluationModelResponse.
        :type code: int
        """
        self._code = code

    @property
    def model(self):
        r"""Gets the model of this ShowOpsEvaluationModelResponse.

        :return: The model of this ShowOpsEvaluationModelResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.Model`
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this ShowOpsEvaluationModelResponse.

        :param model: The model of this ShowOpsEvaluationModelResponse.
        :type model: :class:`huaweicloudsdkagentarts.v1.Model`
        """
        self._model = model

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsEvaluationModelResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsEvaluationModelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
