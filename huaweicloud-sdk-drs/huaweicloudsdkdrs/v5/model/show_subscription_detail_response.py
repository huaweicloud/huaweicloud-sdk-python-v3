# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubscriptionDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'ip': 'str',
        'enterprise_project_id': 'str',
        'status': 'str',
        'subscription_data_type': 'SubscriptionDataType',
        'source_endpoint': 'SubscriptionEndpointInfo',
        'created_time': 'str',
        'begin_time': 'str',
        'now_time': 'str',
        'engine_type': 'str',
        'charge_info': 'ChargeInfoVo',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ip': 'ip',
        'enterprise_project_id': 'enterprise_project_id',
        'status': 'status',
        'subscription_data_type': 'subscription_data_type',
        'source_endpoint': 'source_endpoint',
        'created_time': 'created_time',
        'begin_time': 'begin_time',
        'now_time': 'now_time',
        'engine_type': 'engine_type',
        'charge_info': 'charge_info',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, ip=None, enterprise_project_id=None, status=None, subscription_data_type=None, source_endpoint=None, created_time=None, begin_time=None, now_time=None, engine_type=None, charge_info=None, description=None):
        r"""ShowSubscriptionDetailResponse

        The model defined in huaweicloud sdk

        :param id: 任务id
        :type id: str
        :param name: 任务名称 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50
        :type name: str
        :param ip: 内网ip
        :type ip: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param status: 任务状态，取值： CONFIGURATION：配置中 CREATING：创建中 CREATE_FAILED：创建失败 STARTJOBING：启动中 STARTJOB_FAILED：任务启动失败 SUBSCRIPTION_STARTED：正常 SUBSCRIPTION_FAILED：异常 DELETED：已删除 FROZEN：冻结状态 REBUILD_NODE_STARTED：订阅任务恢复中 REBUILD_NODE_FAILED：订阅任务恢复失败 NODE_UPGRADE_START：升级开始 NODE_UPGRADE_COMPLETE：升级完成 NODE_UPGRADE_FAILED：升级失败
        :type status: str
        :param subscription_data_type: 
        :type subscription_data_type: :class:`huaweicloudsdkdrs.v5.SubscriptionDataType`
        :param source_endpoint: 
        :type source_endpoint: :class:`huaweicloudsdkdrs.v5.SubscriptionEndpointInfo`
        :param created_time: 创建时间，以时间戳表示
        :type created_time: str
        :param begin_time: 开始时间，以时间戳表示
        :type begin_time: str
        :param now_time: 当前时间，以时间戳表示
        :type now_time: str
        :param engine_type: 链路类型，当前仅支持“mysql”
        :type engine_type: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkdrs.v5.ChargeInfoVo`
        :param description: 描述
        :type description: str
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._ip = None
        self._enterprise_project_id = None
        self._status = None
        self._subscription_data_type = None
        self._source_endpoint = None
        self._created_time = None
        self._begin_time = None
        self._now_time = None
        self._engine_type = None
        self._charge_info = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ip is not None:
            self.ip = ip
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if status is not None:
            self.status = status
        if subscription_data_type is not None:
            self.subscription_data_type = subscription_data_type
        if source_endpoint is not None:
            self.source_endpoint = source_endpoint
        if created_time is not None:
            self.created_time = created_time
        if begin_time is not None:
            self.begin_time = begin_time
        if now_time is not None:
            self.now_time = now_time
        if engine_type is not None:
            self.engine_type = engine_type
        if charge_info is not None:
            self.charge_info = charge_info
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this ShowSubscriptionDetailResponse.

        任务id

        :return: The id of this ShowSubscriptionDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSubscriptionDetailResponse.

        任务id

        :param id: The id of this ShowSubscriptionDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowSubscriptionDetailResponse.

        任务名称 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50

        :return: The name of this ShowSubscriptionDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowSubscriptionDetailResponse.

        任务名称 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50

        :param name: The name of this ShowSubscriptionDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def ip(self):
        r"""Gets the ip of this ShowSubscriptionDetailResponse.

        内网ip

        :return: The ip of this ShowSubscriptionDetailResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ShowSubscriptionDetailResponse.

        内网ip

        :param ip: The ip of this ShowSubscriptionDetailResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowSubscriptionDetailResponse.

        企业项目id

        :return: The enterprise_project_id of this ShowSubscriptionDetailResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowSubscriptionDetailResponse.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ShowSubscriptionDetailResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def status(self):
        r"""Gets the status of this ShowSubscriptionDetailResponse.

        任务状态，取值： CONFIGURATION：配置中 CREATING：创建中 CREATE_FAILED：创建失败 STARTJOBING：启动中 STARTJOB_FAILED：任务启动失败 SUBSCRIPTION_STARTED：正常 SUBSCRIPTION_FAILED：异常 DELETED：已删除 FROZEN：冻结状态 REBUILD_NODE_STARTED：订阅任务恢复中 REBUILD_NODE_FAILED：订阅任务恢复失败 NODE_UPGRADE_START：升级开始 NODE_UPGRADE_COMPLETE：升级完成 NODE_UPGRADE_FAILED：升级失败

        :return: The status of this ShowSubscriptionDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSubscriptionDetailResponse.

        任务状态，取值： CONFIGURATION：配置中 CREATING：创建中 CREATE_FAILED：创建失败 STARTJOBING：启动中 STARTJOB_FAILED：任务启动失败 SUBSCRIPTION_STARTED：正常 SUBSCRIPTION_FAILED：异常 DELETED：已删除 FROZEN：冻结状态 REBUILD_NODE_STARTED：订阅任务恢复中 REBUILD_NODE_FAILED：订阅任务恢复失败 NODE_UPGRADE_START：升级开始 NODE_UPGRADE_COMPLETE：升级完成 NODE_UPGRADE_FAILED：升级失败

        :param status: The status of this ShowSubscriptionDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def subscription_data_type(self):
        r"""Gets the subscription_data_type of this ShowSubscriptionDetailResponse.

        :return: The subscription_data_type of this ShowSubscriptionDetailResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.SubscriptionDataType`
        """
        return self._subscription_data_type

    @subscription_data_type.setter
    def subscription_data_type(self, subscription_data_type):
        r"""Sets the subscription_data_type of this ShowSubscriptionDetailResponse.

        :param subscription_data_type: The subscription_data_type of this ShowSubscriptionDetailResponse.
        :type subscription_data_type: :class:`huaweicloudsdkdrs.v5.SubscriptionDataType`
        """
        self._subscription_data_type = subscription_data_type

    @property
    def source_endpoint(self):
        r"""Gets the source_endpoint of this ShowSubscriptionDetailResponse.

        :return: The source_endpoint of this ShowSubscriptionDetailResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.SubscriptionEndpointInfo`
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        r"""Sets the source_endpoint of this ShowSubscriptionDetailResponse.

        :param source_endpoint: The source_endpoint of this ShowSubscriptionDetailResponse.
        :type source_endpoint: :class:`huaweicloudsdkdrs.v5.SubscriptionEndpointInfo`
        """
        self._source_endpoint = source_endpoint

    @property
    def created_time(self):
        r"""Gets the created_time of this ShowSubscriptionDetailResponse.

        创建时间，以时间戳表示

        :return: The created_time of this ShowSubscriptionDetailResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ShowSubscriptionDetailResponse.

        创建时间，以时间戳表示

        :param created_time: The created_time of this ShowSubscriptionDetailResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowSubscriptionDetailResponse.

        开始时间，以时间戳表示

        :return: The begin_time of this ShowSubscriptionDetailResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowSubscriptionDetailResponse.

        开始时间，以时间戳表示

        :param begin_time: The begin_time of this ShowSubscriptionDetailResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def now_time(self):
        r"""Gets the now_time of this ShowSubscriptionDetailResponse.

        当前时间，以时间戳表示

        :return: The now_time of this ShowSubscriptionDetailResponse.
        :rtype: str
        """
        return self._now_time

    @now_time.setter
    def now_time(self, now_time):
        r"""Sets the now_time of this ShowSubscriptionDetailResponse.

        当前时间，以时间戳表示

        :param now_time: The now_time of this ShowSubscriptionDetailResponse.
        :type now_time: str
        """
        self._now_time = now_time

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowSubscriptionDetailResponse.

        链路类型，当前仅支持“mysql”

        :return: The engine_type of this ShowSubscriptionDetailResponse.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowSubscriptionDetailResponse.

        链路类型，当前仅支持“mysql”

        :param engine_type: The engine_type of this ShowSubscriptionDetailResponse.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def charge_info(self):
        r"""Gets the charge_info of this ShowSubscriptionDetailResponse.

        :return: The charge_info of this ShowSubscriptionDetailResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.ChargeInfoVo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this ShowSubscriptionDetailResponse.

        :param charge_info: The charge_info of this ShowSubscriptionDetailResponse.
        :type charge_info: :class:`huaweicloudsdkdrs.v5.ChargeInfoVo`
        """
        self._charge_info = charge_info

    @property
    def description(self):
        r"""Gets the description of this ShowSubscriptionDetailResponse.

        描述

        :return: The description of this ShowSubscriptionDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowSubscriptionDetailResponse.

        描述

        :param description: The description of this ShowSubscriptionDetailResponse.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        import warnings
        warnings.warn("ShowSubscriptionDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowSubscriptionDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
