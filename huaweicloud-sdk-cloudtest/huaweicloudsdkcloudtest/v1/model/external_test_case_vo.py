# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalTestCaseVo:

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
        'owner': 'NameAndIdVo',
        'status': 'NameAndIdVo',
        'result': 'NameAndIdVo',
        'module': 'NameAndIdVo',
        'iteration': 'NameAndIdVo',
        'id': 'str',
        'number': 'str',
        'description': 'str',
        'rank_id': 'str',
        'project_id': 'str',
        'execution_type': 'NameAndIdVo',
        'test_type': 'IntegerIdAndNameVo',
        'create_info': 'CreateInfoVo',
        'execute_info': 'ExecuteInfoVo',
        'associate_issue_info': 'AssociateIssueInfoVo',
        'associate_defect_info': 'AssociateDefectInfoVo'
    }

    attribute_map = {
        'name': 'name',
        'owner': 'owner',
        'status': 'status',
        'result': 'result',
        'module': 'module',
        'iteration': 'iteration',
        'id': 'id',
        'number': 'number',
        'description': 'description',
        'rank_id': 'rank_id',
        'project_id': 'project_id',
        'execution_type': 'execution_type',
        'test_type': 'test_type',
        'create_info': 'create_info',
        'execute_info': 'execute_info',
        'associate_issue_info': 'associate_issue_info',
        'associate_defect_info': 'associate_defect_info'
    }

    def __init__(self, name=None, owner=None, status=None, result=None, module=None, iteration=None, id=None, number=None, description=None, rank_id=None, project_id=None, execution_type=None, test_type=None, create_info=None, execute_info=None, associate_issue_info=None, associate_defect_info=None):
        """ExternalTestCaseVo

        The model defined in huaweicloud sdk

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
        :param id: 用例ID
        :type id: str
        :param number: 用例编号
        :type number: str
        :param description: 用例描述
        :type description: str
        :param rank_id: 用例等级
        :type rank_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param execution_type: 
        :type execution_type: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
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
        """
        
        

        self._name = None
        self._owner = None
        self._status = None
        self._result = None
        self._module = None
        self._iteration = None
        self._id = None
        self._number = None
        self._description = None
        self._rank_id = None
        self._project_id = None
        self._execution_type = None
        self._test_type = None
        self._create_info = None
        self._execute_info = None
        self._associate_issue_info = None
        self._associate_defect_info = None
        self.discriminator = None

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
        if id is not None:
            self.id = id
        if number is not None:
            self.number = number
        if description is not None:
            self.description = description
        if rank_id is not None:
            self.rank_id = rank_id
        if project_id is not None:
            self.project_id = project_id
        if execution_type is not None:
            self.execution_type = execution_type
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

    @property
    def name(self):
        """Gets the name of this ExternalTestCaseVo.

        用例名称

        :return: The name of this ExternalTestCaseVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalTestCaseVo.

        用例名称

        :param name: The name of this ExternalTestCaseVo.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this ExternalTestCaseVo.

        :return: The owner of this ExternalTestCaseVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ExternalTestCaseVo.

        :param owner: The owner of this ExternalTestCaseVo.
        :type owner: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._owner = owner

    @property
    def status(self):
        """Gets the status of this ExternalTestCaseVo.

        :return: The status of this ExternalTestCaseVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExternalTestCaseVo.

        :param status: The status of this ExternalTestCaseVo.
        :type status: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._status = status

    @property
    def result(self):
        """Gets the result of this ExternalTestCaseVo.

        :return: The result of this ExternalTestCaseVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ExternalTestCaseVo.

        :param result: The result of this ExternalTestCaseVo.
        :type result: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._result = result

    @property
    def module(self):
        """Gets the module of this ExternalTestCaseVo.

        :return: The module of this ExternalTestCaseVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this ExternalTestCaseVo.

        :param module: The module of this ExternalTestCaseVo.
        :type module: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._module = module

    @property
    def iteration(self):
        """Gets the iteration of this ExternalTestCaseVo.

        :return: The iteration of this ExternalTestCaseVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        """Sets the iteration of this ExternalTestCaseVo.

        :param iteration: The iteration of this ExternalTestCaseVo.
        :type iteration: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._iteration = iteration

    @property
    def id(self):
        """Gets the id of this ExternalTestCaseVo.

        用例ID

        :return: The id of this ExternalTestCaseVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalTestCaseVo.

        用例ID

        :param id: The id of this ExternalTestCaseVo.
        :type id: str
        """
        self._id = id

    @property
    def number(self):
        """Gets the number of this ExternalTestCaseVo.

        用例编号

        :return: The number of this ExternalTestCaseVo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ExternalTestCaseVo.

        用例编号

        :param number: The number of this ExternalTestCaseVo.
        :type number: str
        """
        self._number = number

    @property
    def description(self):
        """Gets the description of this ExternalTestCaseVo.

        用例描述

        :return: The description of this ExternalTestCaseVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExternalTestCaseVo.

        用例描述

        :param description: The description of this ExternalTestCaseVo.
        :type description: str
        """
        self._description = description

    @property
    def rank_id(self):
        """Gets the rank_id of this ExternalTestCaseVo.

        用例等级

        :return: The rank_id of this ExternalTestCaseVo.
        :rtype: str
        """
        return self._rank_id

    @rank_id.setter
    def rank_id(self, rank_id):
        """Sets the rank_id of this ExternalTestCaseVo.

        用例等级

        :param rank_id: The rank_id of this ExternalTestCaseVo.
        :type rank_id: str
        """
        self._rank_id = rank_id

    @property
    def project_id(self):
        """Gets the project_id of this ExternalTestCaseVo.

        项目ID

        :return: The project_id of this ExternalTestCaseVo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ExternalTestCaseVo.

        项目ID

        :param project_id: The project_id of this ExternalTestCaseVo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def execution_type(self):
        """Gets the execution_type of this ExternalTestCaseVo.

        :return: The execution_type of this ExternalTestCaseVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._execution_type

    @execution_type.setter
    def execution_type(self, execution_type):
        """Sets the execution_type of this ExternalTestCaseVo.

        :param execution_type: The execution_type of this ExternalTestCaseVo.
        :type execution_type: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._execution_type = execution_type

    @property
    def test_type(self):
        """Gets the test_type of this ExternalTestCaseVo.

        :return: The test_type of this ExternalTestCaseVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.IntegerIdAndNameVo`
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        """Sets the test_type of this ExternalTestCaseVo.

        :param test_type: The test_type of this ExternalTestCaseVo.
        :type test_type: :class:`huaweicloudsdkcloudtest.v1.IntegerIdAndNameVo`
        """
        self._test_type = test_type

    @property
    def create_info(self):
        """Gets the create_info of this ExternalTestCaseVo.

        :return: The create_info of this ExternalTestCaseVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CreateInfoVo`
        """
        return self._create_info

    @create_info.setter
    def create_info(self, create_info):
        """Sets the create_info of this ExternalTestCaseVo.

        :param create_info: The create_info of this ExternalTestCaseVo.
        :type create_info: :class:`huaweicloudsdkcloudtest.v1.CreateInfoVo`
        """
        self._create_info = create_info

    @property
    def execute_info(self):
        """Gets the execute_info of this ExternalTestCaseVo.

        :return: The execute_info of this ExternalTestCaseVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ExecuteInfoVo`
        """
        return self._execute_info

    @execute_info.setter
    def execute_info(self, execute_info):
        """Sets the execute_info of this ExternalTestCaseVo.

        :param execute_info: The execute_info of this ExternalTestCaseVo.
        :type execute_info: :class:`huaweicloudsdkcloudtest.v1.ExecuteInfoVo`
        """
        self._execute_info = execute_info

    @property
    def associate_issue_info(self):
        """Gets the associate_issue_info of this ExternalTestCaseVo.

        :return: The associate_issue_info of this ExternalTestCaseVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AssociateIssueInfoVo`
        """
        return self._associate_issue_info

    @associate_issue_info.setter
    def associate_issue_info(self, associate_issue_info):
        """Sets the associate_issue_info of this ExternalTestCaseVo.

        :param associate_issue_info: The associate_issue_info of this ExternalTestCaseVo.
        :type associate_issue_info: :class:`huaweicloudsdkcloudtest.v1.AssociateIssueInfoVo`
        """
        self._associate_issue_info = associate_issue_info

    @property
    def associate_defect_info(self):
        """Gets the associate_defect_info of this ExternalTestCaseVo.

        :return: The associate_defect_info of this ExternalTestCaseVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AssociateDefectInfoVo`
        """
        return self._associate_defect_info

    @associate_defect_info.setter
    def associate_defect_info(self, associate_defect_info):
        """Sets the associate_defect_info of this ExternalTestCaseVo.

        :param associate_defect_info: The associate_defect_info of this ExternalTestCaseVo.
        :type associate_defect_info: :class:`huaweicloudsdkcloudtest.v1.AssociateDefectInfoVo`
        """
        self._associate_defect_info = associate_defect_info

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
        if not isinstance(other, ExternalTestCaseVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
