# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchSubjectRequest:

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
        'owner': 'str',
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'parent_id': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'name': 'name',
        'create_by': 'create_by',
        'owner': 'owner',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'parent_id': 'parent_id'
    }

    def __init__(self, workspace=None, name=None, create_by=None, owner=None, status=None, begin_time=None, end_time=None, limit=None, offset=None, parent_id=None):
        """SearchSubjectRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param name: 按名称或编码模糊查询
        :type name: str
        :param create_by: 按创建者查询
        :type create_by: str
        :param owner: 按负责人查询
        :type owner: str
        :param status: 业务状态
        :type status: str
        :param begin_time: 时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效
        :type begin_time: str
        :param end_time: 时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效
        :type end_time: str
        :param limit: 查询条数，即查询Y条数据。默认值50，取值范围[1,100]
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0
        :type offset: int
        :param parent_id: 父目录ID，根节点没有此ID，空值为所有，-1为根节点下节点
        :type parent_id: int
        """
        
        

        self._workspace = None
        self._name = None
        self._create_by = None
        self._owner = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._parent_id = None
        self.discriminator = None

        self.workspace = workspace
        if name is not None:
            self.name = name
        if create_by is not None:
            self.create_by = create_by
        if owner is not None:
            self.owner = owner
        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def workspace(self):
        """Gets the workspace of this SearchSubjectRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this SearchSubjectRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this SearchSubjectRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this SearchSubjectRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def name(self):
        """Gets the name of this SearchSubjectRequest.

        按名称或编码模糊查询

        :return: The name of this SearchSubjectRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchSubjectRequest.

        按名称或编码模糊查询

        :param name: The name of this SearchSubjectRequest.
        :type name: str
        """
        self._name = name

    @property
    def create_by(self):
        """Gets the create_by of this SearchSubjectRequest.

        按创建者查询

        :return: The create_by of this SearchSubjectRequest.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this SearchSubjectRequest.

        按创建者查询

        :param create_by: The create_by of this SearchSubjectRequest.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def owner(self):
        """Gets the owner of this SearchSubjectRequest.

        按负责人查询

        :return: The owner of this SearchSubjectRequest.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this SearchSubjectRequest.

        按负责人查询

        :param owner: The owner of this SearchSubjectRequest.
        :type owner: str
        """
        self._owner = owner

    @property
    def status(self):
        """Gets the status of this SearchSubjectRequest.

        业务状态

        :return: The status of this SearchSubjectRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchSubjectRequest.

        业务状态

        :param status: The status of this SearchSubjectRequest.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        """Gets the begin_time of this SearchSubjectRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :return: The begin_time of this SearchSubjectRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this SearchSubjectRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :param begin_time: The begin_time of this SearchSubjectRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this SearchSubjectRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :return: The end_time of this SearchSubjectRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SearchSubjectRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :param end_time: The end_time of this SearchSubjectRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this SearchSubjectRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :return: The limit of this SearchSubjectRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchSubjectRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :param limit: The limit of this SearchSubjectRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this SearchSubjectRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :return: The offset of this SearchSubjectRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchSubjectRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :param offset: The offset of this SearchSubjectRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def parent_id(self):
        """Gets the parent_id of this SearchSubjectRequest.

        父目录ID，根节点没有此ID，空值为所有，-1为根节点下节点

        :return: The parent_id of this SearchSubjectRequest.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this SearchSubjectRequest.

        父目录ID，根节点没有此ID，空值为所有，-1为根节点下节点

        :param parent_id: The parent_id of this SearchSubjectRequest.
        :type parent_id: int
        """
        self._parent_id = parent_id

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
        if not isinstance(other, SearchSubjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
