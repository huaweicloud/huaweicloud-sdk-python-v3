# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageDetectionResultDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'politics': 'list[ImageDetectionResultDetailPolitics]',
        'porn': 'list[ImageDetectionResultSimpleDetail]',
        'terrorism': 'list[ImageDetectionResultSimpleDetail]',
        'ad': 'list[ImageDetectionResultAdDetail]'
    }

    attribute_map = {
        'politics': 'politics',
        'porn': 'porn',
        'terrorism': 'terrorism',
        'ad': 'ad'
    }

    def __init__(self, politics=None, porn=None, terrorism=None, ad=None):
        """ImageDetectionResultDetail

        The model defined in huaweicloud sdk

        :param politics: 涉政敏感人物检测结果。
        :type politics: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultDetailPolitics`]
        :param porn: 涉黄检测结果。
        :type porn: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultSimpleDetail`]
        :param terrorism: 涉政、暴恐检测结果。
        :type terrorism: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultSimpleDetail`]
        :param ad: 广告检测结果。
        :type ad: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultAdDetail`]
        """
        
        

        self._politics = None
        self._porn = None
        self._terrorism = None
        self._ad = None
        self.discriminator = None

        if politics is not None:
            self.politics = politics
        if porn is not None:
            self.porn = porn
        if terrorism is not None:
            self.terrorism = terrorism
        if ad is not None:
            self.ad = ad

    @property
    def politics(self):
        """Gets the politics of this ImageDetectionResultDetail.

        涉政敏感人物检测结果。

        :return: The politics of this ImageDetectionResultDetail.
        :rtype: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultDetailPolitics`]
        """
        return self._politics

    @politics.setter
    def politics(self, politics):
        """Sets the politics of this ImageDetectionResultDetail.

        涉政敏感人物检测结果。

        :param politics: The politics of this ImageDetectionResultDetail.
        :type politics: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultDetailPolitics`]
        """
        self._politics = politics

    @property
    def porn(self):
        """Gets the porn of this ImageDetectionResultDetail.

        涉黄检测结果。

        :return: The porn of this ImageDetectionResultDetail.
        :rtype: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultSimpleDetail`]
        """
        return self._porn

    @porn.setter
    def porn(self, porn):
        """Sets the porn of this ImageDetectionResultDetail.

        涉黄检测结果。

        :param porn: The porn of this ImageDetectionResultDetail.
        :type porn: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultSimpleDetail`]
        """
        self._porn = porn

    @property
    def terrorism(self):
        """Gets the terrorism of this ImageDetectionResultDetail.

        涉政、暴恐检测结果。

        :return: The terrorism of this ImageDetectionResultDetail.
        :rtype: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultSimpleDetail`]
        """
        return self._terrorism

    @terrorism.setter
    def terrorism(self, terrorism):
        """Sets the terrorism of this ImageDetectionResultDetail.

        涉政、暴恐检测结果。

        :param terrorism: The terrorism of this ImageDetectionResultDetail.
        :type terrorism: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultSimpleDetail`]
        """
        self._terrorism = terrorism

    @property
    def ad(self):
        """Gets the ad of this ImageDetectionResultDetail.

        广告检测结果。

        :return: The ad of this ImageDetectionResultDetail.
        :rtype: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultAdDetail`]
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """Sets the ad of this ImageDetectionResultDetail.

        广告检测结果。

        :param ad: The ad of this ImageDetectionResultDetail.
        :type ad: list[:class:`huaweicloudsdkmoderation.v2.ImageDetectionResultAdDetail`]
        """
        self._ad = ad

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
        if not isinstance(other, ImageDetectionResultDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
