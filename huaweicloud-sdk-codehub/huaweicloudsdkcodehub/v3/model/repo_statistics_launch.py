# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoStatisticsLaunch:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_statistics': 'bool',
        'join_id': 'str',
        'message': 'str'
    }

    attribute_map = {
        'can_statistics': 'can_statistics',
        'join_id': 'join_id',
        'message': 'message'
    }

    def __init__(self, can_statistics=None, join_id=None, message=None):
        r"""RepoStatisticsLaunch

        The model defined in huaweicloud sdk

        :param can_statistics: 仓库是否可以统计
        :type can_statistics: bool
        :param join_id: sidekiq任务的 id
        :type join_id: str
        :param message: 启动仓库统计返回的信息
        :type message: str
        """
        
        

        self._can_statistics = None
        self._join_id = None
        self._message = None
        self.discriminator = None

        if can_statistics is not None:
            self.can_statistics = can_statistics
        if join_id is not None:
            self.join_id = join_id
        if message is not None:
            self.message = message

    @property
    def can_statistics(self):
        r"""Gets the can_statistics of this RepoStatisticsLaunch.

        仓库是否可以统计

        :return: The can_statistics of this RepoStatisticsLaunch.
        :rtype: bool
        """
        return self._can_statistics

    @can_statistics.setter
    def can_statistics(self, can_statistics):
        r"""Sets the can_statistics of this RepoStatisticsLaunch.

        仓库是否可以统计

        :param can_statistics: The can_statistics of this RepoStatisticsLaunch.
        :type can_statistics: bool
        """
        self._can_statistics = can_statistics

    @property
    def join_id(self):
        r"""Gets the join_id of this RepoStatisticsLaunch.

        sidekiq任务的 id

        :return: The join_id of this RepoStatisticsLaunch.
        :rtype: str
        """
        return self._join_id

    @join_id.setter
    def join_id(self, join_id):
        r"""Sets the join_id of this RepoStatisticsLaunch.

        sidekiq任务的 id

        :param join_id: The join_id of this RepoStatisticsLaunch.
        :type join_id: str
        """
        self._join_id = join_id

    @property
    def message(self):
        r"""Gets the message of this RepoStatisticsLaunch.

        启动仓库统计返回的信息

        :return: The message of this RepoStatisticsLaunch.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this RepoStatisticsLaunch.

        启动仓库统计返回的信息

        :param message: The message of this RepoStatisticsLaunch.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, RepoStatisticsLaunch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
