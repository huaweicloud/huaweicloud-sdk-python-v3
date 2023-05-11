# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionProgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creating': 'str',
        'growing': 'str',
        'restoring': 'str',
        'snapshotting': 'str',
        'repairing': 'str'
    }

    attribute_map = {
        'creating': 'CREATING',
        'growing': 'GROWING',
        'restoring': 'RESTORING',
        'snapshotting': 'SNAPSHOTTING',
        'repairing': 'REPAIRING'
    }

    def __init__(self, creating=None, growing=None, restoring=None, snapshotting=None, repairing=None):
        """ActionProgress

        The model defined in huaweicloud sdk

        :param creating: 创建集群进度，例如：29%
        :type creating: str
        :param growing: 扩容集群进度，例如：29%
        :type growing: str
        :param restoring: 恢复集群进度，例如：29%
        :type restoring: str
        :param snapshotting: 集群快照进度，例如：29%
        :type snapshotting: str
        :param repairing: 修复集群进度，例如：29%
        :type repairing: str
        """
        
        

        self._creating = None
        self._growing = None
        self._restoring = None
        self._snapshotting = None
        self._repairing = None
        self.discriminator = None

        if creating is not None:
            self.creating = creating
        if growing is not None:
            self.growing = growing
        if restoring is not None:
            self.restoring = restoring
        if snapshotting is not None:
            self.snapshotting = snapshotting
        if repairing is not None:
            self.repairing = repairing

    @property
    def creating(self):
        """Gets the creating of this ActionProgress.

        创建集群进度，例如：29%

        :return: The creating of this ActionProgress.
        :rtype: str
        """
        return self._creating

    @creating.setter
    def creating(self, creating):
        """Sets the creating of this ActionProgress.

        创建集群进度，例如：29%

        :param creating: The creating of this ActionProgress.
        :type creating: str
        """
        self._creating = creating

    @property
    def growing(self):
        """Gets the growing of this ActionProgress.

        扩容集群进度，例如：29%

        :return: The growing of this ActionProgress.
        :rtype: str
        """
        return self._growing

    @growing.setter
    def growing(self, growing):
        """Sets the growing of this ActionProgress.

        扩容集群进度，例如：29%

        :param growing: The growing of this ActionProgress.
        :type growing: str
        """
        self._growing = growing

    @property
    def restoring(self):
        """Gets the restoring of this ActionProgress.

        恢复集群进度，例如：29%

        :return: The restoring of this ActionProgress.
        :rtype: str
        """
        return self._restoring

    @restoring.setter
    def restoring(self, restoring):
        """Sets the restoring of this ActionProgress.

        恢复集群进度，例如：29%

        :param restoring: The restoring of this ActionProgress.
        :type restoring: str
        """
        self._restoring = restoring

    @property
    def snapshotting(self):
        """Gets the snapshotting of this ActionProgress.

        集群快照进度，例如：29%

        :return: The snapshotting of this ActionProgress.
        :rtype: str
        """
        return self._snapshotting

    @snapshotting.setter
    def snapshotting(self, snapshotting):
        """Sets the snapshotting of this ActionProgress.

        集群快照进度，例如：29%

        :param snapshotting: The snapshotting of this ActionProgress.
        :type snapshotting: str
        """
        self._snapshotting = snapshotting

    @property
    def repairing(self):
        """Gets the repairing of this ActionProgress.

        修复集群进度，例如：29%

        :return: The repairing of this ActionProgress.
        :rtype: str
        """
        return self._repairing

    @repairing.setter
    def repairing(self, repairing):
        """Sets the repairing of this ActionProgress.

        修复集群进度，例如：29%

        :param repairing: The repairing of this ActionProgress.
        :type repairing: str
        """
        self._repairing = repairing

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
        if not isinstance(other, ActionProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
