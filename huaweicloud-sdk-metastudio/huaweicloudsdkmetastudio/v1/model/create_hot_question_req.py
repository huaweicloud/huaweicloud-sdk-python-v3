# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHotQuestionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'robot_id': 'str',
        'hot_question': 'str'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'hot_question': 'hot_question'
    }

    def __init__(self, robot_id=None, hot_question=None):
        """CreateHotQuestionReq

        The model defined in huaweicloud sdk

        :param robot_id: 机器人ID。
        :type robot_id: str
        :param hot_question: 热点问题。
        :type hot_question: str
        """
        
        

        self._robot_id = None
        self._hot_question = None
        self.discriminator = None

        self.robot_id = robot_id
        self.hot_question = hot_question

    @property
    def robot_id(self):
        """Gets the robot_id of this CreateHotQuestionReq.

        机器人ID。

        :return: The robot_id of this CreateHotQuestionReq.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this CreateHotQuestionReq.

        机器人ID。

        :param robot_id: The robot_id of this CreateHotQuestionReq.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def hot_question(self):
        """Gets the hot_question of this CreateHotQuestionReq.

        热点问题。

        :return: The hot_question of this CreateHotQuestionReq.
        :rtype: str
        """
        return self._hot_question

    @hot_question.setter
    def hot_question(self, hot_question):
        """Sets the hot_question of this CreateHotQuestionReq.

        热点问题。

        :param hot_question: The hot_question of this CreateHotQuestionReq.
        :type hot_question: str
        """
        self._hot_question = hot_question

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
        if not isinstance(other, CreateHotQuestionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
