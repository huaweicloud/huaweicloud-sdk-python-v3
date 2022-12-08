# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CBHInstances:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_ref': 'str',
        'flavor_ref': 'str',
        'instance_name': 'str',
        'name': 'str',
        'personality': 'Personality',
        'user_data': 'str',
        'admin_password': 'str',
        'key_name': 'str',
        'vpc_id': 'str',
        'nics': 'list[Nics]',
        'public_ip': 'PublicIp',
        'count': 'int',
        'root_volume': 'RootVolume',
        'data_volumes': 'DataVolumes',
        'security_groups': 'list[SecurityGroup]',
        'availability_zone': 'str',
        'slave_availability_zone': 'str',
        'extend_param': 'ExtendParam',
        'metadata': 'str',
        'comment': 'str',
        'region': 'str',
        'region_id': 'str',
        'resource_spec_code': 'str',
        'hx_password': 'str',
        'bastion_type': 'str',
        'ipv6_enable': 'bool',
        'end_time': 'str'
    }

    attribute_map = {
        'image_ref': 'image_ref',
        'flavor_ref': 'flavor_ref',
        'instance_name': 'instance_name',
        'name': 'name',
        'personality': 'personality',
        'user_data': 'user_data',
        'admin_password': 'admin_password',
        'key_name': 'key_name',
        'vpc_id': 'vpc_id',
        'nics': 'nics',
        'public_ip': 'public_ip',
        'count': 'count',
        'root_volume': 'root_volume',
        'data_volumes': 'data_volumes',
        'security_groups': 'security_groups',
        'availability_zone': 'availability_zone',
        'slave_availability_zone': 'slave_availability_zone',
        'extend_param': 'extend_param',
        'metadata': 'metadata',
        'comment': 'comment',
        'region': 'region',
        'region_id': 'region_id',
        'resource_spec_code': 'resource_spec_code',
        'hx_password': 'hx_password',
        'bastion_type': 'bastion_type',
        'ipv6_enable': 'ipv6_enable',
        'end_time': 'end_time'
    }

    def __init__(self, image_ref=None, flavor_ref=None, instance_name=None, name=None, personality=None, user_data=None, admin_password=None, key_name=None, vpc_id=None, nics=None, public_ip=None, count=None, root_volume=None, data_volumes=None, security_groups=None, availability_zone=None, slave_availability_zone=None, extend_param=None, metadata=None, comment=None, region=None, region_id=None, resource_spec_code=None, hx_password=None, bastion_type=None, ipv6_enable=None, end_time=None):
        """CBHInstances

        The model defined in huaweicloud sdk

        :param image_ref: 镜像ID
        :type image_ref: str
        :param flavor_ref: 规格ID
        :type flavor_ref: str
        :param instance_name: 堡垒机实例名称
        :type instance_name: str
        :param name: 名字
        :type name: str
        :param personality: 
        :type personality: :class:`huaweicloudsdkcbh.v1.Personality`
        :param user_data: 注入用户数据
        :type user_data: str
        :param admin_password: 初始登录密码
        :type admin_password: str
        :param key_name: 管理员SSH秘钥登录
        :type key_name: str
        :param vpc_id: VPC ID
        :type vpc_id: str
        :param nics: 网卡信息
        :type nics: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkcbh.v1.PublicIp`
        :param count: 弹性数量
        :type count: int
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkcbh.v1.RootVolume`
        :param data_volumes: 
        :type data_volumes: :class:`huaweicloudsdkcbh.v1.DataVolumes`
        :param security_groups: 网卡信息
        :type security_groups: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        :param availability_zone: 分区信息
        :type availability_zone: str
        :param slave_availability_zone: 备用区
        :type slave_availability_zone: str
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcbh.v1.ExtendParam`
        :param metadata: 创建云服务云数据
        :type metadata: str
        :param comment: 描述
        :type comment: str
        :param region: 云服务所在区域ID
        :type region: str
        :param region_id: region标识
        :type region_id: str
        :param resource_spec_code: 资源规格
        :type resource_spec_code: str
        :param hx_password: 前端登录密码
        :type hx_password: str
        :param bastion_type: 堡垒机机机型
        :type bastion_type: str
        :param ipv6_enable: 分区信息
        :type ipv6_enable: bool
        :param end_time: 订购截止日期
        :type end_time: str
        """
        
        

        self._image_ref = None
        self._flavor_ref = None
        self._instance_name = None
        self._name = None
        self._personality = None
        self._user_data = None
        self._admin_password = None
        self._key_name = None
        self._vpc_id = None
        self._nics = None
        self._public_ip = None
        self._count = None
        self._root_volume = None
        self._data_volumes = None
        self._security_groups = None
        self._availability_zone = None
        self._slave_availability_zone = None
        self._extend_param = None
        self._metadata = None
        self._comment = None
        self._region = None
        self._region_id = None
        self._resource_spec_code = None
        self._hx_password = None
        self._bastion_type = None
        self._ipv6_enable = None
        self._end_time = None
        self.discriminator = None

        if image_ref is not None:
            self.image_ref = image_ref
        self.flavor_ref = flavor_ref
        self.instance_name = instance_name
        if name is not None:
            self.name = name
        if personality is not None:
            self.personality = personality
        if user_data is not None:
            self.user_data = user_data
        if admin_password is not None:
            self.admin_password = admin_password
        if key_name is not None:
            self.key_name = key_name
        self.vpc_id = vpc_id
        self.nics = nics
        self.public_ip = public_ip
        if count is not None:
            self.count = count
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        self.security_groups = security_groups
        self.availability_zone = availability_zone
        self.slave_availability_zone = slave_availability_zone
        if extend_param is not None:
            self.extend_param = extend_param
        if metadata is not None:
            self.metadata = metadata
        if comment is not None:
            self.comment = comment
        self.region = region
        if region_id is not None:
            self.region_id = region_id
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        self.hx_password = hx_password
        self.bastion_type = bastion_type
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if end_time is not None:
            self.end_time = end_time

    @property
    def image_ref(self):
        """Gets the image_ref of this CBHInstances.

        镜像ID

        :return: The image_ref of this CBHInstances.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this CBHInstances.

        镜像ID

        :param image_ref: The image_ref of this CBHInstances.
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this CBHInstances.

        规格ID

        :return: The flavor_ref of this CBHInstances.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this CBHInstances.

        规格ID

        :param flavor_ref: The flavor_ref of this CBHInstances.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def instance_name(self):
        """Gets the instance_name of this CBHInstances.

        堡垒机实例名称

        :return: The instance_name of this CBHInstances.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this CBHInstances.

        堡垒机实例名称

        :param instance_name: The instance_name of this CBHInstances.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def name(self):
        """Gets the name of this CBHInstances.

        名字

        :return: The name of this CBHInstances.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CBHInstances.

        名字

        :param name: The name of this CBHInstances.
        :type name: str
        """
        self._name = name

    @property
    def personality(self):
        """Gets the personality of this CBHInstances.

        :return: The personality of this CBHInstances.
        :rtype: :class:`huaweicloudsdkcbh.v1.Personality`
        """
        return self._personality

    @personality.setter
    def personality(self, personality):
        """Sets the personality of this CBHInstances.

        :param personality: The personality of this CBHInstances.
        :type personality: :class:`huaweicloudsdkcbh.v1.Personality`
        """
        self._personality = personality

    @property
    def user_data(self):
        """Gets the user_data of this CBHInstances.

        注入用户数据

        :return: The user_data of this CBHInstances.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CBHInstances.

        注入用户数据

        :param user_data: The user_data of this CBHInstances.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def admin_password(self):
        """Gets the admin_password of this CBHInstances.

        初始登录密码

        :return: The admin_password of this CBHInstances.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """Sets the admin_password of this CBHInstances.

        初始登录密码

        :param admin_password: The admin_password of this CBHInstances.
        :type admin_password: str
        """
        self._admin_password = admin_password

    @property
    def key_name(self):
        """Gets the key_name of this CBHInstances.

        管理员SSH秘钥登录

        :return: The key_name of this CBHInstances.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this CBHInstances.

        管理员SSH秘钥登录

        :param key_name: The key_name of this CBHInstances.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CBHInstances.

        VPC ID

        :return: The vpc_id of this CBHInstances.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CBHInstances.

        VPC ID

        :param vpc_id: The vpc_id of this CBHInstances.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def nics(self):
        """Gets the nics of this CBHInstances.

        网卡信息

        :return: The nics of this CBHInstances.
        :rtype: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this CBHInstances.

        网卡信息

        :param nics: The nics of this CBHInstances.
        :type nics: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        """
        self._nics = nics

    @property
    def public_ip(self):
        """Gets the public_ip of this CBHInstances.

        :return: The public_ip of this CBHInstances.
        :rtype: :class:`huaweicloudsdkcbh.v1.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this CBHInstances.

        :param public_ip: The public_ip of this CBHInstances.
        :type public_ip: :class:`huaweicloudsdkcbh.v1.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def count(self):
        """Gets the count of this CBHInstances.

        弹性数量

        :return: The count of this CBHInstances.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CBHInstances.

        弹性数量

        :param count: The count of this CBHInstances.
        :type count: int
        """
        self._count = count

    @property
    def root_volume(self):
        """Gets the root_volume of this CBHInstances.

        :return: The root_volume of this CBHInstances.
        :rtype: :class:`huaweicloudsdkcbh.v1.RootVolume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this CBHInstances.

        :param root_volume: The root_volume of this CBHInstances.
        :type root_volume: :class:`huaweicloudsdkcbh.v1.RootVolume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        """Gets the data_volumes of this CBHInstances.

        :return: The data_volumes of this CBHInstances.
        :rtype: :class:`huaweicloudsdkcbh.v1.DataVolumes`
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this CBHInstances.

        :param data_volumes: The data_volumes of this CBHInstances.
        :type data_volumes: :class:`huaweicloudsdkcbh.v1.DataVolumes`
        """
        self._data_volumes = data_volumes

    @property
    def security_groups(self):
        """Gets the security_groups of this CBHInstances.

        网卡信息

        :return: The security_groups of this CBHInstances.
        :rtype: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this CBHInstances.

        网卡信息

        :param security_groups: The security_groups of this CBHInstances.
        :type security_groups: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CBHInstances.

        分区信息

        :return: The availability_zone of this CBHInstances.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CBHInstances.

        分区信息

        :param availability_zone: The availability_zone of this CBHInstances.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def slave_availability_zone(self):
        """Gets the slave_availability_zone of this CBHInstances.

        备用区

        :return: The slave_availability_zone of this CBHInstances.
        :rtype: str
        """
        return self._slave_availability_zone

    @slave_availability_zone.setter
    def slave_availability_zone(self, slave_availability_zone):
        """Sets the slave_availability_zone of this CBHInstances.

        备用区

        :param slave_availability_zone: The slave_availability_zone of this CBHInstances.
        :type slave_availability_zone: str
        """
        self._slave_availability_zone = slave_availability_zone

    @property
    def extend_param(self):
        """Gets the extend_param of this CBHInstances.

        :return: The extend_param of this CBHInstances.
        :rtype: :class:`huaweicloudsdkcbh.v1.ExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this CBHInstances.

        :param extend_param: The extend_param of this CBHInstances.
        :type extend_param: :class:`huaweicloudsdkcbh.v1.ExtendParam`
        """
        self._extend_param = extend_param

    @property
    def metadata(self):
        """Gets the metadata of this CBHInstances.

        创建云服务云数据

        :return: The metadata of this CBHInstances.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CBHInstances.

        创建云服务云数据

        :param metadata: The metadata of this CBHInstances.
        :type metadata: str
        """
        self._metadata = metadata

    @property
    def comment(self):
        """Gets the comment of this CBHInstances.

        描述

        :return: The comment of this CBHInstances.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CBHInstances.

        描述

        :param comment: The comment of this CBHInstances.
        :type comment: str
        """
        self._comment = comment

    @property
    def region(self):
        """Gets the region of this CBHInstances.

        云服务所在区域ID

        :return: The region of this CBHInstances.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CBHInstances.

        云服务所在区域ID

        :param region: The region of this CBHInstances.
        :type region: str
        """
        self._region = region

    @property
    def region_id(self):
        """Gets the region_id of this CBHInstances.

        region标识

        :return: The region_id of this CBHInstances.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CBHInstances.

        region标识

        :param region_id: The region_id of this CBHInstances.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this CBHInstances.

        资源规格

        :return: The resource_spec_code of this CBHInstances.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this CBHInstances.

        资源规格

        :param resource_spec_code: The resource_spec_code of this CBHInstances.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def hx_password(self):
        """Gets the hx_password of this CBHInstances.

        前端登录密码

        :return: The hx_password of this CBHInstances.
        :rtype: str
        """
        return self._hx_password

    @hx_password.setter
    def hx_password(self, hx_password):
        """Sets the hx_password of this CBHInstances.

        前端登录密码

        :param hx_password: The hx_password of this CBHInstances.
        :type hx_password: str
        """
        self._hx_password = hx_password

    @property
    def bastion_type(self):
        """Gets the bastion_type of this CBHInstances.

        堡垒机机机型

        :return: The bastion_type of this CBHInstances.
        :rtype: str
        """
        return self._bastion_type

    @bastion_type.setter
    def bastion_type(self, bastion_type):
        """Sets the bastion_type of this CBHInstances.

        堡垒机机机型

        :param bastion_type: The bastion_type of this CBHInstances.
        :type bastion_type: str
        """
        self._bastion_type = bastion_type

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this CBHInstances.

        分区信息

        :return: The ipv6_enable of this CBHInstances.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this CBHInstances.

        分区信息

        :param ipv6_enable: The ipv6_enable of this CBHInstances.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def end_time(self):
        """Gets the end_time of this CBHInstances.

        订购截止日期

        :return: The end_time of this CBHInstances.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CBHInstances.

        订购截止日期

        :param end_time: The end_time of this CBHInstances.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, CBHInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
