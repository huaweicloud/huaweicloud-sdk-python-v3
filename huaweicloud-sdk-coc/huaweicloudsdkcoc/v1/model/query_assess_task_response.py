# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAssessTaskResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'application_name': 'str',
        'application_id': 'str',
        'status': 'str',
        'reason': 'str',
        'progress': 'int',
        'score': 'float',
        'assess_report_id': 'str',
        'create_time': 'int',
        'last_assess_time': 'int',
        'last_update_time': 'int',
        'creator': 'str',
        'creator_name': 'str',
        'operator': 'str',
        'operator_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'application_name': 'application_name',
        'application_id': 'application_id',
        'status': 'status',
        'reason': 'reason',
        'progress': 'progress',
        'score': 'score',
        'assess_report_id': 'assess_report_id',
        'create_time': 'create_time',
        'last_assess_time': 'last_assess_time',
        'last_update_time': 'last_update_time',
        'creator': 'creator',
        'creator_name': 'creator_name',
        'operator': 'operator',
        'operator_name': 'operator_name'
    }

    def __init__(self, id=None, application_name=None, application_id=None, status=None, reason=None, progress=None, score=None, assess_report_id=None, create_time=None, last_assess_time=None, last_update_time=None, creator=None, creator_name=None, operator=None, operator_name=None):
        r"""QueryAssessTaskResponse

        The model defined in huaweicloud sdk

        :param id: 唯一标识ID
        :type id: str
        :param application_name: 应用名称
        :type application_name: str
        :param application_id: 应用ID
        :type application_id: str
        :param status: 评估任务状态.  no_assessment 未评估 assess_finish 评估完成 assess_failed 评估失败 assessing     评估中
        :type status: str
        :param reason: 失败原因
        :type reason: str
        :param progress: 评估进度
        :type progress: int
        :param score: 
        :type score: float
        :param assess_report_id: 评估报告编号ID
        :type assess_report_id: str
        :param create_time: 创建时间
        :type create_time: int
        :param last_assess_time: 最新评估时间
        :type last_assess_time: int
        :param last_update_time: 最新更新时间
        :type last_update_time: int
        :param creator: 创建人ID
        :type creator: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param operator: 操作人ID
        :type operator: str
        :param operator_name: 操作人名称
        :type operator_name: str
        """
        
        

        self._id = None
        self._application_name = None
        self._application_id = None
        self._status = None
        self._reason = None
        self._progress = None
        self._score = None
        self._assess_report_id = None
        self._create_time = None
        self._last_assess_time = None
        self._last_update_time = None
        self._creator = None
        self._creator_name = None
        self._operator = None
        self._operator_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if application_name is not None:
            self.application_name = application_name
        if application_id is not None:
            self.application_id = application_id
        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if progress is not None:
            self.progress = progress
        if score is not None:
            self.score = score
        if assess_report_id is not None:
            self.assess_report_id = assess_report_id
        if create_time is not None:
            self.create_time = create_time
        if last_assess_time is not None:
            self.last_assess_time = last_assess_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if creator is not None:
            self.creator = creator
        if creator_name is not None:
            self.creator_name = creator_name
        if operator is not None:
            self.operator = operator
        if operator_name is not None:
            self.operator_name = operator_name

    @property
    def id(self):
        r"""Gets the id of this QueryAssessTaskResponse.

        唯一标识ID

        :return: The id of this QueryAssessTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QueryAssessTaskResponse.

        唯一标识ID

        :param id: The id of this QueryAssessTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def application_name(self):
        r"""Gets the application_name of this QueryAssessTaskResponse.

        应用名称

        :return: The application_name of this QueryAssessTaskResponse.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this QueryAssessTaskResponse.

        应用名称

        :param application_name: The application_name of this QueryAssessTaskResponse.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def application_id(self):
        r"""Gets the application_id of this QueryAssessTaskResponse.

        应用ID

        :return: The application_id of this QueryAssessTaskResponse.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this QueryAssessTaskResponse.

        应用ID

        :param application_id: The application_id of this QueryAssessTaskResponse.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def status(self):
        r"""Gets the status of this QueryAssessTaskResponse.

        评估任务状态.  no_assessment 未评估 assess_finish 评估完成 assess_failed 评估失败 assessing     评估中

        :return: The status of this QueryAssessTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryAssessTaskResponse.

        评估任务状态.  no_assessment 未评估 assess_finish 评估完成 assess_failed 评估失败 assessing     评估中

        :param status: The status of this QueryAssessTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        r"""Gets the reason of this QueryAssessTaskResponse.

        失败原因

        :return: The reason of this QueryAssessTaskResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this QueryAssessTaskResponse.

        失败原因

        :param reason: The reason of this QueryAssessTaskResponse.
        :type reason: str
        """
        self._reason = reason

    @property
    def progress(self):
        r"""Gets the progress of this QueryAssessTaskResponse.

        评估进度

        :return: The progress of this QueryAssessTaskResponse.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this QueryAssessTaskResponse.

        评估进度

        :param progress: The progress of this QueryAssessTaskResponse.
        :type progress: int
        """
        self._progress = progress

    @property
    def score(self):
        r"""Gets the score of this QueryAssessTaskResponse.

        :return: The score of this QueryAssessTaskResponse.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this QueryAssessTaskResponse.

        :param score: The score of this QueryAssessTaskResponse.
        :type score: float
        """
        self._score = score

    @property
    def assess_report_id(self):
        r"""Gets the assess_report_id of this QueryAssessTaskResponse.

        评估报告编号ID

        :return: The assess_report_id of this QueryAssessTaskResponse.
        :rtype: str
        """
        return self._assess_report_id

    @assess_report_id.setter
    def assess_report_id(self, assess_report_id):
        r"""Sets the assess_report_id of this QueryAssessTaskResponse.

        评估报告编号ID

        :param assess_report_id: The assess_report_id of this QueryAssessTaskResponse.
        :type assess_report_id: str
        """
        self._assess_report_id = assess_report_id

    @property
    def create_time(self):
        r"""Gets the create_time of this QueryAssessTaskResponse.

        创建时间

        :return: The create_time of this QueryAssessTaskResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this QueryAssessTaskResponse.

        创建时间

        :param create_time: The create_time of this QueryAssessTaskResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_assess_time(self):
        r"""Gets the last_assess_time of this QueryAssessTaskResponse.

        最新评估时间

        :return: The last_assess_time of this QueryAssessTaskResponse.
        :rtype: int
        """
        return self._last_assess_time

    @last_assess_time.setter
    def last_assess_time(self, last_assess_time):
        r"""Sets the last_assess_time of this QueryAssessTaskResponse.

        最新评估时间

        :param last_assess_time: The last_assess_time of this QueryAssessTaskResponse.
        :type last_assess_time: int
        """
        self._last_assess_time = last_assess_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this QueryAssessTaskResponse.

        最新更新时间

        :return: The last_update_time of this QueryAssessTaskResponse.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this QueryAssessTaskResponse.

        最新更新时间

        :param last_update_time: The last_update_time of this QueryAssessTaskResponse.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def creator(self):
        r"""Gets the creator of this QueryAssessTaskResponse.

        创建人ID

        :return: The creator of this QueryAssessTaskResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this QueryAssessTaskResponse.

        创建人ID

        :param creator: The creator of this QueryAssessTaskResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def creator_name(self):
        r"""Gets the creator_name of this QueryAssessTaskResponse.

        创建人名称

        :return: The creator_name of this QueryAssessTaskResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this QueryAssessTaskResponse.

        创建人名称

        :param creator_name: The creator_name of this QueryAssessTaskResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def operator(self):
        r"""Gets the operator of this QueryAssessTaskResponse.

        操作人ID

        :return: The operator of this QueryAssessTaskResponse.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this QueryAssessTaskResponse.

        操作人ID

        :param operator: The operator of this QueryAssessTaskResponse.
        :type operator: str
        """
        self._operator = operator

    @property
    def operator_name(self):
        r"""Gets the operator_name of this QueryAssessTaskResponse.

        操作人名称

        :return: The operator_name of this QueryAssessTaskResponse.
        :rtype: str
        """
        return self._operator_name

    @operator_name.setter
    def operator_name(self, operator_name):
        r"""Sets the operator_name of this QueryAssessTaskResponse.

        操作人名称

        :param operator_name: The operator_name of this QueryAssessTaskResponse.
        :type operator_name: str
        """
        self._operator_name = operator_name

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
        if not isinstance(other, QueryAssessTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
