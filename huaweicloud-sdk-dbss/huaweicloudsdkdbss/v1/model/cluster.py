# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Cluster:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'activate_info': 'InstanceActivateInfo',
        'charge_model': 'str',
        'comment': 'str',
        'created': 'int',
        'deploy_mode': 'str',
        'detail': 'ServerList',
        'enterprise_project_id': 'str',
        'expired': 'int',
        'float_ip': 'str',
        'instance_id': 'str',
        'is_active_standby': 'bool',
        'keep_days': 'str',
        'name': 'str',
        'new_version': 'str',
        'public_ip': 'str',
        'remain_days': 'str'
    }

    attribute_map = {
        'activate_info': 'activate_info',
        'charge_model': 'charge_model',
        'comment': 'comment',
        'created': 'created',
        'deploy_mode': 'deploy_mode',
        'detail': 'detail',
        'enterprise_project_id': 'enterprise_project_id',
        'expired': 'expired',
        'float_ip': 'float_ip',
        'instance_id': 'instance_id',
        'is_active_standby': 'is_active_standby',
        'keep_days': 'keep_days',
        'name': 'name',
        'new_version': 'new_version',
        'public_ip': 'public_ip',
        'remain_days': 'remain_days'
    }

    def __init__(self, activate_info=None, charge_model=None, comment=None, created=None, deploy_mode=None, detail=None, enterprise_project_id=None, expired=None, float_ip=None, instance_id=None, is_active_standby=None, keep_days=None, name=None, new_version=None, public_ip=None, remain_days=None):
        r"""Cluster

        The model defined in huaweicloud sdk

        :param activate_info: 
        :type activate_info: :class:`huaweicloudsdkdbss.v1.InstanceActivateInfo`
        :param charge_model: 计费模式  - Period: 包周期  - Demand: 按需
        :type charge_model: str
        :param comment: 备注信息
        :type comment: str
        :param created: 创建时间
        :type created: int
        :param deploy_mode: 部署方式  - CLOUD: 云上  - OUTSIDE：云外
        :type deploy_mode: str
        :param detail: 
        :type detail: :class:`huaweicloudsdkdbss.v1.ServerList`
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param expired: 过期时间
        :type expired: int
        :param float_ip: 浮动IP
        :type float_ip: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param is_active_standby: 是否激活备用
        :type is_active_standby: bool
        :param keep_days: 使用天数
        :type keep_days: str
        :param name: 实例名称
        :type name: str
        :param new_version: 最新版本
        :type new_version: str
        :param public_ip: 公网IP
        :type public_ip: str
        :param remain_days: 剩余天数
        :type remain_days: str
        """
        
        

        self._activate_info = None
        self._charge_model = None
        self._comment = None
        self._created = None
        self._deploy_mode = None
        self._detail = None
        self._enterprise_project_id = None
        self._expired = None
        self._float_ip = None
        self._instance_id = None
        self._is_active_standby = None
        self._keep_days = None
        self._name = None
        self._new_version = None
        self._public_ip = None
        self._remain_days = None
        self.discriminator = None

        if activate_info is not None:
            self.activate_info = activate_info
        if charge_model is not None:
            self.charge_model = charge_model
        if comment is not None:
            self.comment = comment
        if created is not None:
            self.created = created
        if deploy_mode is not None:
            self.deploy_mode = deploy_mode
        if detail is not None:
            self.detail = detail
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if expired is not None:
            self.expired = expired
        if float_ip is not None:
            self.float_ip = float_ip
        if instance_id is not None:
            self.instance_id = instance_id
        if is_active_standby is not None:
            self.is_active_standby = is_active_standby
        if keep_days is not None:
            self.keep_days = keep_days
        if name is not None:
            self.name = name
        if new_version is not None:
            self.new_version = new_version
        if public_ip is not None:
            self.public_ip = public_ip
        if remain_days is not None:
            self.remain_days = remain_days

    @property
    def activate_info(self):
        r"""Gets the activate_info of this Cluster.

        :return: The activate_info of this Cluster.
        :rtype: :class:`huaweicloudsdkdbss.v1.InstanceActivateInfo`
        """
        return self._activate_info

    @activate_info.setter
    def activate_info(self, activate_info):
        r"""Sets the activate_info of this Cluster.

        :param activate_info: The activate_info of this Cluster.
        :type activate_info: :class:`huaweicloudsdkdbss.v1.InstanceActivateInfo`
        """
        self._activate_info = activate_info

    @property
    def charge_model(self):
        r"""Gets the charge_model of this Cluster.

        计费模式  - Period: 包周期  - Demand: 按需

        :return: The charge_model of this Cluster.
        :rtype: str
        """
        return self._charge_model

    @charge_model.setter
    def charge_model(self, charge_model):
        r"""Sets the charge_model of this Cluster.

        计费模式  - Period: 包周期  - Demand: 按需

        :param charge_model: The charge_model of this Cluster.
        :type charge_model: str
        """
        self._charge_model = charge_model

    @property
    def comment(self):
        r"""Gets the comment of this Cluster.

        备注信息

        :return: The comment of this Cluster.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this Cluster.

        备注信息

        :param comment: The comment of this Cluster.
        :type comment: str
        """
        self._comment = comment

    @property
    def created(self):
        r"""Gets the created of this Cluster.

        创建时间

        :return: The created of this Cluster.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this Cluster.

        创建时间

        :param created: The created of this Cluster.
        :type created: int
        """
        self._created = created

    @property
    def deploy_mode(self):
        r"""Gets the deploy_mode of this Cluster.

        部署方式  - CLOUD: 云上  - OUTSIDE：云外

        :return: The deploy_mode of this Cluster.
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        r"""Sets the deploy_mode of this Cluster.

        部署方式  - CLOUD: 云上  - OUTSIDE：云外

        :param deploy_mode: The deploy_mode of this Cluster.
        :type deploy_mode: str
        """
        self._deploy_mode = deploy_mode

    @property
    def detail(self):
        r"""Gets the detail of this Cluster.

        :return: The detail of this Cluster.
        :rtype: :class:`huaweicloudsdkdbss.v1.ServerList`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this Cluster.

        :param detail: The detail of this Cluster.
        :type detail: :class:`huaweicloudsdkdbss.v1.ServerList`
        """
        self._detail = detail

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Cluster.

        企业项目ID

        :return: The enterprise_project_id of this Cluster.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Cluster.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this Cluster.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def expired(self):
        r"""Gets the expired of this Cluster.

        过期时间

        :return: The expired of this Cluster.
        :rtype: int
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        r"""Sets the expired of this Cluster.

        过期时间

        :param expired: The expired of this Cluster.
        :type expired: int
        """
        self._expired = expired

    @property
    def float_ip(self):
        r"""Gets the float_ip of this Cluster.

        浮动IP

        :return: The float_ip of this Cluster.
        :rtype: str
        """
        return self._float_ip

    @float_ip.setter
    def float_ip(self, float_ip):
        r"""Sets the float_ip of this Cluster.

        浮动IP

        :param float_ip: The float_ip of this Cluster.
        :type float_ip: str
        """
        self._float_ip = float_ip

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Cluster.

        实例ID

        :return: The instance_id of this Cluster.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Cluster.

        实例ID

        :param instance_id: The instance_id of this Cluster.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def is_active_standby(self):
        r"""Gets the is_active_standby of this Cluster.

        是否激活备用

        :return: The is_active_standby of this Cluster.
        :rtype: bool
        """
        return self._is_active_standby

    @is_active_standby.setter
    def is_active_standby(self, is_active_standby):
        r"""Sets the is_active_standby of this Cluster.

        是否激活备用

        :param is_active_standby: The is_active_standby of this Cluster.
        :type is_active_standby: bool
        """
        self._is_active_standby = is_active_standby

    @property
    def keep_days(self):
        r"""Gets the keep_days of this Cluster.

        使用天数

        :return: The keep_days of this Cluster.
        :rtype: str
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this Cluster.

        使用天数

        :param keep_days: The keep_days of this Cluster.
        :type keep_days: str
        """
        self._keep_days = keep_days

    @property
    def name(self):
        r"""Gets the name of this Cluster.

        实例名称

        :return: The name of this Cluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Cluster.

        实例名称

        :param name: The name of this Cluster.
        :type name: str
        """
        self._name = name

    @property
    def new_version(self):
        r"""Gets the new_version of this Cluster.

        最新版本

        :return: The new_version of this Cluster.
        :rtype: str
        """
        return self._new_version

    @new_version.setter
    def new_version(self, new_version):
        r"""Sets the new_version of this Cluster.

        最新版本

        :param new_version: The new_version of this Cluster.
        :type new_version: str
        """
        self._new_version = new_version

    @property
    def public_ip(self):
        r"""Gets the public_ip of this Cluster.

        公网IP

        :return: The public_ip of this Cluster.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this Cluster.

        公网IP

        :param public_ip: The public_ip of this Cluster.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def remain_days(self):
        r"""Gets the remain_days of this Cluster.

        剩余天数

        :return: The remain_days of this Cluster.
        :rtype: str
        """
        return self._remain_days

    @remain_days.setter
    def remain_days(self, remain_days):
        r"""Sets the remain_days of this Cluster.

        剩余天数

        :param remain_days: The remain_days of this Cluster.
        :type remain_days: str
        """
        self._remain_days = remain_days

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
        if not isinstance(other, Cluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
