# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregatedSourceStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_error_code': 'str',
        'last_error_message': 'str',
        'last_update_status': 'str',
        'last_update_time': 'str',
        'source_id': 'str',
        'source_name': 'str',
        'source_type': 'str'
    }

    attribute_map = {
        'last_error_code': 'last_error_code',
        'last_error_message': 'last_error_message',
        'last_update_status': 'last_update_status',
        'last_update_time': 'last_update_time',
        'source_id': 'source_id',
        'source_name': 'source_name',
        'source_type': 'source_type'
    }

    def __init__(self, last_error_code=None, last_error_message=None, last_update_status=None, last_update_time=None, source_id=None, source_name=None, source_type=None):
        """AggregatedSourceStatus

        The model defined in huaweicloud sdk

        :param last_error_code: 源帐号最近一次聚合失败时返回的错误码。
        :type last_error_code: str
        :param last_error_message: 源帐号最近一次聚合失败时返回的错误消息。
        :type last_error_message: str
        :param last_update_status: 最近一次更新的状态类型。
        :type last_update_status: str
        :param last_update_time: 最近一次更新的时间。
        :type last_update_time: str
        :param source_id: 源帐号ID或组织。
        :type source_id: str
        :param source_name: 帐号名。
        :type source_name: str
        :param source_type: 源帐号类型（ACCOUNT | ORGANIZATION）。
        :type source_type: str
        """
        
        

        self._last_error_code = None
        self._last_error_message = None
        self._last_update_status = None
        self._last_update_time = None
        self._source_id = None
        self._source_name = None
        self._source_type = None
        self.discriminator = None

        if last_error_code is not None:
            self.last_error_code = last_error_code
        if last_error_message is not None:
            self.last_error_message = last_error_message
        if last_update_status is not None:
            self.last_update_status = last_update_status
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if source_id is not None:
            self.source_id = source_id
        if source_name is not None:
            self.source_name = source_name
        if source_type is not None:
            self.source_type = source_type

    @property
    def last_error_code(self):
        """Gets the last_error_code of this AggregatedSourceStatus.

        源帐号最近一次聚合失败时返回的错误码。

        :return: The last_error_code of this AggregatedSourceStatus.
        :rtype: str
        """
        return self._last_error_code

    @last_error_code.setter
    def last_error_code(self, last_error_code):
        """Sets the last_error_code of this AggregatedSourceStatus.

        源帐号最近一次聚合失败时返回的错误码。

        :param last_error_code: The last_error_code of this AggregatedSourceStatus.
        :type last_error_code: str
        """
        self._last_error_code = last_error_code

    @property
    def last_error_message(self):
        """Gets the last_error_message of this AggregatedSourceStatus.

        源帐号最近一次聚合失败时返回的错误消息。

        :return: The last_error_message of this AggregatedSourceStatus.
        :rtype: str
        """
        return self._last_error_message

    @last_error_message.setter
    def last_error_message(self, last_error_message):
        """Sets the last_error_message of this AggregatedSourceStatus.

        源帐号最近一次聚合失败时返回的错误消息。

        :param last_error_message: The last_error_message of this AggregatedSourceStatus.
        :type last_error_message: str
        """
        self._last_error_message = last_error_message

    @property
    def last_update_status(self):
        """Gets the last_update_status of this AggregatedSourceStatus.

        最近一次更新的状态类型。

        :return: The last_update_status of this AggregatedSourceStatus.
        :rtype: str
        """
        return self._last_update_status

    @last_update_status.setter
    def last_update_status(self, last_update_status):
        """Sets the last_update_status of this AggregatedSourceStatus.

        最近一次更新的状态类型。

        :param last_update_status: The last_update_status of this AggregatedSourceStatus.
        :type last_update_status: str
        """
        self._last_update_status = last_update_status

    @property
    def last_update_time(self):
        """Gets the last_update_time of this AggregatedSourceStatus.

        最近一次更新的时间。

        :return: The last_update_time of this AggregatedSourceStatus.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this AggregatedSourceStatus.

        最近一次更新的时间。

        :param last_update_time: The last_update_time of this AggregatedSourceStatus.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def source_id(self):
        """Gets the source_id of this AggregatedSourceStatus.

        源帐号ID或组织。

        :return: The source_id of this AggregatedSourceStatus.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this AggregatedSourceStatus.

        源帐号ID或组织。

        :param source_id: The source_id of this AggregatedSourceStatus.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def source_name(self):
        """Gets the source_name of this AggregatedSourceStatus.

        帐号名。

        :return: The source_name of this AggregatedSourceStatus.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this AggregatedSourceStatus.

        帐号名。

        :param source_name: The source_name of this AggregatedSourceStatus.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def source_type(self):
        """Gets the source_type of this AggregatedSourceStatus.

        源帐号类型（ACCOUNT | ORGANIZATION）。

        :return: The source_type of this AggregatedSourceStatus.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this AggregatedSourceStatus.

        源帐号类型（ACCOUNT | ORGANIZATION）。

        :param source_type: The source_type of this AggregatedSourceStatus.
        :type source_type: str
        """
        self._source_type = source_type

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
        if not isinstance(other, AggregatedSourceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
