# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisasterRecoveryQueryResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'dr_type': 'str',
        'status': 'str',
        'primary_cluster': 'DisasterRecoveryCluster',
        'standby_cluster': 'DisasterRecoveryCluster',
        'dr_sync_period': 'str',
        'start_time': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'dr_type': 'dr_type',
        'status': 'status',
        'primary_cluster': 'primary_cluster',
        'standby_cluster': 'standby_cluster',
        'dr_sync_period': 'dr_sync_period',
        'start_time': 'start_time',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, name=None, dr_type=None, status=None, primary_cluster=None, standby_cluster=None, dr_sync_period=None, start_time=None, create_time=None):
        """DisasterRecoveryQueryResp

        The model defined in huaweicloud sdk

        :param id: 容灾ID
        :type id: str
        :param name: 容灾名称
        :type name: str
        :param dr_type: 容灾类型
        :type dr_type: str
        :param status: 容灾状态
        :type status: str
        :param primary_cluster: 
        :type primary_cluster: :class:`huaweicloudsdkdws.v2.DisasterRecoveryCluster`
        :param standby_cluster: 
        :type standby_cluster: :class:`huaweicloudsdkdws.v2.DisasterRecoveryCluster`
        :param dr_sync_period: 容灾同步周期
        :type dr_sync_period: str
        :param start_time: 容灾启动时间
        :type start_time: str
        :param create_time: 容灾创建时间
        :type create_time: str
        """
        
        

        self._id = None
        self._name = None
        self._dr_type = None
        self._status = None
        self._primary_cluster = None
        self._standby_cluster = None
        self._dr_sync_period = None
        self._start_time = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if dr_type is not None:
            self.dr_type = dr_type
        if status is not None:
            self.status = status
        if primary_cluster is not None:
            self.primary_cluster = primary_cluster
        if standby_cluster is not None:
            self.standby_cluster = standby_cluster
        if dr_sync_period is not None:
            self.dr_sync_period = dr_sync_period
        if start_time is not None:
            self.start_time = start_time
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        """Gets the id of this DisasterRecoveryQueryResp.

        容灾ID

        :return: The id of this DisasterRecoveryQueryResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DisasterRecoveryQueryResp.

        容灾ID

        :param id: The id of this DisasterRecoveryQueryResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DisasterRecoveryQueryResp.

        容灾名称

        :return: The name of this DisasterRecoveryQueryResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DisasterRecoveryQueryResp.

        容灾名称

        :param name: The name of this DisasterRecoveryQueryResp.
        :type name: str
        """
        self._name = name

    @property
    def dr_type(self):
        """Gets the dr_type of this DisasterRecoveryQueryResp.

        容灾类型

        :return: The dr_type of this DisasterRecoveryQueryResp.
        :rtype: str
        """
        return self._dr_type

    @dr_type.setter
    def dr_type(self, dr_type):
        """Sets the dr_type of this DisasterRecoveryQueryResp.

        容灾类型

        :param dr_type: The dr_type of this DisasterRecoveryQueryResp.
        :type dr_type: str
        """
        self._dr_type = dr_type

    @property
    def status(self):
        """Gets the status of this DisasterRecoveryQueryResp.

        容灾状态

        :return: The status of this DisasterRecoveryQueryResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DisasterRecoveryQueryResp.

        容灾状态

        :param status: The status of this DisasterRecoveryQueryResp.
        :type status: str
        """
        self._status = status

    @property
    def primary_cluster(self):
        """Gets the primary_cluster of this DisasterRecoveryQueryResp.

        :return: The primary_cluster of this DisasterRecoveryQueryResp.
        :rtype: :class:`huaweicloudsdkdws.v2.DisasterRecoveryCluster`
        """
        return self._primary_cluster

    @primary_cluster.setter
    def primary_cluster(self, primary_cluster):
        """Sets the primary_cluster of this DisasterRecoveryQueryResp.

        :param primary_cluster: The primary_cluster of this DisasterRecoveryQueryResp.
        :type primary_cluster: :class:`huaweicloudsdkdws.v2.DisasterRecoveryCluster`
        """
        self._primary_cluster = primary_cluster

    @property
    def standby_cluster(self):
        """Gets the standby_cluster of this DisasterRecoveryQueryResp.

        :return: The standby_cluster of this DisasterRecoveryQueryResp.
        :rtype: :class:`huaweicloudsdkdws.v2.DisasterRecoveryCluster`
        """
        return self._standby_cluster

    @standby_cluster.setter
    def standby_cluster(self, standby_cluster):
        """Sets the standby_cluster of this DisasterRecoveryQueryResp.

        :param standby_cluster: The standby_cluster of this DisasterRecoveryQueryResp.
        :type standby_cluster: :class:`huaweicloudsdkdws.v2.DisasterRecoveryCluster`
        """
        self._standby_cluster = standby_cluster

    @property
    def dr_sync_period(self):
        """Gets the dr_sync_period of this DisasterRecoveryQueryResp.

        容灾同步周期

        :return: The dr_sync_period of this DisasterRecoveryQueryResp.
        :rtype: str
        """
        return self._dr_sync_period

    @dr_sync_period.setter
    def dr_sync_period(self, dr_sync_period):
        """Sets the dr_sync_period of this DisasterRecoveryQueryResp.

        容灾同步周期

        :param dr_sync_period: The dr_sync_period of this DisasterRecoveryQueryResp.
        :type dr_sync_period: str
        """
        self._dr_sync_period = dr_sync_period

    @property
    def start_time(self):
        """Gets the start_time of this DisasterRecoveryQueryResp.

        容灾启动时间

        :return: The start_time of this DisasterRecoveryQueryResp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DisasterRecoveryQueryResp.

        容灾启动时间

        :param start_time: The start_time of this DisasterRecoveryQueryResp.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def create_time(self):
        """Gets the create_time of this DisasterRecoveryQueryResp.

        容灾创建时间

        :return: The create_time of this DisasterRecoveryQueryResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DisasterRecoveryQueryResp.

        容灾创建时间

        :param create_time: The create_time of this DisasterRecoveryQueryResp.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, DisasterRecoveryQueryResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
