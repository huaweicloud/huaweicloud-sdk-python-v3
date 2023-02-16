# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeModeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authority_enable': 'bool',
        'admin_pwd': 'str',
        'https_enable': 'bool'
    }

    attribute_map = {
        'authority_enable': 'authorityEnable',
        'admin_pwd': 'adminPwd',
        'https_enable': 'httpsEnable'
    }

    def __init__(self, authority_enable=None, admin_pwd=None, https_enable=None):
        """ChangeModeReq

        The model defined in huaweicloud sdk

        :param authority_enable: 是否开启安全模式。 - true: 开启安全模式。 - false: 关闭安全模式。 默认为：true。
        :type authority_enable: bool
        :param admin_pwd: 安全模式下集群密码。
        :type admin_pwd: str
        :param https_enable: 是否开启HTTPS。 - true: 开启HTTPS。 - false: 关闭HTTPS。 默认为：true。
        :type https_enable: bool
        """
        
        

        self._authority_enable = None
        self._admin_pwd = None
        self._https_enable = None
        self.discriminator = None

        self.authority_enable = authority_enable
        if admin_pwd is not None:
            self.admin_pwd = admin_pwd
        self.https_enable = https_enable

    @property
    def authority_enable(self):
        """Gets the authority_enable of this ChangeModeReq.

        是否开启安全模式。 - true: 开启安全模式。 - false: 关闭安全模式。 默认为：true。

        :return: The authority_enable of this ChangeModeReq.
        :rtype: bool
        """
        return self._authority_enable

    @authority_enable.setter
    def authority_enable(self, authority_enable):
        """Sets the authority_enable of this ChangeModeReq.

        是否开启安全模式。 - true: 开启安全模式。 - false: 关闭安全模式。 默认为：true。

        :param authority_enable: The authority_enable of this ChangeModeReq.
        :type authority_enable: bool
        """
        self._authority_enable = authority_enable

    @property
    def admin_pwd(self):
        """Gets the admin_pwd of this ChangeModeReq.

        安全模式下集群密码。

        :return: The admin_pwd of this ChangeModeReq.
        :rtype: str
        """
        return self._admin_pwd

    @admin_pwd.setter
    def admin_pwd(self, admin_pwd):
        """Sets the admin_pwd of this ChangeModeReq.

        安全模式下集群密码。

        :param admin_pwd: The admin_pwd of this ChangeModeReq.
        :type admin_pwd: str
        """
        self._admin_pwd = admin_pwd

    @property
    def https_enable(self):
        """Gets the https_enable of this ChangeModeReq.

        是否开启HTTPS。 - true: 开启HTTPS。 - false: 关闭HTTPS。 默认为：true。

        :return: The https_enable of this ChangeModeReq.
        :rtype: bool
        """
        return self._https_enable

    @https_enable.setter
    def https_enable(self, https_enable):
        """Sets the https_enable of this ChangeModeReq.

        是否开启HTTPS。 - true: 开启HTTPS。 - false: 关闭HTTPS。 默认为：true。

        :param https_enable: The https_enable of this ChangeModeReq.
        :type https_enable: bool
        """
        self._https_enable = https_enable

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
        if not isinstance(other, ChangeModeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
