# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceStatusView:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'InstanceStatusType',
        'available_replica': 'int',
        'replica': 'int',
        'fail_detail': 'InstanceFailDetail',
        'last_job_id': 'str',
        'last_job_status': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'available_replica': 'available_replica',
        'replica': 'replica',
        'fail_detail': 'fail_detail',
        'last_job_id': 'last_job_id',
        'last_job_status': 'last_job_status',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, status=None, available_replica=None, replica=None, fail_detail=None, last_job_id=None, last_job_status=None, enterprise_project_id=None):
        """InstanceStatusView

        The model defined in huaweicloud sdk

        :param status: 
        :type status: :class:`huaweicloudsdkservicestage.v2.InstanceStatusType`
        :param available_replica: 正常实例副本数。
        :type available_replica: int
        :param replica: 实例副本数。
        :type replica: int
        :param fail_detail: 
        :type fail_detail: :class:`huaweicloudsdkservicestage.v2.InstanceFailDetail`
        :param last_job_id: 最近Job ID。
        :type last_job_id: str
        :param last_job_status: 最近Job的状态
        :type last_job_status: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._status = None
        self._available_replica = None
        self._replica = None
        self._fail_detail = None
        self._last_job_id = None
        self._last_job_status = None
        self._enterprise_project_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if available_replica is not None:
            self.available_replica = available_replica
        if replica is not None:
            self.replica = replica
        if fail_detail is not None:
            self.fail_detail = fail_detail
        if last_job_id is not None:
            self.last_job_id = last_job_id
        if last_job_status is not None:
            self.last_job_status = last_job_status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def status(self):
        """Gets the status of this InstanceStatusView.

        :return: The status of this InstanceStatusView.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstanceStatusType`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceStatusView.

        :param status: The status of this InstanceStatusView.
        :type status: :class:`huaweicloudsdkservicestage.v2.InstanceStatusType`
        """
        self._status = status

    @property
    def available_replica(self):
        """Gets the available_replica of this InstanceStatusView.

        正常实例副本数。

        :return: The available_replica of this InstanceStatusView.
        :rtype: int
        """
        return self._available_replica

    @available_replica.setter
    def available_replica(self, available_replica):
        """Sets the available_replica of this InstanceStatusView.

        正常实例副本数。

        :param available_replica: The available_replica of this InstanceStatusView.
        :type available_replica: int
        """
        self._available_replica = available_replica

    @property
    def replica(self):
        """Gets the replica of this InstanceStatusView.

        实例副本数。

        :return: The replica of this InstanceStatusView.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        """Sets the replica of this InstanceStatusView.

        实例副本数。

        :param replica: The replica of this InstanceStatusView.
        :type replica: int
        """
        self._replica = replica

    @property
    def fail_detail(self):
        """Gets the fail_detail of this InstanceStatusView.

        :return: The fail_detail of this InstanceStatusView.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstanceFailDetail`
        """
        return self._fail_detail

    @fail_detail.setter
    def fail_detail(self, fail_detail):
        """Sets the fail_detail of this InstanceStatusView.

        :param fail_detail: The fail_detail of this InstanceStatusView.
        :type fail_detail: :class:`huaweicloudsdkservicestage.v2.InstanceFailDetail`
        """
        self._fail_detail = fail_detail

    @property
    def last_job_id(self):
        """Gets the last_job_id of this InstanceStatusView.

        最近Job ID。

        :return: The last_job_id of this InstanceStatusView.
        :rtype: str
        """
        return self._last_job_id

    @last_job_id.setter
    def last_job_id(self, last_job_id):
        """Sets the last_job_id of this InstanceStatusView.

        最近Job ID。

        :param last_job_id: The last_job_id of this InstanceStatusView.
        :type last_job_id: str
        """
        self._last_job_id = last_job_id

    @property
    def last_job_status(self):
        """Gets the last_job_status of this InstanceStatusView.

        最近Job的状态

        :return: The last_job_status of this InstanceStatusView.
        :rtype: str
        """
        return self._last_job_status

    @last_job_status.setter
    def last_job_status(self, last_job_status):
        """Sets the last_job_status of this InstanceStatusView.

        最近Job的状态

        :param last_job_status: The last_job_status of this InstanceStatusView.
        :type last_job_status: str
        """
        self._last_job_status = last_job_status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this InstanceStatusView.

        企业项目ID。

        :return: The enterprise_project_id of this InstanceStatusView.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this InstanceStatusView.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this InstanceStatusView.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, InstanceStatusView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
