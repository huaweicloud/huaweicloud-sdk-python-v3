# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatasourceConnectionResponse(SdkResponse):

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
        'connection_id': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'connection_id': 'connection_id'
    }

    def __init__(self, is_success=None, message=None, connection_id=None):
        r"""CreateDatasourceConnectionResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param connection_id: 连接ID，用于标识跨源连接的UUID。
        :type connection_id: str
        """
        
        super(CreateDatasourceConnectionResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._connection_id = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if connection_id is not None:
            self.connection_id = connection_id

    @property
    def is_success(self):
        r"""Gets the is_success of this CreateDatasourceConnectionResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this CreateDatasourceConnectionResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this CreateDatasourceConnectionResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this CreateDatasourceConnectionResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this CreateDatasourceConnectionResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this CreateDatasourceConnectionResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateDatasourceConnectionResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this CreateDatasourceConnectionResponse.
        :type message: str
        """
        self._message = message

    @property
    def connection_id(self):
        r"""Gets the connection_id of this CreateDatasourceConnectionResponse.

        连接ID，用于标识跨源连接的UUID。

        :return: The connection_id of this CreateDatasourceConnectionResponse.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this CreateDatasourceConnectionResponse.

        连接ID，用于标识跨源连接的UUID。

        :param connection_id: The connection_id of this CreateDatasourceConnectionResponse.
        :type connection_id: str
        """
        self._connection_id = connection_id

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
        if not isinstance(other, CreateDatasourceConnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
