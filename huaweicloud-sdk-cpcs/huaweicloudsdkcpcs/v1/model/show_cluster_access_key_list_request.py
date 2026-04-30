# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterAccessKeyListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'app_name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'limit': 'limit',
        'offset': 'offset',
        'app_name': 'app_name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, cluster_id=None, limit=None, offset=None, app_name=None, sort_key=None, sort_dir=None):
        r"""ShowClusterAccessKeyListRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 密码集群ID
        :type cluster_id: str
        :param limit: 指定查询返回记录条数，默认值10
        :type limit: int
        :param offset: 索引位置，从offset指定的下一条数据开始查询默认值为0
        :type offset: int
        :param app_name: 应用名称
        :type app_name: str
        :param sort_key: 排序属性，目前支持以下属性： - **create_time** : 应用的创建时间（默认）
        :type sort_key: str
        :param sort_dir: 排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序
        :type sort_dir: str
        """
        
        

        self._cluster_id = None
        self._limit = None
        self._offset = None
        self._app_name = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if app_name is not None:
            self.app_name = app_name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowClusterAccessKeyListRequest.

        密码集群ID

        :return: The cluster_id of this ShowClusterAccessKeyListRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowClusterAccessKeyListRequest.

        密码集群ID

        :param cluster_id: The cluster_id of this ShowClusterAccessKeyListRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowClusterAccessKeyListRequest.

        指定查询返回记录条数，默认值10

        :return: The limit of this ShowClusterAccessKeyListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowClusterAccessKeyListRequest.

        指定查询返回记录条数，默认值10

        :param limit: The limit of this ShowClusterAccessKeyListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowClusterAccessKeyListRequest.

        索引位置，从offset指定的下一条数据开始查询默认值为0

        :return: The offset of this ShowClusterAccessKeyListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowClusterAccessKeyListRequest.

        索引位置，从offset指定的下一条数据开始查询默认值为0

        :param offset: The offset of this ShowClusterAccessKeyListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def app_name(self):
        r"""Gets the app_name of this ShowClusterAccessKeyListRequest.

        应用名称

        :return: The app_name of this ShowClusterAccessKeyListRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ShowClusterAccessKeyListRequest.

        应用名称

        :param app_name: The app_name of this ShowClusterAccessKeyListRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ShowClusterAccessKeyListRequest.

        排序属性，目前支持以下属性： - **create_time** : 应用的创建时间（默认）

        :return: The sort_key of this ShowClusterAccessKeyListRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ShowClusterAccessKeyListRequest.

        排序属性，目前支持以下属性： - **create_time** : 应用的创建时间（默认）

        :param sort_key: The sort_key of this ShowClusterAccessKeyListRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ShowClusterAccessKeyListRequest.

        排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序

        :return: The sort_dir of this ShowClusterAccessKeyListRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ShowClusterAccessKeyListRequest.

        排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序

        :param sort_dir: The sort_dir of this ShowClusterAccessKeyListRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ShowClusterAccessKeyListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
