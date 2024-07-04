# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddCustomIngressPortResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'ingress_port': 'int',
        'ingress_port_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'ingress_port': 'ingress_port',
        'ingress_port_id': 'ingress_port_id',
        'status': 'status'
    }

    def __init__(self, protocol=None, ingress_port=None, ingress_port_id=None, status=None):
        """AddCustomIngressPortResponse

        The model defined in huaweicloud sdk

        :param protocol: 实例自定义入方向端口协议。 - HTTP：实例自定义入方向端口使用HTTP协议。 - HTTPS：实例自定义入方向端口使用HTTPS协议。 
        :type protocol: str
        :param ingress_port: 实例自定义入方向端口，支持的端口范围为1024~49151。
        :type ingress_port: int
        :param ingress_port_id: 实例自定义入方向端口ID。
        :type ingress_port_id: str
        :param status: 实例自定义入方向端口的有效状态。 - normal：实例自定义入方向端口状态正常。 - abnormal：实例自定义入方向端口状态异常，无法使用。 
        :type status: str
        """
        
        super(AddCustomIngressPortResponse, self).__init__()

        self._protocol = None
        self._ingress_port = None
        self._ingress_port_id = None
        self._status = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol
        if ingress_port is not None:
            self.ingress_port = ingress_port
        if ingress_port_id is not None:
            self.ingress_port_id = ingress_port_id
        if status is not None:
            self.status = status

    @property
    def protocol(self):
        """Gets the protocol of this AddCustomIngressPortResponse.

        实例自定义入方向端口协议。 - HTTP：实例自定义入方向端口使用HTTP协议。 - HTTPS：实例自定义入方向端口使用HTTPS协议。 

        :return: The protocol of this AddCustomIngressPortResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this AddCustomIngressPortResponse.

        实例自定义入方向端口协议。 - HTTP：实例自定义入方向端口使用HTTP协议。 - HTTPS：实例自定义入方向端口使用HTTPS协议。 

        :param protocol: The protocol of this AddCustomIngressPortResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def ingress_port(self):
        """Gets the ingress_port of this AddCustomIngressPortResponse.

        实例自定义入方向端口，支持的端口范围为1024~49151。

        :return: The ingress_port of this AddCustomIngressPortResponse.
        :rtype: int
        """
        return self._ingress_port

    @ingress_port.setter
    def ingress_port(self, ingress_port):
        """Sets the ingress_port of this AddCustomIngressPortResponse.

        实例自定义入方向端口，支持的端口范围为1024~49151。

        :param ingress_port: The ingress_port of this AddCustomIngressPortResponse.
        :type ingress_port: int
        """
        self._ingress_port = ingress_port

    @property
    def ingress_port_id(self):
        """Gets the ingress_port_id of this AddCustomIngressPortResponse.

        实例自定义入方向端口ID。

        :return: The ingress_port_id of this AddCustomIngressPortResponse.
        :rtype: str
        """
        return self._ingress_port_id

    @ingress_port_id.setter
    def ingress_port_id(self, ingress_port_id):
        """Sets the ingress_port_id of this AddCustomIngressPortResponse.

        实例自定义入方向端口ID。

        :param ingress_port_id: The ingress_port_id of this AddCustomIngressPortResponse.
        :type ingress_port_id: str
        """
        self._ingress_port_id = ingress_port_id

    @property
    def status(self):
        """Gets the status of this AddCustomIngressPortResponse.

        实例自定义入方向端口的有效状态。 - normal：实例自定义入方向端口状态正常。 - abnormal：实例自定义入方向端口状态异常，无法使用。 

        :return: The status of this AddCustomIngressPortResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AddCustomIngressPortResponse.

        实例自定义入方向端口的有效状态。 - normal：实例自定义入方向端口状态正常。 - abnormal：实例自定义入方向端口状态异常，无法使用。 

        :param status: The status of this AddCustomIngressPortResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, AddCustomIngressPortResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
