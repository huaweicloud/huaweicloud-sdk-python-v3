# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeDetectRiskResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'images_num': 'int',
        'baseline_risk_num': 'int',
        'vul_num': 'int',
        'event_num': 'int',
        'protect_node_num': 'int',
        'node_total_num': 'int',
        'cluster_id': 'str',
        'charging_mode': 'str'
    }

    attribute_map = {
        'images_num': 'images_num',
        'baseline_risk_num': 'baseline_risk_num',
        'vul_num': 'vul_num',
        'event_num': 'event_num',
        'protect_node_num': 'protect_node_num',
        'node_total_num': 'node_total_num',
        'cluster_id': 'cluster_id',
        'charging_mode': 'charging_mode'
    }

    def __init__(self, images_num=None, baseline_risk_num=None, vul_num=None, event_num=None, protect_node_num=None, node_total_num=None, cluster_id=None, charging_mode=None):
        r"""NodeDetectRiskResponseInfo

        The model defined in huaweicloud sdk

        :param images_num: 有风险镜像数量
        :type images_num: int
        :param baseline_risk_num: 基线检查风险项总和
        :type baseline_risk_num: int
        :param vul_num: 漏洞数量
        :type vul_num: int
        :param event_num: 告警数量
        :type event_num: int
        :param protect_node_num: 集群开启防护节点数量
        :type protect_node_num: int
        :param node_total_num: 集群节点总数
        :type node_total_num: int
        :param cluster_id: 集群id
        :type cluster_id: str
        :param charging_mode: 付费模式包括： - on_demand：按需 - free：免费
        :type charging_mode: str
        """
        
        

        self._images_num = None
        self._baseline_risk_num = None
        self._vul_num = None
        self._event_num = None
        self._protect_node_num = None
        self._node_total_num = None
        self._cluster_id = None
        self._charging_mode = None
        self.discriminator = None

        if images_num is not None:
            self.images_num = images_num
        if baseline_risk_num is not None:
            self.baseline_risk_num = baseline_risk_num
        if vul_num is not None:
            self.vul_num = vul_num
        if event_num is not None:
            self.event_num = event_num
        if protect_node_num is not None:
            self.protect_node_num = protect_node_num
        if node_total_num is not None:
            self.node_total_num = node_total_num
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if charging_mode is not None:
            self.charging_mode = charging_mode

    @property
    def images_num(self):
        r"""Gets the images_num of this NodeDetectRiskResponseInfo.

        有风险镜像数量

        :return: The images_num of this NodeDetectRiskResponseInfo.
        :rtype: int
        """
        return self._images_num

    @images_num.setter
    def images_num(self, images_num):
        r"""Sets the images_num of this NodeDetectRiskResponseInfo.

        有风险镜像数量

        :param images_num: The images_num of this NodeDetectRiskResponseInfo.
        :type images_num: int
        """
        self._images_num = images_num

    @property
    def baseline_risk_num(self):
        r"""Gets the baseline_risk_num of this NodeDetectRiskResponseInfo.

        基线检查风险项总和

        :return: The baseline_risk_num of this NodeDetectRiskResponseInfo.
        :rtype: int
        """
        return self._baseline_risk_num

    @baseline_risk_num.setter
    def baseline_risk_num(self, baseline_risk_num):
        r"""Sets the baseline_risk_num of this NodeDetectRiskResponseInfo.

        基线检查风险项总和

        :param baseline_risk_num: The baseline_risk_num of this NodeDetectRiskResponseInfo.
        :type baseline_risk_num: int
        """
        self._baseline_risk_num = baseline_risk_num

    @property
    def vul_num(self):
        r"""Gets the vul_num of this NodeDetectRiskResponseInfo.

        漏洞数量

        :return: The vul_num of this NodeDetectRiskResponseInfo.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this NodeDetectRiskResponseInfo.

        漏洞数量

        :param vul_num: The vul_num of this NodeDetectRiskResponseInfo.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def event_num(self):
        r"""Gets the event_num of this NodeDetectRiskResponseInfo.

        告警数量

        :return: The event_num of this NodeDetectRiskResponseInfo.
        :rtype: int
        """
        return self._event_num

    @event_num.setter
    def event_num(self, event_num):
        r"""Sets the event_num of this NodeDetectRiskResponseInfo.

        告警数量

        :param event_num: The event_num of this NodeDetectRiskResponseInfo.
        :type event_num: int
        """
        self._event_num = event_num

    @property
    def protect_node_num(self):
        r"""Gets the protect_node_num of this NodeDetectRiskResponseInfo.

        集群开启防护节点数量

        :return: The protect_node_num of this NodeDetectRiskResponseInfo.
        :rtype: int
        """
        return self._protect_node_num

    @protect_node_num.setter
    def protect_node_num(self, protect_node_num):
        r"""Sets the protect_node_num of this NodeDetectRiskResponseInfo.

        集群开启防护节点数量

        :param protect_node_num: The protect_node_num of this NodeDetectRiskResponseInfo.
        :type protect_node_num: int
        """
        self._protect_node_num = protect_node_num

    @property
    def node_total_num(self):
        r"""Gets the node_total_num of this NodeDetectRiskResponseInfo.

        集群节点总数

        :return: The node_total_num of this NodeDetectRiskResponseInfo.
        :rtype: int
        """
        return self._node_total_num

    @node_total_num.setter
    def node_total_num(self, node_total_num):
        r"""Sets the node_total_num of this NodeDetectRiskResponseInfo.

        集群节点总数

        :param node_total_num: The node_total_num of this NodeDetectRiskResponseInfo.
        :type node_total_num: int
        """
        self._node_total_num = node_total_num

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this NodeDetectRiskResponseInfo.

        集群id

        :return: The cluster_id of this NodeDetectRiskResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this NodeDetectRiskResponseInfo.

        集群id

        :param cluster_id: The cluster_id of this NodeDetectRiskResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this NodeDetectRiskResponseInfo.

        付费模式包括： - on_demand：按需 - free：免费

        :return: The charging_mode of this NodeDetectRiskResponseInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this NodeDetectRiskResponseInfo.

        付费模式包括： - on_demand：按需 - free：免费

        :param charging_mode: The charging_mode of this NodeDetectRiskResponseInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

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
        if not isinstance(other, NodeDetectRiskResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
