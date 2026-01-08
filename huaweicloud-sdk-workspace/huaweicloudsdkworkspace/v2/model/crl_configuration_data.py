# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CrlConfigurationData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'type': 'str',
        'crl_url': 'str',
        'valid_day': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'type': 'type',
        'crl_url': 'crl_url',
        'valid_day': 'valid_day'
    }

    def __init__(self, enable=None, type=None, crl_url=None, valid_day=None):
        r"""CrlConfigurationData

        The model defined in huaweicloud sdk

        :param enable: 是否开启crl配置。
        :type enable: bool
        :param type: 系统生成SYSTEM, 用户自定义CUSTOMIZE。
        :type type: str
        :param crl_url: 当用户自定义时手动输入。
        :type crl_url: str
        :param valid_day: 更新周期。
        :type valid_day: int
        """
        
        

        self._enable = None
        self._type = None
        self._crl_url = None
        self._valid_day = None
        self.discriminator = None

        self.enable = enable
        self.type = type
        if crl_url is not None:
            self.crl_url = crl_url
        self.valid_day = valid_day

    @property
    def enable(self):
        r"""Gets the enable of this CrlConfigurationData.

        是否开启crl配置。

        :return: The enable of this CrlConfigurationData.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this CrlConfigurationData.

        是否开启crl配置。

        :param enable: The enable of this CrlConfigurationData.
        :type enable: bool
        """
        self._enable = enable

    @property
    def type(self):
        r"""Gets the type of this CrlConfigurationData.

        系统生成SYSTEM, 用户自定义CUSTOMIZE。

        :return: The type of this CrlConfigurationData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CrlConfigurationData.

        系统生成SYSTEM, 用户自定义CUSTOMIZE。

        :param type: The type of this CrlConfigurationData.
        :type type: str
        """
        self._type = type

    @property
    def crl_url(self):
        r"""Gets the crl_url of this CrlConfigurationData.

        当用户自定义时手动输入。

        :return: The crl_url of this CrlConfigurationData.
        :rtype: str
        """
        return self._crl_url

    @crl_url.setter
    def crl_url(self, crl_url):
        r"""Sets the crl_url of this CrlConfigurationData.

        当用户自定义时手动输入。

        :param crl_url: The crl_url of this CrlConfigurationData.
        :type crl_url: str
        """
        self._crl_url = crl_url

    @property
    def valid_day(self):
        r"""Gets the valid_day of this CrlConfigurationData.

        更新周期。

        :return: The valid_day of this CrlConfigurationData.
        :rtype: int
        """
        return self._valid_day

    @valid_day.setter
    def valid_day(self, valid_day):
        r"""Sets the valid_day of this CrlConfigurationData.

        更新周期。

        :param valid_day: The valid_day of this CrlConfigurationData.
        :type valid_day: int
        """
        self._valid_day = valid_day

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
        if not isinstance(other, CrlConfigurationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
