# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFunctionCodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'func_urn': 'str',
        'func_name': 'str',
        'domain_id': 'str',
        'runtime': 'str',
        'code_type': 'str',
        'code_url': 'str',
        'code_filename': 'str',
        'code_size': 'int',
        'digest': 'str',
        'last_modified': 'datetime',
        'func_code': 'FuncCode',
        'depend_list': 'list[str]',
        'depend_version_list': 'list[str]',
        'strategy_config': 'StrategyConfig',
        'dependencies': 'list[Dependency]',
        'code_encrypt_kms_key_id': 'str'
    }

    attribute_map = {
        'func_urn': 'func_urn',
        'func_name': 'func_name',
        'domain_id': 'domain_id',
        'runtime': 'runtime',
        'code_type': 'code_type',
        'code_url': 'code_url',
        'code_filename': 'code_filename',
        'code_size': 'code_size',
        'digest': 'digest',
        'last_modified': 'last_modified',
        'func_code': 'func_code',
        'depend_list': 'depend_list',
        'depend_version_list': 'depend_version_list',
        'strategy_config': 'strategy_config',
        'dependencies': 'dependencies',
        'code_encrypt_kms_key_id': 'code_encrypt_kms_key_id'
    }

    def __init__(self, func_urn=None, func_name=None, domain_id=None, runtime=None, code_type=None, code_url=None, code_filename=None, code_size=None, digest=None, last_modified=None, func_code=None, depend_list=None, depend_version_list=None, strategy_config=None, dependencies=None, code_encrypt_kms_key_id=None):
        r"""UpdateFunctionCodeResponse

        The model defined in huaweicloud sdk

        :param func_urn: 函数的URN（Uniform Resource Name），唯一标识函数。
        :type func_urn: str
        :param func_name: 函数名称。
        :type func_name: str
        :param domain_id: 域名id。
        :type domain_id: str
        :param runtime: FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。
        :type runtime: str
        :param code_type: 函数代码类型，取值有5种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。 Custom-Image-Swr: 函数代码来源与SWR自定义镜像。
        :type code_type: str
        :param code_url: 当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。
        :type code_url: str
        :param code_filename: 函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。
        :type code_filename: str
        :param code_size: 函数大小，单位：字节。
        :type code_size: int
        :param digest: 函数代码SHA512 hash值，用于判断函数是否变化。
        :type digest: str
        :param last_modified: 函数最后一次更新时间。
        :type last_modified: datetime
        :param func_code: 
        :type func_code: :class:`huaweicloudsdkfunctiongraph.v2.FuncCode`
        :param depend_list: 依赖id列表
        :type depend_list: list[str]
        :param depend_version_list: 依赖版本id列表
        :type depend_version_list: list[str]
        :param strategy_config: 
        :type strategy_config: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        :param dependencies: 函数依赖代码包列表。
        :type dependencies: list[:class:`huaweicloudsdkfunctiongraph.v2.Dependency`]
        :param code_encrypt_kms_key_id: 用于用户代码加密的kms主秘钥ID。
        :type code_encrypt_kms_key_id: str
        """
        
        super(UpdateFunctionCodeResponse, self).__init__()

        self._func_urn = None
        self._func_name = None
        self._domain_id = None
        self._runtime = None
        self._code_type = None
        self._code_url = None
        self._code_filename = None
        self._code_size = None
        self._digest = None
        self._last_modified = None
        self._func_code = None
        self._depend_list = None
        self._depend_version_list = None
        self._strategy_config = None
        self._dependencies = None
        self._code_encrypt_kms_key_id = None
        self.discriminator = None

        if func_urn is not None:
            self.func_urn = func_urn
        if func_name is not None:
            self.func_name = func_name
        if domain_id is not None:
            self.domain_id = domain_id
        if runtime is not None:
            self.runtime = runtime
        if code_type is not None:
            self.code_type = code_type
        if code_url is not None:
            self.code_url = code_url
        if code_filename is not None:
            self.code_filename = code_filename
        if code_size is not None:
            self.code_size = code_size
        if digest is not None:
            self.digest = digest
        if last_modified is not None:
            self.last_modified = last_modified
        if func_code is not None:
            self.func_code = func_code
        if depend_list is not None:
            self.depend_list = depend_list
        if depend_version_list is not None:
            self.depend_version_list = depend_version_list
        if strategy_config is not None:
            self.strategy_config = strategy_config
        if dependencies is not None:
            self.dependencies = dependencies
        if code_encrypt_kms_key_id is not None:
            self.code_encrypt_kms_key_id = code_encrypt_kms_key_id

    @property
    def func_urn(self):
        r"""Gets the func_urn of this UpdateFunctionCodeResponse.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :return: The func_urn of this UpdateFunctionCodeResponse.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        r"""Sets the func_urn of this UpdateFunctionCodeResponse.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :param func_urn: The func_urn of this UpdateFunctionCodeResponse.
        :type func_urn: str
        """
        self._func_urn = func_urn

    @property
    def func_name(self):
        r"""Gets the func_name of this UpdateFunctionCodeResponse.

        函数名称。

        :return: The func_name of this UpdateFunctionCodeResponse.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        r"""Sets the func_name of this UpdateFunctionCodeResponse.

        函数名称。

        :param func_name: The func_name of this UpdateFunctionCodeResponse.
        :type func_name: str
        """
        self._func_name = func_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UpdateFunctionCodeResponse.

        域名id。

        :return: The domain_id of this UpdateFunctionCodeResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UpdateFunctionCodeResponse.

        域名id。

        :param domain_id: The domain_id of this UpdateFunctionCodeResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def runtime(self):
        r"""Gets the runtime of this UpdateFunctionCodeResponse.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :return: The runtime of this UpdateFunctionCodeResponse.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this UpdateFunctionCodeResponse.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :param runtime: The runtime of this UpdateFunctionCodeResponse.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def code_type(self):
        r"""Gets the code_type of this UpdateFunctionCodeResponse.

        函数代码类型，取值有5种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。 Custom-Image-Swr: 函数代码来源与SWR自定义镜像。

        :return: The code_type of this UpdateFunctionCodeResponse.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        r"""Sets the code_type of this UpdateFunctionCodeResponse.

        函数代码类型，取值有5种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。 Custom-Image-Swr: 函数代码来源与SWR自定义镜像。

        :param code_type: The code_type of this UpdateFunctionCodeResponse.
        :type code_type: str
        """
        self._code_type = code_type

    @property
    def code_url(self):
        r"""Gets the code_url of this UpdateFunctionCodeResponse.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :return: The code_url of this UpdateFunctionCodeResponse.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        r"""Sets the code_url of this UpdateFunctionCodeResponse.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :param code_url: The code_url of this UpdateFunctionCodeResponse.
        :type code_url: str
        """
        self._code_url = code_url

    @property
    def code_filename(self):
        r"""Gets the code_filename of this UpdateFunctionCodeResponse.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :return: The code_filename of this UpdateFunctionCodeResponse.
        :rtype: str
        """
        return self._code_filename

    @code_filename.setter
    def code_filename(self, code_filename):
        r"""Sets the code_filename of this UpdateFunctionCodeResponse.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :param code_filename: The code_filename of this UpdateFunctionCodeResponse.
        :type code_filename: str
        """
        self._code_filename = code_filename

    @property
    def code_size(self):
        r"""Gets the code_size of this UpdateFunctionCodeResponse.

        函数大小，单位：字节。

        :return: The code_size of this UpdateFunctionCodeResponse.
        :rtype: int
        """
        return self._code_size

    @code_size.setter
    def code_size(self, code_size):
        r"""Sets the code_size of this UpdateFunctionCodeResponse.

        函数大小，单位：字节。

        :param code_size: The code_size of this UpdateFunctionCodeResponse.
        :type code_size: int
        """
        self._code_size = code_size

    @property
    def digest(self):
        r"""Gets the digest of this UpdateFunctionCodeResponse.

        函数代码SHA512 hash值，用于判断函数是否变化。

        :return: The digest of this UpdateFunctionCodeResponse.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this UpdateFunctionCodeResponse.

        函数代码SHA512 hash值，用于判断函数是否变化。

        :param digest: The digest of this UpdateFunctionCodeResponse.
        :type digest: str
        """
        self._digest = digest

    @property
    def last_modified(self):
        r"""Gets the last_modified of this UpdateFunctionCodeResponse.

        函数最后一次更新时间。

        :return: The last_modified of this UpdateFunctionCodeResponse.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this UpdateFunctionCodeResponse.

        函数最后一次更新时间。

        :param last_modified: The last_modified of this UpdateFunctionCodeResponse.
        :type last_modified: datetime
        """
        self._last_modified = last_modified

    @property
    def func_code(self):
        r"""Gets the func_code of this UpdateFunctionCodeResponse.

        :return: The func_code of this UpdateFunctionCodeResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncCode`
        """
        return self._func_code

    @func_code.setter
    def func_code(self, func_code):
        r"""Sets the func_code of this UpdateFunctionCodeResponse.

        :param func_code: The func_code of this UpdateFunctionCodeResponse.
        :type func_code: :class:`huaweicloudsdkfunctiongraph.v2.FuncCode`
        """
        self._func_code = func_code

    @property
    def depend_list(self):
        r"""Gets the depend_list of this UpdateFunctionCodeResponse.

        依赖id列表

        :return: The depend_list of this UpdateFunctionCodeResponse.
        :rtype: list[str]
        """
        return self._depend_list

    @depend_list.setter
    def depend_list(self, depend_list):
        r"""Sets the depend_list of this UpdateFunctionCodeResponse.

        依赖id列表

        :param depend_list: The depend_list of this UpdateFunctionCodeResponse.
        :type depend_list: list[str]
        """
        self._depend_list = depend_list

    @property
    def depend_version_list(self):
        r"""Gets the depend_version_list of this UpdateFunctionCodeResponse.

        依赖版本id列表

        :return: The depend_version_list of this UpdateFunctionCodeResponse.
        :rtype: list[str]
        """
        return self._depend_version_list

    @depend_version_list.setter
    def depend_version_list(self, depend_version_list):
        r"""Sets the depend_version_list of this UpdateFunctionCodeResponse.

        依赖版本id列表

        :param depend_version_list: The depend_version_list of this UpdateFunctionCodeResponse.
        :type depend_version_list: list[str]
        """
        self._depend_version_list = depend_version_list

    @property
    def strategy_config(self):
        r"""Gets the strategy_config of this UpdateFunctionCodeResponse.

        :return: The strategy_config of this UpdateFunctionCodeResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        """
        return self._strategy_config

    @strategy_config.setter
    def strategy_config(self, strategy_config):
        r"""Sets the strategy_config of this UpdateFunctionCodeResponse.

        :param strategy_config: The strategy_config of this UpdateFunctionCodeResponse.
        :type strategy_config: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        """
        self._strategy_config = strategy_config

    @property
    def dependencies(self):
        r"""Gets the dependencies of this UpdateFunctionCodeResponse.

        函数依赖代码包列表。

        :return: The dependencies of this UpdateFunctionCodeResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.Dependency`]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        r"""Sets the dependencies of this UpdateFunctionCodeResponse.

        函数依赖代码包列表。

        :param dependencies: The dependencies of this UpdateFunctionCodeResponse.
        :type dependencies: list[:class:`huaweicloudsdkfunctiongraph.v2.Dependency`]
        """
        self._dependencies = dependencies

    @property
    def code_encrypt_kms_key_id(self):
        r"""Gets the code_encrypt_kms_key_id of this UpdateFunctionCodeResponse.

        用于用户代码加密的kms主秘钥ID。

        :return: The code_encrypt_kms_key_id of this UpdateFunctionCodeResponse.
        :rtype: str
        """
        return self._code_encrypt_kms_key_id

    @code_encrypt_kms_key_id.setter
    def code_encrypt_kms_key_id(self, code_encrypt_kms_key_id):
        r"""Sets the code_encrypt_kms_key_id of this UpdateFunctionCodeResponse.

        用于用户代码加密的kms主秘钥ID。

        :param code_encrypt_kms_key_id: The code_encrypt_kms_key_id of this UpdateFunctionCodeResponse.
        :type code_encrypt_kms_key_id: str
        """
        self._code_encrypt_kms_key_id = code_encrypt_kms_key_id

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
        if not isinstance(other, UpdateFunctionCodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
