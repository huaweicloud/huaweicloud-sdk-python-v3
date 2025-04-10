# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConnectivityTaskResponse(SdkResponse):

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
        'connectivity': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'connectivity': 'connectivity'
    }

    def __init__(self, is_success=None, message=None, connectivity=None):
        r"""ShowConnectivityTaskResponse

        The model defined in huaweicloud sdk

        :param is_success: 请求发送是否成功。“true”表示请求发送成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param connectivity: 连通性测试结果
        :type connectivity: str
        """
        
        super(ShowConnectivityTaskResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._connectivity = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if connectivity is not None:
            self.connectivity = connectivity

    @property
    def is_success(self):
        r"""Gets the is_success of this ShowConnectivityTaskResponse.

        请求发送是否成功。“true”表示请求发送成功。

        :return: The is_success of this ShowConnectivityTaskResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ShowConnectivityTaskResponse.

        请求发送是否成功。“true”表示请求发送成功。

        :param is_success: The is_success of this ShowConnectivityTaskResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ShowConnectivityTaskResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ShowConnectivityTaskResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowConnectivityTaskResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ShowConnectivityTaskResponse.
        :type message: str
        """
        self._message = message

    @property
    def connectivity(self):
        r"""Gets the connectivity of this ShowConnectivityTaskResponse.

        连通性测试结果

        :return: The connectivity of this ShowConnectivityTaskResponse.
        :rtype: str
        """
        return self._connectivity

    @connectivity.setter
    def connectivity(self, connectivity):
        r"""Sets the connectivity of this ShowConnectivityTaskResponse.

        连通性测试结果

        :param connectivity: The connectivity of this ShowConnectivityTaskResponse.
        :type connectivity: str
        """
        self._connectivity = connectivity

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
        if not isinstance(other, ShowConnectivityTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
