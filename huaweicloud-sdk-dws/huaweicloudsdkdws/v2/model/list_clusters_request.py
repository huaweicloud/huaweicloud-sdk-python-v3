# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClustersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, enterprise_project_id=None):
        r"""ListClustersRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**： 企业项目ID。查询所有绑定企业项目的集群，则值为all_granted_eps。 **约束限制**： 不涉及。 **取值范围**： all_granted_eps：所有企业项目。 0：表示默认企业项目“default”的ID。 其它：过滤对应企业项目下的数据。 **默认取值**： 不涉及。
        :type enterprise_project_id: str
        """
        
        

        self._enterprise_project_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListClustersRequest.

        **参数解释**： 企业项目ID。查询所有绑定企业项目的集群，则值为all_granted_eps。 **约束限制**： 不涉及。 **取值范围**： all_granted_eps：所有企业项目。 0：表示默认企业项目“default”的ID。 其它：过滤对应企业项目下的数据。 **默认取值**： 不涉及。

        :return: The enterprise_project_id of this ListClustersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListClustersRequest.

        **参数解释**： 企业项目ID。查询所有绑定企业项目的集群，则值为all_granted_eps。 **约束限制**： 不涉及。 **取值范围**： all_granted_eps：所有企业项目。 0：表示默认企业项目“default”的ID。 其它：过滤对应企业项目下的数据。 **默认取值**： 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this ListClustersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListClustersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
