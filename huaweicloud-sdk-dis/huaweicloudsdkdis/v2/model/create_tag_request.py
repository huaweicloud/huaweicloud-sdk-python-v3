# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_id': 'str',
        'body': 'CreateTagReq'
    }

    attribute_map = {
        'stream_id': 'stream_id',
        'body': 'body'
    }

    def __init__(self, stream_id=None, body=None):
        """CreateTagRequest

        The model defined in huaweicloud sdk

        :param stream_id: 通道ID。
        :type stream_id: str
        :param body: Body of the CreateTagRequest
        :type body: :class:`huaweicloudsdkdis.v2.CreateTagReq`
        """
        
        

        self._stream_id = None
        self._body = None
        self.discriminator = None

        self.stream_id = stream_id
        if body is not None:
            self.body = body

    @property
    def stream_id(self):
        """Gets the stream_id of this CreateTagRequest.

        通道ID。

        :return: The stream_id of this CreateTagRequest.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this CreateTagRequest.

        通道ID。

        :param stream_id: The stream_id of this CreateTagRequest.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def body(self):
        """Gets the body of this CreateTagRequest.

        :return: The body of this CreateTagRequest.
        :rtype: :class:`huaweicloudsdkdis.v2.CreateTagReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateTagRequest.

        :param body: The body of this CreateTagRequest.
        :type body: :class:`huaweicloudsdkdis.v2.CreateTagReq`
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
        if not isinstance(other, CreateTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
