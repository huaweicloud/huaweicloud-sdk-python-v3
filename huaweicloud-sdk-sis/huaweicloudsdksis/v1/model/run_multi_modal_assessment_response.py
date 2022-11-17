# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunMultiModalAssessmentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'score': 'float',
        'completeness': 'float',
        'duration': 'float',
        'pronunciation': 'Pronunciation',
        'fluency': 'Fluency',
        'words': 'list[Word]',
        'trace_id': 'str'
    }

    attribute_map = {
        'score': 'score',
        'completeness': 'completeness',
        'duration': 'duration',
        'pronunciation': 'pronunciation',
        'fluency': 'fluency',
        'words': 'words',
        'trace_id': 'traceId'
    }

    def __init__(self, score=None, completeness=None, duration=None, pronunciation=None, fluency=None, words=None, trace_id=None):
        """RunMultiModalAssessmentResponse

        The model defined in huaweicloud sdk

        :param score: 综合评分，0-100
        :type score: float
        :param completeness: 完整性评分，0-100 表示有多少比例的单词发音是清楚的
        :type completeness: float
        :param duration: 音频/视频时长，单位秒
        :type duration: float
        :param pronunciation: 
        :type pronunciation: :class:`huaweicloudsdksis.v1.Pronunciation`
        :param fluency: 
        :type fluency: :class:`huaweicloudsdksis.v1.Fluency`
        :param words: 单词评测打分表
        :type words: list[:class:`huaweicloudsdksis.v1.Word`]
        :param trace_id: 评测失败时定位问题使用的字段
        :type trace_id: str
        """
        
        super(RunMultiModalAssessmentResponse, self).__init__()

        self._score = None
        self._completeness = None
        self._duration = None
        self._pronunciation = None
        self._fluency = None
        self._words = None
        self._trace_id = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if completeness is not None:
            self.completeness = completeness
        if duration is not None:
            self.duration = duration
        if pronunciation is not None:
            self.pronunciation = pronunciation
        if fluency is not None:
            self.fluency = fluency
        if words is not None:
            self.words = words
        if trace_id is not None:
            self.trace_id = trace_id

    @property
    def score(self):
        """Gets the score of this RunMultiModalAssessmentResponse.

        综合评分，0-100

        :return: The score of this RunMultiModalAssessmentResponse.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this RunMultiModalAssessmentResponse.

        综合评分，0-100

        :param score: The score of this RunMultiModalAssessmentResponse.
        :type score: float
        """
        self._score = score

    @property
    def completeness(self):
        """Gets the completeness of this RunMultiModalAssessmentResponse.

        完整性评分，0-100 表示有多少比例的单词发音是清楚的

        :return: The completeness of this RunMultiModalAssessmentResponse.
        :rtype: float
        """
        return self._completeness

    @completeness.setter
    def completeness(self, completeness):
        """Sets the completeness of this RunMultiModalAssessmentResponse.

        完整性评分，0-100 表示有多少比例的单词发音是清楚的

        :param completeness: The completeness of this RunMultiModalAssessmentResponse.
        :type completeness: float
        """
        self._completeness = completeness

    @property
    def duration(self):
        """Gets the duration of this RunMultiModalAssessmentResponse.

        音频/视频时长，单位秒

        :return: The duration of this RunMultiModalAssessmentResponse.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this RunMultiModalAssessmentResponse.

        音频/视频时长，单位秒

        :param duration: The duration of this RunMultiModalAssessmentResponse.
        :type duration: float
        """
        self._duration = duration

    @property
    def pronunciation(self):
        """Gets the pronunciation of this RunMultiModalAssessmentResponse.

        :return: The pronunciation of this RunMultiModalAssessmentResponse.
        :rtype: :class:`huaweicloudsdksis.v1.Pronunciation`
        """
        return self._pronunciation

    @pronunciation.setter
    def pronunciation(self, pronunciation):
        """Sets the pronunciation of this RunMultiModalAssessmentResponse.

        :param pronunciation: The pronunciation of this RunMultiModalAssessmentResponse.
        :type pronunciation: :class:`huaweicloudsdksis.v1.Pronunciation`
        """
        self._pronunciation = pronunciation

    @property
    def fluency(self):
        """Gets the fluency of this RunMultiModalAssessmentResponse.

        :return: The fluency of this RunMultiModalAssessmentResponse.
        :rtype: :class:`huaweicloudsdksis.v1.Fluency`
        """
        return self._fluency

    @fluency.setter
    def fluency(self, fluency):
        """Sets the fluency of this RunMultiModalAssessmentResponse.

        :param fluency: The fluency of this RunMultiModalAssessmentResponse.
        :type fluency: :class:`huaweicloudsdksis.v1.Fluency`
        """
        self._fluency = fluency

    @property
    def words(self):
        """Gets the words of this RunMultiModalAssessmentResponse.

        单词评测打分表

        :return: The words of this RunMultiModalAssessmentResponse.
        :rtype: list[:class:`huaweicloudsdksis.v1.Word`]
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this RunMultiModalAssessmentResponse.

        单词评测打分表

        :param words: The words of this RunMultiModalAssessmentResponse.
        :type words: list[:class:`huaweicloudsdksis.v1.Word`]
        """
        self._words = words

    @property
    def trace_id(self):
        """Gets the trace_id of this RunMultiModalAssessmentResponse.

        评测失败时定位问题使用的字段

        :return: The trace_id of this RunMultiModalAssessmentResponse.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this RunMultiModalAssessmentResponse.

        评测失败时定位问题使用的字段

        :param trace_id: The trace_id of this RunMultiModalAssessmentResponse.
        :type trace_id: str
        """
        self._trace_id = trace_id

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
        if not isinstance(other, RunMultiModalAssessmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
