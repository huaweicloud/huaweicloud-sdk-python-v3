# coding: utf-8

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
        'project_id': 'str',
        'project_ids': 'list[str]',
        'component_id': 'str',
        'name': 'str',
        'status': 'list[str]',
        'is_publish': 'bool',
        'creator_id': 'str',
        'creator_ids': 'list[str]',
        'executor_ids': 'list[str]',
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'group_path_id': 'str',
        'by_group': 'bool',
        'is_banned': 'bool',
        'query_new': 'bool',
        'security_level_list': 'list[int]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'project_ids': 'project_ids',
        'component_id': 'component_id',
        'name': 'name',
        'status': 'status',
        'is_publish': 'is_publish',
        'creator_id': 'creator_id',
        'creator_ids': 'creator_ids',
        'executor_ids': 'executor_ids',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'group_path_id': 'group_path_id',
        'by_group': 'by_group',
        'is_banned': 'is_banned',
        'query_new': 'query_new',
        'security_level_list': 'security_level_list'
    }

    def __init__(self, project_id=None, project_ids=None, component_id=None, name=None, status=None, is_publish=None, creator_id=None, creator_ids=None, executor_ids=None, start_time=None, end_time=None, offset=None, limit=None, sort_key=None, sort_dir=None, group_path_id=None, by_group=None, is_banned=None, query_new=None, security_level_list=None):
        r"""ListPipelineQuery

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**： CodeArts项目ID。 **约束限制**： 不涉及。 **取值范围**： 每个项目ID为32位字符，由数字和字母组成。 **默认取值**： 不涉及。 
        :type project_id: str
        :param project_ids: **参数解释**： CodeArts项目ID列表。 **约束限制**： 不涉及。 **取值范围**： 每个项目ID为32位字符，由数字和字母组成。 **默认取值**： 不涉及。 
        :type project_ids: list[str]
        :param component_id: **参数解释**： 微服务ID。可以通过[查询微服务列表](ListMicroservice.xml)接口获取，其中data.id即为微服务ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符串。 **默认取值**： 不涉及。 
        :type component_id: str
        :param name: **参数解释**： 流水线名称，支持模糊查询。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type name: str
        :param status: **参数解释**： 流水线状态列表。 **约束限制**： 不涉及。 **取值范围**： - COMPLETED：已完成。 - RUNNING：运行中。 - FAILED：失败。 - CANCELED：取消。 - PAUSED：暂停。 - SUSPEND：挂起。 - IGNORED：忽略。 **默认取值**： 不涉及。 
        :type status: list[str]
        :param is_publish: **参数解释**： 是否为变更流水线。 **约束限制**： 不涉及。 **取值范围**： - true：是变更流水线。 - false：非变更流水线。 **默认取值**： 不涉及。 
        :type is_publish: bool
        :param creator_id: **参数解释**： 创建人ID，用户的userId。 **约束限制**： 不涉及。 **取值范围**： 每个ID为32位字符串。 **默认取值**： 不涉及。 
        :type creator_id: str
        :param creator_ids: **参数解释**： 创建人ID列表。 **约束限制**： 不涉及。 **取值范围**： 每个ID为32位字符串。 **默认取值**： 不涉及。 
        :type creator_ids: list[str]
        :param executor_ids: **参数解释**： 执行人ID列表。 **约束限制**： 不涉及。 **取值范围**： 每个ID为32位字符串。 **默认取值**： 不涉及。 
        :type executor_ids: list[str]
        :param start_time: **参数解释**： 流水线开始时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type start_time: str
        :param end_time: **参数解释**： 流水线结束时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type end_time: str
        :param offset: **参数解释**： 起始偏移。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type offset: int
        :param limit: **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type limit: int
        :param sort_key: **参数解释**： 排序字段名称。 **约束限制**： 不涉及。 **取值范围**： - name：流水线名。 - create_time：创建时间。 - update_time：更新时间。 **默认取值**： 不涉及。 
        :type sort_key: str
        :param sort_dir: **参数解释**： 排序规则。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序。 **默认取值**： 不涉及。 
        :type sort_dir: str
        :param group_path_id: **参数解释**： 流水线分组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type group_path_id: str
        :param by_group: **参数解释**： 是否分组查询。 **约束限制**： 不涉及。 **取值范围**： - true：是分组查询。 - false：不是分组查询。 **默认取值**： 不涉及。 
        :type by_group: bool
        :param is_banned: **参数解释**： 是否包含被禁用的流水线。 **约束限制**： 不涉及。 **取值范围**： - true：包含被禁用的流水线。 - false：不包含被禁用的流水线。 **默认取值**： 不涉及。 
        :type is_banned: bool
        :param query_new: **参数解释**： 是否只查询新版流水线。 **约束限制**： 不涉及。 **取值范围**： - true：只查询新版流水线。 - false：不只查询新版流水线。 **默认取值**： true。 
        :type query_new: bool
        :param security_level_list: **参数解释**： 流水线密集等级。 **约束限制**： 非涉密场景无该字段。 **取值范围**： 零及以上正整数。 0：未设置密级。 1：最低密级。 **默认取值**： 不涉及。 
        :type security_level_list: list[int]
        """
        
        

        self._project_id = None
        self._project_ids = None
        self._component_id = None
        self._name = None
        self._status = None
        self._is_publish = None
        self._creator_id = None
        self._creator_ids = None
        self._executor_ids = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._group_path_id = None
        self._by_group = None
        self._is_banned = None
        self._query_new = None
        self._security_level_list = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
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
        if creator_id is not None:
            self.creator_id = creator_id
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
        if group_path_id is not None:
            self.group_path_id = group_path_id
        if by_group is not None:
            self.by_group = by_group
        if is_banned is not None:
            self.is_banned = is_banned
        if query_new is not None:
            self.query_new = query_new
        if security_level_list is not None:
            self.security_level_list = security_level_list

    @property
    def project_id(self):
        r"""Gets the project_id of this ListPipelineQuery.

        **参数解释**： CodeArts项目ID。 **约束限制**： 不涉及。 **取值范围**： 每个项目ID为32位字符，由数字和字母组成。 **默认取值**： 不涉及。 

        :return: The project_id of this ListPipelineQuery.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListPipelineQuery.

        **参数解释**： CodeArts项目ID。 **约束限制**： 不涉及。 **取值范围**： 每个项目ID为32位字符，由数字和字母组成。 **默认取值**： 不涉及。 

        :param project_id: The project_id of this ListPipelineQuery.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_ids(self):
        r"""Gets the project_ids of this ListPipelineQuery.

        **参数解释**： CodeArts项目ID列表。 **约束限制**： 不涉及。 **取值范围**： 每个项目ID为32位字符，由数字和字母组成。 **默认取值**： 不涉及。 

        :return: The project_ids of this ListPipelineQuery.
        :rtype: list[str]
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        r"""Sets the project_ids of this ListPipelineQuery.

        **参数解释**： CodeArts项目ID列表。 **约束限制**： 不涉及。 **取值范围**： 每个项目ID为32位字符，由数字和字母组成。 **默认取值**： 不涉及。 

        :param project_ids: The project_ids of this ListPipelineQuery.
        :type project_ids: list[str]
        """
        self._project_ids = project_ids

    @property
    def component_id(self):
        r"""Gets the component_id of this ListPipelineQuery.

        **参数解释**： 微服务ID。可以通过[查询微服务列表](ListMicroservice.xml)接口获取，其中data.id即为微服务ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符串。 **默认取值**： 不涉及。 

        :return: The component_id of this ListPipelineQuery.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ListPipelineQuery.

        **参数解释**： 微服务ID。可以通过[查询微服务列表](ListMicroservice.xml)接口获取，其中data.id即为微服务ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符串。 **默认取值**： 不涉及。 

        :param component_id: The component_id of this ListPipelineQuery.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def name(self):
        r"""Gets the name of this ListPipelineQuery.

        **参数解释**： 流水线名称，支持模糊查询。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The name of this ListPipelineQuery.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPipelineQuery.

        **参数解释**： 流水线名称，支持模糊查询。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param name: The name of this ListPipelineQuery.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListPipelineQuery.

        **参数解释**： 流水线状态列表。 **约束限制**： 不涉及。 **取值范围**： - COMPLETED：已完成。 - RUNNING：运行中。 - FAILED：失败。 - CANCELED：取消。 - PAUSED：暂停。 - SUSPEND：挂起。 - IGNORED：忽略。 **默认取值**： 不涉及。 

        :return: The status of this ListPipelineQuery.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPipelineQuery.

        **参数解释**： 流水线状态列表。 **约束限制**： 不涉及。 **取值范围**： - COMPLETED：已完成。 - RUNNING：运行中。 - FAILED：失败。 - CANCELED：取消。 - PAUSED：暂停。 - SUSPEND：挂起。 - IGNORED：忽略。 **默认取值**： 不涉及。 

        :param status: The status of this ListPipelineQuery.
        :type status: list[str]
        """
        self._status = status

    @property
    def is_publish(self):
        r"""Gets the is_publish of this ListPipelineQuery.

        **参数解释**： 是否为变更流水线。 **约束限制**： 不涉及。 **取值范围**： - true：是变更流水线。 - false：非变更流水线。 **默认取值**： 不涉及。 

        :return: The is_publish of this ListPipelineQuery.
        :rtype: bool
        """
        return self._is_publish

    @is_publish.setter
    def is_publish(self, is_publish):
        r"""Sets the is_publish of this ListPipelineQuery.

        **参数解释**： 是否为变更流水线。 **约束限制**： 不涉及。 **取值范围**： - true：是变更流水线。 - false：非变更流水线。 **默认取值**： 不涉及。 

        :param is_publish: The is_publish of this ListPipelineQuery.
        :type is_publish: bool
        """
        self._is_publish = is_publish

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ListPipelineQuery.

        **参数解释**： 创建人ID，用户的userId。 **约束限制**： 不涉及。 **取值范围**： 每个ID为32位字符串。 **默认取值**： 不涉及。 

        :return: The creator_id of this ListPipelineQuery.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ListPipelineQuery.

        **参数解释**： 创建人ID，用户的userId。 **约束限制**： 不涉及。 **取值范围**： 每个ID为32位字符串。 **默认取值**： 不涉及。 

        :param creator_id: The creator_id of this ListPipelineQuery.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_ids(self):
        r"""Gets the creator_ids of this ListPipelineQuery.

        **参数解释**： 创建人ID列表。 **约束限制**： 不涉及。 **取值范围**： 每个ID为32位字符串。 **默认取值**： 不涉及。 

        :return: The creator_ids of this ListPipelineQuery.
        :rtype: list[str]
        """
        return self._creator_ids

    @creator_ids.setter
    def creator_ids(self, creator_ids):
        r"""Sets the creator_ids of this ListPipelineQuery.

        **参数解释**： 创建人ID列表。 **约束限制**： 不涉及。 **取值范围**： 每个ID为32位字符串。 **默认取值**： 不涉及。 

        :param creator_ids: The creator_ids of this ListPipelineQuery.
        :type creator_ids: list[str]
        """
        self._creator_ids = creator_ids

    @property
    def executor_ids(self):
        r"""Gets the executor_ids of this ListPipelineQuery.

        **参数解释**： 执行人ID列表。 **约束限制**： 不涉及。 **取值范围**： 每个ID为32位字符串。 **默认取值**： 不涉及。 

        :return: The executor_ids of this ListPipelineQuery.
        :rtype: list[str]
        """
        return self._executor_ids

    @executor_ids.setter
    def executor_ids(self, executor_ids):
        r"""Sets the executor_ids of this ListPipelineQuery.

        **参数解释**： 执行人ID列表。 **约束限制**： 不涉及。 **取值范围**： 每个ID为32位字符串。 **默认取值**： 不涉及。 

        :param executor_ids: The executor_ids of this ListPipelineQuery.
        :type executor_ids: list[str]
        """
        self._executor_ids = executor_ids

    @property
    def start_time(self):
        r"""Gets the start_time of this ListPipelineQuery.

        **参数解释**： 流水线开始时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The start_time of this ListPipelineQuery.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListPipelineQuery.

        **参数解释**： 流水线开始时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param start_time: The start_time of this ListPipelineQuery.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListPipelineQuery.

        **参数解释**： 流水线结束时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The end_time of this ListPipelineQuery.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListPipelineQuery.

        **参数解释**： 流水线结束时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param end_time: The end_time of this ListPipelineQuery.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListPipelineQuery.

        **参数解释**： 起始偏移。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The offset of this ListPipelineQuery.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPipelineQuery.

        **参数解释**： 起始偏移。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param offset: The offset of this ListPipelineQuery.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPipelineQuery.

        **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The limit of this ListPipelineQuery.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPipelineQuery.

        **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param limit: The limit of this ListPipelineQuery.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListPipelineQuery.

        **参数解释**： 排序字段名称。 **约束限制**： 不涉及。 **取值范围**： - name：流水线名。 - create_time：创建时间。 - update_time：更新时间。 **默认取值**： 不涉及。 

        :return: The sort_key of this ListPipelineQuery.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListPipelineQuery.

        **参数解释**： 排序字段名称。 **约束限制**： 不涉及。 **取值范围**： - name：流水线名。 - create_time：创建时间。 - update_time：更新时间。 **默认取值**： 不涉及。 

        :param sort_key: The sort_key of this ListPipelineQuery.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListPipelineQuery.

        **参数解释**： 排序规则。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序。 **默认取值**： 不涉及。 

        :return: The sort_dir of this ListPipelineQuery.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListPipelineQuery.

        **参数解释**： 排序规则。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序。 **默认取值**： 不涉及。 

        :param sort_dir: The sort_dir of this ListPipelineQuery.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def group_path_id(self):
        r"""Gets the group_path_id of this ListPipelineQuery.

        **参数解释**： 流水线分组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The group_path_id of this ListPipelineQuery.
        :rtype: str
        """
        return self._group_path_id

    @group_path_id.setter
    def group_path_id(self, group_path_id):
        r"""Sets the group_path_id of this ListPipelineQuery.

        **参数解释**： 流水线分组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param group_path_id: The group_path_id of this ListPipelineQuery.
        :type group_path_id: str
        """
        self._group_path_id = group_path_id

    @property
    def by_group(self):
        r"""Gets the by_group of this ListPipelineQuery.

        **参数解释**： 是否分组查询。 **约束限制**： 不涉及。 **取值范围**： - true：是分组查询。 - false：不是分组查询。 **默认取值**： 不涉及。 

        :return: The by_group of this ListPipelineQuery.
        :rtype: bool
        """
        return self._by_group

    @by_group.setter
    def by_group(self, by_group):
        r"""Sets the by_group of this ListPipelineQuery.

        **参数解释**： 是否分组查询。 **约束限制**： 不涉及。 **取值范围**： - true：是分组查询。 - false：不是分组查询。 **默认取值**： 不涉及。 

        :param by_group: The by_group of this ListPipelineQuery.
        :type by_group: bool
        """
        self._by_group = by_group

    @property
    def is_banned(self):
        r"""Gets the is_banned of this ListPipelineQuery.

        **参数解释**： 是否包含被禁用的流水线。 **约束限制**： 不涉及。 **取值范围**： - true：包含被禁用的流水线。 - false：不包含被禁用的流水线。 **默认取值**： 不涉及。 

        :return: The is_banned of this ListPipelineQuery.
        :rtype: bool
        """
        return self._is_banned

    @is_banned.setter
    def is_banned(self, is_banned):
        r"""Sets the is_banned of this ListPipelineQuery.

        **参数解释**： 是否包含被禁用的流水线。 **约束限制**： 不涉及。 **取值范围**： - true：包含被禁用的流水线。 - false：不包含被禁用的流水线。 **默认取值**： 不涉及。 

        :param is_banned: The is_banned of this ListPipelineQuery.
        :type is_banned: bool
        """
        self._is_banned = is_banned

    @property
    def query_new(self):
        r"""Gets the query_new of this ListPipelineQuery.

        **参数解释**： 是否只查询新版流水线。 **约束限制**： 不涉及。 **取值范围**： - true：只查询新版流水线。 - false：不只查询新版流水线。 **默认取值**： true。 

        :return: The query_new of this ListPipelineQuery.
        :rtype: bool
        """
        return self._query_new

    @query_new.setter
    def query_new(self, query_new):
        r"""Sets the query_new of this ListPipelineQuery.

        **参数解释**： 是否只查询新版流水线。 **约束限制**： 不涉及。 **取值范围**： - true：只查询新版流水线。 - false：不只查询新版流水线。 **默认取值**： true。 

        :param query_new: The query_new of this ListPipelineQuery.
        :type query_new: bool
        """
        self._query_new = query_new

    @property
    def security_level_list(self):
        r"""Gets the security_level_list of this ListPipelineQuery.

        **参数解释**： 流水线密集等级。 **约束限制**： 非涉密场景无该字段。 **取值范围**： 零及以上正整数。 0：未设置密级。 1：最低密级。 **默认取值**： 不涉及。 

        :return: The security_level_list of this ListPipelineQuery.
        :rtype: list[int]
        """
        return self._security_level_list

    @security_level_list.setter
    def security_level_list(self, security_level_list):
        r"""Sets the security_level_list of this ListPipelineQuery.

        **参数解释**： 流水线密集等级。 **约束限制**： 非涉密场景无该字段。 **取值范围**： 零及以上正整数。 0：未设置密级。 1：最低密级。 **默认取值**： 不涉及。 

        :param security_level_list: The security_level_list of this ListPipelineQuery.
        :type security_level_list: list[int]
        """
        self._security_level_list = security_level_list

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
