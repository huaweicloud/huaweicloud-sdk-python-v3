# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IterationHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iteration_id': 'str',
        'project_id': 'str',
        'operator': 'IterationHistoryOperator',
        'operate': 'str',
        'operate_time': 'str',
        'details': 'list[IterationHistoryDetails]'
    }

    attribute_map = {
        'iteration_id': 'iteration_id',
        'project_id': 'project_id',
        'operator': 'operator',
        'operate': 'operate',
        'operate_time': 'operate_time',
        'details': 'details'
    }

    def __init__(self, iteration_id=None, project_id=None, operator=None, operate=None, operate_time=None, details=None):
        """IterationHistory

        The model defined in huaweicloud sdk

        :param iteration_id: 迭代ID
        :type iteration_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param operator: 
        :type operator: :class:`huaweicloudsdkprojectman.v4.IterationHistoryOperator`
        :param operate: 操作类型
        :type operate: str
        :param operate_time: 操作时间
        :type operate_time: str
        :param details: 操作详情
        :type details: list[:class:`huaweicloudsdkprojectman.v4.IterationHistoryDetails`]
        """
        
        

        self._iteration_id = None
        self._project_id = None
        self._operator = None
        self._operate = None
        self._operate_time = None
        self._details = None
        self.discriminator = None

        if iteration_id is not None:
            self.iteration_id = iteration_id
        if project_id is not None:
            self.project_id = project_id
        if operator is not None:
            self.operator = operator
        if operate is not None:
            self.operate = operate
        if operate_time is not None:
            self.operate_time = operate_time
        if details is not None:
            self.details = details

    @property
    def iteration_id(self):
        """Gets the iteration_id of this IterationHistory.

        迭代ID

        :return: The iteration_id of this IterationHistory.
        :rtype: str
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        """Sets the iteration_id of this IterationHistory.

        迭代ID

        :param iteration_id: The iteration_id of this IterationHistory.
        :type iteration_id: str
        """
        self._iteration_id = iteration_id

    @property
    def project_id(self):
        """Gets the project_id of this IterationHistory.

        项目ID

        :return: The project_id of this IterationHistory.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IterationHistory.

        项目ID

        :param project_id: The project_id of this IterationHistory.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def operator(self):
        """Gets the operator of this IterationHistory.

        :return: The operator of this IterationHistory.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IterationHistoryOperator`
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this IterationHistory.

        :param operator: The operator of this IterationHistory.
        :type operator: :class:`huaweicloudsdkprojectman.v4.IterationHistoryOperator`
        """
        self._operator = operator

    @property
    def operate(self):
        """Gets the operate of this IterationHistory.

        操作类型

        :return: The operate of this IterationHistory.
        :rtype: str
        """
        return self._operate

    @operate.setter
    def operate(self, operate):
        """Sets the operate of this IterationHistory.

        操作类型

        :param operate: The operate of this IterationHistory.
        :type operate: str
        """
        self._operate = operate

    @property
    def operate_time(self):
        """Gets the operate_time of this IterationHistory.

        操作时间

        :return: The operate_time of this IterationHistory.
        :rtype: str
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this IterationHistory.

        操作时间

        :param operate_time: The operate_time of this IterationHistory.
        :type operate_time: str
        """
        self._operate_time = operate_time

    @property
    def details(self):
        """Gets the details of this IterationHistory.

        操作详情

        :return: The details of this IterationHistory.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IterationHistoryDetails`]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this IterationHistory.

        操作详情

        :param details: The details of this IterationHistory.
        :type details: list[:class:`huaweicloudsdkprojectman.v4.IterationHistoryDetails`]
        """
        self._details = details

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
        if not isinstance(other, IterationHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
