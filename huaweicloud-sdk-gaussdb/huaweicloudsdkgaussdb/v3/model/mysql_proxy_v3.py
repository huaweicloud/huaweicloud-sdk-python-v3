# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlProxyV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'status': 'str',
        'address': 'str',
        'port': 'int',
        'pool_status': 'str',
        'delay_threshold_in_seconds': 'int',
        'elb_vip': 'str',
        'eip': 'str',
        'vcpus': 'str',
        'ram': 'str',
        'node_num': 'int',
        'mode': 'str',
        'nodes': 'list[MysqlProxyNodes]',
        'flavor_ref': 'str',
        'name': 'str',
        'transaction_split': 'str'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'status': 'status',
        'address': 'address',
        'port': 'port',
        'pool_status': 'pool_status',
        'delay_threshold_in_seconds': 'delay_threshold_in_seconds',
        'elb_vip': 'elb_vip',
        'eip': 'eip',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'node_num': 'node_num',
        'mode': 'mode',
        'nodes': 'nodes',
        'flavor_ref': 'flavor_ref',
        'name': 'name',
        'transaction_split': 'transaction_split'
    }

    def __init__(self, pool_id=None, status=None, address=None, port=None, pool_status=None, delay_threshold_in_seconds=None, elb_vip=None, eip=None, vcpus=None, ram=None, node_num=None, mode=None, nodes=None, flavor_ref=None, name=None, transaction_split=None):
        """MysqlProxyV3

        The model defined in huaweicloud sdk

        :param pool_id: Proxy实例id。
        :type pool_id: str
        :param status: Proxy实例开启状态。  取值: 值为“ACTIVE”，表示数据库代理正常； “FAILED”，表示数据库代理创建失败； “DELETED”，表示数据库代理已删除； “ABNORMAL”，表示数据库代理异常； “ENABLING PROXY”，表示数据库代理正在开启； “DISABLING PROXY”，表示数据库代理正在关闭； “ADDING PROXY NODE”，表示数据库代理正在扩容； “DELETING READ REPLICAS FROM PROXY”，表示数据库代理正在移除只读节点； “ADDING READ REPLICAS TO PROXY”，表示数据库代理正在添加只读节点； “CHANGING WEIGHTS”，表示数据库代理正在修改只读节点权重。
        :type status: str
        :param address: Proxy读写分离地址。
        :type address: str
        :param port: Proxy端口信息。
        :type port: int
        :param pool_status: Proxy实例状态。 取值范围：ACTIVE、ABNORMAL、FAILED和DELETED。
        :type pool_status: str
        :param delay_threshold_in_seconds: 延时阈值，单位：秒。
        :type delay_threshold_in_seconds: int
        :param elb_vip: Elb模式的虚拟ip信息。
        :type elb_vip: str
        :param eip: 弹性公网IP信息。
        :type eip: str
        :param vcpus: Proxy实例规格的CPU数量。
        :type vcpus: str
        :param ram: Proxy实例规格的内存数量。
        :type ram: str
        :param node_num: Proxy节点个数。
        :type node_num: int
        :param mode: Proxy主备模式，取值范围：Cluster。
        :type mode: str
        :param nodes: Proxy节点信息。
        :type nodes: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyNodes`]
        :param flavor_ref: Proxy规格信息。
        :type flavor_ref: str
        :param name: Proxy实例名称。
        :type name: str
        :param transaction_split: Proxy事务拆分开关状态【ON/OFF】。
        :type transaction_split: str
        """
        
        

        self._pool_id = None
        self._status = None
        self._address = None
        self._port = None
        self._pool_status = None
        self._delay_threshold_in_seconds = None
        self._elb_vip = None
        self._eip = None
        self._vcpus = None
        self._ram = None
        self._node_num = None
        self._mode = None
        self._nodes = None
        self._flavor_ref = None
        self._name = None
        self._transaction_split = None
        self.discriminator = None

        if pool_id is not None:
            self.pool_id = pool_id
        if status is not None:
            self.status = status
        if address is not None:
            self.address = address
        if port is not None:
            self.port = port
        if pool_status is not None:
            self.pool_status = pool_status
        if delay_threshold_in_seconds is not None:
            self.delay_threshold_in_seconds = delay_threshold_in_seconds
        if elb_vip is not None:
            self.elb_vip = elb_vip
        if eip is not None:
            self.eip = eip
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if node_num is not None:
            self.node_num = node_num
        if mode is not None:
            self.mode = mode
        if nodes is not None:
            self.nodes = nodes
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if name is not None:
            self.name = name
        if transaction_split is not None:
            self.transaction_split = transaction_split

    @property
    def pool_id(self):
        """Gets the pool_id of this MysqlProxyV3.

        Proxy实例id。

        :return: The pool_id of this MysqlProxyV3.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this MysqlProxyV3.

        Proxy实例id。

        :param pool_id: The pool_id of this MysqlProxyV3.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def status(self):
        """Gets the status of this MysqlProxyV3.

        Proxy实例开启状态。  取值: 值为“ACTIVE”，表示数据库代理正常； “FAILED”，表示数据库代理创建失败； “DELETED”，表示数据库代理已删除； “ABNORMAL”，表示数据库代理异常； “ENABLING PROXY”，表示数据库代理正在开启； “DISABLING PROXY”，表示数据库代理正在关闭； “ADDING PROXY NODE”，表示数据库代理正在扩容； “DELETING READ REPLICAS FROM PROXY”，表示数据库代理正在移除只读节点； “ADDING READ REPLICAS TO PROXY”，表示数据库代理正在添加只读节点； “CHANGING WEIGHTS”，表示数据库代理正在修改只读节点权重。

        :return: The status of this MysqlProxyV3.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MysqlProxyV3.

        Proxy实例开启状态。  取值: 值为“ACTIVE”，表示数据库代理正常； “FAILED”，表示数据库代理创建失败； “DELETED”，表示数据库代理已删除； “ABNORMAL”，表示数据库代理异常； “ENABLING PROXY”，表示数据库代理正在开启； “DISABLING PROXY”，表示数据库代理正在关闭； “ADDING PROXY NODE”，表示数据库代理正在扩容； “DELETING READ REPLICAS FROM PROXY”，表示数据库代理正在移除只读节点； “ADDING READ REPLICAS TO PROXY”，表示数据库代理正在添加只读节点； “CHANGING WEIGHTS”，表示数据库代理正在修改只读节点权重。

        :param status: The status of this MysqlProxyV3.
        :type status: str
        """
        self._status = status

    @property
    def address(self):
        """Gets the address of this MysqlProxyV3.

        Proxy读写分离地址。

        :return: The address of this MysqlProxyV3.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MysqlProxyV3.

        Proxy读写分离地址。

        :param address: The address of this MysqlProxyV3.
        :type address: str
        """
        self._address = address

    @property
    def port(self):
        """Gets the port of this MysqlProxyV3.

        Proxy端口信息。

        :return: The port of this MysqlProxyV3.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this MysqlProxyV3.

        Proxy端口信息。

        :param port: The port of this MysqlProxyV3.
        :type port: int
        """
        self._port = port

    @property
    def pool_status(self):
        """Gets the pool_status of this MysqlProxyV3.

        Proxy实例状态。 取值范围：ACTIVE、ABNORMAL、FAILED和DELETED。

        :return: The pool_status of this MysqlProxyV3.
        :rtype: str
        """
        return self._pool_status

    @pool_status.setter
    def pool_status(self, pool_status):
        """Sets the pool_status of this MysqlProxyV3.

        Proxy实例状态。 取值范围：ACTIVE、ABNORMAL、FAILED和DELETED。

        :param pool_status: The pool_status of this MysqlProxyV3.
        :type pool_status: str
        """
        self._pool_status = pool_status

    @property
    def delay_threshold_in_seconds(self):
        """Gets the delay_threshold_in_seconds of this MysqlProxyV3.

        延时阈值，单位：秒。

        :return: The delay_threshold_in_seconds of this MysqlProxyV3.
        :rtype: int
        """
        return self._delay_threshold_in_seconds

    @delay_threshold_in_seconds.setter
    def delay_threshold_in_seconds(self, delay_threshold_in_seconds):
        """Sets the delay_threshold_in_seconds of this MysqlProxyV3.

        延时阈值，单位：秒。

        :param delay_threshold_in_seconds: The delay_threshold_in_seconds of this MysqlProxyV3.
        :type delay_threshold_in_seconds: int
        """
        self._delay_threshold_in_seconds = delay_threshold_in_seconds

    @property
    def elb_vip(self):
        """Gets the elb_vip of this MysqlProxyV3.

        Elb模式的虚拟ip信息。

        :return: The elb_vip of this MysqlProxyV3.
        :rtype: str
        """
        return self._elb_vip

    @elb_vip.setter
    def elb_vip(self, elb_vip):
        """Sets the elb_vip of this MysqlProxyV3.

        Elb模式的虚拟ip信息。

        :param elb_vip: The elb_vip of this MysqlProxyV3.
        :type elb_vip: str
        """
        self._elb_vip = elb_vip

    @property
    def eip(self):
        """Gets the eip of this MysqlProxyV3.

        弹性公网IP信息。

        :return: The eip of this MysqlProxyV3.
        :rtype: str
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this MysqlProxyV3.

        弹性公网IP信息。

        :param eip: The eip of this MysqlProxyV3.
        :type eip: str
        """
        self._eip = eip

    @property
    def vcpus(self):
        """Gets the vcpus of this MysqlProxyV3.

        Proxy实例规格的CPU数量。

        :return: The vcpus of this MysqlProxyV3.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this MysqlProxyV3.

        Proxy实例规格的CPU数量。

        :param vcpus: The vcpus of this MysqlProxyV3.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this MysqlProxyV3.

        Proxy实例规格的内存数量。

        :return: The ram of this MysqlProxyV3.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this MysqlProxyV3.

        Proxy实例规格的内存数量。

        :param ram: The ram of this MysqlProxyV3.
        :type ram: str
        """
        self._ram = ram

    @property
    def node_num(self):
        """Gets the node_num of this MysqlProxyV3.

        Proxy节点个数。

        :return: The node_num of this MysqlProxyV3.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this MysqlProxyV3.

        Proxy节点个数。

        :param node_num: The node_num of this MysqlProxyV3.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def mode(self):
        """Gets the mode of this MysqlProxyV3.

        Proxy主备模式，取值范围：Cluster。

        :return: The mode of this MysqlProxyV3.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this MysqlProxyV3.

        Proxy主备模式，取值范围：Cluster。

        :param mode: The mode of this MysqlProxyV3.
        :type mode: str
        """
        self._mode = mode

    @property
    def nodes(self):
        """Gets the nodes of this MysqlProxyV3.

        Proxy节点信息。

        :return: The nodes of this MysqlProxyV3.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyNodes`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this MysqlProxyV3.

        Proxy节点信息。

        :param nodes: The nodes of this MysqlProxyV3.
        :type nodes: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyNodes`]
        """
        self._nodes = nodes

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this MysqlProxyV3.

        Proxy规格信息。

        :return: The flavor_ref of this MysqlProxyV3.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this MysqlProxyV3.

        Proxy规格信息。

        :param flavor_ref: The flavor_ref of this MysqlProxyV3.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def name(self):
        """Gets the name of this MysqlProxyV3.

        Proxy实例名称。

        :return: The name of this MysqlProxyV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MysqlProxyV3.

        Proxy实例名称。

        :param name: The name of this MysqlProxyV3.
        :type name: str
        """
        self._name = name

    @property
    def transaction_split(self):
        """Gets the transaction_split of this MysqlProxyV3.

        Proxy事务拆分开关状态【ON/OFF】。

        :return: The transaction_split of this MysqlProxyV3.
        :rtype: str
        """
        return self._transaction_split

    @transaction_split.setter
    def transaction_split(self, transaction_split):
        """Sets the transaction_split of this MysqlProxyV3.

        Proxy事务拆分开关状态【ON/OFF】。

        :param transaction_split: The transaction_split of this MysqlProxyV3.
        :type transaction_split: str
        """
        self._transaction_split = transaction_split

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
        if not isinstance(other, MysqlProxyV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
