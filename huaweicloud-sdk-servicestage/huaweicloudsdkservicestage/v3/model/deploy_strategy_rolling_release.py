# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployStrategyRollingRelease:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batches': 'int',
        'termination_seconds': 'int',
        'fail_strategy': 'str'
    }

    attribute_map = {
        'batches': 'batches',
        'termination_seconds': 'termination_seconds',
        'fail_strategy': 'fail_strategy'
    }

    def __init__(self, batches=None, termination_seconds=None, fail_strategy=None):
        """DeployStrategyRollingRelease

        The model defined in huaweicloud sdk

        :param batches: 
        :type batches: int
        :param termination_seconds: 
        :type termination_seconds: int
        :param fail_strategy: 只对虚机部署有用，默认是stop，一批执行失败后停止升级。
        :type fail_strategy: str
        """
        
        

        self._batches = None
        self._termination_seconds = None
        self._fail_strategy = None
        self.discriminator = None

        if batches is not None:
            self.batches = batches
        if termination_seconds is not None:
            self.termination_seconds = termination_seconds
        if fail_strategy is not None:
            self.fail_strategy = fail_strategy

    @property
    def batches(self):
        """Gets the batches of this DeployStrategyRollingRelease.

        :return: The batches of this DeployStrategyRollingRelease.
        :rtype: int
        """
        return self._batches

    @batches.setter
    def batches(self, batches):
        """Sets the batches of this DeployStrategyRollingRelease.

        :param batches: The batches of this DeployStrategyRollingRelease.
        :type batches: int
        """
        self._batches = batches

    @property
    def termination_seconds(self):
        """Gets the termination_seconds of this DeployStrategyRollingRelease.

        :return: The termination_seconds of this DeployStrategyRollingRelease.
        :rtype: int
        """
        return self._termination_seconds

    @termination_seconds.setter
    def termination_seconds(self, termination_seconds):
        """Sets the termination_seconds of this DeployStrategyRollingRelease.

        :param termination_seconds: The termination_seconds of this DeployStrategyRollingRelease.
        :type termination_seconds: int
        """
        self._termination_seconds = termination_seconds

    @property
    def fail_strategy(self):
        """Gets the fail_strategy of this DeployStrategyRollingRelease.

        只对虚机部署有用，默认是stop，一批执行失败后停止升级。

        :return: The fail_strategy of this DeployStrategyRollingRelease.
        :rtype: str
        """
        return self._fail_strategy

    @fail_strategy.setter
    def fail_strategy(self, fail_strategy):
        """Sets the fail_strategy of this DeployStrategyRollingRelease.

        只对虚机部署有用，默认是stop，一批执行失败后停止升级。

        :param fail_strategy: The fail_strategy of this DeployStrategyRollingRelease.
        :type fail_strategy: str
        """
        self._fail_strategy = fail_strategy

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
        if not isinstance(other, DeployStrategyRollingRelease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
