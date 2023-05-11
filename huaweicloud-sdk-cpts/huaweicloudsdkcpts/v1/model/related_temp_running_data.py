# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelatedTempRunningData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_run_info_id': 'int',
        'related_temp_running_id': 'int',
        'temp_id': 'int',
        'temp_name': 'str',
        'related_temp_running_data': 'list[TempRunningData]'
    }

    attribute_map = {
        'task_run_info_id': 'task_run_info_id',
        'related_temp_running_id': 'related_temp_running_id',
        'temp_id': 'temp_id',
        'temp_name': 'temp_name',
        'related_temp_running_data': 'related_temp_running_data'
    }

    def __init__(self, task_run_info_id=None, related_temp_running_id=None, temp_id=None, temp_name=None, related_temp_running_data=None):
        """RelatedTempRunningData

        The model defined in huaweicloud sdk

        :param task_run_info_id: task_run_info_id
        :type task_run_info_id: int
        :param related_temp_running_id: related_temp_running_id
        :type related_temp_running_id: int
        :param temp_id: temp_id
        :type temp_id: int
        :param temp_name: temp_name
        :type temp_name: str
        :param related_temp_running_data: related_temp_running_data
        :type related_temp_running_data: list[:class:`huaweicloudsdkcpts.v1.TempRunningData`]
        """
        
        

        self._task_run_info_id = None
        self._related_temp_running_id = None
        self._temp_id = None
        self._temp_name = None
        self._related_temp_running_data = None
        self.discriminator = None

        if task_run_info_id is not None:
            self.task_run_info_id = task_run_info_id
        if related_temp_running_id is not None:
            self.related_temp_running_id = related_temp_running_id
        if temp_id is not None:
            self.temp_id = temp_id
        if temp_name is not None:
            self.temp_name = temp_name
        if related_temp_running_data is not None:
            self.related_temp_running_data = related_temp_running_data

    @property
    def task_run_info_id(self):
        """Gets the task_run_info_id of this RelatedTempRunningData.

        task_run_info_id

        :return: The task_run_info_id of this RelatedTempRunningData.
        :rtype: int
        """
        return self._task_run_info_id

    @task_run_info_id.setter
    def task_run_info_id(self, task_run_info_id):
        """Sets the task_run_info_id of this RelatedTempRunningData.

        task_run_info_id

        :param task_run_info_id: The task_run_info_id of this RelatedTempRunningData.
        :type task_run_info_id: int
        """
        self._task_run_info_id = task_run_info_id

    @property
    def related_temp_running_id(self):
        """Gets the related_temp_running_id of this RelatedTempRunningData.

        related_temp_running_id

        :return: The related_temp_running_id of this RelatedTempRunningData.
        :rtype: int
        """
        return self._related_temp_running_id

    @related_temp_running_id.setter
    def related_temp_running_id(self, related_temp_running_id):
        """Sets the related_temp_running_id of this RelatedTempRunningData.

        related_temp_running_id

        :param related_temp_running_id: The related_temp_running_id of this RelatedTempRunningData.
        :type related_temp_running_id: int
        """
        self._related_temp_running_id = related_temp_running_id

    @property
    def temp_id(self):
        """Gets the temp_id of this RelatedTempRunningData.

        temp_id

        :return: The temp_id of this RelatedTempRunningData.
        :rtype: int
        """
        return self._temp_id

    @temp_id.setter
    def temp_id(self, temp_id):
        """Sets the temp_id of this RelatedTempRunningData.

        temp_id

        :param temp_id: The temp_id of this RelatedTempRunningData.
        :type temp_id: int
        """
        self._temp_id = temp_id

    @property
    def temp_name(self):
        """Gets the temp_name of this RelatedTempRunningData.

        temp_name

        :return: The temp_name of this RelatedTempRunningData.
        :rtype: str
        """
        return self._temp_name

    @temp_name.setter
    def temp_name(self, temp_name):
        """Sets the temp_name of this RelatedTempRunningData.

        temp_name

        :param temp_name: The temp_name of this RelatedTempRunningData.
        :type temp_name: str
        """
        self._temp_name = temp_name

    @property
    def related_temp_running_data(self):
        """Gets the related_temp_running_data of this RelatedTempRunningData.

        related_temp_running_data

        :return: The related_temp_running_data of this RelatedTempRunningData.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.TempRunningData`]
        """
        return self._related_temp_running_data

    @related_temp_running_data.setter
    def related_temp_running_data(self, related_temp_running_data):
        """Sets the related_temp_running_data of this RelatedTempRunningData.

        related_temp_running_data

        :param related_temp_running_data: The related_temp_running_data of this RelatedTempRunningData.
        :type related_temp_running_data: list[:class:`huaweicloudsdkcpts.v1.TempRunningData`]
        """
        self._related_temp_running_data = related_temp_running_data

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
        if not isinstance(other, RelatedTempRunningData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
