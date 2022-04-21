# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OsChange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'adminpass': 'str',
        'keyname': 'str',
        'userid': 'str',
        'imageid': 'str',
        'metadata': 'MetadataInstall'
    }

    attribute_map = {
        'adminpass': 'adminpass',
        'keyname': 'keyname',
        'userid': 'userid',
        'imageid': 'imageid',
        'metadata': 'metadata'
    }

    def __init__(self, adminpass=None, keyname=None, userid=None, imageid=None, metadata=None):
        """OsChange

        The model defined in huaweicloud sdk

        :param adminpass: 裸金属服务器管理员帐号的初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。建议密码复杂度如下：长度为8-26位。密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_&#x3D;+[{}]:,./?）中的三种。密码不能包含用户名或用户名的逆序。 说明：对于Windows裸金属服务器，不能包含用户名中超过两个连续字符的部分。对于Linux裸金属服务器也可使用user_data字段实现密码注入，此时adminpass字段无效。adminpass和keyname不能同时有值。adminpass和keyname如果同时为空，此时，metadata中的user_data属性必须有值。
        :type adminpass: str
        :param keyname: 密钥名称。密钥可以通过7.10.3-创建和导入SSH密钥（OpenStack原生）API创建，或者使用7.10.1-查询SSH密钥列表（OpenStack原生）API查询已有的密钥。
        :type keyname: str
        :param userid: 用户ID（登录管理控制台，进入我的凭证，即可看到“用户ID”）。
        :type userid: str
        :param imageid: 镜像ID。镜像ID可以从镜像服务控制台获取，或者参考《镜像服务API参考》的“查询镜像列表”章节查询。在使用“查询镜像列表”API查询时，可以添加过滤字段“?virtual_env_type&#x3D;Ironic”来筛选裸金属服务器镜像。
        :type imageid: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkbms.v1.MetadataInstall`
        """
        
        

        self._adminpass = None
        self._keyname = None
        self._userid = None
        self._imageid = None
        self._metadata = None
        self.discriminator = None

        if adminpass is not None:
            self.adminpass = adminpass
        if keyname is not None:
            self.keyname = keyname
        if userid is not None:
            self.userid = userid
        self.imageid = imageid
        if metadata is not None:
            self.metadata = metadata

    @property
    def adminpass(self):
        """Gets the adminpass of this OsChange.

        裸金属服务器管理员帐号的初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。建议密码复杂度如下：长度为8-26位。密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。密码不能包含用户名或用户名的逆序。 说明：对于Windows裸金属服务器，不能包含用户名中超过两个连续字符的部分。对于Linux裸金属服务器也可使用user_data字段实现密码注入，此时adminpass字段无效。adminpass和keyname不能同时有值。adminpass和keyname如果同时为空，此时，metadata中的user_data属性必须有值。

        :return: The adminpass of this OsChange.
        :rtype: str
        """
        return self._adminpass

    @adminpass.setter
    def adminpass(self, adminpass):
        """Sets the adminpass of this OsChange.

        裸金属服务器管理员帐号的初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。建议密码复杂度如下：长度为8-26位。密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。密码不能包含用户名或用户名的逆序。 说明：对于Windows裸金属服务器，不能包含用户名中超过两个连续字符的部分。对于Linux裸金属服务器也可使用user_data字段实现密码注入，此时adminpass字段无效。adminpass和keyname不能同时有值。adminpass和keyname如果同时为空，此时，metadata中的user_data属性必须有值。

        :param adminpass: The adminpass of this OsChange.
        :type adminpass: str
        """
        self._adminpass = adminpass

    @property
    def keyname(self):
        """Gets the keyname of this OsChange.

        密钥名称。密钥可以通过7.10.3-创建和导入SSH密钥（OpenStack原生）API创建，或者使用7.10.1-查询SSH密钥列表（OpenStack原生）API查询已有的密钥。

        :return: The keyname of this OsChange.
        :rtype: str
        """
        return self._keyname

    @keyname.setter
    def keyname(self, keyname):
        """Sets the keyname of this OsChange.

        密钥名称。密钥可以通过7.10.3-创建和导入SSH密钥（OpenStack原生）API创建，或者使用7.10.1-查询SSH密钥列表（OpenStack原生）API查询已有的密钥。

        :param keyname: The keyname of this OsChange.
        :type keyname: str
        """
        self._keyname = keyname

    @property
    def userid(self):
        """Gets the userid of this OsChange.

        用户ID（登录管理控制台，进入我的凭证，即可看到“用户ID”）。

        :return: The userid of this OsChange.
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this OsChange.

        用户ID（登录管理控制台，进入我的凭证，即可看到“用户ID”）。

        :param userid: The userid of this OsChange.
        :type userid: str
        """
        self._userid = userid

    @property
    def imageid(self):
        """Gets the imageid of this OsChange.

        镜像ID。镜像ID可以从镜像服务控制台获取，或者参考《镜像服务API参考》的“查询镜像列表”章节查询。在使用“查询镜像列表”API查询时，可以添加过滤字段“?virtual_env_type=Ironic”来筛选裸金属服务器镜像。

        :return: The imageid of this OsChange.
        :rtype: str
        """
        return self._imageid

    @imageid.setter
    def imageid(self, imageid):
        """Sets the imageid of this OsChange.

        镜像ID。镜像ID可以从镜像服务控制台获取，或者参考《镜像服务API参考》的“查询镜像列表”章节查询。在使用“查询镜像列表”API查询时，可以添加过滤字段“?virtual_env_type=Ironic”来筛选裸金属服务器镜像。

        :param imageid: The imageid of this OsChange.
        :type imageid: str
        """
        self._imageid = imageid

    @property
    def metadata(self):
        """Gets the metadata of this OsChange.


        :return: The metadata of this OsChange.
        :rtype: :class:`huaweicloudsdkbms.v1.MetadataInstall`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this OsChange.


        :param metadata: The metadata of this OsChange.
        :type metadata: :class:`huaweicloudsdkbms.v1.MetadataInstall`
        """
        self._metadata = metadata

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
        if not isinstance(other, OsChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
