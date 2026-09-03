# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchErrorInfo4ApiResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'error_trans_infos': 'list[ErrorTransInfo]'
    }

    attribute_map = {
        'total': 'total',
        'error_trans_infos': 'error_trans_infos'
    }

    def __init__(self, total=None, error_trans_infos=None):
        r"""SearchErrorInfo4ApiResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param error_trans_infos: binlog解析错误信息列表
        :type error_trans_infos: list[:class:`huaweicloudsdkdas.v3.ErrorTransInfo`]
        """
        
        super().__init__()

        self._total = None
        self._error_trans_infos = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if error_trans_infos is not None:
            self.error_trans_infos = error_trans_infos

    @property
    def total(self):
        r"""Gets the total of this SearchErrorInfo4ApiResponse.

        总数

        :return: The total of this SearchErrorInfo4ApiResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SearchErrorInfo4ApiResponse.

        总数

        :param total: The total of this SearchErrorInfo4ApiResponse.
        :type total: int
        """
        self._total = total

    @property
    def error_trans_infos(self):
        r"""Gets the error_trans_infos of this SearchErrorInfo4ApiResponse.

        binlog解析错误信息列表

        :return: The error_trans_infos of this SearchErrorInfo4ApiResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ErrorTransInfo`]
        """
        return self._error_trans_infos

    @error_trans_infos.setter
    def error_trans_infos(self, error_trans_infos):
        r"""Sets the error_trans_infos of this SearchErrorInfo4ApiResponse.

        binlog解析错误信息列表

        :param error_trans_infos: The error_trans_infos of this SearchErrorInfo4ApiResponse.
        :type error_trans_infos: list[:class:`huaweicloudsdkdas.v3.ErrorTransInfo`]
        """
        self._error_trans_infos = error_trans_infos

    def to_dict(self):
        import warnings
        warnings.warn("SearchErrorInfo4ApiResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SearchErrorInfo4ApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
