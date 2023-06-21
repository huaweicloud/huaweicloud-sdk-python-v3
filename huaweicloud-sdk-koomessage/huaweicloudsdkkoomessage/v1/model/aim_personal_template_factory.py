# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AimPersonalTemplateFactory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'factory_type': 'str',
        'state': 'int'
    }

    attribute_map = {
        'factory_type': 'factory_type',
        'state': 'state'
    }

    def __init__(self, factory_type=None, state=None):
        """AimPersonalTemplateFactory

        The model defined in huaweicloud sdk

        :param factory_type: 厂商类型。  - HUAWEI：华为 - XIAOMI：小米 - OPPO：OPPO - VIVO：VIVO - MEIZU：魅族  &gt; 各厂商支持的布局类型，布局类型与card_id字段相对应。 &gt; - HUAWEI：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、长文本类（PureText）、横滑类1（Carousel）、横滑类2（CarouselTitle）、视频图文类（VideoImageAndText）、视频类（Video）、电商类（ECImageAndText）、红包类（RedPacket）、个性化红包类（RedPacketPersonal）、增强通知类（Notification2）、图片轮播类1:1（CarouselSquareImage）、图片轮播类16:9（CarouselImageSixteenToNine）、图片轮播类48:65（CarouselVerticalImage）、图文视频类（ImageTextAndVideo）、一般通知类（Notification1）、单卡券（CardVoucher）、多卡券（CardVouchers）、电商多商品类（Ecommerce）、机票类（Trip1）、火车票类（Trip2）、汽车票类（Trip3）、增强机票类（PlaneTrip）、海报类（SimplePoster）、超文本普通类（NativePureText）、超文本增强类（NativeImageAndText）、短剧视频类（ShortVideo） &gt; - XIAOMI：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、红包类（RedPacket）、增强通知类（Notification2）、一般通知类（Notification1） &gt; - OPPO：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、长文本类（PureText）、横滑类（Carousel）、视频类（Video）、电商类（ECImageAndText）、红包类（RedPacket）、图片轮播类1:1（CarouselSquareImage）、图片轮播类16:9（CarouselImageSixteenToNine）、图片轮播类48:65（CarouselVerticalImage） &gt; - MEIZU：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、横滑类1（Carousel）、横滑类2（CarouselTitle） &gt; -  VIVO：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、图片轮播类1:1（CarouselSquareImage）、图片轮播类16:9（CarouselImageSixteenToNine）、图片轮播类48:65（CarouselVerticalImage）、视频类（Video）、电商类（ECImageAndText）、红包类（RedPacket）、增强通知类（Notification2）、一般通知类（Notification1） 
        :type factory_type: str
        :param state: 支持状态。 - 1：支持 - 0：不支持 
        :type state: int
        """
        
        

        self._factory_type = None
        self._state = None
        self.discriminator = None

        self.factory_type = factory_type
        self.state = state

    @property
    def factory_type(self):
        """Gets the factory_type of this AimPersonalTemplateFactory.

        厂商类型。  - HUAWEI：华为 - XIAOMI：小米 - OPPO：OPPO - VIVO：VIVO - MEIZU：魅族  > 各厂商支持的布局类型，布局类型与card_id字段相对应。 > - HUAWEI：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、长文本类（PureText）、横滑类1（Carousel）、横滑类2（CarouselTitle）、视频图文类（VideoImageAndText）、视频类（Video）、电商类（ECImageAndText）、红包类（RedPacket）、个性化红包类（RedPacketPersonal）、增强通知类（Notification2）、图片轮播类1:1（CarouselSquareImage）、图片轮播类16:9（CarouselImageSixteenToNine）、图片轮播类48:65（CarouselVerticalImage）、图文视频类（ImageTextAndVideo）、一般通知类（Notification1）、单卡券（CardVoucher）、多卡券（CardVouchers）、电商多商品类（Ecommerce）、机票类（Trip1）、火车票类（Trip2）、汽车票类（Trip3）、增强机票类（PlaneTrip）、海报类（SimplePoster）、超文本普通类（NativePureText）、超文本增强类（NativeImageAndText）、短剧视频类（ShortVideo） > - XIAOMI：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、红包类（RedPacket）、增强通知类（Notification2）、一般通知类（Notification1） > - OPPO：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、长文本类（PureText）、横滑类（Carousel）、视频类（Video）、电商类（ECImageAndText）、红包类（RedPacket）、图片轮播类1:1（CarouselSquareImage）、图片轮播类16:9（CarouselImageSixteenToNine）、图片轮播类48:65（CarouselVerticalImage） > - MEIZU：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、横滑类1（Carousel）、横滑类2（CarouselTitle） > -  VIVO：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、图片轮播类1:1（CarouselSquareImage）、图片轮播类16:9（CarouselImageSixteenToNine）、图片轮播类48:65（CarouselVerticalImage）、视频类（Video）、电商类（ECImageAndText）、红包类（RedPacket）、增强通知类（Notification2）、一般通知类（Notification1） 

        :return: The factory_type of this AimPersonalTemplateFactory.
        :rtype: str
        """
        return self._factory_type

    @factory_type.setter
    def factory_type(self, factory_type):
        """Sets the factory_type of this AimPersonalTemplateFactory.

        厂商类型。  - HUAWEI：华为 - XIAOMI：小米 - OPPO：OPPO - VIVO：VIVO - MEIZU：魅族  > 各厂商支持的布局类型，布局类型与card_id字段相对应。 > - HUAWEI：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、长文本类（PureText）、横滑类1（Carousel）、横滑类2（CarouselTitle）、视频图文类（VideoImageAndText）、视频类（Video）、电商类（ECImageAndText）、红包类（RedPacket）、个性化红包类（RedPacketPersonal）、增强通知类（Notification2）、图片轮播类1:1（CarouselSquareImage）、图片轮播类16:9（CarouselImageSixteenToNine）、图片轮播类48:65（CarouselVerticalImage）、图文视频类（ImageTextAndVideo）、一般通知类（Notification1）、单卡券（CardVoucher）、多卡券（CardVouchers）、电商多商品类（Ecommerce）、机票类（Trip1）、火车票类（Trip2）、汽车票类（Trip3）、增强机票类（PlaneTrip）、海报类（SimplePoster）、超文本普通类（NativePureText）、超文本增强类（NativeImageAndText）、短剧视频类（ShortVideo） > - XIAOMI：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、红包类（RedPacket）、增强通知类（Notification2）、一般通知类（Notification1） > - OPPO：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、长文本类（PureText）、横滑类（Carousel）、视频类（Video）、电商类（ECImageAndText）、红包类（RedPacket）、图片轮播类1:1（CarouselSquareImage）、图片轮播类16:9（CarouselImageSixteenToNine）、图片轮播类48:65（CarouselVerticalImage） > - MEIZU：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、横滑类1（Carousel）、横滑类2（CarouselTitle） > -  VIVO：多图文类（MultipleImageAndText）、图文类（StandardImageAndText）、图片轮播类1:1（CarouselSquareImage）、图片轮播类16:9（CarouselImageSixteenToNine）、图片轮播类48:65（CarouselVerticalImage）、视频类（Video）、电商类（ECImageAndText）、红包类（RedPacket）、增强通知类（Notification2）、一般通知类（Notification1） 

        :param factory_type: The factory_type of this AimPersonalTemplateFactory.
        :type factory_type: str
        """
        self._factory_type = factory_type

    @property
    def state(self):
        """Gets the state of this AimPersonalTemplateFactory.

        支持状态。 - 1：支持 - 0：不支持 

        :return: The state of this AimPersonalTemplateFactory.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AimPersonalTemplateFactory.

        支持状态。 - 1：支持 - 0：不支持 

        :param state: The state of this AimPersonalTemplateFactory.
        :type state: int
        """
        self._state = state

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
        if not isinstance(other, AimPersonalTemplateFactory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
