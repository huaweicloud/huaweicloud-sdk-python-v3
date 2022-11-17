# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_store_id': 'str',
        'body': 'GetHistoryRequest'
    }

    attribute_map = {
        'data_store_id': 'data_store_id',
        'body': 'body'
    }

    def __init__(self, data_store_id=None, body=None):
        """ListHistoryRequest

        The model defined in huaweicloud sdk

        :param data_store_id: 存储ID
        :type data_store_id: str
        :param body: Body of the ListHistoryRequest
        :type body: :class:`huaweicloudsdkiotanalytics.v1.GetHistoryRequest`
        """
        
        

        self._data_store_id = None
        self._body = None
        self.discriminator = None

        self.data_store_id = data_store_id
        if body is not None:
            self.body = body

    @property
    def data_store_id(self):
        """Gets the data_store_id of this ListHistoryRequest.

        存储ID

        :return: The data_store_id of this ListHistoryRequest.
        :rtype: str
        """
        return self._data_store_id

    @data_store_id.setter
    def data_store_id(self, data_store_id):
        """Sets the data_store_id of this ListHistoryRequest.

        存储ID

        :param data_store_id: The data_store_id of this ListHistoryRequest.
        :type data_store_id: str
        """
        self._data_store_id = data_store_id

    @property
    def body(self):
        """Gets the body of this ListHistoryRequest.

        :return: The body of this ListHistoryRequest.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.GetHistoryRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListHistoryRequest.

        :param body: The body of this ListHistoryRequest.
        :type body: :class:`huaweicloudsdkiotanalytics.v1.GetHistoryRequest`
        """
        self._body = body

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
        if not isinstance(other, ListHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
