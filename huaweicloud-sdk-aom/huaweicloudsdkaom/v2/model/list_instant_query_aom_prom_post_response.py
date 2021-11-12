# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstantQueryAomPromPostResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'data': 'Data'
    }

    attribute_map = {
        'status': 'status',
        'data': 'data'
    }

    def __init__(self, status=None, data=None):
        """ListInstantQueryAomPromPostResponse - a model defined in huaweicloud sdk"""
        
        super(ListInstantQueryAomPromPostResponse, self).__init__()

        self._status = None
        self._data = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if data is not None:
            self.data = data

    @property
    def status(self):
        """Gets the status of this ListInstantQueryAomPromPostResponse.


        :return: The status of this ListInstantQueryAomPromPostResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstantQueryAomPromPostResponse.


        :param status: The status of this ListInstantQueryAomPromPostResponse.
        :type: str
        """
        self._status = status

    @property
    def data(self):
        """Gets the data of this ListInstantQueryAomPromPostResponse.


        :return: The data of this ListInstantQueryAomPromPostResponse.
        :rtype: Data
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListInstantQueryAomPromPostResponse.


        :param data: The data of this ListInstantQueryAomPromPostResponse.
        :type: Data
        """
        self._data = data

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
        if not isinstance(other, ListInstantQueryAomPromPostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
