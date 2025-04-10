# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PcrTestRecordResult:

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
        'sampling_time': 'str',
        'test_time': 'str',
        'test_result': 'str',
        'confidence': 'PcrTestRecordConfidence',
        'words_block_count': 'int',
        'words_block_list': 'list[PcrTestRecordWordsBlockList]'
    }

    attribute_map = {
        'name': 'name',
        'sampling_time': 'sampling_time',
        'test_time': 'test_time',
        'test_result': 'test_result',
        'confidence': 'confidence',
        'words_block_count': 'words_block_count',
        'words_block_list': 'words_block_list'
    }

    def __init__(self, name=None, sampling_time=None, test_time=None, test_result=None, confidence=None, words_block_count=None, words_block_list=None):
        r"""PcrTestRecordResult

        The model defined in huaweicloud sdk

        :param name: 姓名 
        :type name: str
        :param sampling_time: 核酸检测采样时间 
        :type sampling_time: str
        :param test_time: 核酸检测结果更新时间 
        :type test_time: str
        :param test_result: 核酸检测结果，可选值包括：  - \&quot;positive\&quot;,即阳性  - \&quot;negative\&quot;,即阴性  - \&quot;unknown\&quot;,未知 
        :type test_result: str
        :param confidence: 
        :type confidence: :class:`huaweicloudsdkocr.v1.PcrTestRecordConfidence`
        :param words_block_count: 代表检测识别出来的文字块数目。 
        :type words_block_count: int
        :param words_block_list: 识别文字块列表，输出顺序从左到右，从上到下。 
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.PcrTestRecordWordsBlockList`]
        """
        
        

        self._name = None
        self._sampling_time = None
        self._test_time = None
        self._test_result = None
        self._confidence = None
        self._words_block_count = None
        self._words_block_list = None
        self.discriminator = None

        self.name = name
        self.sampling_time = sampling_time
        self.test_time = test_time
        self.test_result = test_result
        self.confidence = confidence
        self.words_block_count = words_block_count
        self.words_block_list = words_block_list

    @property
    def name(self):
        r"""Gets the name of this PcrTestRecordResult.

        姓名 

        :return: The name of this PcrTestRecordResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PcrTestRecordResult.

        姓名 

        :param name: The name of this PcrTestRecordResult.
        :type name: str
        """
        self._name = name

    @property
    def sampling_time(self):
        r"""Gets the sampling_time of this PcrTestRecordResult.

        核酸检测采样时间 

        :return: The sampling_time of this PcrTestRecordResult.
        :rtype: str
        """
        return self._sampling_time

    @sampling_time.setter
    def sampling_time(self, sampling_time):
        r"""Sets the sampling_time of this PcrTestRecordResult.

        核酸检测采样时间 

        :param sampling_time: The sampling_time of this PcrTestRecordResult.
        :type sampling_time: str
        """
        self._sampling_time = sampling_time

    @property
    def test_time(self):
        r"""Gets the test_time of this PcrTestRecordResult.

        核酸检测结果更新时间 

        :return: The test_time of this PcrTestRecordResult.
        :rtype: str
        """
        return self._test_time

    @test_time.setter
    def test_time(self, test_time):
        r"""Sets the test_time of this PcrTestRecordResult.

        核酸检测结果更新时间 

        :param test_time: The test_time of this PcrTestRecordResult.
        :type test_time: str
        """
        self._test_time = test_time

    @property
    def test_result(self):
        r"""Gets the test_result of this PcrTestRecordResult.

        核酸检测结果，可选值包括：  - \"positive\",即阳性  - \"negative\",即阴性  - \"unknown\",未知 

        :return: The test_result of this PcrTestRecordResult.
        :rtype: str
        """
        return self._test_result

    @test_result.setter
    def test_result(self, test_result):
        r"""Sets the test_result of this PcrTestRecordResult.

        核酸检测结果，可选值包括：  - \"positive\",即阳性  - \"negative\",即阴性  - \"unknown\",未知 

        :param test_result: The test_result of this PcrTestRecordResult.
        :type test_result: str
        """
        self._test_result = test_result

    @property
    def confidence(self):
        r"""Gets the confidence of this PcrTestRecordResult.

        :return: The confidence of this PcrTestRecordResult.
        :rtype: :class:`huaweicloudsdkocr.v1.PcrTestRecordConfidence`
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this PcrTestRecordResult.

        :param confidence: The confidence of this PcrTestRecordResult.
        :type confidence: :class:`huaweicloudsdkocr.v1.PcrTestRecordConfidence`
        """
        self._confidence = confidence

    @property
    def words_block_count(self):
        r"""Gets the words_block_count of this PcrTestRecordResult.

        代表检测识别出来的文字块数目。 

        :return: The words_block_count of this PcrTestRecordResult.
        :rtype: int
        """
        return self._words_block_count

    @words_block_count.setter
    def words_block_count(self, words_block_count):
        r"""Sets the words_block_count of this PcrTestRecordResult.

        代表检测识别出来的文字块数目。 

        :param words_block_count: The words_block_count of this PcrTestRecordResult.
        :type words_block_count: int
        """
        self._words_block_count = words_block_count

    @property
    def words_block_list(self):
        r"""Gets the words_block_list of this PcrTestRecordResult.

        识别文字块列表，输出顺序从左到右，从上到下。 

        :return: The words_block_list of this PcrTestRecordResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.PcrTestRecordWordsBlockList`]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        r"""Sets the words_block_list of this PcrTestRecordResult.

        识别文字块列表，输出顺序从左到右，从上到下。 

        :param words_block_list: The words_block_list of this PcrTestRecordResult.
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.PcrTestRecordWordsBlockList`]
        """
        self._words_block_list = words_block_list

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
        if not isinstance(other, PcrTestRecordResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
