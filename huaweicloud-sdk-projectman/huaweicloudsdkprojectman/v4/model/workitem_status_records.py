# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkitemStatusRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'work_item_record_id': 'str',
        'work_item_id': 'str',
        'project_id': 'str',
        'work_item_statuses': 'list[WorkitemStatus]'
    }

    attribute_map = {
        'work_item_record_id': 'work_item_record_id',
        'work_item_id': 'work_item_id',
        'project_id': 'project_id',
        'work_item_statuses': 'work_item_statuses'
    }

    def __init__(self, work_item_record_id=None, work_item_id=None, project_id=None, work_item_statuses=None):
        """WorkitemStatusRecords

        The model defined in huaweicloud sdk

        :param work_item_record_id: 工作项的记录id，一个工作项对应一条记录
        :type work_item_record_id: str
        :param work_item_id: 工作项id
        :type work_item_id: str
        :param project_id: devcloud项目的32位id
        :type project_id: str
        :param work_item_statuses: 操作历史
        :type work_item_statuses: list[:class:`huaweicloudsdkprojectman.v4.WorkitemStatus`]
        """
        
        

        self._work_item_record_id = None
        self._work_item_id = None
        self._project_id = None
        self._work_item_statuses = None
        self.discriminator = None

        if work_item_record_id is not None:
            self.work_item_record_id = work_item_record_id
        if work_item_id is not None:
            self.work_item_id = work_item_id
        if project_id is not None:
            self.project_id = project_id
        if work_item_statuses is not None:
            self.work_item_statuses = work_item_statuses

    @property
    def work_item_record_id(self):
        """Gets the work_item_record_id of this WorkitemStatusRecords.

        工作项的记录id，一个工作项对应一条记录

        :return: The work_item_record_id of this WorkitemStatusRecords.
        :rtype: str
        """
        return self._work_item_record_id

    @work_item_record_id.setter
    def work_item_record_id(self, work_item_record_id):
        """Sets the work_item_record_id of this WorkitemStatusRecords.

        工作项的记录id，一个工作项对应一条记录

        :param work_item_record_id: The work_item_record_id of this WorkitemStatusRecords.
        :type work_item_record_id: str
        """
        self._work_item_record_id = work_item_record_id

    @property
    def work_item_id(self):
        """Gets the work_item_id of this WorkitemStatusRecords.

        工作项id

        :return: The work_item_id of this WorkitemStatusRecords.
        :rtype: str
        """
        return self._work_item_id

    @work_item_id.setter
    def work_item_id(self, work_item_id):
        """Sets the work_item_id of this WorkitemStatusRecords.

        工作项id

        :param work_item_id: The work_item_id of this WorkitemStatusRecords.
        :type work_item_id: str
        """
        self._work_item_id = work_item_id

    @property
    def project_id(self):
        """Gets the project_id of this WorkitemStatusRecords.

        devcloud项目的32位id

        :return: The project_id of this WorkitemStatusRecords.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this WorkitemStatusRecords.

        devcloud项目的32位id

        :param project_id: The project_id of this WorkitemStatusRecords.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def work_item_statuses(self):
        """Gets the work_item_statuses of this WorkitemStatusRecords.

        操作历史

        :return: The work_item_statuses of this WorkitemStatusRecords.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkitemStatus`]
        """
        return self._work_item_statuses

    @work_item_statuses.setter
    def work_item_statuses(self, work_item_statuses):
        """Sets the work_item_statuses of this WorkitemStatusRecords.

        操作历史

        :param work_item_statuses: The work_item_statuses of this WorkitemStatusRecords.
        :type work_item_statuses: list[:class:`huaweicloudsdkprojectman.v4.WorkitemStatus`]
        """
        self._work_item_statuses = work_item_statuses

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
        if not isinstance(other, WorkitemStatusRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
