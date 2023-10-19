# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'project_id': 'str',
        'records': 'list[DomainInfo]',
        'set_id': 'str',
        'total': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'project_id': 'project_id',
        'records': 'records',
        'set_id': 'set_id',
        'total': 'total'
    }

    def __init__(self, limit=None, offset=None, project_id=None, records=None, set_id=None, total=None):
        """ListDomainResponseData

        The model defined in huaweicloud sdk

        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param project_id: 租户项目id
        :type project_id: str
        :param records: 域名信息列表
        :type records: list[:class:`huaweicloudsdkcfw.v1.DomainInfo`]
        :param set_id: 域名组id
        :type set_id: str
        :param total: 总数
        :type total: int
        """
        
        

        self._limit = None
        self._offset = None
        self._project_id = None
        self._records = None
        self._set_id = None
        self._total = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if project_id is not None:
            self.project_id = project_id
        if records is not None:
            self.records = records
        if set_id is not None:
            self.set_id = set_id
        if total is not None:
            self.total = total

    @property
    def limit(self):
        """Gets the limit of this ListDomainResponseData.

        每页显示个数，范围为1-1024

        :return: The limit of this ListDomainResponseData.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDomainResponseData.

        每页显示个数，范围为1-1024

        :param limit: The limit of this ListDomainResponseData.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDomainResponseData.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListDomainResponseData.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDomainResponseData.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListDomainResponseData.
        :type offset: int
        """
        self._offset = offset

    @property
    def project_id(self):
        """Gets the project_id of this ListDomainResponseData.

        租户项目id

        :return: The project_id of this ListDomainResponseData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListDomainResponseData.

        租户项目id

        :param project_id: The project_id of this ListDomainResponseData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def records(self):
        """Gets the records of this ListDomainResponseData.

        域名信息列表

        :return: The records of this ListDomainResponseData.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.DomainInfo`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this ListDomainResponseData.

        域名信息列表

        :param records: The records of this ListDomainResponseData.
        :type records: list[:class:`huaweicloudsdkcfw.v1.DomainInfo`]
        """
        self._records = records

    @property
    def set_id(self):
        """Gets the set_id of this ListDomainResponseData.

        域名组id

        :return: The set_id of this ListDomainResponseData.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this ListDomainResponseData.

        域名组id

        :param set_id: The set_id of this ListDomainResponseData.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def total(self):
        """Gets the total of this ListDomainResponseData.

        总数

        :return: The total of this ListDomainResponseData.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListDomainResponseData.

        总数

        :param total: The total of this ListDomainResponseData.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListDomainResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
