# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PPTAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_analysis': 'bool',
        'ppt_analysis_status': 'str',
        'error_info': 'ErrorResponse',
        'page_count': 'int',
        'pages': 'list[PPTPageInfo]'
    }

    attribute_map = {
        'auto_analysis': 'auto_analysis',
        'ppt_analysis_status': 'ppt_analysis_status',
        'error_info': 'error_info',
        'page_count': 'page_count',
        'pages': 'pages'
    }

    def __init__(self, auto_analysis=None, ppt_analysis_status=None, error_info=None, page_count=None, pages=None):
        r"""PPTAssetMeta

        The model defined in huaweicloud sdk

        :param auto_analysis: **参数解释**： PPT是否需要自动解析。 **约束限制**： 部分过于复杂的PPT或压缩比过高的PPT可能无法解析。 超过50页PPT仅转换50页 转换的图片无法保证完全还原，需要自行确认。 **取值范围**： * true: 自动解析 * false: 无需解析
        :type auto_analysis: bool
        :param ppt_analysis_status: **参数解释**： PPT解析状态。 **约束限制**： 不涉及 **取值范围**： * INITIALIZE：初始 * WAITING：等待 * CONVERTING：解析中 * FAILED：失败 * SUCCEEDED：成功 * CANCELED：取消  **默认取值**： 不涉及
        :type ppt_analysis_status: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        :param page_count: **参数解释**： PPT页面总数。 **约束限制**： 不涉及
        :type page_count: int
        :param pages: PPT页面图片。
        :type pages: list[:class:`huaweicloudsdkmetastudio.v1.PPTPageInfo`]
        """
        
        

        self._auto_analysis = None
        self._ppt_analysis_status = None
        self._error_info = None
        self._page_count = None
        self._pages = None
        self.discriminator = None

        if auto_analysis is not None:
            self.auto_analysis = auto_analysis
        if ppt_analysis_status is not None:
            self.ppt_analysis_status = ppt_analysis_status
        if error_info is not None:
            self.error_info = error_info
        if page_count is not None:
            self.page_count = page_count
        if pages is not None:
            self.pages = pages

    @property
    def auto_analysis(self):
        r"""Gets the auto_analysis of this PPTAssetMeta.

        **参数解释**： PPT是否需要自动解析。 **约束限制**： 部分过于复杂的PPT或压缩比过高的PPT可能无法解析。 超过50页PPT仅转换50页 转换的图片无法保证完全还原，需要自行确认。 **取值范围**： * true: 自动解析 * false: 无需解析

        :return: The auto_analysis of this PPTAssetMeta.
        :rtype: bool
        """
        return self._auto_analysis

    @auto_analysis.setter
    def auto_analysis(self, auto_analysis):
        r"""Sets the auto_analysis of this PPTAssetMeta.

        **参数解释**： PPT是否需要自动解析。 **约束限制**： 部分过于复杂的PPT或压缩比过高的PPT可能无法解析。 超过50页PPT仅转换50页 转换的图片无法保证完全还原，需要自行确认。 **取值范围**： * true: 自动解析 * false: 无需解析

        :param auto_analysis: The auto_analysis of this PPTAssetMeta.
        :type auto_analysis: bool
        """
        self._auto_analysis = auto_analysis

    @property
    def ppt_analysis_status(self):
        r"""Gets the ppt_analysis_status of this PPTAssetMeta.

        **参数解释**： PPT解析状态。 **约束限制**： 不涉及 **取值范围**： * INITIALIZE：初始 * WAITING：等待 * CONVERTING：解析中 * FAILED：失败 * SUCCEEDED：成功 * CANCELED：取消  **默认取值**： 不涉及

        :return: The ppt_analysis_status of this PPTAssetMeta.
        :rtype: str
        """
        return self._ppt_analysis_status

    @ppt_analysis_status.setter
    def ppt_analysis_status(self, ppt_analysis_status):
        r"""Sets the ppt_analysis_status of this PPTAssetMeta.

        **参数解释**： PPT解析状态。 **约束限制**： 不涉及 **取值范围**： * INITIALIZE：初始 * WAITING：等待 * CONVERTING：解析中 * FAILED：失败 * SUCCEEDED：成功 * CANCELED：取消  **默认取值**： 不涉及

        :param ppt_analysis_status: The ppt_analysis_status of this PPTAssetMeta.
        :type ppt_analysis_status: str
        """
        self._ppt_analysis_status = ppt_analysis_status

    @property
    def error_info(self):
        r"""Gets the error_info of this PPTAssetMeta.

        :return: The error_info of this PPTAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this PPTAssetMeta.

        :param error_info: The error_info of this PPTAssetMeta.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

    @property
    def page_count(self):
        r"""Gets the page_count of this PPTAssetMeta.

        **参数解释**： PPT页面总数。 **约束限制**： 不涉及

        :return: The page_count of this PPTAssetMeta.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        r"""Sets the page_count of this PPTAssetMeta.

        **参数解释**： PPT页面总数。 **约束限制**： 不涉及

        :param page_count: The page_count of this PPTAssetMeta.
        :type page_count: int
        """
        self._page_count = page_count

    @property
    def pages(self):
        r"""Gets the pages of this PPTAssetMeta.

        PPT页面图片。

        :return: The pages of this PPTAssetMeta.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.PPTPageInfo`]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        r"""Sets the pages of this PPTAssetMeta.

        PPT页面图片。

        :param pages: The pages of this PPTAssetMeta.
        :type pages: list[:class:`huaweicloudsdkmetastudio.v1.PPTPageInfo`]
        """
        self._pages = pages

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
        if not isinstance(other, PPTAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
