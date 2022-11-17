# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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

    def __init__(self, account_name=None, associated_on_begin=None, associated_on_end=None, offset=None, limit=None, indirect_partner_id=None):
        """QueryIndirectPartnersReq

        The model defined in huaweicloud sdk

        :param account_name: 云经销商伙伴的账号名。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type account_name: str
        :param associated_on_begin: 云经销商关联华为云总经销商的开始时间。 UTC时间（包括时区），比如2016-03-28T00:00:00Z。 此参数不携带或携带值为null时，不作为筛选条件。
        :type associated_on_begin: str
        :param associated_on_end: 云经销商关联华为云总经销商的结束时间。 UTC时间（包括时区），比如2016-03-28T00:00:00Z。 此参数不携带或携带值为null时，不作为筛选条件。
        :type associated_on_end: str
        :param offset: 偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的数量限制。默认值为10。
        :type limit: int
        :param indirect_partner_id: 云经销商ID。获取方法请参见[查询精英服务商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。 如果需要查询具体某个云经销商伙伴，必须携带该字段。除此之外，此参数不做处理。
        :type indirect_partner_id: str
        """
        
        

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

        云经销商伙伴的账号名。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The account_name of this QueryIndirectPartnersReq.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this QueryIndirectPartnersReq.

        云经销商伙伴的账号名。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param account_name: The account_name of this QueryIndirectPartnersReq.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def associated_on_begin(self):
        """Gets the associated_on_begin of this QueryIndirectPartnersReq.

        云经销商关联华为云总经销商的开始时间。 UTC时间（包括时区），比如2016-03-28T00:00:00Z。 此参数不携带或携带值为null时，不作为筛选条件。

        :return: The associated_on_begin of this QueryIndirectPartnersReq.
        :rtype: str
        """
        return self._associated_on_begin

    @associated_on_begin.setter
    def associated_on_begin(self, associated_on_begin):
        """Sets the associated_on_begin of this QueryIndirectPartnersReq.

        云经销商关联华为云总经销商的开始时间。 UTC时间（包括时区），比如2016-03-28T00:00:00Z。 此参数不携带或携带值为null时，不作为筛选条件。

        :param associated_on_begin: The associated_on_begin of this QueryIndirectPartnersReq.
        :type associated_on_begin: str
        """
        self._associated_on_begin = associated_on_begin

    @property
    def associated_on_end(self):
        """Gets the associated_on_end of this QueryIndirectPartnersReq.

        云经销商关联华为云总经销商的结束时间。 UTC时间（包括时区），比如2016-03-28T00:00:00Z。 此参数不携带或携带值为null时，不作为筛选条件。

        :return: The associated_on_end of this QueryIndirectPartnersReq.
        :rtype: str
        """
        return self._associated_on_end

    @associated_on_end.setter
    def associated_on_end(self, associated_on_end):
        """Sets the associated_on_end of this QueryIndirectPartnersReq.

        云经销商关联华为云总经销商的结束时间。 UTC时间（包括时区），比如2016-03-28T00:00:00Z。 此参数不携带或携带值为null时，不作为筛选条件。

        :param associated_on_end: The associated_on_end of this QueryIndirectPartnersReq.
        :type associated_on_end: str
        """
        self._associated_on_end = associated_on_end

    @property
    def offset(self):
        """Gets the offset of this QueryIndirectPartnersReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this QueryIndirectPartnersReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueryIndirectPartnersReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this QueryIndirectPartnersReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this QueryIndirectPartnersReq.

        每次查询的数量限制。默认值为10。

        :return: The limit of this QueryIndirectPartnersReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryIndirectPartnersReq.

        每次查询的数量限制。默认值为10。

        :param limit: The limit of this QueryIndirectPartnersReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this QueryIndirectPartnersReq.

        云经销商ID。获取方法请参见[查询精英服务商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。 如果需要查询具体某个云经销商伙伴，必须携带该字段。除此之外，此参数不做处理。

        :return: The indirect_partner_id of this QueryIndirectPartnersReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this QueryIndirectPartnersReq.

        云经销商ID。获取方法请参见[查询精英服务商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。 如果需要查询具体某个云经销商伙伴，必须携带该字段。除此之外，此参数不做处理。

        :param indirect_partner_id: The indirect_partner_id of this QueryIndirectPartnersReq.
        :type indirect_partner_id: str
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
        if not isinstance(other, QueryIndirectPartnersReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
