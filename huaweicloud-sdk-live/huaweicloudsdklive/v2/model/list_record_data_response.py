# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_data_list': 'list[RecordData]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'record_data_list': 'record_data_list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, record_data_list=None, x_request_id=None):
        """ListRecordDataResponse

        The model defined in huaweicloud sdk

        :param record_data_list: 采样数据列表。 
        :type record_data_list: list[:class:`huaweicloudsdklive.v2.RecordData`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListRecordDataResponse, self).__init__()

        self._record_data_list = None
        self._x_request_id = None
        self.discriminator = None

        if record_data_list is not None:
            self.record_data_list = record_data_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def record_data_list(self):
        """Gets the record_data_list of this ListRecordDataResponse.

        采样数据列表。 

        :return: The record_data_list of this ListRecordDataResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.RecordData`]
        """
        return self._record_data_list

    @record_data_list.setter
    def record_data_list(self, record_data_list):
        """Sets the record_data_list of this ListRecordDataResponse.

        采样数据列表。 

        :param record_data_list: The record_data_list of this ListRecordDataResponse.
        :type record_data_list: list[:class:`huaweicloudsdklive.v2.RecordData`]
        """
        self._record_data_list = record_data_list

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListRecordDataResponse.

        :return: The x_request_id of this ListRecordDataResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListRecordDataResponse.

        :param x_request_id: The x_request_id of this ListRecordDataResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListRecordDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
