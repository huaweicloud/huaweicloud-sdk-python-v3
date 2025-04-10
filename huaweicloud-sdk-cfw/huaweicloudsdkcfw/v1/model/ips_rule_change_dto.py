# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsRuleChangeDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ips_ids': 'list[str]',
        'object_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'ips_ids': 'ips_ids',
        'object_id': 'object_id',
        'status': 'status'
    }

    def __init__(self, ips_ids=None, object_id=None, status=None):
        r"""IpsRuleChangeDto

        The model defined in huaweicloud sdk

        :param ips_ids: ips的id列表
        :type ips_ids: list[str]
        :param object_id: 防护对象id
        :type object_id: str
        :param status: ips规则状态
        :type status: str
        """
        
        

        self._ips_ids = None
        self._object_id = None
        self._status = None
        self.discriminator = None

        if ips_ids is not None:
            self.ips_ids = ips_ids
        if object_id is not None:
            self.object_id = object_id
        if status is not None:
            self.status = status

    @property
    def ips_ids(self):
        r"""Gets the ips_ids of this IpsRuleChangeDto.

        ips的id列表

        :return: The ips_ids of this IpsRuleChangeDto.
        :rtype: list[str]
        """
        return self._ips_ids

    @ips_ids.setter
    def ips_ids(self, ips_ids):
        r"""Sets the ips_ids of this IpsRuleChangeDto.

        ips的id列表

        :param ips_ids: The ips_ids of this IpsRuleChangeDto.
        :type ips_ids: list[str]
        """
        self._ips_ids = ips_ids

    @property
    def object_id(self):
        r"""Gets the object_id of this IpsRuleChangeDto.

        防护对象id

        :return: The object_id of this IpsRuleChangeDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this IpsRuleChangeDto.

        防护对象id

        :param object_id: The object_id of this IpsRuleChangeDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def status(self):
        r"""Gets the status of this IpsRuleChangeDto.

        ips规则状态

        :return: The status of this IpsRuleChangeDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IpsRuleChangeDto.

        ips规则状态

        :param status: The status of this IpsRuleChangeDto.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, IpsRuleChangeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
