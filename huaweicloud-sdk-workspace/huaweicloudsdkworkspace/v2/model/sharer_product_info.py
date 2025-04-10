# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SharerProductInfo:

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
        'is_gpu': 'bool',
        'descriptions': 'str',
        'charge_mode': 'str',
        'resource_type': 'str',
        'cloud_service_type': 'str',
        'package_type': 'str',
        'name': 'dict(str, str)',
        'share_space_size': 'int'
    }

    attribute_map = {
        'product_id': 'product_id',
        'is_gpu': 'is_gpu',
        'descriptions': 'descriptions',
        'charge_mode': 'charge_mode',
        'resource_type': 'resource_type',
        'cloud_service_type': 'cloud_service_type',
        'package_type': 'package_type',
        'name': 'name',
        'share_space_size': 'share_space_size'
    }

    def __init__(self, product_id=None, is_gpu=None, descriptions=None, charge_mode=None, resource_type=None, cloud_service_type=None, package_type=None, name=None, share_space_size=None):
        r"""SharerProductInfo

        The model defined in huaweicloud sdk

        :param product_id: 产品ID。
        :type product_id: str
        :param is_gpu: 是否是GPU类型的规格。
        :type is_gpu: bool
        :param descriptions: 产品描述。
        :type descriptions: str
        :param charge_mode: 周期套餐标识。0表示包周期，1表示按需, 6表示一次性计费。
        :type charge_mode: str
        :param resource_type: 资源规格。
        :type resource_type: str
        :param cloud_service_type: 云服务编码。
        :type cloud_service_type: str
        :param package_type: 套餐类型。 - user_sharer：用户协同套餐 - desktop_sharer: 桌面协同套餐
        :type package_type: str
        :param name: 产品名称&lt;语言，各语言对应的产品名&gt;。
        :type name: dict(str, str)
        :param share_space_size: 协同方数。该套餐支持的最大协同人数。
        :type share_space_size: int
        """
        
        

        self._product_id = None
        self._is_gpu = None
        self._descriptions = None
        self._charge_mode = None
        self._resource_type = None
        self._cloud_service_type = None
        self._package_type = None
        self._name = None
        self._share_space_size = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if is_gpu is not None:
            self.is_gpu = is_gpu
        if descriptions is not None:
            self.descriptions = descriptions
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if resource_type is not None:
            self.resource_type = resource_type
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if package_type is not None:
            self.package_type = package_type
        if name is not None:
            self.name = name
        if share_space_size is not None:
            self.share_space_size = share_space_size

    @property
    def product_id(self):
        r"""Gets the product_id of this SharerProductInfo.

        产品ID。

        :return: The product_id of this SharerProductInfo.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this SharerProductInfo.

        产品ID。

        :param product_id: The product_id of this SharerProductInfo.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def is_gpu(self):
        r"""Gets the is_gpu of this SharerProductInfo.

        是否是GPU类型的规格。

        :return: The is_gpu of this SharerProductInfo.
        :rtype: bool
        """
        return self._is_gpu

    @is_gpu.setter
    def is_gpu(self, is_gpu):
        r"""Sets the is_gpu of this SharerProductInfo.

        是否是GPU类型的规格。

        :param is_gpu: The is_gpu of this SharerProductInfo.
        :type is_gpu: bool
        """
        self._is_gpu = is_gpu

    @property
    def descriptions(self):
        r"""Gets the descriptions of this SharerProductInfo.

        产品描述。

        :return: The descriptions of this SharerProductInfo.
        :rtype: str
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        r"""Sets the descriptions of this SharerProductInfo.

        产品描述。

        :param descriptions: The descriptions of this SharerProductInfo.
        :type descriptions: str
        """
        self._descriptions = descriptions

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this SharerProductInfo.

        周期套餐标识。0表示包周期，1表示按需, 6表示一次性计费。

        :return: The charge_mode of this SharerProductInfo.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this SharerProductInfo.

        周期套餐标识。0表示包周期，1表示按需, 6表示一次性计费。

        :param charge_mode: The charge_mode of this SharerProductInfo.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def resource_type(self):
        r"""Gets the resource_type of this SharerProductInfo.

        资源规格。

        :return: The resource_type of this SharerProductInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this SharerProductInfo.

        资源规格。

        :param resource_type: The resource_type of this SharerProductInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this SharerProductInfo.

        云服务编码。

        :return: The cloud_service_type of this SharerProductInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this SharerProductInfo.

        云服务编码。

        :param cloud_service_type: The cloud_service_type of this SharerProductInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def package_type(self):
        r"""Gets the package_type of this SharerProductInfo.

        套餐类型。 - user_sharer：用户协同套餐 - desktop_sharer: 桌面协同套餐

        :return: The package_type of this SharerProductInfo.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        r"""Sets the package_type of this SharerProductInfo.

        套餐类型。 - user_sharer：用户协同套餐 - desktop_sharer: 桌面协同套餐

        :param package_type: The package_type of this SharerProductInfo.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def name(self):
        r"""Gets the name of this SharerProductInfo.

        产品名称<语言，各语言对应的产品名>。

        :return: The name of this SharerProductInfo.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SharerProductInfo.

        产品名称<语言，各语言对应的产品名>。

        :param name: The name of this SharerProductInfo.
        :type name: dict(str, str)
        """
        self._name = name

    @property
    def share_space_size(self):
        r"""Gets the share_space_size of this SharerProductInfo.

        协同方数。该套餐支持的最大协同人数。

        :return: The share_space_size of this SharerProductInfo.
        :rtype: int
        """
        return self._share_space_size

    @share_space_size.setter
    def share_space_size(self, share_space_size):
        r"""Sets the share_space_size of this SharerProductInfo.

        协同方数。该套餐支持的最大协同人数。

        :param share_space_size: The share_space_size of this SharerProductInfo.
        :type share_space_size: int
        """
        self._share_space_size = share_space_size

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
        if not isinstance(other, SharerProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
