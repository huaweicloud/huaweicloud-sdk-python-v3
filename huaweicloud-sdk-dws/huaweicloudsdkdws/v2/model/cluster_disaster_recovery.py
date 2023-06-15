# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterDisasterRecovery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'primary_cluster': 'ClusterRecoveryProgress',
        'standby_cluster': 'ClusterRecoveryProgress',
        'latest_barrier_time': 'str',
        'last_recovery_spend': 'int',
        'recovery_point_object': 'int',
        'recovery_time_object': 'int'
    }

    attribute_map = {
        'primary_cluster': 'primary_cluster',
        'standby_cluster': 'standby_cluster',
        'latest_barrier_time': 'latest_barrier_time',
        'last_recovery_spend': 'last_recovery_spend',
        'recovery_point_object': 'recovery_point_object',
        'recovery_time_object': 'recovery_time_object'
    }

    def __init__(self, primary_cluster=None, standby_cluster=None, latest_barrier_time=None, last_recovery_spend=None, recovery_point_object=None, recovery_time_object=None):
        """ClusterDisasterRecovery

        The model defined in huaweicloud sdk

        :param primary_cluster: 
        :type primary_cluster: :class:`huaweicloudsdkdws.v2.ClusterRecoveryProgress`
        :param standby_cluster: 
        :type standby_cluster: :class:`huaweicloudsdkdws.v2.ClusterRecoveryProgress`
        :param latest_barrier_time: latest_barrier_time
        :type latest_barrier_time: str
        :param last_recovery_spend: last_recovery_spend
        :type last_recovery_spend: int
        :param recovery_point_object: recovery_point_object
        :type recovery_point_object: int
        :param recovery_time_object: recovery_time_object
        :type recovery_time_object: int
        """
        
        

        self._primary_cluster = None
        self._standby_cluster = None
        self._latest_barrier_time = None
        self._last_recovery_spend = None
        self._recovery_point_object = None
        self._recovery_time_object = None
        self.discriminator = None

        if primary_cluster is not None:
            self.primary_cluster = primary_cluster
        if standby_cluster is not None:
            self.standby_cluster = standby_cluster
        if latest_barrier_time is not None:
            self.latest_barrier_time = latest_barrier_time
        if last_recovery_spend is not None:
            self.last_recovery_spend = last_recovery_spend
        if recovery_point_object is not None:
            self.recovery_point_object = recovery_point_object
        if recovery_time_object is not None:
            self.recovery_time_object = recovery_time_object

    @property
    def primary_cluster(self):
        """Gets the primary_cluster of this ClusterDisasterRecovery.

        :return: The primary_cluster of this ClusterDisasterRecovery.
        :rtype: :class:`huaweicloudsdkdws.v2.ClusterRecoveryProgress`
        """
        return self._primary_cluster

    @primary_cluster.setter
    def primary_cluster(self, primary_cluster):
        """Sets the primary_cluster of this ClusterDisasterRecovery.

        :param primary_cluster: The primary_cluster of this ClusterDisasterRecovery.
        :type primary_cluster: :class:`huaweicloudsdkdws.v2.ClusterRecoveryProgress`
        """
        self._primary_cluster = primary_cluster

    @property
    def standby_cluster(self):
        """Gets the standby_cluster of this ClusterDisasterRecovery.

        :return: The standby_cluster of this ClusterDisasterRecovery.
        :rtype: :class:`huaweicloudsdkdws.v2.ClusterRecoveryProgress`
        """
        return self._standby_cluster

    @standby_cluster.setter
    def standby_cluster(self, standby_cluster):
        """Sets the standby_cluster of this ClusterDisasterRecovery.

        :param standby_cluster: The standby_cluster of this ClusterDisasterRecovery.
        :type standby_cluster: :class:`huaweicloudsdkdws.v2.ClusterRecoveryProgress`
        """
        self._standby_cluster = standby_cluster

    @property
    def latest_barrier_time(self):
        """Gets the latest_barrier_time of this ClusterDisasterRecovery.

        latest_barrier_time

        :return: The latest_barrier_time of this ClusterDisasterRecovery.
        :rtype: str
        """
        return self._latest_barrier_time

    @latest_barrier_time.setter
    def latest_barrier_time(self, latest_barrier_time):
        """Sets the latest_barrier_time of this ClusterDisasterRecovery.

        latest_barrier_time

        :param latest_barrier_time: The latest_barrier_time of this ClusterDisasterRecovery.
        :type latest_barrier_time: str
        """
        self._latest_barrier_time = latest_barrier_time

    @property
    def last_recovery_spend(self):
        """Gets the last_recovery_spend of this ClusterDisasterRecovery.

        last_recovery_spend

        :return: The last_recovery_spend of this ClusterDisasterRecovery.
        :rtype: int
        """
        return self._last_recovery_spend

    @last_recovery_spend.setter
    def last_recovery_spend(self, last_recovery_spend):
        """Sets the last_recovery_spend of this ClusterDisasterRecovery.

        last_recovery_spend

        :param last_recovery_spend: The last_recovery_spend of this ClusterDisasterRecovery.
        :type last_recovery_spend: int
        """
        self._last_recovery_spend = last_recovery_spend

    @property
    def recovery_point_object(self):
        """Gets the recovery_point_object of this ClusterDisasterRecovery.

        recovery_point_object

        :return: The recovery_point_object of this ClusterDisasterRecovery.
        :rtype: int
        """
        return self._recovery_point_object

    @recovery_point_object.setter
    def recovery_point_object(self, recovery_point_object):
        """Sets the recovery_point_object of this ClusterDisasterRecovery.

        recovery_point_object

        :param recovery_point_object: The recovery_point_object of this ClusterDisasterRecovery.
        :type recovery_point_object: int
        """
        self._recovery_point_object = recovery_point_object

    @property
    def recovery_time_object(self):
        """Gets the recovery_time_object of this ClusterDisasterRecovery.

        recovery_time_object

        :return: The recovery_time_object of this ClusterDisasterRecovery.
        :rtype: int
        """
        return self._recovery_time_object

    @recovery_time_object.setter
    def recovery_time_object(self, recovery_time_object):
        """Sets the recovery_time_object of this ClusterDisasterRecovery.

        recovery_time_object

        :param recovery_time_object: The recovery_time_object of this ClusterDisasterRecovery.
        :type recovery_time_object: int
        """
        self._recovery_time_object = recovery_time_object

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
        if not isinstance(other, ClusterDisasterRecovery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
