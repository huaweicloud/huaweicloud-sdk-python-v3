# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPostgresqlHbaInfoHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, instance_id=None, start_time=None, end_time=None):
        """ListPostgresqlHbaInfoHistoryRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param start_time: 开始时间,不传默认当天0点（UTC时区）
        :type start_time: datetime
        :param end_time: 结束时间,不传默认当前时间（UTC时区）
        :type end_time: datetime
        """
        
        

        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.instance_id = instance_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def instance_id(self):
        """Gets the instance_id of this ListPostgresqlHbaInfoHistoryRequest.

        实例id

        :return: The instance_id of this ListPostgresqlHbaInfoHistoryRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListPostgresqlHbaInfoHistoryRequest.

        实例id

        :param instance_id: The instance_id of this ListPostgresqlHbaInfoHistoryRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        """Gets the start_time of this ListPostgresqlHbaInfoHistoryRequest.

        开始时间,不传默认当天0点（UTC时区）

        :return: The start_time of this ListPostgresqlHbaInfoHistoryRequest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListPostgresqlHbaInfoHistoryRequest.

        开始时间,不传默认当天0点（UTC时区）

        :param start_time: The start_time of this ListPostgresqlHbaInfoHistoryRequest.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListPostgresqlHbaInfoHistoryRequest.

        结束时间,不传默认当前时间（UTC时区）

        :return: The end_time of this ListPostgresqlHbaInfoHistoryRequest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListPostgresqlHbaInfoHistoryRequest.

        结束时间,不传默认当前时间（UTC时区）

        :param end_time: The end_time of this ListPostgresqlHbaInfoHistoryRequest.
        :type end_time: datetime
        """
        self._end_time = end_time

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
        if not isinstance(other, ListPostgresqlHbaInfoHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
