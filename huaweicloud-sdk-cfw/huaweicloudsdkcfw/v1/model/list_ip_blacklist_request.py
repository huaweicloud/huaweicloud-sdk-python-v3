# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpBlacklistRequest:

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
        'offset': 'int'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, fw_instance_id=None, limit=None, offset=None):
        r"""ListIpBlacklistRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param limit: 在分页查询的情况下，每页查询的记录条数，范围为1-1024
        :type limit: int
        :param offset: 数据查询的偏移量，在分页查询的时候使用，指定查询记录的起始位置，必须为数字，取值范围为大于等于0
        :type offset: int
        """
        
        

        self._fw_instance_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        self.limit = limit
        self.offset = offset

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListIpBlacklistRequest.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ListIpBlacklistRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListIpBlacklistRequest.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ListIpBlacklistRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ListIpBlacklistRequest.

        在分页查询的情况下，每页查询的记录条数，范围为1-1024

        :return: The limit of this ListIpBlacklistRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIpBlacklistRequest.

        在分页查询的情况下，每页查询的记录条数，范围为1-1024

        :param limit: The limit of this ListIpBlacklistRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListIpBlacklistRequest.

        数据查询的偏移量，在分页查询的时候使用，指定查询记录的起始位置，必须为数字，取值范围为大于等于0

        :return: The offset of this ListIpBlacklistRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListIpBlacklistRequest.

        数据查询的偏移量，在分页查询的时候使用，指定查询记录的起始位置，必须为数字，取值范围为大于等于0

        :param offset: The offset of this ListIpBlacklistRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListIpBlacklistRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
