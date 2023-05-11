# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActivateRecordRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'update_time': 'str',
        'active_status': 'str',
        'project_id': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'update_time': 'update_time',
        'active_status': 'active_status',
        'project_id': 'project_id',
        'node_id': 'node_id'
    }

    def __init__(self, update_time=None, active_status=None, project_id=None, node_id=None):
        """ActivateRecordRecords

        The model defined in huaweicloud sdk

        :param update_time: 更新时间
        :type update_time: str
        :param active_status: 激活状态
        :type active_status: str
        :param project_id: 项目ID
        :type project_id: str
        :param node_id: 节点ID
        :type node_id: str
        """
        
        

        self._update_time = None
        self._active_status = None
        self._project_id = None
        self._node_id = None
        self.discriminator = None

        if update_time is not None:
            self.update_time = update_time
        if active_status is not None:
            self.active_status = active_status
        if project_id is not None:
            self.project_id = project_id
        if node_id is not None:
            self.node_id = node_id

    @property
    def update_time(self):
        """Gets the update_time of this ActivateRecordRecords.

        更新时间

        :return: The update_time of this ActivateRecordRecords.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ActivateRecordRecords.

        更新时间

        :param update_time: The update_time of this ActivateRecordRecords.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def active_status(self):
        """Gets the active_status of this ActivateRecordRecords.

        激活状态

        :return: The active_status of this ActivateRecordRecords.
        :rtype: str
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this ActivateRecordRecords.

        激活状态

        :param active_status: The active_status of this ActivateRecordRecords.
        :type active_status: str
        """
        self._active_status = active_status

    @property
    def project_id(self):
        """Gets the project_id of this ActivateRecordRecords.

        项目ID

        :return: The project_id of this ActivateRecordRecords.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ActivateRecordRecords.

        项目ID

        :param project_id: The project_id of this ActivateRecordRecords.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def node_id(self):
        """Gets the node_id of this ActivateRecordRecords.

        节点ID

        :return: The node_id of this ActivateRecordRecords.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ActivateRecordRecords.

        节点ID

        :param node_id: The node_id of this ActivateRecordRecords.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, ActivateRecordRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
