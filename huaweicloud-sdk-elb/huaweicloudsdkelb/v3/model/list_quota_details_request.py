# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQuotaDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_key': 'list[str]'
    }

    attribute_map = {
        'quota_key': 'quota_key'
    }

    def __init__(self, quota_key=None):
        """ListQuotaDetailsRequest

        The model defined in huaweicloud sdk

        :param quota_key: 资源类型。  取值： loadbalancer、listener、ipgroup、pool、member、members_per_pool、 healthmonitor、l7policy、certificate、security_policy， 其中members_per_pool表示一个pool下最多可关联的member数量。  支持多值查询，查询条件格式：quota_key&#x3D;xxx&amp;quota_key&#x3D;xxx。
        :type quota_key: list[str]
        """
        
        

        self._quota_key = None
        self.discriminator = None

        if quota_key is not None:
            self.quota_key = quota_key

    @property
    def quota_key(self):
        """Gets the quota_key of this ListQuotaDetailsRequest.

        资源类型。  取值： loadbalancer、listener、ipgroup、pool、member、members_per_pool、 healthmonitor、l7policy、certificate、security_policy， 其中members_per_pool表示一个pool下最多可关联的member数量。  支持多值查询，查询条件格式：quota_key=xxx&quota_key=xxx。

        :return: The quota_key of this ListQuotaDetailsRequest.
        :rtype: list[str]
        """
        return self._quota_key

    @quota_key.setter
    def quota_key(self, quota_key):
        """Sets the quota_key of this ListQuotaDetailsRequest.

        资源类型。  取值： loadbalancer、listener、ipgroup、pool、member、members_per_pool、 healthmonitor、l7policy、certificate、security_policy， 其中members_per_pool表示一个pool下最多可关联的member数量。  支持多值查询，查询条件格式：quota_key=xxx&quota_key=xxx。

        :param quota_key: The quota_key of this ListQuotaDetailsRequest.
        :type quota_key: list[str]
        """
        self._quota_key = quota_key

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
        if not isinstance(other, ListQuotaDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
