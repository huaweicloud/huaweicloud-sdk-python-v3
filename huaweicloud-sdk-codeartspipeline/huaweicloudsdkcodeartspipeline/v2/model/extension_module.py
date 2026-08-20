# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionModule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_url': 'str',
        'description': 'str',
        'id': 'int',
        'location': 'str',
        'module_id': 'str',
        'name': 'str',
        'properties': 'ExtensionModuleProperties',
        'publisher': 'str',
        'type': 'str',
        'version': 'str',
        'tags': 'list[str]',
        'url_relative': 'str',
        'properties_list': 'list[object]',
        'manifest_version': 'str',
        'categories': 'list[str]',
        'target': 'str',
        'product_line': 'str'
    }

    attribute_map = {
        'base_url': 'base_url',
        'description': 'description',
        'id': 'id',
        'location': 'location',
        'module_id': 'module_id',
        'name': 'name',
        'properties': 'properties',
        'publisher': 'publisher',
        'type': 'type',
        'version': 'version',
        'tags': 'tags',
        'url_relative': 'url_relative',
        'properties_list': 'properties_list',
        'manifest_version': 'manifest_version',
        'categories': 'categories',
        'target': 'target',
        'product_line': 'product_line'
    }

    def __init__(self, base_url=None, description=None, id=None, location=None, module_id=None, name=None, properties=None, publisher=None, type=None, version=None, tags=None, url_relative=None, properties_list=None, manifest_version=None, categories=None, target=None, product_line=None):
        r"""ExtensionModule

        The model defined in huaweicloud sdk

        :param base_url: 基础url
        :type base_url: str
        :param description: 描述
        :type description: str
        :param id: id
        :type id: int
        :param location: 扩展点
        :type location: str
        :param module_id: 模块id
        :type module_id: str
        :param name: 名称
        :type name: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionModuleProperties`
        :param publisher: 发布商
        :type publisher: str
        :param type: 类型
        :type type: str
        :param version: 版本
        :type version: str
        :param tags: 标签。
        :type tags: list[str]
        :param url_relative: 插件链接地址
        :type url_relative: str
        :param properties_list: 多版本属性列表
        :type properties_list: list[object]
        :param manifest_version: 摘要版本号
        :type manifest_version: str
        :param categories: 分类。
        :type categories: list[str]
        :param target: 目标。预留字段，通常为空。
        :type target: str
        :param product_line: 产品线。预留字段，通常为空。
        :type product_line: str
        """
        
        

        self._base_url = None
        self._description = None
        self._id = None
        self._location = None
        self._module_id = None
        self._name = None
        self._properties = None
        self._publisher = None
        self._type = None
        self._version = None
        self._tags = None
        self._url_relative = None
        self._properties_list = None
        self._manifest_version = None
        self._categories = None
        self._target = None
        self._product_line = None
        self.discriminator = None

        if base_url is not None:
            self.base_url = base_url
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if location is not None:
            self.location = location
        if module_id is not None:
            self.module_id = module_id
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties
        if publisher is not None:
            self.publisher = publisher
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if tags is not None:
            self.tags = tags
        if url_relative is not None:
            self.url_relative = url_relative
        if properties_list is not None:
            self.properties_list = properties_list
        if manifest_version is not None:
            self.manifest_version = manifest_version
        if categories is not None:
            self.categories = categories
        if target is not None:
            self.target = target
        if product_line is not None:
            self.product_line = product_line

    @property
    def base_url(self):
        r"""Gets the base_url of this ExtensionModule.

        基础url

        :return: The base_url of this ExtensionModule.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        r"""Sets the base_url of this ExtensionModule.

        基础url

        :param base_url: The base_url of this ExtensionModule.
        :type base_url: str
        """
        self._base_url = base_url

    @property
    def description(self):
        r"""Gets the description of this ExtensionModule.

        描述

        :return: The description of this ExtensionModule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExtensionModule.

        描述

        :param description: The description of this ExtensionModule.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this ExtensionModule.

        id

        :return: The id of this ExtensionModule.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExtensionModule.

        id

        :param id: The id of this ExtensionModule.
        :type id: int
        """
        self._id = id

    @property
    def location(self):
        r"""Gets the location of this ExtensionModule.

        扩展点

        :return: The location of this ExtensionModule.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ExtensionModule.

        扩展点

        :param location: The location of this ExtensionModule.
        :type location: str
        """
        self._location = location

    @property
    def module_id(self):
        r"""Gets the module_id of this ExtensionModule.

        模块id

        :return: The module_id of this ExtensionModule.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this ExtensionModule.

        模块id

        :param module_id: The module_id of this ExtensionModule.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def name(self):
        r"""Gets the name of this ExtensionModule.

        名称

        :return: The name of this ExtensionModule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExtensionModule.

        名称

        :param name: The name of this ExtensionModule.
        :type name: str
        """
        self._name = name

    @property
    def properties(self):
        r"""Gets the properties of this ExtensionModule.

        :return: The properties of this ExtensionModule.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionModuleProperties`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ExtensionModule.

        :param properties: The properties of this ExtensionModule.
        :type properties: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionModuleProperties`
        """
        self._properties = properties

    @property
    def publisher(self):
        r"""Gets the publisher of this ExtensionModule.

        发布商

        :return: The publisher of this ExtensionModule.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        r"""Sets the publisher of this ExtensionModule.

        发布商

        :param publisher: The publisher of this ExtensionModule.
        :type publisher: str
        """
        self._publisher = publisher

    @property
    def type(self):
        r"""Gets the type of this ExtensionModule.

        类型

        :return: The type of this ExtensionModule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExtensionModule.

        类型

        :param type: The type of this ExtensionModule.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this ExtensionModule.

        版本

        :return: The version of this ExtensionModule.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ExtensionModule.

        版本

        :param version: The version of this ExtensionModule.
        :type version: str
        """
        self._version = version

    @property
    def tags(self):
        r"""Gets the tags of this ExtensionModule.

        标签。

        :return: The tags of this ExtensionModule.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ExtensionModule.

        标签。

        :param tags: The tags of this ExtensionModule.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def url_relative(self):
        r"""Gets the url_relative of this ExtensionModule.

        插件链接地址

        :return: The url_relative of this ExtensionModule.
        :rtype: str
        """
        return self._url_relative

    @url_relative.setter
    def url_relative(self, url_relative):
        r"""Sets the url_relative of this ExtensionModule.

        插件链接地址

        :param url_relative: The url_relative of this ExtensionModule.
        :type url_relative: str
        """
        self._url_relative = url_relative

    @property
    def properties_list(self):
        r"""Gets the properties_list of this ExtensionModule.

        多版本属性列表

        :return: The properties_list of this ExtensionModule.
        :rtype: list[object]
        """
        return self._properties_list

    @properties_list.setter
    def properties_list(self, properties_list):
        r"""Sets the properties_list of this ExtensionModule.

        多版本属性列表

        :param properties_list: The properties_list of this ExtensionModule.
        :type properties_list: list[object]
        """
        self._properties_list = properties_list

    @property
    def manifest_version(self):
        r"""Gets the manifest_version of this ExtensionModule.

        摘要版本号

        :return: The manifest_version of this ExtensionModule.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        r"""Sets the manifest_version of this ExtensionModule.

        摘要版本号

        :param manifest_version: The manifest_version of this ExtensionModule.
        :type manifest_version: str
        """
        self._manifest_version = manifest_version

    @property
    def categories(self):
        r"""Gets the categories of this ExtensionModule.

        分类。

        :return: The categories of this ExtensionModule.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this ExtensionModule.

        分类。

        :param categories: The categories of this ExtensionModule.
        :type categories: list[str]
        """
        self._categories = categories

    @property
    def target(self):
        r"""Gets the target of this ExtensionModule.

        目标。预留字段，通常为空。

        :return: The target of this ExtensionModule.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this ExtensionModule.

        目标。预留字段，通常为空。

        :param target: The target of this ExtensionModule.
        :type target: str
        """
        self._target = target

    @property
    def product_line(self):
        r"""Gets the product_line of this ExtensionModule.

        产品线。预留字段，通常为空。

        :return: The product_line of this ExtensionModule.
        :rtype: str
        """
        return self._product_line

    @product_line.setter
    def product_line(self, product_line):
        r"""Sets the product_line of this ExtensionModule.

        产品线。预留字段，通常为空。

        :param product_line: The product_line of this ExtensionModule.
        :type product_line: str
        """
        self._product_line = product_line

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
        if not isinstance(other, ExtensionModule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
