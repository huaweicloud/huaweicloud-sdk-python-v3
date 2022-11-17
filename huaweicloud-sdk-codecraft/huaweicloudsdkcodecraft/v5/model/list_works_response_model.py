# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorksResponseModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'works_id': 'str',
        'domain_id': 'str',
        'team_id': 'str'
    }

    attribute_map = {
        'works_id': 'works_id',
        'domain_id': 'domain_id',
        'team_id': 'team_id'
    }

    def __init__(self, works_id=None, domain_id=None, team_id=None):
        """ListWorksResponseModel

        The model defined in huaweicloud sdk

        :param works_id: 作品ID
        :type works_id: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param team_id: 团队ID
        :type team_id: str
        """
        
        

        self._works_id = None
        self._domain_id = None
        self._team_id = None
        self.discriminator = None

        self.works_id = works_id
        self.domain_id = domain_id
        self.team_id = team_id

    @property
    def works_id(self):
        """Gets the works_id of this ListWorksResponseModel.

        作品ID

        :return: The works_id of this ListWorksResponseModel.
        :rtype: str
        """
        return self._works_id

    @works_id.setter
    def works_id(self, works_id):
        """Sets the works_id of this ListWorksResponseModel.

        作品ID

        :param works_id: The works_id of this ListWorksResponseModel.
        :type works_id: str
        """
        self._works_id = works_id

    @property
    def domain_id(self):
        """Gets the domain_id of this ListWorksResponseModel.

        租户ID

        :return: The domain_id of this ListWorksResponseModel.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListWorksResponseModel.

        租户ID

        :param domain_id: The domain_id of this ListWorksResponseModel.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def team_id(self):
        """Gets the team_id of this ListWorksResponseModel.

        团队ID

        :return: The team_id of this ListWorksResponseModel.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this ListWorksResponseModel.

        团队ID

        :param team_id: The team_id of this ListWorksResponseModel.
        :type team_id: str
        """
        self._team_id = team_id

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
        if not isinstance(other, ListWorksResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
