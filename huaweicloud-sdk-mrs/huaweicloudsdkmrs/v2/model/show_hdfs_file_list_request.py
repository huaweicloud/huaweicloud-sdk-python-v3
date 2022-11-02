# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHdfsFileListRequest:

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
        'path': 'str',
        'offset': 'str',
        'limit': 'str',
        'sort_key': 'str',
        'order': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'path': 'path',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'order': 'order'
    }

    def __init__(self, cluster_id=None, path=None, offset=None, limit=None, sort_key=None, order=None):
        """ShowHdfsFileListRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。
        :type cluster_id: str
        :param path: 文件目录。 比如访问“/tmp/test”目录列表，此处必须是目录，整体URI为/v2/{project_id}/clusters/{cluster_id}/files?path&#x3D;%2Ftmp%2Ftest 单层目录要遵循以下规则： - 不能为空 - 不能以\&quot;.\&quot;开头或结尾 - 不能包括下列符号 : :*?\&quot;&lt;&gt;|\\;&amp;,&#39;&#x60;!{}[]$%+ - 不能超过255个字节
        :type path: str
        :param offset: 分页参数，表示从该偏移量开始查询文件列表，默认值为0。
        :type offset: str
        :param limit: 分页参数，列表当前分页的数量限制，默认为100，最大1000。
        :type limit: str
        :param sort_key: 列表排序按该属性排序。缺省值：path_suffix - path_suffix：文件或目录名称 - length：文件大小 - modification_time：修改时间
        :type sort_key: str
        :param order: 列表排序方式，desc为降序，asc为升序，默认值为desc。
        :type order: str
        """
        
        

        self._cluster_id = None
        self._path = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._order = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.path = path
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if order is not None:
            self.order = order

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowHdfsFileListRequest.

        集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。

        :return: The cluster_id of this ShowHdfsFileListRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowHdfsFileListRequest.

        集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。

        :param cluster_id: The cluster_id of this ShowHdfsFileListRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def path(self):
        """Gets the path of this ShowHdfsFileListRequest.

        文件目录。 比如访问“/tmp/test”目录列表，此处必须是目录，整体URI为/v2/{project_id}/clusters/{cluster_id}/files?path=%2Ftmp%2Ftest 单层目录要遵循以下规则： - 不能为空 - 不能以\".\"开头或结尾 - 不能包括下列符号 : :*?\"<>|\\;&,'`!{}[]$%+ - 不能超过255个字节

        :return: The path of this ShowHdfsFileListRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ShowHdfsFileListRequest.

        文件目录。 比如访问“/tmp/test”目录列表，此处必须是目录，整体URI为/v2/{project_id}/clusters/{cluster_id}/files?path=%2Ftmp%2Ftest 单层目录要遵循以下规则： - 不能为空 - 不能以\".\"开头或结尾 - 不能包括下列符号 : :*?\"<>|\\;&,'`!{}[]$%+ - 不能超过255个字节

        :param path: The path of this ShowHdfsFileListRequest.
        :type path: str
        """
        self._path = path

    @property
    def offset(self):
        """Gets the offset of this ShowHdfsFileListRequest.

        分页参数，表示从该偏移量开始查询文件列表，默认值为0。

        :return: The offset of this ShowHdfsFileListRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowHdfsFileListRequest.

        分页参数，表示从该偏移量开始查询文件列表，默认值为0。

        :param offset: The offset of this ShowHdfsFileListRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowHdfsFileListRequest.

        分页参数，列表当前分页的数量限制，默认为100，最大1000。

        :return: The limit of this ShowHdfsFileListRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowHdfsFileListRequest.

        分页参数，列表当前分页的数量限制，默认为100，最大1000。

        :param limit: The limit of this ShowHdfsFileListRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def sort_key(self):
        """Gets the sort_key of this ShowHdfsFileListRequest.

        列表排序按该属性排序。缺省值：path_suffix - path_suffix：文件或目录名称 - length：文件大小 - modification_time：修改时间

        :return: The sort_key of this ShowHdfsFileListRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ShowHdfsFileListRequest.

        列表排序按该属性排序。缺省值：path_suffix - path_suffix：文件或目录名称 - length：文件大小 - modification_time：修改时间

        :param sort_key: The sort_key of this ShowHdfsFileListRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def order(self):
        """Gets the order of this ShowHdfsFileListRequest.

        列表排序方式，desc为降序，asc为升序，默认值为desc。

        :return: The order of this ShowHdfsFileListRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ShowHdfsFileListRequest.

        列表排序方式，desc为降序，asc为升序，默认值为desc。

        :param order: The order of this ShowHdfsFileListRequest.
        :type order: str
        """
        self._order = order

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowHdfsFileListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
