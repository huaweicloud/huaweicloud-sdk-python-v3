# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterAccessInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clusterid': 'str',
        'vpcendpoint': 'str',
        'region': 'str'
    }

    attribute_map = {
        'clusterid': 'clusterid',
        'vpcendpoint': 'vpcendpoint',
        'region': 'region'
    }

    def __init__(self, clusterid=None, vpcendpoint=None, region=None):
        r"""ShowClusterAccessInfoRequest

        The model defined in huaweicloud sdk

        :param clusterid: 集群ID
        :type clusterid: str
        :param vpcendpoint: VPC终端节点的IP地址。私网接入的集群必填，且必须是打通线下集群的VPC终端节点。  创建VPC终端节点及查询IP地址的方法请参见[创建终端节点](https://support.huaweicloud.com/usermanual-ucs/ucs_01_0336.html#section2)。
        :type vpcendpoint: str
        :param region: 接入region，私网接入的集群必填
        :type region: str
        """
        
        

        self._clusterid = None
        self._vpcendpoint = None
        self._region = None
        self.discriminator = None

        self.clusterid = clusterid
        if vpcendpoint is not None:
            self.vpcendpoint = vpcendpoint
        if region is not None:
            self.region = region

    @property
    def clusterid(self):
        r"""Gets the clusterid of this ShowClusterAccessInfoRequest.

        集群ID

        :return: The clusterid of this ShowClusterAccessInfoRequest.
        :rtype: str
        """
        return self._clusterid

    @clusterid.setter
    def clusterid(self, clusterid):
        r"""Sets the clusterid of this ShowClusterAccessInfoRequest.

        集群ID

        :param clusterid: The clusterid of this ShowClusterAccessInfoRequest.
        :type clusterid: str
        """
        self._clusterid = clusterid

    @property
    def vpcendpoint(self):
        r"""Gets the vpcendpoint of this ShowClusterAccessInfoRequest.

        VPC终端节点的IP地址。私网接入的集群必填，且必须是打通线下集群的VPC终端节点。  创建VPC终端节点及查询IP地址的方法请参见[创建终端节点](https://support.huaweicloud.com/usermanual-ucs/ucs_01_0336.html#section2)。

        :return: The vpcendpoint of this ShowClusterAccessInfoRequest.
        :rtype: str
        """
        return self._vpcendpoint

    @vpcendpoint.setter
    def vpcendpoint(self, vpcendpoint):
        r"""Sets the vpcendpoint of this ShowClusterAccessInfoRequest.

        VPC终端节点的IP地址。私网接入的集群必填，且必须是打通线下集群的VPC终端节点。  创建VPC终端节点及查询IP地址的方法请参见[创建终端节点](https://support.huaweicloud.com/usermanual-ucs/ucs_01_0336.html#section2)。

        :param vpcendpoint: The vpcendpoint of this ShowClusterAccessInfoRequest.
        :type vpcendpoint: str
        """
        self._vpcendpoint = vpcendpoint

    @property
    def region(self):
        r"""Gets the region of this ShowClusterAccessInfoRequest.

        接入region，私网接入的集群必填

        :return: The region of this ShowClusterAccessInfoRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowClusterAccessInfoRequest.

        接入region，私网接入的集群必填

        :param region: The region of this ShowClusterAccessInfoRequest.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, ShowClusterAccessInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
