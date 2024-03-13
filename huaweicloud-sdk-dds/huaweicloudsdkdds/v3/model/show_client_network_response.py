# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClientNetworkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'client_network_ranges': 'list[str]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'client_network_ranges': 'client_network_ranges'
    }

    def __init__(self, instance_id=None, client_network_ranges=None):
        """ShowClientNetworkResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，可以调用“[查询实例列表和详情](x-wc://file&#x3D;zh-cn_topic_0000001369935045.xml)”接口获取。如果未申请实例，可以调用“[创建实例](x-wc://file&#x3D;zh-cn_topic_0000001369734929.xml)”接口创建。
        :type instance_id: str
        :param client_network_ranges: 客户端所在网段。 &gt; - [跨网段访问配置只有在客户端与副本集实例部署在不同网段的情况下才允许配置，例如访问副本集的客户端所在网段为192.168.0.0/16，副本集所在的网段为172.16.0.0/24，则需要添加跨网段配置192.168.0.0/16才能正常访问。只有副本集有该功能。](tag:ccs,cmcc,ctc,dt,dt_test,fcs,fcs_dt,g42,hic,hk_g42,hk_sbc,hc,hws_ocb,hws_sbc,ocb,tlf,tm,hk,hws_eu)
        :type client_network_ranges: list[str]
        """
        
        super(ShowClientNetworkResponse, self).__init__()

        self._instance_id = None
        self._client_network_ranges = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if client_network_ranges is not None:
            self.client_network_ranges = client_network_ranges

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowClientNetworkResponse.

        实例ID，可以调用“[查询实例列表和详情](x-wc://file=zh-cn_topic_0000001369935045.xml)”接口获取。如果未申请实例，可以调用“[创建实例](x-wc://file=zh-cn_topic_0000001369734929.xml)”接口创建。

        :return: The instance_id of this ShowClientNetworkResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowClientNetworkResponse.

        实例ID，可以调用“[查询实例列表和详情](x-wc://file=zh-cn_topic_0000001369935045.xml)”接口获取。如果未申请实例，可以调用“[创建实例](x-wc://file=zh-cn_topic_0000001369734929.xml)”接口创建。

        :param instance_id: The instance_id of this ShowClientNetworkResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def client_network_ranges(self):
        """Gets the client_network_ranges of this ShowClientNetworkResponse.

        客户端所在网段。 > - [跨网段访问配置只有在客户端与副本集实例部署在不同网段的情况下才允许配置，例如访问副本集的客户端所在网段为192.168.0.0/16，副本集所在的网段为172.16.0.0/24，则需要添加跨网段配置192.168.0.0/16才能正常访问。只有副本集有该功能。](tag:ccs,cmcc,ctc,dt,dt_test,fcs,fcs_dt,g42,hic,hk_g42,hk_sbc,hc,hws_ocb,hws_sbc,ocb,tlf,tm,hk,hws_eu)

        :return: The client_network_ranges of this ShowClientNetworkResponse.
        :rtype: list[str]
        """
        return self._client_network_ranges

    @client_network_ranges.setter
    def client_network_ranges(self, client_network_ranges):
        """Sets the client_network_ranges of this ShowClientNetworkResponse.

        客户端所在网段。 > - [跨网段访问配置只有在客户端与副本集实例部署在不同网段的情况下才允许配置，例如访问副本集的客户端所在网段为192.168.0.0/16，副本集所在的网段为172.16.0.0/24，则需要添加跨网段配置192.168.0.0/16才能正常访问。只有副本集有该功能。](tag:ccs,cmcc,ctc,dt,dt_test,fcs,fcs_dt,g42,hic,hk_g42,hk_sbc,hc,hws_ocb,hws_sbc,ocb,tlf,tm,hk,hws_eu)

        :param client_network_ranges: The client_network_ranges of this ShowClientNetworkResponse.
        :type client_network_ranges: list[str]
        """
        self._client_network_ranges = client_network_ranges

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
        if not isinstance(other, ShowClientNetworkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
