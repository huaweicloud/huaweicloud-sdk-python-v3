# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMappingFunctionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compare_list': 'list[DpeCompareFunctionDetail]',
        'operation_list': 'list[DpeOperateFunctionDetail]'
    }

    attribute_map = {
        'compare_list': 'compare_list',
        'operation_list': 'operation_list'
    }

    def __init__(self, compare_list=None, operation_list=None):
        r"""ShowMappingFunctionResponse

        The model defined in huaweicloud sdk

        :param compare_list: 比较函数信息
        :type compare_list: list[:class:`huaweicloudsdksecmaster.v1.DpeCompareFunctionDetail`]
        :param operation_list: 操作函数信息
        :type operation_list: list[:class:`huaweicloudsdksecmaster.v1.DpeOperateFunctionDetail`]
        """
        
        super().__init__()

        self._compare_list = None
        self._operation_list = None
        self.discriminator = None

        if compare_list is not None:
            self.compare_list = compare_list
        if operation_list is not None:
            self.operation_list = operation_list

    @property
    def compare_list(self):
        r"""Gets the compare_list of this ShowMappingFunctionResponse.

        比较函数信息

        :return: The compare_list of this ShowMappingFunctionResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.DpeCompareFunctionDetail`]
        """
        return self._compare_list

    @compare_list.setter
    def compare_list(self, compare_list):
        r"""Sets the compare_list of this ShowMappingFunctionResponse.

        比较函数信息

        :param compare_list: The compare_list of this ShowMappingFunctionResponse.
        :type compare_list: list[:class:`huaweicloudsdksecmaster.v1.DpeCompareFunctionDetail`]
        """
        self._compare_list = compare_list

    @property
    def operation_list(self):
        r"""Gets the operation_list of this ShowMappingFunctionResponse.

        操作函数信息

        :return: The operation_list of this ShowMappingFunctionResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.DpeOperateFunctionDetail`]
        """
        return self._operation_list

    @operation_list.setter
    def operation_list(self, operation_list):
        r"""Sets the operation_list of this ShowMappingFunctionResponse.

        操作函数信息

        :param operation_list: The operation_list of this ShowMappingFunctionResponse.
        :type operation_list: list[:class:`huaweicloudsdksecmaster.v1.DpeOperateFunctionDetail`]
        """
        self._operation_list = operation_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowMappingFunctionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowMappingFunctionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
