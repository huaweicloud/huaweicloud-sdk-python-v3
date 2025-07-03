# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOrderStatusReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, domain_id=None, start_time=None, end_time=None):
        r"""ShowOrderStatusReq

        The model defined in huaweicloud sdk

        :param domain_id: 租户id
        :type domain_id: str
        :param start_time: 活动开始时间,必填
        :type start_time: str
        :param end_time: 活动结束时间,必填
        :type end_time: str
        """
        
        

        self._domain_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.domain_id = domain_id
        self.start_time = start_time
        self.end_time = end_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowOrderStatusReq.

        租户id

        :return: The domain_id of this ShowOrderStatusReq.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowOrderStatusReq.

        租户id

        :param domain_id: The domain_id of this ShowOrderStatusReq.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowOrderStatusReq.

        活动开始时间,必填

        :return: The start_time of this ShowOrderStatusReq.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowOrderStatusReq.

        活动开始时间,必填

        :param start_time: The start_time of this ShowOrderStatusReq.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowOrderStatusReq.

        活动结束时间,必填

        :return: The end_time of this ShowOrderStatusReq.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowOrderStatusReq.

        活动结束时间,必填

        :param end_time: The end_time of this ShowOrderStatusReq.
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
        if not isinstance(other, ShowOrderStatusReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
