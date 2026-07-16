# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopHyperinstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_at': 'int',
        'hps_cluster_id': 'str',
        'hps_id': 'str',
        'id': 'str',
        'name': 'str',
        'order_id': 'str',
        'status': 'str',
        'servers': 'list[ServerResponse]',
        'update_at': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'create_at': 'create_at',
        'hps_cluster_id': 'hps_cluster_id',
        'hps_id': 'hps_id',
        'id': 'id',
        'name': 'name',
        'order_id': 'order_id',
        'status': 'status',
        'servers': 'servers',
        'update_at': 'update_at',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, create_at=None, hps_cluster_id=None, hps_id=None, id=None, name=None, order_id=None, status=None, servers=None, update_at=None, x_request_id=None):
        r"""StopHyperinstanceResponse

        The model defined in huaweicloud sdk

        :param create_at: **参数解释**：创建时间。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type create_at: int
        :param hps_cluster_id: **参数解释**：超节点集群网络ID。 **约束限制**：不涉及。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **默认取值**：不涉及。
        :type hps_cluster_id: str
        :param hps_id: **参数解释**：超节点ID。 **约束限制**：不涉及。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **默认取值**：不涉及。
        :type hps_id: str
        :param id: **参数解释**：Lite Server超节点ID。 **约束限制**：不涉及。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **默认取值**：不涉及。
        :type id: str
        :param name: **参数解释**：实例名称。 **约束限制**：不涉及。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。 **默认取值**：不涉及。
        :type name: str
        :param order_id: **参数解释**：订单ID。 **约束限制**：不涉及。 **取值范围**：^[a-zA-Z0-9]{1,64}$。 **默认取值**：不涉及。
        :type order_id: str
        :param status: **参数解释**：超节点实例状态。 **约束限制**：不涉及。 **取值范围**： - PROVISIONING：超节点的创建请求已被接受，但是仍在创建过程中； - ACTIVE：超节点处于活动状态，其资源可被使用； - ERROR：超节点创建失败； - REIMAGING：超节点切换操作系统中； - TERMINATING：资源释放中； - TERMINATED：超节点资源已经被释放，其资源不再可用。 **默认取值**：不涉及。
        :type status: str
        :param servers: **参数解释**：超节点子节点实例列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type servers: list[:class:`huaweicloudsdkmodelarts.v1.ServerResponse`]
        :param update_at: **参数解释**：创建时间。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type update_at: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._create_at = None
        self._hps_cluster_id = None
        self._hps_id = None
        self._id = None
        self._name = None
        self._order_id = None
        self._status = None
        self._servers = None
        self._update_at = None
        self._x_request_id = None
        self.discriminator = None

        if create_at is not None:
            self.create_at = create_at
        if hps_cluster_id is not None:
            self.hps_cluster_id = hps_cluster_id
        if hps_id is not None:
            self.hps_id = hps_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status
        if servers is not None:
            self.servers = servers
        if update_at is not None:
            self.update_at = update_at
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def create_at(self):
        r"""Gets the create_at of this StopHyperinstanceResponse.

        **参数解释**：创建时间。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The create_at of this StopHyperinstanceResponse.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this StopHyperinstanceResponse.

        **参数解释**：创建时间。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param create_at: The create_at of this StopHyperinstanceResponse.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def hps_cluster_id(self):
        r"""Gets the hps_cluster_id of this StopHyperinstanceResponse.

        **参数解释**：超节点集群网络ID。 **约束限制**：不涉及。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **默认取值**：不涉及。

        :return: The hps_cluster_id of this StopHyperinstanceResponse.
        :rtype: str
        """
        return self._hps_cluster_id

    @hps_cluster_id.setter
    def hps_cluster_id(self, hps_cluster_id):
        r"""Sets the hps_cluster_id of this StopHyperinstanceResponse.

        **参数解释**：超节点集群网络ID。 **约束限制**：不涉及。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **默认取值**：不涉及。

        :param hps_cluster_id: The hps_cluster_id of this StopHyperinstanceResponse.
        :type hps_cluster_id: str
        """
        self._hps_cluster_id = hps_cluster_id

    @property
    def hps_id(self):
        r"""Gets the hps_id of this StopHyperinstanceResponse.

        **参数解释**：超节点ID。 **约束限制**：不涉及。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **默认取值**：不涉及。

        :return: The hps_id of this StopHyperinstanceResponse.
        :rtype: str
        """
        return self._hps_id

    @hps_id.setter
    def hps_id(self, hps_id):
        r"""Sets the hps_id of this StopHyperinstanceResponse.

        **参数解释**：超节点ID。 **约束限制**：不涉及。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **默认取值**：不涉及。

        :param hps_id: The hps_id of this StopHyperinstanceResponse.
        :type hps_id: str
        """
        self._hps_id = hps_id

    @property
    def id(self):
        r"""Gets the id of this StopHyperinstanceResponse.

        **参数解释**：Lite Server超节点ID。 **约束限制**：不涉及。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **默认取值**：不涉及。

        :return: The id of this StopHyperinstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StopHyperinstanceResponse.

        **参数解释**：Lite Server超节点ID。 **约束限制**：不涉及。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **默认取值**：不涉及。

        :param id: The id of this StopHyperinstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this StopHyperinstanceResponse.

        **参数解释**：实例名称。 **约束限制**：不涉及。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。 **默认取值**：不涉及。

        :return: The name of this StopHyperinstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StopHyperinstanceResponse.

        **参数解释**：实例名称。 **约束限制**：不涉及。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。 **默认取值**：不涉及。

        :param name: The name of this StopHyperinstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def order_id(self):
        r"""Gets the order_id of this StopHyperinstanceResponse.

        **参数解释**：订单ID。 **约束限制**：不涉及。 **取值范围**：^[a-zA-Z0-9]{1,64}$。 **默认取值**：不涉及。

        :return: The order_id of this StopHyperinstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this StopHyperinstanceResponse.

        **参数解释**：订单ID。 **约束限制**：不涉及。 **取值范围**：^[a-zA-Z0-9]{1,64}$。 **默认取值**：不涉及。

        :param order_id: The order_id of this StopHyperinstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def status(self):
        r"""Gets the status of this StopHyperinstanceResponse.

        **参数解释**：超节点实例状态。 **约束限制**：不涉及。 **取值范围**： - PROVISIONING：超节点的创建请求已被接受，但是仍在创建过程中； - ACTIVE：超节点处于活动状态，其资源可被使用； - ERROR：超节点创建失败； - REIMAGING：超节点切换操作系统中； - TERMINATING：资源释放中； - TERMINATED：超节点资源已经被释放，其资源不再可用。 **默认取值**：不涉及。

        :return: The status of this StopHyperinstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StopHyperinstanceResponse.

        **参数解释**：超节点实例状态。 **约束限制**：不涉及。 **取值范围**： - PROVISIONING：超节点的创建请求已被接受，但是仍在创建过程中； - ACTIVE：超节点处于活动状态，其资源可被使用； - ERROR：超节点创建失败； - REIMAGING：超节点切换操作系统中； - TERMINATING：资源释放中； - TERMINATED：超节点资源已经被释放，其资源不再可用。 **默认取值**：不涉及。

        :param status: The status of this StopHyperinstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def servers(self):
        r"""Gets the servers of this StopHyperinstanceResponse.

        **参数解释**：超节点子节点实例列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The servers of this StopHyperinstanceResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ServerResponse`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        r"""Sets the servers of this StopHyperinstanceResponse.

        **参数解释**：超节点子节点实例列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param servers: The servers of this StopHyperinstanceResponse.
        :type servers: list[:class:`huaweicloudsdkmodelarts.v1.ServerResponse`]
        """
        self._servers = servers

    @property
    def update_at(self):
        r"""Gets the update_at of this StopHyperinstanceResponse.

        **参数解释**：创建时间。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The update_at of this StopHyperinstanceResponse.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this StopHyperinstanceResponse.

        **参数解释**：创建时间。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param update_at: The update_at of this StopHyperinstanceResponse.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this StopHyperinstanceResponse.

        :return: The x_request_id of this StopHyperinstanceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this StopHyperinstanceResponse.

        :param x_request_id: The x_request_id of this StopHyperinstanceResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("StopHyperinstanceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, StopHyperinstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
