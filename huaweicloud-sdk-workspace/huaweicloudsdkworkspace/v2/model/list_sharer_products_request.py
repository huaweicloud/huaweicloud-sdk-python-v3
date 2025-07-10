# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSharerProductsRequest:

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
        'share_space_size': 'str',
        'charge_mode': 'str',
        'is_gpu': 'int',
        'package_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'product_id': 'product_id',
        'share_space_size': 'share_space_size',
        'charge_mode': 'charge_mode',
        'is_gpu': 'is_gpu',
        'package_type': 'package_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, product_id=None, share_space_size=None, charge_mode=None, is_gpu=None, package_type=None, limit=None, offset=None):
        r"""ListSharerProductsRequest

        The model defined in huaweicloud sdk

        :param product_id: 产品ID。
        :type product_id: str
        :param share_space_size: 协同方数。该套餐支持的最大协同人数。
        :type share_space_size: str
        :param charge_mode: 周期套餐标识。0表示包周期，1表示按需, 6表示一次性计费。
        :type charge_mode: str
        :param is_gpu: 是否是GPU套餐。1表示GPU套餐，0表示非GPU套餐，默认null查询所有类型。
        :type is_gpu: int
        :param package_type: 套餐系列。user_sharer表示用户协同套餐，desktop_sharer表示桌面协同套餐。
        :type package_type: str
        :param limit: 每页数量，范围0-100，默认100。
        :type limit: int
        :param offset: 偏移量，默认0。
        :type offset: int
        """
        
        

        self._product_id = None
        self._share_space_size = None
        self._charge_mode = None
        self._is_gpu = None
        self._package_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if share_space_size is not None:
            self.share_space_size = share_space_size
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if is_gpu is not None:
            self.is_gpu = is_gpu
        if package_type is not None:
            self.package_type = package_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def product_id(self):
        r"""Gets the product_id of this ListSharerProductsRequest.

        产品ID。

        :return: The product_id of this ListSharerProductsRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ListSharerProductsRequest.

        产品ID。

        :param product_id: The product_id of this ListSharerProductsRequest.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def share_space_size(self):
        r"""Gets the share_space_size of this ListSharerProductsRequest.

        协同方数。该套餐支持的最大协同人数。

        :return: The share_space_size of this ListSharerProductsRequest.
        :rtype: str
        """
        return self._share_space_size

    @share_space_size.setter
    def share_space_size(self, share_space_size):
        r"""Sets the share_space_size of this ListSharerProductsRequest.

        协同方数。该套餐支持的最大协同人数。

        :param share_space_size: The share_space_size of this ListSharerProductsRequest.
        :type share_space_size: str
        """
        self._share_space_size = share_space_size

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this ListSharerProductsRequest.

        周期套餐标识。0表示包周期，1表示按需, 6表示一次性计费。

        :return: The charge_mode of this ListSharerProductsRequest.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this ListSharerProductsRequest.

        周期套餐标识。0表示包周期，1表示按需, 6表示一次性计费。

        :param charge_mode: The charge_mode of this ListSharerProductsRequest.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def is_gpu(self):
        r"""Gets the is_gpu of this ListSharerProductsRequest.

        是否是GPU套餐。1表示GPU套餐，0表示非GPU套餐，默认null查询所有类型。

        :return: The is_gpu of this ListSharerProductsRequest.
        :rtype: int
        """
        return self._is_gpu

    @is_gpu.setter
    def is_gpu(self, is_gpu):
        r"""Sets the is_gpu of this ListSharerProductsRequest.

        是否是GPU套餐。1表示GPU套餐，0表示非GPU套餐，默认null查询所有类型。

        :param is_gpu: The is_gpu of this ListSharerProductsRequest.
        :type is_gpu: int
        """
        self._is_gpu = is_gpu

    @property
    def package_type(self):
        r"""Gets the package_type of this ListSharerProductsRequest.

        套餐系列。user_sharer表示用户协同套餐，desktop_sharer表示桌面协同套餐。

        :return: The package_type of this ListSharerProductsRequest.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        r"""Sets the package_type of this ListSharerProductsRequest.

        套餐系列。user_sharer表示用户协同套餐，desktop_sharer表示桌面协同套餐。

        :param package_type: The package_type of this ListSharerProductsRequest.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def limit(self):
        r"""Gets the limit of this ListSharerProductsRequest.

        每页数量，范围0-100，默认100。

        :return: The limit of this ListSharerProductsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSharerProductsRequest.

        每页数量，范围0-100，默认100。

        :param limit: The limit of this ListSharerProductsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSharerProductsRequest.

        偏移量，默认0。

        :return: The offset of this ListSharerProductsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSharerProductsRequest.

        偏移量，默认0。

        :param offset: The offset of this ListSharerProductsRequest.
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
        if not isinstance(other, ListSharerProductsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
