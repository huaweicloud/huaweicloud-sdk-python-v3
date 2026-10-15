# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPreCheckResp:

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
        'precheck_id': 'str',
        'status': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'id': 'id',
        'precheck_id': 'precheck_id',
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, id=None, precheck_id=None, status=None, error_code=None, error_msg=None):
        r"""PostPreCheckResp

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  任务ID，用于唯一标识一个数据复制任务，在查询、修改、删除等操作中作为任务的识别凭证。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及
        :type id: str
        :param precheck_id: **参数解释**：  预检查后返回的ID，可用于查询预检查结果。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及
        :type precheck_id: str
        :param status: **参数解释**：  预检查结果状态，表示预检查是否通过。  **约束限制**：  不涉及。  **取值范围**：  - success：预检查成功 - failed：预检查失败  **默认取值**：  不涉及
        :type status: str
        :param error_code: **参数解释**：  错误码，当预检查失败时返回的错误代码。  **约束限制**：  不涉及。  **取值范围**：  格式为DRS.XXXXXX。  **默认取值**：  不涉及
        :type error_code: str
        :param error_msg: **参数解释**：  错误详细信息，当预检查失败时返回的具体错误描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type error_msg: str
        """
        
        

        self._id = None
        self._precheck_id = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if precheck_id is not None:
            self.precheck_id = precheck_id
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def id(self):
        r"""Gets the id of this PostPreCheckResp.

        **参数解释**：  任务ID，用于唯一标识一个数据复制任务，在查询、修改、删除等操作中作为任务的识别凭证。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及

        :return: The id of this PostPreCheckResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PostPreCheckResp.

        **参数解释**：  任务ID，用于唯一标识一个数据复制任务，在查询、修改、删除等操作中作为任务的识别凭证。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及

        :param id: The id of this PostPreCheckResp.
        :type id: str
        """
        self._id = id

    @property
    def precheck_id(self):
        r"""Gets the precheck_id of this PostPreCheckResp.

        **参数解释**：  预检查后返回的ID，可用于查询预检查结果。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及

        :return: The precheck_id of this PostPreCheckResp.
        :rtype: str
        """
        return self._precheck_id

    @precheck_id.setter
    def precheck_id(self, precheck_id):
        r"""Sets the precheck_id of this PostPreCheckResp.

        **参数解释**：  预检查后返回的ID，可用于查询预检查结果。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及

        :param precheck_id: The precheck_id of this PostPreCheckResp.
        :type precheck_id: str
        """
        self._precheck_id = precheck_id

    @property
    def status(self):
        r"""Gets the status of this PostPreCheckResp.

        **参数解释**：  预检查结果状态，表示预检查是否通过。  **约束限制**：  不涉及。  **取值范围**：  - success：预检查成功 - failed：预检查失败  **默认取值**：  不涉及

        :return: The status of this PostPreCheckResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PostPreCheckResp.

        **参数解释**：  预检查结果状态，表示预检查是否通过。  **约束限制**：  不涉及。  **取值范围**：  - success：预检查成功 - failed：预检查失败  **默认取值**：  不涉及

        :param status: The status of this PostPreCheckResp.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        r"""Gets the error_code of this PostPreCheckResp.

        **参数解释**：  错误码，当预检查失败时返回的错误代码。  **约束限制**：  不涉及。  **取值范围**：  格式为DRS.XXXXXX。  **默认取值**：  不涉及

        :return: The error_code of this PostPreCheckResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this PostPreCheckResp.

        **参数解释**：  错误码，当预检查失败时返回的错误代码。  **约束限制**：  不涉及。  **取值范围**：  格式为DRS.XXXXXX。  **默认取值**：  不涉及

        :param error_code: The error_code of this PostPreCheckResp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this PostPreCheckResp.

        **参数解释**：  错误详细信息，当预检查失败时返回的具体错误描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The error_msg of this PostPreCheckResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this PostPreCheckResp.

        **参数解释**：  错误详细信息，当预检查失败时返回的具体错误描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param error_msg: The error_msg of this PostPreCheckResp.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, PostPreCheckResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
