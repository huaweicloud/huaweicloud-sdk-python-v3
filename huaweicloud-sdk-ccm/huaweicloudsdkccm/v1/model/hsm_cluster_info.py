# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HsmClusterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hsm_project': 'str',
        'hsm_cluster_id': 'str',
        'hsm_ca_cert': 'str'
    }

    attribute_map = {
        'hsm_project': 'hsm_project',
        'hsm_cluster_id': 'hsm_cluster_id',
        'hsm_ca_cert': 'hsm_ca_cert'
    }

    def __init__(self, hsm_project=None, hsm_cluster_id=None, hsm_ca_cert=None):
        r"""HsmClusterInfo

        The model defined in huaweicloud sdk

        :param hsm_project: 项目信息
        :type hsm_project: str
        :param hsm_cluster_id: 加密机集群标识符
        :type hsm_cluster_id: str
        :param hsm_ca_cert: pem格式证书base64之后的字符串
        :type hsm_ca_cert: str
        """
        
        

        self._hsm_project = None
        self._hsm_cluster_id = None
        self._hsm_ca_cert = None
        self.discriminator = None

        self.hsm_project = hsm_project
        self.hsm_cluster_id = hsm_cluster_id
        self.hsm_ca_cert = hsm_ca_cert

    @property
    def hsm_project(self):
        r"""Gets the hsm_project of this HsmClusterInfo.

        项目信息

        :return: The hsm_project of this HsmClusterInfo.
        :rtype: str
        """
        return self._hsm_project

    @hsm_project.setter
    def hsm_project(self, hsm_project):
        r"""Sets the hsm_project of this HsmClusterInfo.

        项目信息

        :param hsm_project: The hsm_project of this HsmClusterInfo.
        :type hsm_project: str
        """
        self._hsm_project = hsm_project

    @property
    def hsm_cluster_id(self):
        r"""Gets the hsm_cluster_id of this HsmClusterInfo.

        加密机集群标识符

        :return: The hsm_cluster_id of this HsmClusterInfo.
        :rtype: str
        """
        return self._hsm_cluster_id

    @hsm_cluster_id.setter
    def hsm_cluster_id(self, hsm_cluster_id):
        r"""Sets the hsm_cluster_id of this HsmClusterInfo.

        加密机集群标识符

        :param hsm_cluster_id: The hsm_cluster_id of this HsmClusterInfo.
        :type hsm_cluster_id: str
        """
        self._hsm_cluster_id = hsm_cluster_id

    @property
    def hsm_ca_cert(self):
        r"""Gets the hsm_ca_cert of this HsmClusterInfo.

        pem格式证书base64之后的字符串

        :return: The hsm_ca_cert of this HsmClusterInfo.
        :rtype: str
        """
        return self._hsm_ca_cert

    @hsm_ca_cert.setter
    def hsm_ca_cert(self, hsm_ca_cert):
        r"""Sets the hsm_ca_cert of this HsmClusterInfo.

        pem格式证书base64之后的字符串

        :param hsm_ca_cert: The hsm_ca_cert of this HsmClusterInfo.
        :type hsm_ca_cert: str
        """
        self._hsm_ca_cert = hsm_ca_cert

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
        if not isinstance(other, HsmClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
