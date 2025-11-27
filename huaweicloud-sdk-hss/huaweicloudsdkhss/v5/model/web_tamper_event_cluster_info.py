# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperEventClusterInfo:

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
        'cluster_type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'cluster_type': 'cluster_type'
    }

    def __init__(self, cluster_id=None, cluster_name=None, cluster_type=None):
        r"""WebTamperEventClusterInfo

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID **取值范围**： 字符长度1-128位 
        :type cluster_id: str
        :param cluster_name: **参数解释**： 集群名称 **取值范围**： 字符长度1-256位 
        :type cluster_name: str
        :param cluster_type: **参数解释**： 集群类型 **取值范围**： 字符长度1-128位 
        :type cluster_type: str
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._cluster_type = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_type is not None:
            self.cluster_type = cluster_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this WebTamperEventClusterInfo.

        **参数解释**： 集群ID **取值范围**： 字符长度1-128位 

        :return: The cluster_id of this WebTamperEventClusterInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this WebTamperEventClusterInfo.

        **参数解释**： 集群ID **取值范围**： 字符长度1-128位 

        :param cluster_id: The cluster_id of this WebTamperEventClusterInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this WebTamperEventClusterInfo.

        **参数解释**： 集群名称 **取值范围**： 字符长度1-256位 

        :return: The cluster_name of this WebTamperEventClusterInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this WebTamperEventClusterInfo.

        **参数解释**： 集群名称 **取值范围**： 字符长度1-256位 

        :param cluster_name: The cluster_name of this WebTamperEventClusterInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this WebTamperEventClusterInfo.

        **参数解释**： 集群类型 **取值范围**： 字符长度1-128位 

        :return: The cluster_type of this WebTamperEventClusterInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this WebTamperEventClusterInfo.

        **参数解释**： 集群类型 **取值范围**： 字符长度1-128位 

        :param cluster_type: The cluster_type of this WebTamperEventClusterInfo.
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
        if not isinstance(other, WebTamperEventClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
