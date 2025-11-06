# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVaultSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'list_vault_summary': 'list[BccVaultDaySummary]',
        'count': 'int'
    }

    attribute_map = {
        'list_vault_summary': 'list_vault_summary',
        'count': 'count'
    }

    def __init__(self, list_vault_summary=None, count=None):
        r"""ShowVaultSummaryResponse

        The model defined in huaweicloud sdk

        :param list_vault_summary: 列举vault的summary
        :type list_vault_summary: list[:class:`huaweicloudsdkbcc.v1.BccVaultDaySummary`]
        :param count: 存储库数量
        :type count: int
        """
        
        super().__init__()

        self._list_vault_summary = None
        self._count = None
        self.discriminator = None

        if list_vault_summary is not None:
            self.list_vault_summary = list_vault_summary
        if count is not None:
            self.count = count

    @property
    def list_vault_summary(self):
        r"""Gets the list_vault_summary of this ShowVaultSummaryResponse.

        列举vault的summary

        :return: The list_vault_summary of this ShowVaultSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.BccVaultDaySummary`]
        """
        return self._list_vault_summary

    @list_vault_summary.setter
    def list_vault_summary(self, list_vault_summary):
        r"""Sets the list_vault_summary of this ShowVaultSummaryResponse.

        列举vault的summary

        :param list_vault_summary: The list_vault_summary of this ShowVaultSummaryResponse.
        :type list_vault_summary: list[:class:`huaweicloudsdkbcc.v1.BccVaultDaySummary`]
        """
        self._list_vault_summary = list_vault_summary

    @property
    def count(self):
        r"""Gets the count of this ShowVaultSummaryResponse.

        存储库数量

        :return: The count of this ShowVaultSummaryResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowVaultSummaryResponse.

        存储库数量

        :param count: The count of this ShowVaultSummaryResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ShowVaultSummaryResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowVaultSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
