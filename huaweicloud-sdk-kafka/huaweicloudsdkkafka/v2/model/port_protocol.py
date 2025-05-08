# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortProtocol:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'private_plain_enable': 'bool',
        'private_sasl_ssl_enable': 'bool',
        'private_sasl_plaintext_enable': 'bool',
        'public_plain_enable': 'bool',
        'public_sasl_ssl_enable': 'bool',
        'public_sasl_plaintext_enable': 'bool'
    }

    attribute_map = {
        'private_plain_enable': 'private_plain_enable',
        'private_sasl_ssl_enable': 'private_sasl_ssl_enable',
        'private_sasl_plaintext_enable': 'private_sasl_plaintext_enable',
        'public_plain_enable': 'public_plain_enable',
        'public_sasl_ssl_enable': 'public_sasl_ssl_enable',
        'public_sasl_plaintext_enable': 'public_sasl_plaintext_enable'
    }

    def __init__(self, private_plain_enable=None, private_sasl_ssl_enable=None, private_sasl_plaintext_enable=None, public_plain_enable=None, public_sasl_ssl_enable=None, public_sasl_plaintext_enable=None):
        r"""PortProtocol

        The model defined in huaweicloud sdk

        :param private_plain_enable: 是否开启内网明文访问连接方式。  取值范围：   - true: 开启内网明文访问连接方式，连接地址：ip:9092，访问协议PLAINTEXT。   - false: 关闭内网明文访问。  默认为false。
        :type private_plain_enable: bool
        :param private_sasl_ssl_enable: 是否开启安全协议为SASL_SSL的内网密文接入方式。  取值范围：   - true: 开启安全协议为SASL_SSL的内网密文接入方式。           private_sasl_ssl_enable和private_sasl_plaintext_enable不能同时为true。   - false: 关闭安全协议为SASL_SSL的内网接入方式。  默认为false。
        :type private_sasl_ssl_enable: bool
        :param private_sasl_plaintext_enable: 是否开启安全协议为SASL_PLAINTEXT的内网密文接入方式。  取值范围：   - true: 开启安全协议为SASL_PLAINTEXT的内网密文接入方式，连接地址：ip:9093，访问协议SASL_PLAINTEXT。           private_sasl_plaintext_enable和private_sasl_ssl_enable不能同时为true。   - false: 关闭安全协议为SASL_PLAINTEXT的内网密文接入方式。  默认为false。
        :type private_sasl_plaintext_enable: bool
        :param public_plain_enable: 是否开启公网明文访问连接方式。  取值范围：   - true: 开启公网明文访问连接方式，连接地址：ip:9094，访问协议PLAINTEXT。           开启公网明文接入前，需要先开启公网访问功能。   - false: 关闭公网明文接入方式。  默认为false。
        :type public_plain_enable: bool
        :param public_sasl_ssl_enable: 是否开启安全协议为SASL_SSL的公网密文接入。  取值范围：   - true: 开启安全协议为SASL_SSL的公网密文接入方式，连接地址：ip:9095，访问协议：SASL_SSL。           public_sasl_ssl_enable和public_sasl_plaintext_enable不能同时为true。           为true时，需要实例开启公网。   - false: 关闭安全协议为SASL_SSL的公网密文接入方式。  默认为false。
        :type public_sasl_ssl_enable: bool
        :param public_sasl_plaintext_enable: 是否开启安全协议为SASL_PLAINTEXT的公网密文接入方式。  取值范围：   - true: 开启安全协议为SASL_PLAINTEXT的公网密文接入方式，连接地址：ip:9095，访问协议：SASL_PLAINTEXT。           public_sasl_plaintext_enable和public_sasl_ssl_enable不能同时为true。           为true时，需要实例开启公网。   - false: 关闭安全协议为SASL_PLAINTEXT的公网密文接入方式。  默认为false。
        :type public_sasl_plaintext_enable: bool
        """
        
        

        self._private_plain_enable = None
        self._private_sasl_ssl_enable = None
        self._private_sasl_plaintext_enable = None
        self._public_plain_enable = None
        self._public_sasl_ssl_enable = None
        self._public_sasl_plaintext_enable = None
        self.discriminator = None

        if private_plain_enable is not None:
            self.private_plain_enable = private_plain_enable
        if private_sasl_ssl_enable is not None:
            self.private_sasl_ssl_enable = private_sasl_ssl_enable
        if private_sasl_plaintext_enable is not None:
            self.private_sasl_plaintext_enable = private_sasl_plaintext_enable
        if public_plain_enable is not None:
            self.public_plain_enable = public_plain_enable
        if public_sasl_ssl_enable is not None:
            self.public_sasl_ssl_enable = public_sasl_ssl_enable
        if public_sasl_plaintext_enable is not None:
            self.public_sasl_plaintext_enable = public_sasl_plaintext_enable

    @property
    def private_plain_enable(self):
        r"""Gets the private_plain_enable of this PortProtocol.

        是否开启内网明文访问连接方式。  取值范围：   - true: 开启内网明文访问连接方式，连接地址：ip:9092，访问协议PLAINTEXT。   - false: 关闭内网明文访问。  默认为false。

        :return: The private_plain_enable of this PortProtocol.
        :rtype: bool
        """
        return self._private_plain_enable

    @private_plain_enable.setter
    def private_plain_enable(self, private_plain_enable):
        r"""Sets the private_plain_enable of this PortProtocol.

        是否开启内网明文访问连接方式。  取值范围：   - true: 开启内网明文访问连接方式，连接地址：ip:9092，访问协议PLAINTEXT。   - false: 关闭内网明文访问。  默认为false。

        :param private_plain_enable: The private_plain_enable of this PortProtocol.
        :type private_plain_enable: bool
        """
        self._private_plain_enable = private_plain_enable

    @property
    def private_sasl_ssl_enable(self):
        r"""Gets the private_sasl_ssl_enable of this PortProtocol.

        是否开启安全协议为SASL_SSL的内网密文接入方式。  取值范围：   - true: 开启安全协议为SASL_SSL的内网密文接入方式。           private_sasl_ssl_enable和private_sasl_plaintext_enable不能同时为true。   - false: 关闭安全协议为SASL_SSL的内网接入方式。  默认为false。

        :return: The private_sasl_ssl_enable of this PortProtocol.
        :rtype: bool
        """
        return self._private_sasl_ssl_enable

    @private_sasl_ssl_enable.setter
    def private_sasl_ssl_enable(self, private_sasl_ssl_enable):
        r"""Sets the private_sasl_ssl_enable of this PortProtocol.

        是否开启安全协议为SASL_SSL的内网密文接入方式。  取值范围：   - true: 开启安全协议为SASL_SSL的内网密文接入方式。           private_sasl_ssl_enable和private_sasl_plaintext_enable不能同时为true。   - false: 关闭安全协议为SASL_SSL的内网接入方式。  默认为false。

        :param private_sasl_ssl_enable: The private_sasl_ssl_enable of this PortProtocol.
        :type private_sasl_ssl_enable: bool
        """
        self._private_sasl_ssl_enable = private_sasl_ssl_enable

    @property
    def private_sasl_plaintext_enable(self):
        r"""Gets the private_sasl_plaintext_enable of this PortProtocol.

        是否开启安全协议为SASL_PLAINTEXT的内网密文接入方式。  取值范围：   - true: 开启安全协议为SASL_PLAINTEXT的内网密文接入方式，连接地址：ip:9093，访问协议SASL_PLAINTEXT。           private_sasl_plaintext_enable和private_sasl_ssl_enable不能同时为true。   - false: 关闭安全协议为SASL_PLAINTEXT的内网密文接入方式。  默认为false。

        :return: The private_sasl_plaintext_enable of this PortProtocol.
        :rtype: bool
        """
        return self._private_sasl_plaintext_enable

    @private_sasl_plaintext_enable.setter
    def private_sasl_plaintext_enable(self, private_sasl_plaintext_enable):
        r"""Sets the private_sasl_plaintext_enable of this PortProtocol.

        是否开启安全协议为SASL_PLAINTEXT的内网密文接入方式。  取值范围：   - true: 开启安全协议为SASL_PLAINTEXT的内网密文接入方式，连接地址：ip:9093，访问协议SASL_PLAINTEXT。           private_sasl_plaintext_enable和private_sasl_ssl_enable不能同时为true。   - false: 关闭安全协议为SASL_PLAINTEXT的内网密文接入方式。  默认为false。

        :param private_sasl_plaintext_enable: The private_sasl_plaintext_enable of this PortProtocol.
        :type private_sasl_plaintext_enable: bool
        """
        self._private_sasl_plaintext_enable = private_sasl_plaintext_enable

    @property
    def public_plain_enable(self):
        r"""Gets the public_plain_enable of this PortProtocol.

        是否开启公网明文访问连接方式。  取值范围：   - true: 开启公网明文访问连接方式，连接地址：ip:9094，访问协议PLAINTEXT。           开启公网明文接入前，需要先开启公网访问功能。   - false: 关闭公网明文接入方式。  默认为false。

        :return: The public_plain_enable of this PortProtocol.
        :rtype: bool
        """
        return self._public_plain_enable

    @public_plain_enable.setter
    def public_plain_enable(self, public_plain_enable):
        r"""Sets the public_plain_enable of this PortProtocol.

        是否开启公网明文访问连接方式。  取值范围：   - true: 开启公网明文访问连接方式，连接地址：ip:9094，访问协议PLAINTEXT。           开启公网明文接入前，需要先开启公网访问功能。   - false: 关闭公网明文接入方式。  默认为false。

        :param public_plain_enable: The public_plain_enable of this PortProtocol.
        :type public_plain_enable: bool
        """
        self._public_plain_enable = public_plain_enable

    @property
    def public_sasl_ssl_enable(self):
        r"""Gets the public_sasl_ssl_enable of this PortProtocol.

        是否开启安全协议为SASL_SSL的公网密文接入。  取值范围：   - true: 开启安全协议为SASL_SSL的公网密文接入方式，连接地址：ip:9095，访问协议：SASL_SSL。           public_sasl_ssl_enable和public_sasl_plaintext_enable不能同时为true。           为true时，需要实例开启公网。   - false: 关闭安全协议为SASL_SSL的公网密文接入方式。  默认为false。

        :return: The public_sasl_ssl_enable of this PortProtocol.
        :rtype: bool
        """
        return self._public_sasl_ssl_enable

    @public_sasl_ssl_enable.setter
    def public_sasl_ssl_enable(self, public_sasl_ssl_enable):
        r"""Sets the public_sasl_ssl_enable of this PortProtocol.

        是否开启安全协议为SASL_SSL的公网密文接入。  取值范围：   - true: 开启安全协议为SASL_SSL的公网密文接入方式，连接地址：ip:9095，访问协议：SASL_SSL。           public_sasl_ssl_enable和public_sasl_plaintext_enable不能同时为true。           为true时，需要实例开启公网。   - false: 关闭安全协议为SASL_SSL的公网密文接入方式。  默认为false。

        :param public_sasl_ssl_enable: The public_sasl_ssl_enable of this PortProtocol.
        :type public_sasl_ssl_enable: bool
        """
        self._public_sasl_ssl_enable = public_sasl_ssl_enable

    @property
    def public_sasl_plaintext_enable(self):
        r"""Gets the public_sasl_plaintext_enable of this PortProtocol.

        是否开启安全协议为SASL_PLAINTEXT的公网密文接入方式。  取值范围：   - true: 开启安全协议为SASL_PLAINTEXT的公网密文接入方式，连接地址：ip:9095，访问协议：SASL_PLAINTEXT。           public_sasl_plaintext_enable和public_sasl_ssl_enable不能同时为true。           为true时，需要实例开启公网。   - false: 关闭安全协议为SASL_PLAINTEXT的公网密文接入方式。  默认为false。

        :return: The public_sasl_plaintext_enable of this PortProtocol.
        :rtype: bool
        """
        return self._public_sasl_plaintext_enable

    @public_sasl_plaintext_enable.setter
    def public_sasl_plaintext_enable(self, public_sasl_plaintext_enable):
        r"""Sets the public_sasl_plaintext_enable of this PortProtocol.

        是否开启安全协议为SASL_PLAINTEXT的公网密文接入方式。  取值范围：   - true: 开启安全协议为SASL_PLAINTEXT的公网密文接入方式，连接地址：ip:9095，访问协议：SASL_PLAINTEXT。           public_sasl_plaintext_enable和public_sasl_ssl_enable不能同时为true。           为true时，需要实例开启公网。   - false: 关闭安全协议为SASL_PLAINTEXT的公网密文接入方式。  默认为false。

        :param public_sasl_plaintext_enable: The public_sasl_plaintext_enable of this PortProtocol.
        :type public_sasl_plaintext_enable: bool
        """
        self._public_sasl_plaintext_enable = public_sasl_plaintext_enable

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
        if not isinstance(other, PortProtocol):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
