# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResRelation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'self_resource_id': 'str',
        'relation_infos': 'list[RelationInfo]'
    }

    attribute_map = {
        'self_resource_id': 'self_resource_id',
        'relation_infos': 'relation_infos'
    }

    def __init__(self, self_resource_id=None, relation_infos=None):
        r"""ResRelation

        The model defined in huaweicloud sdk

        :param self_resource_id: |参数名称：当前费用对应的资源ID| |参数约束及描述：当前费用对应的资源ID|
        :type self_resource_id: str
        :param relation_infos: |参数名称：当前费用对应资源ID关联的资源信息。| |参数约束及描述：当前费用对应资源ID关联的资源信息，数组个数不超过2层|
        :type relation_infos: list[:class:`huaweicloudsdkbss.v2.RelationInfo`]
        """
        
        

        self._self_resource_id = None
        self._relation_infos = None
        self.discriminator = None

        if self_resource_id is not None:
            self.self_resource_id = self_resource_id
        if relation_infos is not None:
            self.relation_infos = relation_infos

    @property
    def self_resource_id(self):
        r"""Gets the self_resource_id of this ResRelation.

        |参数名称：当前费用对应的资源ID| |参数约束及描述：当前费用对应的资源ID|

        :return: The self_resource_id of this ResRelation.
        :rtype: str
        """
        return self._self_resource_id

    @self_resource_id.setter
    def self_resource_id(self, self_resource_id):
        r"""Sets the self_resource_id of this ResRelation.

        |参数名称：当前费用对应的资源ID| |参数约束及描述：当前费用对应的资源ID|

        :param self_resource_id: The self_resource_id of this ResRelation.
        :type self_resource_id: str
        """
        self._self_resource_id = self_resource_id

    @property
    def relation_infos(self):
        r"""Gets the relation_infos of this ResRelation.

        |参数名称：当前费用对应资源ID关联的资源信息。| |参数约束及描述：当前费用对应资源ID关联的资源信息，数组个数不超过2层|

        :return: The relation_infos of this ResRelation.
        :rtype: list[:class:`huaweicloudsdkbss.v2.RelationInfo`]
        """
        return self._relation_infos

    @relation_infos.setter
    def relation_infos(self, relation_infos):
        r"""Sets the relation_infos of this ResRelation.

        |参数名称：当前费用对应资源ID关联的资源信息。| |参数约束及描述：当前费用对应资源ID关联的资源信息，数组个数不超过2层|

        :param relation_infos: The relation_infos of this ResRelation.
        :type relation_infos: list[:class:`huaweicloudsdkbss.v2.RelationInfo`]
        """
        self._relation_infos = relation_infos

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
        if not isinstance(other, ResRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
