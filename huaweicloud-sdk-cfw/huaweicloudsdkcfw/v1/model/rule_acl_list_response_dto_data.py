# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleAclListResponseDTOData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'total': 'int',
        'object_id': 'str',
        'records': 'list[RuleAclListResponseDTODataRecords]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total',
        'object_id': 'object_id',
        'records': 'records'
    }

    def __init__(self, offset=None, limit=None, total=None, object_id=None, records=None):
        """RuleAclListResponseDTOData

        The model defined in huaweicloud sdk

        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param total: 查询总条数
        :type total: int
        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。
        :type object_id: str
        :param records: records
        :type records: list[:class:`huaweicloudsdkcfw.v1.RuleAclListResponseDTODataRecords`]
        """
        
        

        self._offset = None
        self._limit = None
        self._total = None
        self._object_id = None
        self._records = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if object_id is not None:
            self.object_id = object_id
        if records is not None:
            self.records = records

    @property
    def offset(self):
        """Gets the offset of this RuleAclListResponseDTOData.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this RuleAclListResponseDTOData.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this RuleAclListResponseDTOData.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this RuleAclListResponseDTOData.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this RuleAclListResponseDTOData.

        每页显示个数

        :return: The limit of this RuleAclListResponseDTOData.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this RuleAclListResponseDTOData.

        每页显示个数

        :param limit: The limit of this RuleAclListResponseDTOData.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        """Gets the total of this RuleAclListResponseDTOData.

        查询总条数

        :return: The total of this RuleAclListResponseDTOData.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this RuleAclListResponseDTOData.

        查询总条数

        :param total: The total of this RuleAclListResponseDTOData.
        :type total: int
        """
        self._total = total

    @property
    def object_id(self):
        """Gets the object_id of this RuleAclListResponseDTOData.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :return: The object_id of this RuleAclListResponseDTOData.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this RuleAclListResponseDTOData.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :param object_id: The object_id of this RuleAclListResponseDTOData.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def records(self):
        """Gets the records of this RuleAclListResponseDTOData.

        records

        :return: The records of this RuleAclListResponseDTOData.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.RuleAclListResponseDTODataRecords`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this RuleAclListResponseDTOData.

        records

        :param records: The records of this RuleAclListResponseDTOData.
        :type records: list[:class:`huaweicloudsdkcfw.v1.RuleAclListResponseDTODataRecords`]
        """
        self._records = records

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
        if not isinstance(other, RuleAclListResponseDTOData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
