# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpReferenceTableRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_id': 'str',
        'body': 'UpdateHttpReferenceTableRequestBody'
    }

    attribute_map = {
        'table_id': 'table_id',
        'body': 'body'
    }

    def __init__(self, table_id=None, body=None):
        """UpdateHttpReferenceTableRequest

        The model defined in huaweicloud sdk

        :param table_id: 引用表id
        :type table_id: str
        :param body: Body of the UpdateHttpReferenceTableRequest
        :type body: :class:`huaweicloudsdkedgesec.v2.UpdateHttpReferenceTableRequestBody`
        """
        
        

        self._table_id = None
        self._body = None
        self.discriminator = None

        self.table_id = table_id
        if body is not None:
            self.body = body

    @property
    def table_id(self):
        """Gets the table_id of this UpdateHttpReferenceTableRequest.

        引用表id

        :return: The table_id of this UpdateHttpReferenceTableRequest.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this UpdateHttpReferenceTableRequest.

        引用表id

        :param table_id: The table_id of this UpdateHttpReferenceTableRequest.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def body(self):
        """Gets the body of this UpdateHttpReferenceTableRequest.

        :return: The body of this UpdateHttpReferenceTableRequest.
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpReferenceTableRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateHttpReferenceTableRequest.

        :param body: The body of this UpdateHttpReferenceTableRequest.
        :type body: :class:`huaweicloudsdkedgesec.v2.UpdateHttpReferenceTableRequestBody`
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
        if not isinstance(other, UpdateHttpReferenceTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
