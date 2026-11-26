# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckPermissionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_result': 'bool',
        'error_message': 'str',
        'data_filters': 'list[str]',
        'data_masks': 'list[DataMaskInfo]'
    }

    attribute_map = {
        'check_result': 'check_result',
        'error_message': 'error_message',
        'data_filters': 'data_filters',
        'data_masks': 'data_masks'
    }

    def __init__(self, check_result=None, error_message=None, data_filters=None, data_masks=None):
        r"""CheckPermissionResult

        The model defined in huaweicloud sdk

        :param check_result: 对应输入策略的检查结果
        :type check_result: bool
        :param error_message: 错误信息
        :type error_message: str
        :param data_filters: 行过滤条件列表。
        :type data_filters: list[str]
        :param data_masks: 列掩码条件列表。
        :type data_masks: list[:class:`huaweicloudsdklakeformation.v1.DataMaskInfo`]
        """
        
        

        self._check_result = None
        self._error_message = None
        self._data_filters = None
        self._data_masks = None
        self.discriminator = None

        self.check_result = check_result
        if error_message is not None:
            self.error_message = error_message
        if data_filters is not None:
            self.data_filters = data_filters
        if data_masks is not None:
            self.data_masks = data_masks

    @property
    def check_result(self):
        r"""Gets the check_result of this CheckPermissionResult.

        对应输入策略的检查结果

        :return: The check_result of this CheckPermissionResult.
        :rtype: bool
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        r"""Sets the check_result of this CheckPermissionResult.

        对应输入策略的检查结果

        :param check_result: The check_result of this CheckPermissionResult.
        :type check_result: bool
        """
        self._check_result = check_result

    @property
    def error_message(self):
        r"""Gets the error_message of this CheckPermissionResult.

        错误信息

        :return: The error_message of this CheckPermissionResult.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this CheckPermissionResult.

        错误信息

        :param error_message: The error_message of this CheckPermissionResult.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def data_filters(self):
        r"""Gets the data_filters of this CheckPermissionResult.

        行过滤条件列表。

        :return: The data_filters of this CheckPermissionResult.
        :rtype: list[str]
        """
        return self._data_filters

    @data_filters.setter
    def data_filters(self, data_filters):
        r"""Sets the data_filters of this CheckPermissionResult.

        行过滤条件列表。

        :param data_filters: The data_filters of this CheckPermissionResult.
        :type data_filters: list[str]
        """
        self._data_filters = data_filters

    @property
    def data_masks(self):
        r"""Gets the data_masks of this CheckPermissionResult.

        列掩码条件列表。

        :return: The data_masks of this CheckPermissionResult.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.DataMaskInfo`]
        """
        return self._data_masks

    @data_masks.setter
    def data_masks(self, data_masks):
        r"""Sets the data_masks of this CheckPermissionResult.

        列掩码条件列表。

        :param data_masks: The data_masks of this CheckPermissionResult.
        :type data_masks: list[:class:`huaweicloudsdklakeformation.v1.DataMaskInfo`]
        """
        self._data_masks = data_masks

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
        if not isinstance(other, CheckPermissionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
