# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RebuildDesktopPoolReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_type': 'str',
        'image_id': 'str',
        'os_type': 'str',
        'delay_time': 'int',
        'message': 'str',
        'order_id': 'str',
        'is_fix': 'bool'
    }

    attribute_map = {
        'image_type': 'image_type',
        'image_id': 'image_id',
        'os_type': 'os_type',
        'delay_time': 'delay_time',
        'message': 'message',
        'order_id': 'order_id',
        'is_fix': 'is_fix'
    }

    def __init__(self, image_type=None, image_id=None, os_type=None, delay_time=None, message=None, order_id=None, is_fix=None):
        r"""RebuildDesktopPoolReq

        The model defined in huaweicloud sdk

        :param image_type: 镜像类型。
        :type image_type: str
        :param image_id: 模板ID。
        :type image_id: str
        :param os_type: os类型。
        :type os_type: str
        :param delay_time: 立即重建时给用户预留的保存数据的时间（单位：分钟）。
        :type delay_time: int
        :param message: 下发重建系统盘任务时，给用户发送的提示信息。
        :type message: str
        :param order_id: 订单ID，包周期桌面重建系统盘，涉及收费镜像时需传。
        :type order_id: str
        :param is_fix: 是否是修复行为，修复行为只修复镜像ID与桌面池镜像ID不一致的桌面，用于桌面池切换镜像失败场景的修复。
        :type is_fix: bool
        """
        
        

        self._image_type = None
        self._image_id = None
        self._os_type = None
        self._delay_time = None
        self._message = None
        self._order_id = None
        self._is_fix = None
        self.discriminator = None

        if image_type is not None:
            self.image_type = image_type
        self.image_id = image_id
        if os_type is not None:
            self.os_type = os_type
        if delay_time is not None:
            self.delay_time = delay_time
        if message is not None:
            self.message = message
        if order_id is not None:
            self.order_id = order_id
        if is_fix is not None:
            self.is_fix = is_fix

    @property
    def image_type(self):
        r"""Gets the image_type of this RebuildDesktopPoolReq.

        镜像类型。

        :return: The image_type of this RebuildDesktopPoolReq.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this RebuildDesktopPoolReq.

        镜像类型。

        :param image_type: The image_type of this RebuildDesktopPoolReq.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_id(self):
        r"""Gets the image_id of this RebuildDesktopPoolReq.

        模板ID。

        :return: The image_id of this RebuildDesktopPoolReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this RebuildDesktopPoolReq.

        模板ID。

        :param image_id: The image_id of this RebuildDesktopPoolReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def os_type(self):
        r"""Gets the os_type of this RebuildDesktopPoolReq.

        os类型。

        :return: The os_type of this RebuildDesktopPoolReq.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this RebuildDesktopPoolReq.

        os类型。

        :param os_type: The os_type of this RebuildDesktopPoolReq.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def delay_time(self):
        r"""Gets the delay_time of this RebuildDesktopPoolReq.

        立即重建时给用户预留的保存数据的时间（单位：分钟）。

        :return: The delay_time of this RebuildDesktopPoolReq.
        :rtype: int
        """
        return self._delay_time

    @delay_time.setter
    def delay_time(self, delay_time):
        r"""Sets the delay_time of this RebuildDesktopPoolReq.

        立即重建时给用户预留的保存数据的时间（单位：分钟）。

        :param delay_time: The delay_time of this RebuildDesktopPoolReq.
        :type delay_time: int
        """
        self._delay_time = delay_time

    @property
    def message(self):
        r"""Gets the message of this RebuildDesktopPoolReq.

        下发重建系统盘任务时，给用户发送的提示信息。

        :return: The message of this RebuildDesktopPoolReq.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this RebuildDesktopPoolReq.

        下发重建系统盘任务时，给用户发送的提示信息。

        :param message: The message of this RebuildDesktopPoolReq.
        :type message: str
        """
        self._message = message

    @property
    def order_id(self):
        r"""Gets the order_id of this RebuildDesktopPoolReq.

        订单ID，包周期桌面重建系统盘，涉及收费镜像时需传。

        :return: The order_id of this RebuildDesktopPoolReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this RebuildDesktopPoolReq.

        订单ID，包周期桌面重建系统盘，涉及收费镜像时需传。

        :param order_id: The order_id of this RebuildDesktopPoolReq.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def is_fix(self):
        r"""Gets the is_fix of this RebuildDesktopPoolReq.

        是否是修复行为，修复行为只修复镜像ID与桌面池镜像ID不一致的桌面，用于桌面池切换镜像失败场景的修复。

        :return: The is_fix of this RebuildDesktopPoolReq.
        :rtype: bool
        """
        return self._is_fix

    @is_fix.setter
    def is_fix(self, is_fix):
        r"""Sets the is_fix of this RebuildDesktopPoolReq.

        是否是修复行为，修复行为只修复镜像ID与桌面池镜像ID不一致的桌面，用于桌面池切换镜像失败场景的修复。

        :param is_fix: The is_fix of this RebuildDesktopPoolReq.
        :type is_fix: bool
        """
        self._is_fix = is_fix

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
        if not isinstance(other, RebuildDesktopPoolReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
