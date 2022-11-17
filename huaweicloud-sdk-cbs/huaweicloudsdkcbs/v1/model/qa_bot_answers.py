# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QaBotAnswers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'answers': 'list[QaBotAnswer]',
        'request_id': 'str'
    }

    attribute_map = {
        'answers': 'answers',
        'request_id': 'request_id'
    }

    def __init__(self, answers=None, request_id=None):
        """QaBotAnswers

        The model defined in huaweicloud sdk

        :param answers: 问答机器人回复。
        :type answers: list[:class:`huaweicloudsdkcbs.v1.QaBotAnswer`]
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        

        self._answers = None
        self._request_id = None
        self.discriminator = None

        if answers is not None:
            self.answers = answers
        self.request_id = request_id

    @property
    def answers(self):
        """Gets the answers of this QaBotAnswers.

        问答机器人回复。

        :return: The answers of this QaBotAnswers.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.QaBotAnswer`]
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        """Sets the answers of this QaBotAnswers.

        问答机器人回复。

        :param answers: The answers of this QaBotAnswers.
        :type answers: list[:class:`huaweicloudsdkcbs.v1.QaBotAnswer`]
        """
        self._answers = answers

    @property
    def request_id(self):
        """Gets the request_id of this QaBotAnswers.

        请求ID。

        :return: The request_id of this QaBotAnswers.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this QaBotAnswers.

        请求ID。

        :param request_id: The request_id of this QaBotAnswers.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, QaBotAnswers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
