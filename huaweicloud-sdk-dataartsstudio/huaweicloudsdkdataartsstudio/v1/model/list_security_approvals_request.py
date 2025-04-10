# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityApprovalsRequest:

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
        'limit': 'int',
        'offset': 'int',
        'proposer_name': 'str',
        'approval_id': 'str',
        'workspace_id': 'str',
        'status_list': 'list[int]',
        'application_start_time': 'int',
        'application_end_time': 'int',
        'order_by_desc': 'bool',
        'order_by': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'proposer_name': 'proposer_name',
        'approval_id': 'approval_id',
        'workspace_id': 'workspace_id',
        'status_list': 'status_list',
        'application_start_time': 'application_start_time',
        'application_end_time': 'application_end_time',
        'order_by_desc': 'order_by_desc',
        'order_by': 'order_by'
    }

    def __init__(self, workspace=None, limit=None, offset=None, proposer_name=None, approval_id=None, workspace_id=None, status_list=None, application_start_time=None, application_end_time=None, order_by_desc=None, order_by=None):
        r"""ListSecurityApprovalsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param proposer_name: 申请人名称
        :type proposer_name: str
        :param approval_id: 工单id
        :type approval_id: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param status_list: 工单状态
        :type status_list: list[int]
        :param application_start_time: 申请开始时间
        :type application_start_time: int
        :param application_end_time: 申请结束时间
        :type application_end_time: int
        :param order_by_desc: 升降序
        :type order_by_desc: bool
        :param order_by: 排序参数, START_TIME,END_TIME
        :type order_by: str
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._proposer_name = None
        self._approval_id = None
        self._workspace_id = None
        self._status_list = None
        self._application_start_time = None
        self._application_end_time = None
        self._order_by_desc = None
        self._order_by = None
        self.discriminator = None

        self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if proposer_name is not None:
            self.proposer_name = proposer_name
        if approval_id is not None:
            self.approval_id = approval_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if status_list is not None:
            self.status_list = status_list
        if application_start_time is not None:
            self.application_start_time = application_start_time
        if application_end_time is not None:
            self.application_end_time = application_end_time
        if order_by_desc is not None:
            self.order_by_desc = order_by_desc
        if order_by is not None:
            self.order_by = order_by

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecurityApprovalsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityApprovalsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecurityApprovalsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityApprovalsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityApprovalsRequest.

        limit

        :return: The limit of this ListSecurityApprovalsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityApprovalsRequest.

        limit

        :param limit: The limit of this ListSecurityApprovalsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityApprovalsRequest.

        offset

        :return: The offset of this ListSecurityApprovalsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityApprovalsRequest.

        offset

        :param offset: The offset of this ListSecurityApprovalsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def proposer_name(self):
        r"""Gets the proposer_name of this ListSecurityApprovalsRequest.

        申请人名称

        :return: The proposer_name of this ListSecurityApprovalsRequest.
        :rtype: str
        """
        return self._proposer_name

    @proposer_name.setter
    def proposer_name(self, proposer_name):
        r"""Sets the proposer_name of this ListSecurityApprovalsRequest.

        申请人名称

        :param proposer_name: The proposer_name of this ListSecurityApprovalsRequest.
        :type proposer_name: str
        """
        self._proposer_name = proposer_name

    @property
    def approval_id(self):
        r"""Gets the approval_id of this ListSecurityApprovalsRequest.

        工单id

        :return: The approval_id of this ListSecurityApprovalsRequest.
        :rtype: str
        """
        return self._approval_id

    @approval_id.setter
    def approval_id(self, approval_id):
        r"""Sets the approval_id of this ListSecurityApprovalsRequest.

        工单id

        :param approval_id: The approval_id of this ListSecurityApprovalsRequest.
        :type approval_id: str
        """
        self._approval_id = approval_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListSecurityApprovalsRequest.

        工作空间id

        :return: The workspace_id of this ListSecurityApprovalsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListSecurityApprovalsRequest.

        工作空间id

        :param workspace_id: The workspace_id of this ListSecurityApprovalsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def status_list(self):
        r"""Gets the status_list of this ListSecurityApprovalsRequest.

        工单状态

        :return: The status_list of this ListSecurityApprovalsRequest.
        :rtype: list[int]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this ListSecurityApprovalsRequest.

        工单状态

        :param status_list: The status_list of this ListSecurityApprovalsRequest.
        :type status_list: list[int]
        """
        self._status_list = status_list

    @property
    def application_start_time(self):
        r"""Gets the application_start_time of this ListSecurityApprovalsRequest.

        申请开始时间

        :return: The application_start_time of this ListSecurityApprovalsRequest.
        :rtype: int
        """
        return self._application_start_time

    @application_start_time.setter
    def application_start_time(self, application_start_time):
        r"""Sets the application_start_time of this ListSecurityApprovalsRequest.

        申请开始时间

        :param application_start_time: The application_start_time of this ListSecurityApprovalsRequest.
        :type application_start_time: int
        """
        self._application_start_time = application_start_time

    @property
    def application_end_time(self):
        r"""Gets the application_end_time of this ListSecurityApprovalsRequest.

        申请结束时间

        :return: The application_end_time of this ListSecurityApprovalsRequest.
        :rtype: int
        """
        return self._application_end_time

    @application_end_time.setter
    def application_end_time(self, application_end_time):
        r"""Sets the application_end_time of this ListSecurityApprovalsRequest.

        申请结束时间

        :param application_end_time: The application_end_time of this ListSecurityApprovalsRequest.
        :type application_end_time: int
        """
        self._application_end_time = application_end_time

    @property
    def order_by_desc(self):
        r"""Gets the order_by_desc of this ListSecurityApprovalsRequest.

        升降序

        :return: The order_by_desc of this ListSecurityApprovalsRequest.
        :rtype: bool
        """
        return self._order_by_desc

    @order_by_desc.setter
    def order_by_desc(self, order_by_desc):
        r"""Sets the order_by_desc of this ListSecurityApprovalsRequest.

        升降序

        :param order_by_desc: The order_by_desc of this ListSecurityApprovalsRequest.
        :type order_by_desc: bool
        """
        self._order_by_desc = order_by_desc

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSecurityApprovalsRequest.

        排序参数, START_TIME,END_TIME

        :return: The order_by of this ListSecurityApprovalsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSecurityApprovalsRequest.

        排序参数, START_TIME,END_TIME

        :param order_by: The order_by of this ListSecurityApprovalsRequest.
        :type order_by: str
        """
        self._order_by = order_by

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
        if not isinstance(other, ListSecurityApprovalsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
