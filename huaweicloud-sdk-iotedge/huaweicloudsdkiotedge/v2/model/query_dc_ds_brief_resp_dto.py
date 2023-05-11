# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDcDsBriefRespDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ds_id': 'str',
        'name': 'str',
        'edge_node_id': 'str',
        'module_id': 'str',
        'tpl_id': 'str',
        'quality_report': 'bool',
        'edge_app_name': 'str',
        'connection_info': 'object',
        'module_state': 'str',
        'count': 'int',
        'create_time': 'str',
        'update_time': 'str',
        'synchronized': 'bool',
        'synchronized_time': 'str'
    }

    attribute_map = {
        'ds_id': 'ds_id',
        'name': 'name',
        'edge_node_id': 'edge_node_id',
        'module_id': 'module_id',
        'tpl_id': 'tpl_id',
        'quality_report': 'quality_report',
        'edge_app_name': 'edge_app_name',
        'connection_info': 'connection_info',
        'module_state': 'module_state',
        'count': 'count',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'synchronized': 'synchronized',
        'synchronized_time': 'synchronized_time'
    }

    def __init__(self, ds_id=None, name=None, edge_node_id=None, module_id=None, tpl_id=None, quality_report=None, edge_app_name=None, connection_info=None, module_state=None, count=None, create_time=None, update_time=None, synchronized=None, synchronized_time=None):
        """QueryDcDsBriefRespDTO

        The model defined in huaweicloud sdk

        :param ds_id: 采集数据源id，节点下唯一
        :type ds_id: str
        :param name: 采集数据源名称，允许中、数字、英文大小写、下划线、中划线
        :type name: str
        :param edge_node_id: 边缘节点id
        :type edge_node_id: str
        :param module_id: 模块id
        :type module_id: str
        :param tpl_id: 模板id，节点下唯一
        :type tpl_id: str
        :param quality_report: 质量上报开关，不携带或值不为true，默认为false
        :type quality_report: bool
        :param edge_app_name: 应用ID
        :type edge_app_name: str
        :param connection_info: 数采连接信息
        :type connection_info: object
        :param module_state: 数采连接状态,RUNNING|STOPPED
        :type module_state: str
        :param count: 数采连接下点位数
        :type count: int
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        :param synchronized: 数采配置是否已同步，已同步：true,未同步：false
        :type synchronized: bool
        :param synchronized_time: 数采配置同步时间
        :type synchronized_time: str
        """
        
        

        self._ds_id = None
        self._name = None
        self._edge_node_id = None
        self._module_id = None
        self._tpl_id = None
        self._quality_report = None
        self._edge_app_name = None
        self._connection_info = None
        self._module_state = None
        self._count = None
        self._create_time = None
        self._update_time = None
        self._synchronized = None
        self._synchronized_time = None
        self.discriminator = None

        if ds_id is not None:
            self.ds_id = ds_id
        if name is not None:
            self.name = name
        if edge_node_id is not None:
            self.edge_node_id = edge_node_id
        if module_id is not None:
            self.module_id = module_id
        if tpl_id is not None:
            self.tpl_id = tpl_id
        if quality_report is not None:
            self.quality_report = quality_report
        if edge_app_name is not None:
            self.edge_app_name = edge_app_name
        if connection_info is not None:
            self.connection_info = connection_info
        if module_state is not None:
            self.module_state = module_state
        if count is not None:
            self.count = count
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if synchronized is not None:
            self.synchronized = synchronized
        if synchronized_time is not None:
            self.synchronized_time = synchronized_time

    @property
    def ds_id(self):
        """Gets the ds_id of this QueryDcDsBriefRespDTO.

        采集数据源id，节点下唯一

        :return: The ds_id of this QueryDcDsBriefRespDTO.
        :rtype: str
        """
        return self._ds_id

    @ds_id.setter
    def ds_id(self, ds_id):
        """Sets the ds_id of this QueryDcDsBriefRespDTO.

        采集数据源id，节点下唯一

        :param ds_id: The ds_id of this QueryDcDsBriefRespDTO.
        :type ds_id: str
        """
        self._ds_id = ds_id

    @property
    def name(self):
        """Gets the name of this QueryDcDsBriefRespDTO.

        采集数据源名称，允许中、数字、英文大小写、下划线、中划线

        :return: The name of this QueryDcDsBriefRespDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryDcDsBriefRespDTO.

        采集数据源名称，允许中、数字、英文大小写、下划线、中划线

        :param name: The name of this QueryDcDsBriefRespDTO.
        :type name: str
        """
        self._name = name

    @property
    def edge_node_id(self):
        """Gets the edge_node_id of this QueryDcDsBriefRespDTO.

        边缘节点id

        :return: The edge_node_id of this QueryDcDsBriefRespDTO.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        """Sets the edge_node_id of this QueryDcDsBriefRespDTO.

        边缘节点id

        :param edge_node_id: The edge_node_id of this QueryDcDsBriefRespDTO.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def module_id(self):
        """Gets the module_id of this QueryDcDsBriefRespDTO.

        模块id

        :return: The module_id of this QueryDcDsBriefRespDTO.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this QueryDcDsBriefRespDTO.

        模块id

        :param module_id: The module_id of this QueryDcDsBriefRespDTO.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def tpl_id(self):
        """Gets the tpl_id of this QueryDcDsBriefRespDTO.

        模板id，节点下唯一

        :return: The tpl_id of this QueryDcDsBriefRespDTO.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this QueryDcDsBriefRespDTO.

        模板id，节点下唯一

        :param tpl_id: The tpl_id of this QueryDcDsBriefRespDTO.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def quality_report(self):
        """Gets the quality_report of this QueryDcDsBriefRespDTO.

        质量上报开关，不携带或值不为true，默认为false

        :return: The quality_report of this QueryDcDsBriefRespDTO.
        :rtype: bool
        """
        return self._quality_report

    @quality_report.setter
    def quality_report(self, quality_report):
        """Sets the quality_report of this QueryDcDsBriefRespDTO.

        质量上报开关，不携带或值不为true，默认为false

        :param quality_report: The quality_report of this QueryDcDsBriefRespDTO.
        :type quality_report: bool
        """
        self._quality_report = quality_report

    @property
    def edge_app_name(self):
        """Gets the edge_app_name of this QueryDcDsBriefRespDTO.

        应用ID

        :return: The edge_app_name of this QueryDcDsBriefRespDTO.
        :rtype: str
        """
        return self._edge_app_name

    @edge_app_name.setter
    def edge_app_name(self, edge_app_name):
        """Sets the edge_app_name of this QueryDcDsBriefRespDTO.

        应用ID

        :param edge_app_name: The edge_app_name of this QueryDcDsBriefRespDTO.
        :type edge_app_name: str
        """
        self._edge_app_name = edge_app_name

    @property
    def connection_info(self):
        """Gets the connection_info of this QueryDcDsBriefRespDTO.

        数采连接信息

        :return: The connection_info of this QueryDcDsBriefRespDTO.
        :rtype: object
        """
        return self._connection_info

    @connection_info.setter
    def connection_info(self, connection_info):
        """Sets the connection_info of this QueryDcDsBriefRespDTO.

        数采连接信息

        :param connection_info: The connection_info of this QueryDcDsBriefRespDTO.
        :type connection_info: object
        """
        self._connection_info = connection_info

    @property
    def module_state(self):
        """Gets the module_state of this QueryDcDsBriefRespDTO.

        数采连接状态,RUNNING|STOPPED

        :return: The module_state of this QueryDcDsBriefRespDTO.
        :rtype: str
        """
        return self._module_state

    @module_state.setter
    def module_state(self, module_state):
        """Sets the module_state of this QueryDcDsBriefRespDTO.

        数采连接状态,RUNNING|STOPPED

        :param module_state: The module_state of this QueryDcDsBriefRespDTO.
        :type module_state: str
        """
        self._module_state = module_state

    @property
    def count(self):
        """Gets the count of this QueryDcDsBriefRespDTO.

        数采连接下点位数

        :return: The count of this QueryDcDsBriefRespDTO.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this QueryDcDsBriefRespDTO.

        数采连接下点位数

        :param count: The count of this QueryDcDsBriefRespDTO.
        :type count: int
        """
        self._count = count

    @property
    def create_time(self):
        """Gets the create_time of this QueryDcDsBriefRespDTO.

        创建时间

        :return: The create_time of this QueryDcDsBriefRespDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryDcDsBriefRespDTO.

        创建时间

        :param create_time: The create_time of this QueryDcDsBriefRespDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this QueryDcDsBriefRespDTO.

        最后一次修改时间

        :return: The update_time of this QueryDcDsBriefRespDTO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this QueryDcDsBriefRespDTO.

        最后一次修改时间

        :param update_time: The update_time of this QueryDcDsBriefRespDTO.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def synchronized(self):
        """Gets the synchronized of this QueryDcDsBriefRespDTO.

        数采配置是否已同步，已同步：true,未同步：false

        :return: The synchronized of this QueryDcDsBriefRespDTO.
        :rtype: bool
        """
        return self._synchronized

    @synchronized.setter
    def synchronized(self, synchronized):
        """Sets the synchronized of this QueryDcDsBriefRespDTO.

        数采配置是否已同步，已同步：true,未同步：false

        :param synchronized: The synchronized of this QueryDcDsBriefRespDTO.
        :type synchronized: bool
        """
        self._synchronized = synchronized

    @property
    def synchronized_time(self):
        """Gets the synchronized_time of this QueryDcDsBriefRespDTO.

        数采配置同步时间

        :return: The synchronized_time of this QueryDcDsBriefRespDTO.
        :rtype: str
        """
        return self._synchronized_time

    @synchronized_time.setter
    def synchronized_time(self, synchronized_time):
        """Sets the synchronized_time of this QueryDcDsBriefRespDTO.

        数采配置同步时间

        :param synchronized_time: The synchronized_time of this QueryDcDsBriefRespDTO.
        :type synchronized_time: str
        """
        self._synchronized_time = synchronized_time

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
        if not isinstance(other, QueryDcDsBriefRespDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
