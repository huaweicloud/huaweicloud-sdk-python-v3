# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOnePermRuleRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rw_type': 'str',
        'user_type': 'str'
    }

    attribute_map = {
        'rw_type': 'rw_type',
        'user_type': 'user_type'
    }

    def __init__(self, rw_type=None, user_type=None):
        r"""UpdateOnePermRuleRequestInfo

        The model defined in huaweicloud sdk

        :param rw_type: 授权对象的读写权限   - rw：默认选项，以读写的方式共享   - ro：以只读的方式共享   - none: 没有权限 
        :type rw_type: str
        :param user_type: 授权对象的系统用户对文件系统的访问权限。取值如下：  - no_root_squash：默认选项。客户端使用包括root用户在内的任何用户，NFS服务器都保持客户端使用的用户，不做映射。  - root_squash：客户端使用的是root用户时，映射到NFS服务器的用户为NFS的匿名用户（nfsnobody）。客户端使用非root用户时，NFS服务器保持客户端使用的用户，不做映射。  - all_squash：所有访问NFS服务器的客户端的用户都映射为匿名用户。 
        :type user_type: str
        """
        
        

        self._rw_type = None
        self._user_type = None
        self.discriminator = None

        if rw_type is not None:
            self.rw_type = rw_type
        if user_type is not None:
            self.user_type = user_type

    @property
    def rw_type(self):
        r"""Gets the rw_type of this UpdateOnePermRuleRequestInfo.

        授权对象的读写权限   - rw：默认选项，以读写的方式共享   - ro：以只读的方式共享   - none: 没有权限 

        :return: The rw_type of this UpdateOnePermRuleRequestInfo.
        :rtype: str
        """
        return self._rw_type

    @rw_type.setter
    def rw_type(self, rw_type):
        r"""Sets the rw_type of this UpdateOnePermRuleRequestInfo.

        授权对象的读写权限   - rw：默认选项，以读写的方式共享   - ro：以只读的方式共享   - none: 没有权限 

        :param rw_type: The rw_type of this UpdateOnePermRuleRequestInfo.
        :type rw_type: str
        """
        self._rw_type = rw_type

    @property
    def user_type(self):
        r"""Gets the user_type of this UpdateOnePermRuleRequestInfo.

        授权对象的系统用户对文件系统的访问权限。取值如下：  - no_root_squash：默认选项。客户端使用包括root用户在内的任何用户，NFS服务器都保持客户端使用的用户，不做映射。  - root_squash：客户端使用的是root用户时，映射到NFS服务器的用户为NFS的匿名用户（nfsnobody）。客户端使用非root用户时，NFS服务器保持客户端使用的用户，不做映射。  - all_squash：所有访问NFS服务器的客户端的用户都映射为匿名用户。 

        :return: The user_type of this UpdateOnePermRuleRequestInfo.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        r"""Sets the user_type of this UpdateOnePermRuleRequestInfo.

        授权对象的系统用户对文件系统的访问权限。取值如下：  - no_root_squash：默认选项。客户端使用包括root用户在内的任何用户，NFS服务器都保持客户端使用的用户，不做映射。  - root_squash：客户端使用的是root用户时，映射到NFS服务器的用户为NFS的匿名用户（nfsnobody）。客户端使用非root用户时，NFS服务器保持客户端使用的用户，不做映射。  - all_squash：所有访问NFS服务器的客户端的用户都映射为匿名用户。 

        :param user_type: The user_type of this UpdateOnePermRuleRequestInfo.
        :type user_type: str
        """
        self._user_type = user_type

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
        if not isinstance(other, UpdateOnePermRuleRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
