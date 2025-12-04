# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPackLogInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'pack_log_infos': 'list[PackLogInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'pack_log_infos': 'pack_log_infos'
    }

    def __init__(self, total_count=None, pack_log_infos=None):
        r"""ListPackLogInfosResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释**：  binlog合并下载文件数量。  **约束限制**：  不涉及。
        :type total_count: int
        :param pack_log_infos: **参数解释**：  binlog合并下载文件信息。  **约束限制**：  不涉及。
        :type pack_log_infos: list[:class:`huaweicloudsdkrds.v3.PackLogInfo`]
        """
        
        super().__init__()

        self._total_count = None
        self._pack_log_infos = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if pack_log_infos is not None:
            self.pack_log_infos = pack_log_infos

    @property
    def total_count(self):
        r"""Gets the total_count of this ListPackLogInfosResponse.

        **参数解释**：  binlog合并下载文件数量。  **约束限制**：  不涉及。

        :return: The total_count of this ListPackLogInfosResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListPackLogInfosResponse.

        **参数解释**：  binlog合并下载文件数量。  **约束限制**：  不涉及。

        :param total_count: The total_count of this ListPackLogInfosResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def pack_log_infos(self):
        r"""Gets the pack_log_infos of this ListPackLogInfosResponse.

        **参数解释**：  binlog合并下载文件信息。  **约束限制**：  不涉及。

        :return: The pack_log_infos of this ListPackLogInfosResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PackLogInfo`]
        """
        return self._pack_log_infos

    @pack_log_infos.setter
    def pack_log_infos(self, pack_log_infos):
        r"""Sets the pack_log_infos of this ListPackLogInfosResponse.

        **参数解释**：  binlog合并下载文件信息。  **约束限制**：  不涉及。

        :param pack_log_infos: The pack_log_infos of this ListPackLogInfosResponse.
        :type pack_log_infos: list[:class:`huaweicloudsdkrds.v3.PackLogInfo`]
        """
        self._pack_log_infos = pack_log_infos

    def to_dict(self):
        import warnings
        warnings.warn("ListPackLogInfosResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListPackLogInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
