# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Snapshot:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'cluster_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cluster_id': 'cluster_id',
        'description': 'description'
    }

    def __init__(self, name=None, cluster_id=None, description=None):
        """Snapshot

        The model defined in huaweicloud sdk

        :param name: 快照名称，要求唯一性且必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符，长度为4～64个字符。
        :type name: str
        :param cluster_id: 指定创建快照的集群ID
        :type cluster_id: str
        :param description: 快照描述，若不指定，描述为空。快照描述的字符长度不能超过256个字符，且不支持特殊字符!&lt;&gt;&#39;&#x3D;&amp;\&quot;。
        :type description: str
        """
        
        

        self._name = None
        self._cluster_id = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.cluster_id = cluster_id
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this Snapshot.

        快照名称，要求唯一性且必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符，长度为4～64个字符。

        :return: The name of this Snapshot.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Snapshot.

        快照名称，要求唯一性且必须以字母开头，不区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符，长度为4～64个字符。

        :param name: The name of this Snapshot.
        :type name: str
        """
        self._name = name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this Snapshot.

        指定创建快照的集群ID

        :return: The cluster_id of this Snapshot.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this Snapshot.

        指定创建快照的集群ID

        :param cluster_id: The cluster_id of this Snapshot.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def description(self):
        """Gets the description of this Snapshot.

        快照描述，若不指定，描述为空。快照描述的字符长度不能超过256个字符，且不支持特殊字符!<>'=&\"。

        :return: The description of this Snapshot.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Snapshot.

        快照描述，若不指定，描述为空。快照描述的字符长度不能超过256个字符，且不支持特殊字符!<>'=&\"。

        :param description: The description of this Snapshot.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, Snapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
