# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHotWordsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hot_words_type': 'HotWordsTypeEnum',
        'robot_id': 'str',
        'sis_hot_words': 'CreateSisHotWords'
    }

    attribute_map = {
        'hot_words_type': 'hot_words_type',
        'robot_id': 'robot_id',
        'sis_hot_words': 'sis_hot_words'
    }

    def __init__(self, hot_words_type=None, robot_id=None, sis_hot_words=None):
        """CreateHotWordsReq

        The model defined in huaweicloud sdk

        :param hot_words_type: 
        :type hot_words_type: :class:`huaweicloudsdkmetastudio.v1.HotWordsTypeEnum`
        :param robot_id: 应用ID。
        :type robot_id: str
        :param sis_hot_words: 
        :type sis_hot_words: :class:`huaweicloudsdkmetastudio.v1.CreateSisHotWords`
        """
        
        

        self._hot_words_type = None
        self._robot_id = None
        self._sis_hot_words = None
        self.discriminator = None

        self.hot_words_type = hot_words_type
        self.robot_id = robot_id
        self.sis_hot_words = sis_hot_words

    @property
    def hot_words_type(self):
        """Gets the hot_words_type of this CreateHotWordsReq.

        :return: The hot_words_type of this CreateHotWordsReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HotWordsTypeEnum`
        """
        return self._hot_words_type

    @hot_words_type.setter
    def hot_words_type(self, hot_words_type):
        """Sets the hot_words_type of this CreateHotWordsReq.

        :param hot_words_type: The hot_words_type of this CreateHotWordsReq.
        :type hot_words_type: :class:`huaweicloudsdkmetastudio.v1.HotWordsTypeEnum`
        """
        self._hot_words_type = hot_words_type

    @property
    def robot_id(self):
        """Gets the robot_id of this CreateHotWordsReq.

        应用ID。

        :return: The robot_id of this CreateHotWordsReq.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this CreateHotWordsReq.

        应用ID。

        :param robot_id: The robot_id of this CreateHotWordsReq.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def sis_hot_words(self):
        """Gets the sis_hot_words of this CreateHotWordsReq.

        :return: The sis_hot_words of this CreateHotWordsReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateSisHotWords`
        """
        return self._sis_hot_words

    @sis_hot_words.setter
    def sis_hot_words(self, sis_hot_words):
        """Sets the sis_hot_words of this CreateHotWordsReq.

        :param sis_hot_words: The sis_hot_words of this CreateHotWordsReq.
        :type sis_hot_words: :class:`huaweicloudsdkmetastudio.v1.CreateSisHotWords`
        """
        self._sis_hot_words = sis_hot_words

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
        if not isinstance(other, CreateHotWordsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
