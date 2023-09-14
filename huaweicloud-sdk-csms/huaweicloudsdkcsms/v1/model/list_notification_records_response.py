# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'records': 'list[Record]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'records': 'records',
        'page_info': 'page_info'
    }

    def __init__(self, records=None, page_info=None):
        """ListNotificationRecordsResponse

        The model defined in huaweicloud sdk

        :param records: Record对象。
        :type records: list[:class:`huaweicloudsdkcsms.v1.Record`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcsms.v1.PageInfo`
        """
        
        super(ListNotificationRecordsResponse, self).__init__()

        self._records = None
        self._page_info = None
        self.discriminator = None

        if records is not None:
            self.records = records
        if page_info is not None:
            self.page_info = page_info

    @property
    def records(self):
        """Gets the records of this ListNotificationRecordsResponse.

        Record对象。

        :return: The records of this ListNotificationRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkcsms.v1.Record`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this ListNotificationRecordsResponse.

        Record对象。

        :param records: The records of this ListNotificationRecordsResponse.
        :type records: list[:class:`huaweicloudsdkcsms.v1.Record`]
        """
        self._records = records

    @property
    def page_info(self):
        """Gets the page_info of this ListNotificationRecordsResponse.

        :return: The page_info of this ListNotificationRecordsResponse.
        :rtype: :class:`huaweicloudsdkcsms.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListNotificationRecordsResponse.

        :param page_info: The page_info of this ListNotificationRecordsResponse.
        :type page_info: :class:`huaweicloudsdkcsms.v1.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListNotificationRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
