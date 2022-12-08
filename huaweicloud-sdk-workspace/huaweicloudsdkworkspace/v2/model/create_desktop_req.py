# coding: utf-8

import re
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
        'security_groups': 'list[SecurityGroupInfo]',
        'desktops': 'list[Desktop]',
        'email_notification': 'bool',
        'tags': 'list[Tag]'
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
        'email_notification': 'email_notification',
        'tags': 'tags'
    }

    def __init__(self, desktop_type=None, availability_zone=None, product_id=None, image_type=None, image_id=None, root_volume=None, data_volumes=None, nics=None, security_groups=None, desktops=None, email_notification=None, tags=None):
        """CreateDesktopReq

        The model defined in huaweicloud sdk

        :param desktop_type: 云桌面类型。  - DEDICATED：专属桌面。
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
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        :param desktops: 创建桌面使用的参数列表。长度为1-50。  当前不支持一批桌面不同配置，所有桌面的配置和第一台的一致，如果第一台未设置参数，则取外层的同名参数。
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.Desktop`]
        :param email_notification: 创建成功后是否发送邮件通知桌面用户，默认为true。此参数仅在开通云桌面服务的domain_type为LOCAL_AD时有效，为LITE_AS时无效，因为LITE_AS首次创建桌面时必须发送邮件通知桌面用户修改登录密码。
        :type email_notification: bool
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
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
        self._email_notification = None
        self._tags = None
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
        self.desktops = desktops
        if email_notification is not None:
            self.email_notification = email_notification
        if tags is not None:
            self.tags = tags

    @property
    def desktop_type(self):
        """Gets the desktop_type of this CreateDesktopReq.

        云桌面类型。  - DEDICATED：专属桌面。

        :return: The desktop_type of this CreateDesktopReq.
        :rtype: str
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        """Sets the desktop_type of this CreateDesktopReq.

        云桌面类型。  - DEDICATED：专属桌面。

        :param desktop_type: The desktop_type of this CreateDesktopReq.
        :type desktop_type: str
        """
        self._desktop_type = desktop_type

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateDesktopReq.

        可用分区。将桌面创建到指定的可用分区。如果不指定则使用系统随机的可用分区。

        :return: The availability_zone of this CreateDesktopReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateDesktopReq.

        可用分区。将桌面创建到指定的可用分区。如果不指定则使用系统随机的可用分区。

        :param availability_zone: The availability_zone of this CreateDesktopReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def product_id(self):
        """Gets the product_id of this CreateDesktopReq.

        套餐ID。

        :return: The product_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateDesktopReq.

        套餐ID。

        :param product_id: The product_id of this CreateDesktopReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def image_type(self):
        """Gets the image_type of this CreateDesktopReq.

        镜像类型。默认值为private。  - private：私有镜像。 - gold：公共镜像。

        :return: The image_type of this CreateDesktopReq.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this CreateDesktopReq.

        镜像类型。默认值为private。  - private：私有镜像。 - gold：公共镜像。

        :param image_type: The image_type of this CreateDesktopReq.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_id(self):
        """Gets the image_id of this CreateDesktopReq.

        镜像ID，用于私有镜像创建桌面场景，配合product_id使用。

        :return: The image_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this CreateDesktopReq.

        镜像ID，用于私有镜像创建桌面场景，配合product_id使用。

        :param image_id: The image_id of this CreateDesktopReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def root_volume(self):
        """Gets the root_volume of this CreateDesktopReq.

        :return: The root_volume of this CreateDesktopReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Volume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this CreateDesktopReq.

        :param root_volume: The root_volume of this CreateDesktopReq.
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.Volume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        """Gets the data_volumes of this CreateDesktopReq.

        数据盘列表。

        :return: The data_volumes of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this CreateDesktopReq.

        数据盘列表。

        :param data_volumes: The data_volumes of this CreateDesktopReq.
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        self._data_volumes = data_volumes

    @property
    def nics(self):
        """Gets the nics of this CreateDesktopReq.

        桌面对应的网卡信息，如果不指定则使用默认网卡。

        :return: The nics of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Nic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this CreateDesktopReq.

        桌面对应的网卡信息，如果不指定则使用默认网卡。

        :param nics: The nics of this CreateDesktopReq.
        :type nics: list[:class:`huaweicloudsdkworkspace.v2.Nic`]
        """
        self._nics = nics

    @property
    def security_groups(self):
        """Gets the security_groups of this CreateDesktopReq.

        桌面使用的安全组，如果不指定则默认使用桌面代理中指定的安全组。

        :return: The security_groups of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this CreateDesktopReq.

        桌面使用的安全组，如果不指定则默认使用桌面代理中指定的安全组。

        :param security_groups: The security_groups of this CreateDesktopReq.
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        """
        self._security_groups = security_groups

    @property
    def desktops(self):
        """Gets the desktops of this CreateDesktopReq.

        创建桌面使用的参数列表。长度为1-50。  当前不支持一批桌面不同配置，所有桌面的配置和第一台的一致，如果第一台未设置参数，则取外层的同名参数。

        :return: The desktops of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Desktop`]
        """
        return self._desktops

    @desktops.setter
    def desktops(self, desktops):
        """Sets the desktops of this CreateDesktopReq.

        创建桌面使用的参数列表。长度为1-50。  当前不支持一批桌面不同配置，所有桌面的配置和第一台的一致，如果第一台未设置参数，则取外层的同名参数。

        :param desktops: The desktops of this CreateDesktopReq.
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.Desktop`]
        """
        self._desktops = desktops

    @property
    def email_notification(self):
        """Gets the email_notification of this CreateDesktopReq.

        创建成功后是否发送邮件通知桌面用户，默认为true。此参数仅在开通云桌面服务的domain_type为LOCAL_AD时有效，为LITE_AS时无效，因为LITE_AS首次创建桌面时必须发送邮件通知桌面用户修改登录密码。

        :return: The email_notification of this CreateDesktopReq.
        :rtype: bool
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """Sets the email_notification of this CreateDesktopReq.

        创建成功后是否发送邮件通知桌面用户，默认为true。此参数仅在开通云桌面服务的domain_type为LOCAL_AD时有效，为LITE_AS时无效，因为LITE_AS首次创建桌面时必须发送邮件通知桌面用户修改登录密码。

        :param email_notification: The email_notification of this CreateDesktopReq.
        :type email_notification: bool
        """
        self._email_notification = email_notification

    @property
    def tags(self):
        """Gets the tags of this CreateDesktopReq.

        标签列表。

        :return: The tags of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDesktopReq.

        标签列表。

        :param tags: The tags of this CreateDesktopReq.
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        self._tags = tags

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
