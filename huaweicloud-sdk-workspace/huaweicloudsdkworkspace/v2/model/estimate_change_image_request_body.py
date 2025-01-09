# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EstimateChangeImageRequestBody:

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
        'image_id': 'str'
    }

    attribute_map = {
        'desktop_pool_id': 'desktop_pool_id',
        'desktop_ids': 'desktop_ids',
        'promotion_plan_id': 'promotion_plan_id',
        'image_spec_code': 'image_spec_code',
        'image_id': 'image_id'
    }

    def __init__(self, desktop_pool_id=None, desktop_ids=None, promotion_plan_id=None, image_spec_code=None, image_id=None):
        """EstimateChangeImageRequestBody

        The model defined in huaweicloud sdk

        :param desktop_pool_id: 桌面池ID。当desktop_pool_id与desktop_ids同时存在时，取desktop_ids的值，两者不可同时为空。
        :type desktop_pool_id: str
        :param desktop_ids: 包周期桌面ID列表。 不可同时存在普通桌面和池桌面ID。
        :type desktop_ids: list[str]
        :param promotion_plan_id: 促销计划ID
        :type promotion_plan_id: str
        :param image_spec_code: 云市场镜像的specCode，即将停用。image_spec_code与image_id同时存在时取image_id的值，两者不可同时为空。
        :type image_spec_code: str
        :param image_id: 云市场镜像ID，建议使用image_id。
        :type image_id: str
        """
        
        

        self._desktop_pool_id = None
        self._desktop_ids = None
        self._promotion_plan_id = None
        self._image_spec_code = None
        self._image_id = None
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

    @property
    def desktop_pool_id(self):
        """Gets the desktop_pool_id of this EstimateChangeImageRequestBody.

        桌面池ID。当desktop_pool_id与desktop_ids同时存在时，取desktop_ids的值，两者不可同时为空。

        :return: The desktop_pool_id of this EstimateChangeImageRequestBody.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        """Sets the desktop_pool_id of this EstimateChangeImageRequestBody.

        桌面池ID。当desktop_pool_id与desktop_ids同时存在时，取desktop_ids的值，两者不可同时为空。

        :param desktop_pool_id: The desktop_pool_id of this EstimateChangeImageRequestBody.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def desktop_ids(self):
        """Gets the desktop_ids of this EstimateChangeImageRequestBody.

        包周期桌面ID列表。 不可同时存在普通桌面和池桌面ID。

        :return: The desktop_ids of this EstimateChangeImageRequestBody.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        """Sets the desktop_ids of this EstimateChangeImageRequestBody.

        包周期桌面ID列表。 不可同时存在普通桌面和池桌面ID。

        :param desktop_ids: The desktop_ids of this EstimateChangeImageRequestBody.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def promotion_plan_id(self):
        """Gets the promotion_plan_id of this EstimateChangeImageRequestBody.

        促销计划ID

        :return: The promotion_plan_id of this EstimateChangeImageRequestBody.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        """Sets the promotion_plan_id of this EstimateChangeImageRequestBody.

        促销计划ID

        :param promotion_plan_id: The promotion_plan_id of this EstimateChangeImageRequestBody.
        :type promotion_plan_id: str
        """
        self._promotion_plan_id = promotion_plan_id

    @property
    def image_spec_code(self):
        """Gets the image_spec_code of this EstimateChangeImageRequestBody.

        云市场镜像的specCode，即将停用。image_spec_code与image_id同时存在时取image_id的值，两者不可同时为空。

        :return: The image_spec_code of this EstimateChangeImageRequestBody.
        :rtype: str
        """
        return self._image_spec_code

    @image_spec_code.setter
    def image_spec_code(self, image_spec_code):
        """Sets the image_spec_code of this EstimateChangeImageRequestBody.

        云市场镜像的specCode，即将停用。image_spec_code与image_id同时存在时取image_id的值，两者不可同时为空。

        :param image_spec_code: The image_spec_code of this EstimateChangeImageRequestBody.
        :type image_spec_code: str
        """
        self._image_spec_code = image_spec_code

    @property
    def image_id(self):
        """Gets the image_id of this EstimateChangeImageRequestBody.

        云市场镜像ID，建议使用image_id。

        :return: The image_id of this EstimateChangeImageRequestBody.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this EstimateChangeImageRequestBody.

        云市场镜像ID，建议使用image_id。

        :param image_id: The image_id of this EstimateChangeImageRequestBody.
        :type image_id: str
        """
        self._image_id = image_id

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
        if not isinstance(other, EstimateChangeImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
