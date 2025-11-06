# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageWeakPwdListInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_id': 'str',
        'image_type': 'str',
        'latest_scan_time': 'int',
        'user_name': 'str',
        'service_type': 'str',
        'duration': 'int',
        'desensitized_weak_passwords': 'str',
        'suggestion': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_id': 'image_id',
        'image_type': 'image_type',
        'latest_scan_time': 'latest_scan_time',
        'user_name': 'user_name',
        'service_type': 'service_type',
        'duration': 'duration',
        'desensitized_weak_passwords': 'desensitized_weak_passwords',
        'suggestion': 'suggestion'
    }

    def __init__(self, namespace=None, image_name=None, image_version=None, image_id=None, image_type=None, latest_scan_time=None, user_name=None, service_type=None, duration=None, desensitized_weak_passwords=None, suggestion=None):
        r"""ImageWeakPwdListInfoResponseInfo

        The model defined in huaweicloud sdk

        :param namespace: **参数解释**: 组织名称（只有私有镜像和共享镜像有该字段，本地镜像没有） **取值范围**: 字符长度0-65535位 
        :type namespace: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-128位 
        :type image_version: str
        :param image_id: **参数解释**: 镜像id **取值范围**: 字符长度0-128位 
        :type image_id: str
        :param image_type: **参数解释**: 仓库镜像类型，包含如下: **取值范围**: - SwrPrivate : swr私有镜像。 - SwrShared : swr共享。 - SwrEnterprise : swr企业。 - Harbor : harbor仓库。 - Jfrog : jfrog仓库。 - Other : 其他仓库。 
        :type image_type: str
        :param latest_scan_time: **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值2147483647 
        :type latest_scan_time: int
        :param user_name: **参数解释**: 弱口令账号名称 **取值范围**: 字符长度0-32位 
        :type user_name: str
        :param service_type: **参数解释**: 账号类型 **取值范围**: - system : 系统。 
        :type service_type: str
        :param duration: **参数解释**: 弱口令使用时长，单位天 **取值范围**: 最小值0，最大值2147483647 
        :type duration: int
        :param desensitized_weak_passwords: **参数解释**: 脱敏弱口令 **取值范围**: 字符长度0-128位 
        :type desensitized_weak_passwords: str
        :param suggestion: **参数解释**: 修改建议 **取值范围**: 字符长度0-65534位 
        :type suggestion: str
        """
        
        

        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._image_id = None
        self._image_type = None
        self._latest_scan_time = None
        self._user_name = None
        self._service_type = None
        self._duration = None
        self._desensitized_weak_passwords = None
        self._suggestion = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_id is not None:
            self.image_id = image_id
        if image_type is not None:
            self.image_type = image_type
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if user_name is not None:
            self.user_name = user_name
        if service_type is not None:
            self.service_type = service_type
        if duration is not None:
            self.duration = duration
        if desensitized_weak_passwords is not None:
            self.desensitized_weak_passwords = desensitized_weak_passwords
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def namespace(self):
        r"""Gets the namespace of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 组织名称（只有私有镜像和共享镜像有该字段，本地镜像没有） **取值范围**: 字符长度0-65535位 

        :return: The namespace of this ImageWeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 组织名称（只有私有镜像和共享镜像有该字段，本地镜像没有） **取值范围**: 字符长度0-65535位 

        :param namespace: The namespace of this ImageWeakPwdListInfoResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 

        :return: The image_name of this ImageWeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 

        :param image_name: The image_name of this ImageWeakPwdListInfoResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-128位 

        :return: The image_version of this ImageWeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-128位 

        :param image_version: The image_version of this ImageWeakPwdListInfoResponseInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_id(self):
        r"""Gets the image_id of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-128位 

        :return: The image_id of this ImageWeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-128位 

        :param image_id: The image_id of this ImageWeakPwdListInfoResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_type(self):
        r"""Gets the image_type of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 仓库镜像类型，包含如下: **取值范围**: - SwrPrivate : swr私有镜像。 - SwrShared : swr共享。 - SwrEnterprise : swr企业。 - Harbor : harbor仓库。 - Jfrog : jfrog仓库。 - Other : 其他仓库。 

        :return: The image_type of this ImageWeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 仓库镜像类型，包含如下: **取值范围**: - SwrPrivate : swr私有镜像。 - SwrShared : swr共享。 - SwrEnterprise : swr企业。 - Harbor : harbor仓库。 - Jfrog : jfrog仓库。 - Other : 其他仓库。 

        :param image_type: The image_type of this ImageWeakPwdListInfoResponseInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值2147483647 

        :return: The latest_scan_time of this ImageWeakPwdListInfoResponseInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值2147483647 

        :param latest_scan_time: The latest_scan_time of this ImageWeakPwdListInfoResponseInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def user_name(self):
        r"""Gets the user_name of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 弱口令账号名称 **取值范围**: 字符长度0-32位 

        :return: The user_name of this ImageWeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 弱口令账号名称 **取值范围**: 字符长度0-32位 

        :param user_name: The user_name of this ImageWeakPwdListInfoResponseInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def service_type(self):
        r"""Gets the service_type of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 账号类型 **取值范围**: - system : 系统。 

        :return: The service_type of this ImageWeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 账号类型 **取值范围**: - system : 系统。 

        :param service_type: The service_type of this ImageWeakPwdListInfoResponseInfo.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def duration(self):
        r"""Gets the duration of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 弱口令使用时长，单位天 **取值范围**: 最小值0，最大值2147483647 

        :return: The duration of this ImageWeakPwdListInfoResponseInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 弱口令使用时长，单位天 **取值范围**: 最小值0，最大值2147483647 

        :param duration: The duration of this ImageWeakPwdListInfoResponseInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def desensitized_weak_passwords(self):
        r"""Gets the desensitized_weak_passwords of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 脱敏弱口令 **取值范围**: 字符长度0-128位 

        :return: The desensitized_weak_passwords of this ImageWeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._desensitized_weak_passwords

    @desensitized_weak_passwords.setter
    def desensitized_weak_passwords(self, desensitized_weak_passwords):
        r"""Sets the desensitized_weak_passwords of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 脱敏弱口令 **取值范围**: 字符长度0-128位 

        :param desensitized_weak_passwords: The desensitized_weak_passwords of this ImageWeakPwdListInfoResponseInfo.
        :type desensitized_weak_passwords: str
        """
        self._desensitized_weak_passwords = desensitized_weak_passwords

    @property
    def suggestion(self):
        r"""Gets the suggestion of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 修改建议 **取值范围**: 字符长度0-65534位 

        :return: The suggestion of this ImageWeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this ImageWeakPwdListInfoResponseInfo.

        **参数解释**: 修改建议 **取值范围**: 字符长度0-65534位 

        :param suggestion: The suggestion of this ImageWeakPwdListInfoResponseInfo.
        :type suggestion: str
        """
        self._suggestion = suggestion

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageWeakPwdListInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
