# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDesktopReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_type': 'str',
        'availability_zone': 'str',
        'product_id': 'str',
        'image_type': 'str',
        'image_id': 'str',
        'root_volume': 'Volume',
        'data_volumes': 'list[Volume]',
        'nics': 'list[Nic]',
        'security_groups': 'list[SecurityGroup]',
        'desktops': 'list[Desktop]',
        'desktop_name': 'str',
        'desktop_ips': 'list[str]',
        'size': 'int',
        'email_notification': 'bool',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'apply_shared_vpc_dedicated_param': 'ApplySharedVpcDedicatedParam',
        'eip': 'Eip',
        'desktop_name_policy_id': 'str',
        'hour_package_product_id': 'str',
        'hour_package_offering_id': 'str'
    }

    attribute_map = {
        'desktop_type': 'desktop_type',
        'availability_zone': 'availability_zone',
        'product_id': 'product_id',
        'image_type': 'image_type',
        'image_id': 'image_id',
        'root_volume': 'root_volume',
        'data_volumes': 'data_volumes',
        'nics': 'nics',
        'security_groups': 'security_groups',
        'desktops': 'desktops',
        'desktop_name': 'desktop_name',
        'desktop_ips': 'desktop_ips',
        'size': 'size',
        'email_notification': 'email_notification',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'apply_shared_vpc_dedicated_param': 'apply_shared_vpc_dedicated_param',
        'eip': 'eip',
        'desktop_name_policy_id': 'desktop_name_policy_id',
        'hour_package_product_id': 'hour_package_product_id',
        'hour_package_offering_id': 'hour_package_offering_id'
    }

    def __init__(self, desktop_type=None, availability_zone=None, product_id=None, image_type=None, image_id=None, root_volume=None, data_volumes=None, nics=None, security_groups=None, desktops=None, desktop_name=None, desktop_ips=None, size=None, email_notification=None, enterprise_project_id=None, tags=None, apply_shared_vpc_dedicated_param=None, eip=None, desktop_name_policy_id=None, hour_package_product_id=None, hour_package_offering_id=None):
        r"""CreateDesktopReq

        The model defined in huaweicloud sdk

        :param desktop_type: 云桌面类型。 - DEDICATED：专属桌面，单用户。 - SHARED: 多用户共享桌面。
        :type desktop_type: str
        :param availability_zone: 可用分区。将桌面创建到指定的可用分区。如果不指定则使用系统随机的可用分区。
        :type availability_zone: str
        :param product_id: 套餐ID。
        :type product_id: str
        :param image_type: 镜像类型。默认值为private。  - private：私有镜像。 - gold：公共镜像。
        :type image_type: str
        :param image_id: 镜像ID，用于私有镜像创建桌面场景，配合product_id使用。
        :type image_id: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.Volume`
        :param data_volumes: 数据盘列表。
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        :param nics: 桌面对应的网卡信息，如果不指定则使用默认网卡。
        :type nics: list[:class:`huaweicloudsdkworkspace.v2.Nic`]
        :param security_groups: 桌面使用的安全组，如果不指定则默认使用桌面代理中指定的安全组。
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        :param desktops: 创建桌面使用的参数列表。长度为1-100。  当前不支持一批桌面不同配置，所有桌面的配置和第一台的一致，如果第一台未设置参数，则取外层的同名参数。
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.Desktop`]
        :param desktop_name: 搭配size使用，当size为1时代表桌面名，位数1-15，当size大于1时代表桌面名前缀，位数：1-13。
        :type desktop_name: str
        :param desktop_ips: 桌面指定分配的ip地址列表,最小为0，最大为100。
        :type desktop_ips: list[str]
        :param size: 创建不分配用户的桌面的个数，和desktops不能同时生效，搭配desktop_name使用。
        :type size: int
        :param email_notification: 创建成功后是否发送邮件通知桌面用户，默认为true。
        :type email_notification: bool
        :param enterprise_project_id: 企业项目ID，默认\&quot;0。\&quot;
        :type enterprise_project_id: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        :param apply_shared_vpc_dedicated_param: 
        :type apply_shared_vpc_dedicated_param: :class:`huaweicloudsdkworkspace.v2.ApplySharedVpcDedicatedParam`
        :param eip: 
        :type eip: :class:`huaweicloudsdkworkspace.v2.Eip`
        :param desktop_name_policy_id: 策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。
        :type desktop_name_policy_id: str
        :param hour_package_product_id: 桌面小时包套餐ID。
        :type hour_package_product_id: str
        :param hour_package_offering_id: 桌面小时包offeringID。
        :type hour_package_offering_id: str
        """
        
        

        self._desktop_type = None
        self._availability_zone = None
        self._product_id = None
        self._image_type = None
        self._image_id = None
        self._root_volume = None
        self._data_volumes = None
        self._nics = None
        self._security_groups = None
        self._desktops = None
        self._desktop_name = None
        self._desktop_ips = None
        self._size = None
        self._email_notification = None
        self._enterprise_project_id = None
        self._tags = None
        self._apply_shared_vpc_dedicated_param = None
        self._eip = None
        self._desktop_name_policy_id = None
        self._hour_package_product_id = None
        self._hour_package_offering_id = None
        self.discriminator = None

        self.desktop_type = desktop_type
        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.product_id = product_id
        self.image_type = image_type
        self.image_id = image_id
        self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if nics is not None:
            self.nics = nics
        if security_groups is not None:
            self.security_groups = security_groups
        if desktops is not None:
            self.desktops = desktops
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if desktop_ips is not None:
            self.desktop_ips = desktop_ips
        if size is not None:
            self.size = size
        if email_notification is not None:
            self.email_notification = email_notification
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if apply_shared_vpc_dedicated_param is not None:
            self.apply_shared_vpc_dedicated_param = apply_shared_vpc_dedicated_param
        if eip is not None:
            self.eip = eip
        if desktop_name_policy_id is not None:
            self.desktop_name_policy_id = desktop_name_policy_id
        if hour_package_product_id is not None:
            self.hour_package_product_id = hour_package_product_id
        if hour_package_offering_id is not None:
            self.hour_package_offering_id = hour_package_offering_id

    @property
    def desktop_type(self):
        r"""Gets the desktop_type of this CreateDesktopReq.

        云桌面类型。 - DEDICATED：专属桌面，单用户。 - SHARED: 多用户共享桌面。

        :return: The desktop_type of this CreateDesktopReq.
        :rtype: str
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        r"""Sets the desktop_type of this CreateDesktopReq.

        云桌面类型。 - DEDICATED：专属桌面，单用户。 - SHARED: 多用户共享桌面。

        :param desktop_type: The desktop_type of this CreateDesktopReq.
        :type desktop_type: str
        """
        self._desktop_type = desktop_type

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateDesktopReq.

        可用分区。将桌面创建到指定的可用分区。如果不指定则使用系统随机的可用分区。

        :return: The availability_zone of this CreateDesktopReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateDesktopReq.

        可用分区。将桌面创建到指定的可用分区。如果不指定则使用系统随机的可用分区。

        :param availability_zone: The availability_zone of this CreateDesktopReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateDesktopReq.

        套餐ID。

        :return: The product_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateDesktopReq.

        套餐ID。

        :param product_id: The product_id of this CreateDesktopReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def image_type(self):
        r"""Gets the image_type of this CreateDesktopReq.

        镜像类型。默认值为private。  - private：私有镜像。 - gold：公共镜像。

        :return: The image_type of this CreateDesktopReq.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this CreateDesktopReq.

        镜像类型。默认值为private。  - private：私有镜像。 - gold：公共镜像。

        :param image_type: The image_type of this CreateDesktopReq.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_id(self):
        r"""Gets the image_id of this CreateDesktopReq.

        镜像ID，用于私有镜像创建桌面场景，配合product_id使用。

        :return: The image_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this CreateDesktopReq.

        镜像ID，用于私有镜像创建桌面场景，配合product_id使用。

        :param image_id: The image_id of this CreateDesktopReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def root_volume(self):
        r"""Gets the root_volume of this CreateDesktopReq.

        :return: The root_volume of this CreateDesktopReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Volume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this CreateDesktopReq.

        :param root_volume: The root_volume of this CreateDesktopReq.
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.Volume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this CreateDesktopReq.

        数据盘列表。

        :return: The data_volumes of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this CreateDesktopReq.

        数据盘列表。

        :param data_volumes: The data_volumes of this CreateDesktopReq.
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        self._data_volumes = data_volumes

    @property
    def nics(self):
        r"""Gets the nics of this CreateDesktopReq.

        桌面对应的网卡信息，如果不指定则使用默认网卡。

        :return: The nics of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Nic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        r"""Sets the nics of this CreateDesktopReq.

        桌面对应的网卡信息，如果不指定则使用默认网卡。

        :param nics: The nics of this CreateDesktopReq.
        :type nics: list[:class:`huaweicloudsdkworkspace.v2.Nic`]
        """
        self._nics = nics

    @property
    def security_groups(self):
        r"""Gets the security_groups of this CreateDesktopReq.

        桌面使用的安全组，如果不指定则默认使用桌面代理中指定的安全组。

        :return: The security_groups of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this CreateDesktopReq.

        桌面使用的安全组，如果不指定则默认使用桌面代理中指定的安全组。

        :param security_groups: The security_groups of this CreateDesktopReq.
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def desktops(self):
        r"""Gets the desktops of this CreateDesktopReq.

        创建桌面使用的参数列表。长度为1-100。  当前不支持一批桌面不同配置，所有桌面的配置和第一台的一致，如果第一台未设置参数，则取外层的同名参数。

        :return: The desktops of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Desktop`]
        """
        return self._desktops

    @desktops.setter
    def desktops(self, desktops):
        r"""Sets the desktops of this CreateDesktopReq.

        创建桌面使用的参数列表。长度为1-100。  当前不支持一批桌面不同配置，所有桌面的配置和第一台的一致，如果第一台未设置参数，则取外层的同名参数。

        :param desktops: The desktops of this CreateDesktopReq.
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.Desktop`]
        """
        self._desktops = desktops

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this CreateDesktopReq.

        搭配size使用，当size为1时代表桌面名，位数1-15，当size大于1时代表桌面名前缀，位数：1-13。

        :return: The desktop_name of this CreateDesktopReq.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this CreateDesktopReq.

        搭配size使用，当size为1时代表桌面名，位数1-15，当size大于1时代表桌面名前缀，位数：1-13。

        :param desktop_name: The desktop_name of this CreateDesktopReq.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def desktop_ips(self):
        r"""Gets the desktop_ips of this CreateDesktopReq.

        桌面指定分配的ip地址列表,最小为0，最大为100。

        :return: The desktop_ips of this CreateDesktopReq.
        :rtype: list[str]
        """
        return self._desktop_ips

    @desktop_ips.setter
    def desktop_ips(self, desktop_ips):
        r"""Sets the desktop_ips of this CreateDesktopReq.

        桌面指定分配的ip地址列表,最小为0，最大为100。

        :param desktop_ips: The desktop_ips of this CreateDesktopReq.
        :type desktop_ips: list[str]
        """
        self._desktop_ips = desktop_ips

    @property
    def size(self):
        r"""Gets the size of this CreateDesktopReq.

        创建不分配用户的桌面的个数，和desktops不能同时生效，搭配desktop_name使用。

        :return: The size of this CreateDesktopReq.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this CreateDesktopReq.

        创建不分配用户的桌面的个数，和desktops不能同时生效，搭配desktop_name使用。

        :param size: The size of this CreateDesktopReq.
        :type size: int
        """
        self._size = size

    @property
    def email_notification(self):
        r"""Gets the email_notification of this CreateDesktopReq.

        创建成功后是否发送邮件通知桌面用户，默认为true。

        :return: The email_notification of this CreateDesktopReq.
        :rtype: bool
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        r"""Sets the email_notification of this CreateDesktopReq.

        创建成功后是否发送邮件通知桌面用户，默认为true。

        :param email_notification: The email_notification of this CreateDesktopReq.
        :type email_notification: bool
        """
        self._email_notification = email_notification

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateDesktopReq.

        企业项目ID，默认\"0。\"

        :return: The enterprise_project_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateDesktopReq.

        企业项目ID，默认\"0。\"

        :param enterprise_project_id: The enterprise_project_id of this CreateDesktopReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateDesktopReq.

        标签列表。

        :return: The tags of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateDesktopReq.

        标签列表。

        :param tags: The tags of this CreateDesktopReq.
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        self._tags = tags

    @property
    def apply_shared_vpc_dedicated_param(self):
        r"""Gets the apply_shared_vpc_dedicated_param of this CreateDesktopReq.

        :return: The apply_shared_vpc_dedicated_param of this CreateDesktopReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplySharedVpcDedicatedParam`
        """
        return self._apply_shared_vpc_dedicated_param

    @apply_shared_vpc_dedicated_param.setter
    def apply_shared_vpc_dedicated_param(self, apply_shared_vpc_dedicated_param):
        r"""Sets the apply_shared_vpc_dedicated_param of this CreateDesktopReq.

        :param apply_shared_vpc_dedicated_param: The apply_shared_vpc_dedicated_param of this CreateDesktopReq.
        :type apply_shared_vpc_dedicated_param: :class:`huaweicloudsdkworkspace.v2.ApplySharedVpcDedicatedParam`
        """
        self._apply_shared_vpc_dedicated_param = apply_shared_vpc_dedicated_param

    @property
    def eip(self):
        r"""Gets the eip of this CreateDesktopReq.

        :return: The eip of this CreateDesktopReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Eip`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this CreateDesktopReq.

        :param eip: The eip of this CreateDesktopReq.
        :type eip: :class:`huaweicloudsdkworkspace.v2.Eip`
        """
        self._eip = eip

    @property
    def desktop_name_policy_id(self):
        r"""Gets the desktop_name_policy_id of this CreateDesktopReq.

        策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。

        :return: The desktop_name_policy_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._desktop_name_policy_id

    @desktop_name_policy_id.setter
    def desktop_name_policy_id(self, desktop_name_policy_id):
        r"""Sets the desktop_name_policy_id of this CreateDesktopReq.

        策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。

        :param desktop_name_policy_id: The desktop_name_policy_id of this CreateDesktopReq.
        :type desktop_name_policy_id: str
        """
        self._desktop_name_policy_id = desktop_name_policy_id

    @property
    def hour_package_product_id(self):
        r"""Gets the hour_package_product_id of this CreateDesktopReq.

        桌面小时包套餐ID。

        :return: The hour_package_product_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._hour_package_product_id

    @hour_package_product_id.setter
    def hour_package_product_id(self, hour_package_product_id):
        r"""Sets the hour_package_product_id of this CreateDesktopReq.

        桌面小时包套餐ID。

        :param hour_package_product_id: The hour_package_product_id of this CreateDesktopReq.
        :type hour_package_product_id: str
        """
        self._hour_package_product_id = hour_package_product_id

    @property
    def hour_package_offering_id(self):
        r"""Gets the hour_package_offering_id of this CreateDesktopReq.

        桌面小时包offeringID。

        :return: The hour_package_offering_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._hour_package_offering_id

    @hour_package_offering_id.setter
    def hour_package_offering_id(self, hour_package_offering_id):
        r"""Sets the hour_package_offering_id of this CreateDesktopReq.

        桌面小时包offeringID。

        :param hour_package_offering_id: The hour_package_offering_id of this CreateDesktopReq.
        :type hour_package_offering_id: str
        """
        self._hour_package_offering_id = hour_package_offering_id

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
        if not isinstance(other, CreateDesktopReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
