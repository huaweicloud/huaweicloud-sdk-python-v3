# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OtaModuleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'module_id': 'str',
        'app_id': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'module_name': 'str',
        'alias_name': 'str',
        'description': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'module_id': 'module_id',
        'app_id': 'app_id',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'module_name': 'module_name',
        'alias_name': 'alias_name',
        'description': 'description',
        'create_time': 'create_time'
    }

    def __init__(self, module_id=None, app_id=None, product_id=None, product_name=None, module_name=None, alias_name=None, description=None, create_time=None):
        r"""OtaModuleInfo

        The model defined in huaweicloud sdk

        :param module_id: OTA模块ID
        :type module_id: str
        :param app_id: 资源空间ID
        :type app_id: str
        :param product_id: OTA模块关联的产品ID
        :type product_id: str
        :param product_name: OTA模块关联的产品名称
        :type product_name: str
        :param module_name: OTA模块名称。
        :type module_name: str
        :param alias_name: OTA模块别名
        :type alias_name: str
        :param description: 用于描述模块的功能等信息
        :type description: str
        :param create_time: 创建OTA模块的时间，格式：\&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;。
        :type create_time: str
        """
        
        

        self._module_id = None
        self._app_id = None
        self._product_id = None
        self._product_name = None
        self._module_name = None
        self._alias_name = None
        self._description = None
        self._create_time = None
        self.discriminator = None

        if module_id is not None:
            self.module_id = module_id
        if app_id is not None:
            self.app_id = app_id
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if module_name is not None:
            self.module_name = module_name
        if alias_name is not None:
            self.alias_name = alias_name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time

    @property
    def module_id(self):
        r"""Gets the module_id of this OtaModuleInfo.

        OTA模块ID

        :return: The module_id of this OtaModuleInfo.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this OtaModuleInfo.

        OTA模块ID

        :param module_id: The module_id of this OtaModuleInfo.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def app_id(self):
        r"""Gets the app_id of this OtaModuleInfo.

        资源空间ID

        :return: The app_id of this OtaModuleInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this OtaModuleInfo.

        资源空间ID

        :param app_id: The app_id of this OtaModuleInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def product_id(self):
        r"""Gets the product_id of this OtaModuleInfo.

        OTA模块关联的产品ID

        :return: The product_id of this OtaModuleInfo.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this OtaModuleInfo.

        OTA模块关联的产品ID

        :param product_id: The product_id of this OtaModuleInfo.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        r"""Gets the product_name of this OtaModuleInfo.

        OTA模块关联的产品名称

        :return: The product_name of this OtaModuleInfo.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this OtaModuleInfo.

        OTA模块关联的产品名称

        :param product_name: The product_name of this OtaModuleInfo.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def module_name(self):
        r"""Gets the module_name of this OtaModuleInfo.

        OTA模块名称。

        :return: The module_name of this OtaModuleInfo.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this OtaModuleInfo.

        OTA模块名称。

        :param module_name: The module_name of this OtaModuleInfo.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def alias_name(self):
        r"""Gets the alias_name of this OtaModuleInfo.

        OTA模块别名

        :return: The alias_name of this OtaModuleInfo.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        r"""Sets the alias_name of this OtaModuleInfo.

        OTA模块别名

        :param alias_name: The alias_name of this OtaModuleInfo.
        :type alias_name: str
        """
        self._alias_name = alias_name

    @property
    def description(self):
        r"""Gets the description of this OtaModuleInfo.

        用于描述模块的功能等信息

        :return: The description of this OtaModuleInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OtaModuleInfo.

        用于描述模块的功能等信息

        :param description: The description of this OtaModuleInfo.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this OtaModuleInfo.

        创建OTA模块的时间，格式：\"yyyyMMdd'T'HHmmss'Z'\"。

        :return: The create_time of this OtaModuleInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this OtaModuleInfo.

        创建OTA模块的时间，格式：\"yyyyMMdd'T'HHmmss'Z'\"。

        :param create_time: The create_time of this OtaModuleInfo.
        :type create_time: str
        """
        self._create_time = create_time

    def to_dict(self):
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
        if not isinstance(other, OtaModuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
