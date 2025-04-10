# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageMediaTaggingItemBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'confidence': 'str',
        'type': 'str',
        'tag': 'str',
        'i18n_tag': 'ImageMediaTaggingItemBodyI18nTag',
        'i18n_type': 'ImageMediaTaggingItemBodyI18nType',
        'instances': 'list[ImageMediaTaggingInstance]'
    }

    attribute_map = {
        'confidence': 'confidence',
        'type': 'type',
        'tag': 'tag',
        'i18n_tag': 'i18n_tag',
        'i18n_type': 'i18n_type',
        'instances': 'instances'
    }

    def __init__(self, confidence=None, type=None, tag=None, i18n_tag=None, i18n_type=None, instances=None):
        r"""ImageMediaTaggingItemBody

        The model defined in huaweicloud sdk

        :param confidence: 置信度，将Float型置信度转为String类型返回,取值范围：0-100。
        :type confidence: str
        :param type: 标签的类别。返回的标签类型，包含二十多种大类，具体可以参考[[图像标签](http://support.huaweicloud.com/image_faq/image_01_0037.html)](tag:hc)[[图像标签](https://support.huaweicloud.com/intl/zh-cn/image_faq/image_01_0037.html)](tag:hk) 
        :type type: str
        :param tag: 标签名称。
        :type tag: str
        :param i18n_tag: 
        :type i18n_tag: :class:`huaweicloudsdkimage.v2.ImageMediaTaggingItemBodyI18nTag`
        :param i18n_type: 
        :type i18n_type: :class:`huaweicloudsdkimage.v2.ImageMediaTaggingItemBodyI18nType`
        :param instances: 目标检测框信息，为空则表示没有目标检测框。
        :type instances: list[:class:`huaweicloudsdkimage.v2.ImageMediaTaggingInstance`]
        """
        
        

        self._confidence = None
        self._type = None
        self._tag = None
        self._i18n_tag = None
        self._i18n_type = None
        self._instances = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if type is not None:
            self.type = type
        if tag is not None:
            self.tag = tag
        if i18n_tag is not None:
            self.i18n_tag = i18n_tag
        if i18n_type is not None:
            self.i18n_type = i18n_type
        if instances is not None:
            self.instances = instances

    @property
    def confidence(self):
        r"""Gets the confidence of this ImageMediaTaggingItemBody.

        置信度，将Float型置信度转为String类型返回,取值范围：0-100。

        :return: The confidence of this ImageMediaTaggingItemBody.
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this ImageMediaTaggingItemBody.

        置信度，将Float型置信度转为String类型返回,取值范围：0-100。

        :param confidence: The confidence of this ImageMediaTaggingItemBody.
        :type confidence: str
        """
        self._confidence = confidence

    @property
    def type(self):
        r"""Gets the type of this ImageMediaTaggingItemBody.

        标签的类别。返回的标签类型，包含二十多种大类，具体可以参考[[图像标签](http://support.huaweicloud.com/image_faq/image_01_0037.html)](tag:hc)[[图像标签](https://support.huaweicloud.com/intl/zh-cn/image_faq/image_01_0037.html)](tag:hk) 

        :return: The type of this ImageMediaTaggingItemBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ImageMediaTaggingItemBody.

        标签的类别。返回的标签类型，包含二十多种大类，具体可以参考[[图像标签](http://support.huaweicloud.com/image_faq/image_01_0037.html)](tag:hc)[[图像标签](https://support.huaweicloud.com/intl/zh-cn/image_faq/image_01_0037.html)](tag:hk) 

        :param type: The type of this ImageMediaTaggingItemBody.
        :type type: str
        """
        self._type = type

    @property
    def tag(self):
        r"""Gets the tag of this ImageMediaTaggingItemBody.

        标签名称。

        :return: The tag of this ImageMediaTaggingItemBody.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ImageMediaTaggingItemBody.

        标签名称。

        :param tag: The tag of this ImageMediaTaggingItemBody.
        :type tag: str
        """
        self._tag = tag

    @property
    def i18n_tag(self):
        r"""Gets the i18n_tag of this ImageMediaTaggingItemBody.

        :return: The i18n_tag of this ImageMediaTaggingItemBody.
        :rtype: :class:`huaweicloudsdkimage.v2.ImageMediaTaggingItemBodyI18nTag`
        """
        return self._i18n_tag

    @i18n_tag.setter
    def i18n_tag(self, i18n_tag):
        r"""Sets the i18n_tag of this ImageMediaTaggingItemBody.

        :param i18n_tag: The i18n_tag of this ImageMediaTaggingItemBody.
        :type i18n_tag: :class:`huaweicloudsdkimage.v2.ImageMediaTaggingItemBodyI18nTag`
        """
        self._i18n_tag = i18n_tag

    @property
    def i18n_type(self):
        r"""Gets the i18n_type of this ImageMediaTaggingItemBody.

        :return: The i18n_type of this ImageMediaTaggingItemBody.
        :rtype: :class:`huaweicloudsdkimage.v2.ImageMediaTaggingItemBodyI18nType`
        """
        return self._i18n_type

    @i18n_type.setter
    def i18n_type(self, i18n_type):
        r"""Sets the i18n_type of this ImageMediaTaggingItemBody.

        :param i18n_type: The i18n_type of this ImageMediaTaggingItemBody.
        :type i18n_type: :class:`huaweicloudsdkimage.v2.ImageMediaTaggingItemBodyI18nType`
        """
        self._i18n_type = i18n_type

    @property
    def instances(self):
        r"""Gets the instances of this ImageMediaTaggingItemBody.

        目标检测框信息，为空则表示没有目标检测框。

        :return: The instances of this ImageMediaTaggingItemBody.
        :rtype: list[:class:`huaweicloudsdkimage.v2.ImageMediaTaggingInstance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ImageMediaTaggingItemBody.

        目标检测框信息，为空则表示没有目标检测框。

        :param instances: The instances of this ImageMediaTaggingItemBody.
        :type instances: list[:class:`huaweicloudsdkimage.v2.ImageMediaTaggingInstance`]
        """
        self._instances = instances

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
        if not isinstance(other, ImageMediaTaggingItemBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
