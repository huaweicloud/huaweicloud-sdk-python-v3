# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllInstanceRepositoriesRequest:

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
        'limit': 'int',
        'name': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'name': 'name'
    }

    def __init__(self, marker=None, limit=None, name=None):
        r"""ListAllInstanceRepositoriesRequest

        The model defined in huaweicloud sdk

        :param marker: 分页查询时的查询标记，使用上一次接口调用返回的next_marker值，默认值从第一条数据查询。**注意：marker和limit参数需要配套使用。**
        :type marker: str
        :param limit: 条目数量，用于分页查询，默认值为100，最大值为100
        :type limit: int
        :param name: 仓库名称
        :type name: str
        """
        
        

        self._marker = None
        self._limit = None
        self._name = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name

    @property
    def marker(self):
        r"""Gets the marker of this ListAllInstanceRepositoriesRequest.

        分页查询时的查询标记，使用上一次接口调用返回的next_marker值，默认值从第一条数据查询。**注意：marker和limit参数需要配套使用。**

        :return: The marker of this ListAllInstanceRepositoriesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAllInstanceRepositoriesRequest.

        分页查询时的查询标记，使用上一次接口调用返回的next_marker值，默认值从第一条数据查询。**注意：marker和limit参数需要配套使用。**

        :param marker: The marker of this ListAllInstanceRepositoriesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListAllInstanceRepositoriesRequest.

        条目数量，用于分页查询，默认值为100，最大值为100

        :return: The limit of this ListAllInstanceRepositoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAllInstanceRepositoriesRequest.

        条目数量，用于分页查询，默认值为100，最大值为100

        :param limit: The limit of this ListAllInstanceRepositoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListAllInstanceRepositoriesRequest.

        仓库名称

        :return: The name of this ListAllInstanceRepositoriesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAllInstanceRepositoriesRequest.

        仓库名称

        :param name: The name of this ListAllInstanceRepositoriesRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListAllInstanceRepositoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
