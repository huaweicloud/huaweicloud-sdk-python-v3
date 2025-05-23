# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnfreezeSubCustomersReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_ids': 'list[str]',
        'reason': 'str',
        'indirect_partner_id': 'str',
        'unfreeze_type': 'str'
    }

    attribute_map = {
        'customer_ids': 'customer_ids',
        'reason': 'reason',
        'indirect_partner_id': 'indirect_partner_id',
        'unfreeze_type': 'unfreeze_type'
    }

    def __init__(self, customer_ids=None, reason=None, indirect_partner_id=None, unfreeze_type=None):
        r"""UnfreezeSubCustomersReq

        The model defined in huaweicloud sdk

        :param customer_ids: 需要解冻的客户账号ID列表。 您可以调用查询客户列表接口获取customer_id。
        :type customer_ids: list[str]
        :param reason: 解冻原因。
        :type reason: str
        :param indirect_partner_id: 云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。
        :type indirect_partner_id: str
        :param unfreeze_type: |参数名称：解冻类型| |参数的约束及描述：该参数非必填，解冻类型，支持枚举| |ACCOUNT：解冻账号，ACCOUNT_AND_RESOURCE：解冻账号与资源|
        :type unfreeze_type: str
        """
        
        

        self._customer_ids = None
        self._reason = None
        self._indirect_partner_id = None
        self._unfreeze_type = None
        self.discriminator = None

        self.customer_ids = customer_ids
        self.reason = reason
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if unfreeze_type is not None:
            self.unfreeze_type = unfreeze_type

    @property
    def customer_ids(self):
        r"""Gets the customer_ids of this UnfreezeSubCustomersReq.

        需要解冻的客户账号ID列表。 您可以调用查询客户列表接口获取customer_id。

        :return: The customer_ids of this UnfreezeSubCustomersReq.
        :rtype: list[str]
        """
        return self._customer_ids

    @customer_ids.setter
    def customer_ids(self, customer_ids):
        r"""Sets the customer_ids of this UnfreezeSubCustomersReq.

        需要解冻的客户账号ID列表。 您可以调用查询客户列表接口获取customer_id。

        :param customer_ids: The customer_ids of this UnfreezeSubCustomersReq.
        :type customer_ids: list[str]
        """
        self._customer_ids = customer_ids

    @property
    def reason(self):
        r"""Gets the reason of this UnfreezeSubCustomersReq.

        解冻原因。

        :return: The reason of this UnfreezeSubCustomersReq.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this UnfreezeSubCustomersReq.

        解冻原因。

        :param reason: The reason of this UnfreezeSubCustomersReq.
        :type reason: str
        """
        self._reason = reason

    @property
    def indirect_partner_id(self):
        r"""Gets the indirect_partner_id of this UnfreezeSubCustomersReq.

        云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。

        :return: The indirect_partner_id of this UnfreezeSubCustomersReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        r"""Sets the indirect_partner_id of this UnfreezeSubCustomersReq.

        云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。

        :param indirect_partner_id: The indirect_partner_id of this UnfreezeSubCustomersReq.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def unfreeze_type(self):
        r"""Gets the unfreeze_type of this UnfreezeSubCustomersReq.

        |参数名称：解冻类型| |参数的约束及描述：该参数非必填，解冻类型，支持枚举| |ACCOUNT：解冻账号，ACCOUNT_AND_RESOURCE：解冻账号与资源|

        :return: The unfreeze_type of this UnfreezeSubCustomersReq.
        :rtype: str
        """
        return self._unfreeze_type

    @unfreeze_type.setter
    def unfreeze_type(self, unfreeze_type):
        r"""Sets the unfreeze_type of this UnfreezeSubCustomersReq.

        |参数名称：解冻类型| |参数的约束及描述：该参数非必填，解冻类型，支持枚举| |ACCOUNT：解冻账号，ACCOUNT_AND_RESOURCE：解冻账号与资源|

        :param unfreeze_type: The unfreeze_type of this UnfreezeSubCustomersReq.
        :type unfreeze_type: str
        """
        self._unfreeze_type = unfreeze_type

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
        if not isinstance(other, UnfreezeSubCustomersReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
