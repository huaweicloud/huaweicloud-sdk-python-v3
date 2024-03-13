# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseAwInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aw': 'list[AwInfoDTO]',
        'aw_list': 'list[DetailItem]',
        'case_aw_id': 'str',
        'case_uri': 'str',
        'case_uri_i': 'str',
        'datum_type': 'int',
        'id': 'str',
        'name': 'str',
        'task_exec_id': 'str',
        'task_id': 'str',
        'testcase_id': 'str',
        'transaction_list': 'list[DetailItem]'
    }

    attribute_map = {
        'aw': 'aw',
        'aw_list': 'awList',
        'case_aw_id': 'caseAwId',
        'case_uri': 'caseUri',
        'case_uri_i': 'case_uri_i',
        'datum_type': 'datumType',
        'id': 'id',
        'name': 'name',
        'task_exec_id': 'taskExecId',
        'task_id': 'taskId',
        'testcase_id': 'testcaseId',
        'transaction_list': 'transactionList'
    }

    def __init__(self, aw=None, aw_list=None, case_aw_id=None, case_uri=None, case_uri_i=None, datum_type=None, id=None, name=None, task_exec_id=None, task_id=None, testcase_id=None, transaction_list=None):
        """CaseAwInfo

        The model defined in huaweicloud sdk

        :param aw: aw信息
        :type aw: list[:class:`huaweicloudsdkcpts.v1.AwInfoDTO`]
        :param aw_list: aw详细信息列表
        :type aw_list: list[:class:`huaweicloudsdkcpts.v1.DetailItem`]
        :param case_aw_id: 数据库中dc_case_aw表中的主键ID
        :type case_aw_id: str
        :param case_uri: 数据库中dc_testcase表中的case_uri
        :type case_uri: str
        :param case_uri_i: 数据库中dc_testcase表中的case_uri_iteration
        :type case_uri_i: str
        :param datum_type: 数据类型（用例/aw/事务）
        :type datum_type: int
        :param id: 数据库中dc_case_aw表中的主键ID
        :type id: str
        :param name: 用例名
        :type name: str
        :param task_exec_id: 数据库中dc_testcase表中的testcase_id
        :type task_exec_id: str
        :param task_id: 任务ID
        :type task_id: str
        :param testcase_id: 数据库中dc_testcase表中的testcase_id
        :type testcase_id: str
        :param transaction_list: 事务详细信息列表
        :type transaction_list: list[:class:`huaweicloudsdkcpts.v1.DetailItem`]
        """
        
        

        self._aw = None
        self._aw_list = None
        self._case_aw_id = None
        self._case_uri = None
        self._case_uri_i = None
        self._datum_type = None
        self._id = None
        self._name = None
        self._task_exec_id = None
        self._task_id = None
        self._testcase_id = None
        self._transaction_list = None
        self.discriminator = None

        if aw is not None:
            self.aw = aw
        if aw_list is not None:
            self.aw_list = aw_list
        if case_aw_id is not None:
            self.case_aw_id = case_aw_id
        if case_uri is not None:
            self.case_uri = case_uri
        if case_uri_i is not None:
            self.case_uri_i = case_uri_i
        if datum_type is not None:
            self.datum_type = datum_type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if task_exec_id is not None:
            self.task_exec_id = task_exec_id
        if task_id is not None:
            self.task_id = task_id
        if testcase_id is not None:
            self.testcase_id = testcase_id
        if transaction_list is not None:
            self.transaction_list = transaction_list

    @property
    def aw(self):
        """Gets the aw of this CaseAwInfo.

        aw信息

        :return: The aw of this CaseAwInfo.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.AwInfoDTO`]
        """
        return self._aw

    @aw.setter
    def aw(self, aw):
        """Sets the aw of this CaseAwInfo.

        aw信息

        :param aw: The aw of this CaseAwInfo.
        :type aw: list[:class:`huaweicloudsdkcpts.v1.AwInfoDTO`]
        """
        self._aw = aw

    @property
    def aw_list(self):
        """Gets the aw_list of this CaseAwInfo.

        aw详细信息列表

        :return: The aw_list of this CaseAwInfo.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.DetailItem`]
        """
        return self._aw_list

    @aw_list.setter
    def aw_list(self, aw_list):
        """Sets the aw_list of this CaseAwInfo.

        aw详细信息列表

        :param aw_list: The aw_list of this CaseAwInfo.
        :type aw_list: list[:class:`huaweicloudsdkcpts.v1.DetailItem`]
        """
        self._aw_list = aw_list

    @property
    def case_aw_id(self):
        """Gets the case_aw_id of this CaseAwInfo.

        数据库中dc_case_aw表中的主键ID

        :return: The case_aw_id of this CaseAwInfo.
        :rtype: str
        """
        return self._case_aw_id

    @case_aw_id.setter
    def case_aw_id(self, case_aw_id):
        """Sets the case_aw_id of this CaseAwInfo.

        数据库中dc_case_aw表中的主键ID

        :param case_aw_id: The case_aw_id of this CaseAwInfo.
        :type case_aw_id: str
        """
        self._case_aw_id = case_aw_id

    @property
    def case_uri(self):
        """Gets the case_uri of this CaseAwInfo.

        数据库中dc_testcase表中的case_uri

        :return: The case_uri of this CaseAwInfo.
        :rtype: str
        """
        return self._case_uri

    @case_uri.setter
    def case_uri(self, case_uri):
        """Sets the case_uri of this CaseAwInfo.

        数据库中dc_testcase表中的case_uri

        :param case_uri: The case_uri of this CaseAwInfo.
        :type case_uri: str
        """
        self._case_uri = case_uri

    @property
    def case_uri_i(self):
        """Gets the case_uri_i of this CaseAwInfo.

        数据库中dc_testcase表中的case_uri_iteration

        :return: The case_uri_i of this CaseAwInfo.
        :rtype: str
        """
        return self._case_uri_i

    @case_uri_i.setter
    def case_uri_i(self, case_uri_i):
        """Sets the case_uri_i of this CaseAwInfo.

        数据库中dc_testcase表中的case_uri_iteration

        :param case_uri_i: The case_uri_i of this CaseAwInfo.
        :type case_uri_i: str
        """
        self._case_uri_i = case_uri_i

    @property
    def datum_type(self):
        """Gets the datum_type of this CaseAwInfo.

        数据类型（用例/aw/事务）

        :return: The datum_type of this CaseAwInfo.
        :rtype: int
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type):
        """Sets the datum_type of this CaseAwInfo.

        数据类型（用例/aw/事务）

        :param datum_type: The datum_type of this CaseAwInfo.
        :type datum_type: int
        """
        self._datum_type = datum_type

    @property
    def id(self):
        """Gets the id of this CaseAwInfo.

        数据库中dc_case_aw表中的主键ID

        :return: The id of this CaseAwInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CaseAwInfo.

        数据库中dc_case_aw表中的主键ID

        :param id: The id of this CaseAwInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CaseAwInfo.

        用例名

        :return: The name of this CaseAwInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CaseAwInfo.

        用例名

        :param name: The name of this CaseAwInfo.
        :type name: str
        """
        self._name = name

    @property
    def task_exec_id(self):
        """Gets the task_exec_id of this CaseAwInfo.

        数据库中dc_testcase表中的testcase_id

        :return: The task_exec_id of this CaseAwInfo.
        :rtype: str
        """
        return self._task_exec_id

    @task_exec_id.setter
    def task_exec_id(self, task_exec_id):
        """Sets the task_exec_id of this CaseAwInfo.

        数据库中dc_testcase表中的testcase_id

        :param task_exec_id: The task_exec_id of this CaseAwInfo.
        :type task_exec_id: str
        """
        self._task_exec_id = task_exec_id

    @property
    def task_id(self):
        """Gets the task_id of this CaseAwInfo.

        任务ID

        :return: The task_id of this CaseAwInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CaseAwInfo.

        任务ID

        :param task_id: The task_id of this CaseAwInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def testcase_id(self):
        """Gets the testcase_id of this CaseAwInfo.

        数据库中dc_testcase表中的testcase_id

        :return: The testcase_id of this CaseAwInfo.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        """Sets the testcase_id of this CaseAwInfo.

        数据库中dc_testcase表中的testcase_id

        :param testcase_id: The testcase_id of this CaseAwInfo.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    @property
    def transaction_list(self):
        """Gets the transaction_list of this CaseAwInfo.

        事务详细信息列表

        :return: The transaction_list of this CaseAwInfo.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.DetailItem`]
        """
        return self._transaction_list

    @transaction_list.setter
    def transaction_list(self, transaction_list):
        """Sets the transaction_list of this CaseAwInfo.

        事务详细信息列表

        :param transaction_list: The transaction_list of this CaseAwInfo.
        :type transaction_list: list[:class:`huaweicloudsdkcpts.v1.DetailItem`]
        """
        self._transaction_list = transaction_list

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
        if not isinstance(other, CaseAwInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
