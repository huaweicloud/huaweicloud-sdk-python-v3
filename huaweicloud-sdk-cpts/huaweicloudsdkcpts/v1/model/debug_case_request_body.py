# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugCaseRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'cluster_id': 'int',
        'cluster_type': 'str',
        'without_package': 'int'
    }

    attribute_map = {
        'status': 'status',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'without_package': 'without_package'
    }

    def __init__(self, status=None, cluster_id=None, cluster_type=None, without_package=None):
        """DebugCaseRequestBody

        The model defined in huaweicloud sdk

        :param status: status
        :type status: int
        :param cluster_id: cluster_id
        :type cluster_id: int
        :param cluster_type: cluster_type
        :type cluster_type: str
        :param without_package: without_package
        :type without_package: int
        """
        
        

        self._status = None
        self._cluster_id = None
        self._cluster_type = None
        self._without_package = None
        self.discriminator = None

        self.status = status
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.without_package = without_package

    @property
    def status(self):
        """Gets the status of this DebugCaseRequestBody.

        status

        :return: The status of this DebugCaseRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DebugCaseRequestBody.

        status

        :param status: The status of this DebugCaseRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DebugCaseRequestBody.

        cluster_id

        :return: The cluster_id of this DebugCaseRequestBody.
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DebugCaseRequestBody.

        cluster_id

        :param cluster_id: The cluster_id of this DebugCaseRequestBody.
        :type cluster_id: int
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        """Gets the cluster_type of this DebugCaseRequestBody.

        cluster_type

        :return: The cluster_type of this DebugCaseRequestBody.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this DebugCaseRequestBody.

        cluster_type

        :param cluster_type: The cluster_type of this DebugCaseRequestBody.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def without_package(self):
        """Gets the without_package of this DebugCaseRequestBody.

        without_package

        :return: The without_package of this DebugCaseRequestBody.
        :rtype: int
        """
        return self._without_package

    @without_package.setter
    def without_package(self, without_package):
        """Sets the without_package of this DebugCaseRequestBody.

        without_package

        :param without_package: The without_package of this DebugCaseRequestBody.
        :type without_package: int
        """
        self._without_package = without_package

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
        if not isinstance(other, DebugCaseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
