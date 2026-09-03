# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchBinlogParseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'body': 'SearchBinlogParseRequestBody'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'body': 'body'
    }

    def __init__(self, connection_id=None, body=None):
        r"""SearchBinlogParseRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param body: Body of the SearchBinlogParseRequest
        :type body: :class:`huaweicloudsdkdas.v3.SearchBinlogParseRequestBody`
        """
        
        

        self._connection_id = None
        self._body = None
        self.discriminator = None

        self.connection_id = connection_id
        if body is not None:
            self.body = body

    @property
    def connection_id(self):
        r"""Gets the connection_id of this SearchBinlogParseRequest.

        连接ID

        :return: The connection_id of this SearchBinlogParseRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this SearchBinlogParseRequest.

        连接ID

        :param connection_id: The connection_id of this SearchBinlogParseRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def body(self):
        r"""Gets the body of this SearchBinlogParseRequest.

        :return: The body of this SearchBinlogParseRequest.
        :rtype: :class:`huaweicloudsdkdas.v3.SearchBinlogParseRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SearchBinlogParseRequest.

        :param body: The body of this SearchBinlogParseRequest.
        :type body: :class:`huaweicloudsdkdas.v3.SearchBinlogParseRequestBody`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchBinlogParseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
