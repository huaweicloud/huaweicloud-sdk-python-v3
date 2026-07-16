# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetHyperinstanceOperationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_id': 'str',
        'operation_status': 'str',
        'operation_type': 'str',
        'operation_error': 'ServerOperationError'
    }

    attribute_map = {
        'operation_id': 'operation_id',
        'operation_status': 'operation_status',
        'operation_type': 'operation_type',
        'operation_error': 'operation_error'
    }

    def __init__(self, operation_id=None, operation_status=None, operation_type=None, operation_error=None):
        r"""GetHyperinstanceOperationResponse

        The model defined in huaweicloud sdk

        :param operation_id: **参数解释**：操作ID。 **取值范围**：长度为[8,36]个字符。
        :type operation_id: str
        :param operation_status: **参数解释**：操作状态。 **取值范围**：长度为[8,36]个字符。
        :type operation_status: str
        :param operation_type: **参数解释**：操作类型。 **取值范围**：长度为[8,36]个字符。
        :type operation_type: str
        :param operation_error: 
        :type operation_error: :class:`huaweicloudsdkmodelarts.v1.ServerOperationError`
        """
        
        super().__init__()

        self._operation_id = None
        self._operation_status = None
        self._operation_type = None
        self._operation_error = None
        self.discriminator = None

        if operation_id is not None:
            self.operation_id = operation_id
        if operation_status is not None:
            self.operation_status = operation_status
        if operation_type is not None:
            self.operation_type = operation_type
        if operation_error is not None:
            self.operation_error = operation_error

    @property
    def operation_id(self):
        r"""Gets the operation_id of this GetHyperinstanceOperationResponse.

        **参数解释**：操作ID。 **取值范围**：长度为[8,36]个字符。

        :return: The operation_id of this GetHyperinstanceOperationResponse.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        r"""Sets the operation_id of this GetHyperinstanceOperationResponse.

        **参数解释**：操作ID。 **取值范围**：长度为[8,36]个字符。

        :param operation_id: The operation_id of this GetHyperinstanceOperationResponse.
        :type operation_id: str
        """
        self._operation_id = operation_id

    @property
    def operation_status(self):
        r"""Gets the operation_status of this GetHyperinstanceOperationResponse.

        **参数解释**：操作状态。 **取值范围**：长度为[8,36]个字符。

        :return: The operation_status of this GetHyperinstanceOperationResponse.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        r"""Sets the operation_status of this GetHyperinstanceOperationResponse.

        **参数解释**：操作状态。 **取值范围**：长度为[8,36]个字符。

        :param operation_status: The operation_status of this GetHyperinstanceOperationResponse.
        :type operation_status: str
        """
        self._operation_status = operation_status

    @property
    def operation_type(self):
        r"""Gets the operation_type of this GetHyperinstanceOperationResponse.

        **参数解释**：操作类型。 **取值范围**：长度为[8,36]个字符。

        :return: The operation_type of this GetHyperinstanceOperationResponse.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this GetHyperinstanceOperationResponse.

        **参数解释**：操作类型。 **取值范围**：长度为[8,36]个字符。

        :param operation_type: The operation_type of this GetHyperinstanceOperationResponse.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def operation_error(self):
        r"""Gets the operation_error of this GetHyperinstanceOperationResponse.

        :return: The operation_error of this GetHyperinstanceOperationResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServerOperationError`
        """
        return self._operation_error

    @operation_error.setter
    def operation_error(self, operation_error):
        r"""Sets the operation_error of this GetHyperinstanceOperationResponse.

        :param operation_error: The operation_error of this GetHyperinstanceOperationResponse.
        :type operation_error: :class:`huaweicloudsdkmodelarts.v1.ServerOperationError`
        """
        self._operation_error = operation_error

    def to_dict(self):
        import warnings
        warnings.warn("GetHyperinstanceOperationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GetHyperinstanceOperationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
