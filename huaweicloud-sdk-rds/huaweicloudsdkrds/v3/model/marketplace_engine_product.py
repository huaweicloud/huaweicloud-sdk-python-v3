# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MarketplaceEngineProduct:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_id': 'str',
        'engine_version': 'str',
        'spec_code': 'str',
        'product_id': 'str',
        'bp_name': 'str',
        'bp_domain_id': 'str',
        'instance_mode': 'str',
        'image_id': 'str',
        'user_license_agreement': 'str',
        'agreements': 'list[Agreement]'
    }

    attribute_map = {
        'engine_id': 'engine_id',
        'engine_version': 'engine_version',
        'spec_code': 'spec_code',
        'product_id': 'product_id',
        'bp_name': 'bp_name',
        'bp_domain_id': 'bp_domain_id',
        'instance_mode': 'instance_mode',
        'image_id': 'image_id',
        'user_license_agreement': 'user_license_agreement',
        'agreements': 'agreements'
    }

    def __init__(self, engine_id=None, engine_version=None, spec_code=None, product_id=None, bp_name=None, bp_domain_id=None, instance_mode=None, image_id=None, user_license_agreement=None, agreements=None):
        r"""MarketplaceEngineProduct

        The model defined in huaweicloud sdk

        :param engine_id: 引擎ID。
        :type engine_id: str
        :param engine_version: 引擎版本。
        :type engine_version: str
        :param spec_code: 云市场规格ID。
        :type spec_code: str
        :param product_id: 云市场商品ID。
        :type product_id: str
        :param bp_name: 服务商名称。
        :type bp_name: str
        :param bp_domain_id: 服务商ID。
        :type bp_domain_id: str
        :param instance_mode: 支持的实例类型。  - Single: 单机实例 - Ha: 主备实例 - Replica: 只读实例 - All: 以上类型都支持
        :type instance_mode: str
        :param image_id: 镜像ID。
        :type image_id: str
        :param user_license_agreement: 用户许可。
        :type user_license_agreement: str
        :param agreements: 许可详情列表。
        :type agreements: list[:class:`huaweicloudsdkrds.v3.Agreement`]
        """
        
        

        self._engine_id = None
        self._engine_version = None
        self._spec_code = None
        self._product_id = None
        self._bp_name = None
        self._bp_domain_id = None
        self._instance_mode = None
        self._image_id = None
        self._user_license_agreement = None
        self._agreements = None
        self.discriminator = None

        if engine_id is not None:
            self.engine_id = engine_id
        if engine_version is not None:
            self.engine_version = engine_version
        if spec_code is not None:
            self.spec_code = spec_code
        if product_id is not None:
            self.product_id = product_id
        if bp_name is not None:
            self.bp_name = bp_name
        if bp_domain_id is not None:
            self.bp_domain_id = bp_domain_id
        if instance_mode is not None:
            self.instance_mode = instance_mode
        if image_id is not None:
            self.image_id = image_id
        if user_license_agreement is not None:
            self.user_license_agreement = user_license_agreement
        if agreements is not None:
            self.agreements = agreements

    @property
    def engine_id(self):
        r"""Gets the engine_id of this MarketplaceEngineProduct.

        引擎ID。

        :return: The engine_id of this MarketplaceEngineProduct.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        r"""Sets the engine_id of this MarketplaceEngineProduct.

        引擎ID。

        :param engine_id: The engine_id of this MarketplaceEngineProduct.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def engine_version(self):
        r"""Gets the engine_version of this MarketplaceEngineProduct.

        引擎版本。

        :return: The engine_version of this MarketplaceEngineProduct.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this MarketplaceEngineProduct.

        引擎版本。

        :param engine_version: The engine_version of this MarketplaceEngineProduct.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def spec_code(self):
        r"""Gets the spec_code of this MarketplaceEngineProduct.

        云市场规格ID。

        :return: The spec_code of this MarketplaceEngineProduct.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this MarketplaceEngineProduct.

        云市场规格ID。

        :param spec_code: The spec_code of this MarketplaceEngineProduct.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def product_id(self):
        r"""Gets the product_id of this MarketplaceEngineProduct.

        云市场商品ID。

        :return: The product_id of this MarketplaceEngineProduct.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this MarketplaceEngineProduct.

        云市场商品ID。

        :param product_id: The product_id of this MarketplaceEngineProduct.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def bp_name(self):
        r"""Gets the bp_name of this MarketplaceEngineProduct.

        服务商名称。

        :return: The bp_name of this MarketplaceEngineProduct.
        :rtype: str
        """
        return self._bp_name

    @bp_name.setter
    def bp_name(self, bp_name):
        r"""Sets the bp_name of this MarketplaceEngineProduct.

        服务商名称。

        :param bp_name: The bp_name of this MarketplaceEngineProduct.
        :type bp_name: str
        """
        self._bp_name = bp_name

    @property
    def bp_domain_id(self):
        r"""Gets the bp_domain_id of this MarketplaceEngineProduct.

        服务商ID。

        :return: The bp_domain_id of this MarketplaceEngineProduct.
        :rtype: str
        """
        return self._bp_domain_id

    @bp_domain_id.setter
    def bp_domain_id(self, bp_domain_id):
        r"""Sets the bp_domain_id of this MarketplaceEngineProduct.

        服务商ID。

        :param bp_domain_id: The bp_domain_id of this MarketplaceEngineProduct.
        :type bp_domain_id: str
        """
        self._bp_domain_id = bp_domain_id

    @property
    def instance_mode(self):
        r"""Gets the instance_mode of this MarketplaceEngineProduct.

        支持的实例类型。  - Single: 单机实例 - Ha: 主备实例 - Replica: 只读实例 - All: 以上类型都支持

        :return: The instance_mode of this MarketplaceEngineProduct.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        r"""Sets the instance_mode of this MarketplaceEngineProduct.

        支持的实例类型。  - Single: 单机实例 - Ha: 主备实例 - Replica: 只读实例 - All: 以上类型都支持

        :param instance_mode: The instance_mode of this MarketplaceEngineProduct.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

    @property
    def image_id(self):
        r"""Gets the image_id of this MarketplaceEngineProduct.

        镜像ID。

        :return: The image_id of this MarketplaceEngineProduct.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this MarketplaceEngineProduct.

        镜像ID。

        :param image_id: The image_id of this MarketplaceEngineProduct.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def user_license_agreement(self):
        r"""Gets the user_license_agreement of this MarketplaceEngineProduct.

        用户许可。

        :return: The user_license_agreement of this MarketplaceEngineProduct.
        :rtype: str
        """
        return self._user_license_agreement

    @user_license_agreement.setter
    def user_license_agreement(self, user_license_agreement):
        r"""Sets the user_license_agreement of this MarketplaceEngineProduct.

        用户许可。

        :param user_license_agreement: The user_license_agreement of this MarketplaceEngineProduct.
        :type user_license_agreement: str
        """
        self._user_license_agreement = user_license_agreement

    @property
    def agreements(self):
        r"""Gets the agreements of this MarketplaceEngineProduct.

        许可详情列表。

        :return: The agreements of this MarketplaceEngineProduct.
        :rtype: list[:class:`huaweicloudsdkrds.v3.Agreement`]
        """
        return self._agreements

    @agreements.setter
    def agreements(self, agreements):
        r"""Sets the agreements of this MarketplaceEngineProduct.

        许可详情列表。

        :param agreements: The agreements of this MarketplaceEngineProduct.
        :type agreements: list[:class:`huaweicloudsdkrds.v3.Agreement`]
        """
        self._agreements = agreements

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
        if not isinstance(other, MarketplaceEngineProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
