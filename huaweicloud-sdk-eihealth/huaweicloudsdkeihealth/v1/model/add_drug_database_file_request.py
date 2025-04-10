# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDrugDatabaseFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_id': 'str',
        'body': 'AddDrugDatabaseFileReq'
    }

    attribute_map = {
        'database_id': 'database_id',
        'body': 'body'
    }

    def __init__(self, database_id=None, body=None):
        r"""AddDrugDatabaseFileRequest

        The model defined in huaweicloud sdk

        :param database_id: 数据库id
        :type database_id: str
        :param body: Body of the AddDrugDatabaseFileRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.AddDrugDatabaseFileReq`
        """
        
        

        self._database_id = None
        self._body = None
        self.discriminator = None

        self.database_id = database_id
        if body is not None:
            self.body = body

    @property
    def database_id(self):
        r"""Gets the database_id of this AddDrugDatabaseFileRequest.

        数据库id

        :return: The database_id of this AddDrugDatabaseFileRequest.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        r"""Sets the database_id of this AddDrugDatabaseFileRequest.

        数据库id

        :param database_id: The database_id of this AddDrugDatabaseFileRequest.
        :type database_id: str
        """
        self._database_id = database_id

    @property
    def body(self):
        r"""Gets the body of this AddDrugDatabaseFileRequest.

        :return: The body of this AddDrugDatabaseFileRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.AddDrugDatabaseFileReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AddDrugDatabaseFileRequest.

        :param body: The body of this AddDrugDatabaseFileRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.AddDrugDatabaseFileReq`
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
        if not isinstance(other, AddDrugDatabaseFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
