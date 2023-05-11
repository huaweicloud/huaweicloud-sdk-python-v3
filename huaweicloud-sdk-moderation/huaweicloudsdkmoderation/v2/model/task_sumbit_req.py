# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskSumbitReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'urls': 'list[str]',
        'categories': 'list[str]',
        'moderation_rule': 'str',
        'ad_categories': 'list[str]',
        'show_ocr_text': 'bool'
    }

    attribute_map = {
        'urls': 'urls',
        'categories': 'categories',
        'moderation_rule': 'moderation_rule',
        'ad_categories': 'ad_categories',
        'show_ocr_text': 'show_ocr_text'
    }

    def __init__(self, urls=None, categories=None, moderation_rule=None, ad_categories=None, show_ocr_text=None):
        """TaskSumbitReq

        The model defined in huaweicloud sdk

        :param urls: 图片的URL路径，目前支持： - 公网HTTP/HTTPS URL - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[配置OBS访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)。 &gt; 图片的URL路径列表最多支持500个URL地址。接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 
        :type urls: list[str]
        :param categories: 检测场景。  - politics：是否涉及政治人物的检测。  - terrorism：是否包含涉政敏感人物、涉政暴恐元素的检测。  - porn：是否包含涉黄内容元素的检测。  可通过配置上述场景，来完成对应场景元素的检测。  为空或无此参数时默认检测politics和terrorism(不包含porn)。 
        :type categories: list[str]
        :param moderation_rule: 图像审核规则名称，默认使用default规则。 审核规则的创建和使用请参见[配置审核规则](https://support.huaweicloud.com/api-moderation/moderation_03_0063.html)。 
        :type moderation_rule: str
        :param ad_categories: 图文审核检测场景。当categories包含ad时，该参数生效。  当前支持的场景有系统场景和用户自定义场景: - 系统场景为：   - qr_code：二维码   - politics：涉政   - porn：涉黄   - ad：广告   - abuse：辱骂   - contraband：违禁品 - 用户自定义场景为：自定义黑名单词库。  自定义词库的创建和使用请参见[配置自定义词库](https://support.huaweicloud.com/api-moderation/moderation_03_0027.html)。 
        :type ad_categories: list[str]
        :param show_ocr_text: 是否返回ocr识别的结果。
        :type show_ocr_text: bool
        """
        
        

        self._urls = None
        self._categories = None
        self._moderation_rule = None
        self._ad_categories = None
        self._show_ocr_text = None
        self.discriminator = None

        self.urls = urls
        if categories is not None:
            self.categories = categories
        if moderation_rule is not None:
            self.moderation_rule = moderation_rule
        if ad_categories is not None:
            self.ad_categories = ad_categories
        if show_ocr_text is not None:
            self.show_ocr_text = show_ocr_text

    @property
    def urls(self):
        """Gets the urls of this TaskSumbitReq.

        图片的URL路径，目前支持： - 公网HTTP/HTTPS URL - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[配置OBS访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)。 > 图片的URL路径列表最多支持500个URL地址。接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :return: The urls of this TaskSumbitReq.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this TaskSumbitReq.

        图片的URL路径，目前支持： - 公网HTTP/HTTPS URL - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[配置OBS访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)。 > 图片的URL路径列表最多支持500个URL地址。接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :param urls: The urls of this TaskSumbitReq.
        :type urls: list[str]
        """
        self._urls = urls

    @property
    def categories(self):
        """Gets the categories of this TaskSumbitReq.

        检测场景。  - politics：是否涉及政治人物的检测。  - terrorism：是否包含涉政敏感人物、涉政暴恐元素的检测。  - porn：是否包含涉黄内容元素的检测。  可通过配置上述场景，来完成对应场景元素的检测。  为空或无此参数时默认检测politics和terrorism(不包含porn)。 

        :return: The categories of this TaskSumbitReq.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this TaskSumbitReq.

        检测场景。  - politics：是否涉及政治人物的检测。  - terrorism：是否包含涉政敏感人物、涉政暴恐元素的检测。  - porn：是否包含涉黄内容元素的检测。  可通过配置上述场景，来完成对应场景元素的检测。  为空或无此参数时默认检测politics和terrorism(不包含porn)。 

        :param categories: The categories of this TaskSumbitReq.
        :type categories: list[str]
        """
        self._categories = categories

    @property
    def moderation_rule(self):
        """Gets the moderation_rule of this TaskSumbitReq.

        图像审核规则名称，默认使用default规则。 审核规则的创建和使用请参见[配置审核规则](https://support.huaweicloud.com/api-moderation/moderation_03_0063.html)。 

        :return: The moderation_rule of this TaskSumbitReq.
        :rtype: str
        """
        return self._moderation_rule

    @moderation_rule.setter
    def moderation_rule(self, moderation_rule):
        """Sets the moderation_rule of this TaskSumbitReq.

        图像审核规则名称，默认使用default规则。 审核规则的创建和使用请参见[配置审核规则](https://support.huaweicloud.com/api-moderation/moderation_03_0063.html)。 

        :param moderation_rule: The moderation_rule of this TaskSumbitReq.
        :type moderation_rule: str
        """
        self._moderation_rule = moderation_rule

    @property
    def ad_categories(self):
        """Gets the ad_categories of this TaskSumbitReq.

        图文审核检测场景。当categories包含ad时，该参数生效。  当前支持的场景有系统场景和用户自定义场景: - 系统场景为：   - qr_code：二维码   - politics：涉政   - porn：涉黄   - ad：广告   - abuse：辱骂   - contraband：违禁品 - 用户自定义场景为：自定义黑名单词库。  自定义词库的创建和使用请参见[配置自定义词库](https://support.huaweicloud.com/api-moderation/moderation_03_0027.html)。 

        :return: The ad_categories of this TaskSumbitReq.
        :rtype: list[str]
        """
        return self._ad_categories

    @ad_categories.setter
    def ad_categories(self, ad_categories):
        """Sets the ad_categories of this TaskSumbitReq.

        图文审核检测场景。当categories包含ad时，该参数生效。  当前支持的场景有系统场景和用户自定义场景: - 系统场景为：   - qr_code：二维码   - politics：涉政   - porn：涉黄   - ad：广告   - abuse：辱骂   - contraband：违禁品 - 用户自定义场景为：自定义黑名单词库。  自定义词库的创建和使用请参见[配置自定义词库](https://support.huaweicloud.com/api-moderation/moderation_03_0027.html)。 

        :param ad_categories: The ad_categories of this TaskSumbitReq.
        :type ad_categories: list[str]
        """
        self._ad_categories = ad_categories

    @property
    def show_ocr_text(self):
        """Gets the show_ocr_text of this TaskSumbitReq.

        是否返回ocr识别的结果。

        :return: The show_ocr_text of this TaskSumbitReq.
        :rtype: bool
        """
        return self._show_ocr_text

    @show_ocr_text.setter
    def show_ocr_text(self, show_ocr_text):
        """Sets the show_ocr_text of this TaskSumbitReq.

        是否返回ocr识别的结果。

        :param show_ocr_text: The show_ocr_text of this TaskSumbitReq.
        :type show_ocr_text: bool
        """
        self._show_ocr_text = show_ocr_text

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
        if not isinstance(other, TaskSumbitReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
