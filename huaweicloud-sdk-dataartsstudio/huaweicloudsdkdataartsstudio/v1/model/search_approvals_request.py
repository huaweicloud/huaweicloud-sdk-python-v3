# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchApprovalsRequest:

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
        'biz_id': 'int',
        'name': 'str',
        'create_by': 'str',
        'approver': 'str',
        'approval_status': 'str',
        'approval_status_detail': 'str',
        'approval_type': 'str',
        'biz_type': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'biz_id': 'biz_id',
        'name': 'name',
        'create_by': 'create_by',
        'approver': 'approver',
        'approval_status': 'approval_status',
        'approval_status_detail': 'approval_status_detail',
        'approval_type': 'approval_type',
        'biz_type': 'biz_type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, biz_id=None, name=None, create_by=None, approver=None, approval_status=None, approval_status_detail=None, approval_type=None, biz_type=None, begin_time=None, end_time=None, limit=None, offset=None):
        """SearchApprovalsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param biz_id: 业务定义id
        :type biz_id: int
        :param name: 按名称或编码模糊查询
        :type name: str
        :param create_by: 按创建者查询
        :type create_by: str
        :param approver: 按审核人查询
        :type approver: str
        :param approval_status: 查询待审批，已审批
        :type approval_status: str
        :param approval_status_detail: 查询待审批，已审批
        :type approval_status_detail: str
        :param approval_type: 业务审核类型
        :type approval_type: str
        :param biz_type: 按业务类型查询
        :type biz_type: str
        :param begin_time: 时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效
        :type begin_time: str
        :param end_time: 时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效
        :type end_time: str
        :param limit: 查询条数，即查询Y条数据。默认值50，取值范围[1,100]
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0
        :type offset: int
        """
        
        

        self._workspace = None
        self._biz_id = None
        self._name = None
        self._create_by = None
        self._approver = None
        self._approval_status = None
        self._approval_status_detail = None
        self._approval_type = None
        self._biz_type = None
        self._begin_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if biz_id is not None:
            self.biz_id = biz_id
        if name is not None:
            self.name = name
        if create_by is not None:
            self.create_by = create_by
        if approver is not None:
            self.approver = approver
        if approval_status is not None:
            self.approval_status = approval_status
        if approval_status_detail is not None:
            self.approval_status_detail = approval_status_detail
        if approval_type is not None:
            self.approval_type = approval_type
        if biz_type is not None:
            self.biz_type = biz_type
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this SearchApprovalsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this SearchApprovalsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this SearchApprovalsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this SearchApprovalsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def biz_id(self):
        """Gets the biz_id of this SearchApprovalsRequest.

        业务定义id

        :return: The biz_id of this SearchApprovalsRequest.
        :rtype: int
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        """Sets the biz_id of this SearchApprovalsRequest.

        业务定义id

        :param biz_id: The biz_id of this SearchApprovalsRequest.
        :type biz_id: int
        """
        self._biz_id = biz_id

    @property
    def name(self):
        """Gets the name of this SearchApprovalsRequest.

        按名称或编码模糊查询

        :return: The name of this SearchApprovalsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchApprovalsRequest.

        按名称或编码模糊查询

        :param name: The name of this SearchApprovalsRequest.
        :type name: str
        """
        self._name = name

    @property
    def create_by(self):
        """Gets the create_by of this SearchApprovalsRequest.

        按创建者查询

        :return: The create_by of this SearchApprovalsRequest.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this SearchApprovalsRequest.

        按创建者查询

        :param create_by: The create_by of this SearchApprovalsRequest.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def approver(self):
        """Gets the approver of this SearchApprovalsRequest.

        按审核人查询

        :return: The approver of this SearchApprovalsRequest.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        """Sets the approver of this SearchApprovalsRequest.

        按审核人查询

        :param approver: The approver of this SearchApprovalsRequest.
        :type approver: str
        """
        self._approver = approver

    @property
    def approval_status(self):
        """Gets the approval_status of this SearchApprovalsRequest.

        查询待审批，已审批

        :return: The approval_status of this SearchApprovalsRequest.
        :rtype: str
        """
        return self._approval_status

    @approval_status.setter
    def approval_status(self, approval_status):
        """Sets the approval_status of this SearchApprovalsRequest.

        查询待审批，已审批

        :param approval_status: The approval_status of this SearchApprovalsRequest.
        :type approval_status: str
        """
        self._approval_status = approval_status

    @property
    def approval_status_detail(self):
        """Gets the approval_status_detail of this SearchApprovalsRequest.

        查询待审批，已审批

        :return: The approval_status_detail of this SearchApprovalsRequest.
        :rtype: str
        """
        return self._approval_status_detail

    @approval_status_detail.setter
    def approval_status_detail(self, approval_status_detail):
        """Sets the approval_status_detail of this SearchApprovalsRequest.

        查询待审批，已审批

        :param approval_status_detail: The approval_status_detail of this SearchApprovalsRequest.
        :type approval_status_detail: str
        """
        self._approval_status_detail = approval_status_detail

    @property
    def approval_type(self):
        """Gets the approval_type of this SearchApprovalsRequest.

        业务审核类型

        :return: The approval_type of this SearchApprovalsRequest.
        :rtype: str
        """
        return self._approval_type

    @approval_type.setter
    def approval_type(self, approval_type):
        """Sets the approval_type of this SearchApprovalsRequest.

        业务审核类型

        :param approval_type: The approval_type of this SearchApprovalsRequest.
        :type approval_type: str
        """
        self._approval_type = approval_type

    @property
    def biz_type(self):
        """Gets the biz_type of this SearchApprovalsRequest.

        按业务类型查询

        :return: The biz_type of this SearchApprovalsRequest.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this SearchApprovalsRequest.

        按业务类型查询

        :param biz_type: The biz_type of this SearchApprovalsRequest.
        :type biz_type: str
        """
        self._biz_type = biz_type

    @property
    def begin_time(self):
        """Gets the begin_time of this SearchApprovalsRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :return: The begin_time of this SearchApprovalsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this SearchApprovalsRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :param begin_time: The begin_time of this SearchApprovalsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this SearchApprovalsRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :return: The end_time of this SearchApprovalsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SearchApprovalsRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :param end_time: The end_time of this SearchApprovalsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this SearchApprovalsRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :return: The limit of this SearchApprovalsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchApprovalsRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :param limit: The limit of this SearchApprovalsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this SearchApprovalsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :return: The offset of this SearchApprovalsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchApprovalsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :param offset: The offset of this SearchApprovalsRequest.
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
        if not isinstance(other, SearchApprovalsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
