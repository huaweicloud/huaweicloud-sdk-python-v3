# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceUsageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'str',
        'business': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'business': 'business'
    }

    def __init__(self, resource=None, business=None):
        r"""ShowResourceUsageRequest

        The model defined in huaweicloud sdk

        :param resource: 资源类型。可填多个，用\&quot;,\&quot;分隔。详见[资源类型](metastudio_02_0042.xml)。
        :type resource: str
        :param business: 业务类型。可填多个，用\&quot;,\&quot;分隔。 * VOICE_CLONE：声音制作 * SYNTHETICS_SOUND：声音合成 * ASSET_MANAGER：资产管理 * MODELING_2D：形象制作 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作 * CHAT_2D：分身数字人智能交互 * BUSINESS_CARD_2D：分身数字人名片 * PICTURE_2D：照片数字人视频 * MODELING_3D：3D照片建模 * VDS_3D：3D视觉驱动 * TTSA_3D：3D语音驱动 * FLEXUS_2D：FLEXUS版本资源
        :type business: str
        """
        
        

        self._resource = None
        self._business = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if business is not None:
            self.business = business

    @property
    def resource(self):
        r"""Gets the resource of this ShowResourceUsageRequest.

        资源类型。可填多个，用\",\"分隔。详见[资源类型](metastudio_02_0042.xml)。

        :return: The resource of this ShowResourceUsageRequest.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this ShowResourceUsageRequest.

        资源类型。可填多个，用\",\"分隔。详见[资源类型](metastudio_02_0042.xml)。

        :param resource: The resource of this ShowResourceUsageRequest.
        :type resource: str
        """
        self._resource = resource

    @property
    def business(self):
        r"""Gets the business of this ShowResourceUsageRequest.

        业务类型。可填多个，用\",\"分隔。 * VOICE_CLONE：声音制作 * SYNTHETICS_SOUND：声音合成 * ASSET_MANAGER：资产管理 * MODELING_2D：形象制作 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作 * CHAT_2D：分身数字人智能交互 * BUSINESS_CARD_2D：分身数字人名片 * PICTURE_2D：照片数字人视频 * MODELING_3D：3D照片建模 * VDS_3D：3D视觉驱动 * TTSA_3D：3D语音驱动 * FLEXUS_2D：FLEXUS版本资源

        :return: The business of this ShowResourceUsageRequest.
        :rtype: str
        """
        return self._business

    @business.setter
    def business(self, business):
        r"""Sets the business of this ShowResourceUsageRequest.

        业务类型。可填多个，用\",\"分隔。 * VOICE_CLONE：声音制作 * SYNTHETICS_SOUND：声音合成 * ASSET_MANAGER：资产管理 * MODELING_2D：形象制作 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作 * CHAT_2D：分身数字人智能交互 * BUSINESS_CARD_2D：分身数字人名片 * PICTURE_2D：照片数字人视频 * MODELING_3D：3D照片建模 * VDS_3D：3D视觉驱动 * TTSA_3D：3D语音驱动 * FLEXUS_2D：FLEXUS版本资源

        :param business: The business of this ShowResourceUsageRequest.
        :type business: str
        """
        self._business = business

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
        if not isinstance(other, ShowResourceUsageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
