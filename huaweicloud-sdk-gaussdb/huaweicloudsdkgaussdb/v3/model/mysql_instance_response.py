# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlInstanceResponse:

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
        'datastore': 'MysqlDatastore',
        'mode': 'str',
        'configuration_id': 'str',
        'port': 'str',
        'backup_strategy': 'MysqlBackupStrategy',
        'enterprise_project_id': 'str',
        'region': 'str',
        'availability_zone_mode': 'str',
        'master_availability_zone': 'str',
        'vpc_id': 'str',
        'security_group_id': 'str',
        'subnet_id': 'str',
        'flavor_ref': 'str',
        'charge_info': 'MysqlChargeInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'datastore': 'datastore',
        'mode': 'mode',
        'configuration_id': 'configuration_id',
        'port': 'port',
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'region': 'region',
        'availability_zone_mode': 'availability_zone_mode',
        'master_availability_zone': 'master_availability_zone',
        'vpc_id': 'vpc_id',
        'security_group_id': 'security_group_id',
        'subnet_id': 'subnet_id',
        'flavor_ref': 'flavor_ref',
        'charge_info': 'charge_info'
    }

    def __init__(self, id=None, name=None, status=None, datastore=None, mode=None, configuration_id=None, port=None, backup_strategy=None, enterprise_project_id=None, region=None, availability_zone_mode=None, master_availability_zone=None, vpc_id=None, security_group_id=None, subnet_id=None, flavor_ref=None, charge_info=None):
        """MysqlInstanceResponse

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。用于表示实例的名称，同一租户下，同类型的实例名称可相同。  取值范围：4~64个字符之间，必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线, 不能包含其它的特殊字符。
        :type name: str
        :param status: 实例状态。
        :type status: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastore`
        :param mode: 实例类型，仅支持Cluster。
        :type mode: str
        :param configuration_id: 参数组ID。
        :type configuration_id: str
        :param port: 数据库端口信息。
        :type port: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param region: 区域ID，与请求参数相同。
        :type region: str
        :param availability_zone_mode: 可用区模式，与请求参数相同。
        :type availability_zone_mode: str
        :param master_availability_zone: 主可用区ID。
        :type master_availability_zone: str
        :param vpc_id: 虚拟私有云ID，与请求参数相同。
        :type vpc_id: str
        :param security_group_id: 安全组ID，与请求参数相同。
        :type security_group_id: str
        :param subnet_id: 子网ID，与请求参数相同。
        :type subnet_id: str
        :param flavor_ref: 规格码，与请求参数相同。
        :type flavor_ref: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdb.v3.MysqlChargeInfo`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._datastore = None
        self._mode = None
        self._configuration_id = None
        self._port = None
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._region = None
        self._availability_zone_mode = None
        self._master_availability_zone = None
        self._vpc_id = None
        self._security_group_id = None
        self._subnet_id = None
        self._flavor_ref = None
        self._charge_info = None
        self.discriminator = None

        self.id = id
        self.name = name
        if status is not None:
            self.status = status
        if datastore is not None:
            self.datastore = datastore
        if mode is not None:
            self.mode = mode
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if port is not None:
            self.port = port
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if region is not None:
            self.region = region
        if availability_zone_mode is not None:
            self.availability_zone_mode = availability_zone_mode
        if master_availability_zone is not None:
            self.master_availability_zone = master_availability_zone
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if charge_info is not None:
            self.charge_info = charge_info

    @property
    def id(self):
        """Gets the id of this MysqlInstanceResponse.

        实例ID。

        :return: The id of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MysqlInstanceResponse.

        实例ID。

        :param id: The id of this MysqlInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this MysqlInstanceResponse.

        实例名称。用于表示实例的名称，同一租户下，同类型的实例名称可相同。  取值范围：4~64个字符之间，必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线, 不能包含其它的特殊字符。

        :return: The name of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MysqlInstanceResponse.

        实例名称。用于表示实例的名称，同一租户下，同类型的实例名称可相同。  取值范围：4~64个字符之间，必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线, 不能包含其它的特殊字符。

        :param name: The name of this MysqlInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this MysqlInstanceResponse.

        实例状态。

        :return: The status of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MysqlInstanceResponse.

        实例状态。

        :param status: The status of this MysqlInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def datastore(self):
        """Gets the datastore of this MysqlInstanceResponse.

        :return: The datastore of this MysqlInstanceResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this MysqlInstanceResponse.

        :param datastore: The datastore of this MysqlInstanceResponse.
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastore`
        """
        self._datastore = datastore

    @property
    def mode(self):
        """Gets the mode of this MysqlInstanceResponse.

        实例类型，仅支持Cluster。

        :return: The mode of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this MysqlInstanceResponse.

        实例类型，仅支持Cluster。

        :param mode: The mode of this MysqlInstanceResponse.
        :type mode: str
        """
        self._mode = mode

    @property
    def configuration_id(self):
        """Gets the configuration_id of this MysqlInstanceResponse.

        参数组ID。

        :return: The configuration_id of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this MysqlInstanceResponse.

        参数组ID。

        :param configuration_id: The configuration_id of this MysqlInstanceResponse.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def port(self):
        """Gets the port of this MysqlInstanceResponse.

        数据库端口信息。

        :return: The port of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this MysqlInstanceResponse.

        数据库端口信息。

        :param port: The port of this MysqlInstanceResponse.
        :type port: str
        """
        self._port = port

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this MysqlInstanceResponse.

        :return: The backup_strategy of this MysqlInstanceResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this MysqlInstanceResponse.

        :param backup_strategy: The backup_strategy of this MysqlInstanceResponse.
        :type backup_strategy: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this MysqlInstanceResponse.

        企业项目ID。

        :return: The enterprise_project_id of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this MysqlInstanceResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this MysqlInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def region(self):
        """Gets the region of this MysqlInstanceResponse.

        区域ID，与请求参数相同。

        :return: The region of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this MysqlInstanceResponse.

        区域ID，与请求参数相同。

        :param region: The region of this MysqlInstanceResponse.
        :type region: str
        """
        self._region = region

    @property
    def availability_zone_mode(self):
        """Gets the availability_zone_mode of this MysqlInstanceResponse.

        可用区模式，与请求参数相同。

        :return: The availability_zone_mode of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._availability_zone_mode

    @availability_zone_mode.setter
    def availability_zone_mode(self, availability_zone_mode):
        """Sets the availability_zone_mode of this MysqlInstanceResponse.

        可用区模式，与请求参数相同。

        :param availability_zone_mode: The availability_zone_mode of this MysqlInstanceResponse.
        :type availability_zone_mode: str
        """
        self._availability_zone_mode = availability_zone_mode

    @property
    def master_availability_zone(self):
        """Gets the master_availability_zone of this MysqlInstanceResponse.

        主可用区ID。

        :return: The master_availability_zone of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._master_availability_zone

    @master_availability_zone.setter
    def master_availability_zone(self, master_availability_zone):
        """Sets the master_availability_zone of this MysqlInstanceResponse.

        主可用区ID。

        :param master_availability_zone: The master_availability_zone of this MysqlInstanceResponse.
        :type master_availability_zone: str
        """
        self._master_availability_zone = master_availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this MysqlInstanceResponse.

        虚拟私有云ID，与请求参数相同。

        :return: The vpc_id of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this MysqlInstanceResponse.

        虚拟私有云ID，与请求参数相同。

        :param vpc_id: The vpc_id of this MysqlInstanceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this MysqlInstanceResponse.

        安全组ID，与请求参数相同。

        :return: The security_group_id of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this MysqlInstanceResponse.

        安全组ID，与请求参数相同。

        :param security_group_id: The security_group_id of this MysqlInstanceResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this MysqlInstanceResponse.

        子网ID，与请求参数相同。

        :return: The subnet_id of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this MysqlInstanceResponse.

        子网ID，与请求参数相同。

        :param subnet_id: The subnet_id of this MysqlInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this MysqlInstanceResponse.

        规格码，与请求参数相同。

        :return: The flavor_ref of this MysqlInstanceResponse.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this MysqlInstanceResponse.

        规格码，与请求参数相同。

        :param flavor_ref: The flavor_ref of this MysqlInstanceResponse.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def charge_info(self):
        """Gets the charge_info of this MysqlInstanceResponse.

        :return: The charge_info of this MysqlInstanceResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this MysqlInstanceResponse.

        :param charge_info: The charge_info of this MysqlInstanceResponse.
        :type charge_info: :class:`huaweicloudsdkgaussdb.v3.MysqlChargeInfo`
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
        if not isinstance(other, MysqlInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
