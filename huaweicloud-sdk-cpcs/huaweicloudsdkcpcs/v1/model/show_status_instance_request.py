# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatusInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'app_id': 'str',
        'instance_id': 'str',
        '_from': 'int',
        'to': 'int',
        'period': 'int',
        'filter': 'str',
        'server_type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'app_id': 'app_id',
        'instance_id': 'instance_id',
        '_from': 'from',
        'to': 'to',
        'period': 'period',
        'filter': 'filter',
        'server_type': 'server_type'
    }

    def __init__(self, cluster_id=None, app_id=None, instance_id=None, _from=None, to=None, period=None, filter=None, server_type=None):
        r"""ShowStatusInstanceRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，默认空字符串，默认查询所有集群。
        :type cluster_id: str
        :param app_id: 应用ID，默认空字符串，默认查询所有应用。
        :type app_id: str
        :param instance_id: 集群ID，默认空字符串，默认查询所有集群。
        :type instance_id: str
        :param _from: 查询范围起始时间，毫秒时间戳，默认为0，默认查询三天前。
        :type _from: int
        :param to: 查询范围终止时间，毫秒时间戳，默认为0，默认查询到当前时间。
        :type to: int
        :param period: 数据统计周期，默认0，默认为5分钟。
        :type period: int
        :param filter: 统计类型，默认min，默认用统计周期中数据的最小值。
        :type filter: str
        :param server_type: 服务类型，默认空字符串，默认查询所有服务类型。
        :type server_type: str
        """
        
        

        self._cluster_id = None
        self._app_id = None
        self._instance_id = None
        self.__from = None
        self._to = None
        self._period = None
        self._filter = None
        self._server_type = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if app_id is not None:
            self.app_id = app_id
        if instance_id is not None:
            self.instance_id = instance_id
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if period is not None:
            self.period = period
        if filter is not None:
            self.filter = filter
        if server_type is not None:
            self.server_type = server_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowStatusInstanceRequest.

        集群ID，默认空字符串，默认查询所有集群。

        :return: The cluster_id of this ShowStatusInstanceRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowStatusInstanceRequest.

        集群ID，默认空字符串，默认查询所有集群。

        :param cluster_id: The cluster_id of this ShowStatusInstanceRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowStatusInstanceRequest.

        应用ID，默认空字符串，默认查询所有应用。

        :return: The app_id of this ShowStatusInstanceRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowStatusInstanceRequest.

        应用ID，默认空字符串，默认查询所有应用。

        :param app_id: The app_id of this ShowStatusInstanceRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowStatusInstanceRequest.

        集群ID，默认空字符串，默认查询所有集群。

        :return: The instance_id of this ShowStatusInstanceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowStatusInstanceRequest.

        集群ID，默认空字符串，默认查询所有集群。

        :param instance_id: The instance_id of this ShowStatusInstanceRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def _from(self):
        r"""Gets the _from of this ShowStatusInstanceRequest.

        查询范围起始时间，毫秒时间戳，默认为0，默认查询三天前。

        :return: The _from of this ShowStatusInstanceRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowStatusInstanceRequest.

        查询范围起始时间，毫秒时间戳，默认为0，默认查询三天前。

        :param _from: The _from of this ShowStatusInstanceRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ShowStatusInstanceRequest.

        查询范围终止时间，毫秒时间戳，默认为0，默认查询到当前时间。

        :return: The to of this ShowStatusInstanceRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ShowStatusInstanceRequest.

        查询范围终止时间，毫秒时间戳，默认为0，默认查询到当前时间。

        :param to: The to of this ShowStatusInstanceRequest.
        :type to: int
        """
        self._to = to

    @property
    def period(self):
        r"""Gets the period of this ShowStatusInstanceRequest.

        数据统计周期，默认0，默认为5分钟。

        :return: The period of this ShowStatusInstanceRequest.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this ShowStatusInstanceRequest.

        数据统计周期，默认0，默认为5分钟。

        :param period: The period of this ShowStatusInstanceRequest.
        :type period: int
        """
        self._period = period

    @property
    def filter(self):
        r"""Gets the filter of this ShowStatusInstanceRequest.

        统计类型，默认min，默认用统计周期中数据的最小值。

        :return: The filter of this ShowStatusInstanceRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ShowStatusInstanceRequest.

        统计类型，默认min，默认用统计周期中数据的最小值。

        :param filter: The filter of this ShowStatusInstanceRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def server_type(self):
        r"""Gets the server_type of this ShowStatusInstanceRequest.

        服务类型，默认空字符串，默认查询所有服务类型。

        :return: The server_type of this ShowStatusInstanceRequest.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ShowStatusInstanceRequest.

        服务类型，默认空字符串，默认查询所有服务类型。

        :param server_type: The server_type of this ShowStatusInstanceRequest.
        :type server_type: str
        """
        self._server_type = server_type

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
        if not isinstance(other, ShowStatusInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
