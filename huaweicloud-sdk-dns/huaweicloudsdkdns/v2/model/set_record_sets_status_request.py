# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetRecordSetsStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recordset_id': 'str',
        'body': 'SetRecordSetsStatusReq'
    }

    attribute_map = {
        'recordset_id': 'recordset_id',
        'body': 'body'
    }

    def __init__(self, recordset_id=None, body=None):
        """SetRecordSetsStatusRequest

        The model defined in huaweicloud sdk

        :param recordset_id: 待设置Record Set的ID信息。
        :type recordset_id: str
        :param body: Body of the SetRecordSetsStatusRequest
        :type body: :class:`huaweicloudsdkdns.v2.SetRecordSetsStatusReq`
        """
        
        

        self._recordset_id = None
        self._body = None
        self.discriminator = None

        self.recordset_id = recordset_id
        if body is not None:
            self.body = body

    @property
    def recordset_id(self):
        """Gets the recordset_id of this SetRecordSetsStatusRequest.

        待设置Record Set的ID信息。

        :return: The recordset_id of this SetRecordSetsStatusRequest.
        :rtype: str
        """
        return self._recordset_id

    @recordset_id.setter
    def recordset_id(self, recordset_id):
        """Sets the recordset_id of this SetRecordSetsStatusRequest.

        待设置Record Set的ID信息。

        :param recordset_id: The recordset_id of this SetRecordSetsStatusRequest.
        :type recordset_id: str
        """
        self._recordset_id = recordset_id

    @property
    def body(self):
        """Gets the body of this SetRecordSetsStatusRequest.

        :return: The body of this SetRecordSetsStatusRequest.
        :rtype: :class:`huaweicloudsdkdns.v2.SetRecordSetsStatusReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SetRecordSetsStatusRequest.

        :param body: The body of this SetRecordSetsStatusRequest.
        :type body: :class:`huaweicloudsdkdns.v2.SetRecordSetsStatusReq`
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
        if not isinstance(other, SetRecordSetsStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
