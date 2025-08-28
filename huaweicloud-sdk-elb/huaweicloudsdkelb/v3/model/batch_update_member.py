# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateMember:

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
        'project_id': 'str',
        'admin_state_up': 'bool',
        'subnet_cidr_id': 'str',
        'protocol_port': 'int',
        'weight': 'int',
        'address': 'str',
        'operating_status': 'str',
        'reason': 'MemberHealthCheckFailedReason',
        'status': 'list[MemberStatus]',
        'member_type': 'str',
        'instance_id': 'str',
        'port_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'admin_state_up': 'admin_state_up',
        'subnet_cidr_id': 'subnet_cidr_id',
        'protocol_port': 'protocol_port',
        'weight': 'weight',
        'address': 'address',
        'operating_status': 'operating_status',
        'reason': 'reason',
        'status': 'status',
        'member_type': 'member_type',
        'instance_id': 'instance_id',
        'port_id': 'port_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, id=None, name=None, project_id=None, admin_state_up=None, subnet_cidr_id=None, protocol_port=None, weight=None, address=None, operating_status=None, reason=None, status=None, member_type=None, instance_id=None, port_id=None, created_at=None, updated_at=None, availability_zone=None):
        r"""BatchUpdateMember

        The model defined in huaweicloud sdk

        :param id: **参数解释**：后端服务器ID。  **取值范围**：不涉及  &gt; 此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。
        :type id: str
        :param name: **参数解释**：后端服务器名称。  **取值范围**：不涉及
        :type name: str
        :param project_id: **参数解释**：后端服务器所在的项目ID。  **取值范围**：不涉及
        :type project_id: str
        :param admin_state_up: **参数解释**：后端服务器的管理状态。 虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：不涉及
        :type admin_state_up: bool
        :param subnet_cidr_id: **参数解释**：后端服务器所在的子网，可以是IPv4或IPv6子网。若是IPv4子网，使用对应子网的子网ID（neutron_subnet_id）；若是IPv6子网，使用对应子网的网络ID（neutron_network_id）。 ipv4子网的子网ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到 ipv6子网的网络ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)
        :type subnet_cidr_id: str
        :param protocol_port: **参数解释**：后端服务器业务端口。  **取值范围**：不涉及  &gt;在开启端口透传的pool下创建member传该字段不生效，可不传该字段。
        :type protocol_port: int
        :param weight: **参数解释**：后端服务器的权重，请求将根据pool配置的负载均衡算法和后端服务器的权重进行负载分发。权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  **取值范围**：0-100
        :type weight: int
        :param address: **参数解释**：后端服务器对应的IP地址。  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6地址。](tag:dt)
        :type address: str
        :param operating_status: **参数解释**：后端服务器的健康状态。  **取值范围**： - NO_MONITOR：后端服务器所在的服务器组没有开启健康检查。 - INITIAL：初始化中，表示负载均衡实例配置了健康检查，但查不到数据。 - ONLINE：后端服务器正常。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。 - UNKNOWN：未关联LB实例的pool下的member，或者创建后从未关联ECS的云服务器类型member，状态置为UNKNOWN。
        :type operating_status: str
        :param reason: 
        :type reason: :class:`huaweicloudsdkelb.v3.MemberHealthCheckFailedReason`
        :param status: **参数解释**：后端服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_status为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。
        :type status: list[:class:`huaweicloudsdkelb.v3.MemberStatus`]
        :param member_type: **参数解释**：后端服务器的类型。  **取值范围**： - ip：跨VPC的member。 - instance：关联到ECS的member。
        :type member_type: str
        :param instance_id: **参数解释**：member关联的实例ID，空表示跨VPC场景的member。  **取值范围**：不涉及
        :type instance_id: str
        :param port_id: **参数解释**：IP地址对应的VPC port ID。  **取值范围**：不涉及
        :type port_id: str
        :param created_at: **参数解释**：创建时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)
        :type created_at: str
        :param updated_at: **参数解释**：更新时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)
        :type updated_at: str
        :param availability_zone: **参数解释**：后端服务器所在的可用区。  **取值范围**：不涉及
        :type availability_zone: str
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._admin_state_up = None
        self._subnet_cidr_id = None
        self._protocol_port = None
        self._weight = None
        self._address = None
        self._operating_status = None
        self._reason = None
        self._status = None
        self._member_type = None
        self._instance_id = None
        self._port_id = None
        self._created_at = None
        self._updated_at = None
        self._availability_zone = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.project_id = project_id
        self.admin_state_up = admin_state_up
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        self.protocol_port = protocol_port
        self.weight = weight
        self.address = address
        self.operating_status = operating_status
        if reason is not None:
            self.reason = reason
        if status is not None:
            self.status = status
        if member_type is not None:
            self.member_type = member_type
        if instance_id is not None:
            self.instance_id = instance_id
        self.port_id = port_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def id(self):
        r"""Gets the id of this BatchUpdateMember.

        **参数解释**：后端服务器ID。  **取值范围**：不涉及  > 此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。

        :return: The id of this BatchUpdateMember.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchUpdateMember.

        **参数解释**：后端服务器ID。  **取值范围**：不涉及  > 此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。

        :param id: The id of this BatchUpdateMember.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BatchUpdateMember.

        **参数解释**：后端服务器名称。  **取值范围**：不涉及

        :return: The name of this BatchUpdateMember.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchUpdateMember.

        **参数解释**：后端服务器名称。  **取值范围**：不涉及

        :param name: The name of this BatchUpdateMember.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this BatchUpdateMember.

        **参数解释**：后端服务器所在的项目ID。  **取值范围**：不涉及

        :return: The project_id of this BatchUpdateMember.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BatchUpdateMember.

        **参数解释**：后端服务器所在的项目ID。  **取值范围**：不涉及

        :param project_id: The project_id of this BatchUpdateMember.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this BatchUpdateMember.

        **参数解释**：后端服务器的管理状态。 虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：不涉及

        :return: The admin_state_up of this BatchUpdateMember.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this BatchUpdateMember.

        **参数解释**：后端服务器的管理状态。 虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：不涉及

        :param admin_state_up: The admin_state_up of this BatchUpdateMember.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def subnet_cidr_id(self):
        r"""Gets the subnet_cidr_id of this BatchUpdateMember.

        **参数解释**：后端服务器所在的子网，可以是IPv4或IPv6子网。若是IPv4子网，使用对应子网的子网ID（neutron_subnet_id）；若是IPv6子网，使用对应子网的网络ID（neutron_network_id）。 ipv4子网的子网ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到 ipv6子网的网络ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)

        :return: The subnet_cidr_id of this BatchUpdateMember.
        :rtype: str
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        r"""Sets the subnet_cidr_id of this BatchUpdateMember.

        **参数解释**：后端服务器所在的子网，可以是IPv4或IPv6子网。若是IPv4子网，使用对应子网的子网ID（neutron_subnet_id）；若是IPv6子网，使用对应子网的网络ID（neutron_network_id）。 ipv4子网的子网ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到 ipv6子网的网络ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)

        :param subnet_cidr_id: The subnet_cidr_id of this BatchUpdateMember.
        :type subnet_cidr_id: str
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this BatchUpdateMember.

        **参数解释**：后端服务器业务端口。  **取值范围**：不涉及  >在开启端口透传的pool下创建member传该字段不生效，可不传该字段。

        :return: The protocol_port of this BatchUpdateMember.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this BatchUpdateMember.

        **参数解释**：后端服务器业务端口。  **取值范围**：不涉及  >在开启端口透传的pool下创建member传该字段不生效，可不传该字段。

        :param protocol_port: The protocol_port of this BatchUpdateMember.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def weight(self):
        r"""Gets the weight of this BatchUpdateMember.

        **参数解释**：后端服务器的权重，请求将根据pool配置的负载均衡算法和后端服务器的权重进行负载分发。权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  **取值范围**：0-100

        :return: The weight of this BatchUpdateMember.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this BatchUpdateMember.

        **参数解释**：后端服务器的权重，请求将根据pool配置的负载均衡算法和后端服务器的权重进行负载分发。权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  **取值范围**：0-100

        :param weight: The weight of this BatchUpdateMember.
        :type weight: int
        """
        self._weight = weight

    @property
    def address(self):
        r"""Gets the address of this BatchUpdateMember.

        **参数解释**：后端服务器对应的IP地址。  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6地址。](tag:dt)

        :return: The address of this BatchUpdateMember.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this BatchUpdateMember.

        **参数解释**：后端服务器对应的IP地址。  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6地址。](tag:dt)

        :param address: The address of this BatchUpdateMember.
        :type address: str
        """
        self._address = address

    @property
    def operating_status(self):
        r"""Gets the operating_status of this BatchUpdateMember.

        **参数解释**：后端服务器的健康状态。  **取值范围**： - NO_MONITOR：后端服务器所在的服务器组没有开启健康检查。 - INITIAL：初始化中，表示负载均衡实例配置了健康检查，但查不到数据。 - ONLINE：后端服务器正常。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。 - UNKNOWN：未关联LB实例的pool下的member，或者创建后从未关联ECS的云服务器类型member，状态置为UNKNOWN。

        :return: The operating_status of this BatchUpdateMember.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        r"""Sets the operating_status of this BatchUpdateMember.

        **参数解释**：后端服务器的健康状态。  **取值范围**： - NO_MONITOR：后端服务器所在的服务器组没有开启健康检查。 - INITIAL：初始化中，表示负载均衡实例配置了健康检查，但查不到数据。 - ONLINE：后端服务器正常。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。 - UNKNOWN：未关联LB实例的pool下的member，或者创建后从未关联ECS的云服务器类型member，状态置为UNKNOWN。

        :param operating_status: The operating_status of this BatchUpdateMember.
        :type operating_status: str
        """
        self._operating_status = operating_status

    @property
    def reason(self):
        r"""Gets the reason of this BatchUpdateMember.

        :return: The reason of this BatchUpdateMember.
        :rtype: :class:`huaweicloudsdkelb.v3.MemberHealthCheckFailedReason`
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this BatchUpdateMember.

        :param reason: The reason of this BatchUpdateMember.
        :type reason: :class:`huaweicloudsdkelb.v3.MemberHealthCheckFailedReason`
        """
        self._reason = reason

    @property
    def status(self):
        r"""Gets the status of this BatchUpdateMember.

        **参数解释**：后端服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_status为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。

        :return: The status of this BatchUpdateMember.
        :rtype: list[:class:`huaweicloudsdkelb.v3.MemberStatus`]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchUpdateMember.

        **参数解释**：后端服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_status为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。

        :param status: The status of this BatchUpdateMember.
        :type status: list[:class:`huaweicloudsdkelb.v3.MemberStatus`]
        """
        self._status = status

    @property
    def member_type(self):
        r"""Gets the member_type of this BatchUpdateMember.

        **参数解释**：后端服务器的类型。  **取值范围**： - ip：跨VPC的member。 - instance：关联到ECS的member。

        :return: The member_type of this BatchUpdateMember.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        r"""Sets the member_type of this BatchUpdateMember.

        **参数解释**：后端服务器的类型。  **取值范围**： - ip：跨VPC的member。 - instance：关联到ECS的member。

        :param member_type: The member_type of this BatchUpdateMember.
        :type member_type: str
        """
        self._member_type = member_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BatchUpdateMember.

        **参数解释**：member关联的实例ID，空表示跨VPC场景的member。  **取值范围**：不涉及

        :return: The instance_id of this BatchUpdateMember.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BatchUpdateMember.

        **参数解释**：member关联的实例ID，空表示跨VPC场景的member。  **取值范围**：不涉及

        :param instance_id: The instance_id of this BatchUpdateMember.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def port_id(self):
        r"""Gets the port_id of this BatchUpdateMember.

        **参数解释**：IP地址对应的VPC port ID。  **取值范围**：不涉及

        :return: The port_id of this BatchUpdateMember.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this BatchUpdateMember.

        **参数解释**：IP地址对应的VPC port ID。  **取值范围**：不涉及

        :param port_id: The port_id of this BatchUpdateMember.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def created_at(self):
        r"""Gets the created_at of this BatchUpdateMember.

        **参数解释**：创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :return: The created_at of this BatchUpdateMember.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this BatchUpdateMember.

        **参数解释**：创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :param created_at: The created_at of this BatchUpdateMember.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this BatchUpdateMember.

        **参数解释**：更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :return: The updated_at of this BatchUpdateMember.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this BatchUpdateMember.

        **参数解释**：更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :param updated_at: The updated_at of this BatchUpdateMember.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this BatchUpdateMember.

        **参数解释**：后端服务器所在的可用区。  **取值范围**：不涉及

        :return: The availability_zone of this BatchUpdateMember.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this BatchUpdateMember.

        **参数解释**：后端服务器所在的可用区。  **取值范围**：不涉及

        :param availability_zone: The availability_zone of this BatchUpdateMember.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, BatchUpdateMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
