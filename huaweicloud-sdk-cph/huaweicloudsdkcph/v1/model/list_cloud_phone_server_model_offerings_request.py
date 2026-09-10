# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudPhoneServerModelOfferingsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, marker=None, limit=None):
        r"""ListCloudPhoneServerModelOfferingsRequest

        The model defined in huaweicloud sdk

        :param marker: 分页标记。从marker指定的下一条数据开始查询。
        :type marker: str
        :param limit: 最小值1，最大值1000，默认为100。返回的结果中记录数不超过limit值。
        :type limit: int
        """
        
        

        self._marker = None
        self._limit = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListCloudPhoneServerModelOfferingsRequest.

        分页标记。从marker指定的下一条数据开始查询。

        :return: The marker of this ListCloudPhoneServerModelOfferingsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListCloudPhoneServerModelOfferingsRequest.

        分页标记。从marker指定的下一条数据开始查询。

        :param marker: The marker of this ListCloudPhoneServerModelOfferingsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListCloudPhoneServerModelOfferingsRequest.

        最小值1，最大值1000，默认为100。返回的结果中记录数不超过limit值。

        :return: The limit of this ListCloudPhoneServerModelOfferingsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCloudPhoneServerModelOfferingsRequest.

        最小值1，最大值1000，默认为100。返回的结果中记录数不超过limit值。

        :param limit: The limit of this ListCloudPhoneServerModelOfferingsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListCloudPhoneServerModelOfferingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
