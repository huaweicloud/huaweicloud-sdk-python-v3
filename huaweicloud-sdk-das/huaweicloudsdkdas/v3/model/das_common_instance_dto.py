# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DasCommonInstanceDto:

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
        'status': 'str',
        'type': 'str',
        'enterprise_project_id': 'str',
        'engine_type': 'str',
        'engine_version': 'str',
        'port': 'str',
        'region': 'str',
        'nodes': 'list[DasCommonInstanceNodeDto]',
        'network_type': 'str',
        'related_instance': 'list[RelatedInstance]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'engine_type': 'engine_type',
        'engine_version': 'engine_version',
        'port': 'port',
        'region': 'region',
        'nodes': 'nodes',
        'network_type': 'network_type',
        'related_instance': 'related_instance'
    }

    def __init__(self, id=None, name=None, status=None, type=None, enterprise_project_id=None, engine_type=None, engine_version=None, port=None, region=None, nodes=None, network_type=None, related_instance=None):
        r"""DasCommonInstanceDto

        The model defined in huaweicloud sdk

        :param id: 实例ID
        :type id: str
        :param name: 实例名称
        :type name: str
        :param status: 实例状态
        :type status: str
        :param type: 实例类型
        :type type: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param engine_version: 实例引擎版本
        :type engine_version: str
        :param port: 实例引擎端口
        :type port: str
        :param region: 区域
        :type region: str
        :param nodes: 实例节点列表
        :type nodes: list[:class:`huaweicloudsdkdas.v3.DasCommonInstanceNodeDto`]
        :param network_type: 数据库来源类型
        :type network_type: str
        :param related_instance: 相关实例列表
        :type related_instance: list[:class:`huaweicloudsdkdas.v3.RelatedInstance`]
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._type = None
        self._enterprise_project_id = None
        self._engine_type = None
        self._engine_version = None
        self._port = None
        self._region = None
        self._nodes = None
        self._network_type = None
        self._related_instance = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if engine_type is not None:
            self.engine_type = engine_type
        if engine_version is not None:
            self.engine_version = engine_version
        if port is not None:
            self.port = port
        if region is not None:
            self.region = region
        if nodes is not None:
            self.nodes = nodes
        if network_type is not None:
            self.network_type = network_type
        if related_instance is not None:
            self.related_instance = related_instance

    @property
    def id(self):
        r"""Gets the id of this DasCommonInstanceDto.

        实例ID

        :return: The id of this DasCommonInstanceDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DasCommonInstanceDto.

        实例ID

        :param id: The id of this DasCommonInstanceDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DasCommonInstanceDto.

        实例名称

        :return: The name of this DasCommonInstanceDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DasCommonInstanceDto.

        实例名称

        :param name: The name of this DasCommonInstanceDto.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this DasCommonInstanceDto.

        实例状态

        :return: The status of this DasCommonInstanceDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DasCommonInstanceDto.

        实例状态

        :param status: The status of this DasCommonInstanceDto.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this DasCommonInstanceDto.

        实例类型

        :return: The type of this DasCommonInstanceDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DasCommonInstanceDto.

        实例类型

        :param type: The type of this DasCommonInstanceDto.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this DasCommonInstanceDto.

        企业项目ID

        :return: The enterprise_project_id of this DasCommonInstanceDto.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this DasCommonInstanceDto.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this DasCommonInstanceDto.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this DasCommonInstanceDto.

        数据库引擎类型

        :return: The engine_type of this DasCommonInstanceDto.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this DasCommonInstanceDto.

        数据库引擎类型

        :param engine_type: The engine_type of this DasCommonInstanceDto.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def engine_version(self):
        r"""Gets the engine_version of this DasCommonInstanceDto.

        实例引擎版本

        :return: The engine_version of this DasCommonInstanceDto.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this DasCommonInstanceDto.

        实例引擎版本

        :param engine_version: The engine_version of this DasCommonInstanceDto.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def port(self):
        r"""Gets the port of this DasCommonInstanceDto.

        实例引擎端口

        :return: The port of this DasCommonInstanceDto.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this DasCommonInstanceDto.

        实例引擎端口

        :param port: The port of this DasCommonInstanceDto.
        :type port: str
        """
        self._port = port

    @property
    def region(self):
        r"""Gets the region of this DasCommonInstanceDto.

        区域

        :return: The region of this DasCommonInstanceDto.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DasCommonInstanceDto.

        区域

        :param region: The region of this DasCommonInstanceDto.
        :type region: str
        """
        self._region = region

    @property
    def nodes(self):
        r"""Gets the nodes of this DasCommonInstanceDto.

        实例节点列表

        :return: The nodes of this DasCommonInstanceDto.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DasCommonInstanceNodeDto`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this DasCommonInstanceDto.

        实例节点列表

        :param nodes: The nodes of this DasCommonInstanceDto.
        :type nodes: list[:class:`huaweicloudsdkdas.v3.DasCommonInstanceNodeDto`]
        """
        self._nodes = nodes

    @property
    def network_type(self):
        r"""Gets the network_type of this DasCommonInstanceDto.

        数据库来源类型

        :return: The network_type of this DasCommonInstanceDto.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this DasCommonInstanceDto.

        数据库来源类型

        :param network_type: The network_type of this DasCommonInstanceDto.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def related_instance(self):
        r"""Gets the related_instance of this DasCommonInstanceDto.

        相关实例列表

        :return: The related_instance of this DasCommonInstanceDto.
        :rtype: list[:class:`huaweicloudsdkdas.v3.RelatedInstance`]
        """
        return self._related_instance

    @related_instance.setter
    def related_instance(self, related_instance):
        r"""Sets the related_instance of this DasCommonInstanceDto.

        相关实例列表

        :param related_instance: The related_instance of this DasCommonInstanceDto.
        :type related_instance: list[:class:`huaweicloudsdkdas.v3.RelatedInstance`]
        """
        self._related_instance = related_instance

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
        if not isinstance(other, DasCommonInstanceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
