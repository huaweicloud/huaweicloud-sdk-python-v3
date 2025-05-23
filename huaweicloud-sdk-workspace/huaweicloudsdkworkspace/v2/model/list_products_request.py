# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'flavor_id': 'str',
        'availability_zone': 'str',
        'os_type': 'str',
        'charge_mode': 'str',
        'architecture': 'str',
        'deh_product_id': 'str',
        'is_deh': 'bool',
        'package_type': 'str',
        'products_range': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'product_id': 'product_id',
        'flavor_id': 'flavor_id',
        'availability_zone': 'availability_zone',
        'os_type': 'os_type',
        'charge_mode': 'charge_mode',
        'architecture': 'architecture',
        'deh_product_id': 'deh_product_id',
        'is_deh': 'is_deh',
        'package_type': 'package_type',
        'products_range': 'products_range',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, product_id=None, flavor_id=None, availability_zone=None, os_type=None, charge_mode=None, architecture=None, deh_product_id=None, is_deh=None, package_type=None, products_range=None, limit=None, offset=None):
        r"""ListProductsRequest

        The model defined in huaweicloud sdk

        :param product_id: 产品ID。
        :type product_id: str
        :param flavor_id: 产品flavor_id。
        :type flavor_id: str
        :param availability_zone: 可用分区。
        :type availability_zone: str
        :param os_type: 产品套餐的操作系统类型，当前支持：Windows、Linux。
        :type os_type: str
        :param charge_mode: 周期套餐标识。0表示包周期，1表示按需。
        :type charge_mode: str
        :param architecture: 架构类型，当前支持：arm、x86。
        :type architecture: str
        :param deh_product_id: wdh套餐id。
        :type deh_product_id: str
        :param is_deh: 是否为wdh产品。
        :type is_deh: bool
        :param package_type: 套餐系列。
        :type package_type: str
        :param products_range: 查询套餐的范围(all：查询所有套餐，包括培训版；若为null则不包含培训版套餐）
        :type products_range: str
        :param limit: 每页数量，范围0-100，默认100。
        :type limit: int
        :param offset: 偏移量，默认0。
        :type offset: int
        """
        
        

        self._product_id = None
        self._flavor_id = None
        self._availability_zone = None
        self._os_type = None
        self._charge_mode = None
        self._architecture = None
        self._deh_product_id = None
        self._is_deh = None
        self._package_type = None
        self._products_range = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if os_type is not None:
            self.os_type = os_type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if architecture is not None:
            self.architecture = architecture
        if deh_product_id is not None:
            self.deh_product_id = deh_product_id
        if is_deh is not None:
            self.is_deh = is_deh
        if package_type is not None:
            self.package_type = package_type
        if products_range is not None:
            self.products_range = products_range
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def product_id(self):
        r"""Gets the product_id of this ListProductsRequest.

        产品ID。

        :return: The product_id of this ListProductsRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ListProductsRequest.

        产品ID。

        :param product_id: The product_id of this ListProductsRequest.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ListProductsRequest.

        产品flavor_id。

        :return: The flavor_id of this ListProductsRequest.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ListProductsRequest.

        产品flavor_id。

        :param flavor_id: The flavor_id of this ListProductsRequest.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListProductsRequest.

        可用分区。

        :return: The availability_zone of this ListProductsRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListProductsRequest.

        可用分区。

        :param availability_zone: The availability_zone of this ListProductsRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def os_type(self):
        r"""Gets the os_type of this ListProductsRequest.

        产品套餐的操作系统类型，当前支持：Windows、Linux。

        :return: The os_type of this ListProductsRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListProductsRequest.

        产品套餐的操作系统类型，当前支持：Windows、Linux。

        :param os_type: The os_type of this ListProductsRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this ListProductsRequest.

        周期套餐标识。0表示包周期，1表示按需。

        :return: The charge_mode of this ListProductsRequest.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this ListProductsRequest.

        周期套餐标识。0表示包周期，1表示按需。

        :param charge_mode: The charge_mode of this ListProductsRequest.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def architecture(self):
        r"""Gets the architecture of this ListProductsRequest.

        架构类型，当前支持：arm、x86。

        :return: The architecture of this ListProductsRequest.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        r"""Sets the architecture of this ListProductsRequest.

        架构类型，当前支持：arm、x86。

        :param architecture: The architecture of this ListProductsRequest.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def deh_product_id(self):
        r"""Gets the deh_product_id of this ListProductsRequest.

        wdh套餐id。

        :return: The deh_product_id of this ListProductsRequest.
        :rtype: str
        """
        return self._deh_product_id

    @deh_product_id.setter
    def deh_product_id(self, deh_product_id):
        r"""Sets the deh_product_id of this ListProductsRequest.

        wdh套餐id。

        :param deh_product_id: The deh_product_id of this ListProductsRequest.
        :type deh_product_id: str
        """
        self._deh_product_id = deh_product_id

    @property
    def is_deh(self):
        r"""Gets the is_deh of this ListProductsRequest.

        是否为wdh产品。

        :return: The is_deh of this ListProductsRequest.
        :rtype: bool
        """
        return self._is_deh

    @is_deh.setter
    def is_deh(self, is_deh):
        r"""Sets the is_deh of this ListProductsRequest.

        是否为wdh产品。

        :param is_deh: The is_deh of this ListProductsRequest.
        :type is_deh: bool
        """
        self._is_deh = is_deh

    @property
    def package_type(self):
        r"""Gets the package_type of this ListProductsRequest.

        套餐系列。

        :return: The package_type of this ListProductsRequest.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        r"""Sets the package_type of this ListProductsRequest.

        套餐系列。

        :param package_type: The package_type of this ListProductsRequest.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def products_range(self):
        r"""Gets the products_range of this ListProductsRequest.

        查询套餐的范围(all：查询所有套餐，包括培训版；若为null则不包含培训版套餐）

        :return: The products_range of this ListProductsRequest.
        :rtype: str
        """
        return self._products_range

    @products_range.setter
    def products_range(self, products_range):
        r"""Sets the products_range of this ListProductsRequest.

        查询套餐的范围(all：查询所有套餐，包括培训版；若为null则不包含培训版套餐）

        :param products_range: The products_range of this ListProductsRequest.
        :type products_range: str
        """
        self._products_range = products_range

    @property
    def limit(self):
        r"""Gets the limit of this ListProductsRequest.

        每页数量，范围0-100，默认100。

        :return: The limit of this ListProductsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProductsRequest.

        每页数量，范围0-100，默认100。

        :param limit: The limit of this ListProductsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListProductsRequest.

        偏移量，默认0。

        :return: The offset of this ListProductsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProductsRequest.

        偏移量，默认0。

        :param offset: The offset of this ListProductsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListProductsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
