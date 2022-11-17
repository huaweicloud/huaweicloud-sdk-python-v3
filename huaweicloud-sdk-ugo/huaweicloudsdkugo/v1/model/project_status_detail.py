# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectStatusDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_collection_status': 'str',
        'object_collection_progress': 'str',
        'pre_migration_status': 'str',
        'pre_migration_progress': 'str'
    }

    attribute_map = {
        'object_collection_status': 'object_collection_status',
        'object_collection_progress': 'object_collection_progress',
        'pre_migration_status': 'pre_migration_status',
        'pre_migration_progress': 'pre_migration_progress'
    }

    def __init__(self, object_collection_status=None, object_collection_progress=None, pre_migration_status=None, pre_migration_progress=None):
        """ProjectStatusDetail

        The model defined in huaweicloud sdk

        :param object_collection_status: 采集的状态。
        :type object_collection_status: str
        :param object_collection_progress: 采集的进度。
        :type object_collection_progress: str
        :param pre_migration_status: 评估的状态。
        :type pre_migration_status: str
        :param pre_migration_progress: 评估的进度。
        :type pre_migration_progress: str
        """
        
        

        self._object_collection_status = None
        self._object_collection_progress = None
        self._pre_migration_status = None
        self._pre_migration_progress = None
        self.discriminator = None

        if object_collection_status is not None:
            self.object_collection_status = object_collection_status
        if object_collection_progress is not None:
            self.object_collection_progress = object_collection_progress
        if pre_migration_status is not None:
            self.pre_migration_status = pre_migration_status
        if pre_migration_progress is not None:
            self.pre_migration_progress = pre_migration_progress

    @property
    def object_collection_status(self):
        """Gets the object_collection_status of this ProjectStatusDetail.

        采集的状态。

        :return: The object_collection_status of this ProjectStatusDetail.
        :rtype: str
        """
        return self._object_collection_status

    @object_collection_status.setter
    def object_collection_status(self, object_collection_status):
        """Sets the object_collection_status of this ProjectStatusDetail.

        采集的状态。

        :param object_collection_status: The object_collection_status of this ProjectStatusDetail.
        :type object_collection_status: str
        """
        self._object_collection_status = object_collection_status

    @property
    def object_collection_progress(self):
        """Gets the object_collection_progress of this ProjectStatusDetail.

        采集的进度。

        :return: The object_collection_progress of this ProjectStatusDetail.
        :rtype: str
        """
        return self._object_collection_progress

    @object_collection_progress.setter
    def object_collection_progress(self, object_collection_progress):
        """Sets the object_collection_progress of this ProjectStatusDetail.

        采集的进度。

        :param object_collection_progress: The object_collection_progress of this ProjectStatusDetail.
        :type object_collection_progress: str
        """
        self._object_collection_progress = object_collection_progress

    @property
    def pre_migration_status(self):
        """Gets the pre_migration_status of this ProjectStatusDetail.

        评估的状态。

        :return: The pre_migration_status of this ProjectStatusDetail.
        :rtype: str
        """
        return self._pre_migration_status

    @pre_migration_status.setter
    def pre_migration_status(self, pre_migration_status):
        """Sets the pre_migration_status of this ProjectStatusDetail.

        评估的状态。

        :param pre_migration_status: The pre_migration_status of this ProjectStatusDetail.
        :type pre_migration_status: str
        """
        self._pre_migration_status = pre_migration_status

    @property
    def pre_migration_progress(self):
        """Gets the pre_migration_progress of this ProjectStatusDetail.

        评估的进度。

        :return: The pre_migration_progress of this ProjectStatusDetail.
        :rtype: str
        """
        return self._pre_migration_progress

    @pre_migration_progress.setter
    def pre_migration_progress(self, pre_migration_progress):
        """Sets the pre_migration_progress of this ProjectStatusDetail.

        评估的进度。

        :param pre_migration_progress: The pre_migration_progress of this ProjectStatusDetail.
        :type pre_migration_progress: str
        """
        self._pre_migration_progress = pre_migration_progress

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
        if not isinstance(other, ProjectStatusDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
