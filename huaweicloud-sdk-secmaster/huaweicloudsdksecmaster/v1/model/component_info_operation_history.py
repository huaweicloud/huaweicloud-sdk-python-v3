# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentInfoOperationHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_name': 'str',
        'operation_time': 'str'
    }

    attribute_map = {
        'operation_name': 'operation_name',
        'operation_time': 'operation_time'
    }

    def __init__(self, operation_name=None, operation_time=None):
        r"""ComponentInfoOperationHistory

        The model defined in huaweicloud sdk

        :param operation_name: 操作
        :type operation_name: str
        :param operation_time: 时间点
        :type operation_time: str
        """
        
        

        self._operation_name = None
        self._operation_time = None
        self.discriminator = None

        if operation_name is not None:
            self.operation_name = operation_name
        if operation_time is not None:
            self.operation_time = operation_time

    @property
    def operation_name(self):
        r"""Gets the operation_name of this ComponentInfoOperationHistory.

        操作

        :return: The operation_name of this ComponentInfoOperationHistory.
        :rtype: str
        """
        return self._operation_name

    @operation_name.setter
    def operation_name(self, operation_name):
        r"""Sets the operation_name of this ComponentInfoOperationHistory.

        操作

        :param operation_name: The operation_name of this ComponentInfoOperationHistory.
        :type operation_name: str
        """
        self._operation_name = operation_name

    @property
    def operation_time(self):
        r"""Gets the operation_time of this ComponentInfoOperationHistory.

        时间点

        :return: The operation_time of this ComponentInfoOperationHistory.
        :rtype: str
        """
        return self._operation_time

    @operation_time.setter
    def operation_time(self, operation_time):
        r"""Sets the operation_time of this ComponentInfoOperationHistory.

        时间点

        :param operation_time: The operation_time of this ComponentInfoOperationHistory.
        :type operation_time: str
        """
        self._operation_time = operation_time

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
        if not isinstance(other, ComponentInfoOperationHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
