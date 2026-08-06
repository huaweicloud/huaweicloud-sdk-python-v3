# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccessPointRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keyspace_id': 'str',
        'access_point_name': 'str',
        'type': 'int',
        'identity': 'str',
        'cluster_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'keyspace_id': 'keyspace_id',
        'access_point_name': 'access_point_name',
        'type': 'type',
        'identity': 'identity',
        'cluster_id': 'cluster_id',
        'description': 'description'
    }

    def __init__(self, keyspace_id=None, access_point_name=None, type=None, identity=None, cluster_id=None, description=None):
        r"""CreateAccessPointRequestBody

        The model defined in huaweicloud sdk

        :param keyspace_id: **参数解释：** 接入点归属的可信密钥空间ID **约束限制：** UUID格式，满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及
        :type keyspace_id: str
        :param access_point_name: **参数解释：** 接入点的名称 **约束限制：** 满足正则表达式^[a-zA-Z0-9:/_-]{1,255}$ **取值范围：** 1-255 **默认取值：** 不涉及
        :type access_point_name: str
        :param type: **参数解释：** 接入点的类型 **约束限制：** 不涉及 **取值范围：** - 1：ECS - 2：CCE - 3：Custom **默认取值：** 不涉及
        :type type: int
        :param identity: **参数解释：** 接入点的唯一标志 **约束限制：** ECS接入点填入ecs_id CCE接入点填入CCE集群公钥信息 Custom接入点无需填写，创建Custom接入点后，会生成一对密钥对，可以下载私钥，使用私钥签名，服务端验证签名 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type identity: str
        :param cluster_id: **参数解释：** 创建CCE接入点时必填，CCE集群ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type cluster_id: str
        :param description: **参数解释：** 接入点描述信息 **约束限制：** 不涉及 **取值范围：** 1-255 **默认取值：** 不涉及
        :type description: str
        """
        
        

        self._keyspace_id = None
        self._access_point_name = None
        self._type = None
        self._identity = None
        self._cluster_id = None
        self._description = None
        self.discriminator = None

        self.keyspace_id = keyspace_id
        self.access_point_name = access_point_name
        self.type = type
        if identity is not None:
            self.identity = identity
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if description is not None:
            self.description = description

    @property
    def keyspace_id(self):
        r"""Gets the keyspace_id of this CreateAccessPointRequestBody.

        **参数解释：** 接入点归属的可信密钥空间ID **约束限制：** UUID格式，满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The keyspace_id of this CreateAccessPointRequestBody.
        :rtype: str
        """
        return self._keyspace_id

    @keyspace_id.setter
    def keyspace_id(self, keyspace_id):
        r"""Sets the keyspace_id of this CreateAccessPointRequestBody.

        **参数解释：** 接入点归属的可信密钥空间ID **约束限制：** UUID格式，满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :param keyspace_id: The keyspace_id of this CreateAccessPointRequestBody.
        :type keyspace_id: str
        """
        self._keyspace_id = keyspace_id

    @property
    def access_point_name(self):
        r"""Gets the access_point_name of this CreateAccessPointRequestBody.

        **参数解释：** 接入点的名称 **约束限制：** 满足正则表达式^[a-zA-Z0-9:/_-]{1,255}$ **取值范围：** 1-255 **默认取值：** 不涉及

        :return: The access_point_name of this CreateAccessPointRequestBody.
        :rtype: str
        """
        return self._access_point_name

    @access_point_name.setter
    def access_point_name(self, access_point_name):
        r"""Sets the access_point_name of this CreateAccessPointRequestBody.

        **参数解释：** 接入点的名称 **约束限制：** 满足正则表达式^[a-zA-Z0-9:/_-]{1,255}$ **取值范围：** 1-255 **默认取值：** 不涉及

        :param access_point_name: The access_point_name of this CreateAccessPointRequestBody.
        :type access_point_name: str
        """
        self._access_point_name = access_point_name

    @property
    def type(self):
        r"""Gets the type of this CreateAccessPointRequestBody.

        **参数解释：** 接入点的类型 **约束限制：** 不涉及 **取值范围：** - 1：ECS - 2：CCE - 3：Custom **默认取值：** 不涉及

        :return: The type of this CreateAccessPointRequestBody.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateAccessPointRequestBody.

        **参数解释：** 接入点的类型 **约束限制：** 不涉及 **取值范围：** - 1：ECS - 2：CCE - 3：Custom **默认取值：** 不涉及

        :param type: The type of this CreateAccessPointRequestBody.
        :type type: int
        """
        self._type = type

    @property
    def identity(self):
        r"""Gets the identity of this CreateAccessPointRequestBody.

        **参数解释：** 接入点的唯一标志 **约束限制：** ECS接入点填入ecs_id CCE接入点填入CCE集群公钥信息 Custom接入点无需填写，创建Custom接入点后，会生成一对密钥对，可以下载私钥，使用私钥签名，服务端验证签名 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The identity of this CreateAccessPointRequestBody.
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        r"""Sets the identity of this CreateAccessPointRequestBody.

        **参数解释：** 接入点的唯一标志 **约束限制：** ECS接入点填入ecs_id CCE接入点填入CCE集群公钥信息 Custom接入点无需填写，创建Custom接入点后，会生成一对密钥对，可以下载私钥，使用私钥签名，服务端验证签名 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param identity: The identity of this CreateAccessPointRequestBody.
        :type identity: str
        """
        self._identity = identity

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CreateAccessPointRequestBody.

        **参数解释：** 创建CCE接入点时必填，CCE集群ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The cluster_id of this CreateAccessPointRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CreateAccessPointRequestBody.

        **参数解释：** 创建CCE接入点时必填，CCE集群ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param cluster_id: The cluster_id of this CreateAccessPointRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def description(self):
        r"""Gets the description of this CreateAccessPointRequestBody.

        **参数解释：** 接入点描述信息 **约束限制：** 不涉及 **取值范围：** 1-255 **默认取值：** 不涉及

        :return: The description of this CreateAccessPointRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAccessPointRequestBody.

        **参数解释：** 接入点描述信息 **约束限制：** 不涉及 **取值范围：** 1-255 **默认取值：** 不涉及

        :param description: The description of this CreateAccessPointRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateAccessPointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
