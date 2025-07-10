# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateChangeImageOrderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_pool_id': 'str',
        'desktop_ids': 'list[str]',
        'promotion_plan_id': 'str',
        'image_spec_code': 'str',
        'image_id': 'str',
        'delay_time': 'int',
        'message': 'str'
    }

    attribute_map = {
        'desktop_pool_id': 'desktop_pool_id',
        'desktop_ids': 'desktop_ids',
        'promotion_plan_id': 'promotion_plan_id',
        'image_spec_code': 'image_spec_code',
        'image_id': 'image_id',
        'delay_time': 'delay_time',
        'message': 'message'
    }

    def __init__(self, desktop_pool_id=None, desktop_ids=None, promotion_plan_id=None, image_spec_code=None, image_id=None, delay_time=None, message=None):
        r"""CreateChangeImageOrderRequestBody

        The model defined in huaweicloud sdk

        :param desktop_pool_id: 桌面池ID。当desktop_pool_id与desktop_ids同时存在时，取desktop_ids的值，两者不可同时为空。
        :type desktop_pool_id: str
        :param desktop_ids: 包周期桌面ID列表。 不可同时存在普通桌面和池桌面ID。
        :type desktop_ids: list[str]
        :param promotion_plan_id: 促销计划ID。
        :type promotion_plan_id: str
        :param image_spec_code: 云市场镜像的specCode，即将停用。image_spec_code与image_id同时存在时取image_id的值，两者不可同时为空。
        :type image_spec_code: str
        :param image_id: 云市场镜像ID，建议使用image_id。
        :type image_id: str
        :param delay_time: 立即重建时给用户预留的保存数据的时间（单位：分钟）。
        :type delay_time: int
        :param message: 下发重建系统盘任务时，给用户发送的提示信息。
        :type message: str
        """
        
        

        self._desktop_pool_id = None
        self._desktop_ids = None
        self._promotion_plan_id = None
        self._image_spec_code = None
        self._image_id = None
        self._delay_time = None
        self._message = None
        self.discriminator = None

        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if desktop_ids is not None:
            self.desktop_ids = desktop_ids
        if promotion_plan_id is not None:
            self.promotion_plan_id = promotion_plan_id
        if image_spec_code is not None:
            self.image_spec_code = image_spec_code
        if image_id is not None:
            self.image_id = image_id
        if delay_time is not None:
            self.delay_time = delay_time
        if message is not None:
            self.message = message

    @property
    def desktop_pool_id(self):
        r"""Gets the desktop_pool_id of this CreateChangeImageOrderRequestBody.

        桌面池ID。当desktop_pool_id与desktop_ids同时存在时，取desktop_ids的值，两者不可同时为空。

        :return: The desktop_pool_id of this CreateChangeImageOrderRequestBody.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        r"""Sets the desktop_pool_id of this CreateChangeImageOrderRequestBody.

        桌面池ID。当desktop_pool_id与desktop_ids同时存在时，取desktop_ids的值，两者不可同时为空。

        :param desktop_pool_id: The desktop_pool_id of this CreateChangeImageOrderRequestBody.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this CreateChangeImageOrderRequestBody.

        包周期桌面ID列表。 不可同时存在普通桌面和池桌面ID。

        :return: The desktop_ids of this CreateChangeImageOrderRequestBody.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this CreateChangeImageOrderRequestBody.

        包周期桌面ID列表。 不可同时存在普通桌面和池桌面ID。

        :param desktop_ids: The desktop_ids of this CreateChangeImageOrderRequestBody.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def promotion_plan_id(self):
        r"""Gets the promotion_plan_id of this CreateChangeImageOrderRequestBody.

        促销计划ID。

        :return: The promotion_plan_id of this CreateChangeImageOrderRequestBody.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        r"""Sets the promotion_plan_id of this CreateChangeImageOrderRequestBody.

        促销计划ID。

        :param promotion_plan_id: The promotion_plan_id of this CreateChangeImageOrderRequestBody.
        :type promotion_plan_id: str
        """
        self._promotion_plan_id = promotion_plan_id

    @property
    def image_spec_code(self):
        r"""Gets the image_spec_code of this CreateChangeImageOrderRequestBody.

        云市场镜像的specCode，即将停用。image_spec_code与image_id同时存在时取image_id的值，两者不可同时为空。

        :return: The image_spec_code of this CreateChangeImageOrderRequestBody.
        :rtype: str
        """
        return self._image_spec_code

    @image_spec_code.setter
    def image_spec_code(self, image_spec_code):
        r"""Sets the image_spec_code of this CreateChangeImageOrderRequestBody.

        云市场镜像的specCode，即将停用。image_spec_code与image_id同时存在时取image_id的值，两者不可同时为空。

        :param image_spec_code: The image_spec_code of this CreateChangeImageOrderRequestBody.
        :type image_spec_code: str
        """
        self._image_spec_code = image_spec_code

    @property
    def image_id(self):
        r"""Gets the image_id of this CreateChangeImageOrderRequestBody.

        云市场镜像ID，建议使用image_id。

        :return: The image_id of this CreateChangeImageOrderRequestBody.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this CreateChangeImageOrderRequestBody.

        云市场镜像ID，建议使用image_id。

        :param image_id: The image_id of this CreateChangeImageOrderRequestBody.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def delay_time(self):
        r"""Gets the delay_time of this CreateChangeImageOrderRequestBody.

        立即重建时给用户预留的保存数据的时间（单位：分钟）。

        :return: The delay_time of this CreateChangeImageOrderRequestBody.
        :rtype: int
        """
        return self._delay_time

    @delay_time.setter
    def delay_time(self, delay_time):
        r"""Sets the delay_time of this CreateChangeImageOrderRequestBody.

        立即重建时给用户预留的保存数据的时间（单位：分钟）。

        :param delay_time: The delay_time of this CreateChangeImageOrderRequestBody.
        :type delay_time: int
        """
        self._delay_time = delay_time

    @property
    def message(self):
        r"""Gets the message of this CreateChangeImageOrderRequestBody.

        下发重建系统盘任务时，给用户发送的提示信息。

        :return: The message of this CreateChangeImageOrderRequestBody.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateChangeImageOrderRequestBody.

        下发重建系统盘任务时，给用户发送的提示信息。

        :param message: The message of this CreateChangeImageOrderRequestBody.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, CreateChangeImageOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
