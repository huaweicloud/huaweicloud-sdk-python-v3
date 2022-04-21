# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Phoneme:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'arpa': 'str',
        'ipa': 'str',
        'start_time': 'float',
        'end_time': 'float',
        'fluency': 'PhonemeFluency',
        'pronunciation': 'PhonemePronunciation'
    }

    attribute_map = {
        'arpa': 'arpa',
        'ipa': 'ipa',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'fluency': 'fluency',
        'pronunciation': 'pronunciation'
    }

    def __init__(self, arpa=None, ipa=None, start_time=None, end_time=None, fluency=None, pronunciation=None):
        """Phoneme

        The model defined in huaweicloud sdk

        :param arpa: 音标（ARPAbet音标系统）
        :type arpa: str
        :param ipa: 音标（国际音标系统）
        :type ipa: str
        :param start_time: 
        :type start_time: float
        :param end_time: 
        :type end_time: float
        :param fluency: 
        :type fluency: :class:`huaweicloudsdksis.v1.PhonemeFluency`
        :param pronunciation: 
        :type pronunciation: :class:`huaweicloudsdksis.v1.PhonemePronunciation`
        """
        
        

        self._arpa = None
        self._ipa = None
        self._start_time = None
        self._end_time = None
        self._fluency = None
        self._pronunciation = None
        self.discriminator = None

        self.arpa = arpa
        self.ipa = ipa
        self.start_time = start_time
        self.end_time = end_time
        self.fluency = fluency
        self.pronunciation = pronunciation

    @property
    def arpa(self):
        """Gets the arpa of this Phoneme.

        音标（ARPAbet音标系统）

        :return: The arpa of this Phoneme.
        :rtype: str
        """
        return self._arpa

    @arpa.setter
    def arpa(self, arpa):
        """Sets the arpa of this Phoneme.

        音标（ARPAbet音标系统）

        :param arpa: The arpa of this Phoneme.
        :type arpa: str
        """
        self._arpa = arpa

    @property
    def ipa(self):
        """Gets the ipa of this Phoneme.

        音标（国际音标系统）

        :return: The ipa of this Phoneme.
        :rtype: str
        """
        return self._ipa

    @ipa.setter
    def ipa(self, ipa):
        """Sets the ipa of this Phoneme.

        音标（国际音标系统）

        :param ipa: The ipa of this Phoneme.
        :type ipa: str
        """
        self._ipa = ipa

    @property
    def start_time(self):
        """Gets the start_time of this Phoneme.

        

        :return: The start_time of this Phoneme.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Phoneme.

        

        :param start_time: The start_time of this Phoneme.
        :type start_time: float
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Phoneme.

        

        :return: The end_time of this Phoneme.
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Phoneme.

        

        :param end_time: The end_time of this Phoneme.
        :type end_time: float
        """
        self._end_time = end_time

    @property
    def fluency(self):
        """Gets the fluency of this Phoneme.


        :return: The fluency of this Phoneme.
        :rtype: :class:`huaweicloudsdksis.v1.PhonemeFluency`
        """
        return self._fluency

    @fluency.setter
    def fluency(self, fluency):
        """Sets the fluency of this Phoneme.


        :param fluency: The fluency of this Phoneme.
        :type fluency: :class:`huaweicloudsdksis.v1.PhonemeFluency`
        """
        self._fluency = fluency

    @property
    def pronunciation(self):
        """Gets the pronunciation of this Phoneme.


        :return: The pronunciation of this Phoneme.
        :rtype: :class:`huaweicloudsdksis.v1.PhonemePronunciation`
        """
        return self._pronunciation

    @pronunciation.setter
    def pronunciation(self, pronunciation):
        """Sets the pronunciation of this Phoneme.


        :param pronunciation: The pronunciation of this Phoneme.
        :type pronunciation: :class:`huaweicloudsdksis.v1.PhonemePronunciation`
        """
        self._pronunciation = pronunciation

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
        if not isinstance(other, Phoneme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
