# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterScanStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_cluster_num': 'int',
        'app_vul_cluster_num': 'int',
        'unscan_cluster_num': 'int',
        'all_cluster_num': 'int'
    }

    attribute_map = {
        'risk_cluster_num': 'risk_cluster_num',
        'app_vul_cluster_num': 'app_vul_cluster_num',
        'unscan_cluster_num': 'unscan_cluster_num',
        'all_cluster_num': 'all_cluster_num'
    }

    def __init__(self, risk_cluster_num=None, app_vul_cluster_num=None, unscan_cluster_num=None, all_cluster_num=None):
        r"""ShowClusterScanStatisticsResponse

        The model defined in huaweicloud sdk

        :param risk_cluster_num: 有风险集群数量
        :type risk_cluster_num: int
        :param app_vul_cluster_num: 存在应用漏洞的集群数量
        :type app_vul_cluster_num: int
        :param unscan_cluster_num: 未扫描集群数量
        :type unscan_cluster_num: int
        :param all_cluster_num: 集群总数量
        :type all_cluster_num: int
        """
        
        super(ShowClusterScanStatisticsResponse, self).__init__()

        self._risk_cluster_num = None
        self._app_vul_cluster_num = None
        self._unscan_cluster_num = None
        self._all_cluster_num = None
        self.discriminator = None

        if risk_cluster_num is not None:
            self.risk_cluster_num = risk_cluster_num
        if app_vul_cluster_num is not None:
            self.app_vul_cluster_num = app_vul_cluster_num
        if unscan_cluster_num is not None:
            self.unscan_cluster_num = unscan_cluster_num
        if all_cluster_num is not None:
            self.all_cluster_num = all_cluster_num

    @property
    def risk_cluster_num(self):
        r"""Gets the risk_cluster_num of this ShowClusterScanStatisticsResponse.

        有风险集群数量

        :return: The risk_cluster_num of this ShowClusterScanStatisticsResponse.
        :rtype: int
        """
        return self._risk_cluster_num

    @risk_cluster_num.setter
    def risk_cluster_num(self, risk_cluster_num):
        r"""Sets the risk_cluster_num of this ShowClusterScanStatisticsResponse.

        有风险集群数量

        :param risk_cluster_num: The risk_cluster_num of this ShowClusterScanStatisticsResponse.
        :type risk_cluster_num: int
        """
        self._risk_cluster_num = risk_cluster_num

    @property
    def app_vul_cluster_num(self):
        r"""Gets the app_vul_cluster_num of this ShowClusterScanStatisticsResponse.

        存在应用漏洞的集群数量

        :return: The app_vul_cluster_num of this ShowClusterScanStatisticsResponse.
        :rtype: int
        """
        return self._app_vul_cluster_num

    @app_vul_cluster_num.setter
    def app_vul_cluster_num(self, app_vul_cluster_num):
        r"""Sets the app_vul_cluster_num of this ShowClusterScanStatisticsResponse.

        存在应用漏洞的集群数量

        :param app_vul_cluster_num: The app_vul_cluster_num of this ShowClusterScanStatisticsResponse.
        :type app_vul_cluster_num: int
        """
        self._app_vul_cluster_num = app_vul_cluster_num

    @property
    def unscan_cluster_num(self):
        r"""Gets the unscan_cluster_num of this ShowClusterScanStatisticsResponse.

        未扫描集群数量

        :return: The unscan_cluster_num of this ShowClusterScanStatisticsResponse.
        :rtype: int
        """
        return self._unscan_cluster_num

    @unscan_cluster_num.setter
    def unscan_cluster_num(self, unscan_cluster_num):
        r"""Sets the unscan_cluster_num of this ShowClusterScanStatisticsResponse.

        未扫描集群数量

        :param unscan_cluster_num: The unscan_cluster_num of this ShowClusterScanStatisticsResponse.
        :type unscan_cluster_num: int
        """
        self._unscan_cluster_num = unscan_cluster_num

    @property
    def all_cluster_num(self):
        r"""Gets the all_cluster_num of this ShowClusterScanStatisticsResponse.

        集群总数量

        :return: The all_cluster_num of this ShowClusterScanStatisticsResponse.
        :rtype: int
        """
        return self._all_cluster_num

    @all_cluster_num.setter
    def all_cluster_num(self, all_cluster_num):
        r"""Sets the all_cluster_num of this ShowClusterScanStatisticsResponse.

        集群总数量

        :param all_cluster_num: The all_cluster_num of this ShowClusterScanStatisticsResponse.
        :type all_cluster_num: int
        """
        self._all_cluster_num = all_cluster_num

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
        if not isinstance(other, ShowClusterScanStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
