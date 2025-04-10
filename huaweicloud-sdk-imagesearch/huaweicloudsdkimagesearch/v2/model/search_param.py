# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'last_item': 'SearchAfterParam',
        'min_score': 'float',
        'custom_tags': 'dict(str, list[str])',
        'custom_num_tags': 'dict(str, RangeParam)',
        'image_base64': 'str',
        'image_url': 'str',
        'keywords': 'list[str]',
        'text': 'str',
        'optional_params': 'SearchOptionalParam'
    }

    attribute_map = {
        'search_type': 'search_type',
        'limit': 'limit',
        'offset': 'offset',
        'last_item': 'last_item',
        'min_score': 'min_score',
        'custom_tags': 'custom_tags',
        'custom_num_tags': 'custom_num_tags',
        'image_base64': 'image_base64',
        'image_url': 'image_url',
        'keywords': 'keywords',
        'text': 'text',
        'optional_params': 'optional_params'
    }

    def __init__(self, search_type=None, limit=None, offset=None, last_item=None, min_score=None, custom_tags=None, custom_num_tags=None, image_base64=None, image_url=None, keywords=None, text=None, optional_params=None):
        r"""SearchParam

        The model defined in huaweicloud sdk

        :param search_type: 搜索类型，必须为服务实例支持的搜索类型。服务实例的搜索类型列表可在创建服务实例时进行配置。 &gt; 可以使用枚举名或者枚举值（例如IMAGE/0），枚举值可能会变动，建议使用枚举名。
        :type search_type: str
        :param limit: 返回搜索结果的数量，默认为10，取值范围为[1, 1000]。
        :type limit: int
        :param offset: 返回搜索结果的偏移量，即返回序号在[offset, offset+limit]内的搜索结果。默认为0，取值范围为[0, N]。 - 默认情况下，搜索要求offset+limit &lt;&#x3D; 1000。 - 针对支持全量召回的场景，使用全量召回时，要求offset必须为0。
        :type offset: int
        :param last_item: 
        :type last_item: :class:`huaweicloudsdkimagesearch.v2.SearchAfterParam`
        :param min_score: 返回搜索结果的最小得分，用于对搜索结果进行score过滤，取值范围为[0, 1]。 - 目前仅对IMAGE/CATEGORY搜索类型生效。
        :type min_score: float
        :param custom_tags: 自定义字符标签，用于对搜索结果进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 标签值列表，列表内多个标签值为“或”关系，即满足一个即可。列表长度范围为[1, 32]，标签值类型为字符串，字符长度范围为[1, 64]。
        :type custom_tags: dict(str, list[str])
        :param custom_num_tags: 自定义数值标签，用于对搜索结果进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。针对没有设置该数值标签的数据，会直接过滤。 - value: 标签值的取值范围，标签值在给定的取值范围内即视为符合条件。
        :type custom_num_tags: dict(str, RangeParam)
        :param image_base64: 图像文件的base64字符串，基于图像搜索时，与image_url二选一。要求如下： - 格式：目前仅支持JPEG/JPG/PNG/BMP/WEBP格式的图像。 - 大小：图像文件大小要求不超过5M。 - 尺寸：默认情况下，要求图像的最短边大于64px，最长边小于4096px。部分服务类型有特殊要求，可参见服务类型说明。 - 其他：图片中不能包含旋转信息。
        :type image_base64: str
        :param image_url: 图像文件的服务可访问URL，字符长度范围为[1, 4096]。基于图像搜索时，与image_base64二选一。
        :type image_url: str
        :param keywords: 关键词列表，搜索时关键词数量范围为[1, 10]，关键词字符长度范围为[1, 64]。使用KEYWORD搜索类型进行搜索时，必须提供该参数。
        :type keywords: list[str]
        :param text: 文本字符串，字符长度范围为[1, 512]。
        :type text: str
        :param optional_params: 
        :type optional_params: :class:`huaweicloudsdkimagesearch.v2.SearchOptionalParam`
        """
        
        

        self._search_type = None
        self._limit = None
        self._offset = None
        self._last_item = None
        self._min_score = None
        self._custom_tags = None
        self._custom_num_tags = None
        self._image_base64 = None
        self._image_url = None
        self._keywords = None
        self._text = None
        self._optional_params = None
        self.discriminator = None

        self.search_type = search_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if last_item is not None:
            self.last_item = last_item
        if min_score is not None:
            self.min_score = min_score
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
        if text is not None:
            self.text = text
        if optional_params is not None:
            self.optional_params = optional_params

    @property
    def search_type(self):
        r"""Gets the search_type of this SearchParam.

        搜索类型，必须为服务实例支持的搜索类型。服务实例的搜索类型列表可在创建服务实例时进行配置。 > 可以使用枚举名或者枚举值（例如IMAGE/0），枚举值可能会变动，建议使用枚举名。

        :return: The search_type of this SearchParam.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this SearchParam.

        搜索类型，必须为服务实例支持的搜索类型。服务实例的搜索类型列表可在创建服务实例时进行配置。 > 可以使用枚举名或者枚举值（例如IMAGE/0），枚举值可能会变动，建议使用枚举名。

        :param search_type: The search_type of this SearchParam.
        :type search_type: str
        """
        self._search_type = search_type

    @property
    def limit(self):
        r"""Gets the limit of this SearchParam.

        返回搜索结果的数量，默认为10，取值范围为[1, 1000]。

        :return: The limit of this SearchParam.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchParam.

        返回搜索结果的数量，默认为10，取值范围为[1, 1000]。

        :param limit: The limit of this SearchParam.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this SearchParam.

        返回搜索结果的偏移量，即返回序号在[offset, offset+limit]内的搜索结果。默认为0，取值范围为[0, N]。 - 默认情况下，搜索要求offset+limit <= 1000。 - 针对支持全量召回的场景，使用全量召回时，要求offset必须为0。

        :return: The offset of this SearchParam.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SearchParam.

        返回搜索结果的偏移量，即返回序号在[offset, offset+limit]内的搜索结果。默认为0，取值范围为[0, N]。 - 默认情况下，搜索要求offset+limit <= 1000。 - 针对支持全量召回的场景，使用全量召回时，要求offset必须为0。

        :param offset: The offset of this SearchParam.
        :type offset: int
        """
        self._offset = offset

    @property
    def last_item(self):
        r"""Gets the last_item of this SearchParam.

        :return: The last_item of this SearchParam.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.SearchAfterParam`
        """
        return self._last_item

    @last_item.setter
    def last_item(self, last_item):
        r"""Sets the last_item of this SearchParam.

        :param last_item: The last_item of this SearchParam.
        :type last_item: :class:`huaweicloudsdkimagesearch.v2.SearchAfterParam`
        """
        self._last_item = last_item

    @property
    def min_score(self):
        r"""Gets the min_score of this SearchParam.

        返回搜索结果的最小得分，用于对搜索结果进行score过滤，取值范围为[0, 1]。 - 目前仅对IMAGE/CATEGORY搜索类型生效。

        :return: The min_score of this SearchParam.
        :rtype: float
        """
        return self._min_score

    @min_score.setter
    def min_score(self, min_score):
        r"""Sets the min_score of this SearchParam.

        返回搜索结果的最小得分，用于对搜索结果进行score过滤，取值范围为[0, 1]。 - 目前仅对IMAGE/CATEGORY搜索类型生效。

        :param min_score: The min_score of this SearchParam.
        :type min_score: float
        """
        self._min_score = min_score

    @property
    def custom_tags(self):
        r"""Gets the custom_tags of this SearchParam.

        自定义字符标签，用于对搜索结果进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 标签值列表，列表内多个标签值为“或”关系，即满足一个即可。列表长度范围为[1, 32]，标签值类型为字符串，字符长度范围为[1, 64]。

        :return: The custom_tags of this SearchParam.
        :rtype: dict(str, list[str])
        """
        return self._custom_tags

    @custom_tags.setter
    def custom_tags(self, custom_tags):
        r"""Sets the custom_tags of this SearchParam.

        自定义字符标签，用于对搜索结果进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。 - value: 标签值列表，列表内多个标签值为“或”关系，即满足一个即可。列表长度范围为[1, 32]，标签值类型为字符串，字符长度范围为[1, 64]。

        :param custom_tags: The custom_tags of this SearchParam.
        :type custom_tags: dict(str, list[str])
        """
        self._custom_tags = custom_tags

    @property
    def custom_num_tags(self):
        r"""Gets the custom_num_tags of this SearchParam.

        自定义数值标签，用于对搜索结果进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。针对没有设置该数值标签的数据，会直接过滤。 - value: 标签值的取值范围，标签值在给定的取值范围内即视为符合条件。

        :return: The custom_num_tags of this SearchParam.
        :rtype: dict(str, RangeParam)
        """
        return self._custom_num_tags

    @custom_num_tags.setter
    def custom_num_tags(self, custom_num_tags):
        r"""Sets the custom_num_tags of this SearchParam.

        自定义数值标签，用于对搜索结果进行条件过滤。格式为键值对{key:value}。 - key: 必须为服务实例custom_num_tags中已存在的key，可在创建服务实例时进行配置，或在更新服务实例时进行新增。针对没有设置该数值标签的数据，会直接过滤。 - value: 标签值的取值范围，标签值在给定的取值范围内即视为符合条件。

        :param custom_num_tags: The custom_num_tags of this SearchParam.
        :type custom_num_tags: dict(str, RangeParam)
        """
        self._custom_num_tags = custom_num_tags

    @property
    def image_base64(self):
        r"""Gets the image_base64 of this SearchParam.

        图像文件的base64字符串，基于图像搜索时，与image_url二选一。要求如下： - 格式：目前仅支持JPEG/JPG/PNG/BMP/WEBP格式的图像。 - 大小：图像文件大小要求不超过5M。 - 尺寸：默认情况下，要求图像的最短边大于64px，最长边小于4096px。部分服务类型有特殊要求，可参见服务类型说明。 - 其他：图片中不能包含旋转信息。

        :return: The image_base64 of this SearchParam.
        :rtype: str
        """
        return self._image_base64

    @image_base64.setter
    def image_base64(self, image_base64):
        r"""Sets the image_base64 of this SearchParam.

        图像文件的base64字符串，基于图像搜索时，与image_url二选一。要求如下： - 格式：目前仅支持JPEG/JPG/PNG/BMP/WEBP格式的图像。 - 大小：图像文件大小要求不超过5M。 - 尺寸：默认情况下，要求图像的最短边大于64px，最长边小于4096px。部分服务类型有特殊要求，可参见服务类型说明。 - 其他：图片中不能包含旋转信息。

        :param image_base64: The image_base64 of this SearchParam.
        :type image_base64: str
        """
        self._image_base64 = image_base64

    @property
    def image_url(self):
        r"""Gets the image_url of this SearchParam.

        图像文件的服务可访问URL，字符长度范围为[1, 4096]。基于图像搜索时，与image_base64二选一。

        :return: The image_url of this SearchParam.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this SearchParam.

        图像文件的服务可访问URL，字符长度范围为[1, 4096]。基于图像搜索时，与image_base64二选一。

        :param image_url: The image_url of this SearchParam.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def keywords(self):
        r"""Gets the keywords of this SearchParam.

        关键词列表，搜索时关键词数量范围为[1, 10]，关键词字符长度范围为[1, 64]。使用KEYWORD搜索类型进行搜索时，必须提供该参数。

        :return: The keywords of this SearchParam.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this SearchParam.

        关键词列表，搜索时关键词数量范围为[1, 10]，关键词字符长度范围为[1, 64]。使用KEYWORD搜索类型进行搜索时，必须提供该参数。

        :param keywords: The keywords of this SearchParam.
        :type keywords: list[str]
        """
        self._keywords = keywords

    @property
    def text(self):
        r"""Gets the text of this SearchParam.

        文本字符串，字符长度范围为[1, 512]。

        :return: The text of this SearchParam.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this SearchParam.

        文本字符串，字符长度范围为[1, 512]。

        :param text: The text of this SearchParam.
        :type text: str
        """
        self._text = text

    @property
    def optional_params(self):
        r"""Gets the optional_params of this SearchParam.

        :return: The optional_params of this SearchParam.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.SearchOptionalParam`
        """
        return self._optional_params

    @optional_params.setter
    def optional_params(self, optional_params):
        r"""Sets the optional_params of this SearchParam.

        :param optional_params: The optional_params of this SearchParam.
        :type optional_params: :class:`huaweicloudsdkimagesearch.v2.SearchOptionalParam`
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
        if not isinstance(other, SearchParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
