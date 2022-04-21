# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueRecordV4:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'created_time': 'int',
        'user': 'IssueRecordV4User',
        'details': 'list[IssueRecordV4Details]'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'created_time',
        'user': 'user',
        'details': 'details'
    }

    def __init__(self, id=None, created_time=None, user=None, details=None):
        """IssueRecordV4

        The model defined in huaweicloud sdk

        :param id: 操作记录id
        :type id: int
        :param created_time: 操作记录创建时间
        :type created_time: int
        :param user: 
        :type user: :class:`huaweicloudsdkprojectman.v4.IssueRecordV4User`
        :param details: 操作的记录
        :type details: list[:class:`huaweicloudsdkprojectman.v4.IssueRecordV4Details`]
        """
        
        

        self._id = None
        self._created_time = None
        self._user = None
        self._details = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if user is not None:
            self.user = user
        if details is not None:
            self.details = details

    @property
    def id(self):
        """Gets the id of this IssueRecordV4.

        操作记录id

        :return: The id of this IssueRecordV4.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IssueRecordV4.

        操作记录id

        :param id: The id of this IssueRecordV4.
        :type id: int
        """
        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this IssueRecordV4.

        操作记录创建时间

        :return: The created_time of this IssueRecordV4.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this IssueRecordV4.

        操作记录创建时间

        :param created_time: The created_time of this IssueRecordV4.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def user(self):
        """Gets the user of this IssueRecordV4.


        :return: The user of this IssueRecordV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueRecordV4User`
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this IssueRecordV4.


        :param user: The user of this IssueRecordV4.
        :type user: :class:`huaweicloudsdkprojectman.v4.IssueRecordV4User`
        """
        self._user = user

    @property
    def details(self):
        """Gets the details of this IssueRecordV4.

        操作的记录

        :return: The details of this IssueRecordV4.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueRecordV4Details`]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this IssueRecordV4.

        操作的记录

        :param details: The details of this IssueRecordV4.
        :type details: list[:class:`huaweicloudsdkprojectman.v4.IssueRecordV4Details`]
        """
        self._details = details

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
        if not isinstance(other, IssueRecordV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
