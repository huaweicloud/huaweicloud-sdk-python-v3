# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelineQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_ids': 'list[str]',
        'component_id': 'str',
        'name': 'str',
        'status': 'list[str]',
        'is_publish': 'bool',
        'creator_ids': 'list[str]',
        'executor_ids': 'list[str]',
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'project_ids': 'project_ids',
        'component_id': 'component_id',
        'name': 'name',
        'status': 'status',
        'is_publish': 'is_publish',
        'creator_ids': 'creator_ids',
        'executor_ids': 'executor_ids',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, project_ids=None, component_id=None, name=None, status=None, is_publish=None, creator_ids=None, executor_ids=None, start_time=None, end_time=None, offset=None, limit=None, sort_key=None, sort_dir=None):
        """ListPipelineQuery

        The model defined in huaweicloud sdk

        :param project_ids: 项目ID列表
        :type project_ids: list[str]
        :param component_id: 组件ID
        :type component_id: str
        :param name: 流水线名称
        :type name: str
        :param status: 状态
        :type status: list[str]
        :param is_publish: 是否为变更流水线
        :type is_publish: bool
        :param creator_ids: 创建人ID列表
        :type creator_ids: list[str]
        :param executor_ids: 执行人ID列表
        :type executor_ids: list[str]
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param offset: 起始偏移
        :type offset: int
        :param limit: 查询数量
        :type limit: int
        :param sort_key: 排序字段名称
        :type sort_key: str
        :param sort_dir: 排序规则
        :type sort_dir: str
        """
        
        

        self._project_ids = None
        self._component_id = None
        self._name = None
        self._status = None
        self._is_publish = None
        self._creator_ids = None
        self._executor_ids = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if project_ids is not None:
            self.project_ids = project_ids
        if component_id is not None:
            self.component_id = component_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if is_publish is not None:
            self.is_publish = is_publish
        if creator_ids is not None:
            self.creator_ids = creator_ids
        if executor_ids is not None:
            self.executor_ids = executor_ids
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def project_ids(self):
        """Gets the project_ids of this ListPipelineQuery.

        项目ID列表

        :return: The project_ids of this ListPipelineQuery.
        :rtype: list[str]
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        """Sets the project_ids of this ListPipelineQuery.

        项目ID列表

        :param project_ids: The project_ids of this ListPipelineQuery.
        :type project_ids: list[str]
        """
        self._project_ids = project_ids

    @property
    def component_id(self):
        """Gets the component_id of this ListPipelineQuery.

        组件ID

        :return: The component_id of this ListPipelineQuery.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ListPipelineQuery.

        组件ID

        :param component_id: The component_id of this ListPipelineQuery.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def name(self):
        """Gets the name of this ListPipelineQuery.

        流水线名称

        :return: The name of this ListPipelineQuery.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPipelineQuery.

        流水线名称

        :param name: The name of this ListPipelineQuery.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListPipelineQuery.

        状态

        :return: The status of this ListPipelineQuery.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPipelineQuery.

        状态

        :param status: The status of this ListPipelineQuery.
        :type status: list[str]
        """
        self._status = status

    @property
    def is_publish(self):
        """Gets the is_publish of this ListPipelineQuery.

        是否为变更流水线

        :return: The is_publish of this ListPipelineQuery.
        :rtype: bool
        """
        return self._is_publish

    @is_publish.setter
    def is_publish(self, is_publish):
        """Sets the is_publish of this ListPipelineQuery.

        是否为变更流水线

        :param is_publish: The is_publish of this ListPipelineQuery.
        :type is_publish: bool
        """
        self._is_publish = is_publish

    @property
    def creator_ids(self):
        """Gets the creator_ids of this ListPipelineQuery.

        创建人ID列表

        :return: The creator_ids of this ListPipelineQuery.
        :rtype: list[str]
        """
        return self._creator_ids

    @creator_ids.setter
    def creator_ids(self, creator_ids):
        """Sets the creator_ids of this ListPipelineQuery.

        创建人ID列表

        :param creator_ids: The creator_ids of this ListPipelineQuery.
        :type creator_ids: list[str]
        """
        self._creator_ids = creator_ids

    @property
    def executor_ids(self):
        """Gets the executor_ids of this ListPipelineQuery.

        执行人ID列表

        :return: The executor_ids of this ListPipelineQuery.
        :rtype: list[str]
        """
        return self._executor_ids

    @executor_ids.setter
    def executor_ids(self, executor_ids):
        """Sets the executor_ids of this ListPipelineQuery.

        执行人ID列表

        :param executor_ids: The executor_ids of this ListPipelineQuery.
        :type executor_ids: list[str]
        """
        self._executor_ids = executor_ids

    @property
    def start_time(self):
        """Gets the start_time of this ListPipelineQuery.

        开始时间

        :return: The start_time of this ListPipelineQuery.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListPipelineQuery.

        开始时间

        :param start_time: The start_time of this ListPipelineQuery.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListPipelineQuery.

        结束时间

        :return: The end_time of this ListPipelineQuery.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListPipelineQuery.

        结束时间

        :param end_time: The end_time of this ListPipelineQuery.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this ListPipelineQuery.

        起始偏移

        :return: The offset of this ListPipelineQuery.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPipelineQuery.

        起始偏移

        :param offset: The offset of this ListPipelineQuery.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPipelineQuery.

        查询数量

        :return: The limit of this ListPipelineQuery.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPipelineQuery.

        查询数量

        :param limit: The limit of this ListPipelineQuery.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        """Gets the sort_key of this ListPipelineQuery.

        排序字段名称

        :return: The sort_key of this ListPipelineQuery.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListPipelineQuery.

        排序字段名称

        :param sort_key: The sort_key of this ListPipelineQuery.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListPipelineQuery.

        排序规则

        :return: The sort_dir of this ListPipelineQuery.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListPipelineQuery.

        排序规则

        :param sort_dir: The sort_dir of this ListPipelineQuery.
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
        if not isinstance(other, ListPipelineQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
