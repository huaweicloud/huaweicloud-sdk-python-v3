# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgentStatisticsStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'online': 'int',
        'offline': 'int',
        'not_installed': 'int',
        'total_num': 'int'
    }

    attribute_map = {
        'online': 'online',
        'offline': 'offline',
        'not_installed': 'not_installed',
        'total_num': 'total_num'
    }

    def __init__(self, online=None, offline=None, not_installed=None, total_num=None):
        r"""ShowAgentStatisticsStatusResponse

        The model defined in huaweicloud sdk

        :param online: 主机Agent在线数
        :type online: int
        :param offline: 主机Agent离线数
        :type offline: int
        :param not_installed: 未安装主机Agent的主机数
        :type not_installed: int
        :param total_num: 主机总数
        :type total_num: int
        """
        
        super(ShowAgentStatisticsStatusResponse, self).__init__()

        self._online = None
        self._offline = None
        self._not_installed = None
        self._total_num = None
        self.discriminator = None

        if online is not None:
            self.online = online
        if offline is not None:
            self.offline = offline
        if not_installed is not None:
            self.not_installed = not_installed
        if total_num is not None:
            self.total_num = total_num

    @property
    def online(self):
        r"""Gets the online of this ShowAgentStatisticsStatusResponse.

        主机Agent在线数

        :return: The online of this ShowAgentStatisticsStatusResponse.
        :rtype: int
        """
        return self._online

    @online.setter
    def online(self, online):
        r"""Sets the online of this ShowAgentStatisticsStatusResponse.

        主机Agent在线数

        :param online: The online of this ShowAgentStatisticsStatusResponse.
        :type online: int
        """
        self._online = online

    @property
    def offline(self):
        r"""Gets the offline of this ShowAgentStatisticsStatusResponse.

        主机Agent离线数

        :return: The offline of this ShowAgentStatisticsStatusResponse.
        :rtype: int
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        r"""Sets the offline of this ShowAgentStatisticsStatusResponse.

        主机Agent离线数

        :param offline: The offline of this ShowAgentStatisticsStatusResponse.
        :type offline: int
        """
        self._offline = offline

    @property
    def not_installed(self):
        r"""Gets the not_installed of this ShowAgentStatisticsStatusResponse.

        未安装主机Agent的主机数

        :return: The not_installed of this ShowAgentStatisticsStatusResponse.
        :rtype: int
        """
        return self._not_installed

    @not_installed.setter
    def not_installed(self, not_installed):
        r"""Sets the not_installed of this ShowAgentStatisticsStatusResponse.

        未安装主机Agent的主机数

        :param not_installed: The not_installed of this ShowAgentStatisticsStatusResponse.
        :type not_installed: int
        """
        self._not_installed = not_installed

    @property
    def total_num(self):
        r"""Gets the total_num of this ShowAgentStatisticsStatusResponse.

        主机总数

        :return: The total_num of this ShowAgentStatisticsStatusResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ShowAgentStatisticsStatusResponse.

        主机总数

        :param total_num: The total_num of this ShowAgentStatisticsStatusResponse.
        :type total_num: int
        """
        self._total_num = total_num

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
        if not isinstance(other, ShowAgentStatisticsStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
