# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRetentionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'algorithm': 'str',
        'id': 'int',
        'rules': 'list[Rule]',
        'scope': 'str'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'id': 'id',
        'rules': 'rules',
        'scope': 'scope'
    }

    def __init__(self, algorithm=None, id=None, rules=None, scope=None):
        """ShowRetentionResponse

        The model defined in huaweicloud sdk

        :param algorithm: 回收规则匹配策略，or
        :type algorithm: str
        :param id: ID
        :type id: int
        :param rules: 镜像老化规则
        :type rules: list[:class:`huaweicloudsdkswr.v2.Rule`]
        :param scope: 保留字段
        :type scope: str
        """
        
        super(ShowRetentionResponse, self).__init__()

        self._algorithm = None
        self._id = None
        self._rules = None
        self._scope = None
        self.discriminator = None

        if algorithm is not None:
            self.algorithm = algorithm
        if id is not None:
            self.id = id
        if rules is not None:
            self.rules = rules
        if scope is not None:
            self.scope = scope

    @property
    def algorithm(self):
        """Gets the algorithm of this ShowRetentionResponse.

        回收规则匹配策略，or

        :return: The algorithm of this ShowRetentionResponse.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this ShowRetentionResponse.

        回收规则匹配策略，or

        :param algorithm: The algorithm of this ShowRetentionResponse.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def id(self):
        """Gets the id of this ShowRetentionResponse.

        ID

        :return: The id of this ShowRetentionResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowRetentionResponse.

        ID

        :param id: The id of this ShowRetentionResponse.
        :type id: int
        """
        self._id = id

    @property
    def rules(self):
        """Gets the rules of this ShowRetentionResponse.

        镜像老化规则

        :return: The rules of this ShowRetentionResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.Rule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this ShowRetentionResponse.

        镜像老化规则

        :param rules: The rules of this ShowRetentionResponse.
        :type rules: list[:class:`huaweicloudsdkswr.v2.Rule`]
        """
        self._rules = rules

    @property
    def scope(self):
        """Gets the scope of this ShowRetentionResponse.

        保留字段

        :return: The scope of this ShowRetentionResponse.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ShowRetentionResponse.

        保留字段

        :param scope: The scope of this ShowRetentionResponse.
        :type scope: str
        """
        self._scope = scope

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
        if not isinstance(other, ShowRetentionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
