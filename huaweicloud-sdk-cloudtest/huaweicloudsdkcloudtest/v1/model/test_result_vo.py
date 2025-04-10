# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestResultVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'name': 'str',
        'author': 'str',
        'rank': 'int',
        'result': 'int',
        'round': 'int',
        'preparation': 'str',
        'description': 'str',
        'region': 'str',
        'steps': 'list[ResultStepVo]',
        'number': 'str',
        'author_name': 'str',
        'begin_time': 'datetime',
        'begin_time_timestamp': 'int',
        'end_time': 'datetime',
        'end_time_timestamp': 'int',
        'creation_date': 'str',
        'creation_date_timestamp': 'int',
        'last_modified': 'datetime',
        'last_modified_timestamp': 'int',
        'last_change_time': 'datetime',
        'last_change_time_timestamp': 'int',
        'dfx_test_result': 'str',
        'failure_cause': 'str',
        'parent_uri': 'str',
        'test_case_uri': 'str',
        'test_case_name': 'str',
        'task_uri': 'str',
        'result_name': 'str',
        'test_result_ae': 'str',
        'executor_id': 'str',
        'executor_name': 'str',
        'task_id': 'str',
        'execute_id': 'str',
        'time_cost': 'int',
        'step_txt': 'str',
        'step_expect': 'str',
        'step_actual': 'str',
        'step_result': 'str',
        'release_dev': 'str',
        'creation_version_uri': 'str',
        'version_uri': 'str',
        'project_id': 'str',
        'report_url': 'str',
        'test_case_number': 'str',
        'service_type': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'author': 'author',
        'rank': 'rank',
        'result': 'result',
        'round': 'round',
        'preparation': 'preparation',
        'description': 'description',
        'region': 'region',
        'steps': 'steps',
        'number': 'number',
        'author_name': 'author_name',
        'begin_time': 'begin_time',
        'begin_time_timestamp': 'begin_time_timestamp',
        'end_time': 'end_time',
        'end_time_timestamp': 'end_time_timestamp',
        'creation_date': 'creation_date',
        'creation_date_timestamp': 'creation_date_timestamp',
        'last_modified': 'last_modified',
        'last_modified_timestamp': 'last_modified_timestamp',
        'last_change_time': 'last_change_time',
        'last_change_time_timestamp': 'last_change_time_timestamp',
        'dfx_test_result': 'dfx_test_result',
        'failure_cause': 'failure_cause',
        'parent_uri': 'parent_uri',
        'test_case_uri': 'test_case_uri',
        'test_case_name': 'test_case_name',
        'task_uri': 'task_uri',
        'result_name': 'result_name',
        'test_result_ae': 'test_result_ae',
        'executor_id': 'executor_id',
        'executor_name': 'executor_name',
        'task_id': 'task_id',
        'execute_id': 'execute_id',
        'time_cost': 'time_cost',
        'step_txt': 'step_txt',
        'step_expect': 'step_expect',
        'step_actual': 'step_actual',
        'step_result': 'step_result',
        'release_dev': 'release_dev',
        'creation_version_uri': 'creation_version_uri',
        'version_uri': 'version_uri',
        'project_id': 'project_id',
        'report_url': 'report_url',
        'test_case_number': 'test_case_number',
        'service_type': 'service_type'
    }

    def __init__(self, uri=None, name=None, author=None, rank=None, result=None, round=None, preparation=None, description=None, region=None, steps=None, number=None, author_name=None, begin_time=None, begin_time_timestamp=None, end_time=None, end_time_timestamp=None, creation_date=None, creation_date_timestamp=None, last_modified=None, last_modified_timestamp=None, last_change_time=None, last_change_time_timestamp=None, dfx_test_result=None, failure_cause=None, parent_uri=None, test_case_uri=None, test_case_name=None, task_uri=None, result_name=None, test_result_ae=None, executor_id=None, executor_name=None, task_id=None, execute_id=None, time_cost=None, step_txt=None, step_expect=None, step_actual=None, step_result=None, release_dev=None, creation_version_uri=None, version_uri=None, project_id=None, report_url=None, test_case_number=None, service_type=None):
        r"""TestResultVo

        The model defined in huaweicloud sdk

        :param uri: 结果URI
        :type uri: str
        :param name: 用例结果名称
        :type name: str
        :param author: 创建人ID
        :type author: str
        :param rank: 级别
        :type rank: int
        :param result: 测试结果Code
        :type result: int
        :param round: 执行批次
        :type round: int
        :param preparation: 前置条件
        :type preparation: str
        :param description: 描述
        :type description: str
        :param region: 逻辑Region
        :type region: str
        :param steps: 测试步骤信息
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.ResultStepVo`]
        :param number: 用例结果编号
        :type number: str
        :param author_name: 创建人名称
        :type author_name: str
        :param begin_time: 执行开始时间
        :type begin_time: datetime
        :param begin_time_timestamp: 执行开始时间时间戳
        :type begin_time_timestamp: int
        :param end_time: 执行结束时间
        :type end_time: datetime
        :param end_time_timestamp: 执行结束时间时间戳
        :type end_time_timestamp: int
        :param creation_date: 创建时间
        :type creation_date: str
        :param creation_date_timestamp: 创建时间时间戳
        :type creation_date_timestamp: int
        :param last_modified: 最后修改时间
        :type last_modified: datetime
        :param last_modified_timestamp: 最后修改时间
        :type last_modified_timestamp: int
        :param last_change_time: 最后变更时间
        :type last_change_time: datetime
        :param last_change_time_timestamp: 最后变更时间
        :type last_change_time_timestamp: int
        :param dfx_test_result: DFX测试结果
        :type dfx_test_result: str
        :param failure_cause: 失败原因
        :type failure_cause: str
        :param parent_uri: 父节点URI(分支用例URI或迭代用例URI)
        :type parent_uri: str
        :param test_case_uri: 分支用例URI
        :type test_case_uri: str
        :param test_case_name: 用例名称
        :type test_case_name: str
        :param task_uri: 测试任务URI
        :type task_uri: str
        :param result_name: 测试结果
        :type result_name: str
        :param test_result_ae: 是否自动化执行
        :type test_result_ae: str
        :param executor_id: 执行人ID
        :type executor_id: str
        :param executor_name: 执行人名称
        :type executor_name: str
        :param task_id: 执行机任务ID
        :type task_id: str
        :param execute_id: 执行ID
        :type execute_id: str
        :param time_cost: 执行耗时
        :type time_cost: int
        :param step_txt: 测试步骤
        :type step_txt: str
        :param step_expect: 测试步骤期望结果
        :type step_expect: str
        :param step_actual: 测试步骤实际结果
        :type step_actual: str
        :param step_result: 测试步骤结果
        :type step_result: str
        :param release_dev: 版本号
        :type release_dev: str
        :param creation_version_uri: 创建版本URI
        :type creation_version_uri: str
        :param version_uri: 版本URI
        :type version_uri: str
        :param project_id: 项目ID
        :type project_id: str
        :param report_url: 第三方过来的执行结果，返回跳转到第三方的url
        :type report_url: str
        :param test_case_number: 测试用例编号
        :type test_case_number: str
        :param service_type: 测试类型
        :type service_type: str
        """
        
        

        self._uri = None
        self._name = None
        self._author = None
        self._rank = None
        self._result = None
        self._round = None
        self._preparation = None
        self._description = None
        self._region = None
        self._steps = None
        self._number = None
        self._author_name = None
        self._begin_time = None
        self._begin_time_timestamp = None
        self._end_time = None
        self._end_time_timestamp = None
        self._creation_date = None
        self._creation_date_timestamp = None
        self._last_modified = None
        self._last_modified_timestamp = None
        self._last_change_time = None
        self._last_change_time_timestamp = None
        self._dfx_test_result = None
        self._failure_cause = None
        self._parent_uri = None
        self._test_case_uri = None
        self._test_case_name = None
        self._task_uri = None
        self._result_name = None
        self._test_result_ae = None
        self._executor_id = None
        self._executor_name = None
        self._task_id = None
        self._execute_id = None
        self._time_cost = None
        self._step_txt = None
        self._step_expect = None
        self._step_actual = None
        self._step_result = None
        self._release_dev = None
        self._creation_version_uri = None
        self._version_uri = None
        self._project_id = None
        self._report_url = None
        self._test_case_number = None
        self._service_type = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if author is not None:
            self.author = author
        if rank is not None:
            self.rank = rank
        if result is not None:
            self.result = result
        if round is not None:
            self.round = round
        if preparation is not None:
            self.preparation = preparation
        if description is not None:
            self.description = description
        if region is not None:
            self.region = region
        if steps is not None:
            self.steps = steps
        if number is not None:
            self.number = number
        if author_name is not None:
            self.author_name = author_name
        if begin_time is not None:
            self.begin_time = begin_time
        if begin_time_timestamp is not None:
            self.begin_time_timestamp = begin_time_timestamp
        if end_time is not None:
            self.end_time = end_time
        if end_time_timestamp is not None:
            self.end_time_timestamp = end_time_timestamp
        if creation_date is not None:
            self.creation_date = creation_date
        if creation_date_timestamp is not None:
            self.creation_date_timestamp = creation_date_timestamp
        if last_modified is not None:
            self.last_modified = last_modified
        if last_modified_timestamp is not None:
            self.last_modified_timestamp = last_modified_timestamp
        if last_change_time is not None:
            self.last_change_time = last_change_time
        if last_change_time_timestamp is not None:
            self.last_change_time_timestamp = last_change_time_timestamp
        if dfx_test_result is not None:
            self.dfx_test_result = dfx_test_result
        if failure_cause is not None:
            self.failure_cause = failure_cause
        if parent_uri is not None:
            self.parent_uri = parent_uri
        if test_case_uri is not None:
            self.test_case_uri = test_case_uri
        if test_case_name is not None:
            self.test_case_name = test_case_name
        if task_uri is not None:
            self.task_uri = task_uri
        if result_name is not None:
            self.result_name = result_name
        if test_result_ae is not None:
            self.test_result_ae = test_result_ae
        if executor_id is not None:
            self.executor_id = executor_id
        if executor_name is not None:
            self.executor_name = executor_name
        if task_id is not None:
            self.task_id = task_id
        if execute_id is not None:
            self.execute_id = execute_id
        if time_cost is not None:
            self.time_cost = time_cost
        if step_txt is not None:
            self.step_txt = step_txt
        if step_expect is not None:
            self.step_expect = step_expect
        if step_actual is not None:
            self.step_actual = step_actual
        if step_result is not None:
            self.step_result = step_result
        if release_dev is not None:
            self.release_dev = release_dev
        if creation_version_uri is not None:
            self.creation_version_uri = creation_version_uri
        if version_uri is not None:
            self.version_uri = version_uri
        if project_id is not None:
            self.project_id = project_id
        if report_url is not None:
            self.report_url = report_url
        if test_case_number is not None:
            self.test_case_number = test_case_number
        if service_type is not None:
            self.service_type = service_type

    @property
    def uri(self):
        r"""Gets the uri of this TestResultVo.

        结果URI

        :return: The uri of this TestResultVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this TestResultVo.

        结果URI

        :param uri: The uri of this TestResultVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def name(self):
        r"""Gets the name of this TestResultVo.

        用例结果名称

        :return: The name of this TestResultVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TestResultVo.

        用例结果名称

        :param name: The name of this TestResultVo.
        :type name: str
        """
        self._name = name

    @property
    def author(self):
        r"""Gets the author of this TestResultVo.

        创建人ID

        :return: The author of this TestResultVo.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this TestResultVo.

        创建人ID

        :param author: The author of this TestResultVo.
        :type author: str
        """
        self._author = author

    @property
    def rank(self):
        r"""Gets the rank of this TestResultVo.

        级别

        :return: The rank of this TestResultVo.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        r"""Sets the rank of this TestResultVo.

        级别

        :param rank: The rank of this TestResultVo.
        :type rank: int
        """
        self._rank = rank

    @property
    def result(self):
        r"""Gets the result of this TestResultVo.

        测试结果Code

        :return: The result of this TestResultVo.
        :rtype: int
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this TestResultVo.

        测试结果Code

        :param result: The result of this TestResultVo.
        :type result: int
        """
        self._result = result

    @property
    def round(self):
        r"""Gets the round of this TestResultVo.

        执行批次

        :return: The round of this TestResultVo.
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        r"""Sets the round of this TestResultVo.

        执行批次

        :param round: The round of this TestResultVo.
        :type round: int
        """
        self._round = round

    @property
    def preparation(self):
        r"""Gets the preparation of this TestResultVo.

        前置条件

        :return: The preparation of this TestResultVo.
        :rtype: str
        """
        return self._preparation

    @preparation.setter
    def preparation(self, preparation):
        r"""Sets the preparation of this TestResultVo.

        前置条件

        :param preparation: The preparation of this TestResultVo.
        :type preparation: str
        """
        self._preparation = preparation

    @property
    def description(self):
        r"""Gets the description of this TestResultVo.

        描述

        :return: The description of this TestResultVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TestResultVo.

        描述

        :param description: The description of this TestResultVo.
        :type description: str
        """
        self._description = description

    @property
    def region(self):
        r"""Gets the region of this TestResultVo.

        逻辑Region

        :return: The region of this TestResultVo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this TestResultVo.

        逻辑Region

        :param region: The region of this TestResultVo.
        :type region: str
        """
        self._region = region

    @property
    def steps(self):
        r"""Gets the steps of this TestResultVo.

        测试步骤信息

        :return: The steps of this TestResultVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ResultStepVo`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this TestResultVo.

        测试步骤信息

        :param steps: The steps of this TestResultVo.
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.ResultStepVo`]
        """
        self._steps = steps

    @property
    def number(self):
        r"""Gets the number of this TestResultVo.

        用例结果编号

        :return: The number of this TestResultVo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this TestResultVo.

        用例结果编号

        :param number: The number of this TestResultVo.
        :type number: str
        """
        self._number = number

    @property
    def author_name(self):
        r"""Gets the author_name of this TestResultVo.

        创建人名称

        :return: The author_name of this TestResultVo.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this TestResultVo.

        创建人名称

        :param author_name: The author_name of this TestResultVo.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this TestResultVo.

        执行开始时间

        :return: The begin_time of this TestResultVo.
        :rtype: datetime
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this TestResultVo.

        执行开始时间

        :param begin_time: The begin_time of this TestResultVo.
        :type begin_time: datetime
        """
        self._begin_time = begin_time

    @property
    def begin_time_timestamp(self):
        r"""Gets the begin_time_timestamp of this TestResultVo.

        执行开始时间时间戳

        :return: The begin_time_timestamp of this TestResultVo.
        :rtype: int
        """
        return self._begin_time_timestamp

    @begin_time_timestamp.setter
    def begin_time_timestamp(self, begin_time_timestamp):
        r"""Sets the begin_time_timestamp of this TestResultVo.

        执行开始时间时间戳

        :param begin_time_timestamp: The begin_time_timestamp of this TestResultVo.
        :type begin_time_timestamp: int
        """
        self._begin_time_timestamp = begin_time_timestamp

    @property
    def end_time(self):
        r"""Gets the end_time of this TestResultVo.

        执行结束时间

        :return: The end_time of this TestResultVo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TestResultVo.

        执行结束时间

        :param end_time: The end_time of this TestResultVo.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def end_time_timestamp(self):
        r"""Gets the end_time_timestamp of this TestResultVo.

        执行结束时间时间戳

        :return: The end_time_timestamp of this TestResultVo.
        :rtype: int
        """
        return self._end_time_timestamp

    @end_time_timestamp.setter
    def end_time_timestamp(self, end_time_timestamp):
        r"""Sets the end_time_timestamp of this TestResultVo.

        执行结束时间时间戳

        :param end_time_timestamp: The end_time_timestamp of this TestResultVo.
        :type end_time_timestamp: int
        """
        self._end_time_timestamp = end_time_timestamp

    @property
    def creation_date(self):
        r"""Gets the creation_date of this TestResultVo.

        创建时间

        :return: The creation_date of this TestResultVo.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        r"""Sets the creation_date of this TestResultVo.

        创建时间

        :param creation_date: The creation_date of this TestResultVo.
        :type creation_date: str
        """
        self._creation_date = creation_date

    @property
    def creation_date_timestamp(self):
        r"""Gets the creation_date_timestamp of this TestResultVo.

        创建时间时间戳

        :return: The creation_date_timestamp of this TestResultVo.
        :rtype: int
        """
        return self._creation_date_timestamp

    @creation_date_timestamp.setter
    def creation_date_timestamp(self, creation_date_timestamp):
        r"""Sets the creation_date_timestamp of this TestResultVo.

        创建时间时间戳

        :param creation_date_timestamp: The creation_date_timestamp of this TestResultVo.
        :type creation_date_timestamp: int
        """
        self._creation_date_timestamp = creation_date_timestamp

    @property
    def last_modified(self):
        r"""Gets the last_modified of this TestResultVo.

        最后修改时间

        :return: The last_modified of this TestResultVo.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this TestResultVo.

        最后修改时间

        :param last_modified: The last_modified of this TestResultVo.
        :type last_modified: datetime
        """
        self._last_modified = last_modified

    @property
    def last_modified_timestamp(self):
        r"""Gets the last_modified_timestamp of this TestResultVo.

        最后修改时间

        :return: The last_modified_timestamp of this TestResultVo.
        :rtype: int
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(self, last_modified_timestamp):
        r"""Sets the last_modified_timestamp of this TestResultVo.

        最后修改时间

        :param last_modified_timestamp: The last_modified_timestamp of this TestResultVo.
        :type last_modified_timestamp: int
        """
        self._last_modified_timestamp = last_modified_timestamp

    @property
    def last_change_time(self):
        r"""Gets the last_change_time of this TestResultVo.

        最后变更时间

        :return: The last_change_time of this TestResultVo.
        :rtype: datetime
        """
        return self._last_change_time

    @last_change_time.setter
    def last_change_time(self, last_change_time):
        r"""Sets the last_change_time of this TestResultVo.

        最后变更时间

        :param last_change_time: The last_change_time of this TestResultVo.
        :type last_change_time: datetime
        """
        self._last_change_time = last_change_time

    @property
    def last_change_time_timestamp(self):
        r"""Gets the last_change_time_timestamp of this TestResultVo.

        最后变更时间

        :return: The last_change_time_timestamp of this TestResultVo.
        :rtype: int
        """
        return self._last_change_time_timestamp

    @last_change_time_timestamp.setter
    def last_change_time_timestamp(self, last_change_time_timestamp):
        r"""Sets the last_change_time_timestamp of this TestResultVo.

        最后变更时间

        :param last_change_time_timestamp: The last_change_time_timestamp of this TestResultVo.
        :type last_change_time_timestamp: int
        """
        self._last_change_time_timestamp = last_change_time_timestamp

    @property
    def dfx_test_result(self):
        r"""Gets the dfx_test_result of this TestResultVo.

        DFX测试结果

        :return: The dfx_test_result of this TestResultVo.
        :rtype: str
        """
        return self._dfx_test_result

    @dfx_test_result.setter
    def dfx_test_result(self, dfx_test_result):
        r"""Sets the dfx_test_result of this TestResultVo.

        DFX测试结果

        :param dfx_test_result: The dfx_test_result of this TestResultVo.
        :type dfx_test_result: str
        """
        self._dfx_test_result = dfx_test_result

    @property
    def failure_cause(self):
        r"""Gets the failure_cause of this TestResultVo.

        失败原因

        :return: The failure_cause of this TestResultVo.
        :rtype: str
        """
        return self._failure_cause

    @failure_cause.setter
    def failure_cause(self, failure_cause):
        r"""Sets the failure_cause of this TestResultVo.

        失败原因

        :param failure_cause: The failure_cause of this TestResultVo.
        :type failure_cause: str
        """
        self._failure_cause = failure_cause

    @property
    def parent_uri(self):
        r"""Gets the parent_uri of this TestResultVo.

        父节点URI(分支用例URI或迭代用例URI)

        :return: The parent_uri of this TestResultVo.
        :rtype: str
        """
        return self._parent_uri

    @parent_uri.setter
    def parent_uri(self, parent_uri):
        r"""Sets the parent_uri of this TestResultVo.

        父节点URI(分支用例URI或迭代用例URI)

        :param parent_uri: The parent_uri of this TestResultVo.
        :type parent_uri: str
        """
        self._parent_uri = parent_uri

    @property
    def test_case_uri(self):
        r"""Gets the test_case_uri of this TestResultVo.

        分支用例URI

        :return: The test_case_uri of this TestResultVo.
        :rtype: str
        """
        return self._test_case_uri

    @test_case_uri.setter
    def test_case_uri(self, test_case_uri):
        r"""Sets the test_case_uri of this TestResultVo.

        分支用例URI

        :param test_case_uri: The test_case_uri of this TestResultVo.
        :type test_case_uri: str
        """
        self._test_case_uri = test_case_uri

    @property
    def test_case_name(self):
        r"""Gets the test_case_name of this TestResultVo.

        用例名称

        :return: The test_case_name of this TestResultVo.
        :rtype: str
        """
        return self._test_case_name

    @test_case_name.setter
    def test_case_name(self, test_case_name):
        r"""Sets the test_case_name of this TestResultVo.

        用例名称

        :param test_case_name: The test_case_name of this TestResultVo.
        :type test_case_name: str
        """
        self._test_case_name = test_case_name

    @property
    def task_uri(self):
        r"""Gets the task_uri of this TestResultVo.

        测试任务URI

        :return: The task_uri of this TestResultVo.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this TestResultVo.

        测试任务URI

        :param task_uri: The task_uri of this TestResultVo.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def result_name(self):
        r"""Gets the result_name of this TestResultVo.

        测试结果

        :return: The result_name of this TestResultVo.
        :rtype: str
        """
        return self._result_name

    @result_name.setter
    def result_name(self, result_name):
        r"""Sets the result_name of this TestResultVo.

        测试结果

        :param result_name: The result_name of this TestResultVo.
        :type result_name: str
        """
        self._result_name = result_name

    @property
    def test_result_ae(self):
        r"""Gets the test_result_ae of this TestResultVo.

        是否自动化执行

        :return: The test_result_ae of this TestResultVo.
        :rtype: str
        """
        return self._test_result_ae

    @test_result_ae.setter
    def test_result_ae(self, test_result_ae):
        r"""Sets the test_result_ae of this TestResultVo.

        是否自动化执行

        :param test_result_ae: The test_result_ae of this TestResultVo.
        :type test_result_ae: str
        """
        self._test_result_ae = test_result_ae

    @property
    def executor_id(self):
        r"""Gets the executor_id of this TestResultVo.

        执行人ID

        :return: The executor_id of this TestResultVo.
        :rtype: str
        """
        return self._executor_id

    @executor_id.setter
    def executor_id(self, executor_id):
        r"""Sets the executor_id of this TestResultVo.

        执行人ID

        :param executor_id: The executor_id of this TestResultVo.
        :type executor_id: str
        """
        self._executor_id = executor_id

    @property
    def executor_name(self):
        r"""Gets the executor_name of this TestResultVo.

        执行人名称

        :return: The executor_name of this TestResultVo.
        :rtype: str
        """
        return self._executor_name

    @executor_name.setter
    def executor_name(self, executor_name):
        r"""Sets the executor_name of this TestResultVo.

        执行人名称

        :param executor_name: The executor_name of this TestResultVo.
        :type executor_name: str
        """
        self._executor_name = executor_name

    @property
    def task_id(self):
        r"""Gets the task_id of this TestResultVo.

        执行机任务ID

        :return: The task_id of this TestResultVo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this TestResultVo.

        执行机任务ID

        :param task_id: The task_id of this TestResultVo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def execute_id(self):
        r"""Gets the execute_id of this TestResultVo.

        执行ID

        :return: The execute_id of this TestResultVo.
        :rtype: str
        """
        return self._execute_id

    @execute_id.setter
    def execute_id(self, execute_id):
        r"""Sets the execute_id of this TestResultVo.

        执行ID

        :param execute_id: The execute_id of this TestResultVo.
        :type execute_id: str
        """
        self._execute_id = execute_id

    @property
    def time_cost(self):
        r"""Gets the time_cost of this TestResultVo.

        执行耗时

        :return: The time_cost of this TestResultVo.
        :rtype: int
        """
        return self._time_cost

    @time_cost.setter
    def time_cost(self, time_cost):
        r"""Sets the time_cost of this TestResultVo.

        执行耗时

        :param time_cost: The time_cost of this TestResultVo.
        :type time_cost: int
        """
        self._time_cost = time_cost

    @property
    def step_txt(self):
        r"""Gets the step_txt of this TestResultVo.

        测试步骤

        :return: The step_txt of this TestResultVo.
        :rtype: str
        """
        return self._step_txt

    @step_txt.setter
    def step_txt(self, step_txt):
        r"""Sets the step_txt of this TestResultVo.

        测试步骤

        :param step_txt: The step_txt of this TestResultVo.
        :type step_txt: str
        """
        self._step_txt = step_txt

    @property
    def step_expect(self):
        r"""Gets the step_expect of this TestResultVo.

        测试步骤期望结果

        :return: The step_expect of this TestResultVo.
        :rtype: str
        """
        return self._step_expect

    @step_expect.setter
    def step_expect(self, step_expect):
        r"""Sets the step_expect of this TestResultVo.

        测试步骤期望结果

        :param step_expect: The step_expect of this TestResultVo.
        :type step_expect: str
        """
        self._step_expect = step_expect

    @property
    def step_actual(self):
        r"""Gets the step_actual of this TestResultVo.

        测试步骤实际结果

        :return: The step_actual of this TestResultVo.
        :rtype: str
        """
        return self._step_actual

    @step_actual.setter
    def step_actual(self, step_actual):
        r"""Sets the step_actual of this TestResultVo.

        测试步骤实际结果

        :param step_actual: The step_actual of this TestResultVo.
        :type step_actual: str
        """
        self._step_actual = step_actual

    @property
    def step_result(self):
        r"""Gets the step_result of this TestResultVo.

        测试步骤结果

        :return: The step_result of this TestResultVo.
        :rtype: str
        """
        return self._step_result

    @step_result.setter
    def step_result(self, step_result):
        r"""Sets the step_result of this TestResultVo.

        测试步骤结果

        :param step_result: The step_result of this TestResultVo.
        :type step_result: str
        """
        self._step_result = step_result

    @property
    def release_dev(self):
        r"""Gets the release_dev of this TestResultVo.

        版本号

        :return: The release_dev of this TestResultVo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this TestResultVo.

        版本号

        :param release_dev: The release_dev of this TestResultVo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def creation_version_uri(self):
        r"""Gets the creation_version_uri of this TestResultVo.

        创建版本URI

        :return: The creation_version_uri of this TestResultVo.
        :rtype: str
        """
        return self._creation_version_uri

    @creation_version_uri.setter
    def creation_version_uri(self, creation_version_uri):
        r"""Sets the creation_version_uri of this TestResultVo.

        创建版本URI

        :param creation_version_uri: The creation_version_uri of this TestResultVo.
        :type creation_version_uri: str
        """
        self._creation_version_uri = creation_version_uri

    @property
    def version_uri(self):
        r"""Gets the version_uri of this TestResultVo.

        版本URI

        :return: The version_uri of this TestResultVo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this TestResultVo.

        版本URI

        :param version_uri: The version_uri of this TestResultVo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def project_id(self):
        r"""Gets the project_id of this TestResultVo.

        项目ID

        :return: The project_id of this TestResultVo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TestResultVo.

        项目ID

        :param project_id: The project_id of this TestResultVo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def report_url(self):
        r"""Gets the report_url of this TestResultVo.

        第三方过来的执行结果，返回跳转到第三方的url

        :return: The report_url of this TestResultVo.
        :rtype: str
        """
        return self._report_url

    @report_url.setter
    def report_url(self, report_url):
        r"""Sets the report_url of this TestResultVo.

        第三方过来的执行结果，返回跳转到第三方的url

        :param report_url: The report_url of this TestResultVo.
        :type report_url: str
        """
        self._report_url = report_url

    @property
    def test_case_number(self):
        r"""Gets the test_case_number of this TestResultVo.

        测试用例编号

        :return: The test_case_number of this TestResultVo.
        :rtype: str
        """
        return self._test_case_number

    @test_case_number.setter
    def test_case_number(self, test_case_number):
        r"""Sets the test_case_number of this TestResultVo.

        测试用例编号

        :param test_case_number: The test_case_number of this TestResultVo.
        :type test_case_number: str
        """
        self._test_case_number = test_case_number

    @property
    def service_type(self):
        r"""Gets the service_type of this TestResultVo.

        测试类型

        :return: The service_type of this TestResultVo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this TestResultVo.

        测试类型

        :param service_type: The service_type of this TestResultVo.
        :type service_type: str
        """
        self._service_type = service_type

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
        if not isinstance(other, TestResultVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
