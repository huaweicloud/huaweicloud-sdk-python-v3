# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoSqlQueryEpsQuotaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'quota': 'NoSqlEpsQuotaTotal',
        'used': 'NoSqlEpsQuotaUsed'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'quota': 'quota',
        'used': 'used'
    }

    def __init__(self, enterprise_project_id=None, enterprise_project_name=None, quota=None, used=None):
        """NoSqlQueryEpsQuotaInfo

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称。
        :type enterprise_project_name: str
        :param quota: 
        :type quota: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlEpsQuotaTotal`
        :param used: 
        :type used: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlEpsQuotaUsed`
        """
        
        

        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._quota = None
        self._used = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.enterprise_project_name = enterprise_project_name
        self.quota = quota
        self.used = used

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this NoSqlQueryEpsQuotaInfo.

        企业项目ID。

        :return: The enterprise_project_id of this NoSqlQueryEpsQuotaInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this NoSqlQueryEpsQuotaInfo.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this NoSqlQueryEpsQuotaInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this NoSqlQueryEpsQuotaInfo.

        企业项目名称。

        :return: The enterprise_project_name of this NoSqlQueryEpsQuotaInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this NoSqlQueryEpsQuotaInfo.

        企业项目名称。

        :param enterprise_project_name: The enterprise_project_name of this NoSqlQueryEpsQuotaInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def quota(self):
        """Gets the quota of this NoSqlQueryEpsQuotaInfo.

        :return: The quota of this NoSqlQueryEpsQuotaInfo.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlEpsQuotaTotal`
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this NoSqlQueryEpsQuotaInfo.

        :param quota: The quota of this NoSqlQueryEpsQuotaInfo.
        :type quota: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlEpsQuotaTotal`
        """
        self._quota = quota

    @property
    def used(self):
        """Gets the used of this NoSqlQueryEpsQuotaInfo.

        :return: The used of this NoSqlQueryEpsQuotaInfo.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlEpsQuotaUsed`
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this NoSqlQueryEpsQuotaInfo.

        :param used: The used of this NoSqlQueryEpsQuotaInfo.
        :type used: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlEpsQuotaUsed`
        """
        self._used = used

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
        if not isinstance(other, NoSqlQueryEpsQuotaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
