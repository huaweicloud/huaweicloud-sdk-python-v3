# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'record_id': 'str',
        'offset': 'str',
        'end_offset': 'str',
        'step_id': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'record_id': 'record_id',
        'offset': 'offset',
        'end_offset': 'end_offset',
        'step_id': 'step_id'
    }

    def __init__(self, app_id=None, record_id=None, offset=None, end_offset=None, step_id=None):
        r"""ShowTaskLogsRequest

        The model defined in huaweicloud sdk

        :param app_id: 应用id
        :type app_id: str
        :param record_id: 部署记录id
        :type record_id: str
        :param offset: 起始位置，默认0；长度1-19
        :type offset: str
        :param end_offset: 结束位置，开始为0；长度1-19
        :type end_offset: str
        :param step_id: 步骤id；如果传，则按step查询日志；长度1-60
        :type step_id: str
        """
        
        

        self._app_id = None
        self._record_id = None
        self._offset = None
        self._end_offset = None
        self._step_id = None
        self.discriminator = None

        self.app_id = app_id
        self.record_id = record_id
        self.offset = offset
        self.end_offset = end_offset
        if step_id is not None:
            self.step_id = step_id

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowTaskLogsRequest.

        应用id

        :return: The app_id of this ShowTaskLogsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowTaskLogsRequest.

        应用id

        :param app_id: The app_id of this ShowTaskLogsRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def record_id(self):
        r"""Gets the record_id of this ShowTaskLogsRequest.

        部署记录id

        :return: The record_id of this ShowTaskLogsRequest.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        r"""Sets the record_id of this ShowTaskLogsRequest.

        部署记录id

        :param record_id: The record_id of this ShowTaskLogsRequest.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowTaskLogsRequest.

        起始位置，默认0；长度1-19

        :return: The offset of this ShowTaskLogsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowTaskLogsRequest.

        起始位置，默认0；长度1-19

        :param offset: The offset of this ShowTaskLogsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def end_offset(self):
        r"""Gets the end_offset of this ShowTaskLogsRequest.

        结束位置，开始为0；长度1-19

        :return: The end_offset of this ShowTaskLogsRequest.
        :rtype: str
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        r"""Sets the end_offset of this ShowTaskLogsRequest.

        结束位置，开始为0；长度1-19

        :param end_offset: The end_offset of this ShowTaskLogsRequest.
        :type end_offset: str
        """
        self._end_offset = end_offset

    @property
    def step_id(self):
        r"""Gets the step_id of this ShowTaskLogsRequest.

        步骤id；如果传，则按step查询日志；长度1-60

        :return: The step_id of this ShowTaskLogsRequest.
        :rtype: str
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        r"""Sets the step_id of this ShowTaskLogsRequest.

        步骤id；如果传，则按step查询日志；长度1-60

        :param step_id: The step_id of this ShowTaskLogsRequest.
        :type step_id: str
        """
        self._step_id = step_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowTaskLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
