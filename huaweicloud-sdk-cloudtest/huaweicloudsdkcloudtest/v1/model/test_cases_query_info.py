# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCasesQueryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keyword': 'str',
        'exeplatforms': 'list[str]',
        'own': 'bool',
        'use_offset': 'bool',
        'version_uri': 'str',
        'case_uris': 'list[str]',
        'owner_ids': 'list[str]',
        'status_codes': 'list[str]',
        'rank_ids': 'list[str]',
        'module_ids': 'list[str]',
        'issue_id': 'str',
        'creator_ids': 'list[str]',
        'result_codes': 'list[str]',
        'iteration_ids': 'list[str]',
        'create_start_time': 'str',
        'create_end_time': 'str',
        'associated_issue': 'bool',
        'associated_defects': 'bool',
        'include_sub_issue': 'bool',
        'include_sub_feature': 'bool',
        'label_ids': 'list[str]',
        'execute_start_time': 'str',
        'execute_end_time': 'str',
        'executor_ids': 'list[str]',
        'test_types': 'list[str]',
        'is_keyword': 'bool',
        'issue_tree_search': 'bool',
        'service_type': 'int',
        'service_types': 'list[int]',
        'stage_type': 'int',
        'feature_uri': 'str',
        'sort_field': 'str',
        'sort_type': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'case_type': 'int',
        'custom_field_info': 'list[QueryCustomFieldsInfo]',
        'task_uri': 'str',
        'associate_issue_detail': 'bool',
        'not_assign_task': 'bool',
        'test_designs': 'list[bool]',
        'review_status': 'int'
    }

    attribute_map = {
        'keyword': 'keyword',
        'exeplatforms': 'exeplatforms',
        'own': 'own',
        'use_offset': 'useOffset',
        'version_uri': 'version_uri',
        'case_uris': 'case_uris',
        'owner_ids': 'owner_ids',
        'status_codes': 'status_codes',
        'rank_ids': 'rank_ids',
        'module_ids': 'module_ids',
        'issue_id': 'issue_id',
        'creator_ids': 'creator_ids',
        'result_codes': 'result_codes',
        'iteration_ids': 'iteration_ids',
        'create_start_time': 'create_start_time',
        'create_end_time': 'create_end_time',
        'associated_issue': 'associated_issue',
        'associated_defects': 'associated_defects',
        'include_sub_issue': 'include_sub_issue',
        'include_sub_feature': 'include_sub_feature',
        'label_ids': 'label_ids',
        'execute_start_time': 'execute_start_time',
        'execute_end_time': 'execute_end_time',
        'executor_ids': 'executor_ids',
        'test_types': 'test_types',
        'is_keyword': 'is_keyword',
        'issue_tree_search': 'issue_tree_search',
        'service_type': 'service_type',
        'service_types': 'service_types',
        'stage_type': 'stage_type',
        'feature_uri': 'feature_uri',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'case_type': 'case_type',
        'custom_field_info': 'custom_field_info',
        'task_uri': 'task_uri',
        'associate_issue_detail': 'associate_issue_detail',
        'not_assign_task': 'not_assign_task',
        'test_designs': 'test_designs',
        'review_status': 'review_status'
    }

    def __init__(self, keyword=None, exeplatforms=None, own=None, use_offset=None, version_uri=None, case_uris=None, owner_ids=None, status_codes=None, rank_ids=None, module_ids=None, issue_id=None, creator_ids=None, result_codes=None, iteration_ids=None, create_start_time=None, create_end_time=None, associated_issue=None, associated_defects=None, include_sub_issue=None, include_sub_feature=None, label_ids=None, execute_start_time=None, execute_end_time=None, executor_ids=None, test_types=None, is_keyword=None, issue_tree_search=None, service_type=None, service_types=None, stage_type=None, feature_uri=None, sort_field=None, sort_type=None, page_no=None, page_size=None, case_type=None, custom_field_info=None, task_uri=None, associate_issue_detail=None, not_assign_task=None, test_designs=None, review_status=None):
        r"""TestCasesQueryInfo

        The model defined in huaweicloud sdk

        :param keyword: 关键字查询，用例名或编号
        :type keyword: str
        :param exeplatforms: 执行平台
        :type exeplatforms: list[str]
        :param own: 是否是我的
        :type own: bool
        :param use_offset: 
        :type use_offset: bool
        :param version_uri: 版本URI
        :type version_uri: str
        :param case_uris: 用例URI集合
        :type case_uris: list[str]
        :param owner_ids: 处理者ID集合
        :type owner_ids: list[str]
        :param status_codes: 状态Code集合
        :type status_codes: list[str]
        :param rank_ids: 用例等级ID集合
        :type rank_ids: list[str]
        :param module_ids: 模块ID集合
        :type module_ids: list[str]
        :param issue_id: 需求编号
        :type issue_id: str
        :param creator_ids: 创建者ID集合
        :type creator_ids: list[str]
        :param result_codes: 结果Code集合
        :type result_codes: list[str]
        :param iteration_ids: 归属迭代ID集合
        :type iteration_ids: list[str]
        :param create_start_time: 创建开始时间
        :type create_start_time: str
        :param create_end_time: 创建结束时间
        :type create_end_time: str
        :param associated_issue: 是否关联需求（null：不限，false：未关联，true：已关联）
        :type associated_issue: bool
        :param associated_defects: 是否关联缺陷（null：不限，false：未关联，true：已关联）
        :type associated_defects: bool
        :param include_sub_issue: 是否查询子需求关联的用例，默认true
        :type include_sub_issue: bool
        :param include_sub_feature: 是否查询子目录的用例，默认true
        :type include_sub_feature: bool
        :param label_ids: 标签ID集合
        :type label_ids: list[str]
        :param execute_start_time: 执行开始时间
        :type execute_start_time: str
        :param execute_end_time: 执行结束时间
        :type execute_end_time: str
        :param executor_ids: 执行者ID集合
        :type executor_ids: list[str]
        :param test_types: 类型
        :type test_types: list[str]
        :param is_keyword: 是否组合关键字
        :type is_keyword: bool
        :param issue_tree_search: 是否是需求树点击的查询关联用例
        :type issue_tree_search: bool
        :param service_type: 服务类型
        :type service_type: int
        :param service_types: 服务类型集合
        :type service_types: list[int]
        :param stage_type: 阶段过程（2：测试设计，3：测试执行，4：质量报告）
        :type stage_type: int
        :param feature_uri: 目录URI
        :type feature_uri: str
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_type: 排序方式
        :type sort_type: str
        :param page_no: 当前页数
        :type page_no: int
        :param page_size: 每页条数
        :type page_size: int
        :param case_type: 用例类型
        :type case_type: int
        :param custom_field_info: 用例自定义字段信息
        :type custom_field_info: list[:class:`huaweicloudsdkcloudtest.v1.QueryCustomFieldsInfo`]
        :param task_uri: 测试套uri
        :type task_uri: str
        :param associate_issue_detail: 是否返回需求具体信息（返回需求名称，需求id）
        :type associate_issue_detail: bool
        :param not_assign_task: 该字段为false,则查询全量用例，为true表示查询未分配测试套的用例
        :type not_assign_task: bool
        :param test_designs: 是否来自测试设计（null或者[true, false]：不限，[true]：来自测试设计，[false]：否来自测试设计）
        :type test_designs: list[bool]
        :param review_status: 用例评审状态
        :type review_status: int
        """
        
        

        self._keyword = None
        self._exeplatforms = None
        self._own = None
        self._use_offset = None
        self._version_uri = None
        self._case_uris = None
        self._owner_ids = None
        self._status_codes = None
        self._rank_ids = None
        self._module_ids = None
        self._issue_id = None
        self._creator_ids = None
        self._result_codes = None
        self._iteration_ids = None
        self._create_start_time = None
        self._create_end_time = None
        self._associated_issue = None
        self._associated_defects = None
        self._include_sub_issue = None
        self._include_sub_feature = None
        self._label_ids = None
        self._execute_start_time = None
        self._execute_end_time = None
        self._executor_ids = None
        self._test_types = None
        self._is_keyword = None
        self._issue_tree_search = None
        self._service_type = None
        self._service_types = None
        self._stage_type = None
        self._feature_uri = None
        self._sort_field = None
        self._sort_type = None
        self._page_no = None
        self._page_size = None
        self._case_type = None
        self._custom_field_info = None
        self._task_uri = None
        self._associate_issue_detail = None
        self._not_assign_task = None
        self._test_designs = None
        self._review_status = None
        self.discriminator = None

        if keyword is not None:
            self.keyword = keyword
        if exeplatforms is not None:
            self.exeplatforms = exeplatforms
        if own is not None:
            self.own = own
        if use_offset is not None:
            self.use_offset = use_offset
        if version_uri is not None:
            self.version_uri = version_uri
        if case_uris is not None:
            self.case_uris = case_uris
        if owner_ids is not None:
            self.owner_ids = owner_ids
        if status_codes is not None:
            self.status_codes = status_codes
        if rank_ids is not None:
            self.rank_ids = rank_ids
        if module_ids is not None:
            self.module_ids = module_ids
        if issue_id is not None:
            self.issue_id = issue_id
        if creator_ids is not None:
            self.creator_ids = creator_ids
        if result_codes is not None:
            self.result_codes = result_codes
        if iteration_ids is not None:
            self.iteration_ids = iteration_ids
        if create_start_time is not None:
            self.create_start_time = create_start_time
        if create_end_time is not None:
            self.create_end_time = create_end_time
        if associated_issue is not None:
            self.associated_issue = associated_issue
        if associated_defects is not None:
            self.associated_defects = associated_defects
        if include_sub_issue is not None:
            self.include_sub_issue = include_sub_issue
        if include_sub_feature is not None:
            self.include_sub_feature = include_sub_feature
        if label_ids is not None:
            self.label_ids = label_ids
        if execute_start_time is not None:
            self.execute_start_time = execute_start_time
        if execute_end_time is not None:
            self.execute_end_time = execute_end_time
        if executor_ids is not None:
            self.executor_ids = executor_ids
        if test_types is not None:
            self.test_types = test_types
        if is_keyword is not None:
            self.is_keyword = is_keyword
        if issue_tree_search is not None:
            self.issue_tree_search = issue_tree_search
        if service_type is not None:
            self.service_type = service_type
        if service_types is not None:
            self.service_types = service_types
        if stage_type is not None:
            self.stage_type = stage_type
        if feature_uri is not None:
            self.feature_uri = feature_uri
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if case_type is not None:
            self.case_type = case_type
        if custom_field_info is not None:
            self.custom_field_info = custom_field_info
        if task_uri is not None:
            self.task_uri = task_uri
        if associate_issue_detail is not None:
            self.associate_issue_detail = associate_issue_detail
        if not_assign_task is not None:
            self.not_assign_task = not_assign_task
        if test_designs is not None:
            self.test_designs = test_designs
        if review_status is not None:
            self.review_status = review_status

    @property
    def keyword(self):
        r"""Gets the keyword of this TestCasesQueryInfo.

        关键字查询，用例名或编号

        :return: The keyword of this TestCasesQueryInfo.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this TestCasesQueryInfo.

        关键字查询，用例名或编号

        :param keyword: The keyword of this TestCasesQueryInfo.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def exeplatforms(self):
        r"""Gets the exeplatforms of this TestCasesQueryInfo.

        执行平台

        :return: The exeplatforms of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._exeplatforms

    @exeplatforms.setter
    def exeplatforms(self, exeplatforms):
        r"""Sets the exeplatforms of this TestCasesQueryInfo.

        执行平台

        :param exeplatforms: The exeplatforms of this TestCasesQueryInfo.
        :type exeplatforms: list[str]
        """
        self._exeplatforms = exeplatforms

    @property
    def own(self):
        r"""Gets the own of this TestCasesQueryInfo.

        是否是我的

        :return: The own of this TestCasesQueryInfo.
        :rtype: bool
        """
        return self._own

    @own.setter
    def own(self, own):
        r"""Sets the own of this TestCasesQueryInfo.

        是否是我的

        :param own: The own of this TestCasesQueryInfo.
        :type own: bool
        """
        self._own = own

    @property
    def use_offset(self):
        r"""Gets the use_offset of this TestCasesQueryInfo.

        :return: The use_offset of this TestCasesQueryInfo.
        :rtype: bool
        """
        return self._use_offset

    @use_offset.setter
    def use_offset(self, use_offset):
        r"""Sets the use_offset of this TestCasesQueryInfo.

        :param use_offset: The use_offset of this TestCasesQueryInfo.
        :type use_offset: bool
        """
        self._use_offset = use_offset

    @property
    def version_uri(self):
        r"""Gets the version_uri of this TestCasesQueryInfo.

        版本URI

        :return: The version_uri of this TestCasesQueryInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this TestCasesQueryInfo.

        版本URI

        :param version_uri: The version_uri of this TestCasesQueryInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def case_uris(self):
        r"""Gets the case_uris of this TestCasesQueryInfo.

        用例URI集合

        :return: The case_uris of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._case_uris

    @case_uris.setter
    def case_uris(self, case_uris):
        r"""Sets the case_uris of this TestCasesQueryInfo.

        用例URI集合

        :param case_uris: The case_uris of this TestCasesQueryInfo.
        :type case_uris: list[str]
        """
        self._case_uris = case_uris

    @property
    def owner_ids(self):
        r"""Gets the owner_ids of this TestCasesQueryInfo.

        处理者ID集合

        :return: The owner_ids of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        r"""Sets the owner_ids of this TestCasesQueryInfo.

        处理者ID集合

        :param owner_ids: The owner_ids of this TestCasesQueryInfo.
        :type owner_ids: list[str]
        """
        self._owner_ids = owner_ids

    @property
    def status_codes(self):
        r"""Gets the status_codes of this TestCasesQueryInfo.

        状态Code集合

        :return: The status_codes of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._status_codes

    @status_codes.setter
    def status_codes(self, status_codes):
        r"""Sets the status_codes of this TestCasesQueryInfo.

        状态Code集合

        :param status_codes: The status_codes of this TestCasesQueryInfo.
        :type status_codes: list[str]
        """
        self._status_codes = status_codes

    @property
    def rank_ids(self):
        r"""Gets the rank_ids of this TestCasesQueryInfo.

        用例等级ID集合

        :return: The rank_ids of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._rank_ids

    @rank_ids.setter
    def rank_ids(self, rank_ids):
        r"""Sets the rank_ids of this TestCasesQueryInfo.

        用例等级ID集合

        :param rank_ids: The rank_ids of this TestCasesQueryInfo.
        :type rank_ids: list[str]
        """
        self._rank_ids = rank_ids

    @property
    def module_ids(self):
        r"""Gets the module_ids of this TestCasesQueryInfo.

        模块ID集合

        :return: The module_ids of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._module_ids

    @module_ids.setter
    def module_ids(self, module_ids):
        r"""Sets the module_ids of this TestCasesQueryInfo.

        模块ID集合

        :param module_ids: The module_ids of this TestCasesQueryInfo.
        :type module_ids: list[str]
        """
        self._module_ids = module_ids

    @property
    def issue_id(self):
        r"""Gets the issue_id of this TestCasesQueryInfo.

        需求编号

        :return: The issue_id of this TestCasesQueryInfo.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this TestCasesQueryInfo.

        需求编号

        :param issue_id: The issue_id of this TestCasesQueryInfo.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def creator_ids(self):
        r"""Gets the creator_ids of this TestCasesQueryInfo.

        创建者ID集合

        :return: The creator_ids of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._creator_ids

    @creator_ids.setter
    def creator_ids(self, creator_ids):
        r"""Sets the creator_ids of this TestCasesQueryInfo.

        创建者ID集合

        :param creator_ids: The creator_ids of this TestCasesQueryInfo.
        :type creator_ids: list[str]
        """
        self._creator_ids = creator_ids

    @property
    def result_codes(self):
        r"""Gets the result_codes of this TestCasesQueryInfo.

        结果Code集合

        :return: The result_codes of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._result_codes

    @result_codes.setter
    def result_codes(self, result_codes):
        r"""Sets the result_codes of this TestCasesQueryInfo.

        结果Code集合

        :param result_codes: The result_codes of this TestCasesQueryInfo.
        :type result_codes: list[str]
        """
        self._result_codes = result_codes

    @property
    def iteration_ids(self):
        r"""Gets the iteration_ids of this TestCasesQueryInfo.

        归属迭代ID集合

        :return: The iteration_ids of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._iteration_ids

    @iteration_ids.setter
    def iteration_ids(self, iteration_ids):
        r"""Sets the iteration_ids of this TestCasesQueryInfo.

        归属迭代ID集合

        :param iteration_ids: The iteration_ids of this TestCasesQueryInfo.
        :type iteration_ids: list[str]
        """
        self._iteration_ids = iteration_ids

    @property
    def create_start_time(self):
        r"""Gets the create_start_time of this TestCasesQueryInfo.

        创建开始时间

        :return: The create_start_time of this TestCasesQueryInfo.
        :rtype: str
        """
        return self._create_start_time

    @create_start_time.setter
    def create_start_time(self, create_start_time):
        r"""Sets the create_start_time of this TestCasesQueryInfo.

        创建开始时间

        :param create_start_time: The create_start_time of this TestCasesQueryInfo.
        :type create_start_time: str
        """
        self._create_start_time = create_start_time

    @property
    def create_end_time(self):
        r"""Gets the create_end_time of this TestCasesQueryInfo.

        创建结束时间

        :return: The create_end_time of this TestCasesQueryInfo.
        :rtype: str
        """
        return self._create_end_time

    @create_end_time.setter
    def create_end_time(self, create_end_time):
        r"""Sets the create_end_time of this TestCasesQueryInfo.

        创建结束时间

        :param create_end_time: The create_end_time of this TestCasesQueryInfo.
        :type create_end_time: str
        """
        self._create_end_time = create_end_time

    @property
    def associated_issue(self):
        r"""Gets the associated_issue of this TestCasesQueryInfo.

        是否关联需求（null：不限，false：未关联，true：已关联）

        :return: The associated_issue of this TestCasesQueryInfo.
        :rtype: bool
        """
        return self._associated_issue

    @associated_issue.setter
    def associated_issue(self, associated_issue):
        r"""Sets the associated_issue of this TestCasesQueryInfo.

        是否关联需求（null：不限，false：未关联，true：已关联）

        :param associated_issue: The associated_issue of this TestCasesQueryInfo.
        :type associated_issue: bool
        """
        self._associated_issue = associated_issue

    @property
    def associated_defects(self):
        r"""Gets the associated_defects of this TestCasesQueryInfo.

        是否关联缺陷（null：不限，false：未关联，true：已关联）

        :return: The associated_defects of this TestCasesQueryInfo.
        :rtype: bool
        """
        return self._associated_defects

    @associated_defects.setter
    def associated_defects(self, associated_defects):
        r"""Sets the associated_defects of this TestCasesQueryInfo.

        是否关联缺陷（null：不限，false：未关联，true：已关联）

        :param associated_defects: The associated_defects of this TestCasesQueryInfo.
        :type associated_defects: bool
        """
        self._associated_defects = associated_defects

    @property
    def include_sub_issue(self):
        r"""Gets the include_sub_issue of this TestCasesQueryInfo.

        是否查询子需求关联的用例，默认true

        :return: The include_sub_issue of this TestCasesQueryInfo.
        :rtype: bool
        """
        return self._include_sub_issue

    @include_sub_issue.setter
    def include_sub_issue(self, include_sub_issue):
        r"""Sets the include_sub_issue of this TestCasesQueryInfo.

        是否查询子需求关联的用例，默认true

        :param include_sub_issue: The include_sub_issue of this TestCasesQueryInfo.
        :type include_sub_issue: bool
        """
        self._include_sub_issue = include_sub_issue

    @property
    def include_sub_feature(self):
        r"""Gets the include_sub_feature of this TestCasesQueryInfo.

        是否查询子目录的用例，默认true

        :return: The include_sub_feature of this TestCasesQueryInfo.
        :rtype: bool
        """
        return self._include_sub_feature

    @include_sub_feature.setter
    def include_sub_feature(self, include_sub_feature):
        r"""Sets the include_sub_feature of this TestCasesQueryInfo.

        是否查询子目录的用例，默认true

        :param include_sub_feature: The include_sub_feature of this TestCasesQueryInfo.
        :type include_sub_feature: bool
        """
        self._include_sub_feature = include_sub_feature

    @property
    def label_ids(self):
        r"""Gets the label_ids of this TestCasesQueryInfo.

        标签ID集合

        :return: The label_ids of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._label_ids

    @label_ids.setter
    def label_ids(self, label_ids):
        r"""Sets the label_ids of this TestCasesQueryInfo.

        标签ID集合

        :param label_ids: The label_ids of this TestCasesQueryInfo.
        :type label_ids: list[str]
        """
        self._label_ids = label_ids

    @property
    def execute_start_time(self):
        r"""Gets the execute_start_time of this TestCasesQueryInfo.

        执行开始时间

        :return: The execute_start_time of this TestCasesQueryInfo.
        :rtype: str
        """
        return self._execute_start_time

    @execute_start_time.setter
    def execute_start_time(self, execute_start_time):
        r"""Sets the execute_start_time of this TestCasesQueryInfo.

        执行开始时间

        :param execute_start_time: The execute_start_time of this TestCasesQueryInfo.
        :type execute_start_time: str
        """
        self._execute_start_time = execute_start_time

    @property
    def execute_end_time(self):
        r"""Gets the execute_end_time of this TestCasesQueryInfo.

        执行结束时间

        :return: The execute_end_time of this TestCasesQueryInfo.
        :rtype: str
        """
        return self._execute_end_time

    @execute_end_time.setter
    def execute_end_time(self, execute_end_time):
        r"""Sets the execute_end_time of this TestCasesQueryInfo.

        执行结束时间

        :param execute_end_time: The execute_end_time of this TestCasesQueryInfo.
        :type execute_end_time: str
        """
        self._execute_end_time = execute_end_time

    @property
    def executor_ids(self):
        r"""Gets the executor_ids of this TestCasesQueryInfo.

        执行者ID集合

        :return: The executor_ids of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._executor_ids

    @executor_ids.setter
    def executor_ids(self, executor_ids):
        r"""Sets the executor_ids of this TestCasesQueryInfo.

        执行者ID集合

        :param executor_ids: The executor_ids of this TestCasesQueryInfo.
        :type executor_ids: list[str]
        """
        self._executor_ids = executor_ids

    @property
    def test_types(self):
        r"""Gets the test_types of this TestCasesQueryInfo.

        类型

        :return: The test_types of this TestCasesQueryInfo.
        :rtype: list[str]
        """
        return self._test_types

    @test_types.setter
    def test_types(self, test_types):
        r"""Sets the test_types of this TestCasesQueryInfo.

        类型

        :param test_types: The test_types of this TestCasesQueryInfo.
        :type test_types: list[str]
        """
        self._test_types = test_types

    @property
    def is_keyword(self):
        r"""Gets the is_keyword of this TestCasesQueryInfo.

        是否组合关键字

        :return: The is_keyword of this TestCasesQueryInfo.
        :rtype: bool
        """
        return self._is_keyword

    @is_keyword.setter
    def is_keyword(self, is_keyword):
        r"""Sets the is_keyword of this TestCasesQueryInfo.

        是否组合关键字

        :param is_keyword: The is_keyword of this TestCasesQueryInfo.
        :type is_keyword: bool
        """
        self._is_keyword = is_keyword

    @property
    def issue_tree_search(self):
        r"""Gets the issue_tree_search of this TestCasesQueryInfo.

        是否是需求树点击的查询关联用例

        :return: The issue_tree_search of this TestCasesQueryInfo.
        :rtype: bool
        """
        return self._issue_tree_search

    @issue_tree_search.setter
    def issue_tree_search(self, issue_tree_search):
        r"""Sets the issue_tree_search of this TestCasesQueryInfo.

        是否是需求树点击的查询关联用例

        :param issue_tree_search: The issue_tree_search of this TestCasesQueryInfo.
        :type issue_tree_search: bool
        """
        self._issue_tree_search = issue_tree_search

    @property
    def service_type(self):
        r"""Gets the service_type of this TestCasesQueryInfo.

        服务类型

        :return: The service_type of this TestCasesQueryInfo.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this TestCasesQueryInfo.

        服务类型

        :param service_type: The service_type of this TestCasesQueryInfo.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def service_types(self):
        r"""Gets the service_types of this TestCasesQueryInfo.

        服务类型集合

        :return: The service_types of this TestCasesQueryInfo.
        :rtype: list[int]
        """
        return self._service_types

    @service_types.setter
    def service_types(self, service_types):
        r"""Sets the service_types of this TestCasesQueryInfo.

        服务类型集合

        :param service_types: The service_types of this TestCasesQueryInfo.
        :type service_types: list[int]
        """
        self._service_types = service_types

    @property
    def stage_type(self):
        r"""Gets the stage_type of this TestCasesQueryInfo.

        阶段过程（2：测试设计，3：测试执行，4：质量报告）

        :return: The stage_type of this TestCasesQueryInfo.
        :rtype: int
        """
        return self._stage_type

    @stage_type.setter
    def stage_type(self, stage_type):
        r"""Sets the stage_type of this TestCasesQueryInfo.

        阶段过程（2：测试设计，3：测试执行，4：质量报告）

        :param stage_type: The stage_type of this TestCasesQueryInfo.
        :type stage_type: int
        """
        self._stage_type = stage_type

    @property
    def feature_uri(self):
        r"""Gets the feature_uri of this TestCasesQueryInfo.

        目录URI

        :return: The feature_uri of this TestCasesQueryInfo.
        :rtype: str
        """
        return self._feature_uri

    @feature_uri.setter
    def feature_uri(self, feature_uri):
        r"""Sets the feature_uri of this TestCasesQueryInfo.

        目录URI

        :param feature_uri: The feature_uri of this TestCasesQueryInfo.
        :type feature_uri: str
        """
        self._feature_uri = feature_uri

    @property
    def sort_field(self):
        r"""Gets the sort_field of this TestCasesQueryInfo.

        排序字段

        :return: The sort_field of this TestCasesQueryInfo.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this TestCasesQueryInfo.

        排序字段

        :param sort_field: The sort_field of this TestCasesQueryInfo.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this TestCasesQueryInfo.

        排序方式

        :return: The sort_type of this TestCasesQueryInfo.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this TestCasesQueryInfo.

        排序方式

        :param sort_type: The sort_type of this TestCasesQueryInfo.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def page_no(self):
        r"""Gets the page_no of this TestCasesQueryInfo.

        当前页数

        :return: The page_no of this TestCasesQueryInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this TestCasesQueryInfo.

        当前页数

        :param page_no: The page_no of this TestCasesQueryInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this TestCasesQueryInfo.

        每页条数

        :return: The page_size of this TestCasesQueryInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this TestCasesQueryInfo.

        每页条数

        :param page_size: The page_size of this TestCasesQueryInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def case_type(self):
        r"""Gets the case_type of this TestCasesQueryInfo.

        用例类型

        :return: The case_type of this TestCasesQueryInfo.
        :rtype: int
        """
        return self._case_type

    @case_type.setter
    def case_type(self, case_type):
        r"""Sets the case_type of this TestCasesQueryInfo.

        用例类型

        :param case_type: The case_type of this TestCasesQueryInfo.
        :type case_type: int
        """
        self._case_type = case_type

    @property
    def custom_field_info(self):
        r"""Gets the custom_field_info of this TestCasesQueryInfo.

        用例自定义字段信息

        :return: The custom_field_info of this TestCasesQueryInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.QueryCustomFieldsInfo`]
        """
        return self._custom_field_info

    @custom_field_info.setter
    def custom_field_info(self, custom_field_info):
        r"""Sets the custom_field_info of this TestCasesQueryInfo.

        用例自定义字段信息

        :param custom_field_info: The custom_field_info of this TestCasesQueryInfo.
        :type custom_field_info: list[:class:`huaweicloudsdkcloudtest.v1.QueryCustomFieldsInfo`]
        """
        self._custom_field_info = custom_field_info

    @property
    def task_uri(self):
        r"""Gets the task_uri of this TestCasesQueryInfo.

        测试套uri

        :return: The task_uri of this TestCasesQueryInfo.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this TestCasesQueryInfo.

        测试套uri

        :param task_uri: The task_uri of this TestCasesQueryInfo.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def associate_issue_detail(self):
        r"""Gets the associate_issue_detail of this TestCasesQueryInfo.

        是否返回需求具体信息（返回需求名称，需求id）

        :return: The associate_issue_detail of this TestCasesQueryInfo.
        :rtype: bool
        """
        return self._associate_issue_detail

    @associate_issue_detail.setter
    def associate_issue_detail(self, associate_issue_detail):
        r"""Sets the associate_issue_detail of this TestCasesQueryInfo.

        是否返回需求具体信息（返回需求名称，需求id）

        :param associate_issue_detail: The associate_issue_detail of this TestCasesQueryInfo.
        :type associate_issue_detail: bool
        """
        self._associate_issue_detail = associate_issue_detail

    @property
    def not_assign_task(self):
        r"""Gets the not_assign_task of this TestCasesQueryInfo.

        该字段为false,则查询全量用例，为true表示查询未分配测试套的用例

        :return: The not_assign_task of this TestCasesQueryInfo.
        :rtype: bool
        """
        return self._not_assign_task

    @not_assign_task.setter
    def not_assign_task(self, not_assign_task):
        r"""Sets the not_assign_task of this TestCasesQueryInfo.

        该字段为false,则查询全量用例，为true表示查询未分配测试套的用例

        :param not_assign_task: The not_assign_task of this TestCasesQueryInfo.
        :type not_assign_task: bool
        """
        self._not_assign_task = not_assign_task

    @property
    def test_designs(self):
        r"""Gets the test_designs of this TestCasesQueryInfo.

        是否来自测试设计（null或者[true, false]：不限，[true]：来自测试设计，[false]：否来自测试设计）

        :return: The test_designs of this TestCasesQueryInfo.
        :rtype: list[bool]
        """
        return self._test_designs

    @test_designs.setter
    def test_designs(self, test_designs):
        r"""Sets the test_designs of this TestCasesQueryInfo.

        是否来自测试设计（null或者[true, false]：不限，[true]：来自测试设计，[false]：否来自测试设计）

        :param test_designs: The test_designs of this TestCasesQueryInfo.
        :type test_designs: list[bool]
        """
        self._test_designs = test_designs

    @property
    def review_status(self):
        r"""Gets the review_status of this TestCasesQueryInfo.

        用例评审状态

        :return: The review_status of this TestCasesQueryInfo.
        :rtype: int
        """
        return self._review_status

    @review_status.setter
    def review_status(self, review_status):
        r"""Sets the review_status of this TestCasesQueryInfo.

        用例评审状态

        :param review_status: The review_status of this TestCasesQueryInfo.
        :type review_status: int
        """
        self._review_status = review_status

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
        if not isinstance(other, TestCasesQueryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
