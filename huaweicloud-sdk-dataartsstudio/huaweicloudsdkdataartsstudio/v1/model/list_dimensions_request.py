# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDimensionsRequest:

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
        'l2_id': 'int',
        'derivative_ids': 'list[int]',
        'begin_time': 'str',
        'end_time': 'str',
        'fact_logic_id': 'int',
        'dimension_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'biz_catalog_id': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'name': 'name',
        'create_by': 'create_by',
        'approver': 'approver',
        'status': 'status',
        'l2_id': 'l2_id',
        'derivative_ids': 'derivative_ids',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'fact_logic_id': 'fact_logic_id',
        'dimension_type': 'dimension_type',
        'limit': 'limit',
        'offset': 'offset',
        'biz_catalog_id': 'biz_catalog_id'
    }

    def __init__(self, workspace=None, name=None, create_by=None, approver=None, status=None, l2_id=None, derivative_ids=None, begin_time=None, end_time=None, fact_logic_id=None, dimension_type=None, limit=None, offset=None, biz_catalog_id=None):
        """ListDimensionsRequest

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
        :param l2_id: 主题域l2 id
        :type l2_id: int
        :param derivative_ids: 依据复合指标id列表查维度
        :type derivative_ids: list[int]
        :param begin_time: 时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效
        :type begin_time: str
        :param end_time: 时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效
        :type end_time: str
        :param fact_logic_id: 事实表id
        :type fact_logic_id: int
        :param dimension_type: 维度类型
        :type dimension_type: str
        :param limit: 查询条数，即查询Y条数据。默认值50，取值范围[1,100]
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0
        :type offset: int
        :param biz_catalog_id: 所属的业务分层的id
        :type biz_catalog_id: str
        """
        
        

        self._workspace = None
        self._name = None
        self._create_by = None
        self._approver = None
        self._status = None
        self._l2_id = None
        self._derivative_ids = None
        self._begin_time = None
        self._end_time = None
        self._fact_logic_id = None
        self._dimension_type = None
        self._limit = None
        self._offset = None
        self._biz_catalog_id = None
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
        if l2_id is not None:
            self.l2_id = l2_id
        if derivative_ids is not None:
            self.derivative_ids = derivative_ids
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if fact_logic_id is not None:
            self.fact_logic_id = fact_logic_id
        if dimension_type is not None:
            self.dimension_type = dimension_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if biz_catalog_id is not None:
            self.biz_catalog_id = biz_catalog_id

    @property
    def workspace(self):
        """Gets the workspace of this ListDimensionsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListDimensionsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListDimensionsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListDimensionsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def name(self):
        """Gets the name of this ListDimensionsRequest.

        按名称或编码模糊查询

        :return: The name of this ListDimensionsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDimensionsRequest.

        按名称或编码模糊查询

        :param name: The name of this ListDimensionsRequest.
        :type name: str
        """
        self._name = name

    @property
    def create_by(self):
        """Gets the create_by of this ListDimensionsRequest.

        按创建者查询

        :return: The create_by of this ListDimensionsRequest.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this ListDimensionsRequest.

        按创建者查询

        :param create_by: The create_by of this ListDimensionsRequest.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def approver(self):
        """Gets the approver of this ListDimensionsRequest.

        按审核人查询

        :return: The approver of this ListDimensionsRequest.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        """Sets the approver of this ListDimensionsRequest.

        按审核人查询

        :param approver: The approver of this ListDimensionsRequest.
        :type approver: str
        """
        self._approver = approver

    @property
    def status(self):
        """Gets the status of this ListDimensionsRequest.

        业务状态

        :return: The status of this ListDimensionsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListDimensionsRequest.

        业务状态

        :param status: The status of this ListDimensionsRequest.
        :type status: str
        """
        self._status = status

    @property
    def l2_id(self):
        """Gets the l2_id of this ListDimensionsRequest.

        主题域l2 id

        :return: The l2_id of this ListDimensionsRequest.
        :rtype: int
        """
        return self._l2_id

    @l2_id.setter
    def l2_id(self, l2_id):
        """Sets the l2_id of this ListDimensionsRequest.

        主题域l2 id

        :param l2_id: The l2_id of this ListDimensionsRequest.
        :type l2_id: int
        """
        self._l2_id = l2_id

    @property
    def derivative_ids(self):
        """Gets the derivative_ids of this ListDimensionsRequest.

        依据复合指标id列表查维度

        :return: The derivative_ids of this ListDimensionsRequest.
        :rtype: list[int]
        """
        return self._derivative_ids

    @derivative_ids.setter
    def derivative_ids(self, derivative_ids):
        """Sets the derivative_ids of this ListDimensionsRequest.

        依据复合指标id列表查维度

        :param derivative_ids: The derivative_ids of this ListDimensionsRequest.
        :type derivative_ids: list[int]
        """
        self._derivative_ids = derivative_ids

    @property
    def begin_time(self):
        """Gets the begin_time of this ListDimensionsRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :return: The begin_time of this ListDimensionsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListDimensionsRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :param begin_time: The begin_time of this ListDimensionsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListDimensionsRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :return: The end_time of this ListDimensionsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListDimensionsRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :param end_time: The end_time of this ListDimensionsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def fact_logic_id(self):
        """Gets the fact_logic_id of this ListDimensionsRequest.

        事实表id

        :return: The fact_logic_id of this ListDimensionsRequest.
        :rtype: int
        """
        return self._fact_logic_id

    @fact_logic_id.setter
    def fact_logic_id(self, fact_logic_id):
        """Sets the fact_logic_id of this ListDimensionsRequest.

        事实表id

        :param fact_logic_id: The fact_logic_id of this ListDimensionsRequest.
        :type fact_logic_id: int
        """
        self._fact_logic_id = fact_logic_id

    @property
    def dimension_type(self):
        """Gets the dimension_type of this ListDimensionsRequest.

        维度类型

        :return: The dimension_type of this ListDimensionsRequest.
        :rtype: str
        """
        return self._dimension_type

    @dimension_type.setter
    def dimension_type(self, dimension_type):
        """Sets the dimension_type of this ListDimensionsRequest.

        维度类型

        :param dimension_type: The dimension_type of this ListDimensionsRequest.
        :type dimension_type: str
        """
        self._dimension_type = dimension_type

    @property
    def limit(self):
        """Gets the limit of this ListDimensionsRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :return: The limit of this ListDimensionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDimensionsRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :param limit: The limit of this ListDimensionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDimensionsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :return: The offset of this ListDimensionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDimensionsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :param offset: The offset of this ListDimensionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def biz_catalog_id(self):
        """Gets the biz_catalog_id of this ListDimensionsRequest.

        所属的业务分层的id

        :return: The biz_catalog_id of this ListDimensionsRequest.
        :rtype: str
        """
        return self._biz_catalog_id

    @biz_catalog_id.setter
    def biz_catalog_id(self, biz_catalog_id):
        """Sets the biz_catalog_id of this ListDimensionsRequest.

        所属的业务分层的id

        :param biz_catalog_id: The biz_catalog_id of this ListDimensionsRequest.
        :type biz_catalog_id: str
        """
        self._biz_catalog_id = biz_catalog_id

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
        if not isinstance(other, ListDimensionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
