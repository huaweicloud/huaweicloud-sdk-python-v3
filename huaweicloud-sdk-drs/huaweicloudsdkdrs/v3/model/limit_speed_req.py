# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LimitSpeedReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'speed_limit': 'list[SpeedLimitInfo]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'speed_limit': 'speed_limit'
    }

    def __init__(self, job_id=None, speed_limit=None):
        """LimitSpeedReq

        The model defined in huaweicloud sdk

        :param job_id: 任务id
        :type job_id: str
        :param speed_limit: 限速信息请求体
        :type speed_limit: list[:class:`huaweicloudsdkdrs.v3.SpeedLimitInfo`]
        """
        
        

        self._job_id = None
        self._speed_limit = None
        self.discriminator = None

        self.job_id = job_id
        self.speed_limit = speed_limit

    @property
    def job_id(self):
        """Gets the job_id of this LimitSpeedReq.

        任务id

        :return: The job_id of this LimitSpeedReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this LimitSpeedReq.

        任务id

        :param job_id: The job_id of this LimitSpeedReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def speed_limit(self):
        """Gets the speed_limit of this LimitSpeedReq.

        限速信息请求体

        :return: The speed_limit of this LimitSpeedReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.SpeedLimitInfo`]
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """Sets the speed_limit of this LimitSpeedReq.

        限速信息请求体

        :param speed_limit: The speed_limit of this LimitSpeedReq.
        :type speed_limit: list[:class:`huaweicloudsdkdrs.v3.SpeedLimitInfo`]
        """
        self._speed_limit = speed_limit

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
        if not isinstance(other, LimitSpeedReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
