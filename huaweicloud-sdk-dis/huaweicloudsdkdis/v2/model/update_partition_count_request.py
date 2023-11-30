# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePartitionCountRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'body': 'UpdatePartitionCountReq'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'body': 'body'
    }

    def __init__(self, stream_name=None, body=None):
        """UpdatePartitionCountRequest

        The model defined in huaweicloud sdk

        :param stream_name: 需要变更分区数量的通道名称。
        :type stream_name: str
        :param body: Body of the UpdatePartitionCountRequest
        :type body: :class:`huaweicloudsdkdis.v2.UpdatePartitionCountReq`
        """
        
        

        self._stream_name = None
        self._body = None
        self.discriminator = None

        self.stream_name = stream_name
        if body is not None:
            self.body = body

    @property
    def stream_name(self):
        """Gets the stream_name of this UpdatePartitionCountRequest.

        需要变更分区数量的通道名称。

        :return: The stream_name of this UpdatePartitionCountRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this UpdatePartitionCountRequest.

        需要变更分区数量的通道名称。

        :param stream_name: The stream_name of this UpdatePartitionCountRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def body(self):
        """Gets the body of this UpdatePartitionCountRequest.

        :return: The body of this UpdatePartitionCountRequest.
        :rtype: :class:`huaweicloudsdkdis.v2.UpdatePartitionCountReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdatePartitionCountRequest.

        :param body: The body of this UpdatePartitionCountRequest.
        :type body: :class:`huaweicloudsdkdis.v2.UpdatePartitionCountReq`
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
        if not isinstance(other, UpdatePartitionCountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
