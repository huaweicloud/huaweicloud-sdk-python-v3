# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchAtomicIndexesRequest:

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
        'approver': 'str',
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'l3_id': 'int',
        'table_id': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'name': 'name',
        'create_by': 'create_by',
        'approver': 'approver',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'l3_id': 'l3_id',
        'table_id': 'table_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, name=None, create_by=None, approver=None, status=None, begin_time=None, end_time=None, l3_id=None, table_id=None, limit=None, offset=None):
        """SearchAtomicIndexesRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param name: 按名称或编码模糊查询
        :type name: str
        :param create_by: 按创建者查询
        :type create_by: str
        :param approver: 按审核人查询
        :type approver: str
        :param status: 业务状态
        :type status: str
        :param begin_time: 时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效
        :type begin_time: str
        :param end_time: 时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效
        :type end_time: str
        :param l3_id: 业务对象l3 id
        :type l3_id: int
        :param table_id: 关联表id
        :type table_id: int
        :param limit: 查询条数，即查询Y条数据。默认值50，取值范围[1,100]
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0
        :type offset: int
        """
        
        

        self._workspace = None
        self._name = None
        self._create_by = None
        self._approver = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._l3_id = None
        self._table_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if name is not None:
            self.name = name
        if create_by is not None:
            self.create_by = create_by
        if approver is not None:
            self.approver = approver
        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if l3_id is not None:
            self.l3_id = l3_id
        if table_id is not None:
            self.table_id = table_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this SearchAtomicIndexesRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this SearchAtomicIndexesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this SearchAtomicIndexesRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this SearchAtomicIndexesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def name(self):
        """Gets the name of this SearchAtomicIndexesRequest.

        按名称或编码模糊查询

        :return: The name of this SearchAtomicIndexesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchAtomicIndexesRequest.

        按名称或编码模糊查询

        :param name: The name of this SearchAtomicIndexesRequest.
        :type name: str
        """
        self._name = name

    @property
    def create_by(self):
        """Gets the create_by of this SearchAtomicIndexesRequest.

        按创建者查询

        :return: The create_by of this SearchAtomicIndexesRequest.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this SearchAtomicIndexesRequest.

        按创建者查询

        :param create_by: The create_by of this SearchAtomicIndexesRequest.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def approver(self):
        """Gets the approver of this SearchAtomicIndexesRequest.

        按审核人查询

        :return: The approver of this SearchAtomicIndexesRequest.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        """Sets the approver of this SearchAtomicIndexesRequest.

        按审核人查询

        :param approver: The approver of this SearchAtomicIndexesRequest.
        :type approver: str
        """
        self._approver = approver

    @property
    def status(self):
        """Gets the status of this SearchAtomicIndexesRequest.

        业务状态

        :return: The status of this SearchAtomicIndexesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchAtomicIndexesRequest.

        业务状态

        :param status: The status of this SearchAtomicIndexesRequest.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        """Gets the begin_time of this SearchAtomicIndexesRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :return: The begin_time of this SearchAtomicIndexesRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this SearchAtomicIndexesRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :param begin_time: The begin_time of this SearchAtomicIndexesRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this SearchAtomicIndexesRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :return: The end_time of this SearchAtomicIndexesRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SearchAtomicIndexesRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :param end_time: The end_time of this SearchAtomicIndexesRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def l3_id(self):
        """Gets the l3_id of this SearchAtomicIndexesRequest.

        业务对象l3 id

        :return: The l3_id of this SearchAtomicIndexesRequest.
        :rtype: int
        """
        return self._l3_id

    @l3_id.setter
    def l3_id(self, l3_id):
        """Sets the l3_id of this SearchAtomicIndexesRequest.

        业务对象l3 id

        :param l3_id: The l3_id of this SearchAtomicIndexesRequest.
        :type l3_id: int
        """
        self._l3_id = l3_id

    @property
    def table_id(self):
        """Gets the table_id of this SearchAtomicIndexesRequest.

        关联表id

        :return: The table_id of this SearchAtomicIndexesRequest.
        :rtype: int
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this SearchAtomicIndexesRequest.

        关联表id

        :param table_id: The table_id of this SearchAtomicIndexesRequest.
        :type table_id: int
        """
        self._table_id = table_id

    @property
    def limit(self):
        """Gets the limit of this SearchAtomicIndexesRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :return: The limit of this SearchAtomicIndexesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchAtomicIndexesRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :param limit: The limit of this SearchAtomicIndexesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this SearchAtomicIndexesRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :return: The offset of this SearchAtomicIndexesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchAtomicIndexesRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :param offset: The offset of this SearchAtomicIndexesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, SearchAtomicIndexesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
