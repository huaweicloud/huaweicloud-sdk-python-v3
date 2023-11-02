# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportDatabaseDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'database_id': 'str',
        'body': 'ImportDatabaseDataReq'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'database_id': 'database_id',
        'body': 'body'
    }

    def __init__(self, eihealth_project_id=None, database_id=None, body=None):
        """ImportDatabaseDataRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param database_id: 数据库实例id
        :type database_id: str
        :param body: Body of the ImportDatabaseDataRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataReq`
        """
        
        

        self._eihealth_project_id = None
        self._database_id = None
        self._body = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        self.database_id = database_id
        if body is not None:
            self.body = body

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ImportDatabaseDataRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ImportDatabaseDataRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ImportDatabaseDataRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ImportDatabaseDataRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def database_id(self):
        """Gets the database_id of this ImportDatabaseDataRequest.

        数据库实例id

        :return: The database_id of this ImportDatabaseDataRequest.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """Sets the database_id of this ImportDatabaseDataRequest.

        数据库实例id

        :param database_id: The database_id of this ImportDatabaseDataRequest.
        :type database_id: str
        """
        self._database_id = database_id

    @property
    def body(self):
        """Gets the body of this ImportDatabaseDataRequest.

        :return: The body of this ImportDatabaseDataRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ImportDatabaseDataRequest.

        :param body: The body of this ImportDatabaseDataRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataReq`
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
        if not isinstance(other, ImportDatabaseDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
