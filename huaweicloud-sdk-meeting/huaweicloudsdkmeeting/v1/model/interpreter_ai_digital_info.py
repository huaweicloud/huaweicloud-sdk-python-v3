# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterpreterAiDigitalInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'digital_account': 'str',
        'digital_name': 'str',
        'presenter_account': 'str',
        'presenter_real_name_account': 'str',
        'presenter_name': 'str',
        'presenter_user_id': 'str',
        'local_conf_id': 'str',
        'local_conf_addr': 'str',
        'local_auth_info': 'str',
        'local_need_proxy': 'bool',
        'local_auth_url': 'str',
        'local_auth_app_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'digital_account': 'digitalAccount',
        'digital_name': 'digitalName',
        'presenter_account': 'presenterAccount',
        'presenter_real_name_account': 'presenterRealNameAccount',
        'presenter_name': 'presenterName',
        'presenter_user_id': 'presenterUserID',
        'local_conf_id': 'localConfId',
        'local_conf_addr': 'localConfAddr',
        'local_auth_info': 'localAuthInfo',
        'local_need_proxy': 'localNeedProxy',
        'local_auth_url': 'localAuthUrl',
        'local_auth_app_id': 'localAuthAppId'
    }

    def __init__(self, type=None, digital_account=None, digital_name=None, presenter_account=None, presenter_real_name_account=None, presenter_name=None, presenter_user_id=None, local_conf_id=None, local_conf_addr=None, local_auth_info=None, local_need_proxy=None, local_auth_url=None, local_auth_app_id=None):
        r"""InterpreterAiDigitalInfo

        The model defined in huaweicloud sdk

        :param type: 数字资产类型：PUBLIC（系统公共）、PRIVATE（企业专用账号绑定）、LOCAL（企业本地通用）。
        :type type: str
        :param digital_account: AI传译员场景下绑定使用的数字资产ID（数字人或TTS音色）。
        :type digital_account: str
        :param digital_name: 数字资产名称。
        :type digital_name: str
        :param presenter_account: 专用数字资产绑定的发言人登录账号，翻译对象非匿名必填。
        :type presenter_account: str
        :param presenter_real_name_account: 专用数字资产绑定的发言人登录账号（匿名时），翻译对象匿名必填。
        :type presenter_real_name_account: str
        :param presenter_name: 专用数字资产绑定的发言人名称。
        :type presenter_name: str
        :param presenter_user_id: 发言人用户的userUUID。
        :type presenter_user_id: str
        :param local_conf_id: 本地会议的会议id（第三方对接参数），数字资产为LOCAL时必填。
        :type local_conf_id: str
        :param local_conf_addr: 本地会议对接地址或域名。
        :type local_conf_addr: str
        :param local_auth_info: 本地会议对接鉴权信息。
        :type local_auth_info: str
        :param local_need_proxy: true：需要代理 false：不需要代理。
        :type local_need_proxy: bool
        :param local_auth_url: 本地会议获取动态鉴权信息Url。
        :type local_auth_url: str
        :param local_auth_app_id: 本地会议鉴权AppId。
        :type local_auth_app_id: str
        """
        
        

        self._type = None
        self._digital_account = None
        self._digital_name = None
        self._presenter_account = None
        self._presenter_real_name_account = None
        self._presenter_name = None
        self._presenter_user_id = None
        self._local_conf_id = None
        self._local_conf_addr = None
        self._local_auth_info = None
        self._local_need_proxy = None
        self._local_auth_url = None
        self._local_auth_app_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if digital_account is not None:
            self.digital_account = digital_account
        if digital_name is not None:
            self.digital_name = digital_name
        if presenter_account is not None:
            self.presenter_account = presenter_account
        if presenter_real_name_account is not None:
            self.presenter_real_name_account = presenter_real_name_account
        if presenter_name is not None:
            self.presenter_name = presenter_name
        if presenter_user_id is not None:
            self.presenter_user_id = presenter_user_id
        if local_conf_id is not None:
            self.local_conf_id = local_conf_id
        if local_conf_addr is not None:
            self.local_conf_addr = local_conf_addr
        if local_auth_info is not None:
            self.local_auth_info = local_auth_info
        if local_need_proxy is not None:
            self.local_need_proxy = local_need_proxy
        if local_auth_url is not None:
            self.local_auth_url = local_auth_url
        if local_auth_app_id is not None:
            self.local_auth_app_id = local_auth_app_id

    @property
    def type(self):
        r"""Gets the type of this InterpreterAiDigitalInfo.

        数字资产类型：PUBLIC（系统公共）、PRIVATE（企业专用账号绑定）、LOCAL（企业本地通用）。

        :return: The type of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this InterpreterAiDigitalInfo.

        数字资产类型：PUBLIC（系统公共）、PRIVATE（企业专用账号绑定）、LOCAL（企业本地通用）。

        :param type: The type of this InterpreterAiDigitalInfo.
        :type type: str
        """
        self._type = type

    @property
    def digital_account(self):
        r"""Gets the digital_account of this InterpreterAiDigitalInfo.

        AI传译员场景下绑定使用的数字资产ID（数字人或TTS音色）。

        :return: The digital_account of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._digital_account

    @digital_account.setter
    def digital_account(self, digital_account):
        r"""Sets the digital_account of this InterpreterAiDigitalInfo.

        AI传译员场景下绑定使用的数字资产ID（数字人或TTS音色）。

        :param digital_account: The digital_account of this InterpreterAiDigitalInfo.
        :type digital_account: str
        """
        self._digital_account = digital_account

    @property
    def digital_name(self):
        r"""Gets the digital_name of this InterpreterAiDigitalInfo.

        数字资产名称。

        :return: The digital_name of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._digital_name

    @digital_name.setter
    def digital_name(self, digital_name):
        r"""Sets the digital_name of this InterpreterAiDigitalInfo.

        数字资产名称。

        :param digital_name: The digital_name of this InterpreterAiDigitalInfo.
        :type digital_name: str
        """
        self._digital_name = digital_name

    @property
    def presenter_account(self):
        r"""Gets the presenter_account of this InterpreterAiDigitalInfo.

        专用数字资产绑定的发言人登录账号，翻译对象非匿名必填。

        :return: The presenter_account of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._presenter_account

    @presenter_account.setter
    def presenter_account(self, presenter_account):
        r"""Sets the presenter_account of this InterpreterAiDigitalInfo.

        专用数字资产绑定的发言人登录账号，翻译对象非匿名必填。

        :param presenter_account: The presenter_account of this InterpreterAiDigitalInfo.
        :type presenter_account: str
        """
        self._presenter_account = presenter_account

    @property
    def presenter_real_name_account(self):
        r"""Gets the presenter_real_name_account of this InterpreterAiDigitalInfo.

        专用数字资产绑定的发言人登录账号（匿名时），翻译对象匿名必填。

        :return: The presenter_real_name_account of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._presenter_real_name_account

    @presenter_real_name_account.setter
    def presenter_real_name_account(self, presenter_real_name_account):
        r"""Sets the presenter_real_name_account of this InterpreterAiDigitalInfo.

        专用数字资产绑定的发言人登录账号（匿名时），翻译对象匿名必填。

        :param presenter_real_name_account: The presenter_real_name_account of this InterpreterAiDigitalInfo.
        :type presenter_real_name_account: str
        """
        self._presenter_real_name_account = presenter_real_name_account

    @property
    def presenter_name(self):
        r"""Gets the presenter_name of this InterpreterAiDigitalInfo.

        专用数字资产绑定的发言人名称。

        :return: The presenter_name of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._presenter_name

    @presenter_name.setter
    def presenter_name(self, presenter_name):
        r"""Sets the presenter_name of this InterpreterAiDigitalInfo.

        专用数字资产绑定的发言人名称。

        :param presenter_name: The presenter_name of this InterpreterAiDigitalInfo.
        :type presenter_name: str
        """
        self._presenter_name = presenter_name

    @property
    def presenter_user_id(self):
        r"""Gets the presenter_user_id of this InterpreterAiDigitalInfo.

        发言人用户的userUUID。

        :return: The presenter_user_id of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._presenter_user_id

    @presenter_user_id.setter
    def presenter_user_id(self, presenter_user_id):
        r"""Sets the presenter_user_id of this InterpreterAiDigitalInfo.

        发言人用户的userUUID。

        :param presenter_user_id: The presenter_user_id of this InterpreterAiDigitalInfo.
        :type presenter_user_id: str
        """
        self._presenter_user_id = presenter_user_id

    @property
    def local_conf_id(self):
        r"""Gets the local_conf_id of this InterpreterAiDigitalInfo.

        本地会议的会议id（第三方对接参数），数字资产为LOCAL时必填。

        :return: The local_conf_id of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._local_conf_id

    @local_conf_id.setter
    def local_conf_id(self, local_conf_id):
        r"""Sets the local_conf_id of this InterpreterAiDigitalInfo.

        本地会议的会议id（第三方对接参数），数字资产为LOCAL时必填。

        :param local_conf_id: The local_conf_id of this InterpreterAiDigitalInfo.
        :type local_conf_id: str
        """
        self._local_conf_id = local_conf_id

    @property
    def local_conf_addr(self):
        r"""Gets the local_conf_addr of this InterpreterAiDigitalInfo.

        本地会议对接地址或域名。

        :return: The local_conf_addr of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._local_conf_addr

    @local_conf_addr.setter
    def local_conf_addr(self, local_conf_addr):
        r"""Sets the local_conf_addr of this InterpreterAiDigitalInfo.

        本地会议对接地址或域名。

        :param local_conf_addr: The local_conf_addr of this InterpreterAiDigitalInfo.
        :type local_conf_addr: str
        """
        self._local_conf_addr = local_conf_addr

    @property
    def local_auth_info(self):
        r"""Gets the local_auth_info of this InterpreterAiDigitalInfo.

        本地会议对接鉴权信息。

        :return: The local_auth_info of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._local_auth_info

    @local_auth_info.setter
    def local_auth_info(self, local_auth_info):
        r"""Sets the local_auth_info of this InterpreterAiDigitalInfo.

        本地会议对接鉴权信息。

        :param local_auth_info: The local_auth_info of this InterpreterAiDigitalInfo.
        :type local_auth_info: str
        """
        self._local_auth_info = local_auth_info

    @property
    def local_need_proxy(self):
        r"""Gets the local_need_proxy of this InterpreterAiDigitalInfo.

        true：需要代理 false：不需要代理。

        :return: The local_need_proxy of this InterpreterAiDigitalInfo.
        :rtype: bool
        """
        return self._local_need_proxy

    @local_need_proxy.setter
    def local_need_proxy(self, local_need_proxy):
        r"""Sets the local_need_proxy of this InterpreterAiDigitalInfo.

        true：需要代理 false：不需要代理。

        :param local_need_proxy: The local_need_proxy of this InterpreterAiDigitalInfo.
        :type local_need_proxy: bool
        """
        self._local_need_proxy = local_need_proxy

    @property
    def local_auth_url(self):
        r"""Gets the local_auth_url of this InterpreterAiDigitalInfo.

        本地会议获取动态鉴权信息Url。

        :return: The local_auth_url of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._local_auth_url

    @local_auth_url.setter
    def local_auth_url(self, local_auth_url):
        r"""Sets the local_auth_url of this InterpreterAiDigitalInfo.

        本地会议获取动态鉴权信息Url。

        :param local_auth_url: The local_auth_url of this InterpreterAiDigitalInfo.
        :type local_auth_url: str
        """
        self._local_auth_url = local_auth_url

    @property
    def local_auth_app_id(self):
        r"""Gets the local_auth_app_id of this InterpreterAiDigitalInfo.

        本地会议鉴权AppId。

        :return: The local_auth_app_id of this InterpreterAiDigitalInfo.
        :rtype: str
        """
        return self._local_auth_app_id

    @local_auth_app_id.setter
    def local_auth_app_id(self, local_auth_app_id):
        r"""Sets the local_auth_app_id of this InterpreterAiDigitalInfo.

        本地会议鉴权AppId。

        :param local_auth_app_id: The local_auth_app_id of this InterpreterAiDigitalInfo.
        :type local_auth_app_id: str
        """
        self._local_auth_app_id = local_auth_app_id

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
        if not isinstance(other, InterpreterAiDigitalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
