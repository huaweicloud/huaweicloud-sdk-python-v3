# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgentStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'wait_upgrade_num': 'int',
        'online_num': 'int',
        'not_online_num': 'int',
        'offline_num': 'int',
        'incluster_num': 'int',
        'not_incluster_num': 'int'
    }

    attribute_map = {
        'wait_upgrade_num': 'wait_upgrade_num',
        'online_num': 'online_num',
        'not_online_num': 'not_online_num',
        'offline_num': 'offline_num',
        'incluster_num': 'incluster_num',
        'not_incluster_num': 'not_incluster_num'
    }

    def __init__(self, wait_upgrade_num=None, online_num=None, not_online_num=None, offline_num=None, incluster_num=None, not_incluster_num=None):
        r"""ShowAgentStatisticsResponse

        The model defined in huaweicloud sdk

        :param wait_upgrade_num: 待升级数量
        :type wait_upgrade_num: int
        :param online_num: 在线数量
        :type online_num: int
        :param not_online_num: 不在线数量
        :type not_online_num: int
        :param offline_num: 离线数量
        :type offline_num: int
        :param incluster_num: 集群内节点数
        :type incluster_num: int
        :param not_incluster_num: 非集群内节点数
        :type not_incluster_num: int
        """
        
        super(ShowAgentStatisticsResponse, self).__init__()

        self._wait_upgrade_num = None
        self._online_num = None
        self._not_online_num = None
        self._offline_num = None
        self._incluster_num = None
        self._not_incluster_num = None
        self.discriminator = None

        if wait_upgrade_num is not None:
            self.wait_upgrade_num = wait_upgrade_num
        if online_num is not None:
            self.online_num = online_num
        if not_online_num is not None:
            self.not_online_num = not_online_num
        if offline_num is not None:
            self.offline_num = offline_num
        if incluster_num is not None:
            self.incluster_num = incluster_num
        if not_incluster_num is not None:
            self.not_incluster_num = not_incluster_num

    @property
    def wait_upgrade_num(self):
        r"""Gets the wait_upgrade_num of this ShowAgentStatisticsResponse.

        待升级数量

        :return: The wait_upgrade_num of this ShowAgentStatisticsResponse.
        :rtype: int
        """
        return self._wait_upgrade_num

    @wait_upgrade_num.setter
    def wait_upgrade_num(self, wait_upgrade_num):
        r"""Sets the wait_upgrade_num of this ShowAgentStatisticsResponse.

        待升级数量

        :param wait_upgrade_num: The wait_upgrade_num of this ShowAgentStatisticsResponse.
        :type wait_upgrade_num: int
        """
        self._wait_upgrade_num = wait_upgrade_num

    @property
    def online_num(self):
        r"""Gets the online_num of this ShowAgentStatisticsResponse.

        在线数量

        :return: The online_num of this ShowAgentStatisticsResponse.
        :rtype: int
        """
        return self._online_num

    @online_num.setter
    def online_num(self, online_num):
        r"""Sets the online_num of this ShowAgentStatisticsResponse.

        在线数量

        :param online_num: The online_num of this ShowAgentStatisticsResponse.
        :type online_num: int
        """
        self._online_num = online_num

    @property
    def not_online_num(self):
        r"""Gets the not_online_num of this ShowAgentStatisticsResponse.

        不在线数量

        :return: The not_online_num of this ShowAgentStatisticsResponse.
        :rtype: int
        """
        return self._not_online_num

    @not_online_num.setter
    def not_online_num(self, not_online_num):
        r"""Sets the not_online_num of this ShowAgentStatisticsResponse.

        不在线数量

        :param not_online_num: The not_online_num of this ShowAgentStatisticsResponse.
        :type not_online_num: int
        """
        self._not_online_num = not_online_num

    @property
    def offline_num(self):
        r"""Gets the offline_num of this ShowAgentStatisticsResponse.

        离线数量

        :return: The offline_num of this ShowAgentStatisticsResponse.
        :rtype: int
        """
        return self._offline_num

    @offline_num.setter
    def offline_num(self, offline_num):
        r"""Sets the offline_num of this ShowAgentStatisticsResponse.

        离线数量

        :param offline_num: The offline_num of this ShowAgentStatisticsResponse.
        :type offline_num: int
        """
        self._offline_num = offline_num

    @property
    def incluster_num(self):
        r"""Gets the incluster_num of this ShowAgentStatisticsResponse.

        集群内节点数

        :return: The incluster_num of this ShowAgentStatisticsResponse.
        :rtype: int
        """
        return self._incluster_num

    @incluster_num.setter
    def incluster_num(self, incluster_num):
        r"""Sets the incluster_num of this ShowAgentStatisticsResponse.

        集群内节点数

        :param incluster_num: The incluster_num of this ShowAgentStatisticsResponse.
        :type incluster_num: int
        """
        self._incluster_num = incluster_num

    @property
    def not_incluster_num(self):
        r"""Gets the not_incluster_num of this ShowAgentStatisticsResponse.

        非集群内节点数

        :return: The not_incluster_num of this ShowAgentStatisticsResponse.
        :rtype: int
        """
        return self._not_incluster_num

    @not_incluster_num.setter
    def not_incluster_num(self, not_incluster_num):
        r"""Sets the not_incluster_num of this ShowAgentStatisticsResponse.

        非集群内节点数

        :param not_incluster_num: The not_incluster_num of this ShowAgentStatisticsResponse.
        :type not_incluster_num: int
        """
        self._not_incluster_num = not_incluster_num

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
        if not isinstance(other, ShowAgentStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
