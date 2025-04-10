# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserOrgRelationListResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'org_id': 'str',
        'relation_type': 'str'
    }

    attribute_map = {
        'org_id': 'org_id',
        'relation_type': 'relation_type'
    }

    def __init__(self, org_id=None, relation_type=None):
        r"""UserOrgRelationListResult

        The model defined in huaweicloud sdk

        :param org_id: 组织id
        :type org_id: str
        :param relation_type: 关系类型。
        :type relation_type: str
        """
        
        

        self._org_id = None
        self._relation_type = None
        self.discriminator = None

        self.org_id = org_id
        self.relation_type = relation_type

    @property
    def org_id(self):
        r"""Gets the org_id of this UserOrgRelationListResult.

        组织id

        :return: The org_id of this UserOrgRelationListResult.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        r"""Sets the org_id of this UserOrgRelationListResult.

        组织id

        :param org_id: The org_id of this UserOrgRelationListResult.
        :type org_id: str
        """
        self._org_id = org_id

    @property
    def relation_type(self):
        r"""Gets the relation_type of this UserOrgRelationListResult.

        关系类型。

        :return: The relation_type of this UserOrgRelationListResult.
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        r"""Sets the relation_type of this UserOrgRelationListResult.

        关系类型。

        :param relation_type: The relation_type of this UserOrgRelationListResult.
        :type relation_type: str
        """
        self._relation_type = relation_type

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
        if not isinstance(other, UserOrgRelationListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
