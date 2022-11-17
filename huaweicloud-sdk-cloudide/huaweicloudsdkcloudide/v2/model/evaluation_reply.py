# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationReply:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluation_id': 'str',
        'reply_id': 'str',
        'text': 'str'
    }

    attribute_map = {
        'evaluation_id': 'evaluation_id',
        'reply_id': 'reply_id',
        'text': 'text'
    }

    def __init__(self, evaluation_id=None, reply_id=None, text=None):
        """EvaluationReply

        The model defined in huaweicloud sdk

        :param evaluation_id: 所在评论id
        :type evaluation_id: str
        :param reply_id: 回复评论的id 空表示回复主评论
        :type reply_id: str
        :param text: 评论或回复内容
        :type text: str
        """
        
        

        self._evaluation_id = None
        self._reply_id = None
        self._text = None
        self.discriminator = None

        if evaluation_id is not None:
            self.evaluation_id = evaluation_id
        if reply_id is not None:
            self.reply_id = reply_id
        self.text = text

    @property
    def evaluation_id(self):
        """Gets the evaluation_id of this EvaluationReply.

        所在评论id

        :return: The evaluation_id of this EvaluationReply.
        :rtype: str
        """
        return self._evaluation_id

    @evaluation_id.setter
    def evaluation_id(self, evaluation_id):
        """Sets the evaluation_id of this EvaluationReply.

        所在评论id

        :param evaluation_id: The evaluation_id of this EvaluationReply.
        :type evaluation_id: str
        """
        self._evaluation_id = evaluation_id

    @property
    def reply_id(self):
        """Gets the reply_id of this EvaluationReply.

        回复评论的id 空表示回复主评论

        :return: The reply_id of this EvaluationReply.
        :rtype: str
        """
        return self._reply_id

    @reply_id.setter
    def reply_id(self, reply_id):
        """Sets the reply_id of this EvaluationReply.

        回复评论的id 空表示回复主评论

        :param reply_id: The reply_id of this EvaluationReply.
        :type reply_id: str
        """
        self._reply_id = reply_id

    @property
    def text(self):
        """Gets the text of this EvaluationReply.

        评论或回复内容

        :return: The text of this EvaluationReply.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this EvaluationReply.

        评论或回复内容

        :param text: The text of this EvaluationReply.
        :type text: str
        """
        self._text = text

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
        if not isinstance(other, EvaluationReply):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
