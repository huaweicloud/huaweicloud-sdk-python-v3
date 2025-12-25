# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVifPeerDetectionsRequest:

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
        'sort_key': 'str',
        'sort_dir': 'list[str]',
        'offset': 'int',
        'page_reverse': 'bool',
        'vif_peer_id': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'offset': 'offset',
        'page_reverse': 'page_reverse',
        'vif_peer_id': 'vif_peer_id'
    }

    def __init__(self, marker=None, limit=None, sort_key=None, sort_dir=None, offset=None, page_reverse=None, vif_peer_id=None):
        r"""ListVifPeerDetectionsRequest

        The model defined in huaweicloud sdk

        :param marker: 上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param limit: 每页返回的个数。 取值范围：1~2000。
        :type limit: int
        :param sort_key: 排序字段。
        :type sort_key: str
        :param sort_dir: 返回结果按照升序(asc)或降序(desc)排列，默认为asc
        :type sort_dir: list[str]
        :param offset: 分页偏移量
        :type offset: int
        :param page_reverse: 分页参数
        :type page_reverse: bool
        :param vif_peer_id: 虚拟接口对等体ID
        :type vif_peer_id: str
        """
        
        

        self._marker = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._offset = None
        self._page_reverse = None
        self._vif_peer_id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if offset is not None:
            self.offset = offset
        if page_reverse is not None:
            self.page_reverse = page_reverse
        self.vif_peer_id = vif_peer_id

    @property
    def marker(self):
        r"""Gets the marker of this ListVifPeerDetectionsRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListVifPeerDetectionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListVifPeerDetectionsRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListVifPeerDetectionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListVifPeerDetectionsRequest.

        每页返回的个数。 取值范围：1~2000。

        :return: The limit of this ListVifPeerDetectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVifPeerDetectionsRequest.

        每页返回的个数。 取值范围：1~2000。

        :param limit: The limit of this ListVifPeerDetectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListVifPeerDetectionsRequest.

        排序字段。

        :return: The sort_key of this ListVifPeerDetectionsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListVifPeerDetectionsRequest.

        排序字段。

        :param sort_key: The sort_key of this ListVifPeerDetectionsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListVifPeerDetectionsRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :return: The sort_dir of this ListVifPeerDetectionsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListVifPeerDetectionsRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :param sort_dir: The sort_dir of this ListVifPeerDetectionsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def offset(self):
        r"""Gets the offset of this ListVifPeerDetectionsRequest.

        分页偏移量

        :return: The offset of this ListVifPeerDetectionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVifPeerDetectionsRequest.

        分页偏移量

        :param offset: The offset of this ListVifPeerDetectionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListVifPeerDetectionsRequest.

        分页参数

        :return: The page_reverse of this ListVifPeerDetectionsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListVifPeerDetectionsRequest.

        分页参数

        :param page_reverse: The page_reverse of this ListVifPeerDetectionsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def vif_peer_id(self):
        r"""Gets the vif_peer_id of this ListVifPeerDetectionsRequest.

        虚拟接口对等体ID

        :return: The vif_peer_id of this ListVifPeerDetectionsRequest.
        :rtype: str
        """
        return self._vif_peer_id

    @vif_peer_id.setter
    def vif_peer_id(self, vif_peer_id):
        r"""Sets the vif_peer_id of this ListVifPeerDetectionsRequest.

        虚拟接口对等体ID

        :param vif_peer_id: The vif_peer_id of this ListVifPeerDetectionsRequest.
        :type vif_peer_id: str
        """
        self._vif_peer_id = vif_peer_id

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
        if not isinstance(other, ListVifPeerDetectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
