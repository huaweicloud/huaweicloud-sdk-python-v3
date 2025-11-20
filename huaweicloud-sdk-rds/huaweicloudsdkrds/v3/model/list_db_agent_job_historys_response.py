# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbAgentJobHistorysResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'historys': 'list[ListDbAgentJobHistorysResult]',
        'total_count': 'int'
    }

    attribute_map = {
        'historys': 'historys',
        'total_count': 'total_count'
    }

    def __init__(self, historys=None, total_count=None):
        r"""ListDbAgentJobHistorysResponse

        The model defined in huaweicloud sdk

        :param historys: 执行历史列表。
        :type historys: list[:class:`huaweicloudsdkrds.v3.ListDbAgentJobHistorysResult`]
        :param total_count: 执行历史总数。
        :type total_count: int
        """
        
        super().__init__()

        self._historys = None
        self._total_count = None
        self.discriminator = None

        if historys is not None:
            self.historys = historys
        if total_count is not None:
            self.total_count = total_count

    @property
    def historys(self):
        r"""Gets the historys of this ListDbAgentJobHistorysResponse.

        执行历史列表。

        :return: The historys of this ListDbAgentJobHistorysResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ListDbAgentJobHistorysResult`]
        """
        return self._historys

    @historys.setter
    def historys(self, historys):
        r"""Sets the historys of this ListDbAgentJobHistorysResponse.

        执行历史列表。

        :param historys: The historys of this ListDbAgentJobHistorysResponse.
        :type historys: list[:class:`huaweicloudsdkrds.v3.ListDbAgentJobHistorysResult`]
        """
        self._historys = historys

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDbAgentJobHistorysResponse.

        执行历史总数。

        :return: The total_count of this ListDbAgentJobHistorysResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDbAgentJobHistorysResponse.

        执行历史总数。

        :param total_count: The total_count of this ListDbAgentJobHistorysResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ListDbAgentJobHistorysResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListDbAgentJobHistorysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
