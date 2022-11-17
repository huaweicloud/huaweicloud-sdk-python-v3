# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaRecord:

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
        'operator': 'str',
        'operation_type': 'str',
        'quota_id': 'str',
        'parent_quota_id': 'str',
        'amount': 'float',
        'operation_time': 'str',
        'result': 'str',
        'indirect_partner_account_name': 'str',
        'indirect_partner_id': 'str',
        'indirect_partner_name': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'operator': 'operator',
        'operation_type': 'operation_type',
        'quota_id': 'quota_id',
        'parent_quota_id': 'parent_quota_id',
        'amount': 'amount',
        'operation_time': 'operation_time',
        'result': 'result',
        'indirect_partner_account_name': 'indirect_partner_account_name',
        'indirect_partner_id': 'indirect_partner_id',
        'indirect_partner_name': 'indirect_partner_name',
        'remark': 'remark'
    }

    def __init__(self, id=None, operator=None, operation_type=None, quota_id=None, parent_quota_id=None, amount=None, operation_time=None, result=None, indirect_partner_account_name=None, indirect_partner_id=None, indirect_partner_name=None, remark=None):
        """QuotaRecord

        The model defined in huaweicloud sdk

        :param id: 记录ID。
        :type id: str
        :param operator: 操作员的账号名称。
        :type operator: str
        :param operation_type: 操作类型。 10：发放额度11：回收额度
        :type operation_type: str
        :param quota_id: 云经销商的代金券额度ID。 即华为云总经销商给云经销商发放代金券额度时，产生的云经销商的代金券额度ID，或者从云经销商回收代金券额度时，云经销商的代金券额度ID。
        :type quota_id: str
        :param parent_quota_id: 父额度ID。 这即华为云总经销商给云经销商发放代金券额度时，华为云总经销商的额度ID，或者从云经销商回收代金券额度时，回收的华为云总经销商的额度ID。
        :type parent_quota_id: str
        :param amount: 发放回收的金额。 取值大于0且精确到小数点后2位，单位：元。
        :type amount: float
        :param operation_time: 操作时间，UTC时间，UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。
        :type operation_time: str
        :param result: 操作结果。 0：成功-1：失败
        :type result: str
        :param indirect_partner_account_name: 云经销商的账号名。
        :type indirect_partner_account_name: str
        :param indirect_partner_id: 云经销商ID。
        :type indirect_partner_id: str
        :param indirect_partner_name: 云经销商的公司名称。
        :type indirect_partner_name: str
        :param remark: 备注。
        :type remark: str
        """
        
        

        self._id = None
        self._operator = None
        self._operation_type = None
        self._quota_id = None
        self._parent_quota_id = None
        self._amount = None
        self._operation_time = None
        self._result = None
        self._indirect_partner_account_name = None
        self._indirect_partner_id = None
        self._indirect_partner_name = None
        self._remark = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if operator is not None:
            self.operator = operator
        if operation_type is not None:
            self.operation_type = operation_type
        if quota_id is not None:
            self.quota_id = quota_id
        if parent_quota_id is not None:
            self.parent_quota_id = parent_quota_id
        if amount is not None:
            self.amount = amount
        if operation_time is not None:
            self.operation_time = operation_time
        if result is not None:
            self.result = result
        if indirect_partner_account_name is not None:
            self.indirect_partner_account_name = indirect_partner_account_name
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if indirect_partner_name is not None:
            self.indirect_partner_name = indirect_partner_name
        if remark is not None:
            self.remark = remark

    @property
    def id(self):
        """Gets the id of this QuotaRecord.

        记录ID。

        :return: The id of this QuotaRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuotaRecord.

        记录ID。

        :param id: The id of this QuotaRecord.
        :type id: str
        """
        self._id = id

    @property
    def operator(self):
        """Gets the operator of this QuotaRecord.

        操作员的账号名称。

        :return: The operator of this QuotaRecord.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this QuotaRecord.

        操作员的账号名称。

        :param operator: The operator of this QuotaRecord.
        :type operator: str
        """
        self._operator = operator

    @property
    def operation_type(self):
        """Gets the operation_type of this QuotaRecord.

        操作类型。 10：发放额度11：回收额度

        :return: The operation_type of this QuotaRecord.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this QuotaRecord.

        操作类型。 10：发放额度11：回收额度

        :param operation_type: The operation_type of this QuotaRecord.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def quota_id(self):
        """Gets the quota_id of this QuotaRecord.

        云经销商的代金券额度ID。 即华为云总经销商给云经销商发放代金券额度时，产生的云经销商的代金券额度ID，或者从云经销商回收代金券额度时，云经销商的代金券额度ID。

        :return: The quota_id of this QuotaRecord.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this QuotaRecord.

        云经销商的代金券额度ID。 即华为云总经销商给云经销商发放代金券额度时，产生的云经销商的代金券额度ID，或者从云经销商回收代金券额度时，云经销商的代金券额度ID。

        :param quota_id: The quota_id of this QuotaRecord.
        :type quota_id: str
        """
        self._quota_id = quota_id

    @property
    def parent_quota_id(self):
        """Gets the parent_quota_id of this QuotaRecord.

        父额度ID。 这即华为云总经销商给云经销商发放代金券额度时，华为云总经销商的额度ID，或者从云经销商回收代金券额度时，回收的华为云总经销商的额度ID。

        :return: The parent_quota_id of this QuotaRecord.
        :rtype: str
        """
        return self._parent_quota_id

    @parent_quota_id.setter
    def parent_quota_id(self, parent_quota_id):
        """Sets the parent_quota_id of this QuotaRecord.

        父额度ID。 这即华为云总经销商给云经销商发放代金券额度时，华为云总经销商的额度ID，或者从云经销商回收代金券额度时，回收的华为云总经销商的额度ID。

        :param parent_quota_id: The parent_quota_id of this QuotaRecord.
        :type parent_quota_id: str
        """
        self._parent_quota_id = parent_quota_id

    @property
    def amount(self):
        """Gets the amount of this QuotaRecord.

        发放回收的金额。 取值大于0且精确到小数点后2位，单位：元。

        :return: The amount of this QuotaRecord.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this QuotaRecord.

        发放回收的金额。 取值大于0且精确到小数点后2位，单位：元。

        :param amount: The amount of this QuotaRecord.
        :type amount: float
        """
        self._amount = amount

    @property
    def operation_time(self):
        """Gets the operation_time of this QuotaRecord.

        操作时间，UTC时间，UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The operation_time of this QuotaRecord.
        :rtype: str
        """
        return self._operation_time

    @operation_time.setter
    def operation_time(self, operation_time):
        """Sets the operation_time of this QuotaRecord.

        操作时间，UTC时间，UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :param operation_time: The operation_time of this QuotaRecord.
        :type operation_time: str
        """
        self._operation_time = operation_time

    @property
    def result(self):
        """Gets the result of this QuotaRecord.

        操作结果。 0：成功-1：失败

        :return: The result of this QuotaRecord.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this QuotaRecord.

        操作结果。 0：成功-1：失败

        :param result: The result of this QuotaRecord.
        :type result: str
        """
        self._result = result

    @property
    def indirect_partner_account_name(self):
        """Gets the indirect_partner_account_name of this QuotaRecord.

        云经销商的账号名。

        :return: The indirect_partner_account_name of this QuotaRecord.
        :rtype: str
        """
        return self._indirect_partner_account_name

    @indirect_partner_account_name.setter
    def indirect_partner_account_name(self, indirect_partner_account_name):
        """Sets the indirect_partner_account_name of this QuotaRecord.

        云经销商的账号名。

        :param indirect_partner_account_name: The indirect_partner_account_name of this QuotaRecord.
        :type indirect_partner_account_name: str
        """
        self._indirect_partner_account_name = indirect_partner_account_name

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this QuotaRecord.

        云经销商ID。

        :return: The indirect_partner_id of this QuotaRecord.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this QuotaRecord.

        云经销商ID。

        :param indirect_partner_id: The indirect_partner_id of this QuotaRecord.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def indirect_partner_name(self):
        """Gets the indirect_partner_name of this QuotaRecord.

        云经销商的公司名称。

        :return: The indirect_partner_name of this QuotaRecord.
        :rtype: str
        """
        return self._indirect_partner_name

    @indirect_partner_name.setter
    def indirect_partner_name(self, indirect_partner_name):
        """Sets the indirect_partner_name of this QuotaRecord.

        云经销商的公司名称。

        :param indirect_partner_name: The indirect_partner_name of this QuotaRecord.
        :type indirect_partner_name: str
        """
        self._indirect_partner_name = indirect_partner_name

    @property
    def remark(self):
        """Gets the remark of this QuotaRecord.

        备注。

        :return: The remark of this QuotaRecord.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this QuotaRecord.

        备注。

        :param remark: The remark of this QuotaRecord.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, QuotaRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
