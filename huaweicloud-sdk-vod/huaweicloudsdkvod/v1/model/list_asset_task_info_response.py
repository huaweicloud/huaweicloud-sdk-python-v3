# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetTaskInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'results': 'list[Result]',
        'count': 'int',
        'next_marker': 'str'
    }

    attribute_map = {
        'results': 'results',
        'count': 'count',
        'next_marker': 'next_marker'
    }

    def __init__(self, results=None, count=None, next_marker=None):
        r"""ListAssetTaskInfoResponse

        The model defined in huaweicloud sdk

        :param results: 结果列表展示 
        :type results: list[:class:`huaweicloudsdkvod.v1.Result`]
        :param count: 根据条件的总条目数量 
        :type count: int
        :param next_marker: 下次查询的标志位 
        :type next_marker: str
        """
        
        super().__init__()

        self._results = None
        self._count = None
        self._next_marker = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if count is not None:
            self.count = count
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def results(self):
        r"""Gets the results of this ListAssetTaskInfoResponse.

        结果列表展示 

        :return: The results of this ListAssetTaskInfoResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.Result`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this ListAssetTaskInfoResponse.

        结果列表展示 

        :param results: The results of this ListAssetTaskInfoResponse.
        :type results: list[:class:`huaweicloudsdkvod.v1.Result`]
        """
        self._results = results

    @property
    def count(self):
        r"""Gets the count of this ListAssetTaskInfoResponse.

        根据条件的总条目数量 

        :return: The count of this ListAssetTaskInfoResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAssetTaskInfoResponse.

        根据条件的总条目数量 

        :param count: The count of this ListAssetTaskInfoResponse.
        :type count: int
        """
        self._count = count

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListAssetTaskInfoResponse.

        下次查询的标志位 

        :return: The next_marker of this ListAssetTaskInfoResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListAssetTaskInfoResponse.

        下次查询的标志位 

        :param next_marker: The next_marker of this ListAssetTaskInfoResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    def to_dict(self):
        import warnings
        warnings.warn("ListAssetTaskInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAssetTaskInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
