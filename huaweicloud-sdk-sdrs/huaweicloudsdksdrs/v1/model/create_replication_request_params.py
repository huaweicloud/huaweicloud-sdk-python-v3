# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateReplicationRequestParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_group_id': 'str',
        'volume_id': 'str',
        'name': 'str',
        'description': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'server_group_id': 'server_group_id',
        'volume_id': 'volume_id',
        'name': 'name',
        'description': 'description',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, server_group_id=None, volume_id=None, name=None, description=None, cluster_id=None):
        """CreateReplicationRequestParams

        The model defined in huaweicloud sdk

        :param server_group_id: 保护组的ID。
        :type server_group_id: str
        :param volume_id: 生产站点卷的ID。
        :type volume_id: str
        :param name: 指定复制对的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。
        :type name: str
        :param description: 指定复制对的描述，最大支持长度为64个字节，不能包含左尖括号（&lt;）或右尖括号（&gt;）。
        :type description: str
        :param cluster_id: 专属分布式存储池ID。
        :type cluster_id: str
        """
        
        

        self._server_group_id = None
        self._volume_id = None
        self._name = None
        self._description = None
        self._cluster_id = None
        self.discriminator = None

        self.server_group_id = server_group_id
        self.volume_id = volume_id
        self.name = name
        if description is not None:
            self.description = description
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def server_group_id(self):
        """Gets the server_group_id of this CreateReplicationRequestParams.

        保护组的ID。

        :return: The server_group_id of this CreateReplicationRequestParams.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this CreateReplicationRequestParams.

        保护组的ID。

        :param server_group_id: The server_group_id of this CreateReplicationRequestParams.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def volume_id(self):
        """Gets the volume_id of this CreateReplicationRequestParams.

        生产站点卷的ID。

        :return: The volume_id of this CreateReplicationRequestParams.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this CreateReplicationRequestParams.

        生产站点卷的ID。

        :param volume_id: The volume_id of this CreateReplicationRequestParams.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def name(self):
        """Gets the name of this CreateReplicationRequestParams.

        指定复制对的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。

        :return: The name of this CreateReplicationRequestParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateReplicationRequestParams.

        指定复制对的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。

        :param name: The name of this CreateReplicationRequestParams.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateReplicationRequestParams.

        指定复制对的描述，最大支持长度为64个字节，不能包含左尖括号（<）或右尖括号（>）。

        :return: The description of this CreateReplicationRequestParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateReplicationRequestParams.

        指定复制对的描述，最大支持长度为64个字节，不能包含左尖括号（<）或右尖括号（>）。

        :param description: The description of this CreateReplicationRequestParams.
        :type description: str
        """
        self._description = description

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateReplicationRequestParams.

        专属分布式存储池ID。

        :return: The cluster_id of this CreateReplicationRequestParams.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateReplicationRequestParams.

        专属分布式存储池ID。

        :param cluster_id: The cluster_id of this CreateReplicationRequestParams.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, CreateReplicationRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
