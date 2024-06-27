# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseListVo:

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
        'owner': 'NameAndIdVo',
        'status': 'NameAndIdVo',
        'result': 'NameAndIdVo',
        'module': 'NameAndIdVo',
        'iteration': 'NameAndIdVo',
        'exeplatform': 'str',
        'number': 'str',
        'description': 'str',
        'rank_id': 'str',
        'feature_uri': 'str',
        'release_dev': 'str',
        'is_keyword': 'bool',
        'script_url': 'str',
        'report_url': 'str',
        'project_uuid': 'str',
        'service_type': 'NameAndIdVo',
        'test_type': 'IntegerIdAndNameVo',
        'create_info': 'CreateInfoVo',
        'execute_info': 'ExecuteInfoVo',
        'associate_issue_info': 'AssociateIssueInfoVo',
        'associate_defect_info': 'AssociateDefectInfoVo',
        'case_type': 'int',
        'labels': 'str',
        'custom_field_info': 'list[CustomFieldVo]',
        'is_test_design': 'bool',
        'last_modified': 'int',
        'review_status': 'int'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'owner': 'owner',
        'status': 'status',
        'result': 'result',
        'module': 'module',
        'iteration': 'iteration',
        'exeplatform': 'exeplatform',
        'number': 'number',
        'description': 'description',
        'rank_id': 'rank_id',
        'feature_uri': 'feature_uri',
        'release_dev': 'release_dev',
        'is_keyword': 'is_keyword',
        'script_url': 'script_url',
        'report_url': 'report_url',
        'project_uuid': 'project_uuid',
        'service_type': 'service_type',
        'test_type': 'test_type',
        'create_info': 'create_info',
        'execute_info': 'execute_info',
        'associate_issue_info': 'associate_issue_info',
        'associate_defect_info': 'associate_defect_info',
        'case_type': 'case_type',
        'labels': 'labels',
        'custom_field_info': 'custom_field_info',
        'is_test_design': 'is_test_design',
        'last_modified': 'last_modified',
        'review_status': 'review_status'
    }

    def __init__(self, uri=None, name=None, owner=None, status=None, result=None, module=None, iteration=None, exeplatform=None, number=None, description=None, rank_id=None, feature_uri=None, release_dev=None, is_keyword=None, script_url=None, report_url=None, project_uuid=None, service_type=None, test_type=None, create_info=None, execute_info=None, associate_issue_info=None, associate_defect_info=None, case_type=None, labels=None, custom_field_info=None, is_test_design=None, last_modified=None, review_status=None):
        """TestCaseListVo

        The model defined in huaweicloud sdk

        :param uri: 用例URI
        :type uri: str
        :param name: 用例名称
        :type name: str
        :param owner: 
        :type owner: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param status: 
        :type status: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param result: 
        :type result: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param module: 
        :type module: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param iteration: 
        :type iteration: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param exeplatform: 执行平台，如：apittest,其他三方执行平台
        :type exeplatform: str
        :param number: 用例编号
        :type number: str
        :param description: 用例描述
        :type description: str
        :param rank_id: 用例等级
        :type rank_id: str
        :param feature_uri: 目录URI
        :type feature_uri: str
        :param release_dev: 版本号
        :type release_dev: str
        :param is_keyword: 是否组合关键字
        :type is_keyword: bool
        :param script_url: 脚本路径
        :type script_url: str
        :param report_url: 实时报告地址
        :type report_url: str
        :param project_uuid: 项目ID
        :type project_uuid: str
        :param service_type: 
        :type service_type: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param test_type: 
        :type test_type: :class:`huaweicloudsdkcloudtest.v1.IntegerIdAndNameVo`
        :param create_info: 
        :type create_info: :class:`huaweicloudsdkcloudtest.v1.CreateInfoVo`
        :param execute_info: 
        :type execute_info: :class:`huaweicloudsdkcloudtest.v1.ExecuteInfoVo`
        :param associate_issue_info: 
        :type associate_issue_info: :class:`huaweicloudsdkcloudtest.v1.AssociateIssueInfoVo`
        :param associate_defect_info: 
        :type associate_defect_info: :class:`huaweicloudsdkcloudtest.v1.AssociateDefectInfoVo`
        :param case_type: 用例类型
        :type case_type: int
        :param labels: 用例标签名称列表
        :type labels: str
        :param custom_field_info: 自定义字段信息
        :type custom_field_info: list[:class:`huaweicloudsdkcloudtest.v1.CustomFieldVo`]
        :param is_test_design: 是否来自测试设计（null：不限，false：否来自测试设计，true：来自测试设计）
        :type is_test_design: bool
        :param last_modified: 最后修改时间（null：不限）
        :type last_modified: int
        :param review_status: 用例评审状态（null：0至127）
        :type review_status: int
        """
        
        

        self._uri = None
        self._name = None
        self._owner = None
        self._status = None
        self._result = None
        self._module = None
        self._iteration = None
        self._exeplatform = None
        self._number = None
        self._description = None
        self._rank_id = None
        self._feature_uri = None
        self._release_dev = None
        self._is_keyword = None
        self._script_url = None
        self._report_url = None
        self._project_uuid = None
        self._service_type = None
        self._test_type = None
        self._create_info = None
        self._execute_info = None
        self._associate_issue_info = None
        self._associate_defect_info = None
        self._case_type = None
        self._labels = None
        self._custom_field_info = None
        self._is_test_design = None
        self._last_modified = None
        self._review_status = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if status is not None:
            self.status = status
        if result is not None:
            self.result = result
        if module is not None:
            self.module = module
        if iteration is not None:
            self.iteration = iteration
        if exeplatform is not None:
            self.exeplatform = exeplatform
        if number is not None:
            self.number = number
        if description is not None:
            self.description = description
        if rank_id is not None:
            self.rank_id = rank_id
        if feature_uri is not None:
            self.feature_uri = feature_uri
        if release_dev is not None:
            self.release_dev = release_dev
        if is_keyword is not None:
            self.is_keyword = is_keyword
        if script_url is not None:
            self.script_url = script_url
        if report_url is not None:
            self.report_url = report_url
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if service_type is not None:
            self.service_type = service_type
        if test_type is not None:
            self.test_type = test_type
        if create_info is not None:
            self.create_info = create_info
        if execute_info is not None:
            self.execute_info = execute_info
        if associate_issue_info is not None:
            self.associate_issue_info = associate_issue_info
        if associate_defect_info is not None:
            self.associate_defect_info = associate_defect_info
        if case_type is not None:
            self.case_type = case_type
        if labels is not None:
            self.labels = labels
        if custom_field_info is not None:
            self.custom_field_info = custom_field_info
        if is_test_design is not None:
            self.is_test_design = is_test_design
        if last_modified is not None:
            self.last_modified = last_modified
        if review_status is not None:
            self.review_status = review_status

    @property
    def uri(self):
        """Gets the uri of this TestCaseListVo.

        用例URI

        :return: The uri of this TestCaseListVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this TestCaseListVo.

        用例URI

        :param uri: The uri of this TestCaseListVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def name(self):
        """Gets the name of this TestCaseListVo.

        用例名称

        :return: The name of this TestCaseListVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestCaseListVo.

        用例名称

        :param name: The name of this TestCaseListVo.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this TestCaseListVo.

        :return: The owner of this TestCaseListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this TestCaseListVo.

        :param owner: The owner of this TestCaseListVo.
        :type owner: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._owner = owner

    @property
    def status(self):
        """Gets the status of this TestCaseListVo.

        :return: The status of this TestCaseListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TestCaseListVo.

        :param status: The status of this TestCaseListVo.
        :type status: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._status = status

    @property
    def result(self):
        """Gets the result of this TestCaseListVo.

        :return: The result of this TestCaseListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this TestCaseListVo.

        :param result: The result of this TestCaseListVo.
        :type result: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._result = result

    @property
    def module(self):
        """Gets the module of this TestCaseListVo.

        :return: The module of this TestCaseListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this TestCaseListVo.

        :param module: The module of this TestCaseListVo.
        :type module: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._module = module

    @property
    def iteration(self):
        """Gets the iteration of this TestCaseListVo.

        :return: The iteration of this TestCaseListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        """Sets the iteration of this TestCaseListVo.

        :param iteration: The iteration of this TestCaseListVo.
        :type iteration: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._iteration = iteration

    @property
    def exeplatform(self):
        """Gets the exeplatform of this TestCaseListVo.

        执行平台，如：apittest,其他三方执行平台

        :return: The exeplatform of this TestCaseListVo.
        :rtype: str
        """
        return self._exeplatform

    @exeplatform.setter
    def exeplatform(self, exeplatform):
        """Sets the exeplatform of this TestCaseListVo.

        执行平台，如：apittest,其他三方执行平台

        :param exeplatform: The exeplatform of this TestCaseListVo.
        :type exeplatform: str
        """
        self._exeplatform = exeplatform

    @property
    def number(self):
        """Gets the number of this TestCaseListVo.

        用例编号

        :return: The number of this TestCaseListVo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TestCaseListVo.

        用例编号

        :param number: The number of this TestCaseListVo.
        :type number: str
        """
        self._number = number

    @property
    def description(self):
        """Gets the description of this TestCaseListVo.

        用例描述

        :return: The description of this TestCaseListVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TestCaseListVo.

        用例描述

        :param description: The description of this TestCaseListVo.
        :type description: str
        """
        self._description = description

    @property
    def rank_id(self):
        """Gets the rank_id of this TestCaseListVo.

        用例等级

        :return: The rank_id of this TestCaseListVo.
        :rtype: str
        """
        return self._rank_id

    @rank_id.setter
    def rank_id(self, rank_id):
        """Sets the rank_id of this TestCaseListVo.

        用例等级

        :param rank_id: The rank_id of this TestCaseListVo.
        :type rank_id: str
        """
        self._rank_id = rank_id

    @property
    def feature_uri(self):
        """Gets the feature_uri of this TestCaseListVo.

        目录URI

        :return: The feature_uri of this TestCaseListVo.
        :rtype: str
        """
        return self._feature_uri

    @feature_uri.setter
    def feature_uri(self, feature_uri):
        """Sets the feature_uri of this TestCaseListVo.

        目录URI

        :param feature_uri: The feature_uri of this TestCaseListVo.
        :type feature_uri: str
        """
        self._feature_uri = feature_uri

    @property
    def release_dev(self):
        """Gets the release_dev of this TestCaseListVo.

        版本号

        :return: The release_dev of this TestCaseListVo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        """Sets the release_dev of this TestCaseListVo.

        版本号

        :param release_dev: The release_dev of this TestCaseListVo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def is_keyword(self):
        """Gets the is_keyword of this TestCaseListVo.

        是否组合关键字

        :return: The is_keyword of this TestCaseListVo.
        :rtype: bool
        """
        return self._is_keyword

    @is_keyword.setter
    def is_keyword(self, is_keyword):
        """Sets the is_keyword of this TestCaseListVo.

        是否组合关键字

        :param is_keyword: The is_keyword of this TestCaseListVo.
        :type is_keyword: bool
        """
        self._is_keyword = is_keyword

    @property
    def script_url(self):
        """Gets the script_url of this TestCaseListVo.

        脚本路径

        :return: The script_url of this TestCaseListVo.
        :rtype: str
        """
        return self._script_url

    @script_url.setter
    def script_url(self, script_url):
        """Sets the script_url of this TestCaseListVo.

        脚本路径

        :param script_url: The script_url of this TestCaseListVo.
        :type script_url: str
        """
        self._script_url = script_url

    @property
    def report_url(self):
        """Gets the report_url of this TestCaseListVo.

        实时报告地址

        :return: The report_url of this TestCaseListVo.
        :rtype: str
        """
        return self._report_url

    @report_url.setter
    def report_url(self, report_url):
        """Sets the report_url of this TestCaseListVo.

        实时报告地址

        :param report_url: The report_url of this TestCaseListVo.
        :type report_url: str
        """
        self._report_url = report_url

    @property
    def project_uuid(self):
        """Gets the project_uuid of this TestCaseListVo.

        项目ID

        :return: The project_uuid of this TestCaseListVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this TestCaseListVo.

        项目ID

        :param project_uuid: The project_uuid of this TestCaseListVo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def service_type(self):
        """Gets the service_type of this TestCaseListVo.

        :return: The service_type of this TestCaseListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this TestCaseListVo.

        :param service_type: The service_type of this TestCaseListVo.
        :type service_type: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._service_type = service_type

    @property
    def test_type(self):
        """Gets the test_type of this TestCaseListVo.

        :return: The test_type of this TestCaseListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.IntegerIdAndNameVo`
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        """Sets the test_type of this TestCaseListVo.

        :param test_type: The test_type of this TestCaseListVo.
        :type test_type: :class:`huaweicloudsdkcloudtest.v1.IntegerIdAndNameVo`
        """
        self._test_type = test_type

    @property
    def create_info(self):
        """Gets the create_info of this TestCaseListVo.

        :return: The create_info of this TestCaseListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CreateInfoVo`
        """
        return self._create_info

    @create_info.setter
    def create_info(self, create_info):
        """Sets the create_info of this TestCaseListVo.

        :param create_info: The create_info of this TestCaseListVo.
        :type create_info: :class:`huaweicloudsdkcloudtest.v1.CreateInfoVo`
        """
        self._create_info = create_info

    @property
    def execute_info(self):
        """Gets the execute_info of this TestCaseListVo.

        :return: The execute_info of this TestCaseListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ExecuteInfoVo`
        """
        return self._execute_info

    @execute_info.setter
    def execute_info(self, execute_info):
        """Sets the execute_info of this TestCaseListVo.

        :param execute_info: The execute_info of this TestCaseListVo.
        :type execute_info: :class:`huaweicloudsdkcloudtest.v1.ExecuteInfoVo`
        """
        self._execute_info = execute_info

    @property
    def associate_issue_info(self):
        """Gets the associate_issue_info of this TestCaseListVo.

        :return: The associate_issue_info of this TestCaseListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AssociateIssueInfoVo`
        """
        return self._associate_issue_info

    @associate_issue_info.setter
    def associate_issue_info(self, associate_issue_info):
        """Sets the associate_issue_info of this TestCaseListVo.

        :param associate_issue_info: The associate_issue_info of this TestCaseListVo.
        :type associate_issue_info: :class:`huaweicloudsdkcloudtest.v1.AssociateIssueInfoVo`
        """
        self._associate_issue_info = associate_issue_info

    @property
    def associate_defect_info(self):
        """Gets the associate_defect_info of this TestCaseListVo.

        :return: The associate_defect_info of this TestCaseListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AssociateDefectInfoVo`
        """
        return self._associate_defect_info

    @associate_defect_info.setter
    def associate_defect_info(self, associate_defect_info):
        """Sets the associate_defect_info of this TestCaseListVo.

        :param associate_defect_info: The associate_defect_info of this TestCaseListVo.
        :type associate_defect_info: :class:`huaweicloudsdkcloudtest.v1.AssociateDefectInfoVo`
        """
        self._associate_defect_info = associate_defect_info

    @property
    def case_type(self):
        """Gets the case_type of this TestCaseListVo.

        用例类型

        :return: The case_type of this TestCaseListVo.
        :rtype: int
        """
        return self._case_type

    @case_type.setter
    def case_type(self, case_type):
        """Sets the case_type of this TestCaseListVo.

        用例类型

        :param case_type: The case_type of this TestCaseListVo.
        :type case_type: int
        """
        self._case_type = case_type

    @property
    def labels(self):
        """Gets the labels of this TestCaseListVo.

        用例标签名称列表

        :return: The labels of this TestCaseListVo.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this TestCaseListVo.

        用例标签名称列表

        :param labels: The labels of this TestCaseListVo.
        :type labels: str
        """
        self._labels = labels

    @property
    def custom_field_info(self):
        """Gets the custom_field_info of this TestCaseListVo.

        自定义字段信息

        :return: The custom_field_info of this TestCaseListVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.CustomFieldVo`]
        """
        return self._custom_field_info

    @custom_field_info.setter
    def custom_field_info(self, custom_field_info):
        """Sets the custom_field_info of this TestCaseListVo.

        自定义字段信息

        :param custom_field_info: The custom_field_info of this TestCaseListVo.
        :type custom_field_info: list[:class:`huaweicloudsdkcloudtest.v1.CustomFieldVo`]
        """
        self._custom_field_info = custom_field_info

    @property
    def is_test_design(self):
        """Gets the is_test_design of this TestCaseListVo.

        是否来自测试设计（null：不限，false：否来自测试设计，true：来自测试设计）

        :return: The is_test_design of this TestCaseListVo.
        :rtype: bool
        """
        return self._is_test_design

    @is_test_design.setter
    def is_test_design(self, is_test_design):
        """Sets the is_test_design of this TestCaseListVo.

        是否来自测试设计（null：不限，false：否来自测试设计，true：来自测试设计）

        :param is_test_design: The is_test_design of this TestCaseListVo.
        :type is_test_design: bool
        """
        self._is_test_design = is_test_design

    @property
    def last_modified(self):
        """Gets the last_modified of this TestCaseListVo.

        最后修改时间（null：不限）

        :return: The last_modified of this TestCaseListVo.
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this TestCaseListVo.

        最后修改时间（null：不限）

        :param last_modified: The last_modified of this TestCaseListVo.
        :type last_modified: int
        """
        self._last_modified = last_modified

    @property
    def review_status(self):
        """Gets the review_status of this TestCaseListVo.

        用例评审状态（null：0至127）

        :return: The review_status of this TestCaseListVo.
        :rtype: int
        """
        return self._review_status

    @review_status.setter
    def review_status(self, review_status):
        """Sets the review_status of this TestCaseListVo.

        用例评审状态（null：0至127）

        :param review_status: The review_status of this TestCaseListVo.
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
        if not isinstance(other, TestCaseListVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
