# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSearchAlgorithmsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_algo_count': 'int',
        'search_algo_list': 'list[ListSearchAlgorithmsSearchAlgoList]'
    }

    attribute_map = {
        'search_algo_count': 'search_algo_count',
        'search_algo_list': 'search_algo_list'
    }

    def __init__(self, search_algo_count=None, search_algo_list=None):
        r"""ShowSearchAlgorithmsResponse

        The model defined in huaweicloud sdk

        :param search_algo_count: 超参搜索算法的个数。
        :type search_algo_count: int
        :param search_algo_list: 所有超参搜索算法的列表。
        :type search_algo_list: list[:class:`huaweicloudsdkmodelarts.v1.ListSearchAlgorithmsSearchAlgoList`]
        """
        
        super().__init__()

        self._search_algo_count = None
        self._search_algo_list = None
        self.discriminator = None

        if search_algo_count is not None:
            self.search_algo_count = search_algo_count
        if search_algo_list is not None:
            self.search_algo_list = search_algo_list

    @property
    def search_algo_count(self):
        r"""Gets the search_algo_count of this ShowSearchAlgorithmsResponse.

        超参搜索算法的个数。

        :return: The search_algo_count of this ShowSearchAlgorithmsResponse.
        :rtype: int
        """
        return self._search_algo_count

    @search_algo_count.setter
    def search_algo_count(self, search_algo_count):
        r"""Sets the search_algo_count of this ShowSearchAlgorithmsResponse.

        超参搜索算法的个数。

        :param search_algo_count: The search_algo_count of this ShowSearchAlgorithmsResponse.
        :type search_algo_count: int
        """
        self._search_algo_count = search_algo_count

    @property
    def search_algo_list(self):
        r"""Gets the search_algo_list of this ShowSearchAlgorithmsResponse.

        所有超参搜索算法的列表。

        :return: The search_algo_list of this ShowSearchAlgorithmsResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ListSearchAlgorithmsSearchAlgoList`]
        """
        return self._search_algo_list

    @search_algo_list.setter
    def search_algo_list(self, search_algo_list):
        r"""Sets the search_algo_list of this ShowSearchAlgorithmsResponse.

        所有超参搜索算法的列表。

        :param search_algo_list: The search_algo_list of this ShowSearchAlgorithmsResponse.
        :type search_algo_list: list[:class:`huaweicloudsdkmodelarts.v1.ListSearchAlgorithmsSearchAlgoList`]
        """
        self._search_algo_list = search_algo_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowSearchAlgorithmsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSearchAlgorithmsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
