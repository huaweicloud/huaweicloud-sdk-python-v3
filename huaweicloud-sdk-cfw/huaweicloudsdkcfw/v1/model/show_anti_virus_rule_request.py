# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAntiVirusRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'engine_type': 'int',
        'limit': 'int',
        'offset': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'object_id': 'object_id',
        'engine_type': 'engine_type',
        'limit': 'limit',
        'offset': 'offset',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, object_id=None, engine_type=None, limit=None, offset=None, enterprise_project_id=None):
        r"""ShowAntiVirusRuleRequest

        The model defined in huaweicloud sdk

        :param object_id: 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。
        :type object_id: str
        :param engine_type: 防火墙类型
        :type engine_type: int
        :param limit: 每页显示的数据量
        :type limit: int
        :param offset: 查询偏移量
        :type offset: int
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        """
        
        

        self._object_id = None
        self._engine_type = None
        self._limit = None
        self._offset = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.object_id = object_id
        self.engine_type = engine_type
        self.limit = limit
        self.offset = offset
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def object_id(self):
        r"""Gets the object_id of this ShowAntiVirusRuleRequest.

        防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :return: The object_id of this ShowAntiVirusRuleRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ShowAntiVirusRuleRequest.

        防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :param object_id: The object_id of this ShowAntiVirusRuleRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowAntiVirusRuleRequest.

        防火墙类型

        :return: The engine_type of this ShowAntiVirusRuleRequest.
        :rtype: int
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowAntiVirusRuleRequest.

        防火墙类型

        :param engine_type: The engine_type of this ShowAntiVirusRuleRequest.
        :type engine_type: int
        """
        self._engine_type = engine_type

    @property
    def limit(self):
        r"""Gets the limit of this ShowAntiVirusRuleRequest.

        每页显示的数据量

        :return: The limit of this ShowAntiVirusRuleRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowAntiVirusRuleRequest.

        每页显示的数据量

        :param limit: The limit of this ShowAntiVirusRuleRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowAntiVirusRuleRequest.

        查询偏移量

        :return: The offset of this ShowAntiVirusRuleRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowAntiVirusRuleRequest.

        查询偏移量

        :param offset: The offset of this ShowAntiVirusRuleRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowAntiVirusRuleRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ShowAntiVirusRuleRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowAntiVirusRuleRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ShowAntiVirusRuleRequest.
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
        if not isinstance(other, ShowAntiVirusRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
