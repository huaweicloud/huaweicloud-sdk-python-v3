# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceResponse(SdkResponse):

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
        'description': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'spec': 'str',
        'version': 'str',
        'charge_mode': 'str',
        'access_address': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'expires_at': 'str',
        'status': 'str',
        'obs_bucket_name': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'user_def_obs': 'bool',
        'product_id': 'str',
        'order_id': 'str',
        'vpc_name': 'str',
        'vpc_cidr': 'str',
        'subnet_name': 'str',
        'subnet_cidr': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'spec': 'spec',
        'version': 'version',
        'charge_mode': 'charge_mode',
        'access_address': 'access_address',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'expires_at': 'expires_at',
        'status': 'status',
        'obs_bucket_name': 'obs_bucket_name',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'user_def_obs': 'user_def_obs',
        'product_id': 'product_id',
        'order_id': 'order_id',
        'vpc_name': 'vpc_name',
        'vpc_cidr': 'vpc_cidr',
        'subnet_name': 'subnet_name',
        'subnet_cidr': 'subnet_cidr'
    }

    def __init__(self, id=None, name=None, description=None, vpc_id=None, subnet_id=None, spec=None, version=None, charge_mode=None, access_address=None, created_at=None, updated_at=None, expires_at=None, status=None, obs_bucket_name=None, project_id=None, enterprise_project_id=None, user_def_obs=None, product_id=None, order_id=None, vpc_name=None, vpc_cidr=None, subnet_name=None, subnet_cidr=None):
        r"""ShowInstanceResponse

        The model defined in huaweicloud sdk

        :param id: 实例ID
        :type id: str
        :param name: 实例名称
        :type name: str
        :param description: 实例描述
        :type description: str
        :param vpc_id: 用户虚拟私有云ID
        :type vpc_id: str
        :param subnet_id: 用户子网的网络ID
        :type subnet_id: str
        :param spec: 实例规格
        :type spec: str
        :param version: 实例版本
        :type version: str
        :param charge_mode: 实例计费模式
        :type charge_mode: str
        :param access_address: 访问地址
        :type access_address: str
        :param created_at: 实例创建时间
        :type created_at: str
        :param updated_at: 实例更新时间
        :type updated_at: str
        :param expires_at: 实例过期时间
        :type expires_at: str
        :param status: 实例状态
        :type status: str
        :param obs_bucket_name: obs桶名称
        :type obs_bucket_name: str
        :param project_id: 项目ID
        :type project_id: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param user_def_obs: 是否为用户指定obs桶
        :type user_def_obs: bool
        :param product_id: 产品ID
        :type product_id: str
        :param order_id: 订单ID，包周期预留字段
        :type order_id: str
        :param vpc_name: VPC的名称
        :type vpc_name: str
        :param vpc_cidr: VPC的可用子网的范围
        :type vpc_cidr: str
        :param subnet_name: VPC的子网名称
        :type subnet_name: str
        :param subnet_cidr: 子网的网段
        :type subnet_cidr: str
        """
        
        super(ShowInstanceResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._vpc_id = None
        self._subnet_id = None
        self._spec = None
        self._version = None
        self._charge_mode = None
        self._access_address = None
        self._created_at = None
        self._updated_at = None
        self._expires_at = None
        self._status = None
        self._obs_bucket_name = None
        self._project_id = None
        self._enterprise_project_id = None
        self._user_def_obs = None
        self._product_id = None
        self._order_id = None
        self._vpc_name = None
        self._vpc_cidr = None
        self._subnet_name = None
        self._subnet_cidr = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if spec is not None:
            self.spec = spec
        if version is not None:
            self.version = version
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if access_address is not None:
            self.access_address = access_address
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if expires_at is not None:
            self.expires_at = expires_at
        if status is not None:
            self.status = status
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if project_id is not None:
            self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if user_def_obs is not None:
            self.user_def_obs = user_def_obs
        if product_id is not None:
            self.product_id = product_id
        if order_id is not None:
            self.order_id = order_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if vpc_cidr is not None:
            self.vpc_cidr = vpc_cidr
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if subnet_cidr is not None:
            self.subnet_cidr = subnet_cidr

    @property
    def id(self):
        r"""Gets the id of this ShowInstanceResponse.

        实例ID

        :return: The id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowInstanceResponse.

        实例ID

        :param id: The id of this ShowInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowInstanceResponse.

        实例名称

        :return: The name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowInstanceResponse.

        实例名称

        :param name: The name of this ShowInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowInstanceResponse.

        实例描述

        :return: The description of this ShowInstanceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowInstanceResponse.

        实例描述

        :param description: The description of this ShowInstanceResponse.
        :type description: str
        """
        self._description = description

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ShowInstanceResponse.

        用户虚拟私有云ID

        :return: The vpc_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ShowInstanceResponse.

        用户虚拟私有云ID

        :param vpc_id: The vpc_id of this ShowInstanceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ShowInstanceResponse.

        用户子网的网络ID

        :return: The subnet_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ShowInstanceResponse.

        用户子网的网络ID

        :param subnet_id: The subnet_id of this ShowInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def spec(self):
        r"""Gets the spec of this ShowInstanceResponse.

        实例规格

        :return: The spec of this ShowInstanceResponse.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ShowInstanceResponse.

        实例规格

        :param spec: The spec of this ShowInstanceResponse.
        :type spec: str
        """
        self._spec = spec

    @property
    def version(self):
        r"""Gets the version of this ShowInstanceResponse.

        实例版本

        :return: The version of this ShowInstanceResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowInstanceResponse.

        实例版本

        :param version: The version of this ShowInstanceResponse.
        :type version: str
        """
        self._version = version

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this ShowInstanceResponse.

        实例计费模式

        :return: The charge_mode of this ShowInstanceResponse.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this ShowInstanceResponse.

        实例计费模式

        :param charge_mode: The charge_mode of this ShowInstanceResponse.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def access_address(self):
        r"""Gets the access_address of this ShowInstanceResponse.

        访问地址

        :return: The access_address of this ShowInstanceResponse.
        :rtype: str
        """
        return self._access_address

    @access_address.setter
    def access_address(self, access_address):
        r"""Sets the access_address of this ShowInstanceResponse.

        访问地址

        :param access_address: The access_address of this ShowInstanceResponse.
        :type access_address: str
        """
        self._access_address = access_address

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowInstanceResponse.

        实例创建时间

        :return: The created_at of this ShowInstanceResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowInstanceResponse.

        实例创建时间

        :param created_at: The created_at of this ShowInstanceResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowInstanceResponse.

        实例更新时间

        :return: The updated_at of this ShowInstanceResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowInstanceResponse.

        实例更新时间

        :param updated_at: The updated_at of this ShowInstanceResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def expires_at(self):
        r"""Gets the expires_at of this ShowInstanceResponse.

        实例过期时间

        :return: The expires_at of this ShowInstanceResponse.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this ShowInstanceResponse.

        实例过期时间

        :param expires_at: The expires_at of this ShowInstanceResponse.
        :type expires_at: str
        """
        self._expires_at = expires_at

    @property
    def status(self):
        r"""Gets the status of this ShowInstanceResponse.

        实例状态

        :return: The status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInstanceResponse.

        实例状态

        :param status: The status of this ShowInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this ShowInstanceResponse.

        obs桶名称

        :return: The obs_bucket_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this ShowInstanceResponse.

        obs桶名称

        :param obs_bucket_name: The obs_bucket_name of this ShowInstanceResponse.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowInstanceResponse.

        项目ID

        :return: The project_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowInstanceResponse.

        项目ID

        :param project_id: The project_id of this ShowInstanceResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowInstanceResponse.

        企业项目ID

        :return: The enterprise_project_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowInstanceResponse.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def user_def_obs(self):
        r"""Gets the user_def_obs of this ShowInstanceResponse.

        是否为用户指定obs桶

        :return: The user_def_obs of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._user_def_obs

    @user_def_obs.setter
    def user_def_obs(self, user_def_obs):
        r"""Sets the user_def_obs of this ShowInstanceResponse.

        是否为用户指定obs桶

        :param user_def_obs: The user_def_obs of this ShowInstanceResponse.
        :type user_def_obs: bool
        """
        self._user_def_obs = user_def_obs

    @property
    def product_id(self):
        r"""Gets the product_id of this ShowInstanceResponse.

        产品ID

        :return: The product_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ShowInstanceResponse.

        产品ID

        :param product_id: The product_id of this ShowInstanceResponse.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def order_id(self):
        r"""Gets the order_id of this ShowInstanceResponse.

        订单ID，包周期预留字段

        :return: The order_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ShowInstanceResponse.

        订单ID，包周期预留字段

        :param order_id: The order_id of this ShowInstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this ShowInstanceResponse.

        VPC的名称

        :return: The vpc_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this ShowInstanceResponse.

        VPC的名称

        :param vpc_name: The vpc_name of this ShowInstanceResponse.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def vpc_cidr(self):
        r"""Gets the vpc_cidr of this ShowInstanceResponse.

        VPC的可用子网的范围

        :return: The vpc_cidr of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc_cidr

    @vpc_cidr.setter
    def vpc_cidr(self, vpc_cidr):
        r"""Sets the vpc_cidr of this ShowInstanceResponse.

        VPC的可用子网的范围

        :param vpc_cidr: The vpc_cidr of this ShowInstanceResponse.
        :type vpc_cidr: str
        """
        self._vpc_cidr = vpc_cidr

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this ShowInstanceResponse.

        VPC的子网名称

        :return: The subnet_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this ShowInstanceResponse.

        VPC的子网名称

        :param subnet_name: The subnet_name of this ShowInstanceResponse.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def subnet_cidr(self):
        r"""Gets the subnet_cidr of this ShowInstanceResponse.

        子网的网段

        :return: The subnet_cidr of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        r"""Sets the subnet_cidr of this ShowInstanceResponse.

        子网的网段

        :param subnet_cidr: The subnet_cidr of this ShowInstanceResponse.
        :type subnet_cidr: str
        """
        self._subnet_cidr = subnet_cidr

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
        if not isinstance(other, ShowInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
