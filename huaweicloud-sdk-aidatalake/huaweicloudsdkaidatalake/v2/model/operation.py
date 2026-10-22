# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Operation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_type': 'str',
        'operation_result': 'str'
    }

    attribute_map = {
        'operation_type': 'operation_type',
        'operation_result': 'operation_result'
    }

    def __init__(self, operation_type=None, operation_result=None):
        r"""Operation

        The model defined in huaweicloud sdk

        :param operation_type: **参数解释**：操作类型。 **取值范围**：   - CREATE：创建。   - SCALEIN：缩容。   - SCALEOUT：扩容。   - DELETE：删除。 
        :type operation_type: str
        :param operation_result: **参数解释**：操作结果。 **取值范围**：   - EXECUTING：执行中。   - SUCCESS：操作成功。   - FAILED：操作失败。 
        :type operation_result: str
        """
        
        

        self._operation_type = None
        self._operation_result = None
        self.discriminator = None

        if operation_type is not None:
            self.operation_type = operation_type
        if operation_result is not None:
            self.operation_result = operation_result

    @property
    def operation_type(self):
        r"""Gets the operation_type of this Operation.

        **参数解释**：操作类型。 **取值范围**：   - CREATE：创建。   - SCALEIN：缩容。   - SCALEOUT：扩容。   - DELETE：删除。 

        :return: The operation_type of this Operation.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this Operation.

        **参数解释**：操作类型。 **取值范围**：   - CREATE：创建。   - SCALEIN：缩容。   - SCALEOUT：扩容。   - DELETE：删除。 

        :param operation_type: The operation_type of this Operation.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def operation_result(self):
        r"""Gets the operation_result of this Operation.

        **参数解释**：操作结果。 **取值范围**：   - EXECUTING：执行中。   - SUCCESS：操作成功。   - FAILED：操作失败。 

        :return: The operation_result of this Operation.
        :rtype: str
        """
        return self._operation_result

    @operation_result.setter
    def operation_result(self, operation_result):
        r"""Sets the operation_result of this Operation.

        **参数解释**：操作结果。 **取值范围**：   - EXECUTING：执行中。   - SUCCESS：操作成功。   - FAILED：操作失败。 

        :param operation_result: The operation_result of this Operation.
        :type operation_result: str
        """
        self._operation_result = operation_result

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
        if not isinstance(other, Operation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
