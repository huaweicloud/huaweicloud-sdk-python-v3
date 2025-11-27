# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_type': 'str',
        'web_app_name': 'str',
        'cluster_id': 'str',
        'host_id': 'str',
        'cluster_label_list': 'list[ClusterLabelInfo]',
        'protect_image_list': 'list[ProtectImageInfo]'
    }

    attribute_map = {
        'protect_type': 'protect_type',
        'web_app_name': 'web_app_name',
        'cluster_id': 'cluster_id',
        'host_id': 'host_id',
        'cluster_label_list': 'cluster_label_list',
        'protect_image_list': 'protect_image_list'
    }

    def __init__(self, protect_type=None, web_app_name=None, cluster_id=None, host_id=None, cluster_label_list=None, protect_image_list=None):
        r"""CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo

        The model defined in huaweicloud sdk

        :param protect_type: **参数解释**: 防护类型 **约束限制**: 不涉及 **取值范围**: - cluster：对集群下的容器进行网页防篡改防护 - host：对主机下的容器进行网页防篡改防护  **默认取值**: 不涉及 
        :type protect_type: str
        :param web_app_name: **参数解释**: 网站应用的名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type web_app_name: str
        :param cluster_id: **参数解释**: 集群id **约束限制**: protect_type值为“cluster”时有效 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type cluster_id: str
        :param host_id: **参数解释**: 主机id **约束限制**: protect_type值为“host”时有效 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param cluster_label_list: **参数解释**: 集群标签列表 **约束限制**: protect_type值为“cluster”时生效 **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 
        :type cluster_label_list: list[:class:`huaweicloudsdkhss.v5.ClusterLabelInfo`]
        :param protect_image_list: **参数解释**: 防护的镜像列表 **约束限制**: 不涉及 **取值范围**: 最少1条，最多10条 **默认取值**: 不涉及 
        :type protect_image_list: list[:class:`huaweicloudsdkhss.v5.ProtectImageInfo`]
        """
        
        

        self._protect_type = None
        self._web_app_name = None
        self._cluster_id = None
        self._host_id = None
        self._cluster_label_list = None
        self._protect_image_list = None
        self.discriminator = None

        self.protect_type = protect_type
        self.web_app_name = web_app_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if host_id is not None:
            self.host_id = host_id
        if cluster_label_list is not None:
            self.cluster_label_list = cluster_label_list
        self.protect_image_list = protect_image_list

    @property
    def protect_type(self):
        r"""Gets the protect_type of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 防护类型 **约束限制**: 不涉及 **取值范围**: - cluster：对集群下的容器进行网页防篡改防护 - host：对主机下的容器进行网页防篡改防护  **默认取值**: 不涉及 

        :return: The protect_type of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        r"""Sets the protect_type of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 防护类型 **约束限制**: 不涉及 **取值范围**: - cluster：对集群下的容器进行网页防篡改防护 - host：对主机下的容器进行网页防篡改防护  **默认取值**: 不涉及 

        :param protect_type: The protect_type of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def web_app_name(self):
        r"""Gets the web_app_name of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 网站应用的名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The web_app_name of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :rtype: str
        """
        return self._web_app_name

    @web_app_name.setter
    def web_app_name(self, web_app_name):
        r"""Sets the web_app_name of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 网站应用的名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param web_app_name: The web_app_name of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :type web_app_name: str
        """
        self._web_app_name = web_app_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 集群id **约束限制**: protect_type值为“cluster”时有效 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The cluster_id of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 集群id **约束限制**: protect_type值为“cluster”时有效 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param cluster_id: The cluster_id of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def host_id(self):
        r"""Gets the host_id of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 主机id **约束限制**: protect_type值为“host”时有效 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 主机id **约束限制**: protect_type值为“host”时有效 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def cluster_label_list(self):
        r"""Gets the cluster_label_list of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 集群标签列表 **约束限制**: protect_type值为“cluster”时生效 **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 

        :return: The cluster_label_list of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterLabelInfo`]
        """
        return self._cluster_label_list

    @cluster_label_list.setter
    def cluster_label_list(self, cluster_label_list):
        r"""Sets the cluster_label_list of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 集群标签列表 **约束限制**: protect_type值为“cluster”时生效 **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 

        :param cluster_label_list: The cluster_label_list of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :type cluster_label_list: list[:class:`huaweicloudsdkhss.v5.ClusterLabelInfo`]
        """
        self._cluster_label_list = cluster_label_list

    @property
    def protect_image_list(self):
        r"""Gets the protect_image_list of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 防护的镜像列表 **约束限制**: 不涉及 **取值范围**: 最少1条，最多10条 **默认取值**: 不涉及 

        :return: The protect_image_list of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ProtectImageInfo`]
        """
        return self._protect_image_list

    @protect_image_list.setter
    def protect_image_list(self, protect_image_list):
        r"""Sets the protect_image_list of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.

        **参数解释**: 防护的镜像列表 **约束限制**: 不涉及 **取值范围**: 最少1条，最多10条 **默认取值**: 不涉及 

        :param protect_image_list: The protect_image_list of this CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo.
        :type protect_image_list: list[:class:`huaweicloudsdkhss.v5.ProtectImageInfo`]
        """
        self._protect_image_list = protect_image_list

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
        if not isinstance(other, CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
