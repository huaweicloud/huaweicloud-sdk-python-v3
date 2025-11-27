# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'cluster_name': 'str',
        'cluster_version': 'str',
        'cluster_type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'cluster_version': 'cluster_version',
        'cluster_type': 'cluster_type'
    }

    def __init__(self, cluster_id=None, cluster_name=None, cluster_version=None, cluster_type=None):
        r"""WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID **取值范围**： 字符长度0-128位 
        :type cluster_id: str
        :param cluster_name: **参数解释**： 集群名称 **取值范围**： 字符长度0-256位 
        :type cluster_name: str
        :param cluster_version: **参数解释**： 集群版本 **取值范围**： 字符长度0-256位 
        :type cluster_version: str
        :param cluster_type: **参数解释**： 集群类型 **取值范围**： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群 
        :type cluster_type: str
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._cluster_version = None
        self._cluster_type = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_version is not None:
            self.cluster_version = cluster_version
        if cluster_type is not None:
            self.cluster_type = cluster_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.

        **参数解释**： 集群ID **取值范围**： 字符长度0-128位 

        :return: The cluster_id of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.

        **参数解释**： 集群ID **取值范围**： 字符长度0-128位 

        :param cluster_id: The cluster_id of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.

        **参数解释**： 集群名称 **取值范围**： 字符长度0-256位 

        :return: The cluster_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.

        **参数解释**： 集群名称 **取值范围**： 字符长度0-256位 

        :param cluster_name: The cluster_name of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_version(self):
        r"""Gets the cluster_version of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.

        **参数解释**： 集群版本 **取值范围**： 字符长度0-256位 

        :return: The cluster_version of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        r"""Sets the cluster_version of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.

        **参数解释**： 集群版本 **取值范围**： 字符长度0-256位 

        :param cluster_version: The cluster_version of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.
        :type cluster_version: str
        """
        self._cluster_version = cluster_version

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.

        **参数解释**： 集群类型 **取值范围**： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群 

        :return: The cluster_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.

        **参数解释**： 集群类型 **取值范围**： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群 

        :param cluster_type: The cluster_type of this WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

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
        if not isinstance(other, WebTamperProtectionConfigResponseInfoContainerWtpInfoClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
