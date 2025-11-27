# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OverviewReconcileStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_set_total_num': 'int',
        'health_status_num': 'int',
        'failed_status_num': 'int',
        'unknown_status_num': 'int',
        'progressing_status_num': 'int'
    }

    attribute_map = {
        'config_set_total_num': 'configSetTotalNum',
        'health_status_num': 'healthStatusNum',
        'failed_status_num': 'failedStatusNum',
        'unknown_status_num': 'unknownStatusNum',
        'progressing_status_num': 'progressingStatusNum'
    }

    def __init__(self, config_set_total_num=None, health_status_num=None, failed_status_num=None, unknown_status_num=None, progressing_status_num=None):
        r"""OverviewReconcileStatus

        The model defined in huaweicloud sdk

        :param config_set_total_num: 配置集合总数
        :type config_set_total_num: int
        :param health_status_num: 健康状态的配置集合数量
        :type health_status_num: int
        :param failed_status_num: 失败状态的配置集合数量
        :type failed_status_num: int
        :param unknown_status_num: 未知状态的配置集合数量
        :type unknown_status_num: int
        :param progressing_status_num: 正在处理中的配置集合数量
        :type progressing_status_num: int
        """
        
        

        self._config_set_total_num = None
        self._health_status_num = None
        self._failed_status_num = None
        self._unknown_status_num = None
        self._progressing_status_num = None
        self.discriminator = None

        if config_set_total_num is not None:
            self.config_set_total_num = config_set_total_num
        if health_status_num is not None:
            self.health_status_num = health_status_num
        if failed_status_num is not None:
            self.failed_status_num = failed_status_num
        if unknown_status_num is not None:
            self.unknown_status_num = unknown_status_num
        if progressing_status_num is not None:
            self.progressing_status_num = progressing_status_num

    @property
    def config_set_total_num(self):
        r"""Gets the config_set_total_num of this OverviewReconcileStatus.

        配置集合总数

        :return: The config_set_total_num of this OverviewReconcileStatus.
        :rtype: int
        """
        return self._config_set_total_num

    @config_set_total_num.setter
    def config_set_total_num(self, config_set_total_num):
        r"""Sets the config_set_total_num of this OverviewReconcileStatus.

        配置集合总数

        :param config_set_total_num: The config_set_total_num of this OverviewReconcileStatus.
        :type config_set_total_num: int
        """
        self._config_set_total_num = config_set_total_num

    @property
    def health_status_num(self):
        r"""Gets the health_status_num of this OverviewReconcileStatus.

        健康状态的配置集合数量

        :return: The health_status_num of this OverviewReconcileStatus.
        :rtype: int
        """
        return self._health_status_num

    @health_status_num.setter
    def health_status_num(self, health_status_num):
        r"""Sets the health_status_num of this OverviewReconcileStatus.

        健康状态的配置集合数量

        :param health_status_num: The health_status_num of this OverviewReconcileStatus.
        :type health_status_num: int
        """
        self._health_status_num = health_status_num

    @property
    def failed_status_num(self):
        r"""Gets the failed_status_num of this OverviewReconcileStatus.

        失败状态的配置集合数量

        :return: The failed_status_num of this OverviewReconcileStatus.
        :rtype: int
        """
        return self._failed_status_num

    @failed_status_num.setter
    def failed_status_num(self, failed_status_num):
        r"""Sets the failed_status_num of this OverviewReconcileStatus.

        失败状态的配置集合数量

        :param failed_status_num: The failed_status_num of this OverviewReconcileStatus.
        :type failed_status_num: int
        """
        self._failed_status_num = failed_status_num

    @property
    def unknown_status_num(self):
        r"""Gets the unknown_status_num of this OverviewReconcileStatus.

        未知状态的配置集合数量

        :return: The unknown_status_num of this OverviewReconcileStatus.
        :rtype: int
        """
        return self._unknown_status_num

    @unknown_status_num.setter
    def unknown_status_num(self, unknown_status_num):
        r"""Sets the unknown_status_num of this OverviewReconcileStatus.

        未知状态的配置集合数量

        :param unknown_status_num: The unknown_status_num of this OverviewReconcileStatus.
        :type unknown_status_num: int
        """
        self._unknown_status_num = unknown_status_num

    @property
    def progressing_status_num(self):
        r"""Gets the progressing_status_num of this OverviewReconcileStatus.

        正在处理中的配置集合数量

        :return: The progressing_status_num of this OverviewReconcileStatus.
        :rtype: int
        """
        return self._progressing_status_num

    @progressing_status_num.setter
    def progressing_status_num(self, progressing_status_num):
        r"""Sets the progressing_status_num of this OverviewReconcileStatus.

        正在处理中的配置集合数量

        :param progressing_status_num: The progressing_status_num of this OverviewReconcileStatus.
        :type progressing_status_num: int
        """
        self._progressing_status_num = progressing_status_num

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
        if not isinstance(other, OverviewReconcileStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
