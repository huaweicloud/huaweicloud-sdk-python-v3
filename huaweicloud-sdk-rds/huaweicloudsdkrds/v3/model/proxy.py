# coding: utf-8

import pprint
import re

import six





class Proxy:


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
        'elb_vip': 'str',
        'eip': 'str',
        'port': 'str',
        'pool_status': 'str',
        'delay_threshold_in_kilobytes': 'str',
        'cpu': 'str',
        'mem': 'str',
        'node_num': 'str',
        'nodes': 'ProxyNode',
        'mode': 'str'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'status': 'status',
        'address': 'address',
        'elb_vip': 'elb_vip',
        'eip': 'eip',
        'port': 'port',
        'pool_status': 'pool_status',
        'delay_threshold_in_kilobytes': 'delay_threshold_in_kilobytes',
        'cpu': 'cpu',
        'mem': 'mem',
        'node_num': 'node_num',
        'nodes': 'nodes',
        'mode': 'mode'
    }

    def __init__(self, pool_id=None, status=None, address=None, elb_vip=None, eip=None, port=None, pool_status=None, delay_threshold_in_kilobytes=None, cpu=None, mem=None, node_num=None, nodes=None, mode=None):
        """Proxy - a model defined in huaweicloud sdk"""
        
        

        self._pool_id = None
        self._status = None
        self._address = None
        self._elb_vip = None
        self._eip = None
        self._port = None
        self._pool_status = None
        self._delay_threshold_in_kilobytes = None
        self._cpu = None
        self._mem = None
        self._node_num = None
        self._nodes = None
        self._mode = None
        self.discriminator = None

        self.pool_id = pool_id
        self.status = status
        self.address = address
        self.elb_vip = elb_vip
        self.eip = eip
        self.port = port
        self.pool_status = pool_status
        self.delay_threshold_in_kilobytes = delay_threshold_in_kilobytes
        self.cpu = cpu
        self.mem = mem
        self.node_num = node_num
        self.nodes = nodes
        self.mode = mode

    @property
    def pool_id(self):
        """Gets the pool_id of this Proxy.

        Proxy实例id。

        :return: The pool_id of this Proxy.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this Proxy.

        Proxy实例id。

        :param pool_id: The pool_id of this Proxy.
        :type: str
        """
        self._pool_id = pool_id

    @property
    def status(self):
        """Gets the status of this Proxy.

        Proxy实例开启状态。取值范围：open、closed、frozen、 opening 、closing、freezing、unfreezing，分别对应打开、关闭、已冻结、打开中、关闭中、冻结中、解冻中。

        :return: The status of this Proxy.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Proxy.

        Proxy实例开启状态。取值范围：open、closed、frozen、 opening 、closing、freezing、unfreezing，分别对应打开、关闭、已冻结、打开中、关闭中、冻结中、解冻中。

        :param status: The status of this Proxy.
        :type: str
        """
        self._status = status

    @property
    def address(self):
        """Gets the address of this Proxy.

        Proxy读写分离地址。

        :return: The address of this Proxy.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Proxy.

        Proxy读写分离地址。

        :param address: The address of this Proxy.
        :type: str
        """
        self._address = address

    @property
    def elb_vip(self):
        """Gets the elb_vip of this Proxy.

        elb模式的虚拟ip信息。

        :return: The elb_vip of this Proxy.
        :rtype: str
        """
        return self._elb_vip

    @elb_vip.setter
    def elb_vip(self, elb_vip):
        """Sets the elb_vip of this Proxy.

        elb模式的虚拟ip信息。

        :param elb_vip: The elb_vip of this Proxy.
        :type: str
        """
        self._elb_vip = elb_vip

    @property
    def eip(self):
        """Gets the eip of this Proxy.

        弹性公网ip信息。

        :return: The eip of this Proxy.
        :rtype: str
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this Proxy.

        弹性公网ip信息。

        :param eip: The eip of this Proxy.
        :type: str
        """
        self._eip = eip

    @property
    def port(self):
        """Gets the port of this Proxy.

        Proxy端口信息。

        :return: The port of this Proxy.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Proxy.

        Proxy端口信息。

        :param port: The port of this Proxy.
        :type: str
        """
        self._port = port

    @property
    def pool_status(self):
        """Gets the pool_status of this Proxy.

        Proxy实例状态。 取值范围：creating、normal、deleted

        :return: The pool_status of this Proxy.
        :rtype: str
        """
        return self._pool_status

    @pool_status.setter
    def pool_status(self, pool_status):
        """Sets the pool_status of this Proxy.

        Proxy实例状态。 取值范围：creating、normal、deleted

        :param pool_status: The pool_status of this Proxy.
        :type: str
        """
        self._pool_status = pool_status

    @property
    def delay_threshold_in_kilobytes(self):
        """Gets the delay_threshold_in_kilobytes of this Proxy.

        延时阈值，单位是Byte。

        :return: The delay_threshold_in_kilobytes of this Proxy.
        :rtype: str
        """
        return self._delay_threshold_in_kilobytes

    @delay_threshold_in_kilobytes.setter
    def delay_threshold_in_kilobytes(self, delay_threshold_in_kilobytes):
        """Sets the delay_threshold_in_kilobytes of this Proxy.

        延时阈值，单位是Byte。

        :param delay_threshold_in_kilobytes: The delay_threshold_in_kilobytes of this Proxy.
        :type: str
        """
        self._delay_threshold_in_kilobytes = delay_threshold_in_kilobytes

    @property
    def cpu(self):
        """Gets the cpu of this Proxy.

        Proxy实例规格的cpu数

        :return: The cpu of this Proxy.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this Proxy.

        Proxy实例规格的cpu数

        :param cpu: The cpu of this Proxy.
        :type: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        """Gets the mem of this Proxy.

        Proxy实例规格的内存数。

        :return: The mem of this Proxy.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this Proxy.

        Proxy实例规格的内存数。

        :param mem: The mem of this Proxy.
        :type: str
        """
        self._mem = mem

    @property
    def node_num(self):
        """Gets the node_num of this Proxy.

        Proxy节点个数

        :return: The node_num of this Proxy.
        :rtype: str
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this Proxy.

        Proxy节点个数

        :param node_num: The node_num of this Proxy.
        :type: str
        """
        self._node_num = node_num

    @property
    def nodes(self):
        """Gets the nodes of this Proxy.


        :return: The nodes of this Proxy.
        :rtype: ProxyNode
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this Proxy.


        :param nodes: The nodes of this Proxy.
        :type: ProxyNode
        """
        self._nodes = nodes

    @property
    def mode(self):
        """Gets the mode of this Proxy.

        Proxy主备模式，取值范围：Ha

        :return: The mode of this Proxy.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Proxy.

        Proxy主备模式，取值范围：Ha

        :param mode: The mode of this Proxy.
        :type: str
        """
        self._mode = mode

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Proxy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
