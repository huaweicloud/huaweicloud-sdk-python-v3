# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobCard:

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
        'job_id': 'str',
        'is_send': 'str',
        'end_time': 'str',
        'average_score': 'str',
        'submit_job_num': 'int',
        'create_status': 'str',
        'send_type': 'str',
        'is_score_visibility': 'str',
        'send_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'job_id': 'job_id',
        'is_send': 'is_send',
        'end_time': 'end_time',
        'average_score': 'average_score',
        'submit_job_num': 'submit_job_num',
        'create_status': 'create_status',
        'send_type': 'send_type',
        'is_score_visibility': 'is_score_visibility',
        'send_time': 'send_time'
    }

    def __init__(self, name=None, job_id=None, is_send=None, end_time=None, average_score=None, submit_job_num=None, create_status=None, send_type=None, is_score_visibility=None, send_time=None):
        """JobCard

        The model defined in huaweicloud sdk

        :param name: 作业名称
        :type name: str
        :param job_id: 作业ID
        :type job_id: str
        :param is_send: 作业下发状态(unsend:作业未下发, send:作业已下发)
        :type is_send: str
        :param end_time: 作业截止时间, 日期格式：yyyy-MM-dd HH:mm:ss
        :type end_time: str
        :param average_score: 作业均分
        :type average_score: str
        :param submit_job_num: 作业提交人数
        :type submit_job_num: int
        :param create_status: 作业创建状态(yes:作业可以下发, no:作业不能下发)
        :type create_status: str
        :param send_type: 作业下发类型(specific:指定成员下发, all:下发课堂全员)
        :type send_type: str
        :param is_score_visibility: 作业成绩是否公布(unpublish:表示未公布成绩, publish:表示已公布成绩)
        :type is_score_visibility: str
        :param send_time: 作业下发时间, 日期格式：yyyy-MM-dd HH:mm:ss
        :type send_time: str
        """
        
        

        self._name = None
        self._job_id = None
        self._is_send = None
        self._end_time = None
        self._average_score = None
        self._submit_job_num = None
        self._create_status = None
        self._send_type = None
        self._is_score_visibility = None
        self._send_time = None
        self.discriminator = None

        self.name = name
        self.job_id = job_id
        self.is_send = is_send
        self.end_time = end_time
        self.average_score = average_score
        self.submit_job_num = submit_job_num
        self.create_status = create_status
        self.send_type = send_type
        self.is_score_visibility = is_score_visibility
        self.send_time = send_time

    @property
    def name(self):
        """Gets the name of this JobCard.

        作业名称

        :return: The name of this JobCard.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobCard.

        作业名称

        :param name: The name of this JobCard.
        :type name: str
        """
        self._name = name

    @property
    def job_id(self):
        """Gets the job_id of this JobCard.

        作业ID

        :return: The job_id of this JobCard.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobCard.

        作业ID

        :param job_id: The job_id of this JobCard.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def is_send(self):
        """Gets the is_send of this JobCard.

        作业下发状态(unsend:作业未下发, send:作业已下发)

        :return: The is_send of this JobCard.
        :rtype: str
        """
        return self._is_send

    @is_send.setter
    def is_send(self, is_send):
        """Sets the is_send of this JobCard.

        作业下发状态(unsend:作业未下发, send:作业已下发)

        :param is_send: The is_send of this JobCard.
        :type is_send: str
        """
        self._is_send = is_send

    @property
    def end_time(self):
        """Gets the end_time of this JobCard.

        作业截止时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :return: The end_time of this JobCard.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this JobCard.

        作业截止时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :param end_time: The end_time of this JobCard.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def average_score(self):
        """Gets the average_score of this JobCard.

        作业均分

        :return: The average_score of this JobCard.
        :rtype: str
        """
        return self._average_score

    @average_score.setter
    def average_score(self, average_score):
        """Sets the average_score of this JobCard.

        作业均分

        :param average_score: The average_score of this JobCard.
        :type average_score: str
        """
        self._average_score = average_score

    @property
    def submit_job_num(self):
        """Gets the submit_job_num of this JobCard.

        作业提交人数

        :return: The submit_job_num of this JobCard.
        :rtype: int
        """
        return self._submit_job_num

    @submit_job_num.setter
    def submit_job_num(self, submit_job_num):
        """Sets the submit_job_num of this JobCard.

        作业提交人数

        :param submit_job_num: The submit_job_num of this JobCard.
        :type submit_job_num: int
        """
        self._submit_job_num = submit_job_num

    @property
    def create_status(self):
        """Gets the create_status of this JobCard.

        作业创建状态(yes:作业可以下发, no:作业不能下发)

        :return: The create_status of this JobCard.
        :rtype: str
        """
        return self._create_status

    @create_status.setter
    def create_status(self, create_status):
        """Sets the create_status of this JobCard.

        作业创建状态(yes:作业可以下发, no:作业不能下发)

        :param create_status: The create_status of this JobCard.
        :type create_status: str
        """
        self._create_status = create_status

    @property
    def send_type(self):
        """Gets the send_type of this JobCard.

        作业下发类型(specific:指定成员下发, all:下发课堂全员)

        :return: The send_type of this JobCard.
        :rtype: str
        """
        return self._send_type

    @send_type.setter
    def send_type(self, send_type):
        """Sets the send_type of this JobCard.

        作业下发类型(specific:指定成员下发, all:下发课堂全员)

        :param send_type: The send_type of this JobCard.
        :type send_type: str
        """
        self._send_type = send_type

    @property
    def is_score_visibility(self):
        """Gets the is_score_visibility of this JobCard.

        作业成绩是否公布(unpublish:表示未公布成绩, publish:表示已公布成绩)

        :return: The is_score_visibility of this JobCard.
        :rtype: str
        """
        return self._is_score_visibility

    @is_score_visibility.setter
    def is_score_visibility(self, is_score_visibility):
        """Sets the is_score_visibility of this JobCard.

        作业成绩是否公布(unpublish:表示未公布成绩, publish:表示已公布成绩)

        :param is_score_visibility: The is_score_visibility of this JobCard.
        :type is_score_visibility: str
        """
        self._is_score_visibility = is_score_visibility

    @property
    def send_time(self):
        """Gets the send_time of this JobCard.

        作业下发时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :return: The send_time of this JobCard.
        :rtype: str
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this JobCard.

        作业下发时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :param send_time: The send_time of this JobCard.
        :type send_time: str
        """
        self._send_time = send_time

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
        if not isinstance(other, JobCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
