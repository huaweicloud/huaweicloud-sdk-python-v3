# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OuNameInfo:

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
        'domain_id': 'str',
        'domain': 'str',
        'ou_name': 'str',
        'ou_dn': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'domain': 'domain',
        'ou_name': 'ou_name',
        'ou_dn': 'ou_dn',
        'description': 'description'
    }

    def __init__(self, id=None, domain_id=None, domain=None, ou_name=None, ou_dn=None, description=None):
        r"""OuNameInfo

        The model defined in huaweicloud sdk

        :param id: ouid。
        :type id: str
        :param domain_id: 域id。
        :type domain_id: str
        :param domain: 域名称。
        :type domain: str
        :param ou_name: OU名称。
        :type ou_name: str
        :param ou_dn: ouDn。
        :type ou_dn: str
        :param description: 描述。
        :type description: str
        """
        
        

        self._id = None
        self._domain_id = None
        self._domain = None
        self._ou_name = None
        self._ou_dn = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if domain is not None:
            self.domain = domain
        if ou_name is not None:
            self.ou_name = ou_name
        if ou_dn is not None:
            self.ou_dn = ou_dn
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this OuNameInfo.

        ouid。

        :return: The id of this OuNameInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OuNameInfo.

        ouid。

        :param id: The id of this OuNameInfo.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this OuNameInfo.

        域id。

        :return: The domain_id of this OuNameInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this OuNameInfo.

        域id。

        :param domain_id: The domain_id of this OuNameInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain(self):
        r"""Gets the domain of this OuNameInfo.

        域名称。

        :return: The domain of this OuNameInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this OuNameInfo.

        域名称。

        :param domain: The domain of this OuNameInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def ou_name(self):
        r"""Gets the ou_name of this OuNameInfo.

        OU名称。

        :return: The ou_name of this OuNameInfo.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        r"""Sets the ou_name of this OuNameInfo.

        OU名称。

        :param ou_name: The ou_name of this OuNameInfo.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def ou_dn(self):
        r"""Gets the ou_dn of this OuNameInfo.

        ouDn。

        :return: The ou_dn of this OuNameInfo.
        :rtype: str
        """
        return self._ou_dn

    @ou_dn.setter
    def ou_dn(self, ou_dn):
        r"""Sets the ou_dn of this OuNameInfo.

        ouDn。

        :param ou_dn: The ou_dn of this OuNameInfo.
        :type ou_dn: str
        """
        self._ou_dn = ou_dn

    @property
    def description(self):
        r"""Gets the description of this OuNameInfo.

        描述。

        :return: The description of this OuNameInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OuNameInfo.

        描述。

        :param description: The description of this OuNameInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, OuNameInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
