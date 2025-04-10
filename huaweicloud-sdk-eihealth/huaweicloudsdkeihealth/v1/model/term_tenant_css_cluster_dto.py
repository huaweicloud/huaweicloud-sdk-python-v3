# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TermTenantCssClusterDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'css_id': 'str',
        'name': 'str',
        'is_active': 'bool'
    }

    attribute_map = {
        'css_id': 'css_id',
        'name': 'name',
        'is_active': 'is_active'
    }

    def __init__(self, css_id=None, name=None, is_active=None):
        r"""TermTenantCssClusterDto

        The model defined in huaweicloud sdk

        :param css_id: css集群id
        :type css_id: str
        :param name: css集群名称
        :type name: str
        :param is_active: 集群是否可用
        :type is_active: bool
        """
        
        

        self._css_id = None
        self._name = None
        self._is_active = None
        self.discriminator = None

        if css_id is not None:
            self.css_id = css_id
        if name is not None:
            self.name = name
        if is_active is not None:
            self.is_active = is_active

    @property
    def css_id(self):
        r"""Gets the css_id of this TermTenantCssClusterDto.

        css集群id

        :return: The css_id of this TermTenantCssClusterDto.
        :rtype: str
        """
        return self._css_id

    @css_id.setter
    def css_id(self, css_id):
        r"""Sets the css_id of this TermTenantCssClusterDto.

        css集群id

        :param css_id: The css_id of this TermTenantCssClusterDto.
        :type css_id: str
        """
        self._css_id = css_id

    @property
    def name(self):
        r"""Gets the name of this TermTenantCssClusterDto.

        css集群名称

        :return: The name of this TermTenantCssClusterDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TermTenantCssClusterDto.

        css集群名称

        :param name: The name of this TermTenantCssClusterDto.
        :type name: str
        """
        self._name = name

    @property
    def is_active(self):
        r"""Gets the is_active of this TermTenantCssClusterDto.

        集群是否可用

        :return: The is_active of this TermTenantCssClusterDto.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        r"""Sets the is_active of this TermTenantCssClusterDto.

        集群是否可用

        :param is_active: The is_active of this TermTenantCssClusterDto.
        :type is_active: bool
        """
        self._is_active = is_active

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
        if not isinstance(other, TermTenantCssClusterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
