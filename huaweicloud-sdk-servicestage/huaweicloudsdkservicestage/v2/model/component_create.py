# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'runtime': 'str',
        'category': 'str',
        'sub_category': 'str',
        'description': 'str',
        'source': 'SourceObject',
        'build': 'Build'
    }

    attribute_map = {
        'name': 'name',
        'runtime': 'runtime',
        'category': 'category',
        'sub_category': 'sub_category',
        'description': 'description',
        'source': 'source',
        'build': 'build'
    }

    def __init__(self, name=None, runtime=None, category=None, sub_category=None, description=None, source=None, build=None):
        r"""ComponentCreate

        The model defined in huaweicloud sdk

        :param name: 应用组件名称。
        :type name: str
        :param runtime: 运行时类型。
        :type runtime: str
        :param category: 应用组件类型包括：Webapp、MicroService、Common。
        :type category: str
        :param sub_category: 应用组件子类型。  Webapp的子类型有Web、Magento、Wordpress。  MicroService的子类型有Java Chassis、Go Chassis、Mesher、SpringCloud。  Common的子类型可以为空。 
        :type sub_category: str
        :param description: 描述。
        :type description: str
        :param source: 
        :type source: :class:`huaweicloudsdkservicestage.v2.SourceObject`
        :param build: 
        :type build: :class:`huaweicloudsdkservicestage.v2.Build`
        """
        
        

        self._name = None
        self._runtime = None
        self._category = None
        self._sub_category = None
        self._description = None
        self._source = None
        self._build = None
        self.discriminator = None

        self.name = name
        self.runtime = runtime
        self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        if description is not None:
            self.description = description
        if source is not None:
            self.source = source
        if build is not None:
            self.build = build

    @property
    def name(self):
        r"""Gets the name of this ComponentCreate.

        应用组件名称。

        :return: The name of this ComponentCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComponentCreate.

        应用组件名称。

        :param name: The name of this ComponentCreate.
        :type name: str
        """
        self._name = name

    @property
    def runtime(self):
        r"""Gets the runtime of this ComponentCreate.

        运行时类型。

        :return: The runtime of this ComponentCreate.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this ComponentCreate.

        运行时类型。

        :param runtime: The runtime of this ComponentCreate.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def category(self):
        r"""Gets the category of this ComponentCreate.

        应用组件类型包括：Webapp、MicroService、Common。

        :return: The category of this ComponentCreate.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ComponentCreate.

        应用组件类型包括：Webapp、MicroService、Common。

        :param category: The category of this ComponentCreate.
        :type category: str
        """
        self._category = category

    @property
    def sub_category(self):
        r"""Gets the sub_category of this ComponentCreate.

        应用组件子类型。  Webapp的子类型有Web、Magento、Wordpress。  MicroService的子类型有Java Chassis、Go Chassis、Mesher、SpringCloud。  Common的子类型可以为空。 

        :return: The sub_category of this ComponentCreate.
        :rtype: str
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        r"""Sets the sub_category of this ComponentCreate.

        应用组件子类型。  Webapp的子类型有Web、Magento、Wordpress。  MicroService的子类型有Java Chassis、Go Chassis、Mesher、SpringCloud。  Common的子类型可以为空。 

        :param sub_category: The sub_category of this ComponentCreate.
        :type sub_category: str
        """
        self._sub_category = sub_category

    @property
    def description(self):
        r"""Gets the description of this ComponentCreate.

        描述。

        :return: The description of this ComponentCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ComponentCreate.

        描述。

        :param description: The description of this ComponentCreate.
        :type description: str
        """
        self._description = description

    @property
    def source(self):
        r"""Gets the source of this ComponentCreate.

        :return: The source of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v2.SourceObject`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ComponentCreate.

        :param source: The source of this ComponentCreate.
        :type source: :class:`huaweicloudsdkservicestage.v2.SourceObject`
        """
        self._source = source

    @property
    def build(self):
        r"""Gets the build of this ComponentCreate.

        :return: The build of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v2.Build`
        """
        return self._build

    @build.setter
    def build(self, build):
        r"""Sets the build of this ComponentCreate.

        :param build: The build of this ComponentCreate.
        :type build: :class:`huaweicloudsdkservicestage.v2.Build`
        """
        self._build = build

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
        if not isinstance(other, ComponentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
