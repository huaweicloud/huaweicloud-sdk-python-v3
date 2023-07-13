# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterCompetitionInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_permitted': 'bool',
        'team_id': 'str'
    }

    attribute_map = {
        'is_permitted': 'is_permitted',
        'team_id': 'team_id'
    }

    def __init__(self, is_permitted=None, team_id=None):
        """RegisterCompetitionInfoResponse

        The model defined in huaweicloud sdk

        :param is_permitted: 是否允许提交作品，true-允许，false-不允许
        :type is_permitted: bool
        :param team_id: 团队ID
        :type team_id: str
        """
        
        super(RegisterCompetitionInfoResponse, self).__init__()

        self._is_permitted = None
        self._team_id = None
        self.discriminator = None

        if is_permitted is not None:
            self.is_permitted = is_permitted
        if team_id is not None:
            self.team_id = team_id

    @property
    def is_permitted(self):
        """Gets the is_permitted of this RegisterCompetitionInfoResponse.

        是否允许提交作品，true-允许，false-不允许

        :return: The is_permitted of this RegisterCompetitionInfoResponse.
        :rtype: bool
        """
        return self._is_permitted

    @is_permitted.setter
    def is_permitted(self, is_permitted):
        """Sets the is_permitted of this RegisterCompetitionInfoResponse.

        是否允许提交作品，true-允许，false-不允许

        :param is_permitted: The is_permitted of this RegisterCompetitionInfoResponse.
        :type is_permitted: bool
        """
        self._is_permitted = is_permitted

    @property
    def team_id(self):
        """Gets the team_id of this RegisterCompetitionInfoResponse.

        团队ID

        :return: The team_id of this RegisterCompetitionInfoResponse.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this RegisterCompetitionInfoResponse.

        团队ID

        :param team_id: The team_id of this RegisterCompetitionInfoResponse.
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
        if not isinstance(other, RegisterCompetitionInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
