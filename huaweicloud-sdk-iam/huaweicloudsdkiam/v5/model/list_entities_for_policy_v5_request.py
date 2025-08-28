# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEntitiesForPolicyV5Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'entity_type': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'entity_type': 'entity_type',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, policy_id=None, entity_type=None, limit=None, marker=None):
        r"""ListEntitiesForPolicyV5Request

        The model defined in huaweicloud sdk

        :param policy_id: 身份策略ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type policy_id: str
        :param entity_type: 实体类型，包含user、 group 和 agency三种类型。
        :type entity_type: str
        :param limit: 每页显示的条目数量，范围为1到200条，默认为100条。
        :type limit: int
        :param marker: 分页标记，长度为4到400个字符，只包含字母、数字、\&quot;+\&quot;、\&quot;/\&quot;、\&quot;&#x3D;\&quot;、\&quot;-\&quot;和\&quot;_\&quot;的字符串。
        :type marker: str
        """
        
        

        self._policy_id = None
        self._entity_type = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.policy_id = policy_id
        if entity_type is not None:
            self.entity_type = entity_type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListEntitiesForPolicyV5Request.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The policy_id of this ListEntitiesForPolicyV5Request.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListEntitiesForPolicyV5Request.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param policy_id: The policy_id of this ListEntitiesForPolicyV5Request.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def entity_type(self):
        r"""Gets the entity_type of this ListEntitiesForPolicyV5Request.

        实体类型，包含user、 group 和 agency三种类型。

        :return: The entity_type of this ListEntitiesForPolicyV5Request.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        r"""Sets the entity_type of this ListEntitiesForPolicyV5Request.

        实体类型，包含user、 group 和 agency三种类型。

        :param entity_type: The entity_type of this ListEntitiesForPolicyV5Request.
        :type entity_type: str
        """
        self._entity_type = entity_type

    @property
    def limit(self):
        r"""Gets the limit of this ListEntitiesForPolicyV5Request.

        每页显示的条目数量，范围为1到200条，默认为100条。

        :return: The limit of this ListEntitiesForPolicyV5Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEntitiesForPolicyV5Request.

        每页显示的条目数量，范围为1到200条，默认为100条。

        :param limit: The limit of this ListEntitiesForPolicyV5Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListEntitiesForPolicyV5Request.

        分页标记，长度为4到400个字符，只包含字母、数字、\"+\"、\"/\"、\"=\"、\"-\"和\"_\"的字符串。

        :return: The marker of this ListEntitiesForPolicyV5Request.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListEntitiesForPolicyV5Request.

        分页标记，长度为4到400个字符，只包含字母、数字、\"+\"、\"/\"、\"=\"、\"-\"和\"_\"的字符串。

        :param marker: The marker of this ListEntitiesForPolicyV5Request.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListEntitiesForPolicyV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
