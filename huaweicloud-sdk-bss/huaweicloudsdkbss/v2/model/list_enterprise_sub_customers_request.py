# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnterpriseSubCustomersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sub_customer_account_name': 'str',
        'sub_customer_display_name': 'str',
        'fuzzy_query': 'int',
        'offset': 'int',
        'limit': 'int',
        'org_id': 'str'
    }

    attribute_map = {
        'sub_customer_account_name': 'sub_customer_account_name',
        'sub_customer_display_name': 'sub_customer_display_name',
        'fuzzy_query': 'fuzzy_query',
        'offset': 'offset',
        'limit': 'limit',
        'org_id': 'org_id'
    }

    def __init__(self, sub_customer_account_name=None, sub_customer_display_name=None, fuzzy_query=None, offset=None, limit=None, org_id=None):
        """ListEnterpriseSubCustomersRequest

        The model defined in huaweicloud sdk

        :param sub_customer_account_name: 企业子账号的账号名。根据fuzzy_query取值决定是否按模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。
        :type sub_customer_account_name: str
        :param sub_customer_display_name: 企业子账号的显示名称。根据fuzzy_query取值决定是否按模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。
        :type sub_customer_display_name: str
        :param fuzzy_query: 企业子账号的显示名称、用户名是否按模糊查询。默认值为“0：不按模糊查询”。0：不按模糊查询1：按模糊查询
        :type fuzzy_query: int
        :param offset: 偏移量，从0开始，默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询记录数，默认值为10。
        :type limit: int
        :param org_id: 子账号归属的组织单元ID。此参数不携带或携带值为空时，不作为筛选条件。
        :type org_id: str
        """
        
        

        self._sub_customer_account_name = None
        self._sub_customer_display_name = None
        self._fuzzy_query = None
        self._offset = None
        self._limit = None
        self._org_id = None
        self.discriminator = None

        if sub_customer_account_name is not None:
            self.sub_customer_account_name = sub_customer_account_name
        if sub_customer_display_name is not None:
            self.sub_customer_display_name = sub_customer_display_name
        if fuzzy_query is not None:
            self.fuzzy_query = fuzzy_query
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if org_id is not None:
            self.org_id = org_id

    @property
    def sub_customer_account_name(self):
        """Gets the sub_customer_account_name of this ListEnterpriseSubCustomersRequest.

        企业子账号的账号名。根据fuzzy_query取值决定是否按模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。

        :return: The sub_customer_account_name of this ListEnterpriseSubCustomersRequest.
        :rtype: str
        """
        return self._sub_customer_account_name

    @sub_customer_account_name.setter
    def sub_customer_account_name(self, sub_customer_account_name):
        """Sets the sub_customer_account_name of this ListEnterpriseSubCustomersRequest.

        企业子账号的账号名。根据fuzzy_query取值决定是否按模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。

        :param sub_customer_account_name: The sub_customer_account_name of this ListEnterpriseSubCustomersRequest.
        :type sub_customer_account_name: str
        """
        self._sub_customer_account_name = sub_customer_account_name

    @property
    def sub_customer_display_name(self):
        """Gets the sub_customer_display_name of this ListEnterpriseSubCustomersRequest.

        企业子账号的显示名称。根据fuzzy_query取值决定是否按模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。

        :return: The sub_customer_display_name of this ListEnterpriseSubCustomersRequest.
        :rtype: str
        """
        return self._sub_customer_display_name

    @sub_customer_display_name.setter
    def sub_customer_display_name(self, sub_customer_display_name):
        """Sets the sub_customer_display_name of this ListEnterpriseSubCustomersRequest.

        企业子账号的显示名称。根据fuzzy_query取值决定是否按模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。

        :param sub_customer_display_name: The sub_customer_display_name of this ListEnterpriseSubCustomersRequest.
        :type sub_customer_display_name: str
        """
        self._sub_customer_display_name = sub_customer_display_name

    @property
    def fuzzy_query(self):
        """Gets the fuzzy_query of this ListEnterpriseSubCustomersRequest.

        企业子账号的显示名称、用户名是否按模糊查询。默认值为“0：不按模糊查询”。0：不按模糊查询1：按模糊查询

        :return: The fuzzy_query of this ListEnterpriseSubCustomersRequest.
        :rtype: int
        """
        return self._fuzzy_query

    @fuzzy_query.setter
    def fuzzy_query(self, fuzzy_query):
        """Sets the fuzzy_query of this ListEnterpriseSubCustomersRequest.

        企业子账号的显示名称、用户名是否按模糊查询。默认值为“0：不按模糊查询”。0：不按模糊查询1：按模糊查询

        :param fuzzy_query: The fuzzy_query of this ListEnterpriseSubCustomersRequest.
        :type fuzzy_query: int
        """
        self._fuzzy_query = fuzzy_query

    @property
    def offset(self):
        """Gets the offset of this ListEnterpriseSubCustomersRequest.

        偏移量，从0开始，默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListEnterpriseSubCustomersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEnterpriseSubCustomersRequest.

        偏移量，从0开始，默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListEnterpriseSubCustomersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEnterpriseSubCustomersRequest.

        每次查询记录数，默认值为10。

        :return: The limit of this ListEnterpriseSubCustomersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEnterpriseSubCustomersRequest.

        每次查询记录数，默认值为10。

        :param limit: The limit of this ListEnterpriseSubCustomersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def org_id(self):
        """Gets the org_id of this ListEnterpriseSubCustomersRequest.

        子账号归属的组织单元ID。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The org_id of this ListEnterpriseSubCustomersRequest.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this ListEnterpriseSubCustomersRequest.

        子账号归属的组织单元ID。此参数不携带或携带值为空时，不作为筛选条件。

        :param org_id: The org_id of this ListEnterpriseSubCustomersRequest.
        :type org_id: str
        """
        self._org_id = org_id

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
        if not isinstance(other, ListEnterpriseSubCustomersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
