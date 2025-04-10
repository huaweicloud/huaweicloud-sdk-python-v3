# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePortalInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'change_reason': 'str',
        'background_img': 'str',
        'summary': 'str',
        'tels': 'list[TelModel]',
        'fastapps': 'list[UpdatePortalFastappModel]',
        'hw_pubs': 'list[str]'
    }

    attribute_map = {
        'change_reason': 'change_reason',
        'background_img': 'background_img',
        'summary': 'summary',
        'tels': 'tels',
        'fastapps': 'fastapps',
        'hw_pubs': 'hw_pubs'
    }

    def __init__(self, change_reason=None, background_img=None, summary=None, tels=None, fastapps=None, hw_pubs=None):
        r"""UpdatePortalInfoRequestBody

        The model defined in huaweicloud sdk

        :param change_reason: 修改原因。
        :type change_reason: str
        :param background_img: 主页背景图片资源ID。 &gt; 分辨率大于等于1440*810，支持jpg、jpeg、bmp、png。参数值为上传智能信息服务号图片资源API返回的resource_id。 
        :type background_img: str
        :param summary: 简介。
        :type summary: str
        :param tels: 热线号列表。
        :type tels: list[:class:`huaweicloudsdkkoomessage.v1.TelModel`]
        :param fastapps: 快应用列表。
        :type fastapps: list[:class:`huaweicloudsdkkoomessage.v1.UpdatePortalFastappModel`]
        :param hw_pubs: 华为服务号列表。  &gt; 预留，暂未使用。 
        :type hw_pubs: list[str]
        """
        
        

        self._change_reason = None
        self._background_img = None
        self._summary = None
        self._tels = None
        self._fastapps = None
        self._hw_pubs = None
        self.discriminator = None

        self.change_reason = change_reason
        self.background_img = background_img
        self.summary = summary
        if tels is not None:
            self.tels = tels
        if fastapps is not None:
            self.fastapps = fastapps
        if hw_pubs is not None:
            self.hw_pubs = hw_pubs

    @property
    def change_reason(self):
        r"""Gets the change_reason of this UpdatePortalInfoRequestBody.

        修改原因。

        :return: The change_reason of this UpdatePortalInfoRequestBody.
        :rtype: str
        """
        return self._change_reason

    @change_reason.setter
    def change_reason(self, change_reason):
        r"""Sets the change_reason of this UpdatePortalInfoRequestBody.

        修改原因。

        :param change_reason: The change_reason of this UpdatePortalInfoRequestBody.
        :type change_reason: str
        """
        self._change_reason = change_reason

    @property
    def background_img(self):
        r"""Gets the background_img of this UpdatePortalInfoRequestBody.

        主页背景图片资源ID。 > 分辨率大于等于1440*810，支持jpg、jpeg、bmp、png。参数值为上传智能信息服务号图片资源API返回的resource_id。 

        :return: The background_img of this UpdatePortalInfoRequestBody.
        :rtype: str
        """
        return self._background_img

    @background_img.setter
    def background_img(self, background_img):
        r"""Sets the background_img of this UpdatePortalInfoRequestBody.

        主页背景图片资源ID。 > 分辨率大于等于1440*810，支持jpg、jpeg、bmp、png。参数值为上传智能信息服务号图片资源API返回的resource_id。 

        :param background_img: The background_img of this UpdatePortalInfoRequestBody.
        :type background_img: str
        """
        self._background_img = background_img

    @property
    def summary(self):
        r"""Gets the summary of this UpdatePortalInfoRequestBody.

        简介。

        :return: The summary of this UpdatePortalInfoRequestBody.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this UpdatePortalInfoRequestBody.

        简介。

        :param summary: The summary of this UpdatePortalInfoRequestBody.
        :type summary: str
        """
        self._summary = summary

    @property
    def tels(self):
        r"""Gets the tels of this UpdatePortalInfoRequestBody.

        热线号列表。

        :return: The tels of this UpdatePortalInfoRequestBody.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.TelModel`]
        """
        return self._tels

    @tels.setter
    def tels(self, tels):
        r"""Sets the tels of this UpdatePortalInfoRequestBody.

        热线号列表。

        :param tels: The tels of this UpdatePortalInfoRequestBody.
        :type tels: list[:class:`huaweicloudsdkkoomessage.v1.TelModel`]
        """
        self._tels = tels

    @property
    def fastapps(self):
        r"""Gets the fastapps of this UpdatePortalInfoRequestBody.

        快应用列表。

        :return: The fastapps of this UpdatePortalInfoRequestBody.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.UpdatePortalFastappModel`]
        """
        return self._fastapps

    @fastapps.setter
    def fastapps(self, fastapps):
        r"""Sets the fastapps of this UpdatePortalInfoRequestBody.

        快应用列表。

        :param fastapps: The fastapps of this UpdatePortalInfoRequestBody.
        :type fastapps: list[:class:`huaweicloudsdkkoomessage.v1.UpdatePortalFastappModel`]
        """
        self._fastapps = fastapps

    @property
    def hw_pubs(self):
        r"""Gets the hw_pubs of this UpdatePortalInfoRequestBody.

        华为服务号列表。  > 预留，暂未使用。 

        :return: The hw_pubs of this UpdatePortalInfoRequestBody.
        :rtype: list[str]
        """
        return self._hw_pubs

    @hw_pubs.setter
    def hw_pubs(self, hw_pubs):
        r"""Sets the hw_pubs of this UpdatePortalInfoRequestBody.

        华为服务号列表。  > 预留，暂未使用。 

        :param hw_pubs: The hw_pubs of this UpdatePortalInfoRequestBody.
        :type hw_pubs: list[str]
        """
        self._hw_pubs = hw_pubs

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
        if not isinstance(other, UpdatePortalInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
