# coding: utf-8

import pprint
import re

import six





class QueryIndirectPartnersReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'account_name': 'str',
        'associated_on_begin': 'str',
        'associated_on_end': 'str',
        'offset': 'int',
        'limit': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'account_name': 'account_name',
        'associated_on_begin': 'associated_on_begin',
        'associated_on_end': 'associated_on_end',
        'offset': 'offset',
        'limit': 'limit',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, account_name=None, associated_on_begin=None, associated_on_end=None, offset=0, limit=10, indirect_partner_id=None):
        """QueryIndirectPartnersReq - a model defined in huaweicloud sdk"""
        
        

        self._account_name = None
        self._associated_on_begin = None
        self._associated_on_end = None
        self._offset = None
        self._limit = None
        self._indirect_partner_id = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if associated_on_begin is not None:
            self.associated_on_begin = associated_on_begin
        if associated_on_end is not None:
            self.associated_on_end = associated_on_end
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def account_name(self):
        """Gets the account_name of this QueryIndirectPartnersReq.

        |参数名称：登录名称| |参数约束及描述：登录名称|

        :return: The account_name of this QueryIndirectPartnersReq.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this QueryIndirectPartnersReq.

        |参数名称：登录名称| |参数约束及描述：登录名称|

        :param account_name: The account_name of this QueryIndirectPartnersReq.
        :type: str
        """
        self._account_name = account_name

    @property
    def associated_on_begin(self):
        """Gets the associated_on_begin of this QueryIndirectPartnersReq.

        |参数名称：关联开始时间，UTC时间（包括时区），比如2016-03-28T00:00:00Z| |参数约束及描述：关联开始时间，UTC时间（包括时区），比如2016-03-28T00:00:00Z|

        :return: The associated_on_begin of this QueryIndirectPartnersReq.
        :rtype: str
        """
        return self._associated_on_begin

    @associated_on_begin.setter
    def associated_on_begin(self, associated_on_begin):
        """Sets the associated_on_begin of this QueryIndirectPartnersReq.

        |参数名称：关联开始时间，UTC时间（包括时区），比如2016-03-28T00:00:00Z| |参数约束及描述：关联开始时间，UTC时间（包括时区），比如2016-03-28T00:00:00Z|

        :param associated_on_begin: The associated_on_begin of this QueryIndirectPartnersReq.
        :type: str
        """
        self._associated_on_begin = associated_on_begin

    @property
    def associated_on_end(self):
        """Gets the associated_on_end of this QueryIndirectPartnersReq.

        |参数名称：关联结束时间，UTC时间（包括时区），比如2016-03-28T00:00:00Z| |参数约束及描述：关联结束时间，UTC时间（包括时区），比如2016-03-28T00:00:00Z|

        :return: The associated_on_end of this QueryIndirectPartnersReq.
        :rtype: str
        """
        return self._associated_on_end

    @associated_on_end.setter
    def associated_on_end(self, associated_on_end):
        """Sets the associated_on_end of this QueryIndirectPartnersReq.

        |参数名称：关联结束时间，UTC时间（包括时区），比如2016-03-28T00:00:00Z| |参数约束及描述：关联结束时间，UTC时间（包括时区），比如2016-03-28T00:00:00Z|

        :param associated_on_end: The associated_on_end of this QueryIndirectPartnersReq.
        :type: str
        """
        self._associated_on_end = associated_on_end

    @property
    def offset(self):
        """Gets the offset of this QueryIndirectPartnersReq.

        |参数名称：偏移量，从0开始，默认是0| |参数的约束及描述：偏移量，从0开始，默认是0|

        :return: The offset of this QueryIndirectPartnersReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueryIndirectPartnersReq.

        |参数名称：偏移量，从0开始，默认是0| |参数的约束及描述：偏移量，从0开始，默认是0|

        :param offset: The offset of this QueryIndirectPartnersReq.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this QueryIndirectPartnersReq.

        |参数名称：最大100，默认为10| |参数的约束及描述：最大100，默认为10|

        :return: The limit of this QueryIndirectPartnersReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryIndirectPartnersReq.

        |参数名称：最大100，默认为10| |参数的约束及描述：最大100，默认为10|

        :param limit: The limit of this QueryIndirectPartnersReq.
        :type: int
        """
        self._limit = limit

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this QueryIndirectPartnersReq.

        |参数名称：二级经销商ID| |参数约束及描述：二级经销商ID|

        :return: The indirect_partner_id of this QueryIndirectPartnersReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this QueryIndirectPartnersReq.

        |参数名称：二级经销商ID| |参数约束及描述：二级经销商ID|

        :param indirect_partner_id: The indirect_partner_id of this QueryIndirectPartnersReq.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryIndirectPartnersReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
