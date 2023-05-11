# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLatelyApiStatisticsV2Request:

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
        'api_id': 'str',
        'duration': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'api_id': 'api_id',
        'duration': 'duration'
    }

    def __init__(self, instance_id=None, api_id=None, duration=None):
        """ListLatelyApiStatisticsV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param api_id: API的编号
        :type api_id: str
        :param duration: 最近统计时长，单位必须为h和m，比如1h和1m，分别代表最近1小时和最近1分钟
        :type duration: str
        """
        
        

        self._instance_id = None
        self._api_id = None
        self._duration = None
        self.discriminator = None

        self.instance_id = instance_id
        self.api_id = api_id
        self.duration = duration

    @property
    def instance_id(self):
        """Gets the instance_id of this ListLatelyApiStatisticsV2Request.

        实例ID

        :return: The instance_id of this ListLatelyApiStatisticsV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListLatelyApiStatisticsV2Request.

        实例ID

        :param instance_id: The instance_id of this ListLatelyApiStatisticsV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def api_id(self):
        """Gets the api_id of this ListLatelyApiStatisticsV2Request.

        API的编号

        :return: The api_id of this ListLatelyApiStatisticsV2Request.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ListLatelyApiStatisticsV2Request.

        API的编号

        :param api_id: The api_id of this ListLatelyApiStatisticsV2Request.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def duration(self):
        """Gets the duration of this ListLatelyApiStatisticsV2Request.

        最近统计时长，单位必须为h和m，比如1h和1m，分别代表最近1小时和最近1分钟

        :return: The duration of this ListLatelyApiStatisticsV2Request.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ListLatelyApiStatisticsV2Request.

        最近统计时长，单位必须为h和m，比如1h和1m，分别代表最近1小时和最近1分钟

        :param duration: The duration of this ListLatelyApiStatisticsV2Request.
        :type duration: str
        """
        self._duration = duration

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
        if not isinstance(other, ListLatelyApiStatisticsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
