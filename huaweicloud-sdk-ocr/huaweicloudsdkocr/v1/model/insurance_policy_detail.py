# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsurancePolicyDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'words': 'str',
        'location': 'list[list[int]]'
    }

    attribute_map = {
        'words': 'words',
        'location': 'location'
    }

    def __init__(self, words=None, location=None):
        r"""InsurancePolicyDetail

        The model defined in huaweicloud sdk

        :param words: 对应识别出的文本内容
        :type words: str
        :param location: 对应识别出的四个顶点坐标 
        :type location: list[list[int]]
        """
        
        

        self._words = None
        self._location = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if location is not None:
            self.location = location

    @property
    def words(self):
        r"""Gets the words of this InsurancePolicyDetail.

        对应识别出的文本内容

        :return: The words of this InsurancePolicyDetail.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        r"""Sets the words of this InsurancePolicyDetail.

        对应识别出的文本内容

        :param words: The words of this InsurancePolicyDetail.
        :type words: str
        """
        self._words = words

    @property
    def location(self):
        r"""Gets the location of this InsurancePolicyDetail.

        对应识别出的四个顶点坐标 

        :return: The location of this InsurancePolicyDetail.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this InsurancePolicyDetail.

        对应识别出的四个顶点坐标 

        :param location: The location of this InsurancePolicyDetail.
        :type location: list[list[int]]
        """
        self._location = location

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
        if not isinstance(other, InsurancePolicyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
