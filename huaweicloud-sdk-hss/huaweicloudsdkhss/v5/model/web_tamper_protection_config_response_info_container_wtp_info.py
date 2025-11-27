# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperProtectionConfigResponseInfoContainerWtpInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'web_app_name': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'protect_type': 'str',
        'cluster_info': 'WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo',
        'cluster_label_list': 'list[WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterLabelList]',
        'host_info': 'WebTamperProtectionConfigResponseInfoContainerWtpInfoHostInfo'
    }

    attribute_map = {
        'web_app_name': 'web_app_name',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'protect_type': 'protect_type',
        'cluster_info': 'cluster_info',
        'cluster_label_list': 'cluster_label_list',
        'host_info': 'host_info'
    }

    def __init__(self, web_app_name=None, image_name=None, image_version=None, image_type=None, protect_type=None, cluster_info=None, cluster_label_list=None, host_info=None):
        r"""WebTamperProtectionConfigResponseInfoContainerWtpInfo

        The model defined in huaweicloud sdk

        :param web_app_name: **参数解释**： 网站应用名称 **取值范围**： 字符长度1-128位 
        :type web_app_name: str
        :param image_name: **参数解释**： 镜像名称 **取值范围**： 字符长度1-512位 
        :type image_name: str
        :param image_version: **参数解释**： 镜像版本 **取值范围**： 字符长度1-64位 
        :type image_version: str
        :param image_type: **参数解释**： 镜像类型 **取值范围**： - registry 仓库镜像 - local 本地镜像 - custom 自定义镜像 
        :type image_type: str
        :param protect_type: **参数解释**: 防护类型 **取值范围**: - cluster：对集群下的容器进行网页防篡改防护 - host：对主机下的容器进行网页防篡改防护 
        :type protect_type: str
        :param cluster_info: 
        :type cluster_info: :class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo`
        :param cluster_label_list: **参数解释**: 集群标签列表 **取值范围**: 最少0条，最多10条 
        :type cluster_label_list: list[:class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterLabelList`]
        :param host_info: 
        :type host_info: :class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfoHostInfo`
        """
        
        

        self._web_app_name = None
        self._image_name = None
        self._image_version = None
        self._image_type = None
        self._protect_type = None
        self._cluster_info = None
        self._cluster_label_list = None
        self._host_info = None
        self.discriminator = None

        if web_app_name is not None:
            self.web_app_name = web_app_name
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        if protect_type is not None:
            self.protect_type = protect_type
        if cluster_info is not None:
            self.cluster_info = cluster_info
        if cluster_label_list is not None:
            self.cluster_label_list = cluster_label_list
        if host_info is not None:
            self.host_info = host_info

    @property
    def web_app_name(self):
        r"""Gets the web_app_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**： 网站应用名称 **取值范围**： 字符长度1-128位 

        :return: The web_app_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :rtype: str
        """
        return self._web_app_name

    @web_app_name.setter
    def web_app_name(self, web_app_name):
        r"""Sets the web_app_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**： 网站应用名称 **取值范围**： 字符长度1-128位 

        :param web_app_name: The web_app_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :type web_app_name: str
        """
        self._web_app_name = web_app_name

    @property
    def image_name(self):
        r"""Gets the image_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**： 镜像名称 **取值范围**： 字符长度1-512位 

        :return: The image_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**： 镜像名称 **取值范围**： 字符长度1-512位 

        :param image_name: The image_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**： 镜像版本 **取值范围**： 字符长度1-64位 

        :return: The image_version of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**： 镜像版本 **取值范围**： 字符长度1-64位 

        :param image_version: The image_version of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        r"""Gets the image_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**： 镜像类型 **取值范围**： - registry 仓库镜像 - local 本地镜像 - custom 自定义镜像 

        :return: The image_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**： 镜像类型 **取值范围**： - registry 仓库镜像 - local 本地镜像 - custom 自定义镜像 

        :param image_type: The image_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def protect_type(self):
        r"""Gets the protect_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**: 防护类型 **取值范围**: - cluster：对集群下的容器进行网页防篡改防护 - host：对主机下的容器进行网页防篡改防护 

        :return: The protect_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        r"""Sets the protect_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**: 防护类型 **取值范围**: - cluster：对集群下的容器进行网页防篡改防护 - host：对主机下的容器进行网页防篡改防护 

        :param protect_type: The protect_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def cluster_info(self):
        r"""Gets the cluster_info of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        :return: The cluster_info of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo`
        """
        return self._cluster_info

    @cluster_info.setter
    def cluster_info(self, cluster_info):
        r"""Sets the cluster_info of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        :param cluster_info: The cluster_info of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :type cluster_info: :class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo`
        """
        self._cluster_info = cluster_info

    @property
    def cluster_label_list(self):
        r"""Gets the cluster_label_list of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**: 集群标签列表 **取值范围**: 最少0条，最多10条 

        :return: The cluster_label_list of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterLabelList`]
        """
        return self._cluster_label_list

    @cluster_label_list.setter
    def cluster_label_list(self, cluster_label_list):
        r"""Sets the cluster_label_list of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        **参数解释**: 集群标签列表 **取值范围**: 最少0条，最多10条 

        :param cluster_label_list: The cluster_label_list of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :type cluster_label_list: list[:class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterLabelList`]
        """
        self._cluster_label_list = cluster_label_list

    @property
    def host_info(self):
        r"""Gets the host_info of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        :return: The host_info of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfoHostInfo`
        """
        return self._host_info

    @host_info.setter
    def host_info(self, host_info):
        r"""Sets the host_info of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.

        :param host_info: The host_info of this WebTamperProtectionConfigResponseInfoContainerWtpInfo.
        :type host_info: :class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfoHostInfo`
        """
        self._host_info = host_info

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
        if not isinstance(other, WebTamperProtectionConfigResponseInfoContainerWtpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
