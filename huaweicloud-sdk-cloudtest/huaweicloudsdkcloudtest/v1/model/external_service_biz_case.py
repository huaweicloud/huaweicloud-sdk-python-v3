# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalServiceBizCase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'preparation': 'str',
        'steps': 'list[ExternalServiceCaseStep]',
        'label_list': 'list[str]',
        'module_id': 'str',
        'test_version_id': 'str',
        'fix_version_id': 'str',
        'assigned_id': 'str',
        'issue_id': 'str',
        'status_id': 'str',
        'defect_id_list': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'preparation': 'preparation',
        'steps': 'steps',
        'label_list': 'label_list',
        'module_id': 'module_id',
        'test_version_id': 'test_version_id',
        'fix_version_id': 'fix_version_id',
        'assigned_id': 'assigned_id',
        'issue_id': 'issue_id',
        'status_id': 'status_id',
        'defect_id_list': 'defect_id_list'
    }

    def __init__(self, description=None, preparation=None, steps=None, label_list=None, module_id=None, test_version_id=None, fix_version_id=None, assigned_id=None, issue_id=None, status_id=None, defect_id_list=None):
        """ExternalServiceBizCase

        The model defined in huaweicloud sdk

        :param description: 测试用例描述信息，长度为[0-500]位字符
        :type description: str
        :param preparation: 执行该测试用例时需要满足的前置条件，长度为[0-500]位字符
        :type preparation: str
        :param steps: 测试步骤，数组长度小于10
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.ExternalServiceCaseStep`]
        :param label_list: 标签名称列表，数组长度小于25
        :type label_list: list[str]
        :param module_id: 模块号，长度为[0-32]位字符
        :type module_id: str
        :param test_version_id: 测试版本号，长度为[0-10]位字符
        :type test_version_id: str
        :param fix_version_id: 迭代号，长度为[0-32]位字符
        :type fix_version_id: str
        :param assigned_id: 处理者id信息，固定长度32位字符
        :type assigned_id: str
        :param issue_id: 用例关联的需求id信息，长度为[0-32]位字符
        :type issue_id: str
        :param status_id: 测试用例状态信息，（0-新建，5-设计中，6-测试中，7-完成）
        :type status_id: str
        :param defect_id_list: 缺陷id信息，数组长度小于50个
        :type defect_id_list: list[str]
        """
        
        

        self._description = None
        self._preparation = None
        self._steps = None
        self._label_list = None
        self._module_id = None
        self._test_version_id = None
        self._fix_version_id = None
        self._assigned_id = None
        self._issue_id = None
        self._status_id = None
        self._defect_id_list = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if preparation is not None:
            self.preparation = preparation
        if steps is not None:
            self.steps = steps
        if label_list is not None:
            self.label_list = label_list
        if module_id is not None:
            self.module_id = module_id
        if test_version_id is not None:
            self.test_version_id = test_version_id
        if fix_version_id is not None:
            self.fix_version_id = fix_version_id
        if assigned_id is not None:
            self.assigned_id = assigned_id
        if issue_id is not None:
            self.issue_id = issue_id
        if status_id is not None:
            self.status_id = status_id
        if defect_id_list is not None:
            self.defect_id_list = defect_id_list

    @property
    def description(self):
        """Gets the description of this ExternalServiceBizCase.

        测试用例描述信息，长度为[0-500]位字符

        :return: The description of this ExternalServiceBizCase.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExternalServiceBizCase.

        测试用例描述信息，长度为[0-500]位字符

        :param description: The description of this ExternalServiceBizCase.
        :type description: str
        """
        self._description = description

    @property
    def preparation(self):
        """Gets the preparation of this ExternalServiceBizCase.

        执行该测试用例时需要满足的前置条件，长度为[0-500]位字符

        :return: The preparation of this ExternalServiceBizCase.
        :rtype: str
        """
        return self._preparation

    @preparation.setter
    def preparation(self, preparation):
        """Sets the preparation of this ExternalServiceBizCase.

        执行该测试用例时需要满足的前置条件，长度为[0-500]位字符

        :param preparation: The preparation of this ExternalServiceBizCase.
        :type preparation: str
        """
        self._preparation = preparation

    @property
    def steps(self):
        """Gets the steps of this ExternalServiceBizCase.

        测试步骤，数组长度小于10

        :return: The steps of this ExternalServiceBizCase.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ExternalServiceCaseStep`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this ExternalServiceBizCase.

        测试步骤，数组长度小于10

        :param steps: The steps of this ExternalServiceBizCase.
        :type steps: list[:class:`huaweicloudsdkcloudtest.v1.ExternalServiceCaseStep`]
        """
        self._steps = steps

    @property
    def label_list(self):
        """Gets the label_list of this ExternalServiceBizCase.

        标签名称列表，数组长度小于25

        :return: The label_list of this ExternalServiceBizCase.
        :rtype: list[str]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        """Sets the label_list of this ExternalServiceBizCase.

        标签名称列表，数组长度小于25

        :param label_list: The label_list of this ExternalServiceBizCase.
        :type label_list: list[str]
        """
        self._label_list = label_list

    @property
    def module_id(self):
        """Gets the module_id of this ExternalServiceBizCase.

        模块号，长度为[0-32]位字符

        :return: The module_id of this ExternalServiceBizCase.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this ExternalServiceBizCase.

        模块号，长度为[0-32]位字符

        :param module_id: The module_id of this ExternalServiceBizCase.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def test_version_id(self):
        """Gets the test_version_id of this ExternalServiceBizCase.

        测试版本号，长度为[0-10]位字符

        :return: The test_version_id of this ExternalServiceBizCase.
        :rtype: str
        """
        return self._test_version_id

    @test_version_id.setter
    def test_version_id(self, test_version_id):
        """Sets the test_version_id of this ExternalServiceBizCase.

        测试版本号，长度为[0-10]位字符

        :param test_version_id: The test_version_id of this ExternalServiceBizCase.
        :type test_version_id: str
        """
        self._test_version_id = test_version_id

    @property
    def fix_version_id(self):
        """Gets the fix_version_id of this ExternalServiceBizCase.

        迭代号，长度为[0-32]位字符

        :return: The fix_version_id of this ExternalServiceBizCase.
        :rtype: str
        """
        return self._fix_version_id

    @fix_version_id.setter
    def fix_version_id(self, fix_version_id):
        """Sets the fix_version_id of this ExternalServiceBizCase.

        迭代号，长度为[0-32]位字符

        :param fix_version_id: The fix_version_id of this ExternalServiceBizCase.
        :type fix_version_id: str
        """
        self._fix_version_id = fix_version_id

    @property
    def assigned_id(self):
        """Gets the assigned_id of this ExternalServiceBizCase.

        处理者id信息，固定长度32位字符

        :return: The assigned_id of this ExternalServiceBizCase.
        :rtype: str
        """
        return self._assigned_id

    @assigned_id.setter
    def assigned_id(self, assigned_id):
        """Sets the assigned_id of this ExternalServiceBizCase.

        处理者id信息，固定长度32位字符

        :param assigned_id: The assigned_id of this ExternalServiceBizCase.
        :type assigned_id: str
        """
        self._assigned_id = assigned_id

    @property
    def issue_id(self):
        """Gets the issue_id of this ExternalServiceBizCase.

        用例关联的需求id信息，长度为[0-32]位字符

        :return: The issue_id of this ExternalServiceBizCase.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this ExternalServiceBizCase.

        用例关联的需求id信息，长度为[0-32]位字符

        :param issue_id: The issue_id of this ExternalServiceBizCase.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def status_id(self):
        """Gets the status_id of this ExternalServiceBizCase.

        测试用例状态信息，（0-新建，5-设计中，6-测试中，7-完成）

        :return: The status_id of this ExternalServiceBizCase.
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this ExternalServiceBizCase.

        测试用例状态信息，（0-新建，5-设计中，6-测试中，7-完成）

        :param status_id: The status_id of this ExternalServiceBizCase.
        :type status_id: str
        """
        self._status_id = status_id

    @property
    def defect_id_list(self):
        """Gets the defect_id_list of this ExternalServiceBizCase.

        缺陷id信息，数组长度小于50个

        :return: The defect_id_list of this ExternalServiceBizCase.
        :rtype: list[str]
        """
        return self._defect_id_list

    @defect_id_list.setter
    def defect_id_list(self, defect_id_list):
        """Sets the defect_id_list of this ExternalServiceBizCase.

        缺陷id信息，数组长度小于50个

        :param defect_id_list: The defect_id_list of this ExternalServiceBizCase.
        :type defect_id_list: list[str]
        """
        self._defect_id_list = defect_id_list

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
        if not isinstance(other, ExternalServiceBizCase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
