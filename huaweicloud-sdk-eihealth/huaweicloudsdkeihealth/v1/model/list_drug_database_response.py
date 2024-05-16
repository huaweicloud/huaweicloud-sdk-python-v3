# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDrugDatabaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'databases': 'list[DrugDatabaseDto]',
        'count': 'int',
        'cur_user_count': 'int'
    }

    attribute_map = {
        'databases': 'databases',
        'count': 'count',
        'cur_user_count': 'cur_user_count'
    }

    def __init__(self, databases=None, count=None, cur_user_count=None):
        """ListDrugDatabaseResponse

        The model defined in huaweicloud sdk

        :param databases: 数据库列表
        :type databases: list[:class:`huaweicloudsdkeihealth.v1.DrugDatabaseDto`]
        :param count: 数据库总数
        :type count: int
        :param cur_user_count: 当前用户数据库总数
        :type cur_user_count: int
        """
        
        super(ListDrugDatabaseResponse, self).__init__()

        self._databases = None
        self._count = None
        self._cur_user_count = None
        self.discriminator = None

        if databases is not None:
            self.databases = databases
        if count is not None:
            self.count = count
        if cur_user_count is not None:
            self.cur_user_count = cur_user_count

    @property
    def databases(self):
        """Gets the databases of this ListDrugDatabaseResponse.

        数据库列表

        :return: The databases of this ListDrugDatabaseResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DrugDatabaseDto`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this ListDrugDatabaseResponse.

        数据库列表

        :param databases: The databases of this ListDrugDatabaseResponse.
        :type databases: list[:class:`huaweicloudsdkeihealth.v1.DrugDatabaseDto`]
        """
        self._databases = databases

    @property
    def count(self):
        """Gets the count of this ListDrugDatabaseResponse.

        数据库总数

        :return: The count of this ListDrugDatabaseResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDrugDatabaseResponse.

        数据库总数

        :param count: The count of this ListDrugDatabaseResponse.
        :type count: int
        """
        self._count = count

    @property
    def cur_user_count(self):
        """Gets the cur_user_count of this ListDrugDatabaseResponse.

        当前用户数据库总数

        :return: The cur_user_count of this ListDrugDatabaseResponse.
        :rtype: int
        """
        return self._cur_user_count

    @cur_user_count.setter
    def cur_user_count(self, cur_user_count):
        """Sets the cur_user_count of this ListDrugDatabaseResponse.

        当前用户数据库总数

        :param cur_user_count: The cur_user_count of this ListDrugDatabaseResponse.
        :type cur_user_count: int
        """
        self._cur_user_count = cur_user_count

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
        if not isinstance(other, ListDrugDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
