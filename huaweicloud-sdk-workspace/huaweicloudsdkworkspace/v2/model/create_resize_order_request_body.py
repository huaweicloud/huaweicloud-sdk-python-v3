# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResizeOrderRequestBody:

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
        'product_id': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'desktop_pool_id': 'desktop_pool_id',
        'desktop_ids': 'desktop_ids',
        'promotion_plan_id': 'promotion_plan_id',
        'product_id': 'product_id',
        'mode': 'mode'
    }

    def __init__(self, desktop_pool_id=None, desktop_ids=None, promotion_plan_id=None, product_id=None, mode=None):
        r"""CreateResizeOrderRequestBody

        The model defined in huaweicloud sdk

        :param desktop_pool_id: 桌面池ID。当desktop_pool_id与desktop_ids同时存在时，取desktop_ids的值，两者不可同时为空。
        :type desktop_pool_id: str
        :param desktop_ids: 包周期桌面ID列表。 不可同时存在普通桌面和池桌面ID。
        :type desktop_ids: list[str]
        :param promotion_plan_id: 促销计划ID。
        :type promotion_plan_id: str
        :param product_id: 目标规格产品ID。
        :type product_id: str
        :param mode: 是否支持开机状态下执行变更规格操作。固定传值STOP_DESKTOP，如果桌面处于开机状态，会先关机再变更规格。
        :type mode: str
        """
        
        

        self._desktop_pool_id = None
        self._desktop_ids = None
        self._promotion_plan_id = None
        self._product_id = None
        self._mode = None
        self.discriminator = None

        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if desktop_ids is not None:
            self.desktop_ids = desktop_ids
        if promotion_plan_id is not None:
            self.promotion_plan_id = promotion_plan_id
        if product_id is not None:
            self.product_id = product_id
        if mode is not None:
            self.mode = mode

    @property
    def desktop_pool_id(self):
        r"""Gets the desktop_pool_id of this CreateResizeOrderRequestBody.

        桌面池ID。当desktop_pool_id与desktop_ids同时存在时，取desktop_ids的值，两者不可同时为空。

        :return: The desktop_pool_id of this CreateResizeOrderRequestBody.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        r"""Sets the desktop_pool_id of this CreateResizeOrderRequestBody.

        桌面池ID。当desktop_pool_id与desktop_ids同时存在时，取desktop_ids的值，两者不可同时为空。

        :param desktop_pool_id: The desktop_pool_id of this CreateResizeOrderRequestBody.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this CreateResizeOrderRequestBody.

        包周期桌面ID列表。 不可同时存在普通桌面和池桌面ID。

        :return: The desktop_ids of this CreateResizeOrderRequestBody.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this CreateResizeOrderRequestBody.

        包周期桌面ID列表。 不可同时存在普通桌面和池桌面ID。

        :param desktop_ids: The desktop_ids of this CreateResizeOrderRequestBody.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def promotion_plan_id(self):
        r"""Gets the promotion_plan_id of this CreateResizeOrderRequestBody.

        促销计划ID。

        :return: The promotion_plan_id of this CreateResizeOrderRequestBody.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        r"""Sets the promotion_plan_id of this CreateResizeOrderRequestBody.

        促销计划ID。

        :param promotion_plan_id: The promotion_plan_id of this CreateResizeOrderRequestBody.
        :type promotion_plan_id: str
        """
        self._promotion_plan_id = promotion_plan_id

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateResizeOrderRequestBody.

        目标规格产品ID。

        :return: The product_id of this CreateResizeOrderRequestBody.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateResizeOrderRequestBody.

        目标规格产品ID。

        :param product_id: The product_id of this CreateResizeOrderRequestBody.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def mode(self):
        r"""Gets the mode of this CreateResizeOrderRequestBody.

        是否支持开机状态下执行变更规格操作。固定传值STOP_DESKTOP，如果桌面处于开机状态，会先关机再变更规格。

        :return: The mode of this CreateResizeOrderRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateResizeOrderRequestBody.

        是否支持开机状态下执行变更规格操作。固定传值STOP_DESKTOP，如果桌面处于开机状态，会先关机再变更规格。

        :param mode: The mode of this CreateResizeOrderRequestBody.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, CreateResizeOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
