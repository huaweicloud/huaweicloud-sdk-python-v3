# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchStopTransferTaskRequest:

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
        'body': 'BatchStopTransferTaskReq'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'body': 'body'
    }

    def __init__(self, stream_name=None, body=None):
        r"""BatchStopTransferTaskRequest

        The model defined in huaweicloud sdk

        :param stream_name: 需要查询的通道名称。
        :type stream_name: str
        :param body: Body of the BatchStopTransferTaskRequest
        :type body: :class:`huaweicloudsdkdis.v2.BatchStopTransferTaskReq`
        """
        
        

        self._stream_name = None
        self._body = None
        self.discriminator = None

        self.stream_name = stream_name
        if body is not None:
            self.body = body

    @property
    def stream_name(self):
        r"""Gets the stream_name of this BatchStopTransferTaskRequest.

        需要查询的通道名称。

        :return: The stream_name of this BatchStopTransferTaskRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this BatchStopTransferTaskRequest.

        需要查询的通道名称。

        :param stream_name: The stream_name of this BatchStopTransferTaskRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def body(self):
        r"""Gets the body of this BatchStopTransferTaskRequest.

        :return: The body of this BatchStopTransferTaskRequest.
        :rtype: :class:`huaweicloudsdkdis.v2.BatchStopTransferTaskReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchStopTransferTaskRequest.

        :param body: The body of this BatchStopTransferTaskRequest.
        :type body: :class:`huaweicloudsdkdis.v2.BatchStopTransferTaskReq`
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
        if not isinstance(other, BatchStopTransferTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
