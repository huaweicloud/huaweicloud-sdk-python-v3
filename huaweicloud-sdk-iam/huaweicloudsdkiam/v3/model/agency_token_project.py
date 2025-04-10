# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyTokenProject:

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
        'id': 'str',
        'domain': 'AgencyTokenProjectDomain'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'domain': 'domain'
    }

    def __init__(self, name=None, id=None, domain=None):
        r"""AgencyTokenProject

        The model defined in huaweicloud sdk

        :param name: 委托方A的项目名称。
        :type name: str
        :param id: 委托方A的项目ID。
        :type id: str
        :param domain: 
        :type domain: :class:`huaweicloudsdkiam.v3.AgencyTokenProjectDomain`
        """
        
        

        self._name = None
        self._id = None
        self._domain = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.domain = domain

    @property
    def name(self):
        r"""Gets the name of this AgencyTokenProject.

        委托方A的项目名称。

        :return: The name of this AgencyTokenProject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AgencyTokenProject.

        委托方A的项目名称。

        :param name: The name of this AgencyTokenProject.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this AgencyTokenProject.

        委托方A的项目ID。

        :return: The id of this AgencyTokenProject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AgencyTokenProject.

        委托方A的项目ID。

        :param id: The id of this AgencyTokenProject.
        :type id: str
        """
        self._id = id

    @property
    def domain(self):
        r"""Gets the domain of this AgencyTokenProject.

        :return: The domain of this AgencyTokenProject.
        :rtype: :class:`huaweicloudsdkiam.v3.AgencyTokenProjectDomain`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this AgencyTokenProject.

        :param domain: The domain of this AgencyTokenProject.
        :type domain: :class:`huaweicloudsdkiam.v3.AgencyTokenProjectDomain`
        """
        self._domain = domain

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
        if not isinstance(other, AgencyTokenProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
