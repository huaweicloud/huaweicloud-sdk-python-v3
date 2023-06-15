# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDatabaseUserInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'name': 'str',
        'body': 'DatabaseUserInfoReq'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'name': 'name',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, name=None, body=None):
        """UpdateDatabaseUserInfoRequest

        The model defined in huaweicloud sdk

        :param cluster_id: cluster_id
        :type cluster_id: str
        :param name: name
        :type name: str
        :param body: Body of the UpdateDatabaseUserInfoRequest
        :type body: :class:`huaweicloudsdkdws.v2.DatabaseUserInfoReq`
        """
        
        

        self._cluster_id = None
        self._name = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.name = name
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpdateDatabaseUserInfoRequest.

        cluster_id

        :return: The cluster_id of this UpdateDatabaseUserInfoRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpdateDatabaseUserInfoRequest.

        cluster_id

        :param cluster_id: The cluster_id of this UpdateDatabaseUserInfoRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def name(self):
        """Gets the name of this UpdateDatabaseUserInfoRequest.

        name

        :return: The name of this UpdateDatabaseUserInfoRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDatabaseUserInfoRequest.

        name

        :param name: The name of this UpdateDatabaseUserInfoRequest.
        :type name: str
        """
        self._name = name

    @property
    def body(self):
        """Gets the body of this UpdateDatabaseUserInfoRequest.

        :return: The body of this UpdateDatabaseUserInfoRequest.
        :rtype: :class:`huaweicloudsdkdws.v2.DatabaseUserInfoReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDatabaseUserInfoRequest.

        :param body: The body of this UpdateDatabaseUserInfoRequest.
        :type body: :class:`huaweicloudsdkdws.v2.DatabaseUserInfoReq`
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
        if not isinstance(other, UpdateDatabaseUserInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
