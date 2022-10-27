# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionOnComponentSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'snapshot_index': 'int',
        'replica': 'int',
        'source': 'Source',
        'resource_limit': 'ResourceLimitForUpgrade'
    }

    attribute_map = {
        'snapshot_index': 'snapshot_index',
        'replica': 'replica',
        'source': 'source',
        'resource_limit': 'resource_limit'
    }

    def __init__(self, snapshot_index=None, replica=None, source=None, resource_limit=None):
        """ActionOnComponentSpec

        The model defined in huaweicloud sdk

        :param snapshot_index: 快照序号。
        :type snapshot_index: int
        :param replica: 副本数目。
        :type replica: int
        :param source: 
        :type source: :class:`huaweicloudsdkcae.v1.Source`
        :param resource_limit: 
        :type resource_limit: :class:`huaweicloudsdkcae.v1.ResourceLimitForUpgrade`
        """
        
        

        self._snapshot_index = None
        self._replica = None
        self._source = None
        self._resource_limit = None
        self.discriminator = None

        if snapshot_index is not None:
            self.snapshot_index = snapshot_index
        if replica is not None:
            self.replica = replica
        if source is not None:
            self.source = source
        if resource_limit is not None:
            self.resource_limit = resource_limit

    @property
    def snapshot_index(self):
        """Gets the snapshot_index of this ActionOnComponentSpec.

        快照序号。

        :return: The snapshot_index of this ActionOnComponentSpec.
        :rtype: int
        """
        return self._snapshot_index

    @snapshot_index.setter
    def snapshot_index(self, snapshot_index):
        """Sets the snapshot_index of this ActionOnComponentSpec.

        快照序号。

        :param snapshot_index: The snapshot_index of this ActionOnComponentSpec.
        :type snapshot_index: int
        """
        self._snapshot_index = snapshot_index

    @property
    def replica(self):
        """Gets the replica of this ActionOnComponentSpec.

        副本数目。

        :return: The replica of this ActionOnComponentSpec.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        """Sets the replica of this ActionOnComponentSpec.

        副本数目。

        :param replica: The replica of this ActionOnComponentSpec.
        :type replica: int
        """
        self._replica = replica

    @property
    def source(self):
        """Gets the source of this ActionOnComponentSpec.


        :return: The source of this ActionOnComponentSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.Source`
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ActionOnComponentSpec.


        :param source: The source of this ActionOnComponentSpec.
        :type source: :class:`huaweicloudsdkcae.v1.Source`
        """
        self._source = source

    @property
    def resource_limit(self):
        """Gets the resource_limit of this ActionOnComponentSpec.


        :return: The resource_limit of this ActionOnComponentSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.ResourceLimitForUpgrade`
        """
        return self._resource_limit

    @resource_limit.setter
    def resource_limit(self, resource_limit):
        """Sets the resource_limit of this ActionOnComponentSpec.


        :param resource_limit: The resource_limit of this ActionOnComponentSpec.
        :type resource_limit: :class:`huaweicloudsdkcae.v1.ResourceLimitForUpgrade`
        """
        self._resource_limit = resource_limit

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
        if not isinstance(other, ActionOnComponentSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
