# coding: utf-8

import pprint
import re

import six





class OpExtendInfoCommon:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'progress': 'int',
        'request_id': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'progress': 'progress',
        'request_id': 'request_id',
        'task_id': 'task_id'
    }

    def __init__(self, progress=None, request_id=None, task_id=None):
        """OpExtendInfoCommon - a model defined in huaweicloud sdk"""
        
        

        self._progress = None
        self._request_id = None
        self._task_id = None
        self.discriminator = None

        self.progress = progress
        self.request_id = request_id
        if task_id is not None:
            self.task_id = task_id

    @property
    def progress(self):
        """Gets the progress of this OpExtendInfoCommon.

        进度，取值为0-100

        :return: The progress of this OpExtendInfoCommon.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this OpExtendInfoCommon.

        进度，取值为0-100

        :param progress: The progress of this OpExtendInfoCommon.
        :type: int
        """
        self._progress = progress

    @property
    def request_id(self):
        """Gets the request_id of this OpExtendInfoCommon.

        请求id

        :return: The request_id of this OpExtendInfoCommon.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this OpExtendInfoCommon.

        请求id

        :param request_id: The request_id of this OpExtendInfoCommon.
        :type: str
        """
        self._request_id = request_id

    @property
    def task_id(self):
        """Gets the task_id of this OpExtendInfoCommon.

        备份任务id

        :return: The task_id of this OpExtendInfoCommon.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this OpExtendInfoCommon.

        备份任务id

        :param task_id: The task_id of this OpExtendInfoCommon.
        :type: str
        """
        self._task_id = task_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OpExtendInfoCommon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
