# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerConsoleOutputRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'length': 'int'
    }

    attribute_map = {
        'server_id': 'server_id',
        'length': 'length'
    }

    def __init__(self, server_id=None, length=None):
        r"""ShowServerConsoleOutputRequest

        The model defined in huaweicloud sdk

        :param server_id: 云服务器ID。
        :type server_id: str
        :param length: - 参数解释： 请求log行数。 - 约束限制： 不涉及。 - 取值范围： 大于等于-1。其中-1代表不限长度输出。 - 默认取值： 不填时默认50。
        :type length: int
        """
        
        

        self._server_id = None
        self._length = None
        self.discriminator = None

        self.server_id = server_id
        if length is not None:
            self.length = length

    @property
    def server_id(self):
        r"""Gets the server_id of this ShowServerConsoleOutputRequest.

        云服务器ID。

        :return: The server_id of this ShowServerConsoleOutputRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ShowServerConsoleOutputRequest.

        云服务器ID。

        :param server_id: The server_id of this ShowServerConsoleOutputRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def length(self):
        r"""Gets the length of this ShowServerConsoleOutputRequest.

        - 参数解释： 请求log行数。 - 约束限制： 不涉及。 - 取值范围： 大于等于-1。其中-1代表不限长度输出。 - 默认取值： 不填时默认50。

        :return: The length of this ShowServerConsoleOutputRequest.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        r"""Sets the length of this ShowServerConsoleOutputRequest.

        - 参数解释： 请求log行数。 - 约束限制： 不涉及。 - 取值范围： 大于等于-1。其中-1代表不限长度输出。 - 默认取值： 不填时默认50。

        :param length: The length of this ShowServerConsoleOutputRequest.
        :type length: int
        """
        self._length = length

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
        if not isinstance(other, ShowServerConsoleOutputRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
