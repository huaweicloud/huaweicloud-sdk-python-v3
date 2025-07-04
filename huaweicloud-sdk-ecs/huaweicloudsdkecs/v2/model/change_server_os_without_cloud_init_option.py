# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeServerOsWithoutCloudInitOption:

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
        'mode': 'str',
        'metadata': 'ChangeSeversOsMetadataWithoutCloudInitOption',
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'adminpass': 'adminpass',
        'keyname': 'keyname',
        'userid': 'userid',
        'imageid': 'imageid',
        'mode': 'mode',
        'metadata': 'metadata',
        'is_auto_pay': 'isAutoPay'
    }

    def __init__(self, adminpass=None, keyname=None, userid=None, imageid=None, mode=None, metadata=None, is_auto_pay=None):
        r"""ChangeServerOsWithoutCloudInitOption

        The model defined in huaweicloud sdk

        :param adminpass: 云服务器管理员帐户的初始登录密码。  其中，Windows管理员帐户的用户名为Administrator。  建议密码复杂度如下：  - 长度为8-26位。 - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_&#x3D;+[{}]:,./?）中的三种。  &gt; 说明： &gt;  - 对于Windows弹性云服务器，密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。 - adminpass和keyname不能同时为空。
        :type adminpass: str
        :param keyname: 密钥名称。  密钥可以通过密钥创建接口进行创建（请参见[创建和导入SSH密钥](https://support.huaweicloud.com/api-dew/CreateKeypair.html)），或使用SSH密钥查询接口查询已有的密钥（请参见[查询SSH密钥列表](https://support.huaweicloud.com/api-dew/ListKeypairs.html) ）。
        :type keyname: str
        :param userid: 用户ID。 说明 如果使用秘钥方式切换操作系统，则该字段为必选字段。
        :type userid: str
        :param imageid: 切换系统所使用的新镜像的ID，格式为UUID。  镜像的ID可以从控制台或者参考[《镜像服务API参考》](https://support.huaweicloud.com/api-ims/ims_03_0702.html)的“查询镜像列表”的章节获取。
        :type imageid: str
        :param mode: 取值为withStopServer ，支持开机状态下切换弹性云服务器操作系统。  mode取值为withStopServer时，对开机状态的  弹性云服务器执行切换操作系统操作，系统自动对云服务器先执行关机，再切换操作系统。
        :type mode: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkecs.v2.ChangeSeversOsMetadataWithoutCloudInitOption`
        :param is_auto_pay: 下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付。
        :type is_auto_pay: str
        """
        
        

        self._adminpass = None
        self._keyname = None
        self._userid = None
        self._imageid = None
        self._mode = None
        self._metadata = None
        self._is_auto_pay = None
        self.discriminator = None

        if adminpass is not None:
            self.adminpass = adminpass
        if keyname is not None:
            self.keyname = keyname
        if userid is not None:
            self.userid = userid
        self.imageid = imageid
        if mode is not None:
            self.mode = mode
        if metadata is not None:
            self.metadata = metadata
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def adminpass(self):
        r"""Gets the adminpass of this ChangeServerOsWithoutCloudInitOption.

        云服务器管理员帐户的初始登录密码。  其中，Windows管理员帐户的用户名为Administrator。  建议密码复杂度如下：  - 长度为8-26位。 - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。  > 说明： >  - 对于Windows弹性云服务器，密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。 - adminpass和keyname不能同时为空。

        :return: The adminpass of this ChangeServerOsWithoutCloudInitOption.
        :rtype: str
        """
        return self._adminpass

    @adminpass.setter
    def adminpass(self, adminpass):
        r"""Sets the adminpass of this ChangeServerOsWithoutCloudInitOption.

        云服务器管理员帐户的初始登录密码。  其中，Windows管理员帐户的用户名为Administrator。  建议密码复杂度如下：  - 长度为8-26位。 - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。  > 说明： >  - 对于Windows弹性云服务器，密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。 - adminpass和keyname不能同时为空。

        :param adminpass: The adminpass of this ChangeServerOsWithoutCloudInitOption.
        :type adminpass: str
        """
        self._adminpass = adminpass

    @property
    def keyname(self):
        r"""Gets the keyname of this ChangeServerOsWithoutCloudInitOption.

        密钥名称。  密钥可以通过密钥创建接口进行创建（请参见[创建和导入SSH密钥](https://support.huaweicloud.com/api-dew/CreateKeypair.html)），或使用SSH密钥查询接口查询已有的密钥（请参见[查询SSH密钥列表](https://support.huaweicloud.com/api-dew/ListKeypairs.html) ）。

        :return: The keyname of this ChangeServerOsWithoutCloudInitOption.
        :rtype: str
        """
        return self._keyname

    @keyname.setter
    def keyname(self, keyname):
        r"""Sets the keyname of this ChangeServerOsWithoutCloudInitOption.

        密钥名称。  密钥可以通过密钥创建接口进行创建（请参见[创建和导入SSH密钥](https://support.huaweicloud.com/api-dew/CreateKeypair.html)），或使用SSH密钥查询接口查询已有的密钥（请参见[查询SSH密钥列表](https://support.huaweicloud.com/api-dew/ListKeypairs.html) ）。

        :param keyname: The keyname of this ChangeServerOsWithoutCloudInitOption.
        :type keyname: str
        """
        self._keyname = keyname

    @property
    def userid(self):
        r"""Gets the userid of this ChangeServerOsWithoutCloudInitOption.

        用户ID。 说明 如果使用秘钥方式切换操作系统，则该字段为必选字段。

        :return: The userid of this ChangeServerOsWithoutCloudInitOption.
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        r"""Sets the userid of this ChangeServerOsWithoutCloudInitOption.

        用户ID。 说明 如果使用秘钥方式切换操作系统，则该字段为必选字段。

        :param userid: The userid of this ChangeServerOsWithoutCloudInitOption.
        :type userid: str
        """
        self._userid = userid

    @property
    def imageid(self):
        r"""Gets the imageid of this ChangeServerOsWithoutCloudInitOption.

        切换系统所使用的新镜像的ID，格式为UUID。  镜像的ID可以从控制台或者参考[《镜像服务API参考》](https://support.huaweicloud.com/api-ims/ims_03_0702.html)的“查询镜像列表”的章节获取。

        :return: The imageid of this ChangeServerOsWithoutCloudInitOption.
        :rtype: str
        """
        return self._imageid

    @imageid.setter
    def imageid(self, imageid):
        r"""Sets the imageid of this ChangeServerOsWithoutCloudInitOption.

        切换系统所使用的新镜像的ID，格式为UUID。  镜像的ID可以从控制台或者参考[《镜像服务API参考》](https://support.huaweicloud.com/api-ims/ims_03_0702.html)的“查询镜像列表”的章节获取。

        :param imageid: The imageid of this ChangeServerOsWithoutCloudInitOption.
        :type imageid: str
        """
        self._imageid = imageid

    @property
    def mode(self):
        r"""Gets the mode of this ChangeServerOsWithoutCloudInitOption.

        取值为withStopServer ，支持开机状态下切换弹性云服务器操作系统。  mode取值为withStopServer时，对开机状态的  弹性云服务器执行切换操作系统操作，系统自动对云服务器先执行关机，再切换操作系统。

        :return: The mode of this ChangeServerOsWithoutCloudInitOption.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ChangeServerOsWithoutCloudInitOption.

        取值为withStopServer ，支持开机状态下切换弹性云服务器操作系统。  mode取值为withStopServer时，对开机状态的  弹性云服务器执行切换操作系统操作，系统自动对云服务器先执行关机，再切换操作系统。

        :param mode: The mode of this ChangeServerOsWithoutCloudInitOption.
        :type mode: str
        """
        self._mode = mode

    @property
    def metadata(self):
        r"""Gets the metadata of this ChangeServerOsWithoutCloudInitOption.

        :return: The metadata of this ChangeServerOsWithoutCloudInitOption.
        :rtype: :class:`huaweicloudsdkecs.v2.ChangeSeversOsMetadataWithoutCloudInitOption`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ChangeServerOsWithoutCloudInitOption.

        :param metadata: The metadata of this ChangeServerOsWithoutCloudInitOption.
        :type metadata: :class:`huaweicloudsdkecs.v2.ChangeSeversOsMetadataWithoutCloudInitOption`
        """
        self._metadata = metadata

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ChangeServerOsWithoutCloudInitOption.

        下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付。

        :return: The is_auto_pay of this ChangeServerOsWithoutCloudInitOption.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ChangeServerOsWithoutCloudInitOption.

        下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付。

        :param is_auto_pay: The is_auto_pay of this ChangeServerOsWithoutCloudInitOption.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, ChangeServerOsWithoutCloudInitOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
