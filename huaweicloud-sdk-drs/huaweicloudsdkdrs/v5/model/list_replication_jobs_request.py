# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReplicationJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'name': 'str',
        'status': 'str',
        'dbs_instance_ids': 'list[str]',
        'description': 'str',
        'create_at': 'str',
        'completed_at': 'str',
        'enterprise_project_id': 'str',
        'tags': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'name': 'name',
        'status': 'status',
        'dbs_instance_ids': 'dbs_instance_ids',
        'description': 'description',
        'create_at': 'create_at',
        'completed_at': 'completed_at',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'limit': 'limit',
        'offset': 'offset',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, x_language=None, name=None, status=None, dbs_instance_ids=None, description=None, create_at=None, completed_at=None, enterprise_project_id=None, tags=None, limit=None, offset=None, sort_key=None, sort_dir=None):
        r"""ListReplicationJobsRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。 en-us：英文 zh-cn：中文
        :type x_language: str
        :param name: 任务名称，支持模糊搜索。
        :type name: str
        :param status: 备份迁移任务状态。 TRANSFERRING：恢复中 SUCCESS：成功 FAILED：失败 PRECHECK FAILED：预检查失败
        :type status: str
        :param dbs_instance_ids: 数据库实例ID，最大数量为10。
        :type dbs_instance_ids: list[str]
        :param description: 描述。
        :type description: str
        :param create_at: 创建时间。
        :type create_at: str
        :param completed_at: 完成时间。
        :type completed_at: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param tags: 标签。
        :type tags: str
        :param limit: 查询返回记录的数量限制，默认值为10。
        :type limit: int
        :param offset: 偏移量，默认值为0，表示查询该偏移量后面的记录。
        :type offset: int
        :param sort_key: 排序字段。
        :type sort_key: str
        :param sort_dir: 排序方法。
        :type sort_dir: str
        """
        
        

        self._x_language = None
        self._name = None
        self._status = None
        self._dbs_instance_ids = None
        self._description = None
        self._create_at = None
        self._completed_at = None
        self._enterprise_project_id = None
        self._tags = None
        self._limit = None
        self._offset = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if dbs_instance_ids is not None:
            self.dbs_instance_ids = dbs_instance_ids
        if description is not None:
            self.description = description
        if create_at is not None:
            self.create_at = create_at
        if completed_at is not None:
            self.completed_at = completed_at
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def x_language(self):
        r"""Gets the x_language of this ListReplicationJobsRequest.

        请求语言类型。 en-us：英文 zh-cn：中文

        :return: The x_language of this ListReplicationJobsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListReplicationJobsRequest.

        请求语言类型。 en-us：英文 zh-cn：中文

        :param x_language: The x_language of this ListReplicationJobsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def name(self):
        r"""Gets the name of this ListReplicationJobsRequest.

        任务名称，支持模糊搜索。

        :return: The name of this ListReplicationJobsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListReplicationJobsRequest.

        任务名称，支持模糊搜索。

        :param name: The name of this ListReplicationJobsRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListReplicationJobsRequest.

        备份迁移任务状态。 TRANSFERRING：恢复中 SUCCESS：成功 FAILED：失败 PRECHECK FAILED：预检查失败

        :return: The status of this ListReplicationJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListReplicationJobsRequest.

        备份迁移任务状态。 TRANSFERRING：恢复中 SUCCESS：成功 FAILED：失败 PRECHECK FAILED：预检查失败

        :param status: The status of this ListReplicationJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def dbs_instance_ids(self):
        r"""Gets the dbs_instance_ids of this ListReplicationJobsRequest.

        数据库实例ID，最大数量为10。

        :return: The dbs_instance_ids of this ListReplicationJobsRequest.
        :rtype: list[str]
        """
        return self._dbs_instance_ids

    @dbs_instance_ids.setter
    def dbs_instance_ids(self, dbs_instance_ids):
        r"""Sets the dbs_instance_ids of this ListReplicationJobsRequest.

        数据库实例ID，最大数量为10。

        :param dbs_instance_ids: The dbs_instance_ids of this ListReplicationJobsRequest.
        :type dbs_instance_ids: list[str]
        """
        self._dbs_instance_ids = dbs_instance_ids

    @property
    def description(self):
        r"""Gets the description of this ListReplicationJobsRequest.

        描述。

        :return: The description of this ListReplicationJobsRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListReplicationJobsRequest.

        描述。

        :param description: The description of this ListReplicationJobsRequest.
        :type description: str
        """
        self._description = description

    @property
    def create_at(self):
        r"""Gets the create_at of this ListReplicationJobsRequest.

        创建时间。

        :return: The create_at of this ListReplicationJobsRequest.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ListReplicationJobsRequest.

        创建时间。

        :param create_at: The create_at of this ListReplicationJobsRequest.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def completed_at(self):
        r"""Gets the completed_at of this ListReplicationJobsRequest.

        完成时间。

        :return: The completed_at of this ListReplicationJobsRequest.
        :rtype: str
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        r"""Sets the completed_at of this ListReplicationJobsRequest.

        完成时间。

        :param completed_at: The completed_at of this ListReplicationJobsRequest.
        :type completed_at: str
        """
        self._completed_at = completed_at

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListReplicationJobsRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListReplicationJobsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListReplicationJobsRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListReplicationJobsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this ListReplicationJobsRequest.

        标签。

        :return: The tags of this ListReplicationJobsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListReplicationJobsRequest.

        标签。

        :param tags: The tags of this ListReplicationJobsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def limit(self):
        r"""Gets the limit of this ListReplicationJobsRequest.

        查询返回记录的数量限制，默认值为10。

        :return: The limit of this ListReplicationJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListReplicationJobsRequest.

        查询返回记录的数量限制，默认值为10。

        :param limit: The limit of this ListReplicationJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListReplicationJobsRequest.

        偏移量，默认值为0，表示查询该偏移量后面的记录。

        :return: The offset of this ListReplicationJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListReplicationJobsRequest.

        偏移量，默认值为0，表示查询该偏移量后面的记录。

        :param offset: The offset of this ListReplicationJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListReplicationJobsRequest.

        排序字段。

        :return: The sort_key of this ListReplicationJobsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListReplicationJobsRequest.

        排序字段。

        :param sort_key: The sort_key of this ListReplicationJobsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListReplicationJobsRequest.

        排序方法。

        :return: The sort_dir of this ListReplicationJobsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListReplicationJobsRequest.

        排序方法。

        :param sort_dir: The sort_dir of this ListReplicationJobsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListReplicationJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
