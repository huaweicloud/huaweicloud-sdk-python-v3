# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmNotifyListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'page_size': 'int',
        'alarm_data_id': 'int',
        'region': 'str'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'page_size',
        'alarm_data_id': 'alarm_data_id',
        'region': 'region'
    }

    def __init__(self, page=None, page_size=None, alarm_data_id=None, region=None):
        """AlarmNotifyListRequest

        The model defined in huaweicloud sdk

        :param page: 页码。
        :type page: int
        :param page_size: 每页数量。
        :type page_size: int
        :param alarm_data_id: 告警事件id。
        :type alarm_data_id: int
        :param region: region英文名称。
        :type region: str
        """
        
        

        self._page = None
        self._page_size = None
        self._alarm_data_id = None
        self._region = None
        self.discriminator = None

        self.page = page
        self.page_size = page_size
        self.alarm_data_id = alarm_data_id
        self.region = region

    @property
    def page(self):
        """Gets the page of this AlarmNotifyListRequest.

        页码。

        :return: The page of this AlarmNotifyListRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this AlarmNotifyListRequest.

        页码。

        :param page: The page of this AlarmNotifyListRequest.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this AlarmNotifyListRequest.

        每页数量。

        :return: The page_size of this AlarmNotifyListRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this AlarmNotifyListRequest.

        每页数量。

        :param page_size: The page_size of this AlarmNotifyListRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def alarm_data_id(self):
        """Gets the alarm_data_id of this AlarmNotifyListRequest.

        告警事件id。

        :return: The alarm_data_id of this AlarmNotifyListRequest.
        :rtype: int
        """
        return self._alarm_data_id

    @alarm_data_id.setter
    def alarm_data_id(self, alarm_data_id):
        """Sets the alarm_data_id of this AlarmNotifyListRequest.

        告警事件id。

        :param alarm_data_id: The alarm_data_id of this AlarmNotifyListRequest.
        :type alarm_data_id: int
        """
        self._alarm_data_id = alarm_data_id

    @property
    def region(self):
        """Gets the region of this AlarmNotifyListRequest.

        region英文名称。

        :return: The region of this AlarmNotifyListRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AlarmNotifyListRequest.

        region英文名称。

        :param region: The region of this AlarmNotifyListRequest.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, AlarmNotifyListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
