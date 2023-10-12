# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppsDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'dlm_type': 'str',
        'app_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'time_unit': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'app_id': 'app_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'time_unit': 'time_unit'
    }

    def __init__(self, workspace=None, dlm_type=None, app_id=None, start_time=None, end_time=None, time_unit=None):
        """ShowAppsDetailRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param dlm_type: dlm版本类型
        :type dlm_type: str
        :param app_id: app编号
        :type app_id: str
        :param start_time: 开始时间（13位时间戳）
        :type start_time: int
        :param end_time: 结束时间（13位时间戳）
        :type end_time: int
        :param time_unit: 时间单位
        :type time_unit: str
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._app_id = None
        self._start_time = None
        self._end_time = None
        self._time_unit = None
        self.discriminator = None

        self.workspace = workspace
        self.dlm_type = dlm_type
        self.app_id = app_id
        self.start_time = start_time
        self.end_time = end_time
        self.time_unit = time_unit

    @property
    def workspace(self):
        """Gets the workspace of this ShowAppsDetailRequest.

        工作空间id

        :return: The workspace of this ShowAppsDetailRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowAppsDetailRequest.

        工作空间id

        :param workspace: The workspace of this ShowAppsDetailRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        """Gets the dlm_type of this ShowAppsDetailRequest.

        dlm版本类型

        :return: The dlm_type of this ShowAppsDetailRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        """Sets the dlm_type of this ShowAppsDetailRequest.

        dlm版本类型

        :param dlm_type: The dlm_type of this ShowAppsDetailRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def app_id(self):
        """Gets the app_id of this ShowAppsDetailRequest.

        app编号

        :return: The app_id of this ShowAppsDetailRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowAppsDetailRequest.

        app编号

        :param app_id: The app_id of this ShowAppsDetailRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def start_time(self):
        """Gets the start_time of this ShowAppsDetailRequest.

        开始时间（13位时间戳）

        :return: The start_time of this ShowAppsDetailRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowAppsDetailRequest.

        开始时间（13位时间戳）

        :param start_time: The start_time of this ShowAppsDetailRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowAppsDetailRequest.

        结束时间（13位时间戳）

        :return: The end_time of this ShowAppsDetailRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowAppsDetailRequest.

        结束时间（13位时间戳）

        :param end_time: The end_time of this ShowAppsDetailRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def time_unit(self):
        """Gets the time_unit of this ShowAppsDetailRequest.

        时间单位

        :return: The time_unit of this ShowAppsDetailRequest.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this ShowAppsDetailRequest.

        时间单位

        :param time_unit: The time_unit of this ShowAppsDetailRequest.
        :type time_unit: str
        """
        self._time_unit = time_unit

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
        if not isinstance(other, ShowAppsDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
