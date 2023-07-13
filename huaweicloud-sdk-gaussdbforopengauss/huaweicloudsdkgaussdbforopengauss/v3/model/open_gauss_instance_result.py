# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussInstanceResult:

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
        'datastore': 'OpenGaussDatastoreResult',
        'ha': 'OpenGaussHaResult',
        'replica_num': 'int',
        'backup_strategy': 'OpenGaussBackupStrategyForResponse',
        'port': 'str',
        'enterprise_project_id': 'str',
        'flavor_ref': 'str',
        'volume': 'OpenGaussVolumeResult',
        'region': 'str',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'charge_info': 'OpenGaussChargeInfoResponse'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'datastore': 'datastore',
        'ha': 'ha',
        'replica_num': 'replica_num',
        'backup_strategy': 'backup_strategy',
        'port': 'port',
        'enterprise_project_id': 'enterprise_project_id',
        'flavor_ref': 'flavor_ref',
        'volume': 'volume',
        'region': 'region',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'charge_info': 'charge_info'
    }

    def __init__(self, id=None, name=None, status=None, datastore=None, ha=None, replica_num=None, backup_strategy=None, port=None, enterprise_project_id=None, flavor_ref=None, volume=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, charge_info=None):
        """OpenGaussInstanceResult

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。用于表示实例的名称，同一租户下，同类型的实例名称可相同。  取值范围：4~64个字符之间，必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。
        :type name: str
        :param status: 实例状态。如BUILD，表示创建中。  仅创建按需实例时会返回该参数。
        :type status: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussDatastoreResult`
        :param ha: 
        :type ha: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussHaResult`
        :param replica_num: 实例副本数。
        :type replica_num: int
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategyForResponse`
        :param port: 数据库端口信息，与请求参数相同。
        :type port: str
        :param enterprise_project_id: 项目标签。
        :type enterprise_project_id: str
        :param flavor_ref: 规格码，取值范围：非空。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB的“规格编码”列内容获取。
        :type flavor_ref: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolumeResult`
        :param region: 区域ID。
        :type region: str
        :param availability_zone: 可用区ID。
        :type availability_zone: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID信息。
        :type subnet_id: str
        :param security_group_id: 实例所属的安全组。
        :type security_group_id: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfoResponse`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._datastore = None
        self._ha = None
        self._replica_num = None
        self._backup_strategy = None
        self._port = None
        self._enterprise_project_id = None
        self._flavor_ref = None
        self._volume = None
        self._region = None
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
        if ha is not None:
            self.ha = ha
        if replica_num is not None:
            self.replica_num = replica_num
        self.backup_strategy = backup_strategy
        self.port = port
        self.enterprise_project_id = enterprise_project_id
        self.flavor_ref = flavor_ref
        self.volume = volume
        self.region = region
        self.availability_zone = availability_zone
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.charge_info = charge_info

    @property
    def id(self):
        """Gets the id of this OpenGaussInstanceResult.

        实例ID。

        :return: The id of this OpenGaussInstanceResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OpenGaussInstanceResult.

        实例ID。

        :param id: The id of this OpenGaussInstanceResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this OpenGaussInstanceResult.

        实例名称。用于表示实例的名称，同一租户下，同类型的实例名称可相同。  取值范围：4~64个字符之间，必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :return: The name of this OpenGaussInstanceResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenGaussInstanceResult.

        实例名称。用于表示实例的名称，同一租户下，同类型的实例名称可相同。  取值范围：4~64个字符之间，必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :param name: The name of this OpenGaussInstanceResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this OpenGaussInstanceResult.

        实例状态。如BUILD，表示创建中。  仅创建按需实例时会返回该参数。

        :return: The status of this OpenGaussInstanceResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OpenGaussInstanceResult.

        实例状态。如BUILD，表示创建中。  仅创建按需实例时会返回该参数。

        :param status: The status of this OpenGaussInstanceResult.
        :type status: str
        """
        self._status = status

    @property
    def datastore(self):
        """Gets the datastore of this OpenGaussInstanceResult.

        :return: The datastore of this OpenGaussInstanceResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussDatastoreResult`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this OpenGaussInstanceResult.

        :param datastore: The datastore of this OpenGaussInstanceResult.
        :type datastore: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussDatastoreResult`
        """
        self._datastore = datastore

    @property
    def ha(self):
        """Gets the ha of this OpenGaussInstanceResult.

        :return: The ha of this OpenGaussInstanceResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussHaResult`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this OpenGaussInstanceResult.

        :param ha: The ha of this OpenGaussInstanceResult.
        :type ha: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussHaResult`
        """
        self._ha = ha

    @property
    def replica_num(self):
        """Gets the replica_num of this OpenGaussInstanceResult.

        实例副本数。

        :return: The replica_num of this OpenGaussInstanceResult.
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        """Sets the replica_num of this OpenGaussInstanceResult.

        实例副本数。

        :param replica_num: The replica_num of this OpenGaussInstanceResult.
        :type replica_num: int
        """
        self._replica_num = replica_num

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this OpenGaussInstanceResult.

        :return: The backup_strategy of this OpenGaussInstanceResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategyForResponse`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this OpenGaussInstanceResult.

        :param backup_strategy: The backup_strategy of this OpenGaussInstanceResult.
        :type backup_strategy: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategyForResponse`
        """
        self._backup_strategy = backup_strategy

    @property
    def port(self):
        """Gets the port of this OpenGaussInstanceResult.

        数据库端口信息，与请求参数相同。

        :return: The port of this OpenGaussInstanceResult.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this OpenGaussInstanceResult.

        数据库端口信息，与请求参数相同。

        :param port: The port of this OpenGaussInstanceResult.
        :type port: str
        """
        self._port = port

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this OpenGaussInstanceResult.

        项目标签。

        :return: The enterprise_project_id of this OpenGaussInstanceResult.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this OpenGaussInstanceResult.

        项目标签。

        :param enterprise_project_id: The enterprise_project_id of this OpenGaussInstanceResult.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this OpenGaussInstanceResult.

        规格码，取值范围：非空。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB的“规格编码”列内容获取。

        :return: The flavor_ref of this OpenGaussInstanceResult.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this OpenGaussInstanceResult.

        规格码，取值范围：非空。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB的“规格编码”列内容获取。

        :param flavor_ref: The flavor_ref of this OpenGaussInstanceResult.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        """Gets the volume of this OpenGaussInstanceResult.

        :return: The volume of this OpenGaussInstanceResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolumeResult`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this OpenGaussInstanceResult.

        :param volume: The volume of this OpenGaussInstanceResult.
        :type volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolumeResult`
        """
        self._volume = volume

    @property
    def region(self):
        """Gets the region of this OpenGaussInstanceResult.

        区域ID。

        :return: The region of this OpenGaussInstanceResult.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this OpenGaussInstanceResult.

        区域ID。

        :param region: The region of this OpenGaussInstanceResult.
        :type region: str
        """
        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this OpenGaussInstanceResult.

        可用区ID。

        :return: The availability_zone of this OpenGaussInstanceResult.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this OpenGaussInstanceResult.

        可用区ID。

        :param availability_zone: The availability_zone of this OpenGaussInstanceResult.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this OpenGaussInstanceResult.

        虚拟私有云ID。

        :return: The vpc_id of this OpenGaussInstanceResult.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this OpenGaussInstanceResult.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this OpenGaussInstanceResult.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this OpenGaussInstanceResult.

        子网的网络ID信息。

        :return: The subnet_id of this OpenGaussInstanceResult.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this OpenGaussInstanceResult.

        子网的网络ID信息。

        :param subnet_id: The subnet_id of this OpenGaussInstanceResult.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this OpenGaussInstanceResult.

        实例所属的安全组。

        :return: The security_group_id of this OpenGaussInstanceResult.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this OpenGaussInstanceResult.

        实例所属的安全组。

        :param security_group_id: The security_group_id of this OpenGaussInstanceResult.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def charge_info(self):
        """Gets the charge_info of this OpenGaussInstanceResult.

        :return: The charge_info of this OpenGaussInstanceResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfoResponse`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this OpenGaussInstanceResult.

        :param charge_info: The charge_info of this OpenGaussInstanceResult.
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfoResponse`
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
        if not isinstance(other, OpenGaussInstanceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
