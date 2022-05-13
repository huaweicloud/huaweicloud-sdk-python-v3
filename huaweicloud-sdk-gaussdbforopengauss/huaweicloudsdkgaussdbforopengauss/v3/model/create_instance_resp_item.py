# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceRespItem:

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
        'datastore': 'OpenGaussDatastoreResponse',
        'ha': 'OpenGaussHaResponse',
        'port': 'str',
        'volume': 'OpenGaussVolumeResponse',
        'replica_num': 'int',
        'region': 'str',
        'backup_strategy': 'OpenGaussBackupStrategyForResponse',
        'flavor_ref': 'str',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'charge_info': 'OpenGaussChargeInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'datastore': 'datastore',
        'ha': 'ha',
        'port': 'port',
        'volume': 'volume',
        'replica_num': 'replica_num',
        'region': 'region',
        'backup_strategy': 'backup_strategy',
        'flavor_ref': 'flavor_ref',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'charge_info': 'charge_info'
    }

    def __init__(self, id=None, name=None, status=None, datastore=None, ha=None, port=None, volume=None, replica_num=None, region=None, backup_strategy=None, flavor_ref=None, availability_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, charge_info=None):
        """CreateInstanceRespItem

        The model defined in huaweicloud sdk

        :param id: 实例id
        :type id: str
        :param name: 实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。 取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。
        :type name: str
        :param status: 实例状态。如BUILD，表示创建中。 仅创建按需实例时会返回该参数。
        :type status: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussDatastoreResponse`
        :param ha: 
        :type ha: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussHaResponse`
        :param port: 数据库端口信息。 当不传该参数时，默认端口8000。
        :type port: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolumeResponse`
        :param replica_num: 实例副本数。
        :type replica_num: int
        :param region: 区域ID。创建主实例时必选，其它场景不可选。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。
        :type region: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategyForResponse`
        :param flavor_ref: 规格码。
        :type flavor_ref: str
        :param availability_zone: 可用区ID。GaussDB(for openGauss)取值范围：非空，可选部署在同一可用区或三个不同可用区，可用区之间用逗号隔开。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。
        :type availability_zone: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfo`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._datastore = None
        self._ha = None
        self._port = None
        self._volume = None
        self._replica_num = None
        self._region = None
        self._backup_strategy = None
        self._flavor_ref = None
        self._availability_zone = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._charge_info = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.datastore = datastore
        self.ha = ha
        self.port = port
        self.volume = volume
        self.replica_num = replica_num
        self.region = region
        self.backup_strategy = backup_strategy
        self.flavor_ref = flavor_ref
        self.availability_zone = availability_zone
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.charge_info = charge_info

    @property
    def id(self):
        """Gets the id of this CreateInstanceRespItem.

        实例id

        :return: The id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateInstanceRespItem.

        实例id

        :param id: The id of this CreateInstanceRespItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateInstanceRespItem.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。 取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :return: The name of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceRespItem.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。 取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :param name: The name of this CreateInstanceRespItem.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this CreateInstanceRespItem.

        实例状态。如BUILD，表示创建中。 仅创建按需实例时会返回该参数。

        :return: The status of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateInstanceRespItem.

        实例状态。如BUILD，表示创建中。 仅创建按需实例时会返回该参数。

        :param status: The status of this CreateInstanceRespItem.
        :type status: str
        """
        self._status = status

    @property
    def datastore(self):
        """Gets the datastore of this CreateInstanceRespItem.


        :return: The datastore of this CreateInstanceRespItem.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussDatastoreResponse`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this CreateInstanceRespItem.


        :param datastore: The datastore of this CreateInstanceRespItem.
        :type datastore: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussDatastoreResponse`
        """
        self._datastore = datastore

    @property
    def ha(self):
        """Gets the ha of this CreateInstanceRespItem.


        :return: The ha of this CreateInstanceRespItem.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussHaResponse`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this CreateInstanceRespItem.


        :param ha: The ha of this CreateInstanceRespItem.
        :type ha: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussHaResponse`
        """
        self._ha = ha

    @property
    def port(self):
        """Gets the port of this CreateInstanceRespItem.

        数据库端口信息。 当不传该参数时，默认端口8000。

        :return: The port of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateInstanceRespItem.

        数据库端口信息。 当不传该参数时，默认端口8000。

        :param port: The port of this CreateInstanceRespItem.
        :type port: str
        """
        self._port = port

    @property
    def volume(self):
        """Gets the volume of this CreateInstanceRespItem.


        :return: The volume of this CreateInstanceRespItem.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolumeResponse`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this CreateInstanceRespItem.


        :param volume: The volume of this CreateInstanceRespItem.
        :type volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolumeResponse`
        """
        self._volume = volume

    @property
    def replica_num(self):
        """Gets the replica_num of this CreateInstanceRespItem.

        实例副本数。

        :return: The replica_num of this CreateInstanceRespItem.
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        """Sets the replica_num of this CreateInstanceRespItem.

        实例副本数。

        :param replica_num: The replica_num of this CreateInstanceRespItem.
        :type replica_num: int
        """
        self._replica_num = replica_num

    @property
    def region(self):
        """Gets the region of this CreateInstanceRespItem.

        区域ID。创建主实例时必选，其它场景不可选。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The region of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateInstanceRespItem.

        区域ID。创建主实例时必选，其它场景不可选。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param region: The region of this CreateInstanceRespItem.
        :type region: str
        """
        self._region = region

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this CreateInstanceRespItem.


        :return: The backup_strategy of this CreateInstanceRespItem.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategyForResponse`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this CreateInstanceRespItem.


        :param backup_strategy: The backup_strategy of this CreateInstanceRespItem.
        :type backup_strategy: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategyForResponse`
        """
        self._backup_strategy = backup_strategy

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this CreateInstanceRespItem.

        规格码。

        :return: The flavor_ref of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this CreateInstanceRespItem.

        规格码。

        :param flavor_ref: The flavor_ref of this CreateInstanceRespItem.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateInstanceRespItem.

        可用区ID。GaussDB(for openGauss)取值范围：非空，可选部署在同一可用区或三个不同可用区，可用区之间用逗号隔开。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The availability_zone of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateInstanceRespItem.

        可用区ID。GaussDB(for openGauss)取值范围：非空，可选部署在同一可用区或三个不同可用区，可用区之间用逗号隔开。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param availability_zone: The availability_zone of this CreateInstanceRespItem.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateInstanceRespItem.

        虚拟私有云ID。

        :return: The vpc_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateInstanceRespItem.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this CreateInstanceRespItem.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateInstanceRespItem.

        子网ID。

        :return: The subnet_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateInstanceRespItem.

        子网ID。

        :param subnet_id: The subnet_id of this CreateInstanceRespItem.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateInstanceRespItem.

        安全组ID。

        :return: The security_group_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateInstanceRespItem.

        安全组ID。

        :param security_group_id: The security_group_id of this CreateInstanceRespItem.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def charge_info(self):
        """Gets the charge_info of this CreateInstanceRespItem.


        :return: The charge_info of this CreateInstanceRespItem.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this CreateInstanceRespItem.


        :param charge_info: The charge_info of this CreateInstanceRespItem.
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfo`
        """
        self._charge_info = charge_info

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
        if not isinstance(other, CreateInstanceRespItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
