# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImagePwdComplexityInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'latest_scan_time': 'int',
        'min_length': 'bool',
        'uppercase_letter': 'bool',
        'lowercase_letter': 'bool',
        'number': 'bool',
        'special_character': 'bool',
        'suggestion': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'latest_scan_time': 'latest_scan_time',
        'min_length': 'min_length',
        'uppercase_letter': 'uppercase_letter',
        'lowercase_letter': 'lowercase_letter',
        'number': 'number',
        'special_character': 'special_character',
        'suggestion': 'suggestion'
    }

    def __init__(self, image_id=None, namespace=None, image_name=None, image_version=None, image_type=None, latest_scan_time=None, min_length=None, uppercase_letter=None, lowercase_letter=None, number=None, special_character=None, suggestion=None):
        r"""ImagePwdComplexityInfoResponseInfo

        The model defined in huaweicloud sdk

        :param image_id: **参数解释**: 镜像ID **取值范围**: 字符长度0-128位 
        :type image_id: str
        :param namespace: **参数解释**: 组织名称（只有私有镜像和共享镜像有该字段，本地镜像没有） **取值范围**: 字符长度0-65535位 
        :type namespace: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-256位 
        :type image_version: str
        :param image_type: **参数解释**: 仓库镜像类型 **取值范围**: - SwrPrivate : swr私有镜像。 - SwrShared : swr共享。 - SwrEnterprise : swr企业。 - Harbor : harbor仓库。 - Jfrog : jfrog仓库。 - Other : 其他仓库。 
        :type image_type: str
        :param latest_scan_time: **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值2147483647 
        :type latest_scan_time: int
        :param min_length: **参数解释**： 口令最小长度 **取值范围**： - true：是。 - false：否。 
        :type min_length: bool
        :param uppercase_letter: **参数解释**： 大写字母 **取值范围**： - true：是。 - false：否。 
        :type uppercase_letter: bool
        :param lowercase_letter: **参数解释**： 小写字母 **取值范围**： - true：是。 - false：否。 
        :type lowercase_letter: bool
        :param number: **参数解释**： 数字 **取值范围**： - true：是。 - false：否。 
        :type number: bool
        :param special_character: **参数解释**： 特殊字符 **取值范围**： - true：是。 - false：否。 
        :type special_character: bool
        :param suggestion: **参数解释**: 修改建议 **取值范围**: 字符长度0-65534位 
        :type suggestion: str
        """
        
        

        self._image_id = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._image_type = None
        self._latest_scan_time = None
        self._min_length = None
        self._uppercase_letter = None
        self._lowercase_letter = None
        self._number = None
        self._special_character = None
        self._suggestion = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if min_length is not None:
            self.min_length = min_length
        if uppercase_letter is not None:
            self.uppercase_letter = uppercase_letter
        if lowercase_letter is not None:
            self.lowercase_letter = lowercase_letter
        if number is not None:
            self.number = number
        if special_character is not None:
            self.special_character = special_character
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def image_id(self):
        r"""Gets the image_id of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 镜像ID **取值范围**: 字符长度0-128位 

        :return: The image_id of this ImagePwdComplexityInfoResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 镜像ID **取值范围**: 字符长度0-128位 

        :param image_id: The image_id of this ImagePwdComplexityInfoResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 组织名称（只有私有镜像和共享镜像有该字段，本地镜像没有） **取值范围**: 字符长度0-65535位 

        :return: The namespace of this ImagePwdComplexityInfoResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 组织名称（只有私有镜像和共享镜像有该字段，本地镜像没有） **取值范围**: 字符长度0-65535位 

        :param namespace: The namespace of this ImagePwdComplexityInfoResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 

        :return: The image_name of this ImagePwdComplexityInfoResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 

        :param image_name: The image_name of this ImagePwdComplexityInfoResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-256位 

        :return: The image_version of this ImagePwdComplexityInfoResponseInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-256位 

        :param image_version: The image_version of this ImagePwdComplexityInfoResponseInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        r"""Gets the image_type of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 仓库镜像类型 **取值范围**: - SwrPrivate : swr私有镜像。 - SwrShared : swr共享。 - SwrEnterprise : swr企业。 - Harbor : harbor仓库。 - Jfrog : jfrog仓库。 - Other : 其他仓库。 

        :return: The image_type of this ImagePwdComplexityInfoResponseInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 仓库镜像类型 **取值范围**: - SwrPrivate : swr私有镜像。 - SwrShared : swr共享。 - SwrEnterprise : swr企业。 - Harbor : harbor仓库。 - Jfrog : jfrog仓库。 - Other : 其他仓库。 

        :param image_type: The image_type of this ImagePwdComplexityInfoResponseInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值2147483647 

        :return: The latest_scan_time of this ImagePwdComplexityInfoResponseInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值2147483647 

        :param latest_scan_time: The latest_scan_time of this ImagePwdComplexityInfoResponseInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def min_length(self):
        r"""Gets the min_length of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**： 口令最小长度 **取值范围**： - true：是。 - false：否。 

        :return: The min_length of this ImagePwdComplexityInfoResponseInfo.
        :rtype: bool
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        r"""Sets the min_length of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**： 口令最小长度 **取值范围**： - true：是。 - false：否。 

        :param min_length: The min_length of this ImagePwdComplexityInfoResponseInfo.
        :type min_length: bool
        """
        self._min_length = min_length

    @property
    def uppercase_letter(self):
        r"""Gets the uppercase_letter of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**： 大写字母 **取值范围**： - true：是。 - false：否。 

        :return: The uppercase_letter of this ImagePwdComplexityInfoResponseInfo.
        :rtype: bool
        """
        return self._uppercase_letter

    @uppercase_letter.setter
    def uppercase_letter(self, uppercase_letter):
        r"""Sets the uppercase_letter of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**： 大写字母 **取值范围**： - true：是。 - false：否。 

        :param uppercase_letter: The uppercase_letter of this ImagePwdComplexityInfoResponseInfo.
        :type uppercase_letter: bool
        """
        self._uppercase_letter = uppercase_letter

    @property
    def lowercase_letter(self):
        r"""Gets the lowercase_letter of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**： 小写字母 **取值范围**： - true：是。 - false：否。 

        :return: The lowercase_letter of this ImagePwdComplexityInfoResponseInfo.
        :rtype: bool
        """
        return self._lowercase_letter

    @lowercase_letter.setter
    def lowercase_letter(self, lowercase_letter):
        r"""Sets the lowercase_letter of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**： 小写字母 **取值范围**： - true：是。 - false：否。 

        :param lowercase_letter: The lowercase_letter of this ImagePwdComplexityInfoResponseInfo.
        :type lowercase_letter: bool
        """
        self._lowercase_letter = lowercase_letter

    @property
    def number(self):
        r"""Gets the number of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**： 数字 **取值范围**： - true：是。 - false：否。 

        :return: The number of this ImagePwdComplexityInfoResponseInfo.
        :rtype: bool
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**： 数字 **取值范围**： - true：是。 - false：否。 

        :param number: The number of this ImagePwdComplexityInfoResponseInfo.
        :type number: bool
        """
        self._number = number

    @property
    def special_character(self):
        r"""Gets the special_character of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**： 特殊字符 **取值范围**： - true：是。 - false：否。 

        :return: The special_character of this ImagePwdComplexityInfoResponseInfo.
        :rtype: bool
        """
        return self._special_character

    @special_character.setter
    def special_character(self, special_character):
        r"""Sets the special_character of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**： 特殊字符 **取值范围**： - true：是。 - false：否。 

        :param special_character: The special_character of this ImagePwdComplexityInfoResponseInfo.
        :type special_character: bool
        """
        self._special_character = special_character

    @property
    def suggestion(self):
        r"""Gets the suggestion of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 修改建议 **取值范围**: 字符长度0-65534位 

        :return: The suggestion of this ImagePwdComplexityInfoResponseInfo.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this ImagePwdComplexityInfoResponseInfo.

        **参数解释**: 修改建议 **取值范围**: 字符长度0-65534位 

        :param suggestion: The suggestion of this ImagePwdComplexityInfoResponseInfo.
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
        if not isinstance(other, ImagePwdComplexityInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
