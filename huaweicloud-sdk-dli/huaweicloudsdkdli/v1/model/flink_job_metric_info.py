# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkJobMetricInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'records': 'int',
        'corrupted_records': 'int'
    }

    attribute_map = {
        'name': 'name',
        'records': 'records',
        'corrupted_records': 'corrupted_records'
    }

    def __init__(self, name=None, records=None, corrupted_records=None):
        """FlinkJobMetricInfo

        The model defined in huaweicloud sdk

        :param name: 输入流或输出流名称。
        :type name: str
        :param records: 总记录数。
        :type records: int
        :param corrupted_records: 脏数据记录数。
        :type corrupted_records: int
        """
        
        

        self._name = None
        self._records = None
        self._corrupted_records = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if records is not None:
            self.records = records
        if corrupted_records is not None:
            self.corrupted_records = corrupted_records

    @property
    def name(self):
        """Gets the name of this FlinkJobMetricInfo.

        输入流或输出流名称。

        :return: The name of this FlinkJobMetricInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FlinkJobMetricInfo.

        输入流或输出流名称。

        :param name: The name of this FlinkJobMetricInfo.
        :type name: str
        """
        self._name = name

    @property
    def records(self):
        """Gets the records of this FlinkJobMetricInfo.

        总记录数。

        :return: The records of this FlinkJobMetricInfo.
        :rtype: int
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this FlinkJobMetricInfo.

        总记录数。

        :param records: The records of this FlinkJobMetricInfo.
        :type records: int
        """
        self._records = records

    @property
    def corrupted_records(self):
        """Gets the corrupted_records of this FlinkJobMetricInfo.

        脏数据记录数。

        :return: The corrupted_records of this FlinkJobMetricInfo.
        :rtype: int
        """
        return self._corrupted_records

    @corrupted_records.setter
    def corrupted_records(self, corrupted_records):
        """Sets the corrupted_records of this FlinkJobMetricInfo.

        脏数据记录数。

        :param corrupted_records: The corrupted_records of this FlinkJobMetricInfo.
        :type corrupted_records: int
        """
        self._corrupted_records = corrupted_records

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
        if not isinstance(other, FlinkJobMetricInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
