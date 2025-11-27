# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceViewsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, limit=None, marker=None):
        r"""ListResourceViewsRequest

        The model defined in huaweicloud sdk

        :param limit: 用于分页查询，查询数量，最大的返回数量。取值范围：1-500。
        :type limit: int
        :param marker: 用于分页查询。分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。
        :type marker: str
        """
        
        

        self._limit = None
        self._marker = None
        self.discriminator = None

        self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListResourceViewsRequest.

        用于分页查询，查询数量，最大的返回数量。取值范围：1-500。

        :return: The limit of this ListResourceViewsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourceViewsRequest.

        用于分页查询，查询数量，最大的返回数量。取值范围：1-500。

        :param limit: The limit of this ListResourceViewsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListResourceViewsRequest.

        用于分页查询。分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :return: The marker of this ListResourceViewsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListResourceViewsRequest.

        用于分页查询。分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :param marker: The marker of this ListResourceViewsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListResourceViewsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
