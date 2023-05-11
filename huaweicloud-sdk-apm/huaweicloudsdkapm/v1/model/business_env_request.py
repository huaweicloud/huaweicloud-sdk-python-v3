# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessEnvRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_id': 'int',
        'region': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'business_id': 'business_id',
        'region': 'region',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, business_id=None, region=None, start_time=None, end_time=None):
        """BusinessEnvRequest

        The model defined in huaweicloud sdk

        :param business_id: 应用id。
        :type business_id: int
        :param region: region英文名称。
        :type region: str
        :param start_time: 开始时间。
        :type start_time: str
        :param end_time: 结束时间。
        :type end_time: str
        """
        
        

        self._business_id = None
        self._region = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.business_id = business_id
        self.region = region
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def business_id(self):
        """Gets the business_id of this BusinessEnvRequest.

        应用id。

        :return: The business_id of this BusinessEnvRequest.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this BusinessEnvRequest.

        应用id。

        :param business_id: The business_id of this BusinessEnvRequest.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def region(self):
        """Gets the region of this BusinessEnvRequest.

        region英文名称。

        :return: The region of this BusinessEnvRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this BusinessEnvRequest.

        region英文名称。

        :param region: The region of this BusinessEnvRequest.
        :type region: str
        """
        self._region = region

    @property
    def start_time(self):
        """Gets the start_time of this BusinessEnvRequest.

        开始时间。

        :return: The start_time of this BusinessEnvRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BusinessEnvRequest.

        开始时间。

        :param start_time: The start_time of this BusinessEnvRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this BusinessEnvRequest.

        结束时间。

        :return: The end_time of this BusinessEnvRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this BusinessEnvRequest.

        结束时间。

        :param end_time: The end_time of this BusinessEnvRequest.
        :type end_time: str
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
        if not isinstance(other, BusinessEnvRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
