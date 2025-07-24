# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IRack:

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
        'dc': 'str',
        'region': 'str',
        'location': 'str',
        'size': 'str',
        'unit': 'str',
        'power': 'str',
        'description': 'str',
        'tags': 'list[Tag]',
        'order_status': 'str',
        'is_cloud_based': 'str',
        'operation_status': 'int',
        'freeze_effect': 'int',
        'scene': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'dc': 'dc',
        'region': 'region',
        'location': 'location',
        'size': 'size',
        'unit': 'unit',
        'power': 'power',
        'description': 'description',
        'tags': 'tags',
        'order_status': 'order_status',
        'is_cloud_based': 'is_cloud_based',
        'operation_status': 'operation_status',
        'freeze_effect': 'freeze_effect',
        'scene': 'scene'
    }

    def __init__(self, id=None, name=None, dc=None, region=None, location=None, size=None, unit=None, power=None, description=None, tags=None, order_status=None, is_cloud_based=None, operation_status=None, freeze_effect=None, scene=None):
        r"""IRack

        The model defined in huaweicloud sdk

        :param id: 机柜ID，资源的唯一标识
        :type id: str
        :param name: 机柜名称
        :type name: str
        :param dc: 机房名称
        :type dc: str
        :param region: 局点信息
        :type region: str
        :param location: 机柜位置
        :type location: str
        :param size: 机柜尺寸
        :type size: str
        :param unit: 机柜U位
        :type unit: str
        :param power: 机柜额定功率
        :type power: str
        :param description: 描述
        :type description: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        :param order_status: 订单状态
        :type order_status: str
        :param is_cloud_based: 是否云化纳管柜
        :type is_cloud_based: str
        :param operation_status: 操作状态
        :type operation_status: int
        :param freeze_effect: 冻结效果
        :type freeze_effect: int
        :param scene: 冻结场景
        :type scene: str
        """
        
        

        self._id = None
        self._name = None
        self._dc = None
        self._region = None
        self._location = None
        self._size = None
        self._unit = None
        self._power = None
        self._description = None
        self._tags = None
        self._order_status = None
        self._is_cloud_based = None
        self._operation_status = None
        self._freeze_effect = None
        self._scene = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if dc is not None:
            self.dc = dc
        if region is not None:
            self.region = region
        if location is not None:
            self.location = location
        if size is not None:
            self.size = size
        if unit is not None:
            self.unit = unit
        if power is not None:
            self.power = power
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if order_status is not None:
            self.order_status = order_status
        if is_cloud_based is not None:
            self.is_cloud_based = is_cloud_based
        if operation_status is not None:
            self.operation_status = operation_status
        if freeze_effect is not None:
            self.freeze_effect = freeze_effect
        if scene is not None:
            self.scene = scene

    @property
    def id(self):
        r"""Gets the id of this IRack.

        机柜ID，资源的唯一标识

        :return: The id of this IRack.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IRack.

        机柜ID，资源的唯一标识

        :param id: The id of this IRack.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this IRack.

        机柜名称

        :return: The name of this IRack.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IRack.

        机柜名称

        :param name: The name of this IRack.
        :type name: str
        """
        self._name = name

    @property
    def dc(self):
        r"""Gets the dc of this IRack.

        机房名称

        :return: The dc of this IRack.
        :rtype: str
        """
        return self._dc

    @dc.setter
    def dc(self, dc):
        r"""Sets the dc of this IRack.

        机房名称

        :param dc: The dc of this IRack.
        :type dc: str
        """
        self._dc = dc

    @property
    def region(self):
        r"""Gets the region of this IRack.

        局点信息

        :return: The region of this IRack.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this IRack.

        局点信息

        :param region: The region of this IRack.
        :type region: str
        """
        self._region = region

    @property
    def location(self):
        r"""Gets the location of this IRack.

        机柜位置

        :return: The location of this IRack.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this IRack.

        机柜位置

        :param location: The location of this IRack.
        :type location: str
        """
        self._location = location

    @property
    def size(self):
        r"""Gets the size of this IRack.

        机柜尺寸

        :return: The size of this IRack.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this IRack.

        机柜尺寸

        :param size: The size of this IRack.
        :type size: str
        """
        self._size = size

    @property
    def unit(self):
        r"""Gets the unit of this IRack.

        机柜U位

        :return: The unit of this IRack.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this IRack.

        机柜U位

        :param unit: The unit of this IRack.
        :type unit: str
        """
        self._unit = unit

    @property
    def power(self):
        r"""Gets the power of this IRack.

        机柜额定功率

        :return: The power of this IRack.
        :rtype: str
        """
        return self._power

    @power.setter
    def power(self, power):
        r"""Sets the power of this IRack.

        机柜额定功率

        :param power: The power of this IRack.
        :type power: str
        """
        self._power = power

    @property
    def description(self):
        r"""Gets the description of this IRack.

        描述

        :return: The description of this IRack.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IRack.

        描述

        :param description: The description of this IRack.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this IRack.

        标签

        :return: The tags of this IRack.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this IRack.

        标签

        :param tags: The tags of this IRack.
        :type tags: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        """
        self._tags = tags

    @property
    def order_status(self):
        r"""Gets the order_status of this IRack.

        订单状态

        :return: The order_status of this IRack.
        :rtype: str
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        r"""Sets the order_status of this IRack.

        订单状态

        :param order_status: The order_status of this IRack.
        :type order_status: str
        """
        self._order_status = order_status

    @property
    def is_cloud_based(self):
        r"""Gets the is_cloud_based of this IRack.

        是否云化纳管柜

        :return: The is_cloud_based of this IRack.
        :rtype: str
        """
        return self._is_cloud_based

    @is_cloud_based.setter
    def is_cloud_based(self, is_cloud_based):
        r"""Sets the is_cloud_based of this IRack.

        是否云化纳管柜

        :param is_cloud_based: The is_cloud_based of this IRack.
        :type is_cloud_based: str
        """
        self._is_cloud_based = is_cloud_based

    @property
    def operation_status(self):
        r"""Gets the operation_status of this IRack.

        操作状态

        :return: The operation_status of this IRack.
        :rtype: int
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        r"""Sets the operation_status of this IRack.

        操作状态

        :param operation_status: The operation_status of this IRack.
        :type operation_status: int
        """
        self._operation_status = operation_status

    @property
    def freeze_effect(self):
        r"""Gets the freeze_effect of this IRack.

        冻结效果

        :return: The freeze_effect of this IRack.
        :rtype: int
        """
        return self._freeze_effect

    @freeze_effect.setter
    def freeze_effect(self, freeze_effect):
        r"""Sets the freeze_effect of this IRack.

        冻结效果

        :param freeze_effect: The freeze_effect of this IRack.
        :type freeze_effect: int
        """
        self._freeze_effect = freeze_effect

    @property
    def scene(self):
        r"""Gets the scene of this IRack.

        冻结场景

        :return: The scene of this IRack.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this IRack.

        冻结场景

        :param scene: The scene of this IRack.
        :type scene: str
        """
        self._scene = scene

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
        if not isinstance(other, IRack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
