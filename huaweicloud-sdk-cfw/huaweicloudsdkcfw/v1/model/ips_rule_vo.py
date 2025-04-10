# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsRuleVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'affected_application': 'str',
        'create_time': 'str',
        'default_status': 'str',
        'ips_cve': 'str',
        'ips_group': 'str',
        'ips_id': 'str',
        'ips_level': 'str',
        'ips_name': 'str',
        'ips_rules_type': 'str',
        'ips_status': 'str'
    }

    attribute_map = {
        'affected_application': 'affected_application',
        'create_time': 'create_time',
        'default_status': 'default_status',
        'ips_cve': 'ips_cve',
        'ips_group': 'ips_group',
        'ips_id': 'ips_id',
        'ips_level': 'ips_level',
        'ips_name': 'ips_name',
        'ips_rules_type': 'ips_rules_type',
        'ips_status': 'ips_status'
    }

    def __init__(self, affected_application=None, create_time=None, default_status=None, ips_cve=None, ips_group=None, ips_id=None, ips_level=None, ips_name=None, ips_rules_type=None, ips_status=None):
        r"""IpsRuleVO

        The model defined in huaweicloud sdk

        :param affected_application: 
        :type affected_application: str
        :param create_time: 
        :type create_time: str
        :param default_status: 
        :type default_status: str
        :param ips_cve: 
        :type ips_cve: str
        :param ips_group: 
        :type ips_group: str
        :param ips_id: 
        :type ips_id: str
        :param ips_level: 
        :type ips_level: str
        :param ips_name: 
        :type ips_name: str
        :param ips_rules_type: 
        :type ips_rules_type: str
        :param ips_status: 
        :type ips_status: str
        """
        
        

        self._affected_application = None
        self._create_time = None
        self._default_status = None
        self._ips_cve = None
        self._ips_group = None
        self._ips_id = None
        self._ips_level = None
        self._ips_name = None
        self._ips_rules_type = None
        self._ips_status = None
        self.discriminator = None

        if affected_application is not None:
            self.affected_application = affected_application
        if create_time is not None:
            self.create_time = create_time
        if default_status is not None:
            self.default_status = default_status
        if ips_cve is not None:
            self.ips_cve = ips_cve
        if ips_group is not None:
            self.ips_group = ips_group
        if ips_id is not None:
            self.ips_id = ips_id
        if ips_level is not None:
            self.ips_level = ips_level
        if ips_name is not None:
            self.ips_name = ips_name
        if ips_rules_type is not None:
            self.ips_rules_type = ips_rules_type
        if ips_status is not None:
            self.ips_status = ips_status

    @property
    def affected_application(self):
        r"""Gets the affected_application of this IpsRuleVO.

        :return: The affected_application of this IpsRuleVO.
        :rtype: str
        """
        return self._affected_application

    @affected_application.setter
    def affected_application(self, affected_application):
        r"""Sets the affected_application of this IpsRuleVO.

        :param affected_application: The affected_application of this IpsRuleVO.
        :type affected_application: str
        """
        self._affected_application = affected_application

    @property
    def create_time(self):
        r"""Gets the create_time of this IpsRuleVO.

        :return: The create_time of this IpsRuleVO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this IpsRuleVO.

        :param create_time: The create_time of this IpsRuleVO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def default_status(self):
        r"""Gets the default_status of this IpsRuleVO.

        :return: The default_status of this IpsRuleVO.
        :rtype: str
        """
        return self._default_status

    @default_status.setter
    def default_status(self, default_status):
        r"""Sets the default_status of this IpsRuleVO.

        :param default_status: The default_status of this IpsRuleVO.
        :type default_status: str
        """
        self._default_status = default_status

    @property
    def ips_cve(self):
        r"""Gets the ips_cve of this IpsRuleVO.

        :return: The ips_cve of this IpsRuleVO.
        :rtype: str
        """
        return self._ips_cve

    @ips_cve.setter
    def ips_cve(self, ips_cve):
        r"""Sets the ips_cve of this IpsRuleVO.

        :param ips_cve: The ips_cve of this IpsRuleVO.
        :type ips_cve: str
        """
        self._ips_cve = ips_cve

    @property
    def ips_group(self):
        r"""Gets the ips_group of this IpsRuleVO.

        :return: The ips_group of this IpsRuleVO.
        :rtype: str
        """
        return self._ips_group

    @ips_group.setter
    def ips_group(self, ips_group):
        r"""Sets the ips_group of this IpsRuleVO.

        :param ips_group: The ips_group of this IpsRuleVO.
        :type ips_group: str
        """
        self._ips_group = ips_group

    @property
    def ips_id(self):
        r"""Gets the ips_id of this IpsRuleVO.

        :return: The ips_id of this IpsRuleVO.
        :rtype: str
        """
        return self._ips_id

    @ips_id.setter
    def ips_id(self, ips_id):
        r"""Sets the ips_id of this IpsRuleVO.

        :param ips_id: The ips_id of this IpsRuleVO.
        :type ips_id: str
        """
        self._ips_id = ips_id

    @property
    def ips_level(self):
        r"""Gets the ips_level of this IpsRuleVO.

        :return: The ips_level of this IpsRuleVO.
        :rtype: str
        """
        return self._ips_level

    @ips_level.setter
    def ips_level(self, ips_level):
        r"""Sets the ips_level of this IpsRuleVO.

        :param ips_level: The ips_level of this IpsRuleVO.
        :type ips_level: str
        """
        self._ips_level = ips_level

    @property
    def ips_name(self):
        r"""Gets the ips_name of this IpsRuleVO.

        :return: The ips_name of this IpsRuleVO.
        :rtype: str
        """
        return self._ips_name

    @ips_name.setter
    def ips_name(self, ips_name):
        r"""Sets the ips_name of this IpsRuleVO.

        :param ips_name: The ips_name of this IpsRuleVO.
        :type ips_name: str
        """
        self._ips_name = ips_name

    @property
    def ips_rules_type(self):
        r"""Gets the ips_rules_type of this IpsRuleVO.

        :return: The ips_rules_type of this IpsRuleVO.
        :rtype: str
        """
        return self._ips_rules_type

    @ips_rules_type.setter
    def ips_rules_type(self, ips_rules_type):
        r"""Sets the ips_rules_type of this IpsRuleVO.

        :param ips_rules_type: The ips_rules_type of this IpsRuleVO.
        :type ips_rules_type: str
        """
        self._ips_rules_type = ips_rules_type

    @property
    def ips_status(self):
        r"""Gets the ips_status of this IpsRuleVO.

        :return: The ips_status of this IpsRuleVO.
        :rtype: str
        """
        return self._ips_status

    @ips_status.setter
    def ips_status(self, ips_status):
        r"""Sets the ips_status of this IpsRuleVO.

        :param ips_status: The ips_status of this IpsRuleVO.
        :type ips_status: str
        """
        self._ips_status = ips_status

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
        if not isinstance(other, IpsRuleVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
