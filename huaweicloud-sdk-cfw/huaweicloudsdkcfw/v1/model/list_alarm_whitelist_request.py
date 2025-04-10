# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmWhitelistRequest:

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
        'ip_address': 'str',
        'limit': 'int',
        'offset': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'ip_address': 'ip_address',
        'limit': 'limit',
        'offset': 'offset',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, fw_instance_id=None, ip_address=None, limit=None, offset=None, enterprise_project_id=None):
        r"""ListAlarmWhitelistRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param ip_address: IP地址
        :type ip_address: str
        :param limit: 分页查询数据量限制
        :type limit: int
        :param offset: 查询偏移量
        :type offset: int
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        """
        
        

        self._fw_instance_id = None
        self._ip_address = None
        self._limit = None
        self._offset = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        if ip_address is not None:
            self.ip_address = ip_address
        self.limit = limit
        self.offset = offset
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListAlarmWhitelistRequest.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ListAlarmWhitelistRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListAlarmWhitelistRequest.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ListAlarmWhitelistRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ListAlarmWhitelistRequest.

        IP地址

        :return: The ip_address of this ListAlarmWhitelistRequest.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ListAlarmWhitelistRequest.

        IP地址

        :param ip_address: The ip_address of this ListAlarmWhitelistRequest.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmWhitelistRequest.

        分页查询数据量限制

        :return: The limit of this ListAlarmWhitelistRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmWhitelistRequest.

        分页查询数据量限制

        :param limit: The limit of this ListAlarmWhitelistRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAlarmWhitelistRequest.

        查询偏移量

        :return: The offset of this ListAlarmWhitelistRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlarmWhitelistRequest.

        查询偏移量

        :param offset: The offset of this ListAlarmWhitelistRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAlarmWhitelistRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ListAlarmWhitelistRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAlarmWhitelistRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ListAlarmWhitelistRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListAlarmWhitelistRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
