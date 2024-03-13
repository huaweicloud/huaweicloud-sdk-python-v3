# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllTablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'name': 'str',
        'create_by': 'str',
        'status': 'str',
        'sync_status': 'str',
        'sync_key': 'list[str]',
        'biz_catalog_id': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'biz_catalog_id_list': 'list[int]',
        'biz_type_list': 'list[str]'
    }

    attribute_map = {
        'workspace': 'workspace',
        'name': 'name',
        'create_by': 'create_by',
        'status': 'status',
        'sync_status': 'sync_status',
        'sync_key': 'sync_key',
        'biz_catalog_id': 'biz_catalog_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'biz_catalog_id_list': 'biz_catalog_id_list',
        'biz_type_list': 'biz_type_list'
    }

    def __init__(self, workspace=None, name=None, create_by=None, status=None, sync_status=None, sync_key=None, biz_catalog_id=None, begin_time=None, end_time=None, limit=None, offset=None, biz_catalog_id_list=None, biz_type_list=None):
        """ListAllTablesRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param name: 按名称或编码模糊查询
        :type name: str
        :param create_by: 按创建者查询
        :type create_by: str
        :param status: 业务状态
        :type status: str
        :param sync_status: 
        :type sync_status: str
        :param sync_key: 
        :type sync_key: list[str]
        :param biz_catalog_id: 所属的业务分层的id
        :type biz_catalog_id: str
        :param begin_time: 时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效
        :type begin_time: str
        :param end_time: 时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效
        :type end_time: str
        :param limit: 查询条数，即查询Y条数据。默认值50，取值范围[1,100]
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0
        :type offset: int
        :param biz_catalog_id_list: 所属主题的id列表
        :type biz_catalog_id_list: list[int]
        :param biz_type_list: 查询的表类型，必填
        :type biz_type_list: list[str]
        """
        
        

        self._workspace = None
        self._name = None
        self._create_by = None
        self._status = None
        self._sync_status = None
        self._sync_key = None
        self._biz_catalog_id = None
        self._begin_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._biz_catalog_id_list = None
        self._biz_type_list = None
        self.discriminator = None

        self.workspace = workspace
        if name is not None:
            self.name = name
        if create_by is not None:
            self.create_by = create_by
        if status is not None:
            self.status = status
        if sync_status is not None:
            self.sync_status = sync_status
        if sync_key is not None:
            self.sync_key = sync_key
        if biz_catalog_id is not None:
            self.biz_catalog_id = biz_catalog_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if biz_catalog_id_list is not None:
            self.biz_catalog_id_list = biz_catalog_id_list
        self.biz_type_list = biz_type_list

    @property
    def workspace(self):
        """Gets the workspace of this ListAllTablesRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListAllTablesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListAllTablesRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListAllTablesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def name(self):
        """Gets the name of this ListAllTablesRequest.

        按名称或编码模糊查询

        :return: The name of this ListAllTablesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAllTablesRequest.

        按名称或编码模糊查询

        :param name: The name of this ListAllTablesRequest.
        :type name: str
        """
        self._name = name

    @property
    def create_by(self):
        """Gets the create_by of this ListAllTablesRequest.

        按创建者查询

        :return: The create_by of this ListAllTablesRequest.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this ListAllTablesRequest.

        按创建者查询

        :param create_by: The create_by of this ListAllTablesRequest.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def status(self):
        """Gets the status of this ListAllTablesRequest.

        业务状态

        :return: The status of this ListAllTablesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAllTablesRequest.

        业务状态

        :param status: The status of this ListAllTablesRequest.
        :type status: str
        """
        self._status = status

    @property
    def sync_status(self):
        """Gets the sync_status of this ListAllTablesRequest.

        :return: The sync_status of this ListAllTablesRequest.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this ListAllTablesRequest.

        :param sync_status: The sync_status of this ListAllTablesRequest.
        :type sync_status: str
        """
        self._sync_status = sync_status

    @property
    def sync_key(self):
        """Gets the sync_key of this ListAllTablesRequest.

        :return: The sync_key of this ListAllTablesRequest.
        :rtype: list[str]
        """
        return self._sync_key

    @sync_key.setter
    def sync_key(self, sync_key):
        """Sets the sync_key of this ListAllTablesRequest.

        :param sync_key: The sync_key of this ListAllTablesRequest.
        :type sync_key: list[str]
        """
        self._sync_key = sync_key

    @property
    def biz_catalog_id(self):
        """Gets the biz_catalog_id of this ListAllTablesRequest.

        所属的业务分层的id

        :return: The biz_catalog_id of this ListAllTablesRequest.
        :rtype: str
        """
        return self._biz_catalog_id

    @biz_catalog_id.setter
    def biz_catalog_id(self, biz_catalog_id):
        """Sets the biz_catalog_id of this ListAllTablesRequest.

        所属的业务分层的id

        :param biz_catalog_id: The biz_catalog_id of this ListAllTablesRequest.
        :type biz_catalog_id: str
        """
        self._biz_catalog_id = biz_catalog_id

    @property
    def begin_time(self):
        """Gets the begin_time of this ListAllTablesRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :return: The begin_time of this ListAllTablesRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListAllTablesRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :param begin_time: The begin_time of this ListAllTablesRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAllTablesRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :return: The end_time of this ListAllTablesRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAllTablesRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :param end_time: The end_time of this ListAllTablesRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ListAllTablesRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :return: The limit of this ListAllTablesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAllTablesRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :param limit: The limit of this ListAllTablesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAllTablesRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :return: The offset of this ListAllTablesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAllTablesRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :param offset: The offset of this ListAllTablesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def biz_catalog_id_list(self):
        """Gets the biz_catalog_id_list of this ListAllTablesRequest.

        所属主题的id列表

        :return: The biz_catalog_id_list of this ListAllTablesRequest.
        :rtype: list[int]
        """
        return self._biz_catalog_id_list

    @biz_catalog_id_list.setter
    def biz_catalog_id_list(self, biz_catalog_id_list):
        """Sets the biz_catalog_id_list of this ListAllTablesRequest.

        所属主题的id列表

        :param biz_catalog_id_list: The biz_catalog_id_list of this ListAllTablesRequest.
        :type biz_catalog_id_list: list[int]
        """
        self._biz_catalog_id_list = biz_catalog_id_list

    @property
    def biz_type_list(self):
        """Gets the biz_type_list of this ListAllTablesRequest.

        查询的表类型，必填

        :return: The biz_type_list of this ListAllTablesRequest.
        :rtype: list[str]
        """
        return self._biz_type_list

    @biz_type_list.setter
    def biz_type_list(self, biz_type_list):
        """Sets the biz_type_list of this ListAllTablesRequest.

        查询的表类型，必填

        :param biz_type_list: The biz_type_list of this ListAllTablesRequest.
        :type biz_type_list: list[str]
        """
        self._biz_type_list = biz_type_list

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
        if not isinstance(other, ListAllTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
