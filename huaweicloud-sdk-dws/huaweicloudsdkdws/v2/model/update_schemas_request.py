# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSchemasRequest:

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
        'database_name': 'str',
        'body': 'WorkloadSchemaReq'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'database_name': 'database_name',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, database_name=None, body=None):
        """UpdateSchemasRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param database_name: 数据库名称
        :type database_name: str
        :param body: Body of the UpdateSchemasRequest
        :type body: :class:`huaweicloudsdkdws.v2.WorkloadSchemaReq`
        """
        
        

        self._cluster_id = None
        self._database_name = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.database_name = database_name
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpdateSchemasRequest.

        集群ID

        :return: The cluster_id of this UpdateSchemasRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpdateSchemasRequest.

        集群ID

        :param cluster_id: The cluster_id of this UpdateSchemasRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def database_name(self):
        """Gets the database_name of this UpdateSchemasRequest.

        数据库名称

        :return: The database_name of this UpdateSchemasRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this UpdateSchemasRequest.

        数据库名称

        :param database_name: The database_name of this UpdateSchemasRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def body(self):
        """Gets the body of this UpdateSchemasRequest.

        :return: The body of this UpdateSchemasRequest.
        :rtype: :class:`huaweicloudsdkdws.v2.WorkloadSchemaReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateSchemasRequest.

        :param body: The body of this UpdateSchemasRequest.
        :type body: :class:`huaweicloudsdkdws.v2.WorkloadSchemaReq`
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
        if not isinstance(other, UpdateSchemasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
