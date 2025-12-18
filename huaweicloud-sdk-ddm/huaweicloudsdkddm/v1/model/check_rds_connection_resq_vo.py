# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRdsConnectionResqVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rds_instance_id': 'str',
        'success': 'str',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'rds_instance_id': 'rds_instance_id',
        'success': 'success',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, rds_instance_id=None, success=None, error_code=None, error_message=None):
        r"""CheckRdsConnectionResqVO

        The model defined in huaweicloud sdk

        :param rds_instance_id: **参数解释**：  rds实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in01，长度为36个字符。  **默认取值**：  不涉及。
        :type rds_instance_id: str
        :param success: success
        :type success: str
        :param error_code: **参数解释**：  错误码。  **参数范围**：  不涉及。
        :type error_code: str
        :param error_message: **参数解释**：  错误信息。  **参数范围**：  不涉及。
        :type error_message: str
        """
        
        

        self._rds_instance_id = None
        self._success = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if rds_instance_id is not None:
            self.rds_instance_id = rds_instance_id
        if success is not None:
            self.success = success
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def rds_instance_id(self):
        r"""Gets the rds_instance_id of this CheckRdsConnectionResqVO.

        **参数解释**：  rds实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in01，长度为36个字符。  **默认取值**：  不涉及。

        :return: The rds_instance_id of this CheckRdsConnectionResqVO.
        :rtype: str
        """
        return self._rds_instance_id

    @rds_instance_id.setter
    def rds_instance_id(self, rds_instance_id):
        r"""Sets the rds_instance_id of this CheckRdsConnectionResqVO.

        **参数解释**：  rds实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in01，长度为36个字符。  **默认取值**：  不涉及。

        :param rds_instance_id: The rds_instance_id of this CheckRdsConnectionResqVO.
        :type rds_instance_id: str
        """
        self._rds_instance_id = rds_instance_id

    @property
    def success(self):
        r"""Gets the success of this CheckRdsConnectionResqVO.

        success

        :return: The success of this CheckRdsConnectionResqVO.
        :rtype: str
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this CheckRdsConnectionResqVO.

        success

        :param success: The success of this CheckRdsConnectionResqVO.
        :type success: str
        """
        self._success = success

    @property
    def error_code(self):
        r"""Gets the error_code of this CheckRdsConnectionResqVO.

        **参数解释**：  错误码。  **参数范围**：  不涉及。

        :return: The error_code of this CheckRdsConnectionResqVO.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this CheckRdsConnectionResqVO.

        **参数解释**：  错误码。  **参数范围**：  不涉及。

        :param error_code: The error_code of this CheckRdsConnectionResqVO.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this CheckRdsConnectionResqVO.

        **参数解释**：  错误信息。  **参数范围**：  不涉及。

        :return: The error_message of this CheckRdsConnectionResqVO.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this CheckRdsConnectionResqVO.

        **参数解释**：  错误信息。  **参数范围**：  不涉及。

        :param error_message: The error_message of this CheckRdsConnectionResqVO.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, CheckRdsConnectionResqVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
