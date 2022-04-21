# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterInfoRequestModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'competition_id': 'str',
        'stage_id': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'competition_id': 'competition_id',
        'stage_id': 'stage_id',
        'domain_id': 'domain_id'
    }

    def __init__(self, competition_id=None, stage_id=None, domain_id=None):
        """RegisterInfoRequestModel

        The model defined in huaweicloud sdk

        :param competition_id: 大赛ID，大赛平台提供
        :type competition_id: str
        :param stage_id: 大赛阶段ID，大赛平台提供
        :type stage_id: str
        :param domain_id: 租户ID
        :type domain_id: str
        """
        
        

        self._competition_id = None
        self._stage_id = None
        self._domain_id = None
        self.discriminator = None

        self.competition_id = competition_id
        self.stage_id = stage_id
        self.domain_id = domain_id

    @property
    def competition_id(self):
        """Gets the competition_id of this RegisterInfoRequestModel.

        大赛ID，大赛平台提供

        :return: The competition_id of this RegisterInfoRequestModel.
        :rtype: str
        """
        return self._competition_id

    @competition_id.setter
    def competition_id(self, competition_id):
        """Sets the competition_id of this RegisterInfoRequestModel.

        大赛ID，大赛平台提供

        :param competition_id: The competition_id of this RegisterInfoRequestModel.
        :type competition_id: str
        """
        self._competition_id = competition_id

    @property
    def stage_id(self):
        """Gets the stage_id of this RegisterInfoRequestModel.

        大赛阶段ID，大赛平台提供

        :return: The stage_id of this RegisterInfoRequestModel.
        :rtype: str
        """
        return self._stage_id

    @stage_id.setter
    def stage_id(self, stage_id):
        """Sets the stage_id of this RegisterInfoRequestModel.

        大赛阶段ID，大赛平台提供

        :param stage_id: The stage_id of this RegisterInfoRequestModel.
        :type stage_id: str
        """
        self._stage_id = stage_id

    @property
    def domain_id(self):
        """Gets the domain_id of this RegisterInfoRequestModel.

        租户ID

        :return: The domain_id of this RegisterInfoRequestModel.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this RegisterInfoRequestModel.

        租户ID

        :param domain_id: The domain_id of this RegisterInfoRequestModel.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, RegisterInfoRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
