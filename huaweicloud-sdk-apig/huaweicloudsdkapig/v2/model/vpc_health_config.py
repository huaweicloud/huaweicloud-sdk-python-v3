# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcHealthConfig:

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
        'path': 'str',
        'method': 'str',
        'port': 'int',
        'threshold_normal': 'int',
        'threshold_abnormal': 'int',
        'time_interval': 'int',
        'http_code': 'str',
        'enable_client_ssl': 'bool',
        'status': 'int',
        'timeout': 'int'
    }

    attribute_map = {
        'protocol': 'protocol',
        'path': 'path',
        'method': 'method',
        'port': 'port',
        'threshold_normal': 'threshold_normal',
        'threshold_abnormal': 'threshold_abnormal',
        'time_interval': 'time_interval',
        'http_code': 'http_code',
        'enable_client_ssl': 'enable_client_ssl',
        'status': 'status',
        'timeout': 'timeout'
    }

    def __init__(self, protocol=None, path=None, method=None, port=None, threshold_normal=None, threshold_abnormal=None, time_interval=None, http_code=None, enable_client_ssl=None, status=None, timeout=None):
        r"""VpcHealthConfig

        The model defined in huaweicloud sdk

        :param protocol: 使用以下协议，对VPC中主机执行健康检查： - TCP - HTTP - HTTPS
        :type protocol: str
        :param path: 健康检查时的目标路径。protocol &#x3D; http或https时必选
        :type path: str
        :param method: 健康检查时的请求方法
        :type method: str
        :param port: 健康检查的目标端口，缺少或port &#x3D; 0时为VPC中主机的端口号。  如果此端口存在非0值，则使用此端口进行健康检查。
        :type port: int
        :param threshold_normal: 正常阈值。判定VPC通道中主机正常的依据为：连续检查x成功，x为您设置的正常阈值。
        :type threshold_normal: int
        :param threshold_abnormal: 异常阈值。判定VPC通道中主机异常的依据为：连续检查x失败，x为您设置的异常阈值。
        :type threshold_abnormal: int
        :param time_interval: 间隔时间：连续两次检查的间隔时间，单位为秒。必须大于timeout字段取值。
        :type time_interval: int
        :param http_code: 检查目标HTTP响应时，判断成功使用的HTTP响应码。取值范围为100到599之前的任意整数值，支持如下三种格式： - 多个值，如：200,201,202 - 一系列值，如：200-299 - 组合值，如：201,202,210-299 protocol &#x3D; http时必选
        :type http_code: str
        :param enable_client_ssl: 是否开启双向认证。如果开启，则使用实例配置中的backend_client_certificate配置项的证书
        :type enable_client_ssl: bool
        :param status: 健康检查状态   - 1：可用   - 2：不可用
        :type status: int
        :param timeout: 超时时间：检查期间，无响应的时间，单位为秒。必须小于time_interval字段取值。
        :type timeout: int
        """
        
        

        self._protocol = None
        self._path = None
        self._method = None
        self._port = None
        self._threshold_normal = None
        self._threshold_abnormal = None
        self._time_interval = None
        self._http_code = None
        self._enable_client_ssl = None
        self._status = None
        self._timeout = None
        self.discriminator = None

        self.protocol = protocol
        if path is not None:
            self.path = path
        if method is not None:
            self.method = method
        if port is not None:
            self.port = port
        self.threshold_normal = threshold_normal
        self.threshold_abnormal = threshold_abnormal
        self.time_interval = time_interval
        if http_code is not None:
            self.http_code = http_code
        if enable_client_ssl is not None:
            self.enable_client_ssl = enable_client_ssl
        if status is not None:
            self.status = status
        if timeout is not None:
            self.timeout = timeout

    @property
    def protocol(self):
        r"""Gets the protocol of this VpcHealthConfig.

        使用以下协议，对VPC中主机执行健康检查： - TCP - HTTP - HTTPS

        :return: The protocol of this VpcHealthConfig.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this VpcHealthConfig.

        使用以下协议，对VPC中主机执行健康检查： - TCP - HTTP - HTTPS

        :param protocol: The protocol of this VpcHealthConfig.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def path(self):
        r"""Gets the path of this VpcHealthConfig.

        健康检查时的目标路径。protocol = http或https时必选

        :return: The path of this VpcHealthConfig.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this VpcHealthConfig.

        健康检查时的目标路径。protocol = http或https时必选

        :param path: The path of this VpcHealthConfig.
        :type path: str
        """
        self._path = path

    @property
    def method(self):
        r"""Gets the method of this VpcHealthConfig.

        健康检查时的请求方法

        :return: The method of this VpcHealthConfig.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this VpcHealthConfig.

        健康检查时的请求方法

        :param method: The method of this VpcHealthConfig.
        :type method: str
        """
        self._method = method

    @property
    def port(self):
        r"""Gets the port of this VpcHealthConfig.

        健康检查的目标端口，缺少或port = 0时为VPC中主机的端口号。  如果此端口存在非0值，则使用此端口进行健康检查。

        :return: The port of this VpcHealthConfig.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this VpcHealthConfig.

        健康检查的目标端口，缺少或port = 0时为VPC中主机的端口号。  如果此端口存在非0值，则使用此端口进行健康检查。

        :param port: The port of this VpcHealthConfig.
        :type port: int
        """
        self._port = port

    @property
    def threshold_normal(self):
        r"""Gets the threshold_normal of this VpcHealthConfig.

        正常阈值。判定VPC通道中主机正常的依据为：连续检查x成功，x为您设置的正常阈值。

        :return: The threshold_normal of this VpcHealthConfig.
        :rtype: int
        """
        return self._threshold_normal

    @threshold_normal.setter
    def threshold_normal(self, threshold_normal):
        r"""Sets the threshold_normal of this VpcHealthConfig.

        正常阈值。判定VPC通道中主机正常的依据为：连续检查x成功，x为您设置的正常阈值。

        :param threshold_normal: The threshold_normal of this VpcHealthConfig.
        :type threshold_normal: int
        """
        self._threshold_normal = threshold_normal

    @property
    def threshold_abnormal(self):
        r"""Gets the threshold_abnormal of this VpcHealthConfig.

        异常阈值。判定VPC通道中主机异常的依据为：连续检查x失败，x为您设置的异常阈值。

        :return: The threshold_abnormal of this VpcHealthConfig.
        :rtype: int
        """
        return self._threshold_abnormal

    @threshold_abnormal.setter
    def threshold_abnormal(self, threshold_abnormal):
        r"""Sets the threshold_abnormal of this VpcHealthConfig.

        异常阈值。判定VPC通道中主机异常的依据为：连续检查x失败，x为您设置的异常阈值。

        :param threshold_abnormal: The threshold_abnormal of this VpcHealthConfig.
        :type threshold_abnormal: int
        """
        self._threshold_abnormal = threshold_abnormal

    @property
    def time_interval(self):
        r"""Gets the time_interval of this VpcHealthConfig.

        间隔时间：连续两次检查的间隔时间，单位为秒。必须大于timeout字段取值。

        :return: The time_interval of this VpcHealthConfig.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        r"""Sets the time_interval of this VpcHealthConfig.

        间隔时间：连续两次检查的间隔时间，单位为秒。必须大于timeout字段取值。

        :param time_interval: The time_interval of this VpcHealthConfig.
        :type time_interval: int
        """
        self._time_interval = time_interval

    @property
    def http_code(self):
        r"""Gets the http_code of this VpcHealthConfig.

        检查目标HTTP响应时，判断成功使用的HTTP响应码。取值范围为100到599之前的任意整数值，支持如下三种格式： - 多个值，如：200,201,202 - 一系列值，如：200-299 - 组合值，如：201,202,210-299 protocol = http时必选

        :return: The http_code of this VpcHealthConfig.
        :rtype: str
        """
        return self._http_code

    @http_code.setter
    def http_code(self, http_code):
        r"""Sets the http_code of this VpcHealthConfig.

        检查目标HTTP响应时，判断成功使用的HTTP响应码。取值范围为100到599之前的任意整数值，支持如下三种格式： - 多个值，如：200,201,202 - 一系列值，如：200-299 - 组合值，如：201,202,210-299 protocol = http时必选

        :param http_code: The http_code of this VpcHealthConfig.
        :type http_code: str
        """
        self._http_code = http_code

    @property
    def enable_client_ssl(self):
        r"""Gets the enable_client_ssl of this VpcHealthConfig.

        是否开启双向认证。如果开启，则使用实例配置中的backend_client_certificate配置项的证书

        :return: The enable_client_ssl of this VpcHealthConfig.
        :rtype: bool
        """
        return self._enable_client_ssl

    @enable_client_ssl.setter
    def enable_client_ssl(self, enable_client_ssl):
        r"""Sets the enable_client_ssl of this VpcHealthConfig.

        是否开启双向认证。如果开启，则使用实例配置中的backend_client_certificate配置项的证书

        :param enable_client_ssl: The enable_client_ssl of this VpcHealthConfig.
        :type enable_client_ssl: bool
        """
        self._enable_client_ssl = enable_client_ssl

    @property
    def status(self):
        r"""Gets the status of this VpcHealthConfig.

        健康检查状态   - 1：可用   - 2：不可用

        :return: The status of this VpcHealthConfig.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VpcHealthConfig.

        健康检查状态   - 1：可用   - 2：不可用

        :param status: The status of this VpcHealthConfig.
        :type status: int
        """
        self._status = status

    @property
    def timeout(self):
        r"""Gets the timeout of this VpcHealthConfig.

        超时时间：检查期间，无响应的时间，单位为秒。必须小于time_interval字段取值。

        :return: The timeout of this VpcHealthConfig.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this VpcHealthConfig.

        超时时间：检查期间，无响应的时间，单位为秒。必须小于time_interval字段取值。

        :param timeout: The timeout of this VpcHealthConfig.
        :type timeout: int
        """
        self._timeout = timeout

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
        if not isinstance(other, VpcHealthConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
