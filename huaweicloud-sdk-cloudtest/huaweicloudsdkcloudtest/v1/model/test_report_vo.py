# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestReportVo:

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
        'creator': 'str',
        'updator': 'str',
        'version_uri': 'str',
        'branch_uri': 'str',
        'version_name': 'str',
        'branch_name': 'str',
        'test_conclusion': 'str',
        'test_conclusion_details': 'str',
        'defect_resolution_rate': 'str',
        'defect_resolution_score': 'str',
        'case_execution_rate': 'str',
        'case_execution_score': 'str',
        'case_pass_rate': 'str',
        'case_pass_score': 'str',
        'issue_pass_rate': 'str',
        'issue_pass_score': 'str',
        'issue_coverage_rate': 'str',
        'issue_coverage_score': 'str',
        'project_residual_defect_index': 'str',
        'iterator_residual_defect_index': 'str',
        'case_automation_details': 'CaseAutomationDetailsVo',
        'case_validity_ratio': 'str',
        'issue_details': 'IssuePassDetailsVo',
        'case_details': 'list[NameAndValueVo]',
        'defect_details_by_severity': 'list[IdAndNameAndValueVo]',
        'defect_details_by_module': 'list[IdAndNameAndValueVo]',
        'case_pass_rate_by_test_type': 'list[DetailTestTypeCasePassRateVo]',
        'test_report_custom_report_detail': 'list[CustomReportListVo]',
        'create_time': 'datetime',
        'create_timestamp': 'int',
        'creator_name': 'str',
        'update_time': 'datetime',
        'update_timestamp': 'int',
        'updator_name': 'str',
        'project_uuid': 'str',
        'risk_analysis': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'creator': 'creator',
        'updator': 'updator',
        'version_uri': 'version_uri',
        'branch_uri': 'branch_uri',
        'version_name': 'version_name',
        'branch_name': 'branch_name',
        'test_conclusion': 'test_conclusion',
        'test_conclusion_details': 'test_conclusion_details',
        'defect_resolution_rate': 'defect_resolution_rate',
        'defect_resolution_score': 'defect_resolution_score',
        'case_execution_rate': 'case_execution_rate',
        'case_execution_score': 'case_execution_score',
        'case_pass_rate': 'case_pass_rate',
        'case_pass_score': 'case_pass_score',
        'issue_pass_rate': 'issue_pass_rate',
        'issue_pass_score': 'issue_pass_score',
        'issue_coverage_rate': 'issue_coverage_rate',
        'issue_coverage_score': 'issue_coverage_score',
        'project_residual_defect_index': 'project_residual_defect_index',
        'iterator_residual_defect_index': 'iterator_residual_defect_index',
        'case_automation_details': 'case_automation_details',
        'case_validity_ratio': 'case_validity_ratio',
        'issue_details': 'issue_details',
        'case_details': 'case_details',
        'defect_details_by_severity': 'defect_details_by_severity',
        'defect_details_by_module': 'defect_details_by_module',
        'case_pass_rate_by_test_type': 'case_pass_rate_by_test_type',
        'test_report_custom_report_detail': 'test_report_custom_report_detail',
        'create_time': 'create_time',
        'create_timestamp': 'create_timestamp',
        'creator_name': 'creator_name',
        'update_time': 'update_time',
        'update_timestamp': 'update_timestamp',
        'updator_name': 'updator_name',
        'project_uuid': 'project_uuid',
        'risk_analysis': 'risk_analysis'
    }

    def __init__(self, uri=None, name=None, creator=None, updator=None, version_uri=None, branch_uri=None, version_name=None, branch_name=None, test_conclusion=None, test_conclusion_details=None, defect_resolution_rate=None, defect_resolution_score=None, case_execution_rate=None, case_execution_score=None, case_pass_rate=None, case_pass_score=None, issue_pass_rate=None, issue_pass_score=None, issue_coverage_rate=None, issue_coverage_score=None, project_residual_defect_index=None, iterator_residual_defect_index=None, case_automation_details=None, case_validity_ratio=None, issue_details=None, case_details=None, defect_details_by_severity=None, defect_details_by_module=None, case_pass_rate_by_test_type=None, test_report_custom_report_detail=None, create_time=None, create_timestamp=None, creator_name=None, update_time=None, update_timestamp=None, updator_name=None, project_uuid=None, risk_analysis=None):
        """TestReportVo

        The model defined in huaweicloud sdk

        :param uri: 测试报告Uri
        :type uri: str
        :param name: 测试报告名称
        :type name: str
        :param creator: 创建人ID
        :type creator: str
        :param updator: 修改人ID
        :type updator: str
        :param version_uri: 测试计划Uri
        :type version_uri: str
        :param branch_uri: 分支Uri
        :type branch_uri: str
        :param version_name: 测试计划名称
        :type version_name: str
        :param branch_name: 分支名称
        :type branch_name: str
        :param test_conclusion: 测试结论
        :type test_conclusion: str
        :param test_conclusion_details: 测试结论描述
        :type test_conclusion_details: str
        :param defect_resolution_rate: 缺陷解决率
        :type defect_resolution_rate: str
        :param defect_resolution_score: 缺陷解决分数
        :type defect_resolution_score: str
        :param case_execution_rate: 用例执行率
        :type case_execution_rate: str
        :param case_execution_score: 用例执行分数
        :type case_execution_score: str
        :param case_pass_rate: 用例通过率
        :type case_pass_rate: str
        :param case_pass_score: 用例通过分数
        :type case_pass_score: str
        :param issue_pass_rate: 需求通过率
        :type issue_pass_rate: str
        :param issue_pass_score: 需求通过分数
        :type issue_pass_score: str
        :param issue_coverage_rate: 需求覆盖率
        :type issue_coverage_rate: str
        :param issue_coverage_score: 需求覆盖分数
        :type issue_coverage_score: str
        :param project_residual_defect_index: 项目总遗留DI
        :type project_residual_defect_index: str
        :param iterator_residual_defect_index: 计划新增DI
        :type iterator_residual_defect_index: str
        :param case_automation_details: 
        :type case_automation_details: :class:`huaweicloudsdkcloudtest.v1.CaseAutomationDetailsVo`
        :param case_validity_ratio: 用例有效性比例
        :type case_validity_ratio: str
        :param issue_details: 
        :type issue_details: :class:`huaweicloudsdkcloudtest.v1.IssuePassDetailsVo`
        :param case_details: 用例通过情况
        :type case_details: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        :param defect_details_by_severity: 缺陷严重程度
        :type defect_details_by_severity: list[:class:`huaweicloudsdkcloudtest.v1.IdAndNameAndValueVo`]
        :param defect_details_by_module: 缺陷按照模块分布情况
        :type defect_details_by_module: list[:class:`huaweicloudsdkcloudtest.v1.IdAndNameAndValueVo`]
        :param case_pass_rate_by_test_type: 每个测试类型的用例通过率
        :type case_pass_rate_by_test_type: list[:class:`huaweicloudsdkcloudtest.v1.DetailTestTypeCasePassRateVo`]
        :param test_report_custom_report_detail: 测试报告自定义报告详情
        :type test_report_custom_report_detail: list[:class:`huaweicloudsdkcloudtest.v1.CustomReportListVo`]
        :param create_time: 创建时间
        :type create_time: datetime
        :param create_timestamp: 创建时间戳
        :type create_timestamp: int
        :param creator_name: 创建人名
        :type creator_name: str
        :param update_time: 修改时间
        :type update_time: datetime
        :param update_timestamp: 修改时间戳
        :type update_timestamp: int
        :param updator_name: 修改人名
        :type updator_name: str
        :param project_uuid: 项目ID
        :type project_uuid: str
        :param risk_analysis: 风险分析
        :type risk_analysis: str
        """
        
        

        self._uri = None
        self._name = None
        self._creator = None
        self._updator = None
        self._version_uri = None
        self._branch_uri = None
        self._version_name = None
        self._branch_name = None
        self._test_conclusion = None
        self._test_conclusion_details = None
        self._defect_resolution_rate = None
        self._defect_resolution_score = None
        self._case_execution_rate = None
        self._case_execution_score = None
        self._case_pass_rate = None
        self._case_pass_score = None
        self._issue_pass_rate = None
        self._issue_pass_score = None
        self._issue_coverage_rate = None
        self._issue_coverage_score = None
        self._project_residual_defect_index = None
        self._iterator_residual_defect_index = None
        self._case_automation_details = None
        self._case_validity_ratio = None
        self._issue_details = None
        self._case_details = None
        self._defect_details_by_severity = None
        self._defect_details_by_module = None
        self._case_pass_rate_by_test_type = None
        self._test_report_custom_report_detail = None
        self._create_time = None
        self._create_timestamp = None
        self._creator_name = None
        self._update_time = None
        self._update_timestamp = None
        self._updator_name = None
        self._project_uuid = None
        self._risk_analysis = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if creator is not None:
            self.creator = creator
        if updator is not None:
            self.updator = updator
        if version_uri is not None:
            self.version_uri = version_uri
        if branch_uri is not None:
            self.branch_uri = branch_uri
        if version_name is not None:
            self.version_name = version_name
        if branch_name is not None:
            self.branch_name = branch_name
        if test_conclusion is not None:
            self.test_conclusion = test_conclusion
        if test_conclusion_details is not None:
            self.test_conclusion_details = test_conclusion_details
        if defect_resolution_rate is not None:
            self.defect_resolution_rate = defect_resolution_rate
        if defect_resolution_score is not None:
            self.defect_resolution_score = defect_resolution_score
        if case_execution_rate is not None:
            self.case_execution_rate = case_execution_rate
        if case_execution_score is not None:
            self.case_execution_score = case_execution_score
        if case_pass_rate is not None:
            self.case_pass_rate = case_pass_rate
        if case_pass_score is not None:
            self.case_pass_score = case_pass_score
        if issue_pass_rate is not None:
            self.issue_pass_rate = issue_pass_rate
        if issue_pass_score is not None:
            self.issue_pass_score = issue_pass_score
        if issue_coverage_rate is not None:
            self.issue_coverage_rate = issue_coverage_rate
        if issue_coverage_score is not None:
            self.issue_coverage_score = issue_coverage_score
        if project_residual_defect_index is not None:
            self.project_residual_defect_index = project_residual_defect_index
        if iterator_residual_defect_index is not None:
            self.iterator_residual_defect_index = iterator_residual_defect_index
        if case_automation_details is not None:
            self.case_automation_details = case_automation_details
        if case_validity_ratio is not None:
            self.case_validity_ratio = case_validity_ratio
        if issue_details is not None:
            self.issue_details = issue_details
        if case_details is not None:
            self.case_details = case_details
        if defect_details_by_severity is not None:
            self.defect_details_by_severity = defect_details_by_severity
        if defect_details_by_module is not None:
            self.defect_details_by_module = defect_details_by_module
        if case_pass_rate_by_test_type is not None:
            self.case_pass_rate_by_test_type = case_pass_rate_by_test_type
        if test_report_custom_report_detail is not None:
            self.test_report_custom_report_detail = test_report_custom_report_detail
        if create_time is not None:
            self.create_time = create_time
        if create_timestamp is not None:
            self.create_timestamp = create_timestamp
        if creator_name is not None:
            self.creator_name = creator_name
        if update_time is not None:
            self.update_time = update_time
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp
        if updator_name is not None:
            self.updator_name = updator_name
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if risk_analysis is not None:
            self.risk_analysis = risk_analysis

    @property
    def uri(self):
        """Gets the uri of this TestReportVo.

        测试报告Uri

        :return: The uri of this TestReportVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this TestReportVo.

        测试报告Uri

        :param uri: The uri of this TestReportVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def name(self):
        """Gets the name of this TestReportVo.

        测试报告名称

        :return: The name of this TestReportVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestReportVo.

        测试报告名称

        :param name: The name of this TestReportVo.
        :type name: str
        """
        self._name = name

    @property
    def creator(self):
        """Gets the creator of this TestReportVo.

        创建人ID

        :return: The creator of this TestReportVo.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this TestReportVo.

        创建人ID

        :param creator: The creator of this TestReportVo.
        :type creator: str
        """
        self._creator = creator

    @property
    def updator(self):
        """Gets the updator of this TestReportVo.

        修改人ID

        :return: The updator of this TestReportVo.
        :rtype: str
        """
        return self._updator

    @updator.setter
    def updator(self, updator):
        """Sets the updator of this TestReportVo.

        修改人ID

        :param updator: The updator of this TestReportVo.
        :type updator: str
        """
        self._updator = updator

    @property
    def version_uri(self):
        """Gets the version_uri of this TestReportVo.

        测试计划Uri

        :return: The version_uri of this TestReportVo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        """Sets the version_uri of this TestReportVo.

        测试计划Uri

        :param version_uri: The version_uri of this TestReportVo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def branch_uri(self):
        """Gets the branch_uri of this TestReportVo.

        分支Uri

        :return: The branch_uri of this TestReportVo.
        :rtype: str
        """
        return self._branch_uri

    @branch_uri.setter
    def branch_uri(self, branch_uri):
        """Sets the branch_uri of this TestReportVo.

        分支Uri

        :param branch_uri: The branch_uri of this TestReportVo.
        :type branch_uri: str
        """
        self._branch_uri = branch_uri

    @property
    def version_name(self):
        """Gets the version_name of this TestReportVo.

        测试计划名称

        :return: The version_name of this TestReportVo.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this TestReportVo.

        测试计划名称

        :param version_name: The version_name of this TestReportVo.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def branch_name(self):
        """Gets the branch_name of this TestReportVo.

        分支名称

        :return: The branch_name of this TestReportVo.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this TestReportVo.

        分支名称

        :param branch_name: The branch_name of this TestReportVo.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def test_conclusion(self):
        """Gets the test_conclusion of this TestReportVo.

        测试结论

        :return: The test_conclusion of this TestReportVo.
        :rtype: str
        """
        return self._test_conclusion

    @test_conclusion.setter
    def test_conclusion(self, test_conclusion):
        """Sets the test_conclusion of this TestReportVo.

        测试结论

        :param test_conclusion: The test_conclusion of this TestReportVo.
        :type test_conclusion: str
        """
        self._test_conclusion = test_conclusion

    @property
    def test_conclusion_details(self):
        """Gets the test_conclusion_details of this TestReportVo.

        测试结论描述

        :return: The test_conclusion_details of this TestReportVo.
        :rtype: str
        """
        return self._test_conclusion_details

    @test_conclusion_details.setter
    def test_conclusion_details(self, test_conclusion_details):
        """Sets the test_conclusion_details of this TestReportVo.

        测试结论描述

        :param test_conclusion_details: The test_conclusion_details of this TestReportVo.
        :type test_conclusion_details: str
        """
        self._test_conclusion_details = test_conclusion_details

    @property
    def defect_resolution_rate(self):
        """Gets the defect_resolution_rate of this TestReportVo.

        缺陷解决率

        :return: The defect_resolution_rate of this TestReportVo.
        :rtype: str
        """
        return self._defect_resolution_rate

    @defect_resolution_rate.setter
    def defect_resolution_rate(self, defect_resolution_rate):
        """Sets the defect_resolution_rate of this TestReportVo.

        缺陷解决率

        :param defect_resolution_rate: The defect_resolution_rate of this TestReportVo.
        :type defect_resolution_rate: str
        """
        self._defect_resolution_rate = defect_resolution_rate

    @property
    def defect_resolution_score(self):
        """Gets the defect_resolution_score of this TestReportVo.

        缺陷解决分数

        :return: The defect_resolution_score of this TestReportVo.
        :rtype: str
        """
        return self._defect_resolution_score

    @defect_resolution_score.setter
    def defect_resolution_score(self, defect_resolution_score):
        """Sets the defect_resolution_score of this TestReportVo.

        缺陷解决分数

        :param defect_resolution_score: The defect_resolution_score of this TestReportVo.
        :type defect_resolution_score: str
        """
        self._defect_resolution_score = defect_resolution_score

    @property
    def case_execution_rate(self):
        """Gets the case_execution_rate of this TestReportVo.

        用例执行率

        :return: The case_execution_rate of this TestReportVo.
        :rtype: str
        """
        return self._case_execution_rate

    @case_execution_rate.setter
    def case_execution_rate(self, case_execution_rate):
        """Sets the case_execution_rate of this TestReportVo.

        用例执行率

        :param case_execution_rate: The case_execution_rate of this TestReportVo.
        :type case_execution_rate: str
        """
        self._case_execution_rate = case_execution_rate

    @property
    def case_execution_score(self):
        """Gets the case_execution_score of this TestReportVo.

        用例执行分数

        :return: The case_execution_score of this TestReportVo.
        :rtype: str
        """
        return self._case_execution_score

    @case_execution_score.setter
    def case_execution_score(self, case_execution_score):
        """Sets the case_execution_score of this TestReportVo.

        用例执行分数

        :param case_execution_score: The case_execution_score of this TestReportVo.
        :type case_execution_score: str
        """
        self._case_execution_score = case_execution_score

    @property
    def case_pass_rate(self):
        """Gets the case_pass_rate of this TestReportVo.

        用例通过率

        :return: The case_pass_rate of this TestReportVo.
        :rtype: str
        """
        return self._case_pass_rate

    @case_pass_rate.setter
    def case_pass_rate(self, case_pass_rate):
        """Sets the case_pass_rate of this TestReportVo.

        用例通过率

        :param case_pass_rate: The case_pass_rate of this TestReportVo.
        :type case_pass_rate: str
        """
        self._case_pass_rate = case_pass_rate

    @property
    def case_pass_score(self):
        """Gets the case_pass_score of this TestReportVo.

        用例通过分数

        :return: The case_pass_score of this TestReportVo.
        :rtype: str
        """
        return self._case_pass_score

    @case_pass_score.setter
    def case_pass_score(self, case_pass_score):
        """Sets the case_pass_score of this TestReportVo.

        用例通过分数

        :param case_pass_score: The case_pass_score of this TestReportVo.
        :type case_pass_score: str
        """
        self._case_pass_score = case_pass_score

    @property
    def issue_pass_rate(self):
        """Gets the issue_pass_rate of this TestReportVo.

        需求通过率

        :return: The issue_pass_rate of this TestReportVo.
        :rtype: str
        """
        return self._issue_pass_rate

    @issue_pass_rate.setter
    def issue_pass_rate(self, issue_pass_rate):
        """Sets the issue_pass_rate of this TestReportVo.

        需求通过率

        :param issue_pass_rate: The issue_pass_rate of this TestReportVo.
        :type issue_pass_rate: str
        """
        self._issue_pass_rate = issue_pass_rate

    @property
    def issue_pass_score(self):
        """Gets the issue_pass_score of this TestReportVo.

        需求通过分数

        :return: The issue_pass_score of this TestReportVo.
        :rtype: str
        """
        return self._issue_pass_score

    @issue_pass_score.setter
    def issue_pass_score(self, issue_pass_score):
        """Sets the issue_pass_score of this TestReportVo.

        需求通过分数

        :param issue_pass_score: The issue_pass_score of this TestReportVo.
        :type issue_pass_score: str
        """
        self._issue_pass_score = issue_pass_score

    @property
    def issue_coverage_rate(self):
        """Gets the issue_coverage_rate of this TestReportVo.

        需求覆盖率

        :return: The issue_coverage_rate of this TestReportVo.
        :rtype: str
        """
        return self._issue_coverage_rate

    @issue_coverage_rate.setter
    def issue_coverage_rate(self, issue_coverage_rate):
        """Sets the issue_coverage_rate of this TestReportVo.

        需求覆盖率

        :param issue_coverage_rate: The issue_coverage_rate of this TestReportVo.
        :type issue_coverage_rate: str
        """
        self._issue_coverage_rate = issue_coverage_rate

    @property
    def issue_coverage_score(self):
        """Gets the issue_coverage_score of this TestReportVo.

        需求覆盖分数

        :return: The issue_coverage_score of this TestReportVo.
        :rtype: str
        """
        return self._issue_coverage_score

    @issue_coverage_score.setter
    def issue_coverage_score(self, issue_coverage_score):
        """Sets the issue_coverage_score of this TestReportVo.

        需求覆盖分数

        :param issue_coverage_score: The issue_coverage_score of this TestReportVo.
        :type issue_coverage_score: str
        """
        self._issue_coverage_score = issue_coverage_score

    @property
    def project_residual_defect_index(self):
        """Gets the project_residual_defect_index of this TestReportVo.

        项目总遗留DI

        :return: The project_residual_defect_index of this TestReportVo.
        :rtype: str
        """
        return self._project_residual_defect_index

    @project_residual_defect_index.setter
    def project_residual_defect_index(self, project_residual_defect_index):
        """Sets the project_residual_defect_index of this TestReportVo.

        项目总遗留DI

        :param project_residual_defect_index: The project_residual_defect_index of this TestReportVo.
        :type project_residual_defect_index: str
        """
        self._project_residual_defect_index = project_residual_defect_index

    @property
    def iterator_residual_defect_index(self):
        """Gets the iterator_residual_defect_index of this TestReportVo.

        计划新增DI

        :return: The iterator_residual_defect_index of this TestReportVo.
        :rtype: str
        """
        return self._iterator_residual_defect_index

    @iterator_residual_defect_index.setter
    def iterator_residual_defect_index(self, iterator_residual_defect_index):
        """Sets the iterator_residual_defect_index of this TestReportVo.

        计划新增DI

        :param iterator_residual_defect_index: The iterator_residual_defect_index of this TestReportVo.
        :type iterator_residual_defect_index: str
        """
        self._iterator_residual_defect_index = iterator_residual_defect_index

    @property
    def case_automation_details(self):
        """Gets the case_automation_details of this TestReportVo.

        :return: The case_automation_details of this TestReportVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CaseAutomationDetailsVo`
        """
        return self._case_automation_details

    @case_automation_details.setter
    def case_automation_details(self, case_automation_details):
        """Sets the case_automation_details of this TestReportVo.

        :param case_automation_details: The case_automation_details of this TestReportVo.
        :type case_automation_details: :class:`huaweicloudsdkcloudtest.v1.CaseAutomationDetailsVo`
        """
        self._case_automation_details = case_automation_details

    @property
    def case_validity_ratio(self):
        """Gets the case_validity_ratio of this TestReportVo.

        用例有效性比例

        :return: The case_validity_ratio of this TestReportVo.
        :rtype: str
        """
        return self._case_validity_ratio

    @case_validity_ratio.setter
    def case_validity_ratio(self, case_validity_ratio):
        """Sets the case_validity_ratio of this TestReportVo.

        用例有效性比例

        :param case_validity_ratio: The case_validity_ratio of this TestReportVo.
        :type case_validity_ratio: str
        """
        self._case_validity_ratio = case_validity_ratio

    @property
    def issue_details(self):
        """Gets the issue_details of this TestReportVo.

        :return: The issue_details of this TestReportVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.IssuePassDetailsVo`
        """
        return self._issue_details

    @issue_details.setter
    def issue_details(self, issue_details):
        """Sets the issue_details of this TestReportVo.

        :param issue_details: The issue_details of this TestReportVo.
        :type issue_details: :class:`huaweicloudsdkcloudtest.v1.IssuePassDetailsVo`
        """
        self._issue_details = issue_details

    @property
    def case_details(self):
        """Gets the case_details of this TestReportVo.

        用例通过情况

        :return: The case_details of this TestReportVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        return self._case_details

    @case_details.setter
    def case_details(self, case_details):
        """Sets the case_details of this TestReportVo.

        用例通过情况

        :param case_details: The case_details of this TestReportVo.
        :type case_details: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        self._case_details = case_details

    @property
    def defect_details_by_severity(self):
        """Gets the defect_details_by_severity of this TestReportVo.

        缺陷严重程度

        :return: The defect_details_by_severity of this TestReportVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.IdAndNameAndValueVo`]
        """
        return self._defect_details_by_severity

    @defect_details_by_severity.setter
    def defect_details_by_severity(self, defect_details_by_severity):
        """Sets the defect_details_by_severity of this TestReportVo.

        缺陷严重程度

        :param defect_details_by_severity: The defect_details_by_severity of this TestReportVo.
        :type defect_details_by_severity: list[:class:`huaweicloudsdkcloudtest.v1.IdAndNameAndValueVo`]
        """
        self._defect_details_by_severity = defect_details_by_severity

    @property
    def defect_details_by_module(self):
        """Gets the defect_details_by_module of this TestReportVo.

        缺陷按照模块分布情况

        :return: The defect_details_by_module of this TestReportVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.IdAndNameAndValueVo`]
        """
        return self._defect_details_by_module

    @defect_details_by_module.setter
    def defect_details_by_module(self, defect_details_by_module):
        """Sets the defect_details_by_module of this TestReportVo.

        缺陷按照模块分布情况

        :param defect_details_by_module: The defect_details_by_module of this TestReportVo.
        :type defect_details_by_module: list[:class:`huaweicloudsdkcloudtest.v1.IdAndNameAndValueVo`]
        """
        self._defect_details_by_module = defect_details_by_module

    @property
    def case_pass_rate_by_test_type(self):
        """Gets the case_pass_rate_by_test_type of this TestReportVo.

        每个测试类型的用例通过率

        :return: The case_pass_rate_by_test_type of this TestReportVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.DetailTestTypeCasePassRateVo`]
        """
        return self._case_pass_rate_by_test_type

    @case_pass_rate_by_test_type.setter
    def case_pass_rate_by_test_type(self, case_pass_rate_by_test_type):
        """Sets the case_pass_rate_by_test_type of this TestReportVo.

        每个测试类型的用例通过率

        :param case_pass_rate_by_test_type: The case_pass_rate_by_test_type of this TestReportVo.
        :type case_pass_rate_by_test_type: list[:class:`huaweicloudsdkcloudtest.v1.DetailTestTypeCasePassRateVo`]
        """
        self._case_pass_rate_by_test_type = case_pass_rate_by_test_type

    @property
    def test_report_custom_report_detail(self):
        """Gets the test_report_custom_report_detail of this TestReportVo.

        测试报告自定义报告详情

        :return: The test_report_custom_report_detail of this TestReportVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.CustomReportListVo`]
        """
        return self._test_report_custom_report_detail

    @test_report_custom_report_detail.setter
    def test_report_custom_report_detail(self, test_report_custom_report_detail):
        """Sets the test_report_custom_report_detail of this TestReportVo.

        测试报告自定义报告详情

        :param test_report_custom_report_detail: The test_report_custom_report_detail of this TestReportVo.
        :type test_report_custom_report_detail: list[:class:`huaweicloudsdkcloudtest.v1.CustomReportListVo`]
        """
        self._test_report_custom_report_detail = test_report_custom_report_detail

    @property
    def create_time(self):
        """Gets the create_time of this TestReportVo.

        创建时间

        :return: The create_time of this TestReportVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TestReportVo.

        创建时间

        :param create_time: The create_time of this TestReportVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_timestamp(self):
        """Gets the create_timestamp of this TestReportVo.

        创建时间戳

        :return: The create_timestamp of this TestReportVo.
        :rtype: int
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """Sets the create_timestamp of this TestReportVo.

        创建时间戳

        :param create_timestamp: The create_timestamp of this TestReportVo.
        :type create_timestamp: int
        """
        self._create_timestamp = create_timestamp

    @property
    def creator_name(self):
        """Gets the creator_name of this TestReportVo.

        创建人名

        :return: The creator_name of this TestReportVo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this TestReportVo.

        创建人名

        :param creator_name: The creator_name of this TestReportVo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def update_time(self):
        """Gets the update_time of this TestReportVo.

        修改时间

        :return: The update_time of this TestReportVo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TestReportVo.

        修改时间

        :param update_time: The update_time of this TestReportVo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def update_timestamp(self):
        """Gets the update_timestamp of this TestReportVo.

        修改时间戳

        :return: The update_timestamp of this TestReportVo.
        :rtype: int
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        """Sets the update_timestamp of this TestReportVo.

        修改时间戳

        :param update_timestamp: The update_timestamp of this TestReportVo.
        :type update_timestamp: int
        """
        self._update_timestamp = update_timestamp

    @property
    def updator_name(self):
        """Gets the updator_name of this TestReportVo.

        修改人名

        :return: The updator_name of this TestReportVo.
        :rtype: str
        """
        return self._updator_name

    @updator_name.setter
    def updator_name(self, updator_name):
        """Sets the updator_name of this TestReportVo.

        修改人名

        :param updator_name: The updator_name of this TestReportVo.
        :type updator_name: str
        """
        self._updator_name = updator_name

    @property
    def project_uuid(self):
        """Gets the project_uuid of this TestReportVo.

        项目ID

        :return: The project_uuid of this TestReportVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this TestReportVo.

        项目ID

        :param project_uuid: The project_uuid of this TestReportVo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def risk_analysis(self):
        """Gets the risk_analysis of this TestReportVo.

        风险分析

        :return: The risk_analysis of this TestReportVo.
        :rtype: str
        """
        return self._risk_analysis

    @risk_analysis.setter
    def risk_analysis(self, risk_analysis):
        """Sets the risk_analysis of this TestReportVo.

        风险分析

        :param risk_analysis: The risk_analysis of this TestReportVo.
        :type risk_analysis: str
        """
        self._risk_analysis = risk_analysis

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
        if not isinstance(other, TestReportVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
