# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosisTaskNodeDetail:

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
        'code': 'str',
        'name': 'str',
        'name_zh': 'str',
        'diagnosis_task_id': 'str',
        'status': 'str',
        'diagnosis_record_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'name_zh': 'name_zh',
        'diagnosis_task_id': 'diagnosis_task_id',
        'status': 'status',
        'diagnosis_record_id': 'diagnosis_record_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'message': 'message'
    }

    def __init__(self, id=None, code=None, name=None, name_zh=None, diagnosis_task_id=None, status=None, diagnosis_record_id=None, start_time=None, end_time=None, message=None):
        r"""DiagnosisTaskNodeDetail

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param code: code
        :type code: str
        :param name: 诊断步骤名称
        :type name: str
        :param name_zh: 诊断步骤名称(中文)
        :type name_zh: str
        :param diagnosis_task_id: 诊断任务ID
        :type diagnosis_task_id: str
        :param status: 任务状态，waiting,executing,failed,finish,cancel
        :type status: str
        :param diagnosis_record_id: 诊断步骤主键ID
        :type diagnosis_record_id: str
        :param start_time: 诊断步骤开始时间
        :type start_time: str
        :param end_time: 诊断步骤结束时间
        :type end_time: str
        :param message: 诊断步骤执行结果
        :type message: str
        """
        
        

        self._id = None
        self._code = None
        self._name = None
        self._name_zh = None
        self._diagnosis_task_id = None
        self._status = None
        self._diagnosis_record_id = None
        self._start_time = None
        self._end_time = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if name_zh is not None:
            self.name_zh = name_zh
        if diagnosis_task_id is not None:
            self.diagnosis_task_id = diagnosis_task_id
        if status is not None:
            self.status = status
        if diagnosis_record_id is not None:
            self.diagnosis_record_id = diagnosis_record_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if message is not None:
            self.message = message

    @property
    def id(self):
        r"""Gets the id of this DiagnosisTaskNodeDetail.

        id

        :return: The id of this DiagnosisTaskNodeDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DiagnosisTaskNodeDetail.

        id

        :param id: The id of this DiagnosisTaskNodeDetail.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        r"""Gets the code of this DiagnosisTaskNodeDetail.

        code

        :return: The code of this DiagnosisTaskNodeDetail.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this DiagnosisTaskNodeDetail.

        code

        :param code: The code of this DiagnosisTaskNodeDetail.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        r"""Gets the name of this DiagnosisTaskNodeDetail.

        诊断步骤名称

        :return: The name of this DiagnosisTaskNodeDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DiagnosisTaskNodeDetail.

        诊断步骤名称

        :param name: The name of this DiagnosisTaskNodeDetail.
        :type name: str
        """
        self._name = name

    @property
    def name_zh(self):
        r"""Gets the name_zh of this DiagnosisTaskNodeDetail.

        诊断步骤名称(中文)

        :return: The name_zh of this DiagnosisTaskNodeDetail.
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        r"""Sets the name_zh of this DiagnosisTaskNodeDetail.

        诊断步骤名称(中文)

        :param name_zh: The name_zh of this DiagnosisTaskNodeDetail.
        :type name_zh: str
        """
        self._name_zh = name_zh

    @property
    def diagnosis_task_id(self):
        r"""Gets the diagnosis_task_id of this DiagnosisTaskNodeDetail.

        诊断任务ID

        :return: The diagnosis_task_id of this DiagnosisTaskNodeDetail.
        :rtype: str
        """
        return self._diagnosis_task_id

    @diagnosis_task_id.setter
    def diagnosis_task_id(self, diagnosis_task_id):
        r"""Sets the diagnosis_task_id of this DiagnosisTaskNodeDetail.

        诊断任务ID

        :param diagnosis_task_id: The diagnosis_task_id of this DiagnosisTaskNodeDetail.
        :type diagnosis_task_id: str
        """
        self._diagnosis_task_id = diagnosis_task_id

    @property
    def status(self):
        r"""Gets the status of this DiagnosisTaskNodeDetail.

        任务状态，waiting,executing,failed,finish,cancel

        :return: The status of this DiagnosisTaskNodeDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DiagnosisTaskNodeDetail.

        任务状态，waiting,executing,failed,finish,cancel

        :param status: The status of this DiagnosisTaskNodeDetail.
        :type status: str
        """
        self._status = status

    @property
    def diagnosis_record_id(self):
        r"""Gets the diagnosis_record_id of this DiagnosisTaskNodeDetail.

        诊断步骤主键ID

        :return: The diagnosis_record_id of this DiagnosisTaskNodeDetail.
        :rtype: str
        """
        return self._diagnosis_record_id

    @diagnosis_record_id.setter
    def diagnosis_record_id(self, diagnosis_record_id):
        r"""Sets the diagnosis_record_id of this DiagnosisTaskNodeDetail.

        诊断步骤主键ID

        :param diagnosis_record_id: The diagnosis_record_id of this DiagnosisTaskNodeDetail.
        :type diagnosis_record_id: str
        """
        self._diagnosis_record_id = diagnosis_record_id

    @property
    def start_time(self):
        r"""Gets the start_time of this DiagnosisTaskNodeDetail.

        诊断步骤开始时间

        :return: The start_time of this DiagnosisTaskNodeDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DiagnosisTaskNodeDetail.

        诊断步骤开始时间

        :param start_time: The start_time of this DiagnosisTaskNodeDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this DiagnosisTaskNodeDetail.

        诊断步骤结束时间

        :return: The end_time of this DiagnosisTaskNodeDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this DiagnosisTaskNodeDetail.

        诊断步骤结束时间

        :param end_time: The end_time of this DiagnosisTaskNodeDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def message(self):
        r"""Gets the message of this DiagnosisTaskNodeDetail.

        诊断步骤执行结果

        :return: The message of this DiagnosisTaskNodeDetail.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this DiagnosisTaskNodeDetail.

        诊断步骤执行结果

        :param message: The message of this DiagnosisTaskNodeDetail.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, DiagnosisTaskNodeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
