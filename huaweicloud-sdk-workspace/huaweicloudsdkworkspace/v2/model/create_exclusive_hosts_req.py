# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExclusiveHostsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'name': 'str',
        'apply_desktop_quantity': 'int',
        'quantity': 'int',
        'product_id': 'str',
        'image_volumes': 'list[Volume]',
        'enterprise_project_id': 'str',
        'memory_volumes': 'list[Volume]',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'resize_exclusive_lites': 'ResizeExclusiveLitesReq'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'name': 'name',
        'apply_desktop_quantity': 'apply_desktop_quantity',
        'quantity': 'quantity',
        'product_id': 'product_id',
        'image_volumes': 'image_volumes',
        'enterprise_project_id': 'enterprise_project_id',
        'memory_volumes': 'memory_volumes',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'resize_exclusive_lites': 'resize_exclusive_lites'
    }

    def __init__(self, availability_zone=None, name=None, apply_desktop_quantity=None, quantity=None, product_id=None, image_volumes=None, enterprise_project_id=None, memory_volumes=None, vpc_id=None, subnet_id=None, resize_exclusive_lites=None):
        r"""CreateExclusiveHostsReq

        The model defined in huaweicloud sdk

        :param availability_zone: 可用分区。
        :type availability_zone: str
        :param name: 名称。
        :type name: str
        :param apply_desktop_quantity: 追加桌面数量。
        :type apply_desktop_quantity: int
        :param quantity: 购买数量。
        :type quantity: int
        :param product_id: 产品套餐ID。
        :type product_id: str
        :param image_volumes: 镜像盘列表。
        :type image_volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        :param enterprise_project_id: 企业项目ID，默认\&quot;0。\&quot;
        :type enterprise_project_id: str
        :param memory_volumes: 存储盘列表。
        :type memory_volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        :param vpc_id: vpc id。
        :type vpc_id: str
        :param subnet_id: 子网id。
        :type subnet_id: str
        :param resize_exclusive_lites: 
        :type resize_exclusive_lites: :class:`huaweicloudsdkworkspace.v2.ResizeExclusiveLitesReq`
        """
        
        

        self._availability_zone = None
        self._name = None
        self._apply_desktop_quantity = None
        self._quantity = None
        self._product_id = None
        self._image_volumes = None
        self._enterprise_project_id = None
        self._memory_volumes = None
        self._vpc_id = None
        self._subnet_id = None
        self._resize_exclusive_lites = None
        self.discriminator = None

        self.availability_zone = availability_zone
        if name is not None:
            self.name = name
        if apply_desktop_quantity is not None:
            self.apply_desktop_quantity = apply_desktop_quantity
        self.quantity = quantity
        self.product_id = product_id
        self.image_volumes = image_volumes
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.memory_volumes = memory_volumes
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if resize_exclusive_lites is not None:
            self.resize_exclusive_lites = resize_exclusive_lites

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateExclusiveHostsReq.

        可用分区。

        :return: The availability_zone of this CreateExclusiveHostsReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateExclusiveHostsReq.

        可用分区。

        :param availability_zone: The availability_zone of this CreateExclusiveHostsReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def name(self):
        r"""Gets the name of this CreateExclusiveHostsReq.

        名称。

        :return: The name of this CreateExclusiveHostsReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateExclusiveHostsReq.

        名称。

        :param name: The name of this CreateExclusiveHostsReq.
        :type name: str
        """
        self._name = name

    @property
    def apply_desktop_quantity(self):
        r"""Gets the apply_desktop_quantity of this CreateExclusiveHostsReq.

        追加桌面数量。

        :return: The apply_desktop_quantity of this CreateExclusiveHostsReq.
        :rtype: int
        """
        return self._apply_desktop_quantity

    @apply_desktop_quantity.setter
    def apply_desktop_quantity(self, apply_desktop_quantity):
        r"""Sets the apply_desktop_quantity of this CreateExclusiveHostsReq.

        追加桌面数量。

        :param apply_desktop_quantity: The apply_desktop_quantity of this CreateExclusiveHostsReq.
        :type apply_desktop_quantity: int
        """
        self._apply_desktop_quantity = apply_desktop_quantity

    @property
    def quantity(self):
        r"""Gets the quantity of this CreateExclusiveHostsReq.

        购买数量。

        :return: The quantity of this CreateExclusiveHostsReq.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        r"""Sets the quantity of this CreateExclusiveHostsReq.

        购买数量。

        :param quantity: The quantity of this CreateExclusiveHostsReq.
        :type quantity: int
        """
        self._quantity = quantity

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateExclusiveHostsReq.

        产品套餐ID。

        :return: The product_id of this CreateExclusiveHostsReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateExclusiveHostsReq.

        产品套餐ID。

        :param product_id: The product_id of this CreateExclusiveHostsReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def image_volumes(self):
        r"""Gets the image_volumes of this CreateExclusiveHostsReq.

        镜像盘列表。

        :return: The image_volumes of this CreateExclusiveHostsReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        return self._image_volumes

    @image_volumes.setter
    def image_volumes(self, image_volumes):
        r"""Sets the image_volumes of this CreateExclusiveHostsReq.

        镜像盘列表。

        :param image_volumes: The image_volumes of this CreateExclusiveHostsReq.
        :type image_volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        self._image_volumes = image_volumes

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateExclusiveHostsReq.

        企业项目ID，默认\"0。\"

        :return: The enterprise_project_id of this CreateExclusiveHostsReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateExclusiveHostsReq.

        企业项目ID，默认\"0。\"

        :param enterprise_project_id: The enterprise_project_id of this CreateExclusiveHostsReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def memory_volumes(self):
        r"""Gets the memory_volumes of this CreateExclusiveHostsReq.

        存储盘列表。

        :return: The memory_volumes of this CreateExclusiveHostsReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        return self._memory_volumes

    @memory_volumes.setter
    def memory_volumes(self, memory_volumes):
        r"""Sets the memory_volumes of this CreateExclusiveHostsReq.

        存储盘列表。

        :param memory_volumes: The memory_volumes of this CreateExclusiveHostsReq.
        :type memory_volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        self._memory_volumes = memory_volumes

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateExclusiveHostsReq.

        vpc id。

        :return: The vpc_id of this CreateExclusiveHostsReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateExclusiveHostsReq.

        vpc id。

        :param vpc_id: The vpc_id of this CreateExclusiveHostsReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateExclusiveHostsReq.

        子网id。

        :return: The subnet_id of this CreateExclusiveHostsReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateExclusiveHostsReq.

        子网id。

        :param subnet_id: The subnet_id of this CreateExclusiveHostsReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def resize_exclusive_lites(self):
        r"""Gets the resize_exclusive_lites of this CreateExclusiveHostsReq.

        :return: The resize_exclusive_lites of this CreateExclusiveHostsReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResizeExclusiveLitesReq`
        """
        return self._resize_exclusive_lites

    @resize_exclusive_lites.setter
    def resize_exclusive_lites(self, resize_exclusive_lites):
        r"""Sets the resize_exclusive_lites of this CreateExclusiveHostsReq.

        :param resize_exclusive_lites: The resize_exclusive_lites of this CreateExclusiveHostsReq.
        :type resize_exclusive_lites: :class:`huaweicloudsdkworkspace.v2.ResizeExclusiveLitesReq`
        """
        self._resize_exclusive_lites = resize_exclusive_lites

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
        if not isinstance(other, CreateExclusiveHostsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
