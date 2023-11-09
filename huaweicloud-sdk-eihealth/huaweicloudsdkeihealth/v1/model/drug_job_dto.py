# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DrugJobDto:

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
        'name': 'str',
        'labels': 'list[str]',
        'status': 'str',
        'type': 'str',
        'create_time': 'str',
        'finish_time': 'str',
        'start_time': 'str',
        'failed_message': 'str',
        'user_name': 'str',
        'output_dir': 'str',
        'expect_charge_num': 'int',
        'real_charge_num': 'int',
        'progress': 'Progress'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'labels': 'labels',
        'status': 'status',
        'type': 'type',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'start_time': 'start_time',
        'failed_message': 'failed_message',
        'user_name': 'user_name',
        'output_dir': 'output_dir',
        'expect_charge_num': 'expect_charge_num',
        'real_charge_num': 'real_charge_num',
        'progress': 'progress'
    }

    def __init__(self, id=None, name=None, labels=None, status=None, type=None, create_time=None, finish_time=None, start_time=None, failed_message=None, user_name=None, output_dir=None, expect_charge_num=None, real_charge_num=None, progress=None):
        """DrugJobDto

        The model defined in huaweicloud sdk

        :param id: 作业id
        :type id: str
        :param name: 作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)
        :type name: str
        :param labels: 作业标签
        :type labels: list[str]
        :param status: 作业状态
        :type status: str
        :param type: 作业类型
        :type type: str
        :param create_time: 作业创建时间
        :type create_time: str
        :param finish_time: 作业结束时间
        :type finish_time: str
        :param start_time: 作业结束时间
        :type start_time: str
        :param failed_message: 失败提示，当作业执行失败时会返回
        :type failed_message: str
        :param user_name: 创建任务的用户名称
        :type user_name: str
        :param output_dir: 作业结果输出目录
        :type output_dir: str
        :param expect_charge_num: 预估功能调用消耗次数
        :type expect_charge_num: int
        :param real_charge_num: 实际功能调用消耗次数
        :type real_charge_num: int
        :param progress: 
        :type progress: :class:`huaweicloudsdkeihealth.v1.Progress`
        """
        
        

        self._id = None
        self._name = None
        self._labels = None
        self._status = None
        self._type = None
        self._create_time = None
        self._finish_time = None
        self._start_time = None
        self._failed_message = None
        self._user_name = None
        self._output_dir = None
        self._expect_charge_num = None
        self._real_charge_num = None
        self._progress = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if labels is not None:
            self.labels = labels
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if start_time is not None:
            self.start_time = start_time
        if failed_message is not None:
            self.failed_message = failed_message
        if user_name is not None:
            self.user_name = user_name
        if output_dir is not None:
            self.output_dir = output_dir
        if expect_charge_num is not None:
            self.expect_charge_num = expect_charge_num
        if real_charge_num is not None:
            self.real_charge_num = real_charge_num
        if progress is not None:
            self.progress = progress

    @property
    def id(self):
        """Gets the id of this DrugJobDto.

        作业id

        :return: The id of this DrugJobDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DrugJobDto.

        作业id

        :param id: The id of this DrugJobDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DrugJobDto.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :return: The name of this DrugJobDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DrugJobDto.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :param name: The name of this DrugJobDto.
        :type name: str
        """
        self._name = name

    @property
    def labels(self):
        """Gets the labels of this DrugJobDto.

        作业标签

        :return: The labels of this DrugJobDto.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DrugJobDto.

        作业标签

        :param labels: The labels of this DrugJobDto.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def status(self):
        """Gets the status of this DrugJobDto.

        作业状态

        :return: The status of this DrugJobDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DrugJobDto.

        作业状态

        :param status: The status of this DrugJobDto.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this DrugJobDto.

        作业类型

        :return: The type of this DrugJobDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DrugJobDto.

        作业类型

        :param type: The type of this DrugJobDto.
        :type type: str
        """
        self._type = type

    @property
    def create_time(self):
        """Gets the create_time of this DrugJobDto.

        作业创建时间

        :return: The create_time of this DrugJobDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DrugJobDto.

        作业创建时间

        :param create_time: The create_time of this DrugJobDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        """Gets the finish_time of this DrugJobDto.

        作业结束时间

        :return: The finish_time of this DrugJobDto.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this DrugJobDto.

        作业结束时间

        :param finish_time: The finish_time of this DrugJobDto.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def start_time(self):
        """Gets the start_time of this DrugJobDto.

        作业结束时间

        :return: The start_time of this DrugJobDto.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DrugJobDto.

        作业结束时间

        :param start_time: The start_time of this DrugJobDto.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def failed_message(self):
        """Gets the failed_message of this DrugJobDto.

        失败提示，当作业执行失败时会返回

        :return: The failed_message of this DrugJobDto.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        """Sets the failed_message of this DrugJobDto.

        失败提示，当作业执行失败时会返回

        :param failed_message: The failed_message of this DrugJobDto.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def user_name(self):
        """Gets the user_name of this DrugJobDto.

        创建任务的用户名称

        :return: The user_name of this DrugJobDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this DrugJobDto.

        创建任务的用户名称

        :param user_name: The user_name of this DrugJobDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def output_dir(self):
        """Gets the output_dir of this DrugJobDto.

        作业结果输出目录

        :return: The output_dir of this DrugJobDto.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        """Sets the output_dir of this DrugJobDto.

        作业结果输出目录

        :param output_dir: The output_dir of this DrugJobDto.
        :type output_dir: str
        """
        self._output_dir = output_dir

    @property
    def expect_charge_num(self):
        """Gets the expect_charge_num of this DrugJobDto.

        预估功能调用消耗次数

        :return: The expect_charge_num of this DrugJobDto.
        :rtype: int
        """
        return self._expect_charge_num

    @expect_charge_num.setter
    def expect_charge_num(self, expect_charge_num):
        """Sets the expect_charge_num of this DrugJobDto.

        预估功能调用消耗次数

        :param expect_charge_num: The expect_charge_num of this DrugJobDto.
        :type expect_charge_num: int
        """
        self._expect_charge_num = expect_charge_num

    @property
    def real_charge_num(self):
        """Gets the real_charge_num of this DrugJobDto.

        实际功能调用消耗次数

        :return: The real_charge_num of this DrugJobDto.
        :rtype: int
        """
        return self._real_charge_num

    @real_charge_num.setter
    def real_charge_num(self, real_charge_num):
        """Sets the real_charge_num of this DrugJobDto.

        实际功能调用消耗次数

        :param real_charge_num: The real_charge_num of this DrugJobDto.
        :type real_charge_num: int
        """
        self._real_charge_num = real_charge_num

    @property
    def progress(self):
        """Gets the progress of this DrugJobDto.

        :return: The progress of this DrugJobDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.Progress`
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DrugJobDto.

        :param progress: The progress of this DrugJobDto.
        :type progress: :class:`huaweicloudsdkeihealth.v1.Progress`
        """
        self._progress = progress

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
        if not isinstance(other, DrugJobDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
