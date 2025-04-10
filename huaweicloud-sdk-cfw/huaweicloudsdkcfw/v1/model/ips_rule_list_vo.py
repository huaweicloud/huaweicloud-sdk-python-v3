# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsRuleListVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'limit': 'int',
        'object_id': 'str',
        'offset': 'int',
        'records': 'list[IpsRuleVO]',
        'total': 'int'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'limit': 'limit',
        'object_id': 'object_id',
        'offset': 'offset',
        'records': 'records',
        'total': 'total'
    }

    def __init__(self, fw_instance_id=None, limit=None, object_id=None, offset=None, records=None, total=None):
        r"""IpsRuleListVO

        The model defined in huaweicloud sdk

        :param fw_instance_id: 
        :type fw_instance_id: str
        :param limit: 
        :type limit: int
        :param object_id: 
        :type object_id: str
        :param offset: 
        :type offset: int
        :param records: 
        :type records: list[:class:`huaweicloudsdkcfw.v1.IpsRuleVO`]
        :param total: 
        :type total: int
        """
        
        

        self._fw_instance_id = None
        self._limit = None
        self._object_id = None
        self._offset = None
        self._records = None
        self._total = None
        self.discriminator = None

        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id
        if limit is not None:
            self.limit = limit
        if object_id is not None:
            self.object_id = object_id
        if offset is not None:
            self.offset = offset
        if records is not None:
            self.records = records
        if total is not None:
            self.total = total

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this IpsRuleListVO.

        :return: The fw_instance_id of this IpsRuleListVO.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this IpsRuleListVO.

        :param fw_instance_id: The fw_instance_id of this IpsRuleListVO.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def limit(self):
        r"""Gets the limit of this IpsRuleListVO.

        :return: The limit of this IpsRuleListVO.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this IpsRuleListVO.

        :param limit: The limit of this IpsRuleListVO.
        :type limit: int
        """
        self._limit = limit

    @property
    def object_id(self):
        r"""Gets the object_id of this IpsRuleListVO.

        :return: The object_id of this IpsRuleListVO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this IpsRuleListVO.

        :param object_id: The object_id of this IpsRuleListVO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def offset(self):
        r"""Gets the offset of this IpsRuleListVO.

        :return: The offset of this IpsRuleListVO.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this IpsRuleListVO.

        :param offset: The offset of this IpsRuleListVO.
        :type offset: int
        """
        self._offset = offset

    @property
    def records(self):
        r"""Gets the records of this IpsRuleListVO.

        :return: The records of this IpsRuleListVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.IpsRuleVO`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this IpsRuleListVO.

        :param records: The records of this IpsRuleListVO.
        :type records: list[:class:`huaweicloudsdkcfw.v1.IpsRuleVO`]
        """
        self._records = records

    @property
    def total(self):
        r"""Gets the total of this IpsRuleListVO.

        :return: The total of this IpsRuleListVO.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this IpsRuleListVO.

        :param total: The total of this IpsRuleListVO.
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
        if not isinstance(other, IpsRuleListVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
