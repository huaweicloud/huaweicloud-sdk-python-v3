# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextDetectionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'categories': 'list[str]',
        'white_glossaries': 'list[str]',
        'items': 'list[TextDetectionItemsReq]'
    }

    attribute_map = {
        'categories': 'categories',
        'white_glossaries': 'white_glossaries',
        'items': 'items'
    }

    def __init__(self, categories=None, white_glossaries=None, items=None):
        """TextDetectionReq

        The model defined in huaweicloud sdk

        :param categories: 检测场景。  当前支持的场景有默认场景和用户自定义场景：  - 默认场景为：     * politics：涉政     * porn：涉黄     * ad：广告     * abuse：辱骂     * contraband：违禁品     * flood：灌水   - 用户自定义场景为：自定义黑名单词库。  &gt; - 自定义词库的创建和使用请参见[配置自定义词库](https://support.huaweicloud.com/api-moderation/moderation_03_0027.html)。 &gt; - flood场景不支持使用自定义白名单词库。
        :type categories: list[str]
        :param white_glossaries: 启用的白名单列表  当前白名单使用规则为：  - 不传参数\&quot;white_glossaries\&quot;：     * 表示默认使用2022-09-02 16:00:00之前创建的白名单词库  - 传参数\&quot;white_glossaries\&quot;：   * 参数为空时不使用任何白名单词库     * 参数不为空时使用传入的白名单词库  &gt; - 自定义词库的创建和使用请参见[[配置自定义词库](https://support.huaweicloud.com/api-moderation/moderation_03_0027.html)](tag:hc)。
        :type white_glossaries: list[str]
        :param items: 待检测的文本列表，目前暂时每次只支持传一个item。
        :type items: list[:class:`huaweicloudsdkmoderation.v2.TextDetectionItemsReq`]
        """
        
        

        self._categories = None
        self._white_glossaries = None
        self._items = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories
        if white_glossaries is not None:
            self.white_glossaries = white_glossaries
        self.items = items

    @property
    def categories(self):
        """Gets the categories of this TextDetectionReq.

        检测场景。  当前支持的场景有默认场景和用户自定义场景：  - 默认场景为：     * politics：涉政     * porn：涉黄     * ad：广告     * abuse：辱骂     * contraband：违禁品     * flood：灌水   - 用户自定义场景为：自定义黑名单词库。  > - 自定义词库的创建和使用请参见[配置自定义词库](https://support.huaweicloud.com/api-moderation/moderation_03_0027.html)。 > - flood场景不支持使用自定义白名单词库。

        :return: The categories of this TextDetectionReq.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this TextDetectionReq.

        检测场景。  当前支持的场景有默认场景和用户自定义场景：  - 默认场景为：     * politics：涉政     * porn：涉黄     * ad：广告     * abuse：辱骂     * contraband：违禁品     * flood：灌水   - 用户自定义场景为：自定义黑名单词库。  > - 自定义词库的创建和使用请参见[配置自定义词库](https://support.huaweicloud.com/api-moderation/moderation_03_0027.html)。 > - flood场景不支持使用自定义白名单词库。

        :param categories: The categories of this TextDetectionReq.
        :type categories: list[str]
        """
        self._categories = categories

    @property
    def white_glossaries(self):
        """Gets the white_glossaries of this TextDetectionReq.

        启用的白名单列表  当前白名单使用规则为：  - 不传参数\"white_glossaries\"：     * 表示默认使用2022-09-02 16:00:00之前创建的白名单词库  - 传参数\"white_glossaries\"：   * 参数为空时不使用任何白名单词库     * 参数不为空时使用传入的白名单词库  > - 自定义词库的创建和使用请参见[[配置自定义词库](https://support.huaweicloud.com/api-moderation/moderation_03_0027.html)](tag:hc)。

        :return: The white_glossaries of this TextDetectionReq.
        :rtype: list[str]
        """
        return self._white_glossaries

    @white_glossaries.setter
    def white_glossaries(self, white_glossaries):
        """Sets the white_glossaries of this TextDetectionReq.

        启用的白名单列表  当前白名单使用规则为：  - 不传参数\"white_glossaries\"：     * 表示默认使用2022-09-02 16:00:00之前创建的白名单词库  - 传参数\"white_glossaries\"：   * 参数为空时不使用任何白名单词库     * 参数不为空时使用传入的白名单词库  > - 自定义词库的创建和使用请参见[[配置自定义词库](https://support.huaweicloud.com/api-moderation/moderation_03_0027.html)](tag:hc)。

        :param white_glossaries: The white_glossaries of this TextDetectionReq.
        :type white_glossaries: list[str]
        """
        self._white_glossaries = white_glossaries

    @property
    def items(self):
        """Gets the items of this TextDetectionReq.

        待检测的文本列表，目前暂时每次只支持传一个item。

        :return: The items of this TextDetectionReq.
        :rtype: list[:class:`huaweicloudsdkmoderation.v2.TextDetectionItemsReq`]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this TextDetectionReq.

        待检测的文本列表，目前暂时每次只支持传一个item。

        :param items: The items of this TextDetectionReq.
        :type items: list[:class:`huaweicloudsdkmoderation.v2.TextDetectionItemsReq`]
        """
        self._items = items

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
        if not isinstance(other, TextDetectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
