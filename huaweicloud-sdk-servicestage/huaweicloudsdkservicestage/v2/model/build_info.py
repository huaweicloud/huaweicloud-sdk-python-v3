# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'parameters': 'BuildInfoParameters'
    }

    attribute_map = {
        'id': 'id',
        'parameters': 'parameters'
    }

    def __init__(self, id=None, parameters=None):
        r"""BuildInfo

        The model defined in huaweicloud sdk

        :param id: 构建ID，查看构建列表获取。
        :type id: str
        :param parameters: 
        :type parameters: :class:`huaweicloudsdkservicestage.v2.BuildInfoParameters`
        """
        
        

        self._id = None
        self._parameters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parameters is not None:
            self.parameters = parameters

    @property
    def id(self):
        r"""Gets the id of this BuildInfo.

        构建ID，查看构建列表获取。

        :return: The id of this BuildInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BuildInfo.

        构建ID，查看构建列表获取。

        :param id: The id of this BuildInfo.
        :type id: str
        """
        self._id = id

    @property
    def parameters(self):
        r"""Gets the parameters of this BuildInfo.

        :return: The parameters of this BuildInfo.
        :rtype: :class:`huaweicloudsdkservicestage.v2.BuildInfoParameters`
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this BuildInfo.

        :param parameters: The parameters of this BuildInfo.
        :type parameters: :class:`huaweicloudsdkservicestage.v2.BuildInfoParameters`
        """
        self._parameters = parameters

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
        if not isinstance(other, BuildInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
