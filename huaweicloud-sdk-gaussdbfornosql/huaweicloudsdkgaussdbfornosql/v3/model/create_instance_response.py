# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceResponse(SdkResponse):

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
        'datastore': 'DatastoreResult',
        'name': 'str',
        'created': 'str',
        'status': 'str',
        'region': 'str',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'mode': 'str',
        'flavor': 'list[CreateInstanceFlavorResult]',
        'backup_strategy': 'BackupStrategyResult',
        'enterprise_project_id': 'str',
        'dedicated_resource_id': 'str',
        'ssl_option': 'str',
        'job_id': 'str',
        'order_id': 'str',
        'charge_info': 'ChargeInfoResult'
    }

    attribute_map = {
        'id': 'id',
        'datastore': 'datastore',
        'name': 'name',
        'created': 'created',
        'status': 'status',
        'region': 'region',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'mode': 'mode',
        'flavor': 'flavor',
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'dedicated_resource_id': 'dedicated_resource_id',
        'ssl_option': 'ssl_option',
        'job_id': 'job_id',
        'order_id': 'order_id',
        'charge_info': 'charge_info'
    }

    def __init__(self, id=None, datastore=None, name=None, created=None, status=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, mode=None, flavor=None, backup_strategy=None, enterprise_project_id=None, dedicated_resource_id=None, ssl_option=None, job_id=None, order_id=None, charge_info=None):
        r"""CreateInstanceResponse

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.DatastoreResult`
        :param name: 实例名称，与请求参数相同。
        :type name: str
        :param created: 创建时间为本地时间，格式为“yyyy-mm-dd hh:mm:ss”。
        :type created: str
        :param status: 实例状态，取值为“creating”。
        :type status: str
        :param region: 区域ID，与请求参数相同。
        :type region: str
        :param availability_zone: 可用区ID，与请求参数相同。
        :type availability_zone: str
        :param vpc_id: 虚拟私有云ID，与请求参数相同。
        :type vpc_id: str
        :param subnet_id: 子网ID，与请求参数相同。
        :type subnet_id: str
        :param security_group_id: 实例所属的安全组ID，与请求参数相同。
        :type security_group_id: str
        :param mode: 实例类型，与请求参数相同。
        :type mode: str
        :param flavor: 实例规格详情，与请求参数相同。
        :type flavor: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CreateInstanceFlavorResult`]
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdbfornosql.v3.BackupStrategyResult`
        :param enterprise_project_id: 企业项目ID。取值为“0”，表示为default企业项目。
        :type enterprise_project_id: str
        :param dedicated_resource_id: 专属资源ID，只有创建在专属资源上的实例才会返回该字段。
        :type dedicated_resource_id: str
        :param ssl_option: SSL开关选项，与请求参数相同。
        :type ssl_option: str
        :param job_id: 创建实例的任务ID, 仅创建按需实例时会返回该参数。
        :type job_id: str
        :param order_id: 创建实例的订单ID，仅创建包年包月时返回该参数。
        :type order_id: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdbfornosql.v3.ChargeInfoResult`
        """
        
        super(CreateInstanceResponse, self).__init__()

        self._id = None
        self._datastore = None
        self._name = None
        self._created = None
        self._status = None
        self._region = None
        self._availability_zone = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._mode = None
        self._flavor = None
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._dedicated_resource_id = None
        self._ssl_option = None
        self._job_id = None
        self._order_id = None
        self._charge_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if datastore is not None:
            self.datastore = datastore
        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if mode is not None:
            self.mode = mode
        if flavor is not None:
            self.flavor = flavor
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if dedicated_resource_id is not None:
            self.dedicated_resource_id = dedicated_resource_id
        if ssl_option is not None:
            self.ssl_option = ssl_option
        if job_id is not None:
            self.job_id = job_id
        if order_id is not None:
            self.order_id = order_id
        if charge_info is not None:
            self.charge_info = charge_info

    @property
    def id(self):
        r"""Gets the id of this CreateInstanceResponse.

        实例ID。

        :return: The id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateInstanceResponse.

        实例ID。

        :param id: The id of this CreateInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def datastore(self):
        r"""Gets the datastore of this CreateInstanceResponse.

        :return: The datastore of this CreateInstanceResponse.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DatastoreResult`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this CreateInstanceResponse.

        :param datastore: The datastore of this CreateInstanceResponse.
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.DatastoreResult`
        """
        self._datastore = datastore

    @property
    def name(self):
        r"""Gets the name of this CreateInstanceResponse.

        实例名称，与请求参数相同。

        :return: The name of this CreateInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateInstanceResponse.

        实例名称，与请求参数相同。

        :param name: The name of this CreateInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def created(self):
        r"""Gets the created of this CreateInstanceResponse.

        创建时间为本地时间，格式为“yyyy-mm-dd hh:mm:ss”。

        :return: The created of this CreateInstanceResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this CreateInstanceResponse.

        创建时间为本地时间，格式为“yyyy-mm-dd hh:mm:ss”。

        :param created: The created of this CreateInstanceResponse.
        :type created: str
        """
        self._created = created

    @property
    def status(self):
        r"""Gets the status of this CreateInstanceResponse.

        实例状态，取值为“creating”。

        :return: The status of this CreateInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateInstanceResponse.

        实例状态，取值为“creating”。

        :param status: The status of this CreateInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        r"""Gets the region of this CreateInstanceResponse.

        区域ID，与请求参数相同。

        :return: The region of this CreateInstanceResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateInstanceResponse.

        区域ID，与请求参数相同。

        :param region: The region of this CreateInstanceResponse.
        :type region: str
        """
        self._region = region

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateInstanceResponse.

        可用区ID，与请求参数相同。

        :return: The availability_zone of this CreateInstanceResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateInstanceResponse.

        可用区ID，与请求参数相同。

        :param availability_zone: The availability_zone of this CreateInstanceResponse.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateInstanceResponse.

        虚拟私有云ID，与请求参数相同。

        :return: The vpc_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateInstanceResponse.

        虚拟私有云ID，与请求参数相同。

        :param vpc_id: The vpc_id of this CreateInstanceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateInstanceResponse.

        子网ID，与请求参数相同。

        :return: The subnet_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateInstanceResponse.

        子网ID，与请求参数相同。

        :param subnet_id: The subnet_id of this CreateInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this CreateInstanceResponse.

        实例所属的安全组ID，与请求参数相同。

        :return: The security_group_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this CreateInstanceResponse.

        实例所属的安全组ID，与请求参数相同。

        :param security_group_id: The security_group_id of this CreateInstanceResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def mode(self):
        r"""Gets the mode of this CreateInstanceResponse.

        实例类型，与请求参数相同。

        :return: The mode of this CreateInstanceResponse.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateInstanceResponse.

        实例类型，与请求参数相同。

        :param mode: The mode of this CreateInstanceResponse.
        :type mode: str
        """
        self._mode = mode

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateInstanceResponse.

        实例规格详情，与请求参数相同。

        :return: The flavor of this CreateInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CreateInstanceFlavorResult`]
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateInstanceResponse.

        实例规格详情，与请求参数相同。

        :param flavor: The flavor of this CreateInstanceResponse.
        :type flavor: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CreateInstanceFlavorResult`]
        """
        self._flavor = flavor

    @property
    def backup_strategy(self):
        r"""Gets the backup_strategy of this CreateInstanceResponse.

        :return: The backup_strategy of this CreateInstanceResponse.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.BackupStrategyResult`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        r"""Sets the backup_strategy of this CreateInstanceResponse.

        :param backup_strategy: The backup_strategy of this CreateInstanceResponse.
        :type backup_strategy: :class:`huaweicloudsdkgaussdbfornosql.v3.BackupStrategyResult`
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateInstanceResponse.

        企业项目ID。取值为“0”，表示为default企业项目。

        :return: The enterprise_project_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateInstanceResponse.

        企业项目ID。取值为“0”，表示为default企业项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def dedicated_resource_id(self):
        r"""Gets the dedicated_resource_id of this CreateInstanceResponse.

        专属资源ID，只有创建在专属资源上的实例才会返回该字段。

        :return: The dedicated_resource_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        r"""Sets the dedicated_resource_id of this CreateInstanceResponse.

        专属资源ID，只有创建在专属资源上的实例才会返回该字段。

        :param dedicated_resource_id: The dedicated_resource_id of this CreateInstanceResponse.
        :type dedicated_resource_id: str
        """
        self._dedicated_resource_id = dedicated_resource_id

    @property
    def ssl_option(self):
        r"""Gets the ssl_option of this CreateInstanceResponse.

        SSL开关选项，与请求参数相同。

        :return: The ssl_option of this CreateInstanceResponse.
        :rtype: str
        """
        return self._ssl_option

    @ssl_option.setter
    def ssl_option(self, ssl_option):
        r"""Sets the ssl_option of this CreateInstanceResponse.

        SSL开关选项，与请求参数相同。

        :param ssl_option: The ssl_option of this CreateInstanceResponse.
        :type ssl_option: str
        """
        self._ssl_option = ssl_option

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateInstanceResponse.

        创建实例的任务ID, 仅创建按需实例时会返回该参数。

        :return: The job_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateInstanceResponse.

        创建实例的任务ID, 仅创建按需实例时会返回该参数。

        :param job_id: The job_id of this CreateInstanceResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateInstanceResponse.

        创建实例的订单ID，仅创建包年包月时返回该参数。

        :return: The order_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateInstanceResponse.

        创建实例的订单ID，仅创建包年包月时返回该参数。

        :param order_id: The order_id of this CreateInstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def charge_info(self):
        r"""Gets the charge_info of this CreateInstanceResponse.

        :return: The charge_info of this CreateInstanceResponse.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ChargeInfoResult`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this CreateInstanceResponse.

        :param charge_info: The charge_info of this CreateInstanceResponse.
        :type charge_info: :class:`huaweicloudsdkgaussdbfornosql.v3.ChargeInfoResult`
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
        if not isinstance(other, CreateInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
