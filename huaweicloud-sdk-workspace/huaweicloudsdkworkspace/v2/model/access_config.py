# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_mode': 'str',
        'internet_access_address': 'str',
        'internet_access_port': 'str',
        'dedicated_access_address': 'str',
        'dedicated_access_standby_address': 'list[str]',
        'standby_address_result_code': 'str',
        'dedicated_cidrs': 'str'
    }

    attribute_map = {
        'access_mode': 'access_mode',
        'internet_access_address': 'internet_access_address',
        'internet_access_port': 'internet_access_port',
        'dedicated_access_address': 'dedicated_access_address',
        'dedicated_access_standby_address': 'dedicated_access_standby_address',
        'standby_address_result_code': 'standby_address_result_code',
        'dedicated_cidrs': 'dedicated_cidrs'
    }

    def __init__(self, access_mode=None, internet_access_address=None, internet_access_port=None, dedicated_access_address=None, dedicated_access_standby_address=None, standby_address_result_code=None, dedicated_cidrs=None):
        r"""AccessConfig

        The model defined in huaweicloud sdk

        :param access_mode: 接入方式。 - INTERNET：表示互联网接入 - DEDICATED：表示专线接入 - BOTH：表示同时支持互联网接入和专线接入
        :type access_mode: str
        :param internet_access_address: 互联网接入地址，只有access_mode为“INTERNET”或“BOTH”时才会返回该参数。
        :type internet_access_address: str
        :param internet_access_port: 互联网接入端口。
        :type internet_access_port: str
        :param dedicated_access_address: 专线接入地址，只有access_mode为“DEDICATED”或“BOTH”时才会返回该参数。
        :type dedicated_access_address: str
        :param dedicated_access_standby_address: 专线接入备用地址，只有当开启专线备用线路时才会返回该参数。
        :type dedicated_access_standby_address: list[str]
        :param standby_address_result_code: 专线备用线路失败错误码。
        :type standby_address_result_code: str
        :param dedicated_cidrs: 专线接入网段。接入模式包含专线方式时选填，多个网段信息用分号隔开，列表长度不超过5。
        :type dedicated_cidrs: str
        """
        
        

        self._access_mode = None
        self._internet_access_address = None
        self._internet_access_port = None
        self._dedicated_access_address = None
        self._dedicated_access_standby_address = None
        self._standby_address_result_code = None
        self._dedicated_cidrs = None
        self.discriminator = None

        if access_mode is not None:
            self.access_mode = access_mode
        if internet_access_address is not None:
            self.internet_access_address = internet_access_address
        if internet_access_port is not None:
            self.internet_access_port = internet_access_port
        if dedicated_access_address is not None:
            self.dedicated_access_address = dedicated_access_address
        if dedicated_access_standby_address is not None:
            self.dedicated_access_standby_address = dedicated_access_standby_address
        if standby_address_result_code is not None:
            self.standby_address_result_code = standby_address_result_code
        if dedicated_cidrs is not None:
            self.dedicated_cidrs = dedicated_cidrs

    @property
    def access_mode(self):
        r"""Gets the access_mode of this AccessConfig.

        接入方式。 - INTERNET：表示互联网接入 - DEDICATED：表示专线接入 - BOTH：表示同时支持互联网接入和专线接入

        :return: The access_mode of this AccessConfig.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        r"""Sets the access_mode of this AccessConfig.

        接入方式。 - INTERNET：表示互联网接入 - DEDICATED：表示专线接入 - BOTH：表示同时支持互联网接入和专线接入

        :param access_mode: The access_mode of this AccessConfig.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def internet_access_address(self):
        r"""Gets the internet_access_address of this AccessConfig.

        互联网接入地址，只有access_mode为“INTERNET”或“BOTH”时才会返回该参数。

        :return: The internet_access_address of this AccessConfig.
        :rtype: str
        """
        return self._internet_access_address

    @internet_access_address.setter
    def internet_access_address(self, internet_access_address):
        r"""Sets the internet_access_address of this AccessConfig.

        互联网接入地址，只有access_mode为“INTERNET”或“BOTH”时才会返回该参数。

        :param internet_access_address: The internet_access_address of this AccessConfig.
        :type internet_access_address: str
        """
        self._internet_access_address = internet_access_address

    @property
    def internet_access_port(self):
        r"""Gets the internet_access_port of this AccessConfig.

        互联网接入端口。

        :return: The internet_access_port of this AccessConfig.
        :rtype: str
        """
        return self._internet_access_port

    @internet_access_port.setter
    def internet_access_port(self, internet_access_port):
        r"""Sets the internet_access_port of this AccessConfig.

        互联网接入端口。

        :param internet_access_port: The internet_access_port of this AccessConfig.
        :type internet_access_port: str
        """
        self._internet_access_port = internet_access_port

    @property
    def dedicated_access_address(self):
        r"""Gets the dedicated_access_address of this AccessConfig.

        专线接入地址，只有access_mode为“DEDICATED”或“BOTH”时才会返回该参数。

        :return: The dedicated_access_address of this AccessConfig.
        :rtype: str
        """
        return self._dedicated_access_address

    @dedicated_access_address.setter
    def dedicated_access_address(self, dedicated_access_address):
        r"""Sets the dedicated_access_address of this AccessConfig.

        专线接入地址，只有access_mode为“DEDICATED”或“BOTH”时才会返回该参数。

        :param dedicated_access_address: The dedicated_access_address of this AccessConfig.
        :type dedicated_access_address: str
        """
        self._dedicated_access_address = dedicated_access_address

    @property
    def dedicated_access_standby_address(self):
        r"""Gets the dedicated_access_standby_address of this AccessConfig.

        专线接入备用地址，只有当开启专线备用线路时才会返回该参数。

        :return: The dedicated_access_standby_address of this AccessConfig.
        :rtype: list[str]
        """
        return self._dedicated_access_standby_address

    @dedicated_access_standby_address.setter
    def dedicated_access_standby_address(self, dedicated_access_standby_address):
        r"""Sets the dedicated_access_standby_address of this AccessConfig.

        专线接入备用地址，只有当开启专线备用线路时才会返回该参数。

        :param dedicated_access_standby_address: The dedicated_access_standby_address of this AccessConfig.
        :type dedicated_access_standby_address: list[str]
        """
        self._dedicated_access_standby_address = dedicated_access_standby_address

    @property
    def standby_address_result_code(self):
        r"""Gets the standby_address_result_code of this AccessConfig.

        专线备用线路失败错误码。

        :return: The standby_address_result_code of this AccessConfig.
        :rtype: str
        """
        return self._standby_address_result_code

    @standby_address_result_code.setter
    def standby_address_result_code(self, standby_address_result_code):
        r"""Sets the standby_address_result_code of this AccessConfig.

        专线备用线路失败错误码。

        :param standby_address_result_code: The standby_address_result_code of this AccessConfig.
        :type standby_address_result_code: str
        """
        self._standby_address_result_code = standby_address_result_code

    @property
    def dedicated_cidrs(self):
        r"""Gets the dedicated_cidrs of this AccessConfig.

        专线接入网段。接入模式包含专线方式时选填，多个网段信息用分号隔开，列表长度不超过5。

        :return: The dedicated_cidrs of this AccessConfig.
        :rtype: str
        """
        return self._dedicated_cidrs

    @dedicated_cidrs.setter
    def dedicated_cidrs(self, dedicated_cidrs):
        r"""Sets the dedicated_cidrs of this AccessConfig.

        专线接入网段。接入模式包含专线方式时选填，多个网段信息用分号隔开，列表长度不超过5。

        :param dedicated_cidrs: The dedicated_cidrs of this AccessConfig.
        :type dedicated_cidrs: str
        """
        self._dedicated_cidrs = dedicated_cidrs

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
        if not isinstance(other, AccessConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
