# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTagRequest:

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
        'key': 'str'
    }

    attribute_map = {
        'stream_id': 'stream_id',
        'key': 'key'
    }

    def __init__(self, stream_id=None, key=None):
        r"""DeleteTagRequest

        The model defined in huaweicloud sdk

        :param stream_id: 通道ID。
        :type stream_id: str
        :param key: 标签键。
        :type key: str
        """
        
        

        self._stream_id = None
        self._key = None
        self.discriminator = None

        self.stream_id = stream_id
        self.key = key

    @property
    def stream_id(self):
        r"""Gets the stream_id of this DeleteTagRequest.

        通道ID。

        :return: The stream_id of this DeleteTagRequest.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this DeleteTagRequest.

        通道ID。

        :param stream_id: The stream_id of this DeleteTagRequest.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def key(self):
        r"""Gets the key of this DeleteTagRequest.

        标签键。

        :return: The key of this DeleteTagRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this DeleteTagRequest.

        标签键。

        :param key: The key of this DeleteTagRequest.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, DeleteTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
