# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateChangeOrderReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'period_type': 'int',
        'period_num': 'int',
        'resize_product_id': 'str',
        'expand_volume_id': 'str',
        'expand_new_size': 'int',
        'new_quantity': 'int',
        'exclusive_lites_product_id': 'str',
        'enterprise_project_id': 'str',
        'extend_param': 'OrderExtendParam'
    }

    attribute_map = {
        'type': 'type',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'resize_product_id': 'resize_product_id',
        'expand_volume_id': 'expand_volume_id',
        'expand_new_size': 'expand_new_size',
        'new_quantity': 'new_quantity',
        'exclusive_lites_product_id': 'exclusive_lites_product_id',
        'enterprise_project_id': 'enterprise_project_id',
        'extend_param': 'extend_param'
    }

    def __init__(self, type=None, period_type=None, period_num=None, resize_product_id=None, expand_volume_id=None, expand_new_size=None, new_quantity=None, exclusive_lites_product_id=None, enterprise_project_id=None, extend_param=None):
        r"""CreateChangeOrderReq

        The model defined in huaweicloud sdk

        :param type: 类型 resizeDesktops(变更规格)、expandVolumes(扩容磁盘)。
        :type type: str
        :param period_type: 周期类型，2：包月；3：包年。
        :type period_type: int
        :param period_num: 周期数。
        :type period_num: int
        :param resize_product_id: 变更后规格产品ID，当是resizeDesktops，必传。
        :type resize_product_id: str
        :param expand_volume_id: 扩容的云硬盘的ID，当是expandVolumes，必传。
        :type expand_volume_id: str
        :param expand_new_size: 扩容后云硬盘的总大小，当是expandVolumes，必传。范围10-32760，大小为10的倍数。
        :type expand_new_size: int
        :param new_quantity: 专享主机变更桌面数后桌面路数的总大小，当是jobType是resizeExclusiveLites，必传。
        :type new_quantity: int
        :param exclusive_lites_product_id: 专享主机桌面数的productId，当是resizeExclusiveLites，必传。
        :type exclusive_lites_product_id: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        
        

        self._type = None
        self._period_type = None
        self._period_num = None
        self._resize_product_id = None
        self._expand_volume_id = None
        self._expand_new_size = None
        self._new_quantity = None
        self._exclusive_lites_product_id = None
        self._enterprise_project_id = None
        self._extend_param = None
        self.discriminator = None

        self.type = type
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if resize_product_id is not None:
            self.resize_product_id = resize_product_id
        if expand_volume_id is not None:
            self.expand_volume_id = expand_volume_id
        if expand_new_size is not None:
            self.expand_new_size = expand_new_size
        if new_quantity is not None:
            self.new_quantity = new_quantity
        if exclusive_lites_product_id is not None:
            self.exclusive_lites_product_id = exclusive_lites_product_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def type(self):
        r"""Gets the type of this CreateChangeOrderReq.

        类型 resizeDesktops(变更规格)、expandVolumes(扩容磁盘)。

        :return: The type of this CreateChangeOrderReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateChangeOrderReq.

        类型 resizeDesktops(变更规格)、expandVolumes(扩容磁盘)。

        :param type: The type of this CreateChangeOrderReq.
        :type type: str
        """
        self._type = type

    @property
    def period_type(self):
        r"""Gets the period_type of this CreateChangeOrderReq.

        周期类型，2：包月；3：包年。

        :return: The period_type of this CreateChangeOrderReq.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this CreateChangeOrderReq.

        周期类型，2：包月；3：包年。

        :param period_type: The period_type of this CreateChangeOrderReq.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this CreateChangeOrderReq.

        周期数。

        :return: The period_num of this CreateChangeOrderReq.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this CreateChangeOrderReq.

        周期数。

        :param period_num: The period_num of this CreateChangeOrderReq.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def resize_product_id(self):
        r"""Gets the resize_product_id of this CreateChangeOrderReq.

        变更后规格产品ID，当是resizeDesktops，必传。

        :return: The resize_product_id of this CreateChangeOrderReq.
        :rtype: str
        """
        return self._resize_product_id

    @resize_product_id.setter
    def resize_product_id(self, resize_product_id):
        r"""Sets the resize_product_id of this CreateChangeOrderReq.

        变更后规格产品ID，当是resizeDesktops，必传。

        :param resize_product_id: The resize_product_id of this CreateChangeOrderReq.
        :type resize_product_id: str
        """
        self._resize_product_id = resize_product_id

    @property
    def expand_volume_id(self):
        r"""Gets the expand_volume_id of this CreateChangeOrderReq.

        扩容的云硬盘的ID，当是expandVolumes，必传。

        :return: The expand_volume_id of this CreateChangeOrderReq.
        :rtype: str
        """
        return self._expand_volume_id

    @expand_volume_id.setter
    def expand_volume_id(self, expand_volume_id):
        r"""Sets the expand_volume_id of this CreateChangeOrderReq.

        扩容的云硬盘的ID，当是expandVolumes，必传。

        :param expand_volume_id: The expand_volume_id of this CreateChangeOrderReq.
        :type expand_volume_id: str
        """
        self._expand_volume_id = expand_volume_id

    @property
    def expand_new_size(self):
        r"""Gets the expand_new_size of this CreateChangeOrderReq.

        扩容后云硬盘的总大小，当是expandVolumes，必传。范围10-32760，大小为10的倍数。

        :return: The expand_new_size of this CreateChangeOrderReq.
        :rtype: int
        """
        return self._expand_new_size

    @expand_new_size.setter
    def expand_new_size(self, expand_new_size):
        r"""Sets the expand_new_size of this CreateChangeOrderReq.

        扩容后云硬盘的总大小，当是expandVolumes，必传。范围10-32760，大小为10的倍数。

        :param expand_new_size: The expand_new_size of this CreateChangeOrderReq.
        :type expand_new_size: int
        """
        self._expand_new_size = expand_new_size

    @property
    def new_quantity(self):
        r"""Gets the new_quantity of this CreateChangeOrderReq.

        专享主机变更桌面数后桌面路数的总大小，当是jobType是resizeExclusiveLites，必传。

        :return: The new_quantity of this CreateChangeOrderReq.
        :rtype: int
        """
        return self._new_quantity

    @new_quantity.setter
    def new_quantity(self, new_quantity):
        r"""Sets the new_quantity of this CreateChangeOrderReq.

        专享主机变更桌面数后桌面路数的总大小，当是jobType是resizeExclusiveLites，必传。

        :param new_quantity: The new_quantity of this CreateChangeOrderReq.
        :type new_quantity: int
        """
        self._new_quantity = new_quantity

    @property
    def exclusive_lites_product_id(self):
        r"""Gets the exclusive_lites_product_id of this CreateChangeOrderReq.

        专享主机桌面数的productId，当是resizeExclusiveLites，必传。

        :return: The exclusive_lites_product_id of this CreateChangeOrderReq.
        :rtype: str
        """
        return self._exclusive_lites_product_id

    @exclusive_lites_product_id.setter
    def exclusive_lites_product_id(self, exclusive_lites_product_id):
        r"""Sets the exclusive_lites_product_id of this CreateChangeOrderReq.

        专享主机桌面数的productId，当是resizeExclusiveLites，必传。

        :param exclusive_lites_product_id: The exclusive_lites_product_id of this CreateChangeOrderReq.
        :type exclusive_lites_product_id: str
        """
        self._exclusive_lites_product_id = exclusive_lites_product_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateChangeOrderReq.

        企业项目ID。

        :return: The enterprise_project_id of this CreateChangeOrderReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateChangeOrderReq.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateChangeOrderReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def extend_param(self):
        r"""Gets the extend_param of this CreateChangeOrderReq.

        :return: The extend_param of this CreateChangeOrderReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this CreateChangeOrderReq.

        :param extend_param: The extend_param of this CreateChangeOrderReq.
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, CreateChangeOrderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
