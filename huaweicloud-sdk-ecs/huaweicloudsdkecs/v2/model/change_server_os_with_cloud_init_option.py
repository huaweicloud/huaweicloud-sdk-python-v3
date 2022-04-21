# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeServerOsWithCloudInitOption:

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
        'metadata': 'ChangeSeversOsMetadata',
        'mode': 'str'
    }

    attribute_map = {
        'adminpass': 'adminpass',
        'keyname': 'keyname',
        'userid': 'userid',
        'imageid': 'imageid',
        'metadata': 'metadata',
        'mode': 'mode'
    }

    def __init__(self, adminpass=None, keyname=None, userid=None, imageid=None, metadata=None, mode=None):
        """ChangeServerOsWithCloudInitOption

        The model defined in huaweicloud sdk

        :param adminpass: 云服务器管理员帐户的初始登录密码。  其中，Windows管理员帐户的用户名为Administrator。  建议密码复杂度如下：  - 长度为8-26位。 - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_&#x3D;+[{}]:,./?）中的三种。  &gt; 说明： &gt;  - Windows云服务器的密码，不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。 - 对于Linux弹性云服务器也可使用user_data字段实现密码注入，此时adminpass字段无效。 - adminpass和keyname不能同时有值。 - adminpass和keyname如果同时为空，此时，metadata中的user_data属性必须有值。 - 对于已安装Cloud-init的云服务器，使用adminpass字段切换操作系统时，系统如果提示您使用keypair方式切换操作系统，表示当前区域暂不支持使用密码方式。
        :type adminpass: str
        :param keyname: 密钥名称。  密钥可以通过密钥创建接口进行创建（请参见[创建和导入SSH密钥](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212678.html)），或使用SSH密钥查询接口查询已有的密钥（请参见[查询SSH密钥列表](https://support.huaweicloud.com/api-ecs/ecs_03_1201.html) ）。
        :type keyname: str
        :param userid: 用户ID。 说明 如果使用秘钥方式切换操作系统，则该字段为必选字段。
        :type userid: str
        :param imageid: 切换系统所使用的新镜像的ID，格式为UUID。  镜像的ID可以从控制台或者参考[《镜像服务API参考》](https://support.huaweicloud.com/api-ims/ims_03_0702.html)的“查询镜像列表”的章节获取。
        :type imageid: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkecs.v2.ChangeSeversOsMetadata`
        :param mode: 取值为withStopServer ，支持开机状态下切换弹性云服务器操作系统。 mode取值为withStopServer时，对开机状态的弹性云服务器执行切换操作系统操作，系统自动对云服务器先执行关机，再切换操作系统。
        :type mode: str
        """
        
        

        self._adminpass = None
        self._keyname = None
        self._userid = None
        self._imageid = None
        self._metadata = None
        self._mode = None
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
        if mode is not None:
            self.mode = mode

    @property
    def adminpass(self):
        """Gets the adminpass of this ChangeServerOsWithCloudInitOption.

        云服务器管理员帐户的初始登录密码。  其中，Windows管理员帐户的用户名为Administrator。  建议密码复杂度如下：  - 长度为8-26位。 - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。  > 说明： >  - Windows云服务器的密码，不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。 - 对于Linux弹性云服务器也可使用user_data字段实现密码注入，此时adminpass字段无效。 - adminpass和keyname不能同时有值。 - adminpass和keyname如果同时为空，此时，metadata中的user_data属性必须有值。 - 对于已安装Cloud-init的云服务器，使用adminpass字段切换操作系统时，系统如果提示您使用keypair方式切换操作系统，表示当前区域暂不支持使用密码方式。

        :return: The adminpass of this ChangeServerOsWithCloudInitOption.
        :rtype: str
        """
        return self._adminpass

    @adminpass.setter
    def adminpass(self, adminpass):
        """Sets the adminpass of this ChangeServerOsWithCloudInitOption.

        云服务器管理员帐户的初始登录密码。  其中，Windows管理员帐户的用户名为Administrator。  建议密码复杂度如下：  - 长度为8-26位。 - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。  > 说明： >  - Windows云服务器的密码，不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。 - 对于Linux弹性云服务器也可使用user_data字段实现密码注入，此时adminpass字段无效。 - adminpass和keyname不能同时有值。 - adminpass和keyname如果同时为空，此时，metadata中的user_data属性必须有值。 - 对于已安装Cloud-init的云服务器，使用adminpass字段切换操作系统时，系统如果提示您使用keypair方式切换操作系统，表示当前区域暂不支持使用密码方式。

        :param adminpass: The adminpass of this ChangeServerOsWithCloudInitOption.
        :type adminpass: str
        """
        self._adminpass = adminpass

    @property
    def keyname(self):
        """Gets the keyname of this ChangeServerOsWithCloudInitOption.

        密钥名称。  密钥可以通过密钥创建接口进行创建（请参见[创建和导入SSH密钥](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212678.html)），或使用SSH密钥查询接口查询已有的密钥（请参见[查询SSH密钥列表](https://support.huaweicloud.com/api-ecs/ecs_03_1201.html) ）。

        :return: The keyname of this ChangeServerOsWithCloudInitOption.
        :rtype: str
        """
        return self._keyname

    @keyname.setter
    def keyname(self, keyname):
        """Sets the keyname of this ChangeServerOsWithCloudInitOption.

        密钥名称。  密钥可以通过密钥创建接口进行创建（请参见[创建和导入SSH密钥](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212678.html)），或使用SSH密钥查询接口查询已有的密钥（请参见[查询SSH密钥列表](https://support.huaweicloud.com/api-ecs/ecs_03_1201.html) ）。

        :param keyname: The keyname of this ChangeServerOsWithCloudInitOption.
        :type keyname: str
        """
        self._keyname = keyname

    @property
    def userid(self):
        """Gets the userid of this ChangeServerOsWithCloudInitOption.

        用户ID。 说明 如果使用秘钥方式切换操作系统，则该字段为必选字段。

        :return: The userid of this ChangeServerOsWithCloudInitOption.
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this ChangeServerOsWithCloudInitOption.

        用户ID。 说明 如果使用秘钥方式切换操作系统，则该字段为必选字段。

        :param userid: The userid of this ChangeServerOsWithCloudInitOption.
        :type userid: str
        """
        self._userid = userid

    @property
    def imageid(self):
        """Gets the imageid of this ChangeServerOsWithCloudInitOption.

        切换系统所使用的新镜像的ID，格式为UUID。  镜像的ID可以从控制台或者参考[《镜像服务API参考》](https://support.huaweicloud.com/api-ims/ims_03_0702.html)的“查询镜像列表”的章节获取。

        :return: The imageid of this ChangeServerOsWithCloudInitOption.
        :rtype: str
        """
        return self._imageid

    @imageid.setter
    def imageid(self, imageid):
        """Sets the imageid of this ChangeServerOsWithCloudInitOption.

        切换系统所使用的新镜像的ID，格式为UUID。  镜像的ID可以从控制台或者参考[《镜像服务API参考》](https://support.huaweicloud.com/api-ims/ims_03_0702.html)的“查询镜像列表”的章节获取。

        :param imageid: The imageid of this ChangeServerOsWithCloudInitOption.
        :type imageid: str
        """
        self._imageid = imageid

    @property
    def metadata(self):
        """Gets the metadata of this ChangeServerOsWithCloudInitOption.


        :return: The metadata of this ChangeServerOsWithCloudInitOption.
        :rtype: :class:`huaweicloudsdkecs.v2.ChangeSeversOsMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ChangeServerOsWithCloudInitOption.


        :param metadata: The metadata of this ChangeServerOsWithCloudInitOption.
        :type metadata: :class:`huaweicloudsdkecs.v2.ChangeSeversOsMetadata`
        """
        self._metadata = metadata

    @property
    def mode(self):
        """Gets the mode of this ChangeServerOsWithCloudInitOption.

        取值为withStopServer ，支持开机状态下切换弹性云服务器操作系统。 mode取值为withStopServer时，对开机状态的弹性云服务器执行切换操作系统操作，系统自动对云服务器先执行关机，再切换操作系统。

        :return: The mode of this ChangeServerOsWithCloudInitOption.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ChangeServerOsWithCloudInitOption.

        取值为withStopServer ，支持开机状态下切换弹性云服务器操作系统。 mode取值为withStopServer时，对开机状态的弹性云服务器执行切换操作系统操作，系统自动对云服务器先执行关机，再切换操作系统。

        :param mode: The mode of this ChangeServerOsWithCloudInitOption.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, ChangeServerOsWithCloudInitOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
