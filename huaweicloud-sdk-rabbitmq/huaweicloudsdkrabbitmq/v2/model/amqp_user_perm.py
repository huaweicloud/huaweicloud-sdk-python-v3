# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AMQPUserPerm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vhost': 'str',
        'conf': 'str',
        'write': 'str',
        'read': 'str'
    }

    attribute_map = {
        'vhost': 'vhost',
        'conf': 'conf',
        'write': 'write',
        'read': 'read'
    }

    def __init__(self, vhost=None, conf=None, write=None, read=None):
        r"""AMQPUserPerm

        The model defined in huaweicloud sdk

        :param vhost: 需要配置权限的Vhost名称，一个用户可以配置多个Vhost下的资源权限。
        :type vhost: str
        :param conf: 使用正则表达式匹配资源配置权限。例如，在输入框内输入“^janeway-.*”，则表示授权给该用户当前Vhost下，所有名称以“janeway-”开头的资源的配置权限。
        :type conf: str
        :param write: 使用正则表达式匹配资源写权限。例如，在输入框内输入“.*”，则表示授权给该用户当前Vhost下，所有资源的写权限。
        :type write: str
        :param read: 使用正则表达式匹配资源读权限。例如，在输入框内输入“.*”，则表示授权给该用户当前Vhost下，所有资源的读权限。
        :type read: str
        """
        
        

        self._vhost = None
        self._conf = None
        self._write = None
        self._read = None
        self.discriminator = None

        self.vhost = vhost
        self.conf = conf
        self.write = write
        self.read = read

    @property
    def vhost(self):
        r"""Gets the vhost of this AMQPUserPerm.

        需要配置权限的Vhost名称，一个用户可以配置多个Vhost下的资源权限。

        :return: The vhost of this AMQPUserPerm.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        r"""Sets the vhost of this AMQPUserPerm.

        需要配置权限的Vhost名称，一个用户可以配置多个Vhost下的资源权限。

        :param vhost: The vhost of this AMQPUserPerm.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def conf(self):
        r"""Gets the conf of this AMQPUserPerm.

        使用正则表达式匹配资源配置权限。例如，在输入框内输入“^janeway-.*”，则表示授权给该用户当前Vhost下，所有名称以“janeway-”开头的资源的配置权限。

        :return: The conf of this AMQPUserPerm.
        :rtype: str
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        r"""Sets the conf of this AMQPUserPerm.

        使用正则表达式匹配资源配置权限。例如，在输入框内输入“^janeway-.*”，则表示授权给该用户当前Vhost下，所有名称以“janeway-”开头的资源的配置权限。

        :param conf: The conf of this AMQPUserPerm.
        :type conf: str
        """
        self._conf = conf

    @property
    def write(self):
        r"""Gets the write of this AMQPUserPerm.

        使用正则表达式匹配资源写权限。例如，在输入框内输入“.*”，则表示授权给该用户当前Vhost下，所有资源的写权限。

        :return: The write of this AMQPUserPerm.
        :rtype: str
        """
        return self._write

    @write.setter
    def write(self, write):
        r"""Sets the write of this AMQPUserPerm.

        使用正则表达式匹配资源写权限。例如，在输入框内输入“.*”，则表示授权给该用户当前Vhost下，所有资源的写权限。

        :param write: The write of this AMQPUserPerm.
        :type write: str
        """
        self._write = write

    @property
    def read(self):
        r"""Gets the read of this AMQPUserPerm.

        使用正则表达式匹配资源读权限。例如，在输入框内输入“.*”，则表示授权给该用户当前Vhost下，所有资源的读权限。

        :return: The read of this AMQPUserPerm.
        :rtype: str
        """
        return self._read

    @read.setter
    def read(self, read):
        r"""Sets the read of this AMQPUserPerm.

        使用正则表达式匹配资源读权限。例如，在输入框内输入“.*”，则表示授权给该用户当前Vhost下，所有资源的读权限。

        :param read: The read of this AMQPUserPerm.
        :type read: str
        """
        self._read = read

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
        if not isinstance(other, AMQPUserPerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
