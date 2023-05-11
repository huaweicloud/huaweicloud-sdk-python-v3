# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PcrTestRecordConfidence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'float',
        'sampling_time': 'float',
        'test_time': 'float',
        'test_result': 'float'
    }

    attribute_map = {
        'name': 'name',
        'sampling_time': 'sampling_time',
        'test_time': 'test_time',
        'test_result': 'test_result'
    }

    def __init__(self, name=None, sampling_time=None, test_time=None, test_result=None):
        """PcrTestRecordConfidence

        The model defined in huaweicloud sdk

        :param name: 姓名的置信度 
        :type name: float
        :param sampling_time: 核酸检测采样时间的置信度 
        :type sampling_time: float
        :param test_time: 核酸检测结果更新时间的置信度 
        :type test_time: float
        :param test_result: 核酸检测结果的置信度 
        :type test_result: float
        """
        
        

        self._name = None
        self._sampling_time = None
        self._test_time = None
        self._test_result = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if sampling_time is not None:
            self.sampling_time = sampling_time
        if test_time is not None:
            self.test_time = test_time
        if test_result is not None:
            self.test_result = test_result

    @property
    def name(self):
        """Gets the name of this PcrTestRecordConfidence.

        姓名的置信度 

        :return: The name of this PcrTestRecordConfidence.
        :rtype: float
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PcrTestRecordConfidence.

        姓名的置信度 

        :param name: The name of this PcrTestRecordConfidence.
        :type name: float
        """
        self._name = name

    @property
    def sampling_time(self):
        """Gets the sampling_time of this PcrTestRecordConfidence.

        核酸检测采样时间的置信度 

        :return: The sampling_time of this PcrTestRecordConfidence.
        :rtype: float
        """
        return self._sampling_time

    @sampling_time.setter
    def sampling_time(self, sampling_time):
        """Sets the sampling_time of this PcrTestRecordConfidence.

        核酸检测采样时间的置信度 

        :param sampling_time: The sampling_time of this PcrTestRecordConfidence.
        :type sampling_time: float
        """
        self._sampling_time = sampling_time

    @property
    def test_time(self):
        """Gets the test_time of this PcrTestRecordConfidence.

        核酸检测结果更新时间的置信度 

        :return: The test_time of this PcrTestRecordConfidence.
        :rtype: float
        """
        return self._test_time

    @test_time.setter
    def test_time(self, test_time):
        """Sets the test_time of this PcrTestRecordConfidence.

        核酸检测结果更新时间的置信度 

        :param test_time: The test_time of this PcrTestRecordConfidence.
        :type test_time: float
        """
        self._test_time = test_time

    @property
    def test_result(self):
        """Gets the test_result of this PcrTestRecordConfidence.

        核酸检测结果的置信度 

        :return: The test_result of this PcrTestRecordConfidence.
        :rtype: float
        """
        return self._test_result

    @test_result.setter
    def test_result(self, test_result):
        """Sets the test_result of this PcrTestRecordConfidence.

        核酸检测结果的置信度 

        :param test_result: The test_result of this PcrTestRecordConfidence.
        :type test_result: float
        """
        self._test_result = test_result

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
        if not isinstance(other, PcrTestRecordConfidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
