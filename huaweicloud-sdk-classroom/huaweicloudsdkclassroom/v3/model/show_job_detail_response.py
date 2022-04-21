# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'accept_job_num': 'int',
        'end_time': 'str',
        'is_answer_visibility': 'str',
        'is_score_visibility': 'str',
        'average_score': 'str',
        'score_job_num': 'int',
        'submit_job_num': 'int'
    }

    attribute_map = {
        'accept_job_num': 'accept_job_num',
        'end_time': 'end_time',
        'is_answer_visibility': 'is_answer_visibility',
        'is_score_visibility': 'is_score_visibility',
        'average_score': 'average_score',
        'score_job_num': 'score_job_num',
        'submit_job_num': 'submit_job_num'
    }

    def __init__(self, accept_job_num=None, end_time=None, is_answer_visibility=None, is_score_visibility=None, average_score=None, score_job_num=None, submit_job_num=None):
        """ShowJobDetailResponse

        The model defined in huaweicloud sdk

        :param accept_job_num: 作业下发人数
        :type accept_job_num: int
        :param end_time: 作业截止时间, 日期格式：yyyy-MM-dd HH:mm:ss
        :type end_time: str
        :param is_answer_visibility: 作业答案是否公布(unpublish:表示未公布答案, publish:表示已公布答案)
        :type is_answer_visibility: str
        :param is_score_visibility: 作业成绩是否公布(unpublish:表示未公布成绩, publish:表示已公布成绩)
        :type is_score_visibility: str
        :param average_score: 作业均分
        :type average_score: str
        :param score_job_num: 老师手动评分人数
        :type score_job_num: int
        :param submit_job_num: 作业提交人数
        :type submit_job_num: int
        """
        
        super(ShowJobDetailResponse, self).__init__()

        self._accept_job_num = None
        self._end_time = None
        self._is_answer_visibility = None
        self._is_score_visibility = None
        self._average_score = None
        self._score_job_num = None
        self._submit_job_num = None
        self.discriminator = None

        if accept_job_num is not None:
            self.accept_job_num = accept_job_num
        if end_time is not None:
            self.end_time = end_time
        if is_answer_visibility is not None:
            self.is_answer_visibility = is_answer_visibility
        if is_score_visibility is not None:
            self.is_score_visibility = is_score_visibility
        if average_score is not None:
            self.average_score = average_score
        if score_job_num is not None:
            self.score_job_num = score_job_num
        if submit_job_num is not None:
            self.submit_job_num = submit_job_num

    @property
    def accept_job_num(self):
        """Gets the accept_job_num of this ShowJobDetailResponse.

        作业下发人数

        :return: The accept_job_num of this ShowJobDetailResponse.
        :rtype: int
        """
        return self._accept_job_num

    @accept_job_num.setter
    def accept_job_num(self, accept_job_num):
        """Sets the accept_job_num of this ShowJobDetailResponse.

        作业下发人数

        :param accept_job_num: The accept_job_num of this ShowJobDetailResponse.
        :type accept_job_num: int
        """
        self._accept_job_num = accept_job_num

    @property
    def end_time(self):
        """Gets the end_time of this ShowJobDetailResponse.

        作业截止时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :return: The end_time of this ShowJobDetailResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowJobDetailResponse.

        作业截止时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :param end_time: The end_time of this ShowJobDetailResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def is_answer_visibility(self):
        """Gets the is_answer_visibility of this ShowJobDetailResponse.

        作业答案是否公布(unpublish:表示未公布答案, publish:表示已公布答案)

        :return: The is_answer_visibility of this ShowJobDetailResponse.
        :rtype: str
        """
        return self._is_answer_visibility

    @is_answer_visibility.setter
    def is_answer_visibility(self, is_answer_visibility):
        """Sets the is_answer_visibility of this ShowJobDetailResponse.

        作业答案是否公布(unpublish:表示未公布答案, publish:表示已公布答案)

        :param is_answer_visibility: The is_answer_visibility of this ShowJobDetailResponse.
        :type is_answer_visibility: str
        """
        self._is_answer_visibility = is_answer_visibility

    @property
    def is_score_visibility(self):
        """Gets the is_score_visibility of this ShowJobDetailResponse.

        作业成绩是否公布(unpublish:表示未公布成绩, publish:表示已公布成绩)

        :return: The is_score_visibility of this ShowJobDetailResponse.
        :rtype: str
        """
        return self._is_score_visibility

    @is_score_visibility.setter
    def is_score_visibility(self, is_score_visibility):
        """Sets the is_score_visibility of this ShowJobDetailResponse.

        作业成绩是否公布(unpublish:表示未公布成绩, publish:表示已公布成绩)

        :param is_score_visibility: The is_score_visibility of this ShowJobDetailResponse.
        :type is_score_visibility: str
        """
        self._is_score_visibility = is_score_visibility

    @property
    def average_score(self):
        """Gets the average_score of this ShowJobDetailResponse.

        作业均分

        :return: The average_score of this ShowJobDetailResponse.
        :rtype: str
        """
        return self._average_score

    @average_score.setter
    def average_score(self, average_score):
        """Sets the average_score of this ShowJobDetailResponse.

        作业均分

        :param average_score: The average_score of this ShowJobDetailResponse.
        :type average_score: str
        """
        self._average_score = average_score

    @property
    def score_job_num(self):
        """Gets the score_job_num of this ShowJobDetailResponse.

        老师手动评分人数

        :return: The score_job_num of this ShowJobDetailResponse.
        :rtype: int
        """
        return self._score_job_num

    @score_job_num.setter
    def score_job_num(self, score_job_num):
        """Sets the score_job_num of this ShowJobDetailResponse.

        老师手动评分人数

        :param score_job_num: The score_job_num of this ShowJobDetailResponse.
        :type score_job_num: int
        """
        self._score_job_num = score_job_num

    @property
    def submit_job_num(self):
        """Gets the submit_job_num of this ShowJobDetailResponse.

        作业提交人数

        :return: The submit_job_num of this ShowJobDetailResponse.
        :rtype: int
        """
        return self._submit_job_num

    @submit_job_num.setter
    def submit_job_num(self, submit_job_num):
        """Sets the submit_job_num of this ShowJobDetailResponse.

        作业提交人数

        :param submit_job_num: The submit_job_num of this ShowJobDetailResponse.
        :type submit_job_num: int
        """
        self._submit_job_num = submit_job_num

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
        if not isinstance(other, ShowJobDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
