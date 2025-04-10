# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestPlanJournalList:

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
        'plan_id': 'str',
        'operate_time': 'date',
        'operator': 'NameAndId',
        'detail': 'list[TestPlanJournalDetail]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'plan_id': 'plan_id',
        'operate_time': 'operate_time',
        'operator': 'operator',
        'detail': 'detail'
    }

    def __init__(self, project_id=None, plan_id=None, operate_time=None, operator=None, detail=None):
        r"""TestPlanJournalList

        The model defined in huaweicloud sdk

        :param project_id: 项目id，项目唯一标识，固定长度32位字符
        :type project_id: str
        :param plan_id: 测试计划id
        :type plan_id: str
        :param operate_time: 变更时间
        :type operate_time: date
        :param operator: 
        :type operator: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        :param detail: 历史记录详情
        :type detail: list[:class:`huaweicloudsdkcloudtest.v1.TestPlanJournalDetail`]
        """
        
        

        self._project_id = None
        self._plan_id = None
        self._operate_time = None
        self._operator = None
        self._detail = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if plan_id is not None:
            self.plan_id = plan_id
        if operate_time is not None:
            self.operate_time = operate_time
        if operator is not None:
            self.operator = operator
        if detail is not None:
            self.detail = detail

    @property
    def project_id(self):
        r"""Gets the project_id of this TestPlanJournalList.

        项目id，项目唯一标识，固定长度32位字符

        :return: The project_id of this TestPlanJournalList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TestPlanJournalList.

        项目id，项目唯一标识，固定长度32位字符

        :param project_id: The project_id of this TestPlanJournalList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def plan_id(self):
        r"""Gets the plan_id of this TestPlanJournalList.

        测试计划id

        :return: The plan_id of this TestPlanJournalList.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this TestPlanJournalList.

        测试计划id

        :param plan_id: The plan_id of this TestPlanJournalList.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def operate_time(self):
        r"""Gets the operate_time of this TestPlanJournalList.

        变更时间

        :return: The operate_time of this TestPlanJournalList.
        :rtype: date
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        r"""Sets the operate_time of this TestPlanJournalList.

        变更时间

        :param operate_time: The operate_time of this TestPlanJournalList.
        :type operate_time: date
        """
        self._operate_time = operate_time

    @property
    def operator(self):
        r"""Gets the operator of this TestPlanJournalList.

        :return: The operator of this TestPlanJournalList.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this TestPlanJournalList.

        :param operator: The operator of this TestPlanJournalList.
        :type operator: :class:`huaweicloudsdkcloudtest.v1.NameAndId`
        """
        self._operator = operator

    @property
    def detail(self):
        r"""Gets the detail of this TestPlanJournalList.

        历史记录详情

        :return: The detail of this TestPlanJournalList.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestPlanJournalDetail`]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this TestPlanJournalList.

        历史记录详情

        :param detail: The detail of this TestPlanJournalList.
        :type detail: list[:class:`huaweicloudsdkcloudtest.v1.TestPlanJournalDetail`]
        """
        self._detail = detail

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
        if not isinstance(other, TestPlanJournalList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
