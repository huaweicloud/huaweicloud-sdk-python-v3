# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDataParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'force': 'bool',
        'item_id': 'str',
        'desc': 'str',
        'custom_tags': 'dict(str, str)',
        'custom_num_tags': 'dict(str, float)',
        'image_base64': 'str',
        'image_url': 'str',
        'keywords': 'list[str]',
        'optional_params': 'AddDataOptionalParam'
    }

    attribute_map = {
        'force': 'force',
        'item_id': 'item_id',
        'desc': 'desc',
        'custom_tags': 'custom_tags',
        'custom_num_tags': 'custom_num_tags',
        'image_base64': 'image_base64',
        'image_url': 'image_url',
        'keywords': 'keywords',
        'optional_params': 'optional_params'
    }

    def __init__(self, force=None, item_id=None, desc=None, custom_tags=None, custom_num_tags=None, image_base64=None, image_url=None, keywords=None, optional_params=None):
        """AddDataParam

        The model defined in huaweicloud sdk

        :param force: 是否强制添加数据，默认为false。 - false: 数据已存在则不进行添加。 - true: 数据已存在仍然覆盖添加。
        :type force: bool
        :param item_id: 数据的服务实例级唯一标识，字符长度范围为[1, 256]。
        :type item_id: str
        :param desc: 数据的描述信息，字符长度范围为[1, 2048]。
        :type desc: str
        :param custom_tags: 数据的自定义字符标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为字符串，字符长度范围为[1, 64]。
        :type custom_tags: dict(str, str)
        :param custom_num_tags: 数据的自定义数值标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为数值，格式为double。
        :type custom_num_tags: dict(str, float)
        :param image_base64: 图像文件的base64字符串，图像入库时，与image_url二选一。要求如下： - 格式：目前仅支持JPEG/JPG/PNG/BMP/WEBP格式的图像。 - 大小：图像文件大小要求不超过5M。 - 尺寸：默认情况下，要求图像的最短边大于64px，最长边小于4096px。部分服务类型有特殊要求，可参见服务类型说明。 - 其他：图片中不能包含旋转信息。
        :type image_base64: str
        :param image_url: 图像文件的服务可访问URL，字符长度范围为[1, 4096]。图像入库时，与image_base64二选一。
        :type image_url: str
        :param keywords: 关键词列表，关键词数量范围为[1, 100]，关键词字符长度范围为[1, 64]。支持关键词搜索的服务实例添加数据时，如给定此参数，则直接使用给定的keywords作为关键词，否则会自动生成对应的keywords。
        :type keywords: list[str]
        :param optional_params: 
        :type optional_params: :class:`huaweicloudsdkimagesearch.v2.AddDataOptionalParam`
        """
        
        

        self._force = None
        self._item_id = None
        self._desc = None
        self._custom_tags = None
        self._custom_num_tags = None
        self._image_base64 = None
        self._image_url = None
        self._keywords = None
        self._optional_params = None
        self.discriminator = None

        if force is not None:
            self.force = force
        self.item_id = item_id
        if desc is not None:
            self.desc = desc
        if custom_tags is not None:
            self.custom_tags = custom_tags
        if custom_num_tags is not None:
            self.custom_num_tags = custom_num_tags
        if image_base64 is not None:
            self.image_base64 = image_base64
        if image_url is not None:
            self.image_url = image_url
        if keywords is not None:
            self.keywords = keywords
        if optional_params is not None:
            self.optional_params = optional_params

    @property
    def force(self):
        """Gets the force of this AddDataParam.

        是否强制添加数据，默认为false。 - false: 数据已存在则不进行添加。 - true: 数据已存在仍然覆盖添加。

        :return: The force of this AddDataParam.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this AddDataParam.

        是否强制添加数据，默认为false。 - false: 数据已存在则不进行添加。 - true: 数据已存在仍然覆盖添加。

        :param force: The force of this AddDataParam.
        :type force: bool
        """
        self._force = force

    @property
    def item_id(self):
        """Gets the item_id of this AddDataParam.

        数据的服务实例级唯一标识，字符长度范围为[1, 256]。

        :return: The item_id of this AddDataParam.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this AddDataParam.

        数据的服务实例级唯一标识，字符长度范围为[1, 256]。

        :param item_id: The item_id of this AddDataParam.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def desc(self):
        """Gets the desc of this AddDataParam.

        数据的描述信息，字符长度范围为[1, 2048]。

        :return: The desc of this AddDataParam.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this AddDataParam.

        数据的描述信息，字符长度范围为[1, 2048]。

        :param desc: The desc of this AddDataParam.
        :type desc: str
        """
        self._desc = desc

    @property
    def custom_tags(self):
        """Gets the custom_tags of this AddDataParam.

        数据的自定义字符标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为字符串，字符长度范围为[1, 64]。

        :return: The custom_tags of this AddDataParam.
        :rtype: dict(str, str)
        """
        return self._custom_tags

    @custom_tags.setter
    def custom_tags(self, custom_tags):
        """Sets the custom_tags of this AddDataParam.

        数据的自定义字符标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为字符串，字符长度范围为[1, 64]。

        :param custom_tags: The custom_tags of this AddDataParam.
        :type custom_tags: dict(str, str)
        """
        self._custom_tags = custom_tags

    @property
    def custom_num_tags(self):
        """Gets the custom_num_tags of this AddDataParam.

        数据的自定义数值标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为数值，格式为double。

        :return: The custom_num_tags of this AddDataParam.
        :rtype: dict(str, float)
        """
        return self._custom_num_tags

    @custom_num_tags.setter
    def custom_num_tags(self, custom_num_tags):
        """Sets the custom_num_tags of this AddDataParam.

        数据的自定义数值标签，用于进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 类型为数值，格式为double。

        :param custom_num_tags: The custom_num_tags of this AddDataParam.
        :type custom_num_tags: dict(str, float)
        """
        self._custom_num_tags = custom_num_tags

    @property
    def image_base64(self):
        """Gets the image_base64 of this AddDataParam.

        图像文件的base64字符串，图像入库时，与image_url二选一。要求如下： - 格式：目前仅支持JPEG/JPG/PNG/BMP/WEBP格式的图像。 - 大小：图像文件大小要求不超过5M。 - 尺寸：默认情况下，要求图像的最短边大于64px，最长边小于4096px。部分服务类型有特殊要求，可参见服务类型说明。 - 其他：图片中不能包含旋转信息。

        :return: The image_base64 of this AddDataParam.
        :rtype: str
        """
        return self._image_base64

    @image_base64.setter
    def image_base64(self, image_base64):
        """Sets the image_base64 of this AddDataParam.

        图像文件的base64字符串，图像入库时，与image_url二选一。要求如下： - 格式：目前仅支持JPEG/JPG/PNG/BMP/WEBP格式的图像。 - 大小：图像文件大小要求不超过5M。 - 尺寸：默认情况下，要求图像的最短边大于64px，最长边小于4096px。部分服务类型有特殊要求，可参见服务类型说明。 - 其他：图片中不能包含旋转信息。

        :param image_base64: The image_base64 of this AddDataParam.
        :type image_base64: str
        """
        self._image_base64 = image_base64

    @property
    def image_url(self):
        """Gets the image_url of this AddDataParam.

        图像文件的服务可访问URL，字符长度范围为[1, 4096]。图像入库时，与image_base64二选一。

        :return: The image_url of this AddDataParam.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this AddDataParam.

        图像文件的服务可访问URL，字符长度范围为[1, 4096]。图像入库时，与image_base64二选一。

        :param image_url: The image_url of this AddDataParam.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def keywords(self):
        """Gets the keywords of this AddDataParam.

        关键词列表，关键词数量范围为[1, 100]，关键词字符长度范围为[1, 64]。支持关键词搜索的服务实例添加数据时，如给定此参数，则直接使用给定的keywords作为关键词，否则会自动生成对应的keywords。

        :return: The keywords of this AddDataParam.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this AddDataParam.

        关键词列表，关键词数量范围为[1, 100]，关键词字符长度范围为[1, 64]。支持关键词搜索的服务实例添加数据时，如给定此参数，则直接使用给定的keywords作为关键词，否则会自动生成对应的keywords。

        :param keywords: The keywords of this AddDataParam.
        :type keywords: list[str]
        """
        self._keywords = keywords

    @property
    def optional_params(self):
        """Gets the optional_params of this AddDataParam.

        :return: The optional_params of this AddDataParam.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.AddDataOptionalParam`
        """
        return self._optional_params

    @optional_params.setter
    def optional_params(self, optional_params):
        """Sets the optional_params of this AddDataParam.

        :param optional_params: The optional_params of this AddDataParam.
        :type optional_params: :class:`huaweicloudsdkimagesearch.v2.AddDataOptionalParam`
        """
        self._optional_params = optional_params

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
        if not isinstance(other, AddDataParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
