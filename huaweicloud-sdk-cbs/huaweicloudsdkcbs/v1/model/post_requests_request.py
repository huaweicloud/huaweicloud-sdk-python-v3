# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostRequestsRequest:

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
        'body': 'PostOldRequestsReq'
    }

    attribute_map = {
        'qabot_id': 'qabot_id',
        'body': 'body'
    }

    def __init__(self, qabot_id=None, body=None):
        r"""PostRequestsRequest

        The model defined in huaweicloud sdk

        :param qabot_id: qabot编号，UUID格式，如：303a0a00-c88a-43e3-aa2f-d5b8b9832b02。
        :type qabot_id: str
        :param body: Body of the PostRequestsRequest
        :type body: :class:`huaweicloudsdkcbs.v1.PostOldRequestsReq`
        """
        
        

        self._qabot_id = None
        self._body = None
        self.discriminator = None

        self.qabot_id = qabot_id
        if body is not None:
            self.body = body

    @property
    def qabot_id(self):
        r"""Gets the qabot_id of this PostRequestsRequest.

        qabot编号，UUID格式，如：303a0a00-c88a-43e3-aa2f-d5b8b9832b02。

        :return: The qabot_id of this PostRequestsRequest.
        :rtype: str
        """
        return self._qabot_id

    @qabot_id.setter
    def qabot_id(self, qabot_id):
        r"""Sets the qabot_id of this PostRequestsRequest.

        qabot编号，UUID格式，如：303a0a00-c88a-43e3-aa2f-d5b8b9832b02。

        :param qabot_id: The qabot_id of this PostRequestsRequest.
        :type qabot_id: str
        """
        self._qabot_id = qabot_id

    @property
    def body(self):
        r"""Gets the body of this PostRequestsRequest.

        :return: The body of this PostRequestsRequest.
        :rtype: :class:`huaweicloudsdkcbs.v1.PostOldRequestsReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this PostRequestsRequest.

        :param body: The body of this PostRequestsRequest.
        :type body: :class:`huaweicloudsdkcbs.v1.PostOldRequestsReq`
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
        if not isinstance(other, PostRequestsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
