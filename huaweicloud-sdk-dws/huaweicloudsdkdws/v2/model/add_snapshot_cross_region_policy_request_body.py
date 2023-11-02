# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSnapshotCrossRegionPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'destination_project_id': 'str',
        'destination_region': 'str',
        'status': 'bool',
        'back_keep_day': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'destination_project_id': 'destination_project_id',
        'destination_region': 'destination_region',
        'status': 'status',
        'back_keep_day': 'back_keep_day'
    }

    def __init__(self, cluster_id=None, destination_project_id=None, destination_region=None, status=None, back_keep_day=None):
        """AddSnapshotCrossRegionPolicyRequestBody

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param destination_project_id: 目的项目ID
        :type destination_project_id: str
        :param destination_region: 目的区域
        :type destination_region: str
        :param status: 状态
        :type status: bool
        :param back_keep_day: 保留天数
        :type back_keep_day: int
        """
        
        

        self._cluster_id = None
        self._destination_project_id = None
        self._destination_region = None
        self._status = None
        self._back_keep_day = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.destination_project_id = destination_project_id
        self.destination_region = destination_region
        self.status = status
        self.back_keep_day = back_keep_day

    @property
    def cluster_id(self):
        """Gets the cluster_id of this AddSnapshotCrossRegionPolicyRequestBody.

        集群ID

        :return: The cluster_id of this AddSnapshotCrossRegionPolicyRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this AddSnapshotCrossRegionPolicyRequestBody.

        集群ID

        :param cluster_id: The cluster_id of this AddSnapshotCrossRegionPolicyRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def destination_project_id(self):
        """Gets the destination_project_id of this AddSnapshotCrossRegionPolicyRequestBody.

        目的项目ID

        :return: The destination_project_id of this AddSnapshotCrossRegionPolicyRequestBody.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        """Sets the destination_project_id of this AddSnapshotCrossRegionPolicyRequestBody.

        目的项目ID

        :param destination_project_id: The destination_project_id of this AddSnapshotCrossRegionPolicyRequestBody.
        :type destination_project_id: str
        """
        self._destination_project_id = destination_project_id

    @property
    def destination_region(self):
        """Gets the destination_region of this AddSnapshotCrossRegionPolicyRequestBody.

        目的区域

        :return: The destination_region of this AddSnapshotCrossRegionPolicyRequestBody.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """Sets the destination_region of this AddSnapshotCrossRegionPolicyRequestBody.

        目的区域

        :param destination_region: The destination_region of this AddSnapshotCrossRegionPolicyRequestBody.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def status(self):
        """Gets the status of this AddSnapshotCrossRegionPolicyRequestBody.

        状态

        :return: The status of this AddSnapshotCrossRegionPolicyRequestBody.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AddSnapshotCrossRegionPolicyRequestBody.

        状态

        :param status: The status of this AddSnapshotCrossRegionPolicyRequestBody.
        :type status: bool
        """
        self._status = status

    @property
    def back_keep_day(self):
        """Gets the back_keep_day of this AddSnapshotCrossRegionPolicyRequestBody.

        保留天数

        :return: The back_keep_day of this AddSnapshotCrossRegionPolicyRequestBody.
        :rtype: int
        """
        return self._back_keep_day

    @back_keep_day.setter
    def back_keep_day(self, back_keep_day):
        """Sets the back_keep_day of this AddSnapshotCrossRegionPolicyRequestBody.

        保留天数

        :param back_keep_day: The back_keep_day of this AddSnapshotCrossRegionPolicyRequestBody.
        :type back_keep_day: int
        """
        self._back_keep_day = back_keep_day

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
        if not isinstance(other, AddSnapshotCrossRegionPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
