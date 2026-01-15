# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RebuildDesktopsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_ids': 'list[str]',
        'image_type': 'str',
        'image_id': 'str',
        'encrypt_type': 'EncryptType',
        'kms_id': 'str',
        'os_type': 'str',
        'delay_time': 'int',
        'message': 'str',
        'order_id': 'str',
        'enterprise_project_id': 'str',
        'handle_type': 'str'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'image_type': 'image_type',
        'image_id': 'image_id',
        'encrypt_type': 'encrypt_type',
        'kms_id': 'kms_id',
        'os_type': 'os_type',
        'delay_time': 'delay_time',
        'message': 'message',
        'order_id': 'order_id',
        'enterprise_project_id': 'enterprise_project_id',
        'handle_type': 'handle_type'
    }

    def __init__(self, desktop_ids=None, image_type=None, image_id=None, encrypt_type=None, kms_id=None, os_type=None, delay_time=None, message=None, order_id=None, enterprise_project_id=None, handle_type=None):
        r"""RebuildDesktopsReq

        The model defined in huaweicloud sdk

        :param desktop_ids: 计算机id列表。
        :type desktop_ids: list[str]
        :param image_type: 镜像类型 - 公共镜像：gold - 私有镜像：private - 市场镜像：market
        :type image_type: str
        :param image_id: 模板ID。
        :type image_id: str
        :param encrypt_type: 
        :type encrypt_type: :class:`huaweicloudsdkworkspace.v2.EncryptType`
        :param kms_id: 密钥ID，encrypt_type为ENCRYPTED时必传。
        :type kms_id: str
        :param os_type: os类型。
        :type os_type: str
        :param delay_time: 立即重建时给用户预留的保存数据的时间（单位：分钟）。
        :type delay_time: int
        :param message: 下发重建系统盘任务时，给用户发送的提示信息。
        :type message: str
        :param order_id: 订单ID，包周期桌面重建系统盘，涉及收费镜像时需传。
        :type order_id: str
        :param enterprise_project_id: 企业项目ID，默认\&quot;0。\&quot;
        :type enterprise_project_id: str
        :param handle_type: 处理类型 - ONLY_FOR_EXPAND：仅对新扩容桌面生效 - FOR_EXPAND_AND_IDLE：对新扩容桌面与空闲桌面生效 - FOR_EXPAND_AND_ALL：对新扩容桌面与已有全部桌面生效
        :type handle_type: str
        """
        
        

        self._desktop_ids = None
        self._image_type = None
        self._image_id = None
        self._encrypt_type = None
        self._kms_id = None
        self._os_type = None
        self._delay_time = None
        self._message = None
        self._order_id = None
        self._enterprise_project_id = None
        self._handle_type = None
        self.discriminator = None

        self.desktop_ids = desktop_ids
        self.image_type = image_type
        self.image_id = image_id
        if encrypt_type is not None:
            self.encrypt_type = encrypt_type
        if kms_id is not None:
            self.kms_id = kms_id
        if os_type is not None:
            self.os_type = os_type
        if delay_time is not None:
            self.delay_time = delay_time
        if message is not None:
            self.message = message
        if order_id is not None:
            self.order_id = order_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if handle_type is not None:
            self.handle_type = handle_type

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this RebuildDesktopsReq.

        计算机id列表。

        :return: The desktop_ids of this RebuildDesktopsReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this RebuildDesktopsReq.

        计算机id列表。

        :param desktop_ids: The desktop_ids of this RebuildDesktopsReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def image_type(self):
        r"""Gets the image_type of this RebuildDesktopsReq.

        镜像类型 - 公共镜像：gold - 私有镜像：private - 市场镜像：market

        :return: The image_type of this RebuildDesktopsReq.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this RebuildDesktopsReq.

        镜像类型 - 公共镜像：gold - 私有镜像：private - 市场镜像：market

        :param image_type: The image_type of this RebuildDesktopsReq.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_id(self):
        r"""Gets the image_id of this RebuildDesktopsReq.

        模板ID。

        :return: The image_id of this RebuildDesktopsReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this RebuildDesktopsReq.

        模板ID。

        :param image_id: The image_id of this RebuildDesktopsReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def encrypt_type(self):
        r"""Gets the encrypt_type of this RebuildDesktopsReq.

        :return: The encrypt_type of this RebuildDesktopsReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.EncryptType`
        """
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, encrypt_type):
        r"""Sets the encrypt_type of this RebuildDesktopsReq.

        :param encrypt_type: The encrypt_type of this RebuildDesktopsReq.
        :type encrypt_type: :class:`huaweicloudsdkworkspace.v2.EncryptType`
        """
        self._encrypt_type = encrypt_type

    @property
    def kms_id(self):
        r"""Gets the kms_id of this RebuildDesktopsReq.

        密钥ID，encrypt_type为ENCRYPTED时必传。

        :return: The kms_id of this RebuildDesktopsReq.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        r"""Sets the kms_id of this RebuildDesktopsReq.

        密钥ID，encrypt_type为ENCRYPTED时必传。

        :param kms_id: The kms_id of this RebuildDesktopsReq.
        :type kms_id: str
        """
        self._kms_id = kms_id

    @property
    def os_type(self):
        r"""Gets the os_type of this RebuildDesktopsReq.

        os类型。

        :return: The os_type of this RebuildDesktopsReq.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this RebuildDesktopsReq.

        os类型。

        :param os_type: The os_type of this RebuildDesktopsReq.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def delay_time(self):
        r"""Gets the delay_time of this RebuildDesktopsReq.

        立即重建时给用户预留的保存数据的时间（单位：分钟）。

        :return: The delay_time of this RebuildDesktopsReq.
        :rtype: int
        """
        return self._delay_time

    @delay_time.setter
    def delay_time(self, delay_time):
        r"""Sets the delay_time of this RebuildDesktopsReq.

        立即重建时给用户预留的保存数据的时间（单位：分钟）。

        :param delay_time: The delay_time of this RebuildDesktopsReq.
        :type delay_time: int
        """
        self._delay_time = delay_time

    @property
    def message(self):
        r"""Gets the message of this RebuildDesktopsReq.

        下发重建系统盘任务时，给用户发送的提示信息。

        :return: The message of this RebuildDesktopsReq.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this RebuildDesktopsReq.

        下发重建系统盘任务时，给用户发送的提示信息。

        :param message: The message of this RebuildDesktopsReq.
        :type message: str
        """
        self._message = message

    @property
    def order_id(self):
        r"""Gets the order_id of this RebuildDesktopsReq.

        订单ID，包周期桌面重建系统盘，涉及收费镜像时需传。

        :return: The order_id of this RebuildDesktopsReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this RebuildDesktopsReq.

        订单ID，包周期桌面重建系统盘，涉及收费镜像时需传。

        :param order_id: The order_id of this RebuildDesktopsReq.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this RebuildDesktopsReq.

        企业项目ID，默认\"0。\"

        :return: The enterprise_project_id of this RebuildDesktopsReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this RebuildDesktopsReq.

        企业项目ID，默认\"0。\"

        :param enterprise_project_id: The enterprise_project_id of this RebuildDesktopsReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def handle_type(self):
        r"""Gets the handle_type of this RebuildDesktopsReq.

        处理类型 - ONLY_FOR_EXPAND：仅对新扩容桌面生效 - FOR_EXPAND_AND_IDLE：对新扩容桌面与空闲桌面生效 - FOR_EXPAND_AND_ALL：对新扩容桌面与已有全部桌面生效

        :return: The handle_type of this RebuildDesktopsReq.
        :rtype: str
        """
        return self._handle_type

    @handle_type.setter
    def handle_type(self, handle_type):
        r"""Sets the handle_type of this RebuildDesktopsReq.

        处理类型 - ONLY_FOR_EXPAND：仅对新扩容桌面生效 - FOR_EXPAND_AND_IDLE：对新扩容桌面与空闲桌面生效 - FOR_EXPAND_AND_ALL：对新扩容桌面与已有全部桌面生效

        :param handle_type: The handle_type of this RebuildDesktopsReq.
        :type handle_type: str
        """
        self._handle_type = handle_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RebuildDesktopsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
