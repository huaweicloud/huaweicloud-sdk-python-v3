# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEvaluationReplyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reply_id': 'int'
    }

    attribute_map = {
        'reply_id': 'reply_id'
    }

    def __init__(self, reply_id=None):
        r"""DeleteEvaluationReplyRequest

        The model defined in huaweicloud sdk

        :param reply_id: 回复id
        :type reply_id: int
        """
        
        

        self._reply_id = None
        self.discriminator = None

        self.reply_id = reply_id

    @property
    def reply_id(self):
        r"""Gets the reply_id of this DeleteEvaluationReplyRequest.

        回复id

        :return: The reply_id of this DeleteEvaluationReplyRequest.
        :rtype: int
        """
        return self._reply_id

    @reply_id.setter
    def reply_id(self, reply_id):
        r"""Sets the reply_id of this DeleteEvaluationReplyRequest.

        回复id

        :param reply_id: The reply_id of this DeleteEvaluationReplyRequest.
        :type reply_id: int
        """
        self._reply_id = reply_id

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
        if not isinstance(other, DeleteEvaluationReplyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
