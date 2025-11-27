# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'enablestatus': 'bool',
        'clustergroupid': 'str',
        'limit': 'int',
        'offset': 'int',
        'order_by': 'str',
        'order': 'str',
        'managetype': 'str',
        'clusterids': 'str'
    }

    attribute_map = {
        'category': 'category',
        'enablestatus': 'enablestatus',
        'clustergroupid': 'clustergroupid',
        'limit': 'limit',
        'offset': 'offset',
        'order_by': 'order_by',
        'order': 'order',
        'managetype': 'managetype',
        'clusterids': 'clusterids'
    }

    def __init__(self, category=None, enablestatus=None, clustergroupid=None, limit=None, offset=None, order_by=None, order=None, managetype=None, clusterids=None):
        r"""ShowClusterListRequest

        The model defined in huaweicloud sdk

        :param category: 获取特定category的集群。
        :type category: str
        :param enablestatus: 是否获取集群的资源信息。不填或者填写为true为获取集群资源汇总信息，置为false为不获取集群状态信息；缺省值为true
        :type enablestatus: bool
        :param clustergroupid: 容器舰队ID。不填会返回用户所有集群，填了之后会返回属于该容器舰队的集群。
        :type clustergroupid: str
        :param limit: 分页获取列表时，页的大小，默认为-1
        :type limit: int
        :param offset: 分页获取列表时，起始偏移量，默认为0
        :type offset: int
        :param order_by: 分页获取列表时，排序参数，支持 create_at 和 update_at
        :type order_by: str
        :param order: 分页获取列表时，排序方向，支持 desc 和 asc
        :type order: str
        :param managetype: 获取集群列表时，根据集群类型筛选，不传参时默认为 all ，支持 all ，grouped，discrete 三种类型。 - grouped：在舰队中纳管的集群 - discrete：未加入舰队的集群 - all：所有集群
        :type managetype: str
        :param clusterids: 集群ID。多个ID以英文逗号分隔。
        :type clusterids: str
        """
        
        

        self._category = None
        self._enablestatus = None
        self._clustergroupid = None
        self._limit = None
        self._offset = None
        self._order_by = None
        self._order = None
        self._managetype = None
        self._clusterids = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if enablestatus is not None:
            self.enablestatus = enablestatus
        if clustergroupid is not None:
            self.clustergroupid = clustergroupid
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order
        if managetype is not None:
            self.managetype = managetype
        if clusterids is not None:
            self.clusterids = clusterids

    @property
    def category(self):
        r"""Gets the category of this ShowClusterListRequest.

        获取特定category的集群。

        :return: The category of this ShowClusterListRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowClusterListRequest.

        获取特定category的集群。

        :param category: The category of this ShowClusterListRequest.
        :type category: str
        """
        self._category = category

    @property
    def enablestatus(self):
        r"""Gets the enablestatus of this ShowClusterListRequest.

        是否获取集群的资源信息。不填或者填写为true为获取集群资源汇总信息，置为false为不获取集群状态信息；缺省值为true

        :return: The enablestatus of this ShowClusterListRequest.
        :rtype: bool
        """
        return self._enablestatus

    @enablestatus.setter
    def enablestatus(self, enablestatus):
        r"""Sets the enablestatus of this ShowClusterListRequest.

        是否获取集群的资源信息。不填或者填写为true为获取集群资源汇总信息，置为false为不获取集群状态信息；缺省值为true

        :param enablestatus: The enablestatus of this ShowClusterListRequest.
        :type enablestatus: bool
        """
        self._enablestatus = enablestatus

    @property
    def clustergroupid(self):
        r"""Gets the clustergroupid of this ShowClusterListRequest.

        容器舰队ID。不填会返回用户所有集群，填了之后会返回属于该容器舰队的集群。

        :return: The clustergroupid of this ShowClusterListRequest.
        :rtype: str
        """
        return self._clustergroupid

    @clustergroupid.setter
    def clustergroupid(self, clustergroupid):
        r"""Sets the clustergroupid of this ShowClusterListRequest.

        容器舰队ID。不填会返回用户所有集群，填了之后会返回属于该容器舰队的集群。

        :param clustergroupid: The clustergroupid of this ShowClusterListRequest.
        :type clustergroupid: str
        """
        self._clustergroupid = clustergroupid

    @property
    def limit(self):
        r"""Gets the limit of this ShowClusterListRequest.

        分页获取列表时，页的大小，默认为-1

        :return: The limit of this ShowClusterListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowClusterListRequest.

        分页获取列表时，页的大小，默认为-1

        :param limit: The limit of this ShowClusterListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowClusterListRequest.

        分页获取列表时，起始偏移量，默认为0

        :return: The offset of this ShowClusterListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowClusterListRequest.

        分页获取列表时，起始偏移量，默认为0

        :param offset: The offset of this ShowClusterListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def order_by(self):
        r"""Gets the order_by of this ShowClusterListRequest.

        分页获取列表时，排序参数，支持 create_at 和 update_at

        :return: The order_by of this ShowClusterListRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ShowClusterListRequest.

        分页获取列表时，排序参数，支持 create_at 和 update_at

        :param order_by: The order_by of this ShowClusterListRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        r"""Gets the order of this ShowClusterListRequest.

        分页获取列表时，排序方向，支持 desc 和 asc

        :return: The order of this ShowClusterListRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ShowClusterListRequest.

        分页获取列表时，排序方向，支持 desc 和 asc

        :param order: The order of this ShowClusterListRequest.
        :type order: str
        """
        self._order = order

    @property
    def managetype(self):
        r"""Gets the managetype of this ShowClusterListRequest.

        获取集群列表时，根据集群类型筛选，不传参时默认为 all ，支持 all ，grouped，discrete 三种类型。 - grouped：在舰队中纳管的集群 - discrete：未加入舰队的集群 - all：所有集群

        :return: The managetype of this ShowClusterListRequest.
        :rtype: str
        """
        return self._managetype

    @managetype.setter
    def managetype(self, managetype):
        r"""Sets the managetype of this ShowClusterListRequest.

        获取集群列表时，根据集群类型筛选，不传参时默认为 all ，支持 all ，grouped，discrete 三种类型。 - grouped：在舰队中纳管的集群 - discrete：未加入舰队的集群 - all：所有集群

        :param managetype: The managetype of this ShowClusterListRequest.
        :type managetype: str
        """
        self._managetype = managetype

    @property
    def clusterids(self):
        r"""Gets the clusterids of this ShowClusterListRequest.

        集群ID。多个ID以英文逗号分隔。

        :return: The clusterids of this ShowClusterListRequest.
        :rtype: str
        """
        return self._clusterids

    @clusterids.setter
    def clusterids(self, clusterids):
        r"""Sets the clusterids of this ShowClusterListRequest.

        集群ID。多个ID以英文逗号分隔。

        :param clusterids: The clusterids of this ShowClusterListRequest.
        :type clusterids: str
        """
        self._clusterids = clusterids

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
        if not isinstance(other, ShowClusterListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
