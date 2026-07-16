# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInferDeploymentPodsRequest:

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
        'deployment_name': 'str',
        'name': 'str',
        'status': 'list[str]',
        'limit': 'int',
        'offset': 'str',
        'pod_name': 'str',
        'pod_id': 'str',
        'pod_node_ip': 'str',
        'pod_node_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'deployment_name': 'deployment_name',
        'name': 'name',
        'status': 'status',
        'limit': 'limit',
        'offset': 'offset',
        'pod_name': 'pod_name',
        'pod_id': 'pod_id',
        'pod_node_ip': 'pod_node_ip',
        'pod_node_name': 'pod_node_name'
    }

    def __init__(self, id=None, deployment_name=None, name=None, status=None, limit=None, offset=None, pod_name=None, pod_id=None, pod_node_ip=None, pod_node_name=None):
        r"""ListInferDeploymentPodsRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。
        :type id: str
        :param deployment_name: **参数解释：** 部署名称，在创建部署时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其name字段即为部署名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type deployment_name: str
        :param name: **参数解释：** 服务实例名字，可以为all，为all时去查询所有的服务实例。 **约束限制：** 不涉及。 **取值范围：** 服务实例名字。 **默认取值：** 不涉及。
        :type name: str
        :param status: **参数解释：** pod状态，一次支持多种状态筛选，多种状态以\&quot;,\&quot;连接，不能存在空格。默认不过滤。取值范围有7种RUNNING（运行中）、PENDING（未就绪）、SUCCEEDED（成功）、FAILED（失败）、ABNORMAL（异常）、UNKNOWN（未知）、DELETED（已删除）。 **约束限制：** 不涉及。
        :type status: list[str]
        :param limit: **参数解释：** 指定每一页返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。
        :type limit: int
        :param offset: **参数解释：** 分页列表的起始页。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。
        :type offset: str
        :param pod_name: **参数解释：** pod名字。 **取值范围：** 不涉及。
        :type pod_name: str
        :param pod_id: **参数解释：** pod ID。 **取值范围：** 不涉及。
        :type pod_id: str
        :param pod_node_ip: **参数解释：** pod节点IP地址。 **取值范围：** 不涉及。
        :type pod_node_ip: str
        :param pod_node_name: **参数解释：** pod节点名称。 **取值范围：** 不涉及。
        :type pod_node_name: str
        """
        
        

        self._id = None
        self._deployment_name = None
        self._name = None
        self._status = None
        self._limit = None
        self._offset = None
        self._pod_name = None
        self._pod_id = None
        self._pod_node_ip = None
        self._pod_node_name = None
        self.discriminator = None

        self.id = id
        self.deployment_name = deployment_name
        self.name = name
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if pod_name is not None:
            self.pod_name = pod_name
        if pod_id is not None:
            self.pod_id = pod_id
        if pod_node_ip is not None:
            self.pod_node_ip = pod_node_ip
        if pod_node_name is not None:
            self.pod_node_name = pod_node_name

    @property
    def id(self):
        r"""Gets the id of this ListInferDeploymentPodsRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :return: The id of this ListInferDeploymentPodsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListInferDeploymentPodsRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :param id: The id of this ListInferDeploymentPodsRequest.
        :type id: str
        """
        self._id = id

    @property
    def deployment_name(self):
        r"""Gets the deployment_name of this ListInferDeploymentPodsRequest.

        **参数解释：** 部署名称，在创建部署时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其name字段即为部署名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The deployment_name of this ListInferDeploymentPodsRequest.
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        r"""Sets the deployment_name of this ListInferDeploymentPodsRequest.

        **参数解释：** 部署名称，在创建部署时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其name字段即为部署名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param deployment_name: The deployment_name of this ListInferDeploymentPodsRequest.
        :type deployment_name: str
        """
        self._deployment_name = deployment_name

    @property
    def name(self):
        r"""Gets the name of this ListInferDeploymentPodsRequest.

        **参数解释：** 服务实例名字，可以为all，为all时去查询所有的服务实例。 **约束限制：** 不涉及。 **取值范围：** 服务实例名字。 **默认取值：** 不涉及。

        :return: The name of this ListInferDeploymentPodsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInferDeploymentPodsRequest.

        **参数解释：** 服务实例名字，可以为all，为all时去查询所有的服务实例。 **约束限制：** 不涉及。 **取值范围：** 服务实例名字。 **默认取值：** 不涉及。

        :param name: The name of this ListInferDeploymentPodsRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListInferDeploymentPodsRequest.

        **参数解释：** pod状态，一次支持多种状态筛选，多种状态以\",\"连接，不能存在空格。默认不过滤。取值范围有7种RUNNING（运行中）、PENDING（未就绪）、SUCCEEDED（成功）、FAILED（失败）、ABNORMAL（异常）、UNKNOWN（未知）、DELETED（已删除）。 **约束限制：** 不涉及。

        :return: The status of this ListInferDeploymentPodsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListInferDeploymentPodsRequest.

        **参数解释：** pod状态，一次支持多种状态筛选，多种状态以\",\"连接，不能存在空格。默认不过滤。取值范围有7种RUNNING（运行中）、PENDING（未就绪）、SUCCEEDED（成功）、FAILED（失败）、ABNORMAL（异常）、UNKNOWN（未知）、DELETED（已删除）。 **约束限制：** 不涉及。

        :param status: The status of this ListInferDeploymentPodsRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def limit(self):
        r"""Gets the limit of this ListInferDeploymentPodsRequest.

        **参数解释：** 指定每一页返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :return: The limit of this ListInferDeploymentPodsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInferDeploymentPodsRequest.

        **参数解释：** 指定每一页返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :param limit: The limit of this ListInferDeploymentPodsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInferDeploymentPodsRequest.

        **参数解释：** 分页列表的起始页。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。

        :return: The offset of this ListInferDeploymentPodsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInferDeploymentPodsRequest.

        **参数解释：** 分页列表的起始页。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。

        :param offset: The offset of this ListInferDeploymentPodsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ListInferDeploymentPodsRequest.

        **参数解释：** pod名字。 **取值范围：** 不涉及。

        :return: The pod_name of this ListInferDeploymentPodsRequest.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ListInferDeploymentPodsRequest.

        **参数解释：** pod名字。 **取值范围：** 不涉及。

        :param pod_name: The pod_name of this ListInferDeploymentPodsRequest.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def pod_id(self):
        r"""Gets the pod_id of this ListInferDeploymentPodsRequest.

        **参数解释：** pod ID。 **取值范围：** 不涉及。

        :return: The pod_id of this ListInferDeploymentPodsRequest.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        r"""Sets the pod_id of this ListInferDeploymentPodsRequest.

        **参数解释：** pod ID。 **取值范围：** 不涉及。

        :param pod_id: The pod_id of this ListInferDeploymentPodsRequest.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def pod_node_ip(self):
        r"""Gets the pod_node_ip of this ListInferDeploymentPodsRequest.

        **参数解释：** pod节点IP地址。 **取值范围：** 不涉及。

        :return: The pod_node_ip of this ListInferDeploymentPodsRequest.
        :rtype: str
        """
        return self._pod_node_ip

    @pod_node_ip.setter
    def pod_node_ip(self, pod_node_ip):
        r"""Sets the pod_node_ip of this ListInferDeploymentPodsRequest.

        **参数解释：** pod节点IP地址。 **取值范围：** 不涉及。

        :param pod_node_ip: The pod_node_ip of this ListInferDeploymentPodsRequest.
        :type pod_node_ip: str
        """
        self._pod_node_ip = pod_node_ip

    @property
    def pod_node_name(self):
        r"""Gets the pod_node_name of this ListInferDeploymentPodsRequest.

        **参数解释：** pod节点名称。 **取值范围：** 不涉及。

        :return: The pod_node_name of this ListInferDeploymentPodsRequest.
        :rtype: str
        """
        return self._pod_node_name

    @pod_node_name.setter
    def pod_node_name(self, pod_node_name):
        r"""Sets the pod_node_name of this ListInferDeploymentPodsRequest.

        **参数解释：** pod节点名称。 **取值范围：** 不涉及。

        :param pod_node_name: The pod_node_name of this ListInferDeploymentPodsRequest.
        :type pod_node_name: str
        """
        self._pod_node_name = pod_node_name

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
        if not isinstance(other, ListInferDeploymentPodsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
