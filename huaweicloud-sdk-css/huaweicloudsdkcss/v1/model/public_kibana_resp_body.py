# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicKibanaRespBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_size': 'int',
        'elb_white_list_resp': 'KibanaElbWhiteListResp',
        'public_kibana_ip': 'str',
        'bandwidth_resource_id': 'str'
    }

    attribute_map = {
        'eip_size': 'eipSize',
        'elb_white_list_resp': 'elbWhiteListResp',
        'public_kibana_ip': 'publicKibanaIp',
        'bandwidth_resource_id': 'bandwidthResourceId'
    }

    def __init__(self, eip_size=None, elb_white_list_resp=None, public_kibana_ip=None, bandwidth_resource_id=None):
        r"""PublicKibanaRespBody

        The model defined in huaweicloud sdk

        :param eip_size: 带宽大小。单位：Mbit/s
        :type eip_size: int
        :param elb_white_list_resp: 
        :type elb_white_list_resp: :class:`huaweicloudsdkcss.v1.KibanaElbWhiteListResp`
        :param public_kibana_ip: kibana访问IP。
        :type public_kibana_ip: str
        :param bandwidth_resource_id: 当前kibana公网对应的资源Id。
        :type bandwidth_resource_id: str
        """
        
        

        self._eip_size = None
        self._elb_white_list_resp = None
        self._public_kibana_ip = None
        self._bandwidth_resource_id = None
        self.discriminator = None

        if eip_size is not None:
            self.eip_size = eip_size
        if elb_white_list_resp is not None:
            self.elb_white_list_resp = elb_white_list_resp
        if public_kibana_ip is not None:
            self.public_kibana_ip = public_kibana_ip
        if bandwidth_resource_id is not None:
            self.bandwidth_resource_id = bandwidth_resource_id

    @property
    def eip_size(self):
        r"""Gets the eip_size of this PublicKibanaRespBody.

        带宽大小。单位：Mbit/s

        :return: The eip_size of this PublicKibanaRespBody.
        :rtype: int
        """
        return self._eip_size

    @eip_size.setter
    def eip_size(self, eip_size):
        r"""Sets the eip_size of this PublicKibanaRespBody.

        带宽大小。单位：Mbit/s

        :param eip_size: The eip_size of this PublicKibanaRespBody.
        :type eip_size: int
        """
        self._eip_size = eip_size

    @property
    def elb_white_list_resp(self):
        r"""Gets the elb_white_list_resp of this PublicKibanaRespBody.

        :return: The elb_white_list_resp of this PublicKibanaRespBody.
        :rtype: :class:`huaweicloudsdkcss.v1.KibanaElbWhiteListResp`
        """
        return self._elb_white_list_resp

    @elb_white_list_resp.setter
    def elb_white_list_resp(self, elb_white_list_resp):
        r"""Sets the elb_white_list_resp of this PublicKibanaRespBody.

        :param elb_white_list_resp: The elb_white_list_resp of this PublicKibanaRespBody.
        :type elb_white_list_resp: :class:`huaweicloudsdkcss.v1.KibanaElbWhiteListResp`
        """
        self._elb_white_list_resp = elb_white_list_resp

    @property
    def public_kibana_ip(self):
        r"""Gets the public_kibana_ip of this PublicKibanaRespBody.

        kibana访问IP。

        :return: The public_kibana_ip of this PublicKibanaRespBody.
        :rtype: str
        """
        return self._public_kibana_ip

    @public_kibana_ip.setter
    def public_kibana_ip(self, public_kibana_ip):
        r"""Sets the public_kibana_ip of this PublicKibanaRespBody.

        kibana访问IP。

        :param public_kibana_ip: The public_kibana_ip of this PublicKibanaRespBody.
        :type public_kibana_ip: str
        """
        self._public_kibana_ip = public_kibana_ip

    @property
    def bandwidth_resource_id(self):
        r"""Gets the bandwidth_resource_id of this PublicKibanaRespBody.

        当前kibana公网对应的资源Id。

        :return: The bandwidth_resource_id of this PublicKibanaRespBody.
        :rtype: str
        """
        return self._bandwidth_resource_id

    @bandwidth_resource_id.setter
    def bandwidth_resource_id(self, bandwidth_resource_id):
        r"""Sets the bandwidth_resource_id of this PublicKibanaRespBody.

        当前kibana公网对应的资源Id。

        :param bandwidth_resource_id: The bandwidth_resource_id of this PublicKibanaRespBody.
        :type bandwidth_resource_id: str
        """
        self._bandwidth_resource_id = bandwidth_resource_id

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
        if not isinstance(other, PublicKibanaRespBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
