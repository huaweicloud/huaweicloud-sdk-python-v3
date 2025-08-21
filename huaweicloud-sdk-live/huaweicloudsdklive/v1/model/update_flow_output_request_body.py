# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlowOutputRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cidr_whitelist': 'list[str]',
        'destination': 'str',
        'encryption': 'FlowSourceDecryption',
        'output_status': 'str',
        'port': 'int',
        'stream_id': 'str',
        'description': 'str',
        'min_latency': 'int'
    }

    attribute_map = {
        'cidr_whitelist': 'cidr_whitelist',
        'destination': 'destination',
        'encryption': 'encryption',
        'output_status': 'output_status',
        'port': 'port',
        'stream_id': 'stream_id',
        'description': 'description',
        'min_latency': 'min_latency'
    }

    def __init__(self, cidr_whitelist=None, destination=None, encryption=None, output_status=None, port=None, stream_id=None, description=None, min_latency=None):
        r"""UpdateFlowOutputRequestBody

        The model defined in huaweicloud sdk

        :param cidr_whitelist: ip白名单，最大20条ip白名单
        :type cidr_whitelist: list[str]
        :param destination: 推流地址，支持ip和域名，最大值64
        :type destination: str
        :param encryption: 
        :type encryption: :class:`huaweicloudsdklive.v1.FlowSourceDecryption`
        :param output_status: 输出状态，ENABLED：启用，DISABLED：禁用
        :type output_status: str
        :param port: 端口
        :type port: int
        :param stream_id: srt-caller模式支持设置streamid
        :type stream_id: str
        :param description: 输出描述
        :type description: str
        :param min_latency: 最小时延，单位毫秒，默认值2000，最小值10，最大值15000
        :type min_latency: int
        """
        
        

        self._cidr_whitelist = None
        self._destination = None
        self._encryption = None
        self._output_status = None
        self._port = None
        self._stream_id = None
        self._description = None
        self._min_latency = None
        self.discriminator = None

        if cidr_whitelist is not None:
            self.cidr_whitelist = cidr_whitelist
        if destination is not None:
            self.destination = destination
        if encryption is not None:
            self.encryption = encryption
        if output_status is not None:
            self.output_status = output_status
        if port is not None:
            self.port = port
        if stream_id is not None:
            self.stream_id = stream_id
        if description is not None:
            self.description = description
        if min_latency is not None:
            self.min_latency = min_latency

    @property
    def cidr_whitelist(self):
        r"""Gets the cidr_whitelist of this UpdateFlowOutputRequestBody.

        ip白名单，最大20条ip白名单

        :return: The cidr_whitelist of this UpdateFlowOutputRequestBody.
        :rtype: list[str]
        """
        return self._cidr_whitelist

    @cidr_whitelist.setter
    def cidr_whitelist(self, cidr_whitelist):
        r"""Sets the cidr_whitelist of this UpdateFlowOutputRequestBody.

        ip白名单，最大20条ip白名单

        :param cidr_whitelist: The cidr_whitelist of this UpdateFlowOutputRequestBody.
        :type cidr_whitelist: list[str]
        """
        self._cidr_whitelist = cidr_whitelist

    @property
    def destination(self):
        r"""Gets the destination of this UpdateFlowOutputRequestBody.

        推流地址，支持ip和域名，最大值64

        :return: The destination of this UpdateFlowOutputRequestBody.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this UpdateFlowOutputRequestBody.

        推流地址，支持ip和域名，最大值64

        :param destination: The destination of this UpdateFlowOutputRequestBody.
        :type destination: str
        """
        self._destination = destination

    @property
    def encryption(self):
        r"""Gets the encryption of this UpdateFlowOutputRequestBody.

        :return: The encryption of this UpdateFlowOutputRequestBody.
        :rtype: :class:`huaweicloudsdklive.v1.FlowSourceDecryption`
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        r"""Sets the encryption of this UpdateFlowOutputRequestBody.

        :param encryption: The encryption of this UpdateFlowOutputRequestBody.
        :type encryption: :class:`huaweicloudsdklive.v1.FlowSourceDecryption`
        """
        self._encryption = encryption

    @property
    def output_status(self):
        r"""Gets the output_status of this UpdateFlowOutputRequestBody.

        输出状态，ENABLED：启用，DISABLED：禁用

        :return: The output_status of this UpdateFlowOutputRequestBody.
        :rtype: str
        """
        return self._output_status

    @output_status.setter
    def output_status(self, output_status):
        r"""Sets the output_status of this UpdateFlowOutputRequestBody.

        输出状态，ENABLED：启用，DISABLED：禁用

        :param output_status: The output_status of this UpdateFlowOutputRequestBody.
        :type output_status: str
        """
        self._output_status = output_status

    @property
    def port(self):
        r"""Gets the port of this UpdateFlowOutputRequestBody.

        端口

        :return: The port of this UpdateFlowOutputRequestBody.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this UpdateFlowOutputRequestBody.

        端口

        :param port: The port of this UpdateFlowOutputRequestBody.
        :type port: int
        """
        self._port = port

    @property
    def stream_id(self):
        r"""Gets the stream_id of this UpdateFlowOutputRequestBody.

        srt-caller模式支持设置streamid

        :return: The stream_id of this UpdateFlowOutputRequestBody.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this UpdateFlowOutputRequestBody.

        srt-caller模式支持设置streamid

        :param stream_id: The stream_id of this UpdateFlowOutputRequestBody.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def description(self):
        r"""Gets the description of this UpdateFlowOutputRequestBody.

        输出描述

        :return: The description of this UpdateFlowOutputRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateFlowOutputRequestBody.

        输出描述

        :param description: The description of this UpdateFlowOutputRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def min_latency(self):
        r"""Gets the min_latency of this UpdateFlowOutputRequestBody.

        最小时延，单位毫秒，默认值2000，最小值10，最大值15000

        :return: The min_latency of this UpdateFlowOutputRequestBody.
        :rtype: int
        """
        return self._min_latency

    @min_latency.setter
    def min_latency(self, min_latency):
        r"""Sets the min_latency of this UpdateFlowOutputRequestBody.

        最小时延，单位毫秒，默认值2000，最小值10，最大值15000

        :param min_latency: The min_latency of this UpdateFlowOutputRequestBody.
        :type min_latency: int
        """
        self._min_latency = min_latency

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
        if not isinstance(other, UpdateFlowOutputRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
