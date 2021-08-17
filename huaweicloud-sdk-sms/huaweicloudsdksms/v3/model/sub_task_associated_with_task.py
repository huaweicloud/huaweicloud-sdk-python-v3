# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTaskAssociatedWithTask:


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
        'name': 'str',
        'progress': 'int',
        'start_date': 'int',
        'end_date': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'progress': 'progress',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, id=None, name=None, progress=None, start_date=None, end_date=None):
        """SubTaskAssociatedWithTask - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._progress = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if progress is not None:
            self.progress = progress
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def id(self):
        """Gets the id of this SubTaskAssociatedWithTask.

        子任务id

        :return: The id of this SubTaskAssociatedWithTask.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubTaskAssociatedWithTask.

        子任务id

        :param id: The id of this SubTaskAssociatedWithTask.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SubTaskAssociatedWithTask.

        子任务名称

        :return: The name of this SubTaskAssociatedWithTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubTaskAssociatedWithTask.

        子任务名称

        :param name: The name of this SubTaskAssociatedWithTask.
        :type: str
        """
        self._name = name

    @property
    def progress(self):
        """Gets the progress of this SubTaskAssociatedWithTask.

        子任务的进度，取值为0-100之间的整数

        :return: The progress of this SubTaskAssociatedWithTask.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this SubTaskAssociatedWithTask.

        子任务的进度，取值为0-100之间的整数

        :param progress: The progress of this SubTaskAssociatedWithTask.
        :type: int
        """
        self._progress = progress

    @property
    def start_date(self):
        """Gets the start_date of this SubTaskAssociatedWithTask.

        子任务开始时间

        :return: The start_date of this SubTaskAssociatedWithTask.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SubTaskAssociatedWithTask.

        子任务开始时间

        :param start_date: The start_date of this SubTaskAssociatedWithTask.
        :type: int
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SubTaskAssociatedWithTask.

        子任务结束时间（如果子任务还没有结束，则为空）

        :return: The end_date of this SubTaskAssociatedWithTask.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SubTaskAssociatedWithTask.

        子任务结束时间（如果子任务还没有结束，则为空）

        :param end_date: The end_date of this SubTaskAssociatedWithTask.
        :type: int
        """
        self._end_date = end_date

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
        if not isinstance(other, SubTaskAssociatedWithTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
