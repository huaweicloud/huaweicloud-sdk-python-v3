# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateResponseBody:

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
        'is_template': 'str',
        'region': 'str',
        'projectid': 'str',
        'target_server_name': 'str',
        'availability_zone': 'str',
        'volumetype': 'str',
        'flavor': 'str',
        'vpc': 'VpcObject',
        'nics': 'list[Nics]',
        'security_groups': 'list[SgObject]',
        'publicip': 'PublicIp',
        'disk': 'list[TemplateDisk]',
        'data_volume_type': 'str',
        'target_password': 'str',
        'image_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_template': 'is_template',
        'region': 'region',
        'projectid': 'projectid',
        'target_server_name': 'target_server_name',
        'availability_zone': 'availability_zone',
        'volumetype': 'volumetype',
        'flavor': 'flavor',
        'vpc': 'vpc',
        'nics': 'nics',
        'security_groups': 'security_groups',
        'publicip': 'publicip',
        'disk': 'disk',
        'data_volume_type': 'data_volume_type',
        'target_password': 'target_password',
        'image_id': 'image_id'
    }

    def __init__(self, id=None, name=None, is_template=None, region=None, projectid=None, target_server_name=None, availability_zone=None, volumetype=None, flavor=None, vpc=None, nics=None, security_groups=None, publicip=None, disk=None, data_volume_type=None, target_password=None, image_id=None):
        """TemplateResponseBody

        The model defined in huaweicloud sdk

        :param id: 模板ID
        :type id: str
        :param name: 模板名称
        :type name: str
        :param is_template: 是否是通用模板，如果模板关联一个任务，则不算通用模板
        :type is_template: str
        :param region: Region信息
        :type region: str
        :param projectid: 项目ID
        :type projectid: str
        :param target_server_name: 目标端服务器名称
        :type target_server_name: str
        :param availability_zone: 可用区
        :type availability_zone: str
        :param volumetype: 数据盘磁盘类型 SAS:串行连接SCSI SSD:固态硬盘 SATA:串口硬盘 
        :type volumetype: str
        :param flavor: 虚拟机规格
        :type flavor: str
        :param vpc: 
        :type vpc: :class:`huaweicloudsdksms.v3.VpcObject`
        :param nics: 网卡信息，支持多个网卡，如果是自动创建，只填一个，ID使用“autoCreate”
        :type nics: list[:class:`huaweicloudsdksms.v3.Nics`]
        :param security_groups: 安全组，支持多个安全组，如果是自动创建，只填一个，ID使用“autoCreate”
        :type security_groups: list[:class:`huaweicloudsdksms.v3.SgObject`]
        :param publicip: 
        :type publicip: :class:`huaweicloudsdksms.v3.PublicIp`
        :param disk: 磁盘信息
        :type disk: list[:class:`huaweicloudsdksms.v3.TemplateDisk`]
        :param data_volume_type: 数据盘磁盘类型 SAS:串行连接SCSI SSD:固态硬盘 SATA:串口硬盘 
        :type data_volume_type: str
        :param target_password: 目的端密码
        :type target_password: str
        :param image_id: 用户选择镜像版本Id值
        :type image_id: str
        """
        
        

        self._id = None
        self._name = None
        self._is_template = None
        self._region = None
        self._projectid = None
        self._target_server_name = None
        self._availability_zone = None
        self._volumetype = None
        self._flavor = None
        self._vpc = None
        self._nics = None
        self._security_groups = None
        self._publicip = None
        self._disk = None
        self._data_volume_type = None
        self._target_password = None
        self._image_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if is_template is not None:
            self.is_template = is_template
        self.region = region
        self.projectid = projectid
        self.target_server_name = target_server_name
        self.availability_zone = availability_zone
        self.volumetype = volumetype
        self.flavor = flavor
        self.vpc = vpc
        self.nics = nics
        self.security_groups = security_groups
        self.publicip = publicip
        self.disk = disk
        self.data_volume_type = data_volume_type
        self.target_password = target_password
        if image_id is not None:
            self.image_id = image_id

    @property
    def id(self):
        """Gets the id of this TemplateResponseBody.

        模板ID

        :return: The id of this TemplateResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateResponseBody.

        模板ID

        :param id: The id of this TemplateResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TemplateResponseBody.

        模板名称

        :return: The name of this TemplateResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateResponseBody.

        模板名称

        :param name: The name of this TemplateResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def is_template(self):
        """Gets the is_template of this TemplateResponseBody.

        是否是通用模板，如果模板关联一个任务，则不算通用模板

        :return: The is_template of this TemplateResponseBody.
        :rtype: str
        """
        return self._is_template

    @is_template.setter
    def is_template(self, is_template):
        """Sets the is_template of this TemplateResponseBody.

        是否是通用模板，如果模板关联一个任务，则不算通用模板

        :param is_template: The is_template of this TemplateResponseBody.
        :type is_template: str
        """
        self._is_template = is_template

    @property
    def region(self):
        """Gets the region of this TemplateResponseBody.

        Region信息

        :return: The region of this TemplateResponseBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TemplateResponseBody.

        Region信息

        :param region: The region of this TemplateResponseBody.
        :type region: str
        """
        self._region = region

    @property
    def projectid(self):
        """Gets the projectid of this TemplateResponseBody.

        项目ID

        :return: The projectid of this TemplateResponseBody.
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this TemplateResponseBody.

        项目ID

        :param projectid: The projectid of this TemplateResponseBody.
        :type projectid: str
        """
        self._projectid = projectid

    @property
    def target_server_name(self):
        """Gets the target_server_name of this TemplateResponseBody.

        目标端服务器名称

        :return: The target_server_name of this TemplateResponseBody.
        :rtype: str
        """
        return self._target_server_name

    @target_server_name.setter
    def target_server_name(self, target_server_name):
        """Sets the target_server_name of this TemplateResponseBody.

        目标端服务器名称

        :param target_server_name: The target_server_name of this TemplateResponseBody.
        :type target_server_name: str
        """
        self._target_server_name = target_server_name

    @property
    def availability_zone(self):
        """Gets the availability_zone of this TemplateResponseBody.

        可用区

        :return: The availability_zone of this TemplateResponseBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this TemplateResponseBody.

        可用区

        :param availability_zone: The availability_zone of this TemplateResponseBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def volumetype(self):
        """Gets the volumetype of this TemplateResponseBody.

        数据盘磁盘类型 SAS:串行连接SCSI SSD:固态硬盘 SATA:串口硬盘 

        :return: The volumetype of this TemplateResponseBody.
        :rtype: str
        """
        return self._volumetype

    @volumetype.setter
    def volumetype(self, volumetype):
        """Sets the volumetype of this TemplateResponseBody.

        数据盘磁盘类型 SAS:串行连接SCSI SSD:固态硬盘 SATA:串口硬盘 

        :param volumetype: The volumetype of this TemplateResponseBody.
        :type volumetype: str
        """
        self._volumetype = volumetype

    @property
    def flavor(self):
        """Gets the flavor of this TemplateResponseBody.

        虚拟机规格

        :return: The flavor of this TemplateResponseBody.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this TemplateResponseBody.

        虚拟机规格

        :param flavor: The flavor of this TemplateResponseBody.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def vpc(self):
        """Gets the vpc of this TemplateResponseBody.

        :return: The vpc of this TemplateResponseBody.
        :rtype: :class:`huaweicloudsdksms.v3.VpcObject`
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this TemplateResponseBody.

        :param vpc: The vpc of this TemplateResponseBody.
        :type vpc: :class:`huaweicloudsdksms.v3.VpcObject`
        """
        self._vpc = vpc

    @property
    def nics(self):
        """Gets the nics of this TemplateResponseBody.

        网卡信息，支持多个网卡，如果是自动创建，只填一个，ID使用“autoCreate”

        :return: The nics of this TemplateResponseBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.Nics`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this TemplateResponseBody.

        网卡信息，支持多个网卡，如果是自动创建，只填一个，ID使用“autoCreate”

        :param nics: The nics of this TemplateResponseBody.
        :type nics: list[:class:`huaweicloudsdksms.v3.Nics`]
        """
        self._nics = nics

    @property
    def security_groups(self):
        """Gets the security_groups of this TemplateResponseBody.

        安全组，支持多个安全组，如果是自动创建，只填一个，ID使用“autoCreate”

        :return: The security_groups of this TemplateResponseBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.SgObject`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this TemplateResponseBody.

        安全组，支持多个安全组，如果是自动创建，只填一个，ID使用“autoCreate”

        :param security_groups: The security_groups of this TemplateResponseBody.
        :type security_groups: list[:class:`huaweicloudsdksms.v3.SgObject`]
        """
        self._security_groups = security_groups

    @property
    def publicip(self):
        """Gets the publicip of this TemplateResponseBody.

        :return: The publicip of this TemplateResponseBody.
        :rtype: :class:`huaweicloudsdksms.v3.PublicIp`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this TemplateResponseBody.

        :param publicip: The publicip of this TemplateResponseBody.
        :type publicip: :class:`huaweicloudsdksms.v3.PublicIp`
        """
        self._publicip = publicip

    @property
    def disk(self):
        """Gets the disk of this TemplateResponseBody.

        磁盘信息

        :return: The disk of this TemplateResponseBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.TemplateDisk`]
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this TemplateResponseBody.

        磁盘信息

        :param disk: The disk of this TemplateResponseBody.
        :type disk: list[:class:`huaweicloudsdksms.v3.TemplateDisk`]
        """
        self._disk = disk

    @property
    def data_volume_type(self):
        """Gets the data_volume_type of this TemplateResponseBody.

        数据盘磁盘类型 SAS:串行连接SCSI SSD:固态硬盘 SATA:串口硬盘 

        :return: The data_volume_type of this TemplateResponseBody.
        :rtype: str
        """
        return self._data_volume_type

    @data_volume_type.setter
    def data_volume_type(self, data_volume_type):
        """Sets the data_volume_type of this TemplateResponseBody.

        数据盘磁盘类型 SAS:串行连接SCSI SSD:固态硬盘 SATA:串口硬盘 

        :param data_volume_type: The data_volume_type of this TemplateResponseBody.
        :type data_volume_type: str
        """
        self._data_volume_type = data_volume_type

    @property
    def target_password(self):
        """Gets the target_password of this TemplateResponseBody.

        目的端密码

        :return: The target_password of this TemplateResponseBody.
        :rtype: str
        """
        return self._target_password

    @target_password.setter
    def target_password(self, target_password):
        """Sets the target_password of this TemplateResponseBody.

        目的端密码

        :param target_password: The target_password of this TemplateResponseBody.
        :type target_password: str
        """
        self._target_password = target_password

    @property
    def image_id(self):
        """Gets the image_id of this TemplateResponseBody.

        用户选择镜像版本Id值

        :return: The image_id of this TemplateResponseBody.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this TemplateResponseBody.

        用户选择镜像版本Id值

        :param image_id: The image_id of this TemplateResponseBody.
        :type image_id: str
        """
        self._image_id = image_id

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
        if not isinstance(other, TemplateResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
