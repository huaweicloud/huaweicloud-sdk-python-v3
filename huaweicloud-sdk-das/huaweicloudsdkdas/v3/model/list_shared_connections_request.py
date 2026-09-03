# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSharedConnectionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'keywords': 'str',
        'cur_page': 'str',
        'per_page': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'keywords': 'keywords',
        'cur_page': 'cur_page',
        'per_page': 'per_page'
    }

    def __init__(self, connection_id=None, keywords=None, cur_page=None, per_page=None):
        r"""ListSharedConnectionsRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param keywords: 搜索关键字
        :type keywords: str
        :param cur_page: 当前页码
        :type cur_page: str
        :param per_page: 每页记录数
        :type per_page: str
        """
        
        

        self._connection_id = None
        self._keywords = None
        self._cur_page = None
        self._per_page = None
        self.discriminator = None

        self.connection_id = connection_id
        if keywords is not None:
            self.keywords = keywords
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ListSharedConnectionsRequest.

        连接ID

        :return: The connection_id of this ListSharedConnectionsRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ListSharedConnectionsRequest.

        连接ID

        :param connection_id: The connection_id of this ListSharedConnectionsRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def keywords(self):
        r"""Gets the keywords of this ListSharedConnectionsRequest.

        搜索关键字

        :return: The keywords of this ListSharedConnectionsRequest.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this ListSharedConnectionsRequest.

        搜索关键字

        :param keywords: The keywords of this ListSharedConnectionsRequest.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListSharedConnectionsRequest.

        当前页码

        :return: The cur_page of this ListSharedConnectionsRequest.
        :rtype: str
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListSharedConnectionsRequest.

        当前页码

        :param cur_page: The cur_page of this ListSharedConnectionsRequest.
        :type cur_page: str
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListSharedConnectionsRequest.

        每页记录数

        :return: The per_page of this ListSharedConnectionsRequest.
        :rtype: str
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListSharedConnectionsRequest.

        每页记录数

        :param per_page: The per_page of this ListSharedConnectionsRequest.
        :type per_page: str
        """
        self._per_page = per_page

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
        if not isinstance(other, ListSharedConnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
