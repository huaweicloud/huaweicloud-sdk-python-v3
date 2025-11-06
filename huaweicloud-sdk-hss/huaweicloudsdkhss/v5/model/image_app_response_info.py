# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageAppResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'app_type': 'str',
        'app_version': 'str',
        'vul_num': 'int',
        'app_path': 'str',
        'layer_digest': 'str',
        'is_compliant': 'bool',
        'latest_scan_time': 'int',
        'image_type': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_id': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_type': 'app_type',
        'app_version': 'app_version',
        'vul_num': 'vul_num',
        'app_path': 'app_path',
        'layer_digest': 'layer_digest',
        'is_compliant': 'is_compliant',
        'latest_scan_time': 'latest_scan_time',
        'image_type': 'image_type',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_id': 'image_id'
    }

    def __init__(self, app_name=None, app_type=None, app_version=None, vul_num=None, app_path=None, layer_digest=None, is_compliant=None, latest_scan_time=None, image_type=None, namespace=None, image_name=None, image_version=None, image_id=None):
        r"""ImageAppResponseInfo

        The model defined in huaweicloud sdk

        :param app_name: **参数解释**: 软件名称 **取值范围**: 字符长度0-128位 
        :type app_name: str
        :param app_type: **参数解释**: 软件类型 **取值范围**: 字符长度0-128位 
        :type app_type: str
        :param app_version: **参数解释**: 软件版本 **取值范围**: 字符长度0-128位 
        :type app_version: str
        :param vul_num: **参数解释**: 漏洞总数 **取值范围**: 最小值0，最大值20000 
        :type vul_num: int
        :param app_path: **参数解释**: 软件路径 **取值范围**: 字符长度0-128位 
        :type app_path: str
        :param layer_digest: **参数解释**: 层digest **取值范围**: 字符长度0-128位 
        :type layer_digest: str
        :param is_compliant: **参数解释**: 是否合规，false为不合规 **取值范围**: - true：是。 - false：否。 
        :type is_compliant: bool
        :param latest_scan_time: **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值9223372036854775807 
        :type latest_scan_time: int
        :param image_type: **参数解释**: 仓库镜像类型，包含如下: **取值范围**: - SwrPrivate : swr私有镜像。 - SwrShared : swr共享。 - SwrEnterprise : swr企业。 - Harbor : harbor仓库。 - Jfrog : jfrog仓库。 - Other : 其他仓库。 
        :type image_type: str
        :param namespace: **参数解释**: 组织名称 **取值范围**: 字符长度0-65535位 
        :type namespace: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-65535位 
        :type image_version: str
        :param image_id: **参数解释**: 镜像id **取值范围**: 字符长度0-65535位 
        :type image_id: str
        """
        
        

        self._app_name = None
        self._app_type = None
        self._app_version = None
        self._vul_num = None
        self._app_path = None
        self._layer_digest = None
        self._is_compliant = None
        self._latest_scan_time = None
        self._image_type = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._image_id = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if app_type is not None:
            self.app_type = app_type
        if app_version is not None:
            self.app_version = app_version
        if vul_num is not None:
            self.vul_num = vul_num
        if app_path is not None:
            self.app_path = app_path
        if layer_digest is not None:
            self.layer_digest = layer_digest
        if is_compliant is not None:
            self.is_compliant = is_compliant
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if image_type is not None:
            self.image_type = image_type
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_id is not None:
            self.image_id = image_id

    @property
    def app_name(self):
        r"""Gets the app_name of this ImageAppResponseInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度0-128位 

        :return: The app_name of this ImageAppResponseInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ImageAppResponseInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度0-128位 

        :param app_name: The app_name of this ImageAppResponseInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_type(self):
        r"""Gets the app_type of this ImageAppResponseInfo.

        **参数解释**: 软件类型 **取值范围**: 字符长度0-128位 

        :return: The app_type of this ImageAppResponseInfo.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ImageAppResponseInfo.

        **参数解释**: 软件类型 **取值范围**: 字符长度0-128位 

        :param app_type: The app_type of this ImageAppResponseInfo.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def app_version(self):
        r"""Gets the app_version of this ImageAppResponseInfo.

        **参数解释**: 软件版本 **取值范围**: 字符长度0-128位 

        :return: The app_version of this ImageAppResponseInfo.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this ImageAppResponseInfo.

        **参数解释**: 软件版本 **取值范围**: 字符长度0-128位 

        :param app_version: The app_version of this ImageAppResponseInfo.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def vul_num(self):
        r"""Gets the vul_num of this ImageAppResponseInfo.

        **参数解释**: 漏洞总数 **取值范围**: 最小值0，最大值20000 

        :return: The vul_num of this ImageAppResponseInfo.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this ImageAppResponseInfo.

        **参数解释**: 漏洞总数 **取值范围**: 最小值0，最大值20000 

        :param vul_num: The vul_num of this ImageAppResponseInfo.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def app_path(self):
        r"""Gets the app_path of this ImageAppResponseInfo.

        **参数解释**: 软件路径 **取值范围**: 字符长度0-128位 

        :return: The app_path of this ImageAppResponseInfo.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        r"""Sets the app_path of this ImageAppResponseInfo.

        **参数解释**: 软件路径 **取值范围**: 字符长度0-128位 

        :param app_path: The app_path of this ImageAppResponseInfo.
        :type app_path: str
        """
        self._app_path = app_path

    @property
    def layer_digest(self):
        r"""Gets the layer_digest of this ImageAppResponseInfo.

        **参数解释**: 层digest **取值范围**: 字符长度0-128位 

        :return: The layer_digest of this ImageAppResponseInfo.
        :rtype: str
        """
        return self._layer_digest

    @layer_digest.setter
    def layer_digest(self, layer_digest):
        r"""Sets the layer_digest of this ImageAppResponseInfo.

        **参数解释**: 层digest **取值范围**: 字符长度0-128位 

        :param layer_digest: The layer_digest of this ImageAppResponseInfo.
        :type layer_digest: str
        """
        self._layer_digest = layer_digest

    @property
    def is_compliant(self):
        r"""Gets the is_compliant of this ImageAppResponseInfo.

        **参数解释**: 是否合规，false为不合规 **取值范围**: - true：是。 - false：否。 

        :return: The is_compliant of this ImageAppResponseInfo.
        :rtype: bool
        """
        return self._is_compliant

    @is_compliant.setter
    def is_compliant(self, is_compliant):
        r"""Sets the is_compliant of this ImageAppResponseInfo.

        **参数解释**: 是否合规，false为不合规 **取值范围**: - true：是。 - false：否。 

        :param is_compliant: The is_compliant of this ImageAppResponseInfo.
        :type is_compliant: bool
        """
        self._is_compliant = is_compliant

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this ImageAppResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The latest_scan_time of this ImageAppResponseInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this ImageAppResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值9223372036854775807 

        :param latest_scan_time: The latest_scan_time of this ImageAppResponseInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def image_type(self):
        r"""Gets the image_type of this ImageAppResponseInfo.

        **参数解释**: 仓库镜像类型，包含如下: **取值范围**: - SwrPrivate : swr私有镜像。 - SwrShared : swr共享。 - SwrEnterprise : swr企业。 - Harbor : harbor仓库。 - Jfrog : jfrog仓库。 - Other : 其他仓库。 

        :return: The image_type of this ImageAppResponseInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ImageAppResponseInfo.

        **参数解释**: 仓库镜像类型，包含如下: **取值范围**: - SwrPrivate : swr私有镜像。 - SwrShared : swr共享。 - SwrEnterprise : swr企业。 - Harbor : harbor仓库。 - Jfrog : jfrog仓库。 - Other : 其他仓库。 

        :param image_type: The image_type of this ImageAppResponseInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def namespace(self):
        r"""Gets the namespace of this ImageAppResponseInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-65535位 

        :return: The namespace of this ImageAppResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ImageAppResponseInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-65535位 

        :param namespace: The namespace of this ImageAppResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ImageAppResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 

        :return: The image_name of this ImageAppResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImageAppResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 

        :param image_name: The image_name of this ImageAppResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ImageAppResponseInfo.

        **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-65535位 

        :return: The image_version of this ImageAppResponseInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ImageAppResponseInfo.

        **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-65535位 

        :param image_version: The image_version of this ImageAppResponseInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_id(self):
        r"""Gets the image_id of this ImageAppResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-65535位 

        :return: The image_id of this ImageAppResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ImageAppResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-65535位 

        :param image_id: The image_id of this ImageAppResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

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
        if not isinstance(other, ImageAppResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
