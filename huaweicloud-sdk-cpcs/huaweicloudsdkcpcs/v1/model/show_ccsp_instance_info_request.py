# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCcspInstanceInfoRequest:

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
        'name': 'str',
        'offset': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'cluster_id': 'str',
        'status': 'int',
        'is_normal': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'cluster_id': 'cluster_id',
        'status': 'status',
        'is_normal': 'is_normal'
    }

    def __init__(self, limit=None, name=None, offset=None, sort_key=None, sort_dir=None, cluster_id=None, status=None, is_normal=None):
        r"""ShowCcspInstanceInfoRequest

        The model defined in huaweicloud sdk

        :param limit: 指定查询返回记录条数，默认值10
        :type limit: int
        :param name: 实例名称
        :type name: str
        :param offset: 索引位置，从offset指定的下一条数据开始查询默认值为0
        :type offset: int
        :param sort_key: 排序属性，目前支持以下属性： - **create_time** : 实例创建时间（默认）
        :type sort_key: str
        :param sort_dir: 排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序
        :type sort_dir: str
        :param cluster_id: 密码服务集群ID
        :type cluster_id: str
        :param status: 实例的服务状态: - **enable** : 启用； - **disable** : 停用
        :type status: int
        :param is_normal: 实例健康状态： - **true** : 正常； - **false** : 异常
        :type is_normal: bool
        """
        
        

        self._limit = None
        self._name = None
        self._offset = None
        self._sort_key = None
        self._sort_dir = None
        self._cluster_id = None
        self._status = None
        self._is_normal = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if status is not None:
            self.status = status
        if is_normal is not None:
            self.is_normal = is_normal

    @property
    def limit(self):
        r"""Gets the limit of this ShowCcspInstanceInfoRequest.

        指定查询返回记录条数，默认值10

        :return: The limit of this ShowCcspInstanceInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowCcspInstanceInfoRequest.

        指定查询返回记录条数，默认值10

        :param limit: The limit of this ShowCcspInstanceInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ShowCcspInstanceInfoRequest.

        实例名称

        :return: The name of this ShowCcspInstanceInfoRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowCcspInstanceInfoRequest.

        实例名称

        :param name: The name of this ShowCcspInstanceInfoRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ShowCcspInstanceInfoRequest.

        索引位置，从offset指定的下一条数据开始查询默认值为0

        :return: The offset of this ShowCcspInstanceInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowCcspInstanceInfoRequest.

        索引位置，从offset指定的下一条数据开始查询默认值为0

        :param offset: The offset of this ShowCcspInstanceInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ShowCcspInstanceInfoRequest.

        排序属性，目前支持以下属性： - **create_time** : 实例创建时间（默认）

        :return: The sort_key of this ShowCcspInstanceInfoRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ShowCcspInstanceInfoRequest.

        排序属性，目前支持以下属性： - **create_time** : 实例创建时间（默认）

        :param sort_key: The sort_key of this ShowCcspInstanceInfoRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ShowCcspInstanceInfoRequest.

        排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序

        :return: The sort_dir of this ShowCcspInstanceInfoRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ShowCcspInstanceInfoRequest.

        排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序

        :param sort_dir: The sort_dir of this ShowCcspInstanceInfoRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowCcspInstanceInfoRequest.

        密码服务集群ID

        :return: The cluster_id of this ShowCcspInstanceInfoRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowCcspInstanceInfoRequest.

        密码服务集群ID

        :param cluster_id: The cluster_id of this ShowCcspInstanceInfoRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def status(self):
        r"""Gets the status of this ShowCcspInstanceInfoRequest.

        实例的服务状态: - **enable** : 启用； - **disable** : 停用

        :return: The status of this ShowCcspInstanceInfoRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowCcspInstanceInfoRequest.

        实例的服务状态: - **enable** : 启用； - **disable** : 停用

        :param status: The status of this ShowCcspInstanceInfoRequest.
        :type status: int
        """
        self._status = status

    @property
    def is_normal(self):
        r"""Gets the is_normal of this ShowCcspInstanceInfoRequest.

        实例健康状态： - **true** : 正常； - **false** : 异常

        :return: The is_normal of this ShowCcspInstanceInfoRequest.
        :rtype: bool
        """
        return self._is_normal

    @is_normal.setter
    def is_normal(self, is_normal):
        r"""Sets the is_normal of this ShowCcspInstanceInfoRequest.

        实例健康状态： - **true** : 正常； - **false** : 异常

        :param is_normal: The is_normal of this ShowCcspInstanceInfoRequest.
        :type is_normal: bool
        """
        self._is_normal = is_normal

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
        if not isinstance(other, ShowCcspInstanceInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
