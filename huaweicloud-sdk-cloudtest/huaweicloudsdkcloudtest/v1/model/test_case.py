# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_type': 'str',
        'case_design_desc': 'str',
        'case_name': 'str',
        'case_num': 'str',
        'create_time': 'datetime',
        'creator_name': 'str',
        'creator_num': 'str',
        'deleted': 'str',
        'expected_results': 'str',
        'extra_param': 'str',
        'factor_combination_json': 'str',
        'operation_and_expected_result': 'str',
        'id': 'str',
        'is_archive': 'bool',
        'mindmap_id': 'str',
        'node_id': 'str',
        'batch_id': 'str',
        'branch_id': 'str',
        'plan_id': 'str',
        'prerequisite': 'str',
        'test_case_level': 'str',
        'test_procedure': 'str',
        'update_name': 'str',
        'update_num': 'str',
        'update_time': 'datetime',
        'url': 'str',
        'uri': 'str',
        'project_id': 'str',
        'service_id': 'str'
    }

    attribute_map = {
        'auto_type': 'auto_type',
        'case_design_desc': 'case_design_desc',
        'case_name': 'case_name',
        'case_num': 'case_num',
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'creator_num': 'creator_num',
        'deleted': 'deleted',
        'expected_results': 'expected_results',
        'extra_param': 'extra_param',
        'factor_combination_json': 'factor_combination_json',
        'operation_and_expected_result': 'operation_and_expected_result',
        'id': 'id',
        'is_archive': 'is_archive',
        'mindmap_id': 'mindmap_id',
        'node_id': 'node_id',
        'batch_id': 'batch_id',
        'branch_id': 'branch_id',
        'plan_id': 'plan_id',
        'prerequisite': 'prerequisite',
        'test_case_level': 'test_case_level',
        'test_procedure': 'test_procedure',
        'update_name': 'update_name',
        'update_num': 'update_num',
        'update_time': 'update_time',
        'url': 'url',
        'uri': 'uri',
        'project_id': 'project_id',
        'service_id': 'service_id'
    }

    def __init__(self, auto_type=None, case_design_desc=None, case_name=None, case_num=None, create_time=None, creator_name=None, creator_num=None, deleted=None, expected_results=None, extra_param=None, factor_combination_json=None, operation_and_expected_result=None, id=None, is_archive=None, mindmap_id=None, node_id=None, batch_id=None, branch_id=None, plan_id=None, prerequisite=None, test_case_level=None, test_procedure=None, update_name=None, update_num=None, update_time=None, url=None, uri=None, project_id=None, service_id=None):
        r"""TestCase

        The model defined in huaweicloud sdk

        :param auto_type: 自动化类型
        :type auto_type: str
        :param case_design_desc: 用例设计描述
        :type case_design_desc: str
        :param case_name: 用例名称
        :type case_name: str
        :param case_num: 用例编号
        :type case_num: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param creator_name: 创建人名字
        :type creator_name: str
        :param creator_num: 创建人工号
        :type creator_num: str
        :param deleted: 删除状态
        :type deleted: str
        :param expected_results: 预期结果
        :type expected_results: str
        :param extra_param: 额外模板字段：以json形式存储，前台解析
        :type extra_param: str
        :param factor_combination_json: 因子组合json
        :type factor_combination_json: str
        :param operation_and_expected_result: 操作及预期结果
        :type operation_and_expected_result: str
        :param id: id 主键
        :type id: str
        :param is_archive: 状态
        :type is_archive: bool
        :param mindmap_id: 脑图id
        :type mindmap_id: str
        :param node_id: 节点id
        :type node_id: str
        :param batch_id: 批次id
        :type batch_id: str
        :param branch_id: 分支ID
        :type branch_id: str
        :param plan_id: 计划ID
        :type plan_id: str
        :param prerequisite: 用例前置步骤
        :type prerequisite: str
        :param test_case_level: 测试用例级别
        :type test_case_level: str
        :param test_procedure: 测试步骤
        :type test_procedure: str
        :param update_name: 更新人名字
        :type update_name: str
        :param update_num: 更新人工号
        :type update_num: str
        :param update_time: 更新时间
        :type update_time: datetime
        :param url: url
        :type url: str
        :param uri: uri
        :type uri: str
        :param project_id: 项目id
        :type project_id: str
        :param service_id: 服务id
        :type service_id: str
        """
        
        

        self._auto_type = None
        self._case_design_desc = None
        self._case_name = None
        self._case_num = None
        self._create_time = None
        self._creator_name = None
        self._creator_num = None
        self._deleted = None
        self._expected_results = None
        self._extra_param = None
        self._factor_combination_json = None
        self._operation_and_expected_result = None
        self._id = None
        self._is_archive = None
        self._mindmap_id = None
        self._node_id = None
        self._batch_id = None
        self._branch_id = None
        self._plan_id = None
        self._prerequisite = None
        self._test_case_level = None
        self._test_procedure = None
        self._update_name = None
        self._update_num = None
        self._update_time = None
        self._url = None
        self._uri = None
        self._project_id = None
        self._service_id = None
        self.discriminator = None

        if auto_type is not None:
            self.auto_type = auto_type
        if case_design_desc is not None:
            self.case_design_desc = case_design_desc
        if case_name is not None:
            self.case_name = case_name
        if case_num is not None:
            self.case_num = case_num
        if create_time is not None:
            self.create_time = create_time
        if creator_name is not None:
            self.creator_name = creator_name
        if creator_num is not None:
            self.creator_num = creator_num
        if deleted is not None:
            self.deleted = deleted
        if expected_results is not None:
            self.expected_results = expected_results
        if extra_param is not None:
            self.extra_param = extra_param
        if factor_combination_json is not None:
            self.factor_combination_json = factor_combination_json
        if operation_and_expected_result is not None:
            self.operation_and_expected_result = operation_and_expected_result
        if id is not None:
            self.id = id
        if is_archive is not None:
            self.is_archive = is_archive
        if mindmap_id is not None:
            self.mindmap_id = mindmap_id
        if node_id is not None:
            self.node_id = node_id
        if batch_id is not None:
            self.batch_id = batch_id
        if branch_id is not None:
            self.branch_id = branch_id
        if plan_id is not None:
            self.plan_id = plan_id
        if prerequisite is not None:
            self.prerequisite = prerequisite
        if test_case_level is not None:
            self.test_case_level = test_case_level
        if test_procedure is not None:
            self.test_procedure = test_procedure
        if update_name is not None:
            self.update_name = update_name
        if update_num is not None:
            self.update_num = update_num
        if update_time is not None:
            self.update_time = update_time
        if url is not None:
            self.url = url
        if uri is not None:
            self.uri = uri
        if project_id is not None:
            self.project_id = project_id
        if service_id is not None:
            self.service_id = service_id

    @property
    def auto_type(self):
        r"""Gets the auto_type of this TestCase.

        自动化类型

        :return: The auto_type of this TestCase.
        :rtype: str
        """
        return self._auto_type

    @auto_type.setter
    def auto_type(self, auto_type):
        r"""Sets the auto_type of this TestCase.

        自动化类型

        :param auto_type: The auto_type of this TestCase.
        :type auto_type: str
        """
        self._auto_type = auto_type

    @property
    def case_design_desc(self):
        r"""Gets the case_design_desc of this TestCase.

        用例设计描述

        :return: The case_design_desc of this TestCase.
        :rtype: str
        """
        return self._case_design_desc

    @case_design_desc.setter
    def case_design_desc(self, case_design_desc):
        r"""Sets the case_design_desc of this TestCase.

        用例设计描述

        :param case_design_desc: The case_design_desc of this TestCase.
        :type case_design_desc: str
        """
        self._case_design_desc = case_design_desc

    @property
    def case_name(self):
        r"""Gets the case_name of this TestCase.

        用例名称

        :return: The case_name of this TestCase.
        :rtype: str
        """
        return self._case_name

    @case_name.setter
    def case_name(self, case_name):
        r"""Sets the case_name of this TestCase.

        用例名称

        :param case_name: The case_name of this TestCase.
        :type case_name: str
        """
        self._case_name = case_name

    @property
    def case_num(self):
        r"""Gets the case_num of this TestCase.

        用例编号

        :return: The case_num of this TestCase.
        :rtype: str
        """
        return self._case_num

    @case_num.setter
    def case_num(self, case_num):
        r"""Sets the case_num of this TestCase.

        用例编号

        :param case_num: The case_num of this TestCase.
        :type case_num: str
        """
        self._case_num = case_num

    @property
    def create_time(self):
        r"""Gets the create_time of this TestCase.

        创建时间

        :return: The create_time of this TestCase.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TestCase.

        创建时间

        :param create_time: The create_time of this TestCase.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this TestCase.

        创建人名字

        :return: The creator_name of this TestCase.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this TestCase.

        创建人名字

        :param creator_name: The creator_name of this TestCase.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def creator_num(self):
        r"""Gets the creator_num of this TestCase.

        创建人工号

        :return: The creator_num of this TestCase.
        :rtype: str
        """
        return self._creator_num

    @creator_num.setter
    def creator_num(self, creator_num):
        r"""Sets the creator_num of this TestCase.

        创建人工号

        :param creator_num: The creator_num of this TestCase.
        :type creator_num: str
        """
        self._creator_num = creator_num

    @property
    def deleted(self):
        r"""Gets the deleted of this TestCase.

        删除状态

        :return: The deleted of this TestCase.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this TestCase.

        删除状态

        :param deleted: The deleted of this TestCase.
        :type deleted: str
        """
        self._deleted = deleted

    @property
    def expected_results(self):
        r"""Gets the expected_results of this TestCase.

        预期结果

        :return: The expected_results of this TestCase.
        :rtype: str
        """
        return self._expected_results

    @expected_results.setter
    def expected_results(self, expected_results):
        r"""Sets the expected_results of this TestCase.

        预期结果

        :param expected_results: The expected_results of this TestCase.
        :type expected_results: str
        """
        self._expected_results = expected_results

    @property
    def extra_param(self):
        r"""Gets the extra_param of this TestCase.

        额外模板字段：以json形式存储，前台解析

        :return: The extra_param of this TestCase.
        :rtype: str
        """
        return self._extra_param

    @extra_param.setter
    def extra_param(self, extra_param):
        r"""Sets the extra_param of this TestCase.

        额外模板字段：以json形式存储，前台解析

        :param extra_param: The extra_param of this TestCase.
        :type extra_param: str
        """
        self._extra_param = extra_param

    @property
    def factor_combination_json(self):
        r"""Gets the factor_combination_json of this TestCase.

        因子组合json

        :return: The factor_combination_json of this TestCase.
        :rtype: str
        """
        return self._factor_combination_json

    @factor_combination_json.setter
    def factor_combination_json(self, factor_combination_json):
        r"""Sets the factor_combination_json of this TestCase.

        因子组合json

        :param factor_combination_json: The factor_combination_json of this TestCase.
        :type factor_combination_json: str
        """
        self._factor_combination_json = factor_combination_json

    @property
    def operation_and_expected_result(self):
        r"""Gets the operation_and_expected_result of this TestCase.

        操作及预期结果

        :return: The operation_and_expected_result of this TestCase.
        :rtype: str
        """
        return self._operation_and_expected_result

    @operation_and_expected_result.setter
    def operation_and_expected_result(self, operation_and_expected_result):
        r"""Sets the operation_and_expected_result of this TestCase.

        操作及预期结果

        :param operation_and_expected_result: The operation_and_expected_result of this TestCase.
        :type operation_and_expected_result: str
        """
        self._operation_and_expected_result = operation_and_expected_result

    @property
    def id(self):
        r"""Gets the id of this TestCase.

        id 主键

        :return: The id of this TestCase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TestCase.

        id 主键

        :param id: The id of this TestCase.
        :type id: str
        """
        self._id = id

    @property
    def is_archive(self):
        r"""Gets the is_archive of this TestCase.

        状态

        :return: The is_archive of this TestCase.
        :rtype: bool
        """
        return self._is_archive

    @is_archive.setter
    def is_archive(self, is_archive):
        r"""Sets the is_archive of this TestCase.

        状态

        :param is_archive: The is_archive of this TestCase.
        :type is_archive: bool
        """
        self._is_archive = is_archive

    @property
    def mindmap_id(self):
        r"""Gets the mindmap_id of this TestCase.

        脑图id

        :return: The mindmap_id of this TestCase.
        :rtype: str
        """
        return self._mindmap_id

    @mindmap_id.setter
    def mindmap_id(self, mindmap_id):
        r"""Sets the mindmap_id of this TestCase.

        脑图id

        :param mindmap_id: The mindmap_id of this TestCase.
        :type mindmap_id: str
        """
        self._mindmap_id = mindmap_id

    @property
    def node_id(self):
        r"""Gets the node_id of this TestCase.

        节点id

        :return: The node_id of this TestCase.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this TestCase.

        节点id

        :param node_id: The node_id of this TestCase.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def batch_id(self):
        r"""Gets the batch_id of this TestCase.

        批次id

        :return: The batch_id of this TestCase.
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        r"""Sets the batch_id of this TestCase.

        批次id

        :param batch_id: The batch_id of this TestCase.
        :type batch_id: str
        """
        self._batch_id = batch_id

    @property
    def branch_id(self):
        r"""Gets the branch_id of this TestCase.

        分支ID

        :return: The branch_id of this TestCase.
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        r"""Sets the branch_id of this TestCase.

        分支ID

        :param branch_id: The branch_id of this TestCase.
        :type branch_id: str
        """
        self._branch_id = branch_id

    @property
    def plan_id(self):
        r"""Gets the plan_id of this TestCase.

        计划ID

        :return: The plan_id of this TestCase.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this TestCase.

        计划ID

        :param plan_id: The plan_id of this TestCase.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def prerequisite(self):
        r"""Gets the prerequisite of this TestCase.

        用例前置步骤

        :return: The prerequisite of this TestCase.
        :rtype: str
        """
        return self._prerequisite

    @prerequisite.setter
    def prerequisite(self, prerequisite):
        r"""Sets the prerequisite of this TestCase.

        用例前置步骤

        :param prerequisite: The prerequisite of this TestCase.
        :type prerequisite: str
        """
        self._prerequisite = prerequisite

    @property
    def test_case_level(self):
        r"""Gets the test_case_level of this TestCase.

        测试用例级别

        :return: The test_case_level of this TestCase.
        :rtype: str
        """
        return self._test_case_level

    @test_case_level.setter
    def test_case_level(self, test_case_level):
        r"""Sets the test_case_level of this TestCase.

        测试用例级别

        :param test_case_level: The test_case_level of this TestCase.
        :type test_case_level: str
        """
        self._test_case_level = test_case_level

    @property
    def test_procedure(self):
        r"""Gets the test_procedure of this TestCase.

        测试步骤

        :return: The test_procedure of this TestCase.
        :rtype: str
        """
        return self._test_procedure

    @test_procedure.setter
    def test_procedure(self, test_procedure):
        r"""Sets the test_procedure of this TestCase.

        测试步骤

        :param test_procedure: The test_procedure of this TestCase.
        :type test_procedure: str
        """
        self._test_procedure = test_procedure

    @property
    def update_name(self):
        r"""Gets the update_name of this TestCase.

        更新人名字

        :return: The update_name of this TestCase.
        :rtype: str
        """
        return self._update_name

    @update_name.setter
    def update_name(self, update_name):
        r"""Sets the update_name of this TestCase.

        更新人名字

        :param update_name: The update_name of this TestCase.
        :type update_name: str
        """
        self._update_name = update_name

    @property
    def update_num(self):
        r"""Gets the update_num of this TestCase.

        更新人工号

        :return: The update_num of this TestCase.
        :rtype: str
        """
        return self._update_num

    @update_num.setter
    def update_num(self, update_num):
        r"""Sets the update_num of this TestCase.

        更新人工号

        :param update_num: The update_num of this TestCase.
        :type update_num: str
        """
        self._update_num = update_num

    @property
    def update_time(self):
        r"""Gets the update_time of this TestCase.

        更新时间

        :return: The update_time of this TestCase.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TestCase.

        更新时间

        :param update_time: The update_time of this TestCase.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def url(self):
        r"""Gets the url of this TestCase.

        url

        :return: The url of this TestCase.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this TestCase.

        url

        :param url: The url of this TestCase.
        :type url: str
        """
        self._url = url

    @property
    def uri(self):
        r"""Gets the uri of this TestCase.

        uri

        :return: The uri of this TestCase.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this TestCase.

        uri

        :param uri: The uri of this TestCase.
        :type uri: str
        """
        self._uri = uri

    @property
    def project_id(self):
        r"""Gets the project_id of this TestCase.

        项目id

        :return: The project_id of this TestCase.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TestCase.

        项目id

        :param project_id: The project_id of this TestCase.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def service_id(self):
        r"""Gets the service_id of this TestCase.

        服务id

        :return: The service_id of this TestCase.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this TestCase.

        服务id

        :param service_id: The service_id of this TestCase.
        :type service_id: str
        """
        self._service_id = service_id

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
        if not isinstance(other, TestCase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
