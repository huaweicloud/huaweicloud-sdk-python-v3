# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobInstanceDagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'league_id': 'str',
        'round_id': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'league_id': 'league_id',
        'round_id': 'round_id'
    }

    def __init__(self, instance_id=None, league_id=None, round_id=None):
        """ShowJobInstanceDagRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例id，最大32位，字母和数字组成
        :type instance_id: str
        :param league_id: 联盟id，最大32位，字母和数字组成
        :type league_id: str
        :param round_id: 轮数，最小值0最大值0x7fffffff
        :type round_id: int
        """
        
        

        self._instance_id = None
        self._league_id = None
        self._round_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.league_id = league_id
        self.round_id = round_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowJobInstanceDagRequest.

        实例id，最大32位，字母和数字组成

        :return: The instance_id of this ShowJobInstanceDagRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowJobInstanceDagRequest.

        实例id，最大32位，字母和数字组成

        :param instance_id: The instance_id of this ShowJobInstanceDagRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def league_id(self):
        """Gets the league_id of this ShowJobInstanceDagRequest.

        联盟id，最大32位，字母和数字组成

        :return: The league_id of this ShowJobInstanceDagRequest.
        :rtype: str
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this ShowJobInstanceDagRequest.

        联盟id，最大32位，字母和数字组成

        :param league_id: The league_id of this ShowJobInstanceDagRequest.
        :type league_id: str
        """
        self._league_id = league_id

    @property
    def round_id(self):
        """Gets the round_id of this ShowJobInstanceDagRequest.

        轮数，最小值0最大值0x7fffffff

        :return: The round_id of this ShowJobInstanceDagRequest.
        :rtype: int
        """
        return self._round_id

    @round_id.setter
    def round_id(self, round_id):
        """Sets the round_id of this ShowJobInstanceDagRequest.

        轮数，最小值0最大值0x7fffffff

        :param round_id: The round_id of this ShowJobInstanceDagRequest.
        :type round_id: int
        """
        self._round_id = round_id

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
        if not isinstance(other, ShowJobInstanceDagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
