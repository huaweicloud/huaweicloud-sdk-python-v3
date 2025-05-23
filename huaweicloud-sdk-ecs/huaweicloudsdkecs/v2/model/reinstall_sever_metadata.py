# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReinstallSeverMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'system__encrypted': 'str',
        'system__cmkid': 'str',
        'user_data': 'str',
        'byol': 'str'
    }

    attribute_map = {
        'system__encrypted': '__system__encrypted',
        'system__cmkid': '__system__cmkid',
        'user_data': 'user_data',
        'byol': 'BYOL'
    }

    def __init__(self, system__encrypted=None, system__cmkid=None, user_data=None, byol=None):
        r"""ReinstallSeverMetadata

        The model defined in huaweicloud sdk

        :param system__encrypted: metadata中的表示加密功能的字段，0代表不加密，1代表加密。  该字段不存在时，云硬盘默认为不加密。
        :type system__encrypted: str
        :param system__cmkid: metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。  &gt; 说明：  - 请参考[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)，通过HTTPS请求获取密钥ID。
        :type system__cmkid: str
        :param user_data: 重装云服务器过程中注入用户数据。  支持注入文本、文本文件或gzip文件。注入内容最大长度32KB。注入内容，需要进行base64格式编码。  了解更多用户数据注入请参考[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)。
        :type user_data: str
        :param byol: 如果您已拥有操作系统或软件的许可证（一般是指按物理插槽数、物理内核数等进行认证的许可证），您可以通过自带许可（BYOL）的方式将业务完整迁移到云平台，继续使用您的许可证。 - true： 使用自有license - 其他值： 视为非法参数，接口报错
        :type byol: str
        """
        
        

        self._system__encrypted = None
        self._system__cmkid = None
        self._user_data = None
        self._byol = None
        self.discriminator = None

        if system__encrypted is not None:
            self.system__encrypted = system__encrypted
        if system__cmkid is not None:
            self.system__cmkid = system__cmkid
        if user_data is not None:
            self.user_data = user_data
        if byol is not None:
            self.byol = byol

    @property
    def system__encrypted(self):
        r"""Gets the system__encrypted of this ReinstallSeverMetadata.

        metadata中的表示加密功能的字段，0代表不加密，1代表加密。  该字段不存在时，云硬盘默认为不加密。

        :return: The system__encrypted of this ReinstallSeverMetadata.
        :rtype: str
        """
        return self._system__encrypted

    @system__encrypted.setter
    def system__encrypted(self, system__encrypted):
        r"""Sets the system__encrypted of this ReinstallSeverMetadata.

        metadata中的表示加密功能的字段，0代表不加密，1代表加密。  该字段不存在时，云硬盘默认为不加密。

        :param system__encrypted: The system__encrypted of this ReinstallSeverMetadata.
        :type system__encrypted: str
        """
        self._system__encrypted = system__encrypted

    @property
    def system__cmkid(self):
        r"""Gets the system__cmkid of this ReinstallSeverMetadata.

        metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。  > 说明：  - 请参考[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)，通过HTTPS请求获取密钥ID。

        :return: The system__cmkid of this ReinstallSeverMetadata.
        :rtype: str
        """
        return self._system__cmkid

    @system__cmkid.setter
    def system__cmkid(self, system__cmkid):
        r"""Sets the system__cmkid of this ReinstallSeverMetadata.

        metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。  > 说明：  - 请参考[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)，通过HTTPS请求获取密钥ID。

        :param system__cmkid: The system__cmkid of this ReinstallSeverMetadata.
        :type system__cmkid: str
        """
        self._system__cmkid = system__cmkid

    @property
    def user_data(self):
        r"""Gets the user_data of this ReinstallSeverMetadata.

        重装云服务器过程中注入用户数据。  支持注入文本、文本文件或gzip文件。注入内容最大长度32KB。注入内容，需要进行base64格式编码。  了解更多用户数据注入请参考[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)。

        :return: The user_data of this ReinstallSeverMetadata.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this ReinstallSeverMetadata.

        重装云服务器过程中注入用户数据。  支持注入文本、文本文件或gzip文件。注入内容最大长度32KB。注入内容，需要进行base64格式编码。  了解更多用户数据注入请参考[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)。

        :param user_data: The user_data of this ReinstallSeverMetadata.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def byol(self):
        r"""Gets the byol of this ReinstallSeverMetadata.

        如果您已拥有操作系统或软件的许可证（一般是指按物理插槽数、物理内核数等进行认证的许可证），您可以通过自带许可（BYOL）的方式将业务完整迁移到云平台，继续使用您的许可证。 - true： 使用自有license - 其他值： 视为非法参数，接口报错

        :return: The byol of this ReinstallSeverMetadata.
        :rtype: str
        """
        return self._byol

    @byol.setter
    def byol(self, byol):
        r"""Sets the byol of this ReinstallSeverMetadata.

        如果您已拥有操作系统或软件的许可证（一般是指按物理插槽数、物理内核数等进行认证的许可证），您可以通过自带许可（BYOL）的方式将业务完整迁移到云平台，继续使用您的许可证。 - true： 使用自有license - 其他值： 视为非法参数，接口报错

        :param byol: The byol of this ReinstallSeverMetadata.
        :type byol: str
        """
        self._byol = byol

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
        if not isinstance(other, ReinstallSeverMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
