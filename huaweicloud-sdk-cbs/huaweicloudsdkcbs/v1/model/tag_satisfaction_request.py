# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagSatisfactionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'qabot_id': 'str',
        'request_id': 'str',
        'body': 'PostSatisfactionReq'
    }

    attribute_map = {
        'qabot_id': 'qabot_id',
        'request_id': 'request_id',
        'body': 'body'
    }

    def __init__(self, qabot_id=None, request_id=None, body=None):
        """TagSatisfactionRequest

        The model defined in huaweicloud sdk

        :param qabot_id: qabot编号，UUID格式。
        :type qabot_id: str
        :param request_id: 请求ID，由问答机器人会话生成。
        :type request_id: str
        :param body: Body of the TagSatisfactionRequest
        :type body: :class:`huaweicloudsdkcbs.v1.PostSatisfactionReq`
        """
        
        

        self._qabot_id = None
        self._request_id = None
        self._body = None
        self.discriminator = None

        self.qabot_id = qabot_id
        self.request_id = request_id
        if body is not None:
            self.body = body

    @property
    def qabot_id(self):
        """Gets the qabot_id of this TagSatisfactionRequest.

        qabot编号，UUID格式。

        :return: The qabot_id of this TagSatisfactionRequest.
        :rtype: str
        """
        return self._qabot_id

    @qabot_id.setter
    def qabot_id(self, qabot_id):
        """Sets the qabot_id of this TagSatisfactionRequest.

        qabot编号，UUID格式。

        :param qabot_id: The qabot_id of this TagSatisfactionRequest.
        :type qabot_id: str
        """
        self._qabot_id = qabot_id

    @property
    def request_id(self):
        """Gets the request_id of this TagSatisfactionRequest.

        请求ID，由问答机器人会话生成。

        :return: The request_id of this TagSatisfactionRequest.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this TagSatisfactionRequest.

        请求ID，由问答机器人会话生成。

        :param request_id: The request_id of this TagSatisfactionRequest.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def body(self):
        """Gets the body of this TagSatisfactionRequest.

        :return: The body of this TagSatisfactionRequest.
        :rtype: :class:`huaweicloudsdkcbs.v1.PostSatisfactionReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this TagSatisfactionRequest.

        :param body: The body of this TagSatisfactionRequest.
        :type body: :class:`huaweicloudsdkcbs.v1.PostSatisfactionReq`
        """
        self._body = body

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
        if not isinstance(other, TagSatisfactionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
