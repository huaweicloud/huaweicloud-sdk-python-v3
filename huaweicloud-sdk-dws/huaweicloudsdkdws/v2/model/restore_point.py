# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestorePoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'back_ref': 'str',
        'restore_time': 'int',
        'cluster_id': 'str'
    }

    attribute_map = {
        'back_ref': 'back_ref',
        'restore_time': 'restore_time',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, back_ref=None, restore_time=None, cluster_id=None):
        """RestorePoint

        The model defined in huaweicloud sdk

        :param back_ref: 快照ID
        :type back_ref: str
        :param restore_time: 恢复时间
        :type restore_time: int
        :param cluster_id: 集群ID
        :type cluster_id: str
        """
        
        

        self._back_ref = None
        self._restore_time = None
        self._cluster_id = None
        self.discriminator = None

        if back_ref is not None:
            self.back_ref = back_ref
        if restore_time is not None:
            self.restore_time = restore_time
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def back_ref(self):
        """Gets the back_ref of this RestorePoint.

        快照ID

        :return: The back_ref of this RestorePoint.
        :rtype: str
        """
        return self._back_ref

    @back_ref.setter
    def back_ref(self, back_ref):
        """Sets the back_ref of this RestorePoint.

        快照ID

        :param back_ref: The back_ref of this RestorePoint.
        :type back_ref: str
        """
        self._back_ref = back_ref

    @property
    def restore_time(self):
        """Gets the restore_time of this RestorePoint.

        恢复时间

        :return: The restore_time of this RestorePoint.
        :rtype: int
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this RestorePoint.

        恢复时间

        :param restore_time: The restore_time of this RestorePoint.
        :type restore_time: int
        """
        self._restore_time = restore_time

    @property
    def cluster_id(self):
        """Gets the cluster_id of this RestorePoint.

        集群ID

        :return: The cluster_id of this RestorePoint.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this RestorePoint.

        集群ID

        :param cluster_id: The cluster_id of this RestorePoint.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, RestorePoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
