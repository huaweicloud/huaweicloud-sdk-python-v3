# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageScanRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_type': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'is_blocking': 'bool',
        'repository_address': 'str',
        'login_user_name': 'str',
        'login_password': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'scan_type': 'scan_type',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'is_blocking': 'is_blocking',
        'repository_address': 'repository_address',
        'login_user_name': 'login_user_name',
        'login_password': 'login_password',
        'namespace': 'namespace'
    }

    def __init__(self, scan_type=None, image_name=None, image_version=None, is_blocking=None, repository_address=None, login_user_name=None, login_password=None, namespace=None):
        r"""ImageScanRequestInfo

        The model defined in huaweicloud sdk

        :param scan_type: **参数解释**: 扫描类型 **约束限制**: 不涉及 **取值范围**: - local_image：本地镜像，镜像扫描参数。 - remote_image：远程镜像仓，镜像扫描参数。  **默认取值**: 不涉及 
        :type scan_type: str
        :param image_name: **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type image_version: str
        :param is_blocking: **参数解释**: 流水线是否阻断 **约束限制**: 不涉及 **取值范围**:   - true：流水线被阻断。   - false：流水线未阻断。  **默认取值**: 不涉及 
        :type is_blocking: bool
        :param repository_address: **参数解释**: 镜像仓地址 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type repository_address: str
        :param login_user_name: **参数解释**: 镜像仓登录用户名 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type login_user_name: str
        :param login_password: **参数解释**: 镜像仓登录密码 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type login_password: str
        :param namespace: **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type namespace: str
        """
        
        

        self._scan_type = None
        self._image_name = None
        self._image_version = None
        self._is_blocking = None
        self._repository_address = None
        self._login_user_name = None
        self._login_password = None
        self._namespace = None
        self.discriminator = None

        if scan_type is not None:
            self.scan_type = scan_type
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if is_blocking is not None:
            self.is_blocking = is_blocking
        if repository_address is not None:
            self.repository_address = repository_address
        if login_user_name is not None:
            self.login_user_name = login_user_name
        if login_password is not None:
            self.login_password = login_password
        if namespace is not None:
            self.namespace = namespace

    @property
    def scan_type(self):
        r"""Gets the scan_type of this ImageScanRequestInfo.

        **参数解释**: 扫描类型 **约束限制**: 不涉及 **取值范围**: - local_image：本地镜像，镜像扫描参数。 - remote_image：远程镜像仓，镜像扫描参数。  **默认取值**: 不涉及 

        :return: The scan_type of this ImageScanRequestInfo.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this ImageScanRequestInfo.

        **参数解释**: 扫描类型 **约束限制**: 不涉及 **取值范围**: - local_image：本地镜像，镜像扫描参数。 - remote_image：远程镜像仓，镜像扫描参数。  **默认取值**: 不涉及 

        :param scan_type: The scan_type of this ImageScanRequestInfo.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def image_name(self):
        r"""Gets the image_name of this ImageScanRequestInfo.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The image_name of this ImageScanRequestInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImageScanRequestInfo.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param image_name: The image_name of this ImageScanRequestInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ImageScanRequestInfo.

        **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The image_version of this ImageScanRequestInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ImageScanRequestInfo.

        **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param image_version: The image_version of this ImageScanRequestInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def is_blocking(self):
        r"""Gets the is_blocking of this ImageScanRequestInfo.

        **参数解释**: 流水线是否阻断 **约束限制**: 不涉及 **取值范围**:   - true：流水线被阻断。   - false：流水线未阻断。  **默认取值**: 不涉及 

        :return: The is_blocking of this ImageScanRequestInfo.
        :rtype: bool
        """
        return self._is_blocking

    @is_blocking.setter
    def is_blocking(self, is_blocking):
        r"""Sets the is_blocking of this ImageScanRequestInfo.

        **参数解释**: 流水线是否阻断 **约束限制**: 不涉及 **取值范围**:   - true：流水线被阻断。   - false：流水线未阻断。  **默认取值**: 不涉及 

        :param is_blocking: The is_blocking of this ImageScanRequestInfo.
        :type is_blocking: bool
        """
        self._is_blocking = is_blocking

    @property
    def repository_address(self):
        r"""Gets the repository_address of this ImageScanRequestInfo.

        **参数解释**: 镜像仓地址 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The repository_address of this ImageScanRequestInfo.
        :rtype: str
        """
        return self._repository_address

    @repository_address.setter
    def repository_address(self, repository_address):
        r"""Sets the repository_address of this ImageScanRequestInfo.

        **参数解释**: 镜像仓地址 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param repository_address: The repository_address of this ImageScanRequestInfo.
        :type repository_address: str
        """
        self._repository_address = repository_address

    @property
    def login_user_name(self):
        r"""Gets the login_user_name of this ImageScanRequestInfo.

        **参数解释**: 镜像仓登录用户名 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The login_user_name of this ImageScanRequestInfo.
        :rtype: str
        """
        return self._login_user_name

    @login_user_name.setter
    def login_user_name(self, login_user_name):
        r"""Sets the login_user_name of this ImageScanRequestInfo.

        **参数解释**: 镜像仓登录用户名 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param login_user_name: The login_user_name of this ImageScanRequestInfo.
        :type login_user_name: str
        """
        self._login_user_name = login_user_name

    @property
    def login_password(self):
        r"""Gets the login_password of this ImageScanRequestInfo.

        **参数解释**: 镜像仓登录密码 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The login_password of this ImageScanRequestInfo.
        :rtype: str
        """
        return self._login_password

    @login_password.setter
    def login_password(self, login_password):
        r"""Sets the login_password of this ImageScanRequestInfo.

        **参数解释**: 镜像仓登录密码 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param login_password: The login_password of this ImageScanRequestInfo.
        :type login_password: str
        """
        self._login_password = login_password

    @property
    def namespace(self):
        r"""Gets the namespace of this ImageScanRequestInfo.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The namespace of this ImageScanRequestInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ImageScanRequestInfo.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param namespace: The namespace of this ImageScanRequestInfo.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, ImageScanRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
