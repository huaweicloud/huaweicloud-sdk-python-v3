# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectVersionsV4ResponseBodyIterations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'end_time': 'str',
        'id': 'int',
        'name': 'str',
        'begin_time': 'str',
        'status': 'str',
        'updated_time': 'int',
        'deleted': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'end_time': 'end_time',
        'id': 'id',
        'name': 'name',
        'begin_time': 'begin_time',
        'status': 'status',
        'updated_time': 'updated_time',
        'deleted': 'deleted'
    }

    def __init__(self, description=None, end_time=None, id=None, name=None, begin_time=None, status=None, updated_time=None, deleted=None):
        """ListProjectVersionsV4ResponseBodyIterations

        The model defined in huaweicloud sdk

        :param description: 迭代描述
        :type description: str
        :param end_time: 迭代结束时间
        :type end_time: str
        :param id: 迭代id
        :type id: int
        :param name: 迭代标题
        :type name: str
        :param begin_time: 迭代开始时间
        :type begin_time: str
        :param status: 迭代状态
        :type status: str
        :param updated_time: 迭代更新时间，长整型时间戳
        :type updated_time: int
        :param deleted: 迭代是否已经删除，false, 未删除， true已经删除
        :type deleted: bool
        """
        
        

        self._description = None
        self._end_time = None
        self._id = None
        self._name = None
        self._begin_time = None
        self._status = None
        self._updated_time = None
        self._deleted = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if end_time is not None:
            self.end_time = end_time
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if begin_time is not None:
            self.begin_time = begin_time
        if status is not None:
            self.status = status
        if updated_time is not None:
            self.updated_time = updated_time
        if deleted is not None:
            self.deleted = deleted

    @property
    def description(self):
        """Gets the description of this ListProjectVersionsV4ResponseBodyIterations.

        迭代描述

        :return: The description of this ListProjectVersionsV4ResponseBodyIterations.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListProjectVersionsV4ResponseBodyIterations.

        迭代描述

        :param description: The description of this ListProjectVersionsV4ResponseBodyIterations.
        :type description: str
        """
        self._description = description

    @property
    def end_time(self):
        """Gets the end_time of this ListProjectVersionsV4ResponseBodyIterations.

        迭代结束时间

        :return: The end_time of this ListProjectVersionsV4ResponseBodyIterations.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListProjectVersionsV4ResponseBodyIterations.

        迭代结束时间

        :param end_time: The end_time of this ListProjectVersionsV4ResponseBodyIterations.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def id(self):
        """Gets the id of this ListProjectVersionsV4ResponseBodyIterations.

        迭代id

        :return: The id of this ListProjectVersionsV4ResponseBodyIterations.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListProjectVersionsV4ResponseBodyIterations.

        迭代id

        :param id: The id of this ListProjectVersionsV4ResponseBodyIterations.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListProjectVersionsV4ResponseBodyIterations.

        迭代标题

        :return: The name of this ListProjectVersionsV4ResponseBodyIterations.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListProjectVersionsV4ResponseBodyIterations.

        迭代标题

        :param name: The name of this ListProjectVersionsV4ResponseBodyIterations.
        :type name: str
        """
        self._name = name

    @property
    def begin_time(self):
        """Gets the begin_time of this ListProjectVersionsV4ResponseBodyIterations.

        迭代开始时间

        :return: The begin_time of this ListProjectVersionsV4ResponseBodyIterations.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListProjectVersionsV4ResponseBodyIterations.

        迭代开始时间

        :param begin_time: The begin_time of this ListProjectVersionsV4ResponseBodyIterations.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def status(self):
        """Gets the status of this ListProjectVersionsV4ResponseBodyIterations.

        迭代状态

        :return: The status of this ListProjectVersionsV4ResponseBodyIterations.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListProjectVersionsV4ResponseBodyIterations.

        迭代状态

        :param status: The status of this ListProjectVersionsV4ResponseBodyIterations.
        :type status: str
        """
        self._status = status

    @property
    def updated_time(self):
        """Gets the updated_time of this ListProjectVersionsV4ResponseBodyIterations.

        迭代更新时间，长整型时间戳

        :return: The updated_time of this ListProjectVersionsV4ResponseBodyIterations.
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ListProjectVersionsV4ResponseBodyIterations.

        迭代更新时间，长整型时间戳

        :param updated_time: The updated_time of this ListProjectVersionsV4ResponseBodyIterations.
        :type updated_time: int
        """
        self._updated_time = updated_time

    @property
    def deleted(self):
        """Gets the deleted of this ListProjectVersionsV4ResponseBodyIterations.

        迭代是否已经删除，false, 未删除， true已经删除

        :return: The deleted of this ListProjectVersionsV4ResponseBodyIterations.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ListProjectVersionsV4ResponseBodyIterations.

        迭代是否已经删除，false, 未删除， true已经删除

        :param deleted: The deleted of this ListProjectVersionsV4ResponseBodyIterations.
        :type deleted: bool
        """
        self._deleted = deleted

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
        if not isinstance(other, ListProjectVersionsV4ResponseBodyIterations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
