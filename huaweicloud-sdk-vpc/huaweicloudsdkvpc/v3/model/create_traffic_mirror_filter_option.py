# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTrafficMirrorFilterOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, description=None, name=None):
        r"""CreateTrafficMirrorFilterOption

        The model defined in huaweicloud sdk

        :param description: 功能说明：流量镜像筛选条件的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param name: 功能说明：流量镜像筛选条件的名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        """
        
        

        self._description = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name

    @property
    def description(self):
        r"""Gets the description of this CreateTrafficMirrorFilterOption.

        功能说明：流量镜像筛选条件的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this CreateTrafficMirrorFilterOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateTrafficMirrorFilterOption.

        功能说明：流量镜像筛选条件的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this CreateTrafficMirrorFilterOption.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this CreateTrafficMirrorFilterOption.

        功能说明：流量镜像筛选条件的名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this CreateTrafficMirrorFilterOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateTrafficMirrorFilterOption.

        功能说明：流量镜像筛选条件的名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this CreateTrafficMirrorFilterOption.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CreateTrafficMirrorFilterOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
