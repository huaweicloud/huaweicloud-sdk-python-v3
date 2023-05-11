# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuoteDatabaseReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_project_id': 'str',
        'source_databases': 'list[DatabaseSrcReq]'
    }

    attribute_map = {
        'source_project_id': 'source_project_id',
        'source_databases': 'source_databases'
    }

    def __init__(self, source_project_id=None, source_databases=None):
        """QuoteDatabaseReq

        The model defined in huaweicloud sdk

        :param source_project_id: 源项目id
        :type source_project_id: str
        :param source_databases: 源数据库列表
        :type source_databases: list[:class:`huaweicloudsdkeihealth.v1.DatabaseSrcReq`]
        """
        
        

        self._source_project_id = None
        self._source_databases = None
        self.discriminator = None

        self.source_project_id = source_project_id
        self.source_databases = source_databases

    @property
    def source_project_id(self):
        """Gets the source_project_id of this QuoteDatabaseReq.

        源项目id

        :return: The source_project_id of this QuoteDatabaseReq.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this QuoteDatabaseReq.

        源项目id

        :param source_project_id: The source_project_id of this QuoteDatabaseReq.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def source_databases(self):
        """Gets the source_databases of this QuoteDatabaseReq.

        源数据库列表

        :return: The source_databases of this QuoteDatabaseReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DatabaseSrcReq`]
        """
        return self._source_databases

    @source_databases.setter
    def source_databases(self, source_databases):
        """Sets the source_databases of this QuoteDatabaseReq.

        源数据库列表

        :param source_databases: The source_databases of this QuoteDatabaseReq.
        :type source_databases: list[:class:`huaweicloudsdkeihealth.v1.DatabaseSrcReq`]
        """
        self._source_databases = source_databases

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
        if not isinstance(other, QuoteDatabaseReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
