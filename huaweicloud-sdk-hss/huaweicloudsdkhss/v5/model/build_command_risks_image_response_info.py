# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildCommandRisksImageResponseInfo:

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
        'image_digest': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'image_size': 'int',
        'latest_scan_time': 'int',
        'risk_detail_info': 'BuildCommandRiskDetailListResponseInfo'
    }

    attribute_map = {
        'namespace': 'namespace',
        'image_digest': 'image_digest',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'image_size': 'image_size',
        'latest_scan_time': 'latest_scan_time',
        'risk_detail_info': 'risk_detail_info'
    }

    def __init__(self, namespace=None, image_digest=None, image_id=None, image_name=None, image_version=None, image_type=None, image_size=None, latest_scan_time=None, risk_detail_info=None):
        r"""BuildCommandRisksImageResponseInfo

        The model defined in huaweicloud sdk

        :param namespace: **参数解释**: 组织名称 **取值范围**: 字符长度0-64 
        :type namespace: str
        :param image_digest: **参数解释**: 镜像digest **取值范围**: 字符长度0-128 
        :type image_digest: str
        :param image_id: **参数解释**: 镜像id **取值范围**: 字符长度0-128 
        :type image_id: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-128 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本 **取值范围**: 字符长度0-128 
        :type image_version: str
        :param image_type: **参数解释**: 镜像类型  **取值范围**:   - private_image：私有镜像   - shared_image：共享镜像   - instance_image：企业镜像   - harbor：Harbor镜像   - jfrog：Jfrog镜像   - cicd：cicd镜像
        :type image_type: str
        :param image_size: **参数解释**: 版本大小 **取值范围**: 大小0-9223372036854775807 
        :type image_size: int
        :param latest_scan_time: **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 大小0-9223372036854775807 
        :type latest_scan_time: int
        :param risk_detail_info: 
        :type risk_detail_info: :class:`huaweicloudsdkhss.v5.BuildCommandRiskDetailListResponseInfo`
        """
        
        

        self._namespace = None
        self._image_digest = None
        self._image_id = None
        self._image_name = None
        self._image_version = None
        self._image_type = None
        self._image_size = None
        self._latest_scan_time = None
        self._risk_detail_info = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if image_digest is not None:
            self.image_digest = image_digest
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        if image_size is not None:
            self.image_size = image_size
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if risk_detail_info is not None:
            self.risk_detail_info = risk_detail_info

    @property
    def namespace(self):
        r"""Gets the namespace of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-64 

        :return: The namespace of this BuildCommandRisksImageResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-64 

        :param namespace: The namespace of this BuildCommandRisksImageResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_digest(self):
        r"""Gets the image_digest of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 镜像digest **取值范围**: 字符长度0-128 

        :return: The image_digest of this BuildCommandRisksImageResponseInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 镜像digest **取值范围**: 字符长度0-128 

        :param image_digest: The image_digest of this BuildCommandRisksImageResponseInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_id(self):
        r"""Gets the image_id of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-128 

        :return: The image_id of this BuildCommandRisksImageResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-128 

        :param image_id: The image_id of this BuildCommandRisksImageResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-128 

        :return: The image_name of this BuildCommandRisksImageResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-128 

        :param image_name: The image_name of this BuildCommandRisksImageResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-128 

        :return: The image_version of this BuildCommandRisksImageResponseInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 镜像版本 **取值范围**: 字符长度0-128 

        :param image_version: The image_version of this BuildCommandRisksImageResponseInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        r"""Gets the image_type of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 镜像类型  **取值范围**:   - private_image：私有镜像   - shared_image：共享镜像   - instance_image：企业镜像   - harbor：Harbor镜像   - jfrog：Jfrog镜像   - cicd：cicd镜像

        :return: The image_type of this BuildCommandRisksImageResponseInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 镜像类型  **取值范围**:   - private_image：私有镜像   - shared_image：共享镜像   - instance_image：企业镜像   - harbor：Harbor镜像   - jfrog：Jfrog镜像   - cicd：cicd镜像

        :param image_type: The image_type of this BuildCommandRisksImageResponseInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_size(self):
        r"""Gets the image_size of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 版本大小 **取值范围**: 大小0-9223372036854775807 

        :return: The image_size of this BuildCommandRisksImageResponseInfo.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 版本大小 **取值范围**: 大小0-9223372036854775807 

        :param image_size: The image_size of this BuildCommandRisksImageResponseInfo.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 大小0-9223372036854775807 

        :return: The latest_scan_time of this BuildCommandRisksImageResponseInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this BuildCommandRisksImageResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 大小0-9223372036854775807 

        :param latest_scan_time: The latest_scan_time of this BuildCommandRisksImageResponseInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def risk_detail_info(self):
        r"""Gets the risk_detail_info of this BuildCommandRisksImageResponseInfo.

        :return: The risk_detail_info of this BuildCommandRisksImageResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.BuildCommandRiskDetailListResponseInfo`
        """
        return self._risk_detail_info

    @risk_detail_info.setter
    def risk_detail_info(self, risk_detail_info):
        r"""Sets the risk_detail_info of this BuildCommandRisksImageResponseInfo.

        :param risk_detail_info: The risk_detail_info of this BuildCommandRisksImageResponseInfo.
        :type risk_detail_info: :class:`huaweicloudsdkhss.v5.BuildCommandRiskDetailListResponseInfo`
        """
        self._risk_detail_info = risk_detail_info

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
        if not isinstance(other, BuildCommandRisksImageResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
