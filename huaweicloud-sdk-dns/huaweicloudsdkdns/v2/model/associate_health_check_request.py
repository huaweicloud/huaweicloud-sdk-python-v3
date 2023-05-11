# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateHealthCheckRequest:

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
        'body': 'AssociateHealthCheckReq'
    }

    attribute_map = {
        'recordset_id': 'recordset_id',
        'body': 'body'
    }

    def __init__(self, recordset_id=None, body=None):
        """AssociateHealthCheckRequest

        The model defined in huaweicloud sdk

        :param recordset_id: 待查询的recordset ID。
        :type recordset_id: str
        :param body: Body of the AssociateHealthCheckRequest
        :type body: :class:`huaweicloudsdkdns.v2.AssociateHealthCheckReq`
        """
        
        

        self._recordset_id = None
        self._body = None
        self.discriminator = None

        self.recordset_id = recordset_id
        if body is not None:
            self.body = body

    @property
    def recordset_id(self):
        """Gets the recordset_id of this AssociateHealthCheckRequest.

        待查询的recordset ID。

        :return: The recordset_id of this AssociateHealthCheckRequest.
        :rtype: str
        """
        return self._recordset_id

    @recordset_id.setter
    def recordset_id(self, recordset_id):
        """Sets the recordset_id of this AssociateHealthCheckRequest.

        待查询的recordset ID。

        :param recordset_id: The recordset_id of this AssociateHealthCheckRequest.
        :type recordset_id: str
        """
        self._recordset_id = recordset_id

    @property
    def body(self):
        """Gets the body of this AssociateHealthCheckRequest.

        :return: The body of this AssociateHealthCheckRequest.
        :rtype: :class:`huaweicloudsdkdns.v2.AssociateHealthCheckReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AssociateHealthCheckRequest.

        :param body: The body of this AssociateHealthCheckRequest.
        :type body: :class:`huaweicloudsdkdns.v2.AssociateHealthCheckReq`
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
        if not isinstance(other, AssociateHealthCheckRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
