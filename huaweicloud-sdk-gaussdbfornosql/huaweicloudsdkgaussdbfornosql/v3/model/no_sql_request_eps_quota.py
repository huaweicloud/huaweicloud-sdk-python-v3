# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoSqlRequestEpsQuota:

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
        'quota': 'NoSqlEpsQuotaRequestInfo'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'quota': 'quota'
    }

    def __init__(self, enterprise_project_id=None, quota=None):
        r"""NoSqlRequestEpsQuota

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param quota: 
        :type quota: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlEpsQuotaRequestInfo`
        """
        
        

        self._enterprise_project_id = None
        self._quota = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.quota = quota

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this NoSqlRequestEpsQuota.

        企业项目ID。

        :return: The enterprise_project_id of this NoSqlRequestEpsQuota.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this NoSqlRequestEpsQuota.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this NoSqlRequestEpsQuota.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def quota(self):
        r"""Gets the quota of this NoSqlRequestEpsQuota.

        :return: The quota of this NoSqlRequestEpsQuota.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlEpsQuotaRequestInfo`
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this NoSqlRequestEpsQuota.

        :param quota: The quota of this NoSqlRequestEpsQuota.
        :type quota: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlEpsQuotaRequestInfo`
        """
        self._quota = quota

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
        if not isinstance(other, NoSqlRequestEpsQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
