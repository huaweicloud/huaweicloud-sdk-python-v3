# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateReplicationNameRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'replication_id': 'str',
        'body': 'UpdateReplicationNameRequestBody'
    }

    attribute_map = {
        'replication_id': 'replication_id',
        'body': 'body'
    }

    def __init__(self, replication_id=None, body=None):
        """UpdateReplicationNameRequest

        The model defined in huaweicloud sdk

        :param replication_id: replication_id
        :type replication_id: str
        :param body: Body of the UpdateReplicationNameRequest
        :type body: :class:`huaweicloudsdksdrs.v1.UpdateReplicationNameRequestBody`
        """
        
        

        self._replication_id = None
        self._body = None
        self.discriminator = None

        self.replication_id = replication_id
        if body is not None:
            self.body = body

    @property
    def replication_id(self):
        """Gets the replication_id of this UpdateReplicationNameRequest.

        replication_id

        :return: The replication_id of this UpdateReplicationNameRequest.
        :rtype: str
        """
        return self._replication_id

    @replication_id.setter
    def replication_id(self, replication_id):
        """Sets the replication_id of this UpdateReplicationNameRequest.

        replication_id

        :param replication_id: The replication_id of this UpdateReplicationNameRequest.
        :type replication_id: str
        """
        self._replication_id = replication_id

    @property
    def body(self):
        """Gets the body of this UpdateReplicationNameRequest.

        :return: The body of this UpdateReplicationNameRequest.
        :rtype: :class:`huaweicloudsdksdrs.v1.UpdateReplicationNameRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateReplicationNameRequest.

        :param body: The body of this UpdateReplicationNameRequest.
        :type body: :class:`huaweicloudsdksdrs.v1.UpdateReplicationNameRequestBody`
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
        if not isinstance(other, UpdateReplicationNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
