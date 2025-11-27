# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpecialConfigurationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'page_size': 'int',
        'page_number': 'int'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'page_size': 'page_size',
        'page_number': 'page_number'
    }

    def __init__(self, domain_name=None, page_size=None, page_number=None):
        r"""ListSpecialConfigurationRequest

        The model defined in huaweicloud sdk

        :param domain_name: **参数解释：** 加速域名  **约束限制：** 仅支持查询已经在CDN添加成功的域名 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type domain_name: str
        :param page_size: **参数解释：** 每页加速域名的数量 **约束限制：** 不涉及 **取值范围：** 1-10000 **默认取值：** 30
        :type page_size: int
        :param page_number: **参数解释：** 查询的页码 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 1
        :type page_number: int
        """
        
        

        self._domain_name = None
        self._page_size = None
        self._page_number = None
        self.discriminator = None

        self.domain_name = domain_name
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListSpecialConfigurationRequest.

        **参数解释：** 加速域名  **约束限制：** 仅支持查询已经在CDN添加成功的域名 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The domain_name of this ListSpecialConfigurationRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListSpecialConfigurationRequest.

        **参数解释：** 加速域名  **约束限制：** 仅支持查询已经在CDN添加成功的域名 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param domain_name: The domain_name of this ListSpecialConfigurationRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def page_size(self):
        r"""Gets the page_size of this ListSpecialConfigurationRequest.

        **参数解释：** 每页加速域名的数量 **约束限制：** 不涉及 **取值范围：** 1-10000 **默认取值：** 30

        :return: The page_size of this ListSpecialConfigurationRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListSpecialConfigurationRequest.

        **参数解释：** 每页加速域名的数量 **约束限制：** 不涉及 **取值范围：** 1-10000 **默认取值：** 30

        :param page_size: The page_size of this ListSpecialConfigurationRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        r"""Gets the page_number of this ListSpecialConfigurationRequest.

        **参数解释：** 查询的页码 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 1

        :return: The page_number of this ListSpecialConfigurationRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this ListSpecialConfigurationRequest.

        **参数解释：** 查询的页码 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 1

        :param page_number: The page_number of this ListSpecialConfigurationRequest.
        :type page_number: int
        """
        self._page_number = page_number

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
        if not isinstance(other, ListSpecialConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
