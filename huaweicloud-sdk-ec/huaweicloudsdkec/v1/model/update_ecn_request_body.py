# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEcnRequestBody:

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
        'description': 'str',
        'ecn_asn': 'int',
        'ieg_asn': 'int',
        'hub_enable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'ecn_asn': 'ecn_asn',
        'ieg_asn': 'ieg_asn',
        'hub_enable': 'hub_enable'
    }

    def __init__(self, name=None, description=None, ecn_asn=None, ieg_asn=None, hub_enable=None):
        """UpdateEcnRequestBody

        The model defined in huaweicloud sdk

        :param name: 企业连接网络名字
        :type name: str
        :param description: 描述信息
        :type description: str
        :param ecn_asn: 企业连接网络AS号
        :type ecn_asn: int
        :param ieg_asn: 智能企业网关AS号
        :type ieg_asn: int
        :param hub_enable: 分支互联开关
        :type hub_enable: bool
        """
        
        

        self._name = None
        self._description = None
        self._ecn_asn = None
        self._ieg_asn = None
        self._hub_enable = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ecn_asn is not None:
            self.ecn_asn = ecn_asn
        if ieg_asn is not None:
            self.ieg_asn = ieg_asn
        if hub_enable is not None:
            self.hub_enable = hub_enable

    @property
    def name(self):
        """Gets the name of this UpdateEcnRequestBody.

        企业连接网络名字

        :return: The name of this UpdateEcnRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateEcnRequestBody.

        企业连接网络名字

        :param name: The name of this UpdateEcnRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateEcnRequestBody.

        描述信息

        :return: The description of this UpdateEcnRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateEcnRequestBody.

        描述信息

        :param description: The description of this UpdateEcnRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def ecn_asn(self):
        """Gets the ecn_asn of this UpdateEcnRequestBody.

        企业连接网络AS号

        :return: The ecn_asn of this UpdateEcnRequestBody.
        :rtype: int
        """
        return self._ecn_asn

    @ecn_asn.setter
    def ecn_asn(self, ecn_asn):
        """Sets the ecn_asn of this UpdateEcnRequestBody.

        企业连接网络AS号

        :param ecn_asn: The ecn_asn of this UpdateEcnRequestBody.
        :type ecn_asn: int
        """
        self._ecn_asn = ecn_asn

    @property
    def ieg_asn(self):
        """Gets the ieg_asn of this UpdateEcnRequestBody.

        智能企业网关AS号

        :return: The ieg_asn of this UpdateEcnRequestBody.
        :rtype: int
        """
        return self._ieg_asn

    @ieg_asn.setter
    def ieg_asn(self, ieg_asn):
        """Sets the ieg_asn of this UpdateEcnRequestBody.

        智能企业网关AS号

        :param ieg_asn: The ieg_asn of this UpdateEcnRequestBody.
        :type ieg_asn: int
        """
        self._ieg_asn = ieg_asn

    @property
    def hub_enable(self):
        """Gets the hub_enable of this UpdateEcnRequestBody.

        分支互联开关

        :return: The hub_enable of this UpdateEcnRequestBody.
        :rtype: bool
        """
        return self._hub_enable

    @hub_enable.setter
    def hub_enable(self, hub_enable):
        """Sets the hub_enable of this UpdateEcnRequestBody.

        分支互联开关

        :param hub_enable: The hub_enable of this UpdateEcnRequestBody.
        :type hub_enable: bool
        """
        self._hub_enable = hub_enable

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
        if not isinstance(other, UpdateEcnRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
