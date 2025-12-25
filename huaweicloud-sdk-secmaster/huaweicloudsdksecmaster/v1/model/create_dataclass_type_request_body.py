# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDataclassTypeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_category': 'str',
        'sub_category_code': 'str',
        'category': 'str',
        'category_code': 'str',
        'name': 'str',
        'business_code': 'str',
        'dataclass_business_code': 'str',
        'description': 'str',
        'level': 'int',
        'enabled': 'bool',
        'sla': 'int'
    }

    attribute_map = {
        'sub_category': 'sub_category',
        'sub_category_code': 'sub_category_code',
        'category': 'category',
        'category_code': 'category_code',
        'name': 'name',
        'business_code': 'business_code',
        'dataclass_business_code': 'dataclass_business_code',
        'description': 'description',
        'level': 'level',
        'enabled': 'enabled',
        'sla': 'sla'
    }

    def __init__(self, sub_category=None, sub_category_code=None, category=None, category_code=None, name=None, business_code=None, dataclass_business_code=None, description=None, level=None, enabled=None, sla=None):
        r"""CreateDataclassTypeRequestBody

        The model defined in huaweicloud sdk

        :param sub_category: 子类型名称，告警类型、事件类型必填；威胁情报、漏洞类型、自定义类型不填
        :type sub_category: str
        :param sub_category_code: 子类型标识。告警类型、事件类型必填；威胁情报、漏洞类型、自定义类型不填
        :type sub_category_code: str
        :param category: 类型名称，告警类型、事件类型、威胁情报、漏洞类型必填；自定义类型不填
        :type category: str
        :param category_code: 类型标识。告警类型、事件类型、威胁情报、漏洞类型必填；自定义类型不填
        :type category_code: str
        :param name: 自定义类型名称。创建类型时，代表类型名称，创建子类型时，代表子类型名称。（自定义类型必填，其余类型不填）
        :type name: str
        :param business_code: 自定义类型标识。创建类型时代表类型标识；创建子类型时代表子类型标识。（自定义类型必填，其余类型不填）
        :type business_code: str
        :param dataclass_business_code: 数据类业务编码，创建自定义类型必填。（其余类型不填）
        :type dataclass_business_code: str
        :param description: 类型描述
        :type description: str
        :param level: 类型层级，创建自定义类型必填，枚举值：1-类型，2-子类型。（其余类型不填）
        :type level: int
        :param enabled: 类型启用禁用状态，启用：true，禁用：false
        :type enabled: bool
        :param sla: 响应时长
        :type sla: int
        """
        
        

        self._sub_category = None
        self._sub_category_code = None
        self._category = None
        self._category_code = None
        self._name = None
        self._business_code = None
        self._dataclass_business_code = None
        self._description = None
        self._level = None
        self._enabled = None
        self._sla = None
        self.discriminator = None

        if sub_category is not None:
            self.sub_category = sub_category
        if sub_category_code is not None:
            self.sub_category_code = sub_category_code
        if category is not None:
            self.category = category
        if category_code is not None:
            self.category_code = category_code
        if name is not None:
            self.name = name
        if business_code is not None:
            self.business_code = business_code
        if dataclass_business_code is not None:
            self.dataclass_business_code = dataclass_business_code
        if description is not None:
            self.description = description
        if level is not None:
            self.level = level
        self.enabled = enabled
        self.sla = sla

    @property
    def sub_category(self):
        r"""Gets the sub_category of this CreateDataclassTypeRequestBody.

        子类型名称，告警类型、事件类型必填；威胁情报、漏洞类型、自定义类型不填

        :return: The sub_category of this CreateDataclassTypeRequestBody.
        :rtype: str
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        r"""Sets the sub_category of this CreateDataclassTypeRequestBody.

        子类型名称，告警类型、事件类型必填；威胁情报、漏洞类型、自定义类型不填

        :param sub_category: The sub_category of this CreateDataclassTypeRequestBody.
        :type sub_category: str
        """
        self._sub_category = sub_category

    @property
    def sub_category_code(self):
        r"""Gets the sub_category_code of this CreateDataclassTypeRequestBody.

        子类型标识。告警类型、事件类型必填；威胁情报、漏洞类型、自定义类型不填

        :return: The sub_category_code of this CreateDataclassTypeRequestBody.
        :rtype: str
        """
        return self._sub_category_code

    @sub_category_code.setter
    def sub_category_code(self, sub_category_code):
        r"""Sets the sub_category_code of this CreateDataclassTypeRequestBody.

        子类型标识。告警类型、事件类型必填；威胁情报、漏洞类型、自定义类型不填

        :param sub_category_code: The sub_category_code of this CreateDataclassTypeRequestBody.
        :type sub_category_code: str
        """
        self._sub_category_code = sub_category_code

    @property
    def category(self):
        r"""Gets the category of this CreateDataclassTypeRequestBody.

        类型名称，告警类型、事件类型、威胁情报、漏洞类型必填；自定义类型不填

        :return: The category of this CreateDataclassTypeRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateDataclassTypeRequestBody.

        类型名称，告警类型、事件类型、威胁情报、漏洞类型必填；自定义类型不填

        :param category: The category of this CreateDataclassTypeRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def category_code(self):
        r"""Gets the category_code of this CreateDataclassTypeRequestBody.

        类型标识。告警类型、事件类型、威胁情报、漏洞类型必填；自定义类型不填

        :return: The category_code of this CreateDataclassTypeRequestBody.
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        r"""Sets the category_code of this CreateDataclassTypeRequestBody.

        类型标识。告警类型、事件类型、威胁情报、漏洞类型必填；自定义类型不填

        :param category_code: The category_code of this CreateDataclassTypeRequestBody.
        :type category_code: str
        """
        self._category_code = category_code

    @property
    def name(self):
        r"""Gets the name of this CreateDataclassTypeRequestBody.

        自定义类型名称。创建类型时，代表类型名称，创建子类型时，代表子类型名称。（自定义类型必填，其余类型不填）

        :return: The name of this CreateDataclassTypeRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDataclassTypeRequestBody.

        自定义类型名称。创建类型时，代表类型名称，创建子类型时，代表子类型名称。（自定义类型必填，其余类型不填）

        :param name: The name of this CreateDataclassTypeRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def business_code(self):
        r"""Gets the business_code of this CreateDataclassTypeRequestBody.

        自定义类型标识。创建类型时代表类型标识；创建子类型时代表子类型标识。（自定义类型必填，其余类型不填）

        :return: The business_code of this CreateDataclassTypeRequestBody.
        :rtype: str
        """
        return self._business_code

    @business_code.setter
    def business_code(self, business_code):
        r"""Sets the business_code of this CreateDataclassTypeRequestBody.

        自定义类型标识。创建类型时代表类型标识；创建子类型时代表子类型标识。（自定义类型必填，其余类型不填）

        :param business_code: The business_code of this CreateDataclassTypeRequestBody.
        :type business_code: str
        """
        self._business_code = business_code

    @property
    def dataclass_business_code(self):
        r"""Gets the dataclass_business_code of this CreateDataclassTypeRequestBody.

        数据类业务编码，创建自定义类型必填。（其余类型不填）

        :return: The dataclass_business_code of this CreateDataclassTypeRequestBody.
        :rtype: str
        """
        return self._dataclass_business_code

    @dataclass_business_code.setter
    def dataclass_business_code(self, dataclass_business_code):
        r"""Sets the dataclass_business_code of this CreateDataclassTypeRequestBody.

        数据类业务编码，创建自定义类型必填。（其余类型不填）

        :param dataclass_business_code: The dataclass_business_code of this CreateDataclassTypeRequestBody.
        :type dataclass_business_code: str
        """
        self._dataclass_business_code = dataclass_business_code

    @property
    def description(self):
        r"""Gets the description of this CreateDataclassTypeRequestBody.

        类型描述

        :return: The description of this CreateDataclassTypeRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDataclassTypeRequestBody.

        类型描述

        :param description: The description of this CreateDataclassTypeRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def level(self):
        r"""Gets the level of this CreateDataclassTypeRequestBody.

        类型层级，创建自定义类型必填，枚举值：1-类型，2-子类型。（其余类型不填）

        :return: The level of this CreateDataclassTypeRequestBody.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CreateDataclassTypeRequestBody.

        类型层级，创建自定义类型必填，枚举值：1-类型，2-子类型。（其余类型不填）

        :param level: The level of this CreateDataclassTypeRequestBody.
        :type level: int
        """
        self._level = level

    @property
    def enabled(self):
        r"""Gets the enabled of this CreateDataclassTypeRequestBody.

        类型启用禁用状态，启用：true，禁用：false

        :return: The enabled of this CreateDataclassTypeRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CreateDataclassTypeRequestBody.

        类型启用禁用状态，启用：true，禁用：false

        :param enabled: The enabled of this CreateDataclassTypeRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def sla(self):
        r"""Gets the sla of this CreateDataclassTypeRequestBody.

        响应时长

        :return: The sla of this CreateDataclassTypeRequestBody.
        :rtype: int
        """
        return self._sla

    @sla.setter
    def sla(self, sla):
        r"""Sets the sla of this CreateDataclassTypeRequestBody.

        响应时长

        :param sla: The sla of this CreateDataclassTypeRequestBody.
        :type sla: int
        """
        self._sla = sla

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
        if not isinstance(other, CreateDataclassTypeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
