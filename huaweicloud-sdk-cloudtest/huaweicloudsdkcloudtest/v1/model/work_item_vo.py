# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'owner': 'str',
        'path': 'str',
        'start_date': 'str',
        'due_date': 'str',
        'region': 'str',
        'creator': 'str',
        'updator': 'str',
        'project_uuid': 'str',
        'work_item_id': 'str',
        'status_id': 'str',
        'status_name': 'str',
        'tracker_id': 'str',
        'tracker_name': 'str',
        'iteration_id': 'str',
        'module_id': 'str',
        'severity_id': 'str',
        'severity_name': 'str',
        'parent_workitem_id': 'str',
        'board_id': 'str',
        'board_name': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'iteration_name': 'str',
        'module_name': 'str',
        'module_path': 'str',
        'module_path_name': 'str',
        'owner_name': 'str',
        'have_child_dynamic': 'bool',
        'has_child': 'bool',
        'issue_dynamic_count': 'int',
        'case_count': 'int',
        'sequence_id': 'str',
        'pi_id': 'str',
        'pi_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'owner': 'owner',
        'path': 'path',
        'start_date': 'start_date',
        'due_date': 'due_date',
        'region': 'region',
        'creator': 'creator',
        'updator': 'updator',
        'project_uuid': 'project_uuid',
        'work_item_id': 'work_item_id',
        'status_id': 'status_id',
        'status_name': 'status_name',
        'tracker_id': 'tracker_id',
        'tracker_name': 'tracker_name',
        'iteration_id': 'iteration_id',
        'module_id': 'module_id',
        'severity_id': 'severity_id',
        'severity_name': 'severity_name',
        'parent_workitem_id': 'parent_workitem_id',
        'board_id': 'board_id',
        'board_name': 'board_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'iteration_name': 'iteration_name',
        'module_name': 'module_name',
        'module_path': 'module_path',
        'module_path_name': 'module_path_name',
        'owner_name': 'owner_name',
        'have_child_dynamic': 'have_child_dynamic',
        'has_child': 'has_child',
        'issue_dynamic_count': 'issue_dynamic_count',
        'case_count': 'case_count',
        'sequence_id': 'sequence_id',
        'pi_id': 'pi_id',
        'pi_name': 'pi_name'
    }

    def __init__(self, name=None, owner=None, path=None, start_date=None, due_date=None, region=None, creator=None, updator=None, project_uuid=None, work_item_id=None, status_id=None, status_name=None, tracker_id=None, tracker_name=None, iteration_id=None, module_id=None, severity_id=None, severity_name=None, parent_workitem_id=None, board_id=None, board_name=None, create_time=None, update_time=None, iteration_name=None, module_name=None, module_path=None, module_path_name=None, owner_name=None, have_child_dynamic=None, has_child=None, issue_dynamic_count=None, case_count=None, sequence_id=None, pi_id=None, pi_name=None):
        r"""WorkItemVo

        The model defined in huaweicloud sdk

        :param name: 工作项名称
        :type name: str
        :param owner: 处理人
        :type owner: str
        :param path: 工作项路径
        :type path: str
        :param start_date: 预计开始日期
        :type start_date: str
        :param due_date: 预计结束日期
        :type due_date: str
        :param region: 逻辑region，外部使用公有云实际区域，内部使用默认值
        :type region: str
        :param creator: 创建人
        :type creator: str
        :param updator: 更新人
        :type updator: str
        :param project_uuid: 项目ID，外部使用项目ID，内部使用默认值
        :type project_uuid: str
        :param work_item_id: 工作项编号
        :type work_item_id: str
        :param status_id: 状态ID
        :type status_id: str
        :param status_name: 状态
        :type status_name: str
        :param tracker_id: 类型ID
        :type tracker_id: str
        :param tracker_name: 类型
        :type tracker_name: str
        :param iteration_id: 迭代ID
        :type iteration_id: str
        :param module_id: 模块ID
        :type module_id: str
        :param severity_id: 重要程度ID
        :type severity_id: str
        :param severity_name: 重要程度
        :type severity_name: str
        :param parent_workitem_id: 父工作项编号
        :type parent_workitem_id: str
        :param board_id: 看板ID
        :type board_id: str
        :param board_name: 看板
        :type board_name: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param iteration_name: 迭代名
        :type iteration_name: str
        :param module_name: 模块名
        :type module_name: str
        :param module_path: 模块path
        :type module_path: str
        :param module_path_name: 模块路径名称
        :type module_path_name: str
        :param owner_name: 处理人
        :type owner_name: str
        :param have_child_dynamic: 父工作项下是否有子工作项包含动态
        :type have_child_dynamic: bool
        :param has_child: 父工作项下是否有子工作项
        :type has_child: bool
        :param issue_dynamic_count: 需求动态数量
        :type issue_dynamic_count: int
        :param case_count: 用例数量
        :type case_count: int
        :param sequence_id: xBoard项目工作项序列号
        :type sequence_id: str
        :param pi_id: pi的id，层级关系：pi -&gt; 迭代 -&gt; 需求
        :type pi_id: str
        :param pi_name: 迭代ID
        :type pi_name: str
        """
        
        

        self._name = None
        self._owner = None
        self._path = None
        self._start_date = None
        self._due_date = None
        self._region = None
        self._creator = None
        self._updator = None
        self._project_uuid = None
        self._work_item_id = None
        self._status_id = None
        self._status_name = None
        self._tracker_id = None
        self._tracker_name = None
        self._iteration_id = None
        self._module_id = None
        self._severity_id = None
        self._severity_name = None
        self._parent_workitem_id = None
        self._board_id = None
        self._board_name = None
        self._create_time = None
        self._update_time = None
        self._iteration_name = None
        self._module_name = None
        self._module_path = None
        self._module_path_name = None
        self._owner_name = None
        self._have_child_dynamic = None
        self._has_child = None
        self._issue_dynamic_count = None
        self._case_count = None
        self._sequence_id = None
        self._pi_id = None
        self._pi_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if path is not None:
            self.path = path
        if start_date is not None:
            self.start_date = start_date
        if due_date is not None:
            self.due_date = due_date
        if region is not None:
            self.region = region
        if creator is not None:
            self.creator = creator
        if updator is not None:
            self.updator = updator
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if work_item_id is not None:
            self.work_item_id = work_item_id
        if status_id is not None:
            self.status_id = status_id
        if status_name is not None:
            self.status_name = status_name
        if tracker_id is not None:
            self.tracker_id = tracker_id
        if tracker_name is not None:
            self.tracker_name = tracker_name
        if iteration_id is not None:
            self.iteration_id = iteration_id
        if module_id is not None:
            self.module_id = module_id
        if severity_id is not None:
            self.severity_id = severity_id
        if severity_name is not None:
            self.severity_name = severity_name
        if parent_workitem_id is not None:
            self.parent_workitem_id = parent_workitem_id
        if board_id is not None:
            self.board_id = board_id
        if board_name is not None:
            self.board_name = board_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if iteration_name is not None:
            self.iteration_name = iteration_name
        if module_name is not None:
            self.module_name = module_name
        if module_path is not None:
            self.module_path = module_path
        if module_path_name is not None:
            self.module_path_name = module_path_name
        if owner_name is not None:
            self.owner_name = owner_name
        if have_child_dynamic is not None:
            self.have_child_dynamic = have_child_dynamic
        if has_child is not None:
            self.has_child = has_child
        if issue_dynamic_count is not None:
            self.issue_dynamic_count = issue_dynamic_count
        if case_count is not None:
            self.case_count = case_count
        if sequence_id is not None:
            self.sequence_id = sequence_id
        if pi_id is not None:
            self.pi_id = pi_id
        if pi_name is not None:
            self.pi_name = pi_name

    @property
    def name(self):
        r"""Gets the name of this WorkItemVo.

        工作项名称

        :return: The name of this WorkItemVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkItemVo.

        工作项名称

        :param name: The name of this WorkItemVo.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        r"""Gets the owner of this WorkItemVo.

        处理人

        :return: The owner of this WorkItemVo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this WorkItemVo.

        处理人

        :param owner: The owner of this WorkItemVo.
        :type owner: str
        """
        self._owner = owner

    @property
    def path(self):
        r"""Gets the path of this WorkItemVo.

        工作项路径

        :return: The path of this WorkItemVo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this WorkItemVo.

        工作项路径

        :param path: The path of this WorkItemVo.
        :type path: str
        """
        self._path = path

    @property
    def start_date(self):
        r"""Gets the start_date of this WorkItemVo.

        预计开始日期

        :return: The start_date of this WorkItemVo.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this WorkItemVo.

        预计开始日期

        :param start_date: The start_date of this WorkItemVo.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def due_date(self):
        r"""Gets the due_date of this WorkItemVo.

        预计结束日期

        :return: The due_date of this WorkItemVo.
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        r"""Sets the due_date of this WorkItemVo.

        预计结束日期

        :param due_date: The due_date of this WorkItemVo.
        :type due_date: str
        """
        self._due_date = due_date

    @property
    def region(self):
        r"""Gets the region of this WorkItemVo.

        逻辑region，外部使用公有云实际区域，内部使用默认值

        :return: The region of this WorkItemVo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this WorkItemVo.

        逻辑region，外部使用公有云实际区域，内部使用默认值

        :param region: The region of this WorkItemVo.
        :type region: str
        """
        self._region = region

    @property
    def creator(self):
        r"""Gets the creator of this WorkItemVo.

        创建人

        :return: The creator of this WorkItemVo.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this WorkItemVo.

        创建人

        :param creator: The creator of this WorkItemVo.
        :type creator: str
        """
        self._creator = creator

    @property
    def updator(self):
        r"""Gets the updator of this WorkItemVo.

        更新人

        :return: The updator of this WorkItemVo.
        :rtype: str
        """
        return self._updator

    @updator.setter
    def updator(self, updator):
        r"""Sets the updator of this WorkItemVo.

        更新人

        :param updator: The updator of this WorkItemVo.
        :type updator: str
        """
        self._updator = updator

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this WorkItemVo.

        项目ID，外部使用项目ID，内部使用默认值

        :return: The project_uuid of this WorkItemVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this WorkItemVo.

        项目ID，外部使用项目ID，内部使用默认值

        :param project_uuid: The project_uuid of this WorkItemVo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def work_item_id(self):
        r"""Gets the work_item_id of this WorkItemVo.

        工作项编号

        :return: The work_item_id of this WorkItemVo.
        :rtype: str
        """
        return self._work_item_id

    @work_item_id.setter
    def work_item_id(self, work_item_id):
        r"""Sets the work_item_id of this WorkItemVo.

        工作项编号

        :param work_item_id: The work_item_id of this WorkItemVo.
        :type work_item_id: str
        """
        self._work_item_id = work_item_id

    @property
    def status_id(self):
        r"""Gets the status_id of this WorkItemVo.

        状态ID

        :return: The status_id of this WorkItemVo.
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        r"""Sets the status_id of this WorkItemVo.

        状态ID

        :param status_id: The status_id of this WorkItemVo.
        :type status_id: str
        """
        self._status_id = status_id

    @property
    def status_name(self):
        r"""Gets the status_name of this WorkItemVo.

        状态

        :return: The status_name of this WorkItemVo.
        :rtype: str
        """
        return self._status_name

    @status_name.setter
    def status_name(self, status_name):
        r"""Sets the status_name of this WorkItemVo.

        状态

        :param status_name: The status_name of this WorkItemVo.
        :type status_name: str
        """
        self._status_name = status_name

    @property
    def tracker_id(self):
        r"""Gets the tracker_id of this WorkItemVo.

        类型ID

        :return: The tracker_id of this WorkItemVo.
        :rtype: str
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        r"""Sets the tracker_id of this WorkItemVo.

        类型ID

        :param tracker_id: The tracker_id of this WorkItemVo.
        :type tracker_id: str
        """
        self._tracker_id = tracker_id

    @property
    def tracker_name(self):
        r"""Gets the tracker_name of this WorkItemVo.

        类型

        :return: The tracker_name of this WorkItemVo.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        r"""Sets the tracker_name of this WorkItemVo.

        类型

        :param tracker_name: The tracker_name of this WorkItemVo.
        :type tracker_name: str
        """
        self._tracker_name = tracker_name

    @property
    def iteration_id(self):
        r"""Gets the iteration_id of this WorkItemVo.

        迭代ID

        :return: The iteration_id of this WorkItemVo.
        :rtype: str
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        r"""Sets the iteration_id of this WorkItemVo.

        迭代ID

        :param iteration_id: The iteration_id of this WorkItemVo.
        :type iteration_id: str
        """
        self._iteration_id = iteration_id

    @property
    def module_id(self):
        r"""Gets the module_id of this WorkItemVo.

        模块ID

        :return: The module_id of this WorkItemVo.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this WorkItemVo.

        模块ID

        :param module_id: The module_id of this WorkItemVo.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def severity_id(self):
        r"""Gets the severity_id of this WorkItemVo.

        重要程度ID

        :return: The severity_id of this WorkItemVo.
        :rtype: str
        """
        return self._severity_id

    @severity_id.setter
    def severity_id(self, severity_id):
        r"""Sets the severity_id of this WorkItemVo.

        重要程度ID

        :param severity_id: The severity_id of this WorkItemVo.
        :type severity_id: str
        """
        self._severity_id = severity_id

    @property
    def severity_name(self):
        r"""Gets the severity_name of this WorkItemVo.

        重要程度

        :return: The severity_name of this WorkItemVo.
        :rtype: str
        """
        return self._severity_name

    @severity_name.setter
    def severity_name(self, severity_name):
        r"""Sets the severity_name of this WorkItemVo.

        重要程度

        :param severity_name: The severity_name of this WorkItemVo.
        :type severity_name: str
        """
        self._severity_name = severity_name

    @property
    def parent_workitem_id(self):
        r"""Gets the parent_workitem_id of this WorkItemVo.

        父工作项编号

        :return: The parent_workitem_id of this WorkItemVo.
        :rtype: str
        """
        return self._parent_workitem_id

    @parent_workitem_id.setter
    def parent_workitem_id(self, parent_workitem_id):
        r"""Sets the parent_workitem_id of this WorkItemVo.

        父工作项编号

        :param parent_workitem_id: The parent_workitem_id of this WorkItemVo.
        :type parent_workitem_id: str
        """
        self._parent_workitem_id = parent_workitem_id

    @property
    def board_id(self):
        r"""Gets the board_id of this WorkItemVo.

        看板ID

        :return: The board_id of this WorkItemVo.
        :rtype: str
        """
        return self._board_id

    @board_id.setter
    def board_id(self, board_id):
        r"""Sets the board_id of this WorkItemVo.

        看板ID

        :param board_id: The board_id of this WorkItemVo.
        :type board_id: str
        """
        self._board_id = board_id

    @property
    def board_name(self):
        r"""Gets the board_name of this WorkItemVo.

        看板

        :return: The board_name of this WorkItemVo.
        :rtype: str
        """
        return self._board_name

    @board_name.setter
    def board_name(self, board_name):
        r"""Sets the board_name of this WorkItemVo.

        看板

        :param board_name: The board_name of this WorkItemVo.
        :type board_name: str
        """
        self._board_name = board_name

    @property
    def create_time(self):
        r"""Gets the create_time of this WorkItemVo.

        创建时间

        :return: The create_time of this WorkItemVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WorkItemVo.

        创建时间

        :param create_time: The create_time of this WorkItemVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this WorkItemVo.

        更新时间

        :return: The update_time of this WorkItemVo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this WorkItemVo.

        更新时间

        :param update_time: The update_time of this WorkItemVo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def iteration_name(self):
        r"""Gets the iteration_name of this WorkItemVo.

        迭代名

        :return: The iteration_name of this WorkItemVo.
        :rtype: str
        """
        return self._iteration_name

    @iteration_name.setter
    def iteration_name(self, iteration_name):
        r"""Sets the iteration_name of this WorkItemVo.

        迭代名

        :param iteration_name: The iteration_name of this WorkItemVo.
        :type iteration_name: str
        """
        self._iteration_name = iteration_name

    @property
    def module_name(self):
        r"""Gets the module_name of this WorkItemVo.

        模块名

        :return: The module_name of this WorkItemVo.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this WorkItemVo.

        模块名

        :param module_name: The module_name of this WorkItemVo.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def module_path(self):
        r"""Gets the module_path of this WorkItemVo.

        模块path

        :return: The module_path of this WorkItemVo.
        :rtype: str
        """
        return self._module_path

    @module_path.setter
    def module_path(self, module_path):
        r"""Sets the module_path of this WorkItemVo.

        模块path

        :param module_path: The module_path of this WorkItemVo.
        :type module_path: str
        """
        self._module_path = module_path

    @property
    def module_path_name(self):
        r"""Gets the module_path_name of this WorkItemVo.

        模块路径名称

        :return: The module_path_name of this WorkItemVo.
        :rtype: str
        """
        return self._module_path_name

    @module_path_name.setter
    def module_path_name(self, module_path_name):
        r"""Sets the module_path_name of this WorkItemVo.

        模块路径名称

        :param module_path_name: The module_path_name of this WorkItemVo.
        :type module_path_name: str
        """
        self._module_path_name = module_path_name

    @property
    def owner_name(self):
        r"""Gets the owner_name of this WorkItemVo.

        处理人

        :return: The owner_name of this WorkItemVo.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this WorkItemVo.

        处理人

        :param owner_name: The owner_name of this WorkItemVo.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def have_child_dynamic(self):
        r"""Gets the have_child_dynamic of this WorkItemVo.

        父工作项下是否有子工作项包含动态

        :return: The have_child_dynamic of this WorkItemVo.
        :rtype: bool
        """
        return self._have_child_dynamic

    @have_child_dynamic.setter
    def have_child_dynamic(self, have_child_dynamic):
        r"""Sets the have_child_dynamic of this WorkItemVo.

        父工作项下是否有子工作项包含动态

        :param have_child_dynamic: The have_child_dynamic of this WorkItemVo.
        :type have_child_dynamic: bool
        """
        self._have_child_dynamic = have_child_dynamic

    @property
    def has_child(self):
        r"""Gets the has_child of this WorkItemVo.

        父工作项下是否有子工作项

        :return: The has_child of this WorkItemVo.
        :rtype: bool
        """
        return self._has_child

    @has_child.setter
    def has_child(self, has_child):
        r"""Sets the has_child of this WorkItemVo.

        父工作项下是否有子工作项

        :param has_child: The has_child of this WorkItemVo.
        :type has_child: bool
        """
        self._has_child = has_child

    @property
    def issue_dynamic_count(self):
        r"""Gets the issue_dynamic_count of this WorkItemVo.

        需求动态数量

        :return: The issue_dynamic_count of this WorkItemVo.
        :rtype: int
        """
        return self._issue_dynamic_count

    @issue_dynamic_count.setter
    def issue_dynamic_count(self, issue_dynamic_count):
        r"""Sets the issue_dynamic_count of this WorkItemVo.

        需求动态数量

        :param issue_dynamic_count: The issue_dynamic_count of this WorkItemVo.
        :type issue_dynamic_count: int
        """
        self._issue_dynamic_count = issue_dynamic_count

    @property
    def case_count(self):
        r"""Gets the case_count of this WorkItemVo.

        用例数量

        :return: The case_count of this WorkItemVo.
        :rtype: int
        """
        return self._case_count

    @case_count.setter
    def case_count(self, case_count):
        r"""Sets the case_count of this WorkItemVo.

        用例数量

        :param case_count: The case_count of this WorkItemVo.
        :type case_count: int
        """
        self._case_count = case_count

    @property
    def sequence_id(self):
        r"""Gets the sequence_id of this WorkItemVo.

        xBoard项目工作项序列号

        :return: The sequence_id of this WorkItemVo.
        :rtype: str
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        r"""Sets the sequence_id of this WorkItemVo.

        xBoard项目工作项序列号

        :param sequence_id: The sequence_id of this WorkItemVo.
        :type sequence_id: str
        """
        self._sequence_id = sequence_id

    @property
    def pi_id(self):
        r"""Gets the pi_id of this WorkItemVo.

        pi的id，层级关系：pi -> 迭代 -> 需求

        :return: The pi_id of this WorkItemVo.
        :rtype: str
        """
        return self._pi_id

    @pi_id.setter
    def pi_id(self, pi_id):
        r"""Sets the pi_id of this WorkItemVo.

        pi的id，层级关系：pi -> 迭代 -> 需求

        :param pi_id: The pi_id of this WorkItemVo.
        :type pi_id: str
        """
        self._pi_id = pi_id

    @property
    def pi_name(self):
        r"""Gets the pi_name of this WorkItemVo.

        迭代ID

        :return: The pi_name of this WorkItemVo.
        :rtype: str
        """
        return self._pi_name

    @pi_name.setter
    def pi_name(self, pi_name):
        r"""Sets the pi_name of this WorkItemVo.

        迭代ID

        :param pi_name: The pi_name of this WorkItemVo.
        :type pi_name: str
        """
        self._pi_name = pi_name

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
        if not isinstance(other, WorkItemVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
