# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDatabaseUserRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'name': 'str',
        'cascade': 'bool'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'name': 'name',
        'cascade': 'cascade'
    }

    def __init__(self, cluster_id=None, name=None, cascade=None):
        r"""DeleteDatabaseUserRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param name: **参数解释**： 数据库用户名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        :param cascade: **参数解释**： 是否忽略大小写。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false
        :type cascade: bool
        """
        
        

        self._cluster_id = None
        self._name = None
        self._cascade = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.name = name
        if cascade is not None:
            self.cascade = cascade

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this DeleteDatabaseUserRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The cluster_id of this DeleteDatabaseUserRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this DeleteDatabaseUserRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this DeleteDatabaseUserRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def name(self):
        r"""Gets the name of this DeleteDatabaseUserRequest.

        **参数解释**： 数据库用户名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this DeleteDatabaseUserRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DeleteDatabaseUserRequest.

        **参数解释**： 数据库用户名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this DeleteDatabaseUserRequest.
        :type name: str
        """
        self._name = name

    @property
    def cascade(self):
        r"""Gets the cascade of this DeleteDatabaseUserRequest.

        **参数解释**： 是否忽略大小写。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false

        :return: The cascade of this DeleteDatabaseUserRequest.
        :rtype: bool
        """
        return self._cascade

    @cascade.setter
    def cascade(self, cascade):
        r"""Sets the cascade of this DeleteDatabaseUserRequest.

        **参数解释**： 是否忽略大小写。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false

        :param cascade: The cascade of this DeleteDatabaseUserRequest.
        :type cascade: bool
        """
        self._cascade = cascade

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
        if not isinstance(other, DeleteDatabaseUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
