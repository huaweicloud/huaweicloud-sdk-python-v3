# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTmlogInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tmlogs': 'list[TmlogInfo]',
        'total': 'int'
    }

    attribute_map = {
        'tmlogs': 'tmlogs',
        'total': 'total'
    }

    def __init__(self, tmlogs=None, total=None):
        r"""ShowTmlogInfosResponse

        The model defined in huaweicloud sdk

        :param tmlogs: TMLOG信息列表。
        :type tmlogs: list[:class:`huaweicloudsdkddm.v1.TmlogInfo`]
        :param total: 查询到TMLOG的节点总数
        :type total: int
        """
        
        super().__init__()

        self._tmlogs = None
        self._total = None
        self.discriminator = None

        if tmlogs is not None:
            self.tmlogs = tmlogs
        if total is not None:
            self.total = total

    @property
    def tmlogs(self):
        r"""Gets the tmlogs of this ShowTmlogInfosResponse.

        TMLOG信息列表。

        :return: The tmlogs of this ShowTmlogInfosResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.TmlogInfo`]
        """
        return self._tmlogs

    @tmlogs.setter
    def tmlogs(self, tmlogs):
        r"""Sets the tmlogs of this ShowTmlogInfosResponse.

        TMLOG信息列表。

        :param tmlogs: The tmlogs of this ShowTmlogInfosResponse.
        :type tmlogs: list[:class:`huaweicloudsdkddm.v1.TmlogInfo`]
        """
        self._tmlogs = tmlogs

    @property
    def total(self):
        r"""Gets the total of this ShowTmlogInfosResponse.

        查询到TMLOG的节点总数

        :return: The total of this ShowTmlogInfosResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowTmlogInfosResponse.

        查询到TMLOG的节点总数

        :param total: The total of this ShowTmlogInfosResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ShowTmlogInfosResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTmlogInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
