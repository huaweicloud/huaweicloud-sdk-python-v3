# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'username': 'str',
        'metric': 'list[Metric]'
    }

    attribute_map = {
        'username': 'username',
        'metric': 'metric'
    }

    def __init__(self, username=None, metric=None):
        r"""UserMetric

        The model defined in huaweicloud sdk

        :param username: 用户名称。
        :type username: str
        :param metric: 桌面使用统计信息 * &#x60;user_usage&#x60; -  用户使用时长(单位:秒)，同一时间登录多台PC的话;相应的时间会累加 * &#x60;user_login_count&#x60; -  用户登录次数(单位:次) * &#x60;user_login_success_count&#x60; -  用户登录成功次数(单位:次) * &#x60;user_login_fail_count&#x60; -  用户登录失败次数(单位:次)
        :type metric: list[:class:`huaweicloudsdkworkspace.v2.Metric`]
        """
        
        

        self._username = None
        self._metric = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if metric is not None:
            self.metric = metric

    @property
    def username(self):
        r"""Gets the username of this UserMetric.

        用户名称。

        :return: The username of this UserMetric.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this UserMetric.

        用户名称。

        :param username: The username of this UserMetric.
        :type username: str
        """
        self._username = username

    @property
    def metric(self):
        r"""Gets the metric of this UserMetric.

        桌面使用统计信息 * `user_usage` -  用户使用时长(单位:秒)，同一时间登录多台PC的话;相应的时间会累加 * `user_login_count` -  用户登录次数(单位:次) * `user_login_success_count` -  用户登录成功次数(单位:次) * `user_login_fail_count` -  用户登录失败次数(单位:次)

        :return: The metric of this UserMetric.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Metric`]
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this UserMetric.

        桌面使用统计信息 * `user_usage` -  用户使用时长(单位:秒)，同一时间登录多台PC的话;相应的时间会累加 * `user_login_count` -  用户登录次数(单位:次) * `user_login_success_count` -  用户登录成功次数(单位:次) * `user_login_fail_count` -  用户登录失败次数(单位:次)

        :param metric: The metric of this UserMetric.
        :type metric: list[:class:`huaweicloudsdkworkspace.v2.Metric`]
        """
        self._metric = metric

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
        if not isinstance(other, UserMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
