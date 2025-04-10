# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataSyncStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'abnormal_count': 'int',
        'running_count': 'int',
        'type_two_way_count': 'int',
        'type_unidirectional_count': 'int'
    }

    attribute_map = {
        'abnormal_count': 'abnormal_count',
        'running_count': 'running_count',
        'type_two_way_count': 'type_two_way_count',
        'type_unidirectional_count': 'type_unidirectional_count'
    }

    def __init__(self, abnormal_count=None, running_count=None, type_two_way_count=None, type_unidirectional_count=None):
        r"""DataSyncStatistics

        The model defined in huaweicloud sdk

        :param abnormal_count: 
        :type abnormal_count: int
        :param running_count: 
        :type running_count: int
        :param type_two_way_count: 
        :type type_two_way_count: int
        :param type_unidirectional_count: 
        :type type_unidirectional_count: int
        """
        
        

        self._abnormal_count = None
        self._running_count = None
        self._type_two_way_count = None
        self._type_unidirectional_count = None
        self.discriminator = None

        if abnormal_count is not None:
            self.abnormal_count = abnormal_count
        if running_count is not None:
            self.running_count = running_count
        if type_two_way_count is not None:
            self.type_two_way_count = type_two_way_count
        if type_unidirectional_count is not None:
            self.type_unidirectional_count = type_unidirectional_count

    @property
    def abnormal_count(self):
        r"""Gets the abnormal_count of this DataSyncStatistics.

        :return: The abnormal_count of this DataSyncStatistics.
        :rtype: int
        """
        return self._abnormal_count

    @abnormal_count.setter
    def abnormal_count(self, abnormal_count):
        r"""Sets the abnormal_count of this DataSyncStatistics.

        :param abnormal_count: The abnormal_count of this DataSyncStatistics.
        :type abnormal_count: int
        """
        self._abnormal_count = abnormal_count

    @property
    def running_count(self):
        r"""Gets the running_count of this DataSyncStatistics.

        :return: The running_count of this DataSyncStatistics.
        :rtype: int
        """
        return self._running_count

    @running_count.setter
    def running_count(self, running_count):
        r"""Sets the running_count of this DataSyncStatistics.

        :param running_count: The running_count of this DataSyncStatistics.
        :type running_count: int
        """
        self._running_count = running_count

    @property
    def type_two_way_count(self):
        r"""Gets the type_two_way_count of this DataSyncStatistics.

        :return: The type_two_way_count of this DataSyncStatistics.
        :rtype: int
        """
        return self._type_two_way_count

    @type_two_way_count.setter
    def type_two_way_count(self, type_two_way_count):
        r"""Sets the type_two_way_count of this DataSyncStatistics.

        :param type_two_way_count: The type_two_way_count of this DataSyncStatistics.
        :type type_two_way_count: int
        """
        self._type_two_way_count = type_two_way_count

    @property
    def type_unidirectional_count(self):
        r"""Gets the type_unidirectional_count of this DataSyncStatistics.

        :return: The type_unidirectional_count of this DataSyncStatistics.
        :rtype: int
        """
        return self._type_unidirectional_count

    @type_unidirectional_count.setter
    def type_unidirectional_count(self, type_unidirectional_count):
        r"""Sets the type_unidirectional_count of this DataSyncStatistics.

        :param type_unidirectional_count: The type_unidirectional_count of this DataSyncStatistics.
        :type type_unidirectional_count: int
        """
        self._type_unidirectional_count = type_unidirectional_count

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
        if not isinstance(other, DataSyncStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
