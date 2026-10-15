# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLinkFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'engine_type': 'str',
        'job_type': 'str',
        'job_direction': 'str',
        'net_type': 'str',
        'node_type': 'str',
        'is_multi_write': 'bool'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'engine_type': 'engine_type',
        'job_type': 'job_type',
        'job_direction': 'job_direction',
        'net_type': 'net_type',
        'node_type': 'node_type',
        'is_multi_write': 'is_multi_write'
    }

    def __init__(self, x_language=None, engine_type=None, job_type=None, job_direction=None, net_type=None, node_type=None, is_multi_write=None):
        r"""ShowLinkFlavorsRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param engine_type: 引擎类型。
        :type engine_type: str
        :param job_type: 任务场景。取值：     - migration：实时迁移。     - sync：实时同步。     - cloudDataGuard：实时灾备。     - subscription：数据订阅。     - replay：录制回放。     - verify：校验任务。     - cdc：CDC任务。
        :type job_type: str
        :param job_direction: 任务方向。取值：     - up：入云 ，灾备场景时对应本云为备。     - down：出云，灾备场景时对应本云为主。     - non-dbs：自建。
        :type job_direction: str
        :param net_type: 网络类型。取值：     - eip：公网网络。     - vpc：VPC网络，灾备场景不支持选择VPC网络。     - vpn：VPN、专线网络。
        :type net_type: str
        :param node_type: 任务实例规格类型。取值：     - micro：极小规格。     - small：小规格。     - medium：中规格。     - high：大规格。     - xlarge：超大规格。     - 2xlarge：极大规格。
        :type node_type: str
        :param is_multi_write: 灾备类型是否双主灾备。说明：     - job_type 是cloudDataGuard时，必填，灾备类型是双主灾备时，is_multi_write取值true, 否则为false。     - job_type 是其他类型时，is_multi_write是非必选参数。
        :type is_multi_write: bool
        """
        
        

        self._x_language = None
        self._engine_type = None
        self._job_type = None
        self._job_direction = None
        self._net_type = None
        self._node_type = None
        self._is_multi_write = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if engine_type is not None:
            self.engine_type = engine_type
        if job_type is not None:
            self.job_type = job_type
        if job_direction is not None:
            self.job_direction = job_direction
        if net_type is not None:
            self.net_type = net_type
        if node_type is not None:
            self.node_type = node_type
        if is_multi_write is not None:
            self.is_multi_write = is_multi_write

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowLinkFlavorsRequest.

        请求语言类型。

        :return: The x_language of this ShowLinkFlavorsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowLinkFlavorsRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowLinkFlavorsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowLinkFlavorsRequest.

        引擎类型。

        :return: The engine_type of this ShowLinkFlavorsRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowLinkFlavorsRequest.

        引擎类型。

        :param engine_type: The engine_type of this ShowLinkFlavorsRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def job_type(self):
        r"""Gets the job_type of this ShowLinkFlavorsRequest.

        任务场景。取值：     - migration：实时迁移。     - sync：实时同步。     - cloudDataGuard：实时灾备。     - subscription：数据订阅。     - replay：录制回放。     - verify：校验任务。     - cdc：CDC任务。

        :return: The job_type of this ShowLinkFlavorsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ShowLinkFlavorsRequest.

        任务场景。取值：     - migration：实时迁移。     - sync：实时同步。     - cloudDataGuard：实时灾备。     - subscription：数据订阅。     - replay：录制回放。     - verify：校验任务。     - cdc：CDC任务。

        :param job_type: The job_type of this ShowLinkFlavorsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_direction(self):
        r"""Gets the job_direction of this ShowLinkFlavorsRequest.

        任务方向。取值：     - up：入云 ，灾备场景时对应本云为备。     - down：出云，灾备场景时对应本云为主。     - non-dbs：自建。

        :return: The job_direction of this ShowLinkFlavorsRequest.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        r"""Sets the job_direction of this ShowLinkFlavorsRequest.

        任务方向。取值：     - up：入云 ，灾备场景时对应本云为备。     - down：出云，灾备场景时对应本云为主。     - non-dbs：自建。

        :param job_direction: The job_direction of this ShowLinkFlavorsRequest.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def net_type(self):
        r"""Gets the net_type of this ShowLinkFlavorsRequest.

        网络类型。取值：     - eip：公网网络。     - vpc：VPC网络，灾备场景不支持选择VPC网络。     - vpn：VPN、专线网络。

        :return: The net_type of this ShowLinkFlavorsRequest.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        r"""Sets the net_type of this ShowLinkFlavorsRequest.

        网络类型。取值：     - eip：公网网络。     - vpc：VPC网络，灾备场景不支持选择VPC网络。     - vpn：VPN、专线网络。

        :param net_type: The net_type of this ShowLinkFlavorsRequest.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def node_type(self):
        r"""Gets the node_type of this ShowLinkFlavorsRequest.

        任务实例规格类型。取值：     - micro：极小规格。     - small：小规格。     - medium：中规格。     - high：大规格。     - xlarge：超大规格。     - 2xlarge：极大规格。

        :return: The node_type of this ShowLinkFlavorsRequest.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this ShowLinkFlavorsRequest.

        任务实例规格类型。取值：     - micro：极小规格。     - small：小规格。     - medium：中规格。     - high：大规格。     - xlarge：超大规格。     - 2xlarge：极大规格。

        :param node_type: The node_type of this ShowLinkFlavorsRequest.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def is_multi_write(self):
        r"""Gets the is_multi_write of this ShowLinkFlavorsRequest.

        灾备类型是否双主灾备。说明：     - job_type 是cloudDataGuard时，必填，灾备类型是双主灾备时，is_multi_write取值true, 否则为false。     - job_type 是其他类型时，is_multi_write是非必选参数。

        :return: The is_multi_write of this ShowLinkFlavorsRequest.
        :rtype: bool
        """
        return self._is_multi_write

    @is_multi_write.setter
    def is_multi_write(self, is_multi_write):
        r"""Sets the is_multi_write of this ShowLinkFlavorsRequest.

        灾备类型是否双主灾备。说明：     - job_type 是cloudDataGuard时，必填，灾备类型是双主灾备时，is_multi_write取值true, 否则为false。     - job_type 是其他类型时，is_multi_write是非必选参数。

        :param is_multi_write: The is_multi_write of this ShowLinkFlavorsRequest.
        :type is_multi_write: bool
        """
        self._is_multi_write = is_multi_write

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
        if not isinstance(other, ShowLinkFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
