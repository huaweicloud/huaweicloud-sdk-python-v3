# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCicdConfigurationCommandRequestBody:

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
        'cicd_id': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'is_blocking': 'bool',
        'repository_address': 'str',
        'login_user_name': 'str',
        'login_password': 'str',
        'namespace': 'str',
        'is_image_scan': 'bool',
        'image_scan_info': 'ImageScanRequestInfo',
        'is_iac_scan': 'bool',
        'iac_scan_info': 'IacScanRequestInfo'
    }

    attribute_map = {
        'scan_type': 'scan_type',
        'cicd_id': 'cicd_id',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'is_blocking': 'is_blocking',
        'repository_address': 'repository_address',
        'login_user_name': 'login_user_name',
        'login_password': 'login_password',
        'namespace': 'namespace',
        'is_image_scan': 'is_image_scan',
        'image_scan_info': 'image_scan_info',
        'is_iac_scan': 'is_iac_scan',
        'iac_scan_info': 'iac_scan_info'
    }

    def __init__(self, scan_type=None, cicd_id=None, image_name=None, image_version=None, is_blocking=None, repository_address=None, login_user_name=None, login_password=None, namespace=None, is_image_scan=None, image_scan_info=None, is_iac_scan=None, iac_scan_info=None):
        r"""CreateCicdConfigurationCommandRequestBody

        The model defined in huaweicloud sdk

        :param scan_type: **参数解释**： 扫描类型 **约束限制**: 不涉及 **取值范围**: - local_image：本地镜像，镜像扫描参数 - remote_image：远程镜像仓，镜像扫描参数 - local_directory：本地目录，iac扫描参数 - remote_address：https远程地址 - git_repository_address：git仓库地址  **默认取值**: 不涉及 
        :type scan_type: str
        :param cicd_id: **参数解释**： cicd标识 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type cicd_id: str
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
        :param is_image_scan: **参数解释**: 是否进行镜像扫描 **约束限制**: 不涉及 **取值范围**:   - true：镜像扫描。   - false：不进行镜像扫描。  **默认取值**: 不涉及 
        :type is_image_scan: bool
        :param image_scan_info: 
        :type image_scan_info: :class:`huaweicloudsdkhss.v5.ImageScanRequestInfo`
        :param is_iac_scan: **参数解释**: 是否进行iac扫描 **约束限制**: 不涉及 **取值范围**:   - true：iac扫描。   - false：不进行iac扫描。  **默认取值**: 不涉及 
        :type is_iac_scan: bool
        :param iac_scan_info: 
        :type iac_scan_info: :class:`huaweicloudsdkhss.v5.IacScanRequestInfo`
        """
        
        

        self._scan_type = None
        self._cicd_id = None
        self._image_name = None
        self._image_version = None
        self._is_blocking = None
        self._repository_address = None
        self._login_user_name = None
        self._login_password = None
        self._namespace = None
        self._is_image_scan = None
        self._image_scan_info = None
        self._is_iac_scan = None
        self._iac_scan_info = None
        self.discriminator = None

        if scan_type is not None:
            self.scan_type = scan_type
        self.cicd_id = cicd_id
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
        if is_image_scan is not None:
            self.is_image_scan = is_image_scan
        if image_scan_info is not None:
            self.image_scan_info = image_scan_info
        if is_iac_scan is not None:
            self.is_iac_scan = is_iac_scan
        if iac_scan_info is not None:
            self.iac_scan_info = iac_scan_info

    @property
    def scan_type(self):
        r"""Gets the scan_type of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**： 扫描类型 **约束限制**: 不涉及 **取值范围**: - local_image：本地镜像，镜像扫描参数 - remote_image：远程镜像仓，镜像扫描参数 - local_directory：本地目录，iac扫描参数 - remote_address：https远程地址 - git_repository_address：git仓库地址  **默认取值**: 不涉及 

        :return: The scan_type of this CreateCicdConfigurationCommandRequestBody.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**： 扫描类型 **约束限制**: 不涉及 **取值范围**: - local_image：本地镜像，镜像扫描参数 - remote_image：远程镜像仓，镜像扫描参数 - local_directory：本地目录，iac扫描参数 - remote_address：https远程地址 - git_repository_address：git仓库地址  **默认取值**: 不涉及 

        :param scan_type: The scan_type of this CreateCicdConfigurationCommandRequestBody.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def cicd_id(self):
        r"""Gets the cicd_id of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**： cicd标识 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The cicd_id of this CreateCicdConfigurationCommandRequestBody.
        :rtype: str
        """
        return self._cicd_id

    @cicd_id.setter
    def cicd_id(self, cicd_id):
        r"""Sets the cicd_id of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**： cicd标识 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param cicd_id: The cicd_id of this CreateCicdConfigurationCommandRequestBody.
        :type cicd_id: str
        """
        self._cicd_id = cicd_id

    @property
    def image_name(self):
        r"""Gets the image_name of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The image_name of this CreateCicdConfigurationCommandRequestBody.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param image_name: The image_name of this CreateCicdConfigurationCommandRequestBody.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The image_version of this CreateCicdConfigurationCommandRequestBody.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param image_version: The image_version of this CreateCicdConfigurationCommandRequestBody.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def is_blocking(self):
        r"""Gets the is_blocking of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 流水线是否阻断 **约束限制**: 不涉及 **取值范围**:   - true：流水线被阻断。   - false：流水线未阻断。  **默认取值**: 不涉及 

        :return: The is_blocking of this CreateCicdConfigurationCommandRequestBody.
        :rtype: bool
        """
        return self._is_blocking

    @is_blocking.setter
    def is_blocking(self, is_blocking):
        r"""Sets the is_blocking of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 流水线是否阻断 **约束限制**: 不涉及 **取值范围**:   - true：流水线被阻断。   - false：流水线未阻断。  **默认取值**: 不涉及 

        :param is_blocking: The is_blocking of this CreateCicdConfigurationCommandRequestBody.
        :type is_blocking: bool
        """
        self._is_blocking = is_blocking

    @property
    def repository_address(self):
        r"""Gets the repository_address of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 镜像仓地址 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The repository_address of this CreateCicdConfigurationCommandRequestBody.
        :rtype: str
        """
        return self._repository_address

    @repository_address.setter
    def repository_address(self, repository_address):
        r"""Sets the repository_address of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 镜像仓地址 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param repository_address: The repository_address of this CreateCicdConfigurationCommandRequestBody.
        :type repository_address: str
        """
        self._repository_address = repository_address

    @property
    def login_user_name(self):
        r"""Gets the login_user_name of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 镜像仓登录用户名 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The login_user_name of this CreateCicdConfigurationCommandRequestBody.
        :rtype: str
        """
        return self._login_user_name

    @login_user_name.setter
    def login_user_name(self, login_user_name):
        r"""Sets the login_user_name of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 镜像仓登录用户名 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param login_user_name: The login_user_name of this CreateCicdConfigurationCommandRequestBody.
        :type login_user_name: str
        """
        self._login_user_name = login_user_name

    @property
    def login_password(self):
        r"""Gets the login_password of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 镜像仓登录密码 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The login_password of this CreateCicdConfigurationCommandRequestBody.
        :rtype: str
        """
        return self._login_password

    @login_password.setter
    def login_password(self, login_password):
        r"""Sets the login_password of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 镜像仓登录密码 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param login_password: The login_password of this CreateCicdConfigurationCommandRequestBody.
        :type login_password: str
        """
        self._login_password = login_password

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The namespace of this CreateCicdConfigurationCommandRequestBody.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param namespace: The namespace of this CreateCicdConfigurationCommandRequestBody.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def is_image_scan(self):
        r"""Gets the is_image_scan of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 是否进行镜像扫描 **约束限制**: 不涉及 **取值范围**:   - true：镜像扫描。   - false：不进行镜像扫描。  **默认取值**: 不涉及 

        :return: The is_image_scan of this CreateCicdConfigurationCommandRequestBody.
        :rtype: bool
        """
        return self._is_image_scan

    @is_image_scan.setter
    def is_image_scan(self, is_image_scan):
        r"""Sets the is_image_scan of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 是否进行镜像扫描 **约束限制**: 不涉及 **取值范围**:   - true：镜像扫描。   - false：不进行镜像扫描。  **默认取值**: 不涉及 

        :param is_image_scan: The is_image_scan of this CreateCicdConfigurationCommandRequestBody.
        :type is_image_scan: bool
        """
        self._is_image_scan = is_image_scan

    @property
    def image_scan_info(self):
        r"""Gets the image_scan_info of this CreateCicdConfigurationCommandRequestBody.

        :return: The image_scan_info of this CreateCicdConfigurationCommandRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.ImageScanRequestInfo`
        """
        return self._image_scan_info

    @image_scan_info.setter
    def image_scan_info(self, image_scan_info):
        r"""Sets the image_scan_info of this CreateCicdConfigurationCommandRequestBody.

        :param image_scan_info: The image_scan_info of this CreateCicdConfigurationCommandRequestBody.
        :type image_scan_info: :class:`huaweicloudsdkhss.v5.ImageScanRequestInfo`
        """
        self._image_scan_info = image_scan_info

    @property
    def is_iac_scan(self):
        r"""Gets the is_iac_scan of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 是否进行iac扫描 **约束限制**: 不涉及 **取值范围**:   - true：iac扫描。   - false：不进行iac扫描。  **默认取值**: 不涉及 

        :return: The is_iac_scan of this CreateCicdConfigurationCommandRequestBody.
        :rtype: bool
        """
        return self._is_iac_scan

    @is_iac_scan.setter
    def is_iac_scan(self, is_iac_scan):
        r"""Sets the is_iac_scan of this CreateCicdConfigurationCommandRequestBody.

        **参数解释**: 是否进行iac扫描 **约束限制**: 不涉及 **取值范围**:   - true：iac扫描。   - false：不进行iac扫描。  **默认取值**: 不涉及 

        :param is_iac_scan: The is_iac_scan of this CreateCicdConfigurationCommandRequestBody.
        :type is_iac_scan: bool
        """
        self._is_iac_scan = is_iac_scan

    @property
    def iac_scan_info(self):
        r"""Gets the iac_scan_info of this CreateCicdConfigurationCommandRequestBody.

        :return: The iac_scan_info of this CreateCicdConfigurationCommandRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.IacScanRequestInfo`
        """
        return self._iac_scan_info

    @iac_scan_info.setter
    def iac_scan_info(self, iac_scan_info):
        r"""Sets the iac_scan_info of this CreateCicdConfigurationCommandRequestBody.

        :param iac_scan_info: The iac_scan_info of this CreateCicdConfigurationCommandRequestBody.
        :type iac_scan_info: :class:`huaweicloudsdkhss.v5.IacScanRequestInfo`
        """
        self._iac_scan_info = iac_scan_info

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
        if not isinstance(other, CreateCicdConfigurationCommandRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
