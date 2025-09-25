# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateImagesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'image_id': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'namespace': 'str',
        'image_digest': 'str',
        'scan_status': 'str',
        'vul_num': 'int',
        'unsafe_setting_num': 'int',
        'malicious_file_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'namespace': 'namespace',
        'image_digest': 'image_digest',
        'scan_status': 'scan_status',
        'vul_num': 'vul_num',
        'unsafe_setting_num': 'unsafe_setting_num',
        'malicious_file_num': 'malicious_file_num'
    }

    def __init__(self, id=None, image_id=None, image_name=None, image_version=None, image_type=None, namespace=None, image_digest=None, scan_status=None, vul_num=None, unsafe_setting_num=None, malicious_file_num=None):
        r"""AssociateImagesInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**: id **取值范围**: 最小值0，最大值9223372036854775807 
        :type id: int
        :param image_id: **参数解释**: 镜像id **取值范围**: 字符长度0-64位 
        :type image_id: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-128位 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 
        :type image_version: str
        :param image_type: **参数解释**: 镜像类型 **取值范围**: - private_image：SWR私有镜像。 - shared_image：SWR共享镜像。 - instance_image：SWR企业版镜像。 - harbor：Harbor仓库镜像。 - jfrog：Jfrog镜像。 
        :type image_type: str
        :param namespace: **参数解释**: 组织名称 **取值范围**: 字符长度0-64位 
        :type namespace: str
        :param image_digest: **参数解释**: 镜像digest **取值范围**: 字符长度0-128位 
        :type image_digest: str
        :param scan_status: **参数解释**： 扫描状态 **取值范围**： - unscan：未扫描。 - success：扫描完成。 - scanning：正在扫描。 - failed：扫描失败。 - download_failed：下载失败。 - image_oversized：镜像超大。 - waiting_for_scan：等待扫描。 
        :type scan_status: str
        :param vul_num: **参数解释**: 漏洞个数 **取值范围**: 取值0-2147483647 
        :type vul_num: int
        :param unsafe_setting_num: **参数解释**: 基线扫描未通过数 **取值范围**: 取值0-2147483647 
        :type unsafe_setting_num: int
        :param malicious_file_num: **参数解释**: 恶意文件数 **取值范围**: 取值0-2147483647 
        :type malicious_file_num: int
        """
        
        

        self._id = None
        self._image_id = None
        self._image_name = None
        self._image_version = None
        self._image_type = None
        self._namespace = None
        self._image_digest = None
        self._scan_status = None
        self._vul_num = None
        self._unsafe_setting_num = None
        self._malicious_file_num = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        if namespace is not None:
            self.namespace = namespace
        if image_digest is not None:
            self.image_digest = image_digest
        if scan_status is not None:
            self.scan_status = scan_status
        if vul_num is not None:
            self.vul_num = vul_num
        if unsafe_setting_num is not None:
            self.unsafe_setting_num = unsafe_setting_num
        if malicious_file_num is not None:
            self.malicious_file_num = malicious_file_num

    @property
    def id(self):
        r"""Gets the id of this AssociateImagesInfo.

        **参数解释**: id **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The id of this AssociateImagesInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AssociateImagesInfo.

        **参数解释**: id **取值范围**: 最小值0，最大值9223372036854775807 

        :param id: The id of this AssociateImagesInfo.
        :type id: int
        """
        self._id = id

    @property
    def image_id(self):
        r"""Gets the image_id of this AssociateImagesInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-64位 

        :return: The image_id of this AssociateImagesInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this AssociateImagesInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-64位 

        :param image_id: The image_id of this AssociateImagesInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this AssociateImagesInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-128位 

        :return: The image_name of this AssociateImagesInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this AssociateImagesInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-128位 

        :param image_name: The image_name of this AssociateImagesInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this AssociateImagesInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 

        :return: The image_version of this AssociateImagesInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this AssociateImagesInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-64位 

        :param image_version: The image_version of this AssociateImagesInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        r"""Gets the image_type of this AssociateImagesInfo.

        **参数解释**: 镜像类型 **取值范围**: - private_image：SWR私有镜像。 - shared_image：SWR共享镜像。 - instance_image：SWR企业版镜像。 - harbor：Harbor仓库镜像。 - jfrog：Jfrog镜像。 

        :return: The image_type of this AssociateImagesInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this AssociateImagesInfo.

        **参数解释**: 镜像类型 **取值范围**: - private_image：SWR私有镜像。 - shared_image：SWR共享镜像。 - instance_image：SWR企业版镜像。 - harbor：Harbor仓库镜像。 - jfrog：Jfrog镜像。 

        :param image_type: The image_type of this AssociateImagesInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def namespace(self):
        r"""Gets the namespace of this AssociateImagesInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-64位 

        :return: The namespace of this AssociateImagesInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this AssociateImagesInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-64位 

        :param namespace: The namespace of this AssociateImagesInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_digest(self):
        r"""Gets the image_digest of this AssociateImagesInfo.

        **参数解释**: 镜像digest **取值范围**: 字符长度0-128位 

        :return: The image_digest of this AssociateImagesInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this AssociateImagesInfo.

        **参数解释**: 镜像digest **取值范围**: 字符长度0-128位 

        :param image_digest: The image_digest of this AssociateImagesInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def scan_status(self):
        r"""Gets the scan_status of this AssociateImagesInfo.

        **参数解释**： 扫描状态 **取值范围**： - unscan：未扫描。 - success：扫描完成。 - scanning：正在扫描。 - failed：扫描失败。 - download_failed：下载失败。 - image_oversized：镜像超大。 - waiting_for_scan：等待扫描。 

        :return: The scan_status of this AssociateImagesInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this AssociateImagesInfo.

        **参数解释**： 扫描状态 **取值范围**： - unscan：未扫描。 - success：扫描完成。 - scanning：正在扫描。 - failed：扫描失败。 - download_failed：下载失败。 - image_oversized：镜像超大。 - waiting_for_scan：等待扫描。 

        :param scan_status: The scan_status of this AssociateImagesInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def vul_num(self):
        r"""Gets the vul_num of this AssociateImagesInfo.

        **参数解释**: 漏洞个数 **取值范围**: 取值0-2147483647 

        :return: The vul_num of this AssociateImagesInfo.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this AssociateImagesInfo.

        **参数解释**: 漏洞个数 **取值范围**: 取值0-2147483647 

        :param vul_num: The vul_num of this AssociateImagesInfo.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def unsafe_setting_num(self):
        r"""Gets the unsafe_setting_num of this AssociateImagesInfo.

        **参数解释**: 基线扫描未通过数 **取值范围**: 取值0-2147483647 

        :return: The unsafe_setting_num of this AssociateImagesInfo.
        :rtype: int
        """
        return self._unsafe_setting_num

    @unsafe_setting_num.setter
    def unsafe_setting_num(self, unsafe_setting_num):
        r"""Sets the unsafe_setting_num of this AssociateImagesInfo.

        **参数解释**: 基线扫描未通过数 **取值范围**: 取值0-2147483647 

        :param unsafe_setting_num: The unsafe_setting_num of this AssociateImagesInfo.
        :type unsafe_setting_num: int
        """
        self._unsafe_setting_num = unsafe_setting_num

    @property
    def malicious_file_num(self):
        r"""Gets the malicious_file_num of this AssociateImagesInfo.

        **参数解释**: 恶意文件数 **取值范围**: 取值0-2147483647 

        :return: The malicious_file_num of this AssociateImagesInfo.
        :rtype: int
        """
        return self._malicious_file_num

    @malicious_file_num.setter
    def malicious_file_num(self, malicious_file_num):
        r"""Sets the malicious_file_num of this AssociateImagesInfo.

        **参数解释**: 恶意文件数 **取值范围**: 取值0-2147483647 

        :param malicious_file_num: The malicious_file_num of this AssociateImagesInfo.
        :type malicious_file_num: int
        """
        self._malicious_file_num = malicious_file_num

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
        if not isinstance(other, AssociateImagesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
