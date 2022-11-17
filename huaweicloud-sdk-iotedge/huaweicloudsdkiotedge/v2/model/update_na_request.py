# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNaRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'na_id': 'str',
        'body': 'UpdateNaRequestDTO'
    }

    attribute_map = {
        'na_id': 'na_id',
        'body': 'body'
    }

    def __init__(self, na_id=None, body=None):
        """UpdateNaRequest

        The model defined in huaweicloud sdk

        :param na_id: 北向数据接收端点ID
        :type na_id: str
        :param body: Body of the UpdateNaRequest
        :type body: :class:`huaweicloudsdkiotedge.v2.UpdateNaRequestDTO`
        """
        
        

        self._na_id = None
        self._body = None
        self.discriminator = None

        self.na_id = na_id
        if body is not None:
            self.body = body

    @property
    def na_id(self):
        """Gets the na_id of this UpdateNaRequest.

        北向数据接收端点ID

        :return: The na_id of this UpdateNaRequest.
        :rtype: str
        """
        return self._na_id

    @na_id.setter
    def na_id(self, na_id):
        """Sets the na_id of this UpdateNaRequest.

        北向数据接收端点ID

        :param na_id: The na_id of this UpdateNaRequest.
        :type na_id: str
        """
        self._na_id = na_id

    @property
    def body(self):
        """Gets the body of this UpdateNaRequest.

        :return: The body of this UpdateNaRequest.
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateNaRequestDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateNaRequest.

        :param body: The body of this UpdateNaRequest.
        :type body: :class:`huaweicloudsdkiotedge.v2.UpdateNaRequestDTO`
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
        if not isinstance(other, UpdateNaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
