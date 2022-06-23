# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSnapshotReq:

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
        'description': 'str',
        'indices': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'indices': 'indices'
    }

    def __init__(self, name=None, description=None, indices=None):
        """CreateSnapshotReq

        The model defined in huaweicloud sdk

        :param name: 快照名称，快照名称在4位到64位之间，必须以字母开头，可以包含字母、数字、中划线或者下划线，注意字母不能大写且不能包含其他特殊字符。
        :type name: str
        :param description: 快照描述，0～256个字符，不能包含!&lt;&gt;&#x3D;&amp;\\\&quot;&#39;字符。
        :type description: str
        :param indices: 指定要备份的索引名称，多个索引用逗号隔开，默认备份所有索引。支持使用“\\*”匹配多个索引，例如：2018-06\\*，表示备份名称前缀是2018-06的所有索引的数据。  0～1024个字符，不能包含空格和大写字母，且不能包含\\\&quot;\\\\&lt;|&gt;/?特殊字符。
        :type indices: str
        """
        
        

        self._name = None
        self._description = None
        self._indices = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if indices is not None:
            self.indices = indices

    @property
    def name(self):
        """Gets the name of this CreateSnapshotReq.

        快照名称，快照名称在4位到64位之间，必须以字母开头，可以包含字母、数字、中划线或者下划线，注意字母不能大写且不能包含其他特殊字符。

        :return: The name of this CreateSnapshotReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSnapshotReq.

        快照名称，快照名称在4位到64位之间，必须以字母开头，可以包含字母、数字、中划线或者下划线，注意字母不能大写且不能包含其他特殊字符。

        :param name: The name of this CreateSnapshotReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateSnapshotReq.

        快照描述，0～256个字符，不能包含!<>=&\\\"'字符。

        :return: The description of this CreateSnapshotReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSnapshotReq.

        快照描述，0～256个字符，不能包含!<>=&\\\"'字符。

        :param description: The description of this CreateSnapshotReq.
        :type description: str
        """
        self._description = description

    @property
    def indices(self):
        """Gets the indices of this CreateSnapshotReq.

        指定要备份的索引名称，多个索引用逗号隔开，默认备份所有索引。支持使用“\\*”匹配多个索引，例如：2018-06\\*，表示备份名称前缀是2018-06的所有索引的数据。  0～1024个字符，不能包含空格和大写字母，且不能包含\\\"\\\\<|>/?特殊字符。

        :return: The indices of this CreateSnapshotReq.
        :rtype: str
        """
        return self._indices

    @indices.setter
    def indices(self, indices):
        """Sets the indices of this CreateSnapshotReq.

        指定要备份的索引名称，多个索引用逗号隔开，默认备份所有索引。支持使用“\\*”匹配多个索引，例如：2018-06\\*，表示备份名称前缀是2018-06的所有索引的数据。  0～1024个字符，不能包含空格和大写字母，且不能包含\\\"\\\\<|>/?特殊字符。

        :param indices: The indices of this CreateSnapshotReq.
        :type indices: str
        """
        self._indices = indices

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
        if not isinstance(other, CreateSnapshotReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
