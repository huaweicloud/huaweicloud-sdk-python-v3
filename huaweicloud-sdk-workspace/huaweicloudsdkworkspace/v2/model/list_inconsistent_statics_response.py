# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInconsistentStaticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'int',
        'image_id': 'int',
        'disk_num': 'int',
        'disk_size': 'int'
    }

    attribute_map = {
        'product_id': 'product_id',
        'image_id': 'image_id',
        'disk_num': 'disk_num',
        'disk_size': 'disk_size'
    }

    def __init__(self, product_id=None, image_id=None, disk_num=None, disk_size=None):
        r"""ListInconsistentStaticsResponse

        The model defined in huaweicloud sdk

        :param product_id: 统计productID与桌面池套餐ID不一致的桌面数量
        :type product_id: int
        :param image_id: 统计imageID与桌面池镜像ID不一致的桌面数量
        :type image_id: int
        :param disk_num: 统计数据盘数量与桌面池配置不一致的桌面数量
        :type disk_num: int
        :param disk_size: 统计磁盘累加容量与桌面池配置不一致的桌面数量
        :type disk_size: int
        """
        
        super().__init__()

        self._product_id = None
        self._image_id = None
        self._disk_num = None
        self._disk_size = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if image_id is not None:
            self.image_id = image_id
        if disk_num is not None:
            self.disk_num = disk_num
        if disk_size is not None:
            self.disk_size = disk_size

    @property
    def product_id(self):
        r"""Gets the product_id of this ListInconsistentStaticsResponse.

        统计productID与桌面池套餐ID不一致的桌面数量

        :return: The product_id of this ListInconsistentStaticsResponse.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ListInconsistentStaticsResponse.

        统计productID与桌面池套餐ID不一致的桌面数量

        :param product_id: The product_id of this ListInconsistentStaticsResponse.
        :type product_id: int
        """
        self._product_id = product_id

    @property
    def image_id(self):
        r"""Gets the image_id of this ListInconsistentStaticsResponse.

        统计imageID与桌面池镜像ID不一致的桌面数量

        :return: The image_id of this ListInconsistentStaticsResponse.
        :rtype: int
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListInconsistentStaticsResponse.

        统计imageID与桌面池镜像ID不一致的桌面数量

        :param image_id: The image_id of this ListInconsistentStaticsResponse.
        :type image_id: int
        """
        self._image_id = image_id

    @property
    def disk_num(self):
        r"""Gets the disk_num of this ListInconsistentStaticsResponse.

        统计数据盘数量与桌面池配置不一致的桌面数量

        :return: The disk_num of this ListInconsistentStaticsResponse.
        :rtype: int
        """
        return self._disk_num

    @disk_num.setter
    def disk_num(self, disk_num):
        r"""Sets the disk_num of this ListInconsistentStaticsResponse.

        统计数据盘数量与桌面池配置不一致的桌面数量

        :param disk_num: The disk_num of this ListInconsistentStaticsResponse.
        :type disk_num: int
        """
        self._disk_num = disk_num

    @property
    def disk_size(self):
        r"""Gets the disk_size of this ListInconsistentStaticsResponse.

        统计磁盘累加容量与桌面池配置不一致的桌面数量

        :return: The disk_size of this ListInconsistentStaticsResponse.
        :rtype: int
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        r"""Sets the disk_size of this ListInconsistentStaticsResponse.

        统计磁盘累加容量与桌面池配置不一致的桌面数量

        :param disk_size: The disk_size of this ListInconsistentStaticsResponse.
        :type disk_size: int
        """
        self._disk_size = disk_size

    def to_dict(self):
        import warnings
        warnings.warn("ListInconsistentStaticsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListInconsistentStaticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
