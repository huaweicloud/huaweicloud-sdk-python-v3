# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlinkSqlJobGraphResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'error_code': 'str',
        'stream_graph': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'error_code': 'error_code',
        'stream_graph': 'stream_graph'
    }

    def __init__(self, is_success=None, message=None, error_code=None, stream_graph=None):
        r"""CreateFlinkSqlJobGraphResponse

        The model defined in huaweicloud sdk

        :param is_success: 
        :type is_success: bool
        :param message: 
        :type message: str
        :param error_code: 
        :type error_code: str
        :param stream_graph: 静态流图的描述信息
        :type stream_graph: str
        """
        
        super(CreateFlinkSqlJobGraphResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._error_code = None
        self._stream_graph = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if error_code is not None:
            self.error_code = error_code
        if stream_graph is not None:
            self.stream_graph = stream_graph

    @property
    def is_success(self):
        r"""Gets the is_success of this CreateFlinkSqlJobGraphResponse.

        :return: The is_success of this CreateFlinkSqlJobGraphResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this CreateFlinkSqlJobGraphResponse.

        :param is_success: The is_success of this CreateFlinkSqlJobGraphResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this CreateFlinkSqlJobGraphResponse.

        :return: The message of this CreateFlinkSqlJobGraphResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateFlinkSqlJobGraphResponse.

        :param message: The message of this CreateFlinkSqlJobGraphResponse.
        :type message: str
        """
        self._message = message

    @property
    def error_code(self):
        r"""Gets the error_code of this CreateFlinkSqlJobGraphResponse.

        :return: The error_code of this CreateFlinkSqlJobGraphResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this CreateFlinkSqlJobGraphResponse.

        :param error_code: The error_code of this CreateFlinkSqlJobGraphResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def stream_graph(self):
        r"""Gets the stream_graph of this CreateFlinkSqlJobGraphResponse.

        静态流图的描述信息

        :return: The stream_graph of this CreateFlinkSqlJobGraphResponse.
        :rtype: str
        """
        return self._stream_graph

    @stream_graph.setter
    def stream_graph(self, stream_graph):
        r"""Sets the stream_graph of this CreateFlinkSqlJobGraphResponse.

        静态流图的描述信息

        :param stream_graph: The stream_graph of this CreateFlinkSqlJobGraphResponse.
        :type stream_graph: str
        """
        self._stream_graph = stream_graph

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
        if not isinstance(other, CreateFlinkSqlJobGraphResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
