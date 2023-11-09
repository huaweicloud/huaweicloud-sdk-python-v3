# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLeagueRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'league_id': 'str',
        'body': 'LeagueUpdateVo'
    }

    attribute_map = {
        'league_id': 'league_id',
        'body': 'body'
    }

    def __init__(self, league_id=None, body=None):
        """UpdateLeagueRequest

        The model defined in huaweicloud sdk

        :param league_id: 联盟id，最大32位，字母和数字组成
        :type league_id: str
        :param body: Body of the UpdateLeagueRequest
        :type body: :class:`huaweicloudsdktics.v1.LeagueUpdateVo`
        """
        
        

        self._league_id = None
        self._body = None
        self.discriminator = None

        self.league_id = league_id
        if body is not None:
            self.body = body

    @property
    def league_id(self):
        """Gets the league_id of this UpdateLeagueRequest.

        联盟id，最大32位，字母和数字组成

        :return: The league_id of this UpdateLeagueRequest.
        :rtype: str
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this UpdateLeagueRequest.

        联盟id，最大32位，字母和数字组成

        :param league_id: The league_id of this UpdateLeagueRequest.
        :type league_id: str
        """
        self._league_id = league_id

    @property
    def body(self):
        """Gets the body of this UpdateLeagueRequest.

        :return: The body of this UpdateLeagueRequest.
        :rtype: :class:`huaweicloudsdktics.v1.LeagueUpdateVo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateLeagueRequest.

        :param body: The body of this UpdateLeagueRequest.
        :type body: :class:`huaweicloudsdktics.v1.LeagueUpdateVo`
        """
        self._body = body

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
        if not isinstance(other, UpdateLeagueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
