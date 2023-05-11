# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueStatus:

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
        'status_id': 'int',
        'name': 'str',
        'tracker_ids': 'list[int]',
        'status_attribute': 'StatusAttribute'
    }

    attribute_map = {
        'id': 'id',
        'status_id': 'status_id',
        'name': 'name',
        'tracker_ids': 'tracker_ids',
        'status_attribute': 'status_attribute'
    }

    def __init__(self, id=None, status_id=None, name=None, tracker_ids=None, status_attribute=None):
        """IssueStatus

        The model defined in huaweicloud sdk

        :param id: 状态uuid
        :type id: str
        :param status_id: 状态数字id
        :type status_id: int
        :param name: 状态名称
        :type name: str
        :param tracker_ids: 关联的工作项类型列表
        :type tracker_ids: list[int]
        :param status_attribute: 
        :type status_attribute: :class:`huaweicloudsdkprojectman.v4.StatusAttribute`
        """
        
        

        self._id = None
        self._status_id = None
        self._name = None
        self._tracker_ids = None
        self._status_attribute = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status_id is not None:
            self.status_id = status_id
        if name is not None:
            self.name = name
        if tracker_ids is not None:
            self.tracker_ids = tracker_ids
        if status_attribute is not None:
            self.status_attribute = status_attribute

    @property
    def id(self):
        """Gets the id of this IssueStatus.

        状态uuid

        :return: The id of this IssueStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IssueStatus.

        状态uuid

        :param id: The id of this IssueStatus.
        :type id: str
        """
        self._id = id

    @property
    def status_id(self):
        """Gets the status_id of this IssueStatus.

        状态数字id

        :return: The status_id of this IssueStatus.
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this IssueStatus.

        状态数字id

        :param status_id: The status_id of this IssueStatus.
        :type status_id: int
        """
        self._status_id = status_id

    @property
    def name(self):
        """Gets the name of this IssueStatus.

        状态名称

        :return: The name of this IssueStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IssueStatus.

        状态名称

        :param name: The name of this IssueStatus.
        :type name: str
        """
        self._name = name

    @property
    def tracker_ids(self):
        """Gets the tracker_ids of this IssueStatus.

        关联的工作项类型列表

        :return: The tracker_ids of this IssueStatus.
        :rtype: list[int]
        """
        return self._tracker_ids

    @tracker_ids.setter
    def tracker_ids(self, tracker_ids):
        """Sets the tracker_ids of this IssueStatus.

        关联的工作项类型列表

        :param tracker_ids: The tracker_ids of this IssueStatus.
        :type tracker_ids: list[int]
        """
        self._tracker_ids = tracker_ids

    @property
    def status_attribute(self):
        """Gets the status_attribute of this IssueStatus.

        :return: The status_attribute of this IssueStatus.
        :rtype: :class:`huaweicloudsdkprojectman.v4.StatusAttribute`
        """
        return self._status_attribute

    @status_attribute.setter
    def status_attribute(self, status_attribute):
        """Sets the status_attribute of this IssueStatus.

        :param status_attribute: The status_attribute of this IssueStatus.
        :type status_attribute: :class:`huaweicloudsdkprojectman.v4.StatusAttribute`
        """
        self._status_attribute = status_attribute

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
        if not isinstance(other, IssueStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
