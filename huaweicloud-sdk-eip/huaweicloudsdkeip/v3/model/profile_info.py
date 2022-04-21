# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProfileInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'local_network_port': 'str',
        'standalone': 'bool',
        'notify_status': 'str',
        'create_time': 'str',
        'fake_network_type': 'bool',
        'create_source': 'str',
        'ecs_id': 'str',
        'lock_status': 'str',
        'freezed_status': 'str',
        'bandwith_info': 'BandwidthInfoResp'
    }

    attribute_map = {
        'local_network_port': 'local_network_port',
        'standalone': 'standalone',
        'notify_status': 'notify_status',
        'create_time': 'create_time',
        'fake_network_type': 'fake_network_type',
        'create_source': 'create_source',
        'ecs_id': 'ecs_id',
        'lock_status': 'lock_status',
        'freezed_status': 'freezed_status',
        'bandwith_info': 'bandwith_info'
    }

    def __init__(self, local_network_port=None, standalone=None, notify_status=None, create_time=None, fake_network_type=None, create_source=None, ecs_id=None, lock_status=None, freezed_status=None, bandwith_info=None):
        """ProfileInfo

        The model defined in huaweicloud sdk

        :param local_network_port: 公网IP附属的5_xxx网络（如5_bgp）中的port_id
        :type local_network_port: str
        :param standalone: 标识公网IP是否是和虚机一起创建的。true-独立创建；false-和虚机一起创建
        :type standalone: bool
        :param notify_status: 云服务标识公网IP创建进度, EIP服务内部使用。
        :type notify_status: str
        :param create_time: 公网IP创建时间
        :type create_time: str
        :param fake_network_type: 该字段仅仅用于表示eip的bgp类型是否是真实的静态sbgp * 1. 如果为true，则该eip可以切换bgp类型 * 2. 如果为false，则该eip不可以切换bgp类型
        :type fake_network_type: bool
        :param create_source: 标识IP是和哪类资源一起购买的
        :type create_source: str
        :param ecs_id: 标识和公网IP一起购买的ecs的id
        :type ecs_id: str
        :param lock_status: 公网IP加锁状态, eg:\&quot;POLICE,LOCKED\&quot;。POLICE-公安冻结；LOCKED-普通冻结；普通冻结细分状态：ARREAR-欠费；DELABLE-可删除；
        :type lock_status: str
        :param freezed_status: 公网IP冻结状态。
        :type freezed_status: str
        :param bandwith_info: 
        :type bandwith_info: :class:`huaweicloudsdkeip.v3.BandwidthInfoResp`
        """
        
        

        self._local_network_port = None
        self._standalone = None
        self._notify_status = None
        self._create_time = None
        self._fake_network_type = None
        self._create_source = None
        self._ecs_id = None
        self._lock_status = None
        self._freezed_status = None
        self._bandwith_info = None
        self.discriminator = None

        if local_network_port is not None:
            self.local_network_port = local_network_port
        if standalone is not None:
            self.standalone = standalone
        if notify_status is not None:
            self.notify_status = notify_status
        if create_time is not None:
            self.create_time = create_time
        if fake_network_type is not None:
            self.fake_network_type = fake_network_type
        if create_source is not None:
            self.create_source = create_source
        if ecs_id is not None:
            self.ecs_id = ecs_id
        if lock_status is not None:
            self.lock_status = lock_status
        if freezed_status is not None:
            self.freezed_status = freezed_status
        if bandwith_info is not None:
            self.bandwith_info = bandwith_info

    @property
    def local_network_port(self):
        """Gets the local_network_port of this ProfileInfo.

        公网IP附属的5_xxx网络（如5_bgp）中的port_id

        :return: The local_network_port of this ProfileInfo.
        :rtype: str
        """
        return self._local_network_port

    @local_network_port.setter
    def local_network_port(self, local_network_port):
        """Sets the local_network_port of this ProfileInfo.

        公网IP附属的5_xxx网络（如5_bgp）中的port_id

        :param local_network_port: The local_network_port of this ProfileInfo.
        :type local_network_port: str
        """
        self._local_network_port = local_network_port

    @property
    def standalone(self):
        """Gets the standalone of this ProfileInfo.

        标识公网IP是否是和虚机一起创建的。true-独立创建；false-和虚机一起创建

        :return: The standalone of this ProfileInfo.
        :rtype: bool
        """
        return self._standalone

    @standalone.setter
    def standalone(self, standalone):
        """Sets the standalone of this ProfileInfo.

        标识公网IP是否是和虚机一起创建的。true-独立创建；false-和虚机一起创建

        :param standalone: The standalone of this ProfileInfo.
        :type standalone: bool
        """
        self._standalone = standalone

    @property
    def notify_status(self):
        """Gets the notify_status of this ProfileInfo.

        云服务标识公网IP创建进度, EIP服务内部使用。

        :return: The notify_status of this ProfileInfo.
        :rtype: str
        """
        return self._notify_status

    @notify_status.setter
    def notify_status(self, notify_status):
        """Sets the notify_status of this ProfileInfo.

        云服务标识公网IP创建进度, EIP服务内部使用。

        :param notify_status: The notify_status of this ProfileInfo.
        :type notify_status: str
        """
        self._notify_status = notify_status

    @property
    def create_time(self):
        """Gets the create_time of this ProfileInfo.

        公网IP创建时间

        :return: The create_time of this ProfileInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ProfileInfo.

        公网IP创建时间

        :param create_time: The create_time of this ProfileInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def fake_network_type(self):
        """Gets the fake_network_type of this ProfileInfo.

        该字段仅仅用于表示eip的bgp类型是否是真实的静态sbgp * 1. 如果为true，则该eip可以切换bgp类型 * 2. 如果为false，则该eip不可以切换bgp类型

        :return: The fake_network_type of this ProfileInfo.
        :rtype: bool
        """
        return self._fake_network_type

    @fake_network_type.setter
    def fake_network_type(self, fake_network_type):
        """Sets the fake_network_type of this ProfileInfo.

        该字段仅仅用于表示eip的bgp类型是否是真实的静态sbgp * 1. 如果为true，则该eip可以切换bgp类型 * 2. 如果为false，则该eip不可以切换bgp类型

        :param fake_network_type: The fake_network_type of this ProfileInfo.
        :type fake_network_type: bool
        """
        self._fake_network_type = fake_network_type

    @property
    def create_source(self):
        """Gets the create_source of this ProfileInfo.

        标识IP是和哪类资源一起购买的

        :return: The create_source of this ProfileInfo.
        :rtype: str
        """
        return self._create_source

    @create_source.setter
    def create_source(self, create_source):
        """Sets the create_source of this ProfileInfo.

        标识IP是和哪类资源一起购买的

        :param create_source: The create_source of this ProfileInfo.
        :type create_source: str
        """
        self._create_source = create_source

    @property
    def ecs_id(self):
        """Gets the ecs_id of this ProfileInfo.

        标识和公网IP一起购买的ecs的id

        :return: The ecs_id of this ProfileInfo.
        :rtype: str
        """
        return self._ecs_id

    @ecs_id.setter
    def ecs_id(self, ecs_id):
        """Sets the ecs_id of this ProfileInfo.

        标识和公网IP一起购买的ecs的id

        :param ecs_id: The ecs_id of this ProfileInfo.
        :type ecs_id: str
        """
        self._ecs_id = ecs_id

    @property
    def lock_status(self):
        """Gets the lock_status of this ProfileInfo.

        公网IP加锁状态, eg:\"POLICE,LOCKED\"。POLICE-公安冻结；LOCKED-普通冻结；普通冻结细分状态：ARREAR-欠费；DELABLE-可删除；

        :return: The lock_status of this ProfileInfo.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        """Sets the lock_status of this ProfileInfo.

        公网IP加锁状态, eg:\"POLICE,LOCKED\"。POLICE-公安冻结；LOCKED-普通冻结；普通冻结细分状态：ARREAR-欠费；DELABLE-可删除；

        :param lock_status: The lock_status of this ProfileInfo.
        :type lock_status: str
        """
        self._lock_status = lock_status

    @property
    def freezed_status(self):
        """Gets the freezed_status of this ProfileInfo.

        公网IP冻结状态。

        :return: The freezed_status of this ProfileInfo.
        :rtype: str
        """
        return self._freezed_status

    @freezed_status.setter
    def freezed_status(self, freezed_status):
        """Sets the freezed_status of this ProfileInfo.

        公网IP冻结状态。

        :param freezed_status: The freezed_status of this ProfileInfo.
        :type freezed_status: str
        """
        self._freezed_status = freezed_status

    @property
    def bandwith_info(self):
        """Gets the bandwith_info of this ProfileInfo.


        :return: The bandwith_info of this ProfileInfo.
        :rtype: :class:`huaweicloudsdkeip.v3.BandwidthInfoResp`
        """
        return self._bandwith_info

    @bandwith_info.setter
    def bandwith_info(self, bandwith_info):
        """Sets the bandwith_info of this ProfileInfo.


        :param bandwith_info: The bandwith_info of this ProfileInfo.
        :type bandwith_info: :class:`huaweicloudsdkeip.v3.BandwidthInfoResp`
        """
        self._bandwith_info = bandwith_info

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
        if not isinstance(other, ProfileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
