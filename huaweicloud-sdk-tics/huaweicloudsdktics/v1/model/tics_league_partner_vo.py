# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsLeaguePartnerVo:

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
        'partner_domain_alias': 'str',
        'partner_domain_name': 'str',
        'partner_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'partner_domain_alias': 'partner_domain_alias',
        'partner_domain_name': 'partner_domain_name',
        'partner_status': 'partner_status'
    }

    def __init__(self, id=None, partner_domain_alias=None, partner_domain_name=None, partner_status=None):
        """TicsLeaguePartnerVo

        The model defined in huaweicloud sdk

        :param id: 联盟合作方Id
        :type id: str
        :param partner_domain_alias: 联盟合作方别名
        :type partner_domain_alias: str
        :param partner_domain_name: 联盟合作方租户名
        :type partner_domain_name: str
        :param partner_status: 联盟合作方状态
        :type partner_status: str
        """
        
        

        self._id = None
        self._partner_domain_alias = None
        self._partner_domain_name = None
        self._partner_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if partner_domain_alias is not None:
            self.partner_domain_alias = partner_domain_alias
        if partner_domain_name is not None:
            self.partner_domain_name = partner_domain_name
        if partner_status is not None:
            self.partner_status = partner_status

    @property
    def id(self):
        """Gets the id of this TicsLeaguePartnerVo.

        联盟合作方Id

        :return: The id of this TicsLeaguePartnerVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TicsLeaguePartnerVo.

        联盟合作方Id

        :param id: The id of this TicsLeaguePartnerVo.
        :type id: str
        """
        self._id = id

    @property
    def partner_domain_alias(self):
        """Gets the partner_domain_alias of this TicsLeaguePartnerVo.

        联盟合作方别名

        :return: The partner_domain_alias of this TicsLeaguePartnerVo.
        :rtype: str
        """
        return self._partner_domain_alias

    @partner_domain_alias.setter
    def partner_domain_alias(self, partner_domain_alias):
        """Sets the partner_domain_alias of this TicsLeaguePartnerVo.

        联盟合作方别名

        :param partner_domain_alias: The partner_domain_alias of this TicsLeaguePartnerVo.
        :type partner_domain_alias: str
        """
        self._partner_domain_alias = partner_domain_alias

    @property
    def partner_domain_name(self):
        """Gets the partner_domain_name of this TicsLeaguePartnerVo.

        联盟合作方租户名

        :return: The partner_domain_name of this TicsLeaguePartnerVo.
        :rtype: str
        """
        return self._partner_domain_name

    @partner_domain_name.setter
    def partner_domain_name(self, partner_domain_name):
        """Sets the partner_domain_name of this TicsLeaguePartnerVo.

        联盟合作方租户名

        :param partner_domain_name: The partner_domain_name of this TicsLeaguePartnerVo.
        :type partner_domain_name: str
        """
        self._partner_domain_name = partner_domain_name

    @property
    def partner_status(self):
        """Gets the partner_status of this TicsLeaguePartnerVo.

        联盟合作方状态

        :return: The partner_status of this TicsLeaguePartnerVo.
        :rtype: str
        """
        return self._partner_status

    @partner_status.setter
    def partner_status(self, partner_status):
        """Sets the partner_status of this TicsLeaguePartnerVo.

        联盟合作方状态

        :param partner_status: The partner_status of this TicsLeaguePartnerVo.
        :type partner_status: str
        """
        self._partner_status = partner_status

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
        if not isinstance(other, TicsLeaguePartnerVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
