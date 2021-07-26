# coding: utf-8

import re
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
        """AgencyTokenProject - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._id = None
        self._domain = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.domain = domain

    @property
    def name(self):
        """Gets the name of this AgencyTokenProject.

        委托方A的项目名称。

        :return: The name of this AgencyTokenProject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgencyTokenProject.

        委托方A的项目名称。

        :param name: The name of this AgencyTokenProject.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this AgencyTokenProject.

        委托方A的项目ID。

        :return: The id of this AgencyTokenProject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AgencyTokenProject.

        委托方A的项目ID。

        :param id: The id of this AgencyTokenProject.
        :type: str
        """
        self._id = id

    @property
    def domain(self):
        """Gets the domain of this AgencyTokenProject.


        :return: The domain of this AgencyTokenProject.
        :rtype: AgencyTokenProjectDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AgencyTokenProject.


        :param domain: The domain of this AgencyTokenProject.
        :type: AgencyTokenProjectDomain
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AgencyTokenProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
